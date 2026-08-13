#!/usr/bin/env python3
from pathlib import Path

from repository import validate_repository

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    findings = validate_repository(ROOT)
    if findings:
        print("Validation failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Validated 22 Claude web skills with no findings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
