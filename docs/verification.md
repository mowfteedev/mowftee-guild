# Kiểm tra bản dùng cá nhân

Ngày kiểm tra: 26/10/2026, local Linux. Phạm vi: script Bash chép/gỡ, gói plugin, định dạng và tài liệu của bộ 24 skill. Các ca thử cài/gỡ và bật/tắt dùng HOME/profile tạm; sau đó đã cài plugin vào profile làm việc và xác nhận trạng thái.

| Kiểm tra | Kết quả |
| --- | --- |
| `bash -n setup.sh` | Hợp lệ |
| `python3 -m unittest discover -s tests -v` | 13 tests, OK |
| Validator định dạng từ skill-creator | 24/24 SKILL.md hợp lệ |
| Liên kết file trong Markdown | Các đích file đều tồn tại trong lần kiểm tra |
| `git diff --check` | Không có lỗi whitespace được phát hiện |
| `python3 scripts/package_plugin.py` | Tạo ZIP chứa manifest, LICENSE, mục đăng ký và đủ 24 skill/runbook |
| Codex CLI 0.164.0 | Cài/gỡ, khám phá 24 skill có namespace, runbook và bật/tắt qua API cấu hình native trong profile tạm |
| Antigravity CLI 1.4.7 | Validate strict gói sạch, cài/gỡ, bật/tắt và liệt kê đủ 24 skill |

Các test ở [tests/test_setup.py](../tests/test_setup.py) kiểm: chép đúng nội dung cho ba host, cập nhật bản đã chép, gỡ cả skill cũ có dấu nhận biết, giữ file từ nguồn khác, xử lý symlink và bảo vệ repo nguồn. Bản cài phải mang đúng LICENSE gốc, giữ license riêng nếu có, và không thay bản đã cài khi thiếu LICENSE nguồn.

Hai test ở [test_plugin_package.py](../tests/test_plugin_package.py) kiểm nội dung ZIP khớp nguồn, giữ LICENSE và mục đăng ký; loại các file repo/scratch nằm ngoài phần tài nguyên chọn đóng gói, từ chối tài nguyên liên kết ra ngoài. Đây không phải bộ quét secret tổng quát. Các kiểm tra host native ở bảng trên được chạy riêng tại local, không nằm trong 13 test Python.

Python chỉ phục vụ test và tạo ZIP. Người dùng cài plugin cần CLI/host hỗ trợ, hoặc dùng Bash để chép skill theo cách cũ. Kết quả của CLI quản lý đã bỏ không dùng làm bằng chứng cho bản hiện tại.

[GitHub Actions](https://github.com/mowfteedev/mowftee-guild/actions) chạy 13 test Python trên Ubuntu và macOS, build gói ZIP và đính kèm artifact từ job Linux. Các job này không cài Codex/Antigravity hoặc chạy model; xem trạng thái từng lần push trực tiếp tại đó.

## Các điểm đã đối chiếu trong đợt tối ưu

- Quickstart cũ từng clone bản `main` ở snapshot `15d7332`: thử `./setup.sh install codex` trả exit code 0 nhưng chép 10 skill vào Antigravity, không có bản Codex mong đợi. Bản 24 skill/plugin nay được đưa vào `main`, và hướng dẫn clone đã trở về nhánh chính.
- Quy tắc loại lỗi import/runner đã được tự rà lại theo hai tình huống: nó là triệu chứng mục tiêu, hoặc là lỗi khác chặn ca kiểm tra. Việc đối chiếu này là rà nội dung, chưa phải chạy yêu cầu debug qua model độc lập.
- Workflow và mẫu ghi chú có mục lục cùng liên kết tới file hiện có. Mẫu kết quả chưa điền số đo/PASS; mục người nhận chỉ dùng khi có nhu cầu thật.
- Plugin 0.1.0 có manifest thật và gói ZIP đã thử. Kiểm profile làm việc sau cài cho thấy 24 skill được bật trên Codex và Antigravity liệt kê đủ 24 skill; nội dung bản cài được đối chiếu với ZIP.

Đây là tự kiểm của người triển khai. Kiểm định dạng, đóng gói, khám phá skill và cài/gỡ không chứng minh chất lượng trả lời của 24 skill. Chưa kiểm giao diện App/IDE, chưa chạy benchmark model và chưa phát hành lên danh mục plugin công khai.
