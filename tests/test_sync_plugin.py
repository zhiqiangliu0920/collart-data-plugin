import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('sync_plugin', Path(__file__).resolve().parents[1]/'scripts/sync_plugin.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root, self.state = self.base/'source', self.base/'state'
        self.root.mkdir()
        self.state.mkdir()
        self.files = {
            sync.MANIFEST: json.dumps({'name':'collart-data-assistant','version':'0.1.0'}),
            '.agents/plugins/marketplace.json':json.dumps({'name':'personal'}),
            sync.PLUGIN+'scripts/kb.py':'# fixture',
            sync.PLUGIN+'knowledge/INDEX.md':'old knowledge',
        }
        for name, content in self.files.items():
            dest = self.root/name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding='utf-8')
        sync.write_json(self.state/'state.json', {'files':sync.inventory(self.root), 'commit':None, 'version':'0.1.0'})

    def snapshot(self, files=None):
        entries=[]
        for name, content in (files or self.files).items():
            blob=content.encode()
            entries.append({'path':name,'content':content,'sha':hashlib.sha1(b'blob '+str(len(blob)).encode()+b'\0'+blob).hexdigest()})
        path=self.base/'snapshot.json'
        sync.write_json(path, {'repository':sync.REPOSITORY,'commit':'a'*40,'files':entries})
        return path

    def fake_run(self, command):
        if 'read_marketplace_name.py' in str(command):
            return 'personal\n'
        if 'update_plugin_cachebuster.py' in str(command):
            path=Path(command[-1])/'.codex-plugin/plugin.json'
            manifest=json.loads(path.read_text())
            manifest['version']='0.1.0+codex.fixture'
            sync.write_json(path,manifest)
        if 'check' in command:
            return json.dumps({'entries':17,'errors':[],'warnings':['draft']})
        return '{}'

    def entry(self, root):
        return {'version':json.loads((root/sync.MANIFEST).read_text())['version']}

    def test_paths_and_symlink_escape_are_rejected(self):
        for name in ['../private', '/absolute', 'C:/keys', '.git/config', 'a\\b']:
            with self.assertRaises(ValueError):
                sync.safe_path(self.root,name)

    def test_corrupt_blob_is_rejected(self):
        path=self.snapshot()
        value=json.loads(path.read_text())
        value['files'][0]['content']+='changed'
        sync.write_json(path,value)
        with self.assertRaisesRegex(ValueError,'hash mismatch'):
            sync.load_snapshot(path)

    def test_local_edits_block_update_without_touching_content(self):
        path=self.root/(sync.PLUGIN+'knowledge/INDEX.md')
        path.write_text('unpublished work')
        with self.assertRaisesRegex(RuntimeError,'local changes'):
            sync.apply_snapshot(self.root,self.state,self.snapshot(),self.base)
        self.assertEqual(path.read_text(),'unpublished work')

    def test_failed_install_restores_source_and_baseline(self):
        before=sync.inventory(self.root)
        baseline=(self.state/'state.json').read_bytes()
        files={**self.files, sync.PLUGIN+'knowledge/INDEX.md':'new knowledge', 'README.md':'new file'}
        attempts=[]
        def failing_run(command):
            if command[:3]==['codex','plugin','add']:
                attempts.append(command)
                if len(attempts)==1:
                    raise RuntimeError('installation failed')
            return self.fake_run(command)
        with patch.object(sync,'configured_plugin',side_effect=self.entry), patch.object(sync,'run',side_effect=failing_run):
            with self.assertRaisesRegex(RuntimeError,'installation failed'):
                sync.apply_snapshot(self.root,self.state,self.snapshot(files),self.base)
        self.assertEqual(sync.inventory(self.root),before)
        self.assertEqual((self.state/'state.json').read_bytes(),baseline)
        self.assertEqual(len(attempts),2)

    def test_success_then_same_commit_does_not_reinstall(self):
        snapshot=self.snapshot({**self.files,sync.PLUGIN+'knowledge/INDEX.md':'new knowledge'})
        with patch.object(sync,'configured_plugin',side_effect=self.entry), patch.object(sync,'run',side_effect=self.fake_run) as runner, patch.object(sync,'check_cache',return_value='fixture-cache'):
            updated=sync.apply_snapshot(self.root,self.state,snapshot,self.base)
            runner.reset_mock()
            same=sync.apply_snapshot(self.root,self.state,snapshot,self.base)
        self.assertEqual(updated['status'],'updated')
        self.assertEqual(same['status'],'unchanged')
        runner.assert_not_called()

    def test_cache_comparison_detects_stale_knowledge(self):
        cache=self.base/'codex/plugins/cache/personal/collart-data-assistant/0.1.0'
        shutil.copytree(self.root/sync.PLUGIN,cache)
        with patch.dict(sync.os.environ,{'CODEX_HOME':str(self.base/'codex')}):
            sync.check_cache(self.root,self.state,'0.1.0')
            (cache/'knowledge/INDEX.md').write_text('stale')
            with self.assertRaisesRegex(RuntimeError,'cache differs'):
                sync.check_cache(self.root,self.state,'0.1.0')


if __name__=='__main__':
    unittest.main()
