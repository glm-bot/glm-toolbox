#!/usr/bin/env python3
"""rename_seq.py — Đổi tên hàng loạt file trong thư mục theo số thứ tự.

Ví dụ:
    python rename_seq.py ~/Pictures --prefix trip_ --start 1 --width 3
      => trip_001.jpg, trip_002.png, ...
"""
import argparse
from pathlib import Path


def new_name(prefix: str, n: int, width: int, suffix: str) -> str:
    return f"{prefix}{n:0{width}d}{suffix}"


def main() -> None:
    p = argparse.ArgumentParser(description="Đổi tên file hàng loạt theo số thứ tự.")
    p.add_argument("folder", type=Path, help="Thư mục chứa file cần đổi tên")
    p.add_argument("--prefix", default="file_", help="Tiền tố tên mới (mặc định: file_)")
    p.add_argument("--start", type=int, default=1, help="Số bắt đầu (mặc định: 1)")
    p.add_argument("--width", type=int, default=3, help="Số chữ số của phần số (mặc định: 3)")
    p.add_argument("--dry-run", action="store_true", help="Chỉ in ra kết quả, không đổi tên")
    args = p.parse_args()
    if not args.folder.is_dir():
        raise SystemExit(f"Không tìm thấy thư mục: {args.folder}")

    files = sorted(f for f in args.folder.iterdir() if f.is_file() and not f.name.startswith("."))
    n = args.start
    for f in files:
        target = f.with_name(new_name(args.prefix, n, args.width, f.suffix.lower()))
        # Né tên đã tồn tại (trừ chính nó)
        while target.exists() and target != f:
            n += 1
            target = f.with_name(new_name(args.prefix, n, args.width, f.suffix.lower()))
        print(f"{'[dry-run] ' if args.dry_run else ''}{f.name} -> {target.name}")
        if not args.dry_run and target != f:
            f.rename(target)
        n += 1


if __name__ == "__main__":
    main()
