#!/usr/bin/env python3
"""organize.py — Sắp xếp file trong một thư mục vào các thư mục con theo loại.

Ví dụ:
    python organize.py ~/Downloads            # sắp xếp thật
    python organize.py ~/Downloads --dry-run  # chỉ xem trước, không di chuyển
"""
import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tiff", ".ico"},
    "documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md", ".csv", ".rtf"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"},
    "audio": {".mp3", ".wav", ".flac", ".ogg", ".m4a"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".webm"},
    "code": {".py", ".js", ".ts", ".java", ".c", ".cpp", ".go", ".rs", ".sh", ".html", ".css", ".json", ".yaml", ".yml"},
}


def category_for(suffix: str) -> str:
    return next((cat for cat, exts in CATEGORIES.items() if suffix in exts), "others")


def unique_target(target_dir: Path, name: str) -> Path:
    """Trả về đường dẫn không trùng: tên_1.ext, tên_2.ext ..."""
    target = target_dir / name
    i = 1
    while target.exists():
        target = target_dir / f"{Path(name).stem}_{i}{Path(name).suffix}"
        i += 1
    return target


def organize(root: Path, dry_run: bool) -> int:
    moved = 0
    for item in sorted(root.iterdir()):
        if not item.is_file() or item.name.startswith("."):
            continue
        target_dir = root / category_for(item.suffix.lower())
        target = unique_target(target_dir, item.name)
        print(f"{'[dry-run] ' if dry_run else ''}{item.name} -> {target_dir.name}/{target.name}")
        if not dry_run:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
        moved += 1
    return moved


def main() -> None:
    p = argparse.ArgumentParser(description="Sắp xếp file theo loại vào thư mục con.")
    p.add_argument("folder", type=Path, help="Thư mục cần sắp xếp")
    p.add_argument("--dry-run", action="store_true", help="Chỉ in ra kết quả, không di chuyển file")
    args = p.parse_args()
    if not args.folder.is_dir():
        raise SystemExit(f"Không tìm thấy thư mục: {args.folder}")
    n = organize(args.folder.resolve(), args.dry_run)
    print(f"\n{'Sẽ di chuyển' if args.dry_run else 'Đã di chuyển'} {n} file.")


if __name__ == "__main__":
    main()
