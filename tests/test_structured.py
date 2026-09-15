import argparse
import datetime as dt
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1];P=ROOT/'plugins/collart-data-assistant'
def mod(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
kb=mod('kb',P/'scripts/kb.py');query=mod('query',P/'scripts/query.py');build=mod('build',ROOT/'scripts/build.py');review=mod('source_review',ROOT/'scripts/source_review.py')
def search(q,project=None,kind=None,history=False):return argparse.Namespace(query=q,project=project,kind=kind,include_history=history,limit=3,scope='auto')
def read(id,**kw):return argparse.Namespace(**dict(dict(id=id,section=None,field=None,start_line=None,end_line=None,offset=0,max_chars=2800,full=False,toc=False),**kw))

CASES=[
 ('Android 收入','collart_android','metric','android.revenue',['purchase_revenue','ad_revenue']),
 ('免费看广告按钮点击率','collart_android','event','android.ads',['generate_watch_ad','曝光']),
 ('Web 画像登录号','collart_web','business','web.identity',['user_id','user_ids','OR']),
 ('Fashion 收入与 Web 交集','collart_fashion','metric','fashion.revenue',['600','交集']),
 ('ASA 关键词归因','collart_ios','metric','ios.asa',['CNY','去重','2026-07-20']),
 ('成熟留存','collart_android','metric','shared.activity',['NULL','cohort','N-1']),
 ('ADS无法使用回退原始埋点',None,'business','shared.routing',['DM','7 天','GA4']),
 ('没有连接只读权限',None,'policy','shared.access',['连接','7 天','只读']),
 ('Web 用户价值分层','collart_web','metric','web.value',['500','100','50']),
]

class RetrievalTests(unittest.TestCase):
    def test_fixed_questions_retrieve_needed_boundaries(self):
        for q,project,kind,id,terms in CASES:
            with self.subTest(question=q):
                r=kb.search(P,search(q,project,kind));self.assertIn(id,[x['id'] for x in r['results']])
                body=kb.read(P,read(id,full=True))['body']
                for t in terms:self.assertIn(t,body)

    def test_exact_table_field_and_bounded_sections(self):
        table='aidata2025.ads_collartweb.ads_oper_user_profile_df'
        self.assertEqual(kb.search(P,search(table))['results'][0]['id'],'table:'+table)
        r=kb.read(P,read(table,field='user_ids'));self.assertIn('| `user_ids` |',r['body']);self.assertIn('使用边界',r['body']);self.assertNotIn('| `device.browser` |',r['body'])
        r=kb.read(P,read('fashion.events',section='Step 4',max_chars=120));self.assertLessEqual(len(r['body']),120)
        if r['truncated']:
            next=kb.read(P,read('fashion.events',section='Step 4',offset=r['next_offset'],max_chars=120));self.assertNotEqual(next['body'],r['body'])

    def test_default_output_and_legacy_ids(self):
        self.assertLessEqual(len(kb.search(P,search('收入'))['results']),3)
        self.assertLessEqual(len(kb.read(P,read('shared.routing'))['body']),2800)
        self.assertEqual(kb.read(P,read('android-revenue-trend'))['id'],'android.revenue')
        archived=next(k for k,v in kb.load(P,'_meta/aliases.json').items() if v.get('archived'))
        self.assertTrue(kb.read(P,read(archived))['archived'])

    def test_path_escape_and_invalid_boundaries(self):
        for path in ['../secret','../../private']:
            with self.assertRaises(ValueError):kb.inside(P,path)
        for kw in [{'start_line':0},{'offset':-1},{'max_chars':0},{'field':'missing'},{'section':'not-a-section'}]:
            with self.assertRaises(ValueError):kb.read(P,read('web.identity',**kw))

    def test_metadata_only_index_and_targeted_read(self):
        self.assertFalse((P/'_meta/search-index.json').exists())
        self.assertTrue(all('text' not in r for r in kb.load(P,'_meta/catalog.json')['entries']))
        original=kb.load;opened=[]
        def load(root,path,default=None):opened.append(path);return original(root,path,default)
        with patch.object(kb,'load',side_effect=load):kb.read(P,read('web.identity'))
        self.assertNotIn('_meta/search-index.json',opened)

    def test_source_hash_and_live_fallback(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);shutil.copytree(P,root,dirs_exist_ok=True)
            p=root/'knowledge/collart_web/business/identity.md';m,b=kb.parse(p);p.write_text(kb.encode(m,b+'\n\nunique_live_marker'),encoding='utf-8')
            r=kb.search(root,search('unique_live_marker'));self.assertEqual(r['index_state'],'live_fallback');self.assertEqual(r['results'][0]['id'],'web.identity')
            self.assertTrue(kb.read(root,read('web.identity'))['index_stale'])
            s=next(s for s in kb.load(root,'_meta/sources.json')['sources'] if s.get('origin')=='dataform');(root/s['path']).write_text('changed',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'integrity'):kb.read(root,read(s['id']))

class QueryBoundaryTests(unittest.TestCase):
    def test_seven_day_edges_and_no_arbitrary_history(self):
        now=dt.date(2026,9,14)
        self.assertEqual(query.window(now=now),(dt.date(2026,9,7),dt.date(2026,9,13)))
        self.assertEqual(query.window(include_today=True,now=now),(dt.date(2026,9,8),now))
        for start,end,today in [('2026-08-01','2026-08-07',False),('2026-09-06','2026-09-13',False),('2026-09-07','2026-09-14',True),('2026-09-14','2026-09-14',False),('2026-09-12','2026-09-11',False)]:
            with self.assertRaises(ValueError):query.window(start,end,today,now)

    def test_all_raw_products_are_bounded_and_read_only(self):
        for project in query.PRODUCTS:
            r=query.raw_events(project,now=dt.date(2026,9,14));sql=r['sql'];query.read_only(sql)
            self.assertIn("_TABLE_SUFFIX BETWEEN '20260907' AND '20260913'",sql)
            self.assertIn('app_info.id',sql)
            if project in ['collart_web','collart_fashion']:
                self.assertIn('studio|fashion',sql);self.assertIn('@internal_user_ids',sql);self.assertIn('ERROR(',sql);self.assertIn('IS NOT NULL',sql)
            if project=='collart_ios':self.assertIn('manual_install',sql)
        with self.assertRaises(ValueError):query.raw_events('anything; DROP TABLE x')

    def test_write_escapes_fail(self):
        bad=['DELETE FROM t','WITH x AS (SELECT 1) DELETE FROM t','SELECT 1; DROP TABLE t','CALL x()','EXPORT DATA OPTIONS(uri="gs://x") AS SELECT 1','SELECT 1 INTO t','SELECT EXTERNAL_QUERY("c","UPDATE x")','EXECUTE IMMEDIATE "SELECT 1"','SELECT 1 /* unclosed']
        for sql in bad:
            with self.subTest(sql=sql),self.assertRaises(ValueError):query.read_only(sql)
        query.read_only("-- UPDATE is a comment\nSELECT 'DELETE', 1 /* DROP */;")

    def test_warehouse_source_windows_are_preserved(self):
        p=P/'sources/dataform/aidata/definitions/dwd/daily/h_dwd_oper_sub_order_revenue_df.sqlx'
        self.assertIn('最近30天',p.read_text(encoding='utf-8'))
        self.assertIn('30',p.read_text(encoding='utf-8'))
        for p in (P/'knowledge').rglob('*.sql'):query.read_only(p.read_text(encoding='utf-8'))

class BuildTests(unittest.TestCase):
    def test_complete_fields_and_shared_multi_output_sources(self):
        self.assertEqual(build.validate(ROOT)['errors'],[])
        tables=kb.load(P,'_meta/catalog.json')['entries'];self.assertEqual(len({r['tables'][0] for r in tables if r['kind']=='table'}),sum(r['kind']=='table' for r in tables))
        s=next(s for s in kb.load(P,'_meta/sources.json')['sources'] if s.get('origin')=='dataform' and len(s.get('outputs',[]))>1)
        for table in s['outputs']:self.assertIn(s['id'],kb.resolve(P,table)[0]['sources'])

    def test_deterministic_index_and_new_structure_only(self):
        expected=kb.artifacts(P);kb.index(P)
        self.assertEqual(kb.artifacts(P),expected)
        for name in ['library','presets','provenance']:self.assertFalse((P/name).exists())

    def test_sources_change_marks_knowledge_without_restoring_old_folders(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'repo';shutil.copytree(P,root/'plugins/collart-data-assistant');(root/'maintainer').mkdir()
            source=next(s for s in kb.load(P,'_meta/sources.json')['sources'] if s.get('origin')=='dataform' and 'ads_oper_user_profile_df.sqlx' in s['id'] and 'collart_web' in s['id'])
            updated=dict(source,sha256='a'*64);capture=Path(t)/'capture.json';capture.write_text(json.dumps({'sources':[updated]}),encoding='utf-8')
            result=review.detect(root,capture=capture);change=next(c for c in result['changes'] if c['source']==source['id']);self.assertIn('web.identity',change['documents'])
            review.queue(root,result);review.queue(root,{'changes':[]});self.assertTrue(kb.resolve(root/'plugins/collart-data-assistant','web.identity')[0]['review_required'])
            self.assertTrue(json.loads((root/'maintainer/review-queue.json').read_text(encoding='utf-8'))['changes'])
            self.assertFalse((root/'plugins/collart-data-assistant/library').exists())

    def test_relative_source_requires_exist(self):
        for p in (P/'sources/dataform').rglob('*'):
            if not p.is_file():continue
            for dep in re.findall(r'require\([\"\x27](\.[^\"\x27]+)',p.read_text(encoding='utf-8')):
                q=(p.parent/dep).with_suffix('.js');self.assertTrue(q.is_file(),str(q))

    def test_source_impact_follows_transitive_knowledge_links(self):
        catalog=kb.load(P,'_meta/catalog.json')['entries']
        affected=review.dependent_documents(P,catalog,{'android.activity'})
        self.assertIn('android.acquisition',affected)
        self.assertIn('android.templates',affected)
        self.assertNotIn('ios.asa',affected)

if __name__=='__main__':unittest.main()
