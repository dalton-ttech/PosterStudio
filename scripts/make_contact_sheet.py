#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a simple local review contact sheet.")
    parser.add_argument("input_dir")
    parser.add_argument("output")
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--thumb-width", type=int, default=360)
    parser.add_argument("--label-height", type=int, default=36)
    args = parser.parse_args()

    files = [
        p for p in sorted(Path(args.input_dir).iterdir())
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS
    ]
    if not files:
        raise SystemExit("No images found.")

    thumbs = []
    max_h = 0
    for path in files:
        with Image.open(path) as im:
            img = im.convert("RGB")
            scale = args.thumb_width / img.width
            h = max(1, round(img.height * scale))
            img = img.resize((args.thumb_width, h), Image.Resampling.LANCZOS)
            thumbs.append((path, img))
            max_h = max(max_h, h)

    cols = max(1, args.columns)
    rows = math.ceil(len(thumbs) / cols)
    gap = 20
    cell_w = args.thumb_width
    cell_h = max_h + args.label_height
    canvas_w = gap + cols * (cell_w + gap)
    canvas_h = gap + rows * (cell_h + gap)

    sheet = Image.new("RGB", (canvas_w, canvas_h), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for i, (path, img) in enumerate(thumbs):
        row, col = divmod(i, cols)
        x = gap + col * (cell_w + gap)
        y = gap + row * (cell_h + gap)
        sheet.paste(img, (x, y))
        draw.text((x, y + max_h + 8), path.stem, fill="black", font=font)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=92)
    print(out.resolve())


if __name__ == "__main__":
    main()
