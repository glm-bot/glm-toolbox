# glm-toolbox

Bộ công cụ dòng lệnh nhỏ bằng Python, **chỉ dùng thư viện chuẩn** — không cần `pip install` gì cả.

## Các script

### 1. `organize.py` — dọn dẹp thư mục

Sắp xếp file trong một thư mục vào các thư mục con theo loại: `images/`, `documents/`, `archives/`, `audio/`, `video/`, `code/`, `others/`. File trùng tên sẽ được tự động đổi thành `tên_1.ext` thay vì ghi đè.

```bash
python organize.py ~/Downloads --dry-run   # xem trước, không di chuyển file
python organize.py ~/Downloads             # sắp xếp thật
```

### 2. `rename_seq.py` — đổi tên hàng loạt

Đổi tên file theo số thứ tự, giữ nguyên phần mở rộng, tự né tên file đã tồn tại.

```bash
python rename_seq.py ~/Pictures --prefix trip_ --start 1 --width 3
# => trip_001.jpg, trip_002.png, ...
```

### 3. `checksum.py` — manifest SHA-256

Tạo và kiểm tra file manifest để đối chiếu tính toàn vẹn của dữ liệu (định dạng tương thích với `sha256sum`).

```bash
python checksum.py file1.zip file2.zip > SHA256SUMS   # tạo manifest
python checksum.py --check SHA256SUMS                  # kiểm tra, exit code 1 nếu sai/thiếu
```

## CI

Mỗi lần push, GitHub Actions sẽ biên dịch kiểm tra (`py_compile`) toàn bộ script và chạy smoke test cho cả ba công cụ. Xem [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## Giấy phép

MIT — xem [LICENSE](LICENSE).
