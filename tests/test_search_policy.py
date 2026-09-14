import importlib.util,json,subprocess,sys,tempfile,unittest
from pathlib import Path
KB=Path(__file__).resolve().parents[1]/'plugins/collart-data-assistant/scripts/kb.py'
class SearchPolicyTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
  (self.root/'library').mkdir();(self.root/'knowledge').mkdir()
  rows=[]
  for name,business,review in [('current','documented','reviewed_static'),('deprecated','deprecated','reviewed_static'),('uncertain','uncertain','needs_review')]:
   (self.root/'library'/f'{name}.txt').write_text('SearchNeedle '+name,encoding='utf-8')
   rows.append({'id':'ai-knowledge:'+name,'record_id':'ai-knowledge:'+name,'aliases':['ai-knowledge:new/'+name],'material':'library/'+name+'.txt','title':name,'project':'shared','kind':'table','status':'included','business_status':business,'review_status':review,'dates':[],'source':'ai-knowledge','path':'new/'+name})
  (self.root/'library/catalog.json').write_text(json.dumps({'sources':rows}),encoding='utf-8')
 def run_kb(self,*args):
  import os
  env={**os.environ,'PYTHONIOENCODING':'utf-8'}
  return json.loads(subprocess.check_output([sys.executable,'-B',str(KB),'--root',str(self.root),*args],env=env).decode('utf-8'))
 def test_default_hides_deprecated_and_unreviewed(self):
  r=self.run_kb('search','SearchNeedle');self.assertEqual([x['title'] for x in r['results']],['current']);self.assertIsNone(r['historical_or_unreviewed_matches']);self.assertEqual(r['excluded_records'],2)
 def test_history_and_specific_status_are_available(self):
  self.assertEqual(self.run_kb('search','SearchNeedle','--include-history')['matches'],3)
  self.assertEqual(self.run_kb('search','SearchNeedle','--business-status','deprecated')['results'][0]['title'],'deprecated')
 def test_old_and_new_source_paths_read_same_body_without_source_root(self):
  old=self.run_kb('read','ai-knowledge:current');new=self.run_kb('read','ai-knowledge:new/current');self.assertEqual(old['body'],new['body'])
