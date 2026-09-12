#!/usr/bin/env python3
"""Portable knowledge catalog. Python 3.10+, standard library only; no network."""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
STATES = {"draft", "documented", "verified", "deprecated"}
KINDS = {"business", "table", "metric", "event", "lineage", "sql", "quality", "playbook"}
SLUG = re.compile(r"[a-z0-9]+(?:[-_][a-z0-9]+)*\Z")


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path leaves root: {relative}")
    return path


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def parse(path):
    text = path.read_text(encoding="utf-8-sig")
    parts = text.split("---\n", 2)
    if len(parts) != 3 or parts[0]:
        raise ValueError(f"{path.name}: missing frontmatter")
    meta = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep or not re.fullmatch(r"[a-z_]+", key) or key in meta:
            raise ValueError(f"{path.name}: invalid or duplicate metadata key")
        # A deliberately small YAML subset: every value is a JSON literal.
        meta[key] = json.loads(value.strip())
    return meta, parts[2].strip()


def encode(meta, body):
    lines = [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in meta.items()]
    return "---\n" + "\n".join(lines) + "\n---\n\n" + body.strip() + "\n"


def records(root):
    output = []
    for path in sorted((root / "knowledge").glob("*/*.md")):
        inside(root, path.relative_to(root))
        meta, body = parse(path)
        output.append((meta, body, path.relative_to(root).as_posix(), sha(path)))
    return output


def artifacts(rows):
    catalog = {"schema_version": 1, "entries": [dict(m, path=p, sha256=h) for m, _, p, h in rows]}
    lines = ["# 团队知识索引", "", "由 `scripts/kb.py index` 生成。documented = 有文档依据，尚未独立核验；draft = 待确认；verified 仅在所记范围和日期内有效。", "", "| 项目 | 类型 | 知识 | 状态 | 最后核验 | 下次复核 |", "|---|---|---|---|---|---|"]
    for meta, _, path, _ in rows:
        title = meta["title"].replace("|", "\\|")
        lines.append(f"| {meta['project']} | {meta['kind']} | [{title}]({path.removeprefix('knowledge/')}) | {meta['status']} | {meta['verified_at'] or '未核验'} | {meta['review_after'] or '未设置'} |")
    return {"catalog.json": dump(catalog), "knowledge/INDEX.md": "\n".join(lines) + "\n"}


def sources(root):
    return json.loads((root / "provenance/sources.json").read_text(encoding="utf-8"))["sources"]


def check(root, today):
    errors, warnings = [], []
    rows, source_rows = records(root), sources(root)
    source_ids = {s["id"] for s in source_rows}
    if len(source_ids) != len(source_rows):
        errors.append("duplicate source ID")
    if not rows:
        errors.append("knowledge is empty")
    seen = set()
    required = {"id", "title", "project", "kind", "status", "updated_at", "verified_at", "review_after", "owner", "verified_by", "effective_from", "sources", "tags", "supersedes", "verification_evidence"}
    for meta, body, path, _ in rows:
        missing = required - meta.keys()
        if missing:
            errors.append(f"{path}: missing {sorted(missing)}")
            continue
        ident = meta["id"]
        if not isinstance(ident, str) or not SLUG.fullmatch(ident) or ident in seen:
            errors.append(f"{path}: invalid or duplicate id")
        seen.add(ident)
        if not isinstance(meta["project"], str) or not SLUG.fullmatch(meta["project"]) or Path(path).parent.name != meta["project"]:
            errors.append(f"{path}: invalid project or directory mismatch")
        if meta["status"] not in STATES or meta["kind"] not in KINDS:
            errors.append(f"{path}: invalid status/kind")
        for field in ("title", "updated_at"):
            if not isinstance(meta[field], str) or not meta[field].strip():
                errors.append(f"{path}: {field} must be a nonempty string")
        for field in ("sources", "tags", "supersedes", "verification_evidence"):
            if not isinstance(meta[field], list) or any(not isinstance(v, str) for v in meta[field]):
                errors.append(f"{path}: {field} must be a string list")
        for field in ("updated_at", "verified_at", "review_after", "effective_from"):
            try:
                if meta[field] is not None:
                    dt.date.fromisoformat(meta[field])
            except (ValueError, TypeError):
                errors.append(f"{path}: invalid {field}")
        if isinstance(meta["sources"], list):
            unknown = set(meta["sources"]) - source_ids
            if unknown:
                errors.append(f"{path}: unknown sources {sorted(unknown)}")
        if meta["status"] in {"documented", "verified"} and not meta["sources"]:
            errors.append(f"{path}: documented/verified requires sources")
        if meta["status"] == "verified":
            if not all(meta[key] for key in ("owner", "verified_by", "verified_at", "review_after", "verification_evidence")):
                errors.append(f"{path}: verified requires owner, reviewer, dates and evidence")
            for evidence in meta["verification_evidence"]:
                if not inside(root, evidence).is_file():
                    errors.append(f"{path}: missing verification evidence")
            if meta["verified_at"] and meta["verified_at"] > today.isoformat():
                errors.append(f"{path}: verification date is in the future")
        elif meta["verified_at"] or meta["verified_by"] or meta["verification_evidence"]:
            if meta["status"] != "deprecated":
                errors.append(f"{path}: unverified entry has verification claims")
        if meta["review_after"] and meta["review_after"] <= today.isoformat() and meta["status"] != "deprecated":
            warnings.append(f"{ident}: review_due")
        if meta["status"] == "draft":
            warnings.append(f"{ident}: draft")
        if not body.startswith("# "):
            errors.append(f"{path}: body needs a title")
    for meta, _, path, _ in rows:
        for target in meta.get("supersedes", []):
            if target not in seen or target == meta["id"]:
                errors.append(f"{path}: invalid supersedes target")
    for source in source_rows:
        excerpt = inside(root, source["excerpt"])
        if not excerpt.is_file() or sha(excerpt) != source["excerpt_sha256"]:
            errors.append(f"{source['id']}: evidence missing/changed")
        if not re.fullmatch(r"[0-9a-f]{64}", source["source_sha256"]):
            errors.append(f"{source['id']}: invalid source hash")
        inside(root, source["source_path"])
    for relative, expected in artifacts(rows).items():
        path = root / relative
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            errors.append(f"{relative}: stale index; run index")
    # Targeted package checks; these do not certify business truth or all privacy risks.
    forbidden = {
        "private key": r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----",
        "personal Windows path": r"[A-Za-z]:[\\/]Users[\\/][^<\s]+",
        "email address": r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
        "literal user UUID": r"\b[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}\b",
        "Feishu webhook": r"https://[^\s/]+/open-apis/bot/v2/hook/[^\s\"<>]+",
    }
    for file in root.rglob("*"):
        if not file.is_file() or ".git" in file.relative_to(root).parts or file.suffix not in {".md", ".json", ".txt", ".yaml", ".sql"}:
            continue
        inside(root, file.relative_to(root))
        text = file.read_text(encoding="utf-8")
        for name, pattern in forbidden.items():
            if name == "literal user UUID" and file.relative_to(root).as_posix() == "config/internal-user-ids.json":
                continue  # Explicit company test-account configuration, not arbitrary user records.
            if re.search(pattern, text):
                errors.append(f"{file.relative_to(root)}: {name}")
        if file.suffix != ".md":
            continue
        # Ignore fenced code examples, and validate file targets, not heading anchors.
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\n]+)\)", prose):
            target = match.group(1).strip().strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            linked = inside(root, file.parent.relative_to(root) / target)
            if not linked.exists():
                errors.append(f"{file.relative_to(root)}: broken link {target}")
    config = json.loads((root / "config/internal-user-ids.json").read_text(encoding="utf-8"))
    ids = config.get("user_ids", [])
    if not ids or any(not isinstance(x, str) or not re.fullmatch(forbidden["literal user UUID"], x) for x in ids) or len(set(x.upper() for x in ids)) != len(ids):
        errors.append("invalid or empty internal-user configuration")
    mapping = json.loads((root / "provenance/integration-map.json").read_text(encoding="utf-8"))
    for item in mapping["inputs"]:
        if not inside(root, item["destination"]).exists():
            errors.append(f"missing integration destination: {item['destination']}")
    counts = {state: sum(m["status"] == state for m, *_ in rows) for state in sorted(STATES)}
    return {"as_of": today.isoformat(), "entries": len(rows), "states": counts, "errors": errors, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--authoring", action="store_true", help="explicitly acknowledge edits to a source workspace, never an installed cache")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("index", help="rebuild local catalog and Markdown index")
    query = sub.add_parser("search", help="search live knowledge files, including drafts")
    query.add_argument("query")
    query.add_argument("--project")
    query.add_argument("--limit", type=int, default=8)
    validate = sub.add_parser("check", help="validate package, no queries or network")
    validate.add_argument("--as-of", type=dt.date.fromisoformat, default=dt.date.today())
    validate.add_argument("--strict", action="store_true", help="warnings also fail")
    upstream = sub.add_parser("source-check", help="compare captured sources to a supplied local root")
    upstream.add_argument("--source-root", type=Path, required=True)
    create = sub.add_parser("new", help="create a draft; does not change existing knowledge")
    create.add_argument("--id", required=True)
    create.add_argument("--project", required=True)
    create.add_argument("--kind", choices=sorted(KINDS), required=True)
    create.add_argument("--title", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command in {"new", "index"}:
        if not args.authoring:
            raise ValueError("writes require --authoring and an explicit source workspace via --root")
        if "--root" not in sys.argv:
            raise ValueError("writes require explicit --root")
        parts = [p.casefold() for p in root.parts]
        if any(parts[i:i+2] == ["plugins", "cache"] for i in range(len(parts)-1)):
            raise ValueError("installed plugin cache is not an authoring workspace")
        if not (root / ".codex-plugin/plugin.json").is_file():
            raise ValueError("source workspace must contain the plugin manifest")
    if args.command == "index":
        output = artifacts(records(root))
        for relative, content in output.items():
            write(inside(root, relative), content)
        print(dump({"written": list(output)}), end="")
    elif args.command == "check":
        report = check(root, args.as_of)
        print(dump(report), end="")
        return int(bool(report["errors"] or (args.strict and report["warnings"])))
    elif args.command == "search":
        words = args.query.casefold().split()
        if not words or args.limit < 1:
            raise ValueError("query must be nonempty and limit positive")
        hits = []
        for meta, body, path, _ in records(root):
            if args.project and meta["project"] not in {args.project, "shared"}:
                continue
            searchable = (dump(meta) + body).casefold()
            score = sum(word in searchable for word in words)
            if score == len(words):
                hit = {key: meta[key] for key in ("id", "title", "project", "status", "verified_at", "review_after")}
                hit.update(path=path, review_due=bool(meta["review_after"] and meta["review_after"] <= dt.date.today().isoformat()))
                hits.append(hit)
        print(dump({"matches": len(hits), "results": hits[:args.limit]}), end="")
    elif args.command == "source-check":
        changed = []
        for source in sources(root):
            path = inside(args.source_root, source["source_path"])
            state = "missing" if not path.is_file() else ("same" if sha(path) == source["source_sha256"] else "changed")
            if state != "same":
                affected = [m["id"] for m, *_ in records(root) if source["id"] in m["sources"]]
                changed.append({"source_id": source["id"], "state": state, "affected_entries": affected})
        print(dump({"checked": len(sources(root)), "changes": changed}), end="")
        return int(bool(changed))
    elif args.command == "new":
        if not SLUG.fullmatch(args.id) or not SLUG.fullmatch(args.project) or not args.title.strip() or "\n" in args.title or "\r" in args.title:
            raise ValueError("invalid id/project/title")
        if any(meta["id"] == args.id for meta, *_ in records(root)):
            raise ValueError("ID already exists; update its original entry")
        today = dt.date.today()
        meta = dict(id=args.id, title=args.title, project=args.project, kind=args.kind, status="draft", updated_at=today.isoformat(), verified_at=None, review_after=(today + dt.timedelta(days=14)).isoformat(), owner=None, verified_by=None, effective_from=None, sources=[], tags=[], supersedes=[], verification_evidence=[])
        body = f"# {args.title}\n\n## 适用范围\n\n待补充项目、时间窗与问题。\n\n## 知识内容\n\n待补充；本条为候选，不能作为已确认口径。\n\n## 证据与待确认项\n\n记录原话或来源，并明确缺失的验证。"
        path = inside(root, f"knowledge/{args.project}/{args.id}.md")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(encode(meta, body))
        print(dump({"created": path.relative_to(root).as_posix(), "status": "draft", "next": "补充正文与来源后运行 index 和 check"}), end="")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(dump({"error": str(exc)}), end="")
        sys.exit(2)
