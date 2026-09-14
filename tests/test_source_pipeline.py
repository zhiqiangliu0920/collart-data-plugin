import hashlib,importlib.util,json,shutil,sys,tempfile,unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_pipeline as pipe
import release_state as release
from unittest.mock import patch

class SourceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.base=Path(self.tmp.name)
        self.cfg={'sources':{s:str(self.base/s) for s in ['ai-knowledge','cursor_summary','codex_summary']},'distribution':str(self.base/'installed-source')}
        for p in self.cfg['sources'].values():Path(p).mkdir()
        self.stage=self.base/'stage';self.plugin=self.stage/pipe.PLUGIN
        pipe.write_json(self.plugin/'config/internal-user-ids.json',{'user_ids':[]})
        pipe.write_json(self.plugin/'provenance/sources.json',{'sources':[]})
    def source(self,name,rel,text):
        p=Path(self.cfg['sources'][name])/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8');return p
    def test_all_three_inputs_add_modify_and_noop(self):
        previous=None
        for source in self.cfg['sources']:
            self.source(source,'topic.md','# '+source+'\nOriginal unique business evidence')
            result,_=pipe.build(self.cfg,self.stage)
            self.assertNotEqual(result['source_fingerprint'],previous);previous=result['source_fingerprint']
            self.source(source,'topic.md','# '+source+'\nModified business evidence')
            result,_=pipe.build(self.cfg,self.stage);self.assertNotEqual(result['source_fingerprint'],previous);previous=result['source_fingerprint']
        before={str(p):p.read_bytes() for p in self.plugin.rglob('*') if p.is_file()}
        again,rows=pipe.build(self.cfg,self.stage)
        self.assertEqual(again['source_fingerprint'],previous)
        self.assertEqual(before,{str(p):p.read_bytes() for p in self.plugin.rglob('*') if p.is_file()})
        self.assertEqual(len(rows),3)
    def test_credential_file_is_not_read_and_literal_is_held(self):
        self.source('ai-knowledge','0global/service-accounts/private.json','invalid secret encoding ignored')
        self.source('ai-knowledge','notes.md','-----BEGIN '+'PRIVATE KEY-----')
        rows,contents=pipe.scan(self.cfg)
        self.assertEqual(len(contents),0);self.assertEqual(rows[0]['status'],'pending')
        self.assertTrue(any(r['sha256'] is None and r['status']=='excluded' for r in rows))
    def test_output_in_any_folder_never_becomes_input(self):
        self.source('ai-knowledge','_generated/new-package/.codex-plugin/plugin.json','{}')
        self.source('ai-knowledge','_generated/new-package/notes.md','# Must not ingest')
        self.source('ai-knowledge','_generated/github_publish_20990101/report.md','# loop')
        rows,contents=pipe.scan(self.cfg);self.assertFalse(contents);self.assertTrue(all(x['status']=='excluded' for x in rows))
    def test_generated_dictionary_and_report_are_included(self):
        self.source('ai-knowledge','_generated/table_docs_20260521/tables/example.md','# Historical dictionary\n2026-05-21\nfield: event_date')
        self.source('ai-knowledge','_generated/review_20260909/report.md','# Formal report\n2026-09-09')
        rows,_=pipe.scan(self.cfg);self.assertTrue(all(x['status']=='historical' for x in rows))
    def test_crlf_source_survives_github_text_roundtrip(self):
        p=self.source('ai-knowledge','topic.md','# Windows document\nLine two\n')
        p.write_bytes(b'# Windows document\r\nLine two\r\n')
        result,rows=pipe.build(self.cfg,self.stage);row=rows[0]
        published=(self.plugin/row['material']).read_text(encoding='utf-8')
        self.assertNotIn('\r',published)
        self.assertEqual(pipe.sha(published),row['content_sha256'])
        self.assertEqual(pipe.sha((self.plugin/row['material']).read_bytes()),row['content_sha256'])
        self.assertNotEqual(row['sha256'],row['content_sha256'])
    def test_identical_text_deduplicates_without_losing_provenance(self):
        for s in self.cfg['sources']:self.source(s,'topic.md','# Same business text')
        result,rows=pipe.build(self.cfg,self.stage);self.assertEqual(result['texts'],1);self.assertEqual(len(rows),3);self.assertEqual(sum(r['status']=='duplicate' for r in rows),2)
    def test_conflicting_definitions_kept_separate(self):
        self.source('cursor_summary','revenue.md','# Revenue\nUse source A in May')
        self.source('codex_summary','revenue.md','# Revenue\nUse source B in September')
        result,rows=pipe.build(self.cfg,self.stage);self.assertEqual(result['texts'],2)
        self.assertTrue(all(r['status']=='historical' for r in rows))
    def test_review_is_bound_to_exact_content(self):
        p=self.source('ai-knowledge','_generated/run/data.json','[{"country":"US","revenue":20}]')
        self.cfg['reviews']={'ai-knowledge:_generated/run/data.json':{'sha256':pipe.sha(p.read_bytes()),'aggregate_or_schema':True}}
        self.assertEqual(pipe.scan(self.cfg)[0][0]['status'],'historical')
        p.write_text('[{"country":"US","revenue":30}]')
        self.assertEqual(pipe.scan(self.cfg)[0][0]['status'],'pending')
    def test_standalone_library_retains_deleted_source(self):
        original=self.source('ai-knowledge','topic.md','# Unique standalone phrase')
        pipe.build(self.cfg,self.stage)
        shutil.copytree(self.stage,Path(self.cfg['distribution']))
        original.unlink();pipe.build(self.cfg,self.stage)
        manifest=json.loads((self.plugin/'library/catalog.json').read_text(encoding='utf-8'))
        row=manifest['sources'][0];self.assertEqual(row['status'],'historical')
        self.assertIn('standalone phrase',(self.plugin/row['material']).read_text(encoding='utf-8'))
    def test_temporarily_unreadable_source_preserves_prior_evidence_as_history(self):
        original=self.source('ai-knowledge','topic.md','# Readable prior evidence')
        pipe.build(self.cfg,self.stage)
        shutil.copytree(self.stage,Path(self.cfg['distribution']))
        read_bytes=Path.read_bytes
        def unavailable(path):
            if path==original:raise OSError('cloud file temporarily unavailable')
            return read_bytes(path)
        with patch.object(Path,'read_bytes',unavailable):
            result,rows=pipe.build(self.cfg,self.stage)
        self.assertEqual(rows[0]['status'],'pending')
        self.assertIsNone(rows[0]['sha256'])
        manifest=json.loads((self.plugin/'library/catalog.json').read_text(encoding='utf-8'))
        retained=next(r for r in manifest['sources'] if r['status']=='historical')
        self.assertIn('prior evidence',(self.plugin/retained['material']).read_text(encoding='utf-8'))
    def test_relative_links_resolve_to_bundled_evidence(self):
        self.source('ai-knowledge','report.md','# Report\n[Query](queries/example.sql)')
        self.source('ai-knowledge','queries/example.sql','SELECT 1')
        pipe.build(self.cfg,self.stage)
        rows=json.loads((self.plugin/'library/catalog.json').read_text(encoding='utf-8'))['sources']
        report=next(r for r in rows if r['path']=='report.md')
        self.assertTrue((self.plugin/report['links'][0]['material']).is_file())
    def test_three_way_preserves_remote_edit_and_holds_collision(self):
        updates,conflicts=pipe.prepare_changes({'a':'old','b':'old'},{'a':'local','b':'old','c':'new'},{'a':'remote','b':'remote','remote-only':'x'})
        self.assertEqual(updates,{'c':'new'});self.assertEqual(conflicts,['a'])
    def test_pending_install_does_not_claim_success_or_erase_publication(self):
        state=self.base/'state';pipe.write_json(state/'release-status.json',{'published_commit':'new','installation':'pending'})
        pipe.write_json(state/'state.json',{'commit':'old','version':'old'})
        with self.assertRaises(ValueError):release.installed(state)
        self.assertEqual(json.loads((state/'release-status.json').read_text())['published_commit'],'new')
    def test_unavailable_remote_snapshot_preserves_state_and_can_retry(self):
        state=self.base/'state';pipe.write_json(state/'release-status.json',{'published_commit':'old','installation':'installed'})
        snapshot=self.base/'remote.json';before=(state/'release-status.json').read_bytes()
        with self.assertRaises(FileNotFoundError):release.published(state,snapshot,'fingerprint')
        self.assertEqual((state/'release-status.json').read_bytes(),before)
        files={'plugins/collart-data-assistant/.codex-plugin/plugin.json':json.dumps({'name':'collart-data-assistant','version':'0.2.0'}),'.agents/plugins/marketplace.json':'{}','plugins/collart-data-assistant/scripts/kb.py':'# fixture','plugins/collart-data-assistant/knowledge/INDEX.md':'# fixture'}
        entries=[]
        for p,t in files.items():
            b=t.encode();entries.append({'path':p,'content':t,'sha':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()})
        pipe.write_json(snapshot,{'repository':'zhiqiangliu0920/collart-ai-knowledge','commit':'a'*40,'files':entries})
        result=release.published(state,snapshot,'fingerprint')
        self.assertEqual(result['installation'],'pending');self.assertEqual(result['published_commit'],'a'*40)

if __name__=='__main__':unittest.main()
