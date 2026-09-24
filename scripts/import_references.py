#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from PIL import Image

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"references": []}


def main() -> None:
    parser = argparse.ArgumentParser(description="Import human-selected reference images.")
    parser.add_argument("project_code", help="e.g. ZQJ")
    parser.add_argument("--style", default="S01", help="Style-family id, e.g. S01")
    parser.add_argument("--inbox", default="private/library/inbox")
    parser.add_argument("--library", default="private/library/references")
    parser.add_argument("--manifest", default="private/library/manifest.json")
    args = parser.parse_args()

    inbox = Path(args.inbox)
    library = Path(args.library)
    manifest_path = Path(args.manifest)
    library.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    inbox.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(manifest_path)
    refs = manifest.setdefault("references", [])
    known_hashes = {x.get("sha256") for x in refs if x.get("sha256")}
    code = args.project_code.upper()

    existing_nums = []
    for item in refs:
        rid = item.get("id", "")
        if rid.startswith(code + "-R"):
            try:
                existing_nums.append(int(rid.split("-R", 1)[1].split("-", 1)[0]))
            except ValueError:
                pass
    next_num = max(existing_nums, default=0) + 1

    imported = 0
    duplicates = 0

    for src in sorted(inbox.iterdir()):
        if not src.is_file() or src.suffix.lower() not in IMAGE_EXTS:
            continue
        sha = digest(src)
        if sha in known_hashes:
            duplicates += 1
            continue

        rid = f"{code}-R{next_num:03d}-{args.style.upper()}"
        dst = library / f"{rid}{src.suffix.lower()}"

        with Image.open(src) as im:
            width, height = im.size

        shutil.copy2(src, dst)
        refs.append(
            {
                "id": rid,
                "filename": dst.name,
                "source": "human-selected",
                "project_code": code,
                "style_family": args.style.upper(),
                "sha256": sha,
                "width": width,
                "height": height,
                "tags": [],
                "notes": "",
                "usage": {"mimic": None, "inspired": None},
            }
        )
        known_hashes.add(sha)
        next_num += 1
        imported += 1

    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"imported": imported, "duplicates_skipped": duplicates}, ensure_ascii=False))


if __name__ == "__main__":
    main()
