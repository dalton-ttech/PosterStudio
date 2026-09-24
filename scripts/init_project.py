#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a local PosterStudio project.")
    parser.add_argument("project_code", help="Short code such as ZQJ")
    parser.add_argument("--brand", default="", help="Brand name")
    parser.add_argument("--root", default="private/projects", help="Local project root")
    args = parser.parse_args()

    stamp = datetime.now().strftime("%Y%m%d")
    project_dir = Path(args.root) / f"{stamp}-{args.project_code.upper()}"
    dirs = [
        "00-brief",
        "01-research",
        "02-reference",
        "03-generation",
        "04-review",
        "05-revisions",
        "06-final",
    ]
    for name in dirs:
        (project_dir / name).mkdir(parents=True, exist_ok=True)

    project = {
        "project_code": args.project_code.upper(),
        "brand": args.brand,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "status": "research",
        "selected_references": [],
        "generations": [],
        "selected_output": None,
    }
    (project_dir / "project.json").write_text(
        json.dumps(project, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(project_dir.resolve())


if __name__ == "__main__":
    main()
