"""Distribution regressions for the maintainer's read-only/recent-events contract.

These are offline packaging checks, not a SQL sandbox or an IAM enforcement test.
"""
from pathlib import Path
import datetime as dt
import json
import re
import sqlite3
import subprocess
import sys
import unittest

P=Path(__file__).resolve().parents[1]/'plugins/collart-data-assistant'

class DataAccessPolicyTests(unittest.TestCase):
    def test_both_entrypoints_require_the_shared_policy(self):
        for name in ['collart-analysis','collart-knowledge-maintain']:
            body=(P/'skills'/name/'SKILL.md').read_text(encoding='utf-8')
            self.assertIn('../../docs/data-access-policy.md',body)
            self.assertIn('不能分批读取更早日期',body)
            self.assertIn('禁止通过 SQL、API、脚本',body)

    def test_every_maintained_raw_events_query_is_bounded_by_execution_date(self):
        raw=[]
        for path in (P/'presets').glob('*.sql'):
            sql=path.read_text(encoding='utf-8')
            code=re.sub(r'--[^\n]*','',sql)
            self.assertNotRegex(code,r'(?im)^\s*(INSERT|UPDATE|DELETE|MERGE|TRUNCATE|CREATE|ALTER|DROP|LOAD|CALL|EXECUTE)\b')
            if not re.search(r'`[^`]*\.events[^`]*`',code):continue
            raw.append(path.name)
            self.assertIn("ASSERT @start_date >= DATE_SUB(CURRENT_DATE('Asia/Shanghai'), INTERVAL 30 DAY)",code)
            self.assertIn("ASSERT @end_date < CURRENT_DATE('Asia/Shanghai')",code)
            self.assertIn('DATE_DIFF(@end_date, @start_date, DAY) BETWEEN 0 AND 29',code)
            self.assertIn("_TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', @start_date) AND FORMAT_DATE('%Y%m%d', @end_date)",code)
        self.assertEqual(set(raw),{'probe_event_names.sql','extract_event_param.sql'})

    def test_event_time_filter_preserves_anonymous_only_when_requested(self):
        # Execute the actual SQL predicate with ARRAY expansion adapted to a SQLite CTE.
        sql=(P/'presets/internal_user_filter_event_time.sql').read_text(encoding='utf-8')
        predicate=re.sub(r'--[^\n]*','',sql).strip().removeprefix('AND ')
        predicate=predicate.replace('UNNEST(@internal_user_ids) AS internal_id','internal_users')
        conn=sqlite3.connect(':memory:');self.addCleanup(conn.close)
        query="WITH events(user_id) AS (VALUES (NULL), ('employee'), ('customer')), internal_users(internal_id) AS (VALUES ('EMPLOYEE')) SELECT user_id FROM events WHERE "+predicate
        self.assertEqual(conn.execute(query,{'include_anonymous':True}).fetchall(),[(None,),('customer',)])
        self.assertEqual(conn.execute(query,{'include_anonymous':False}).fetchall(),[('customer',)])

    def test_reading_historical_material_exposes_the_access_contract(self):
        catalog=json.loads((P/'library/catalog.json').read_text(encoding='utf-8'))['sources']
        source=next(s for s in catalog if s.get('material') and s['status']=='historical')
        run=subprocess.run([sys.executable,'-B',str(P/'scripts/kb.py'),'read',source['id']],capture_output=True,encoding='utf-8',check=True)
        result=json.loads(run.stdout)
        self.assertIn('禁止读取更早日期或拆批绕过',result['data_access_policy'])
        self.assertTrue(result['body'])

if __name__=='__main__':unittest.main()
