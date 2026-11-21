#!/usr/bin/env python3
"""checksum.py — Tạo / kiểm tra file manifest SHA-256 (định dạng sha256sum).

Tạo manifest:  python checksum.py file1 file2 ... > SHA256SUMS
Kiểm tra:      python checksum.py --check SHA256SUMS
"""
import argparse
import hashlib
import sys
from pathlib import Path


def hash_file(path: Path, algo: str = "sha256", chunk: int = 1 << 20) -> str:
    h = hashlib.new(algo)
    with path.open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def check(manifest: Path) -> int:
    ok = bad = missing = 0
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, _, name = line.partition("  ")
        path = Path(name)
        if not path.exists():
            print(f"MISSING  {name}")
            missing += 1
        elif hash_file(path) == digest:
            print(f"OK       {name}")
            ok += 1
        else:
            print(f"FAILED   {name}")
            bad += 1
    print(f"\n{ok} ok, {bad} sai, {missing} thiếu")
    return 1 if (bad or missing) else 0


def main() -> None:
    p = argparse.ArgumentParser(description="Tạo / kiểm tra manifest SHA-256.")
    p.add_argument("files", nargs="*", type=Path, help="Các file cần băm")
    p.add_argument("--check", type=Path, metavar="MANIFEST", help="File manifest cần kiểm tra")
    args = p.parse_args()

    if args.check:
        sys.exit(check(args.check))

    if not args.files:
        p.error("hãy cung cấp file cần băm, hoặc dùng --check")
    for f in args.files:
        print(f"{hash_file(f)}  {f}")


if __name__ == "__main__":
    main()
