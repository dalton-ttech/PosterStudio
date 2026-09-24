#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image


def fit_crop(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    src_ratio = img.width / img.height
    dst_ratio = target_w / target_h
    if src_ratio > dst_ratio:
        new_h = target_h
        new_w = round(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = round(new_w / src_ratio)
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = max(0, (new_w - target_w) // 2)
    top = max(0, (new_h - target_h) // 2)
    return resized.crop((left, top, left + target_w, top + target_h))


def main() -> None:
    parser = argparse.ArgumentParser(description="Export final poster dimensions.")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--mode", choices=["fit-crop", "resize"], default="fit-crop")
    args = parser.parse_args()

    with Image.open(args.input) as im:
        img = im.convert("RGBA")
        if args.mode == "resize":
            out_img = img.resize((args.width, args.height), Image.Resampling.LANCZOS)
        else:
            out_img = fit_crop(img, args.width, args.height)

        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.suffix.lower() in {".jpg", ".jpeg"}:
            out_img = out_img.convert("RGB")
            out_img.save(out, quality=95)
        else:
            out_img.save(out)

    print(out.resolve())


if __name__ == "__main__":
    main()
