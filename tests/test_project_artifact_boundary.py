import json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_pipeline as pipe

class ProjectArtifactBoundaryTests(unittest.TestCase):
    def test_restored_or_new_artifacts_never_become_knowledge(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            paths=['collart_web/reports/2026-09/report.md','collart_android/sql-snippets/draft.sql',
                   'collart_ios/sql_presets/retention.sql','collart_fashion/analysis_playbooks/funnel.md']
            for name in paths:
                p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('# '+name+'\nSELECT 1;',encoding='utf-8')
            rows,contents=pipe.scan({'sources':{'ai-knowledge':str(root)}})
            bypath={r['path']:r for r in rows}
            for name in paths[:2]:
                self.assertEqual(bypath[name]['status'],'excluded')
                self.assertIsNone(bypath[name]['sha256'])
                self.assertTrue(bypath[name]['reason'].startswith('项目工作产物'))
            for name in paths[2:]:self.assertEqual(bypath[name]['status'],'included')

    def test_scope_does_not_exclude_other_sources_or_topic_names(self):
        self.assertFalse(pipe.project_artifact('cursor_summary','collart_web/reports/report.md'))
        self.assertFalse(pipe.project_artifact('ai-knowledge','collart_web/analysis_playbooks/reports/method.md'))
        self.assertFalse(pipe.project_artifact('ai-knowledge','reports/historical.md'))

if __name__=='__main__':unittest.main()
