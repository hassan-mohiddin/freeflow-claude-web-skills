#!/usr/bin/env python3
import argparse
from pathlib import Path

from repository import build_release

ROOT = Path(__file__).resolve().parents[1]


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build deterministic Freeflow Claude web skill archives."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "dist",
        help="Release output directory (default: ./dist)",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    result = build_release(ROOT, arguments.output_dir)
    print(f"Built {len(result.archives)} archives in {arguments.output_dir.resolve()}")
    print(f"Checksums: {result.checksums}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
