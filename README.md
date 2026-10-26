# ⚔️ mowftee-guild

Bộ **24 skill tiếng Việt** để dùng với Codex hoặc Google Antigravity. Mỗi skill là hướng dẫn Markdown theo một chuyên môn: lập kế hoạch, giao diện, backend, dữ liệu, sửa lỗi, kiểm thử, vận hành… Một trợ lý có thể lần lượt dùng các góc nhìn đó; không cần dựng đội agent hay hệ thống quản lý riêng.

## Cài, cập nhật và gỡ

Bản 24 skill hiện ở nhánh `feat/guild-v2-specialized-skills`; `main` vẫn là bản cũ. Clone đúng nhánh để dùng các lệnh dưới đây:

```bash
git clone --branch feat/guild-v2-specialized-skills --single-branch https://github.com/mowfteedev/mowftee-guild.git
cd mowftee-guild

# Codex
./setup.sh install codex
./setup.sh uninstall codex

# Google Antigravity App/IDE
./setup.sh install antigravity
./setup.sh uninstall antigravity
```

Antigravity CLI dùng `./setup.sh install antigravity-cli` và `./setup.sh uninstall antigravity-cli`. Bỏ tên công cụ thì mặc định Antigravity App/IDE. Script chỉ cần Bash và các lệnh chép/xóa thông thường, không cần Python, pip hay npm.

**Cập nhật:** sửa file trong repo hoặc chạy `git pull --ff-only` ở đúng nhánh, rồi chạy lại `install`. Bản đã cài sẽ được thay bằng nội dung trong repo; giữ tùy chỉnh ở repo trước khi cài lại. Nếu Git báo có thay đổi cục bộ hoặc nhánh phân kỳ, giữ các chỉnh sửa đó và xử lý trước. Thư mục trùng tên từ nguồn khác được giữ nguyên; xem [chi tiết cài đặt](docs/installation.md).

## Gọi skill để dùng

Trong Codex, gọi như `$backend`, `$frontend`, `$tester` hoặc chọn từ `/skills`. Trong Antigravity App, gọi như `/backend`. Ví dụ:

```text
Dùng $systematic-debugging để sửa lỗi tạo đơn hàng bị lặp khi gửi lại request.
Tái hiện trước, xác minh nguyên nhân, sửa tối thiểu rồi kiểm lại cùng ca và hồi quy liên quan.
```

Chỉ gọi skill phù hợp đầu việc; không cần gọi đủ vai trò, tạo báo cáo hay có người duyệt khác. Khi sửa lỗi, giữ [bốn bước kiểm chứng](workflows/04-sua-loi.md) và báo rõ phần chưa làm được. Bằng chứng cần khớp với phiên bản và điều kiện đang kiểm; không kết luận “đã fix” chỉ vì đã đổi code.

👉 [Danh sách 24 skill và vai trò](docs/skills-catalog.md) · [Ví dụ sử dụng](docs/usage.md)

## Nội dung trong repo

- `skills/`: `SKILL.md` và runbook chuyên môn; đây là phần được chép vào host.
- [Workflow](workflows/README.md): chọn trình tự cho MVP, tính năng, bảo trì, sửa lỗi hoặc phát hành.
- [Mẫu ghi chú](templates/memory/README.md): chỉ copy phần hữu ích khi cần lưu; cài skill không tự tạo `.memory/`.
- `setup.sh`: chép vào và gỡ ra. Không có manifest, profile, hash database, transaction hay dịch vụ chạy nền.

Độ chi tiết nằm trong kiến thức và cách làm việc của skill. Các tài liệu phụ không phải thủ tục bắt buộc để sử dụng. Xem [giới thiệu plugin](docs/plugins.md) để hiểu cách đóng gói bộ skill và điểm khác với MCP.

`SKILL.md` giữ phạm vi, quy tắc cốt lõi và đầu ra. Mỗi `references/runbook.md` có bảng quyết định và một ví dụ cụ thể để chọn cách xử lý, kiểm lỗi và nhận biết giới hạn. Ví dụ: [hai request tranh sản phẩm cuối](skills/backend/references/runbook.md), [kết quả tìm kiếm trả sai thứ tự](skills/frontend/references/runbook.md), [đổi cột khi app cũ vẫn chạy](skills/migration-specialist/references/runbook.md). Đây là hướng dẫn minh họa, không phải kết quả benchmark hành vi của trợ lý.

## Tài liệu và kiểm tra

[Nguyên tắc sử dụng](docs/protocol.md) · [Thay đổi từ bản quản lý cũ](docs/migration-v2.md) · [Nguồn tham khảo](docs/sources.md) · [Kiểm chứng](docs/verification.md) · [Changelog](CHANGELOG.md)

Để kiểm tra script khi chỉnh sửa repo:

```bash
bash -n setup.sh
python3 -m unittest discover -s tests -v
```

Python chỉ dùng cho bộ test phát triển, không cần khi cài/gỡ. Mã và nội dung gốc phát hành theo [MIT License](LICENSE). Repo giữ một bản license ở gốc; script chép bản đó thành `LICENSE.txt` trong mỗi skill được cài. Nếu chép riêng một skill bằng tay để chia sẻ, chép kèm `LICENSE` vào thư mục đó.
