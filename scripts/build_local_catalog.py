"""Compatibility entry point for the full review catalog."""
from catalog_review import build
if __name__ == "__main__":
    import argparse,json
    from pathlib import Path
    p=argparse.ArgumentParser();p.add_argument("--root",type=Path,required=True);p.add_argument("--audit",type=Path,required=True);p.add_argument("--evidence",type=Path);a=p.parse_args();print(json.dumps(build(a.root,a.audit,a.evidence),ensure_ascii=False,indent=2))
