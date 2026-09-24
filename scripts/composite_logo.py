#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(description="Composite an exact source logo onto a poster.")
    parser.add_argument("poster")
    parser.add_argument("logo")
    parser.add_argument("output")
    parser.add_argument("--x", type=int, required=True)
    parser.add_argument("--y", type=int, required=True)
    parser.add_argument("--width", type=int, required=True, help="Target logo width in pixels")
    args = parser.parse_args()

    with Image.open(args.poster) as p, Image.open(args.logo) as l:
        poster = p.convert("RGBA")
        logo = l.convert("RGBA")
        scale = args.width / logo.width
        logo = logo.resize((args.width, max(1, round(logo.height * scale))), Image.Resampling.LANCZOS)
        poster.alpha_composite(logo, (args.x, args.y))
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        poster.save(out)
        print(out.resolve())


if __name__ == "__main__":
    main()
