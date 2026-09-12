"""Observable offline behavior in isolated copies. Run: python -m unittest discover -s tests -v"""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("kb", PACKAGE / "scripts/kb.py")
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="team-knowledge-test-")
        self.scratch = Path(self.temp.name).resolve()
        self.root = self.scratch / "同事 新位置" / "team-data-knowledge"
        shutil.copytree(PACKAGE, self.root, ignore=shutil.ignore_patterns("__pycache__", ".git"))

    def tearDown(self):
        # Only this test-owned directory is recursively cleaned.
        assert self.root.resolve().is_relative_to(self.scratch)
        self.temp.cleanup()

    def run_cli(self, *args, code=0):
        prefix = ["--root", str(self.root), "--authoring"] if args[0] in {"new", "index"} else []
        result = subprocess.run([sys.executable, "-B", "-X", "utf8", str(self.root / "scripts/kb.py"), *prefix, *args], cwd=self.scratch, text=True, encoding="utf-8", capture_output=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def edit(self, relative, update):
        path = self.root / relative
        meta, body = kb.parse(path)
        update(meta)
        kb.write(path, kb.encode(meta, body))

    def test_relocated_package_valid_and_searchable(self):
        report = self.run_cli("check", "--as-of", "2026-09-12")
        self.assertFalse(report["errors"])
        result = self.run_cli("search", "user_ids", "--project", "collart_web")
        self.assertTrue(any(hit["id"] == "collart_web-identity" for hit in result["results"]))
        self.assertTrue(all(hit["verified_at"] is None for hit in result["results"]))

    def test_new_draft_found_without_reindex_then_check_detects_stale_catalog(self):
        self.run_cli("new", "--id", "new-rule", "--project", "sample", "--kind", "metric", "--title", "独有检索词")
        self.assertEqual(self.run_cli("search", "独有检索词")["matches"], 1)
        self.assertTrue(any("stale index" in x for x in self.run_cli("check", code=1)["errors"]))
        self.run_cli("index")
        self.assertFalse(self.run_cli("check")["errors"])
        self.run_cli("new", "--id", "new-rule", "--project", "sample", "--kind", "metric", "--title", "重复", code=2)

    def test_path_traversal_cannot_create_outside_knowledge(self):
        self.run_cli("new", "--id", "escape", "--project", "../../outside", "--kind", "metric", "--title", "越界", code=2)
        self.assertFalse((self.scratch / "outside").exists())

    def test_verified_requires_real_evidence_fields(self):
        self.edit("knowledge/collart_web/identity.md", lambda m: m.update(status="verified"))
        self.run_cli("index")
        report = self.run_cli("check", code=1)
        self.assertTrue(any("requires owner, reviewer" in e for e in report["errors"]))

    def test_duplicate_identity_rejected(self):
        shutil.copyfile(self.root / "knowledge/collart_web/identity.md", self.root / "knowledge/collart_web/duplicate.md")
        self.run_cli("index")
        self.assertTrue(any("duplicate id" in e for e in self.run_cli("check", code=1)["errors"]))

    def test_broken_link_and_evidence_tampering_rejected(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as stream:
            stream.write("\n[断链](missing.md)\n")
        with (self.root / "provenance/excerpts/metrics.txt").open("a", encoding="utf-8") as stream:
            stream.write("\nchanged\n")
        errors = self.run_cli("check", code=1)["errors"]
        self.assertTrue(any("broken link" in e for e in errors))
        self.assertTrue(any("evidence missing/changed" in e for e in errors))

    def test_source_drift_reports_affected_entries(self):
        original = self.scratch / "sources"
        original.mkdir()
        doc = original / "routing.md"
        doc.write_text("original", encoding="utf-8")
        source = kb.sources(self.root)[0]
        source.update(source_path="routing.md", source_sha256=kb.sha(doc))
        kb.write(self.root / "provenance/sources.json", kb.dump({"sources": [source]}))
        self.assertFalse(self.run_cli("source-check", "--source-root", str(original))["changes"])
        doc.write_text("changed", encoding="utf-8")
        report = self.run_cli("source-check", "--source-root", str(original), code=1)
        self.assertIn("shared-table-routing", report["changes"][0]["affected_entries"])

    def test_review_due_is_reported_and_strict_fails(self):
        report = self.run_cli("check", "--as-of", "2026-11-01", "--strict", code=1)
        self.assertTrue(any("review_due" in warning for warning in report["warnings"]))

    def test_default_install_location_cannot_be_written_implicitly(self):
        before = (self.root / "catalog.json").read_bytes()
        result = subprocess.run([sys.executable, "-B", str(self.root / "scripts/kb.py"), "index"], capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(before, (self.root / "catalog.json").read_bytes())

    def test_explicit_authoring_cannot_write_plugin_cache(self):
        cache = self.scratch / "plugins/cache/collart-data-assistant"
        shutil.copytree(self.root, cache)
        result = subprocess.run([sys.executable, "-B", str(cache / "scripts/kb.py"), "--root", str(cache), "--authoring", "index"], capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"installed plugin cache", result.stdout)

    def test_empty_internal_exclusion_list_is_not_silently_accepted(self):
        path = self.root / "config/internal-user-ids.json"
        config = json.loads(path.read_text(encoding="utf-8"))
        config["user_ids"] = []
        kb.write(path, kb.dump(config))
        self.assertIn("invalid or empty internal-user configuration", self.run_cli("check", code=1)["errors"])


if __name__ == "__main__":
    unittest.main()
