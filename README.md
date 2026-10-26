# ⚔️ mowftee-guild

Bộ **23 skill tiếng Việt** để dùng với Codex hoặc Google Antigravity. Mỗi skill là hướng dẫn Markdown theo một chuyên môn: lập kế hoạch, giao diện, backend, dữ liệu, kiểm thử, vận hành… Một trợ lý có thể lần lượt dùng các góc nhìn đó; không cần dựng đội agent hay hệ thống quản lý riêng.

## Cài và gỡ

```bash
git clone https://github.com/mowfteedev/mowftee-guild.git
cd mowftee-guild

# Codex
./setup.sh install codex
./setup.sh uninstall codex

# Google Antigravity App/IDE
./setup.sh install antigravity
./setup.sh uninstall antigravity
```

Antigravity CLI dùng `./setup.sh install antigravity-cli` và `./setup.sh uninstall antigravity-cli`. Bỏ tên công cụ thì mặc định Antigravity App/IDE. Script chỉ cần Bash và các lệnh chép/xóa thông thường, không cần Python, pip hay npm.

**Cập nhật:** sửa file trong repo hoặc kéo bản mới về, rồi chạy lại lệnh `install`. Lệnh này thay bản đã chép bằng nội dung hiện tại. Thư mục trùng tên từ nguồn khác được giữ nguyên; script báo vị trí để anh tự xem lại. Xem [chi tiết cài đặt](docs/installation.md).

## Gọi skill để dùng

Trong Codex, gọi như `$backend`, `$frontend`, `$tester` hoặc chọn từ `/skills`. Trong Antigravity App, gọi như `/backend`. Ví dụ:

```text
Dùng $backend để sửa lỗi tạo đơn hàng bị lặp khi gửi lại request.
Đọc code hiện tại, sửa trong phạm vi liên quan và kiểm tra lại kết quả.
```

Chỉ gọi skill phù hợp đầu việc. Không bắt buộc chạy đủ quy trình, tạo báo cáo hay có người duyệt khác. Skill vẫn cần làm rõ điều chưa biết, kiểm chứng kết quả thật và tôn trọng phạm vi anh đã yêu cầu.

👉 [Danh sách 23 skill và vai trò](docs/skills-catalog.md) · [Ví dụ sử dụng](docs/usage.md)

## Nội dung trong repo

- `skills/`: `SKILL.md` và runbook chuyên môn; đây là phần được chép vào host.
- `workflows/`: các trình tự tham khảo cho MVP, tính năng mới, sửa lỗi, review, vận hành. Dùng khi thấy hữu ích.
- `templates/memory/`: mẫu ghi chú dự án tùy chọn, có thể copy và điền bằng tay khi cần lưu kiến trúc hoặc tiến độ.
- `setup.sh`: chép vào và gỡ ra. Không có manifest, profile, hash database, transaction hay dịch vụ chạy nền.

Độ chi tiết nằm trong kiến thức và cách làm việc của skill. Các tài liệu phụ không phải thủ tục bắt buộc để sử dụng. Plugin/MCP chưa nằm trong bản này.

`SKILL.md` giữ phạm vi, quy tắc cốt lõi và đầu ra. Mỗi `references/runbook.md` có bảng quyết định và một ví dụ cụ thể để chọn cách xử lý, kiểm lỗi và nhận biết giới hạn. Ví dụ: [hai request tranh sản phẩm cuối](skills/backend/references/runbook.md), [kết quả tìm kiếm trả sai thứ tự](skills/frontend/references/runbook.md), [đổi cột khi app cũ vẫn chạy](skills/migration-specialist/references/runbook.md). Đây là hướng dẫn minh họa, không phải kết quả benchmark hành vi của trợ lý.

## Tài liệu và kiểm tra

[Nguyên tắc sử dụng](docs/protocol.md) · [Thay đổi từ bản quản lý cũ](docs/migration-v2.md) · [Nguồn tham khảo](docs/sources.md) · [Kiểm chứng](docs/verification.md) · [Changelog](CHANGELOG.md)

Để kiểm tra script khi chỉnh sửa repo:

```bash
bash -n setup.sh
python3 -m unittest discover -s tests -v
```

Python chỉ dùng cho bộ test phát triển, không cần khi cài/gỡ. Mã và nội dung gốc phát hành theo [MIT License](LICENSE). Repo giữ một bản license ở gốc; script chép bản đó thành `LICENSE.txt` trong mỗi skill được cài. Nếu chép riêng một skill bằng tay để chia sẻ, chép kèm `LICENSE` vào thư mục đó.
