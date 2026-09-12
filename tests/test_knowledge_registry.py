import contextlib,hashlib,io,json,subprocess,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_pipeline as pipe
import knowledge_registry as registry

class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.src=self.root/'source';self.src.mkdir();self.stage=self.root/'stage'
        self.cfg={'sources':{'ai-knowledge':str(self.src)},'distribution':str(self.root/'installed')}
        pipe.write_json(self.stage/pipe.PLUGIN/'config/internal-user-ids.json',{'user_ids':[]})
        pipe.write_json(self.stage/pipe.PLUGIN/'provenance/sources.json',{'sources':[]})
    def file(self,name,body):
        path=self.src/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body,encoding='utf-8');return path
    def record(self,path,old='old.md',**overrides):
        row={'id':'ai-knowledge:'+old,'path':path,'original_path':old,'aliases':['ai-knowledge:'+old,'ai-knowledge:'+path],'reviewed_sha256':pipe.sha((self.src/path).read_bytes()),'business_status':'documented','review_status':'reviewed_static','reviewed_on':'2026-09-12','summary':'内容审阅结论','scope':'collart_web','disposition':'move'}
        row.update(overrides);pipe.write_json(self.src/'0global/knowledge_registry.json',{'documents':[row]});return row
    def test_move_preserves_identity_reference_and_noop(self):
        self.file('old.md','# Original evidence')
        pipe.build(self.cfg,self.stage)
        import shutil
        shutil.copytree(self.stage,self.cfg['distribution'])
        old=self.src/'old.md';new=self.src/'reports/new.md';new.parent.mkdir();old.replace(new)
        self.record('reports/new.md');self.file('report.md','# Report\n[Evidence](reports/new.md)')
        self.file('old.md','<!-- knowledge-redirect: ai-knowledge:old.md -->\n[Moved](reports/new.md)')
        result,rows=pipe.build(self.cfg,self.stage)
        catalog=json.loads((self.stage/pipe.PLUGIN/'library/catalog.json').read_text(encoding='utf-8'))['sources']
        matches=[r for r in catalog if r['id']=='ai-knowledge:old.md'];self.assertEqual(len(matches),1)
        self.assertEqual(matches[0]['path'],'reports/new.md');self.assertEqual(matches[0]['project'],'collart_web')
        self.assertFalse(any('@' in r['id'] for r in catalog))
        report=next(r for r in catalog if r['path']=='report.md')
        self.assertEqual(report['links'][0]['source_id'],'ai-knowledge:old.md')
        self.assertEqual(result,pipe.build(self.cfg,self.stage)[0])
        # Advance the distribution baseline as a successful installation would.
        # A redirect must not then make the moved source appear to be deleted.
        shutil.copytree(self.stage,self.cfg['distribution'],dirs_exist_ok=True)
        before={p.relative_to(self.stage).as_posix():p.read_bytes() for p in self.stage.rglob('*') if p.is_file()}
        self.assertEqual(result,pipe.build(self.cfg,self.stage)[0])
        self.assertEqual(before,{p.relative_to(self.stage).as_posix():p.read_bytes() for p in self.stage.rglob('*') if p.is_file()})
    def test_body_change_invalidates_review(self):
        p=self.file('new.md','# Original');self.record('new.md');p.write_text('# Changed')
        row=next(r for r in pipe.scan(self.cfg)[0] if r['path']=='new.md')
        self.assertEqual(row['review_status'],'needs_review');self.assertEqual(row['business_status'],'uncertain')
        self.assertNotEqual(row['summary'],'内容审阅结论')
    def test_old_hash_review_survives_pure_move(self):
        self.file('reports/data.json','[{"country":"US","revenue":20}]');r=self.record('reports/data.json',old='_generated/run/data.json',business_status='historical')
        self.cfg['reviews']={r['id']:{'sha256':r['reviewed_sha256'],'aggregate_or_schema':True}}
        row=next(r for r in pipe.scan(self.cfg)[0] if r['path']=='reports/data.json');self.assertEqual(row['status'],'historical')
    def test_ambiguous_alias_is_rejected(self):
        self.file('a.md','# a');self.file('b.md','# b');a=self.record('a.md');b={**a,'id':'ai-knowledge:b.md','path':'b.md'}
        pipe.write_json(self.src/'0global/knowledge_registry.json',{'documents':[a,b]})
        with self.assertRaises(ValueError):registry.load(self.src)
    def test_json_redaction_does_not_authorize_unknown_user_ids(self):
        uid='12345678-1234-1234-1234-123456789abc'
        p=self.file('_generated/run/result.json',json.dumps({'job_id':uid,'rows':[{'country':'US','count':2}]}))
        ident='ai-knowledge:_generated/run/result.json';self.cfg['reviews']={ident:{'sha256':pipe.sha(p.read_bytes()),'aggregate_or_schema':True,'redact_json_keys':['job_id']}}
        row=pipe.scan(self.cfg)[0][0];self.assertEqual(row['status'],'historical')
        p.write_text(json.dumps({'job_id':uid,'rows':[{'user_id':uid}]}));self.cfg['reviews'][ident]['sha256']=pipe.sha(p.read_bytes())
        row=pipe.scan(self.cfg)[0][0];self.assertEqual(row['status'],'pending')
    def test_redirect_is_never_a_second_source(self):
        self.file('new.md','# Body');self.record('new.md');self.file('old.md','<!-- knowledge-redirect: ai-knowledge:old.md -->\n[Body](new.md)')
        rows,texts=pipe.scan(self.cfg);self.assertEqual(len(texts),1)
        self.assertEqual(next(r for r in rows if r['path']=='old.md')['status'],'excluded')
    def test_editorial_change_affects_fingerprint(self):
        self.file('new.md','# Body');self.record('new.md');one=pipe.build(self.cfg,self.stage)[0]['source_fingerprint']
        self.record('new.md',business_status='deprecated');two=pipe.build(self.cfg,self.stage)[0]['source_fingerprint'];self.assertNotEqual(one,two)
    def test_all_three_source_moves_use_registered_id(self):
        for source in ['ai-knowledge','cursor_summary','codex_summary']:
            with self.subTest(source=source):
                self.file('moved/topic.md','# '+source)
                rec=self.record('moved/topic.md',id=source+':old.md',aliases=[source+':old.md',source+':moved/topic.md'])
                external=self.root/(source+'.json');pipe.write_json(external,{'documents':[rec]})
                cfg={**self.cfg,'sources':{source:str(self.src)},'source_registries':{source:str(external)}}
                rows,_=pipe.scan(cfg);row=next(r for r in rows if r['path']=='moved/topic.md');self.assertEqual(row['id'],source+':old.md')
                self.assertEqual(row['review_status'],'reviewed_static')
    def test_sql_labels_and_comments_are_not_write_statements(self):
        sql="-- CALL example(); MERGE historical_table\nSELECT 'Subscription update' AS label, 'CREATE -- quoted label' AS category"
        self.assertEqual(pipe.sql_operations(sql),['SELECT'])
        self.assertEqual(pipe.sql_operations("UPDATE `example.table` SET x='MERGE'"),['UPDATE'])
        self.assertEqual(pipe.sql_operations('DROP TABLE a; ALTER TABLE b ADD COLUMN c INT64; TRUNCATE TABLE d; EXECUTE IMMEDIATE query;'),['ALTER','DROP','EXECUTE','TRUNCATE'])

if __name__=='__main__':unittest.main()
