Language: [Tiếng Việt](./README.md) | English

# glm-toolbox

A small Python command-line toolkit, **standard library only** — no `pip install` required at all.

## Scripts

### 1. `organize.py` — folder cleanup

Sorts the files in a directory into type-based subdirectories: `images/`, `documents/`, `archives/`, `audio/`, `video/`, `code/`, `others/`. Files with duplicate names are automatically renamed to `tên_1.ext` instead of being overwritten.

```bash
python organize.py ~/Downloads --dry-run   # preview, no files moved
python organize.py ~/Downloads             # actually sort
```

### 2. `rename_seq.py` — bulk renaming

Renames files with sequential numbers, keeps the original extensions, and automatically avoids names that already exist.

```bash
python rename_seq.py ~/Pictures --prefix trip_ --start 1 --width 3
# => trip_001.jpg, trip_002.png, ...
```

### 3. `checksum.py` — SHA-256 manifest

Creates and verifies manifest files to check data integrity (format compatible with `sha256sum`).

```bash
python checksum.py file1.zip file2.zip > SHA256SUMS   # create manifest
python checksum.py --check SHA256SUMS                  # verify, exit code 1 on mismatch/missing
```

## CI

On every push, GitHub Actions runs a compile check (`py_compile`) over all scripts and smoke-tests all three tools. See [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## License

MIT — see [LICENSE](LICENSE).
