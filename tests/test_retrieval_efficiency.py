"""Business retrieval, bounded output and portability regressions. No warehouse calls."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

P = Path(__file__).resolve().parents[1] / 'plugins/collart-data-assistant'
spec = importlib.util.spec_from_file_location('efficiency_kb', P/'scripts/kb.py')
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


class RetrievalTests(unittest.TestCase):
    def run_kb(self, *args, root=P):
        proc = subprocess.run([sys.executable, '-B', str(P/'scripts/kb.py'), '--root', str(root), *args], capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return json.loads(proc.stdout.decode('utf-8'))

    def test_android_income_returns_contracts_first(self):
        r = self.run_kb('search', '收入', '--project', 'collart_android')
        ids = [x['id'] for x in r['results']]
        self.assertEqual(ids[0], 'android-revenue-trend')
        self.assertIn('shared-payment-evidence', ids[:3])
        self.assertIn('shared-table-routing', ids[:3])
        self.assertNotIn('shared-internal-users', ids)
        self.assertEqual(r['searched_scopes'], ['topics'])

    def test_compound_question_and_business_alias_preserve_unknowns(self):
        question = '分析 Collart 安卓 最近 7 个完整日的收入变化，以及免费看广告按钮的点击率'
        r = self.run_kb('search', question, '--project', 'collart_android')
        ids = [x['id'] for x in r['results']]
        self.assertIn('android-revenue-trend', ids[:3])
        self.assertIn('android-reward-ad-click', ids[:3])
        body = self.run_kb('read', 'android-reward-ad-click')['body']
        self.assertIn('尚未核对当前 UI', body)
        self.assertIn('没有确认该按钮曝光事件', body)
        self.assertIn('不能把广告展示成功作为按钮曝光', body)
        self.assertNotIn('verified"', body)

    def test_exact_table_and_company_rules(self):
        result = self.run_kb('search', 'aidata2025.ads_collartweb.ads_oper_user_active_di', '--project', 'collart_web')
        self.assertEqual(result['results'][0]['id'], 'shared-table-routing')
        for project in ['collart_android', 'collart_web', 'collart_ios', 'collart_fashion']:
            r = self.run_kb('search', 'metric_name', '--project', project)
            self.assertIn('company-event-rule-contract', [x['id'] for x in r['results']])

    def test_topic_query_does_not_read_material_catalog_or_bodies(self):
        original = Path.read_text
        reads = []
        def observed(path, *args, **kwargs):
            reads.append(path.as_posix())
            return original(path, *args, **kwargs)
        with patch.object(Path, 'read_text', observed), patch.object(sys, 'argv', ['kb', 'search', '收入', '--project', 'collart_android']):
            with contextlib.redirect_stdout(io.StringIO()):
                kb.main()
        self.assertFalse(any(x.endswith('library/catalog.json') or '/library/text/' in x for x in reads))
        self.assertEqual(sum(x.endswith('library/topic_impacts.json') for x in reads), 1)

    def test_section_read_and_lossless_continuation(self):
        ident = 'ai-knowledge:collart_android/tables/storytemplate-10a27.analytics_232977577.events_.md'
        base = ['read', ident, '--section', '4.15 触发生成事件']
        full = self.run_kb(*base, '--full')
        self.assertLess(len(full['body']), 1000)
        self.assertIn('generate_watch_ad_reward_earned', full['body'])
        self.assertNotIn('ai_service_task_create', full['body'])
        chunks, offset = [], 0
        while True:
            result = self.run_kb(*base, '--max-chars', '220', '--offset', str(offset))
            self.assertLessEqual(len(result['body']), 220)
            self.assertIn('最近 30 天', result['data_access_policy'])
            chunks.append(result['body'])
            if not result['truncated']:
                break
            offset = result['next_offset']
        self.assertEqual(''.join(chunks), full['body'])

    def test_index_falls_back_on_same_length_edit_without_writing(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(P/'knowledge', root/'knowledge')
            shutil.copytree(P/'config', root/'config')
            (root/'library').mkdir()
            shutil.copyfile(P/'library/topic_impacts.json', root/'library/topic_impacts.json')
            shutil.copyfile(P/'search-index.json', root/'search-index.json')
            path = root/'knowledge/collart_android/android-revenue-trend.md'
            text = path.read_text(encoding='utf-8')
            path.write_text(text.replace('Android 近七日收入变化', 'Android 近七日营收变化'), encoding='utf-8')
            before = (root/'search-index.json').read_bytes()
            result = self.run_kb('search', '收入', '--project', 'collart_android', root=root)
            self.assertEqual(result['index_state'], 'live_fallback')
            self.assertEqual((root/'search-index.json').read_bytes(), before)

    def test_invalid_selection_and_limits_fail(self):
        for args in [('search', '收入', '--limit', '0'), ('read', 'android-revenue-trend', '--offset', '-1'),
                     ('read', 'android-revenue-trend', '--section', 'absent'),
                     ('read', 'android-revenue-trend', '--start-line', '99999')]:
            p = subprocess.run([sys.executable, '-B', str(P/'scripts/kb.py'), *args], capture_output=True)
            self.assertEqual(p.returncode, 2)


if __name__ == '__main__':
    unittest.main()
