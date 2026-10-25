# Kiểm tra bản dùng cá nhân

Ngày kiểm tra: 26/10/2026, local Linux. Phạm vi: script Bash chép/gỡ và cấu trúc file Markdown. Các thao tác thử dùng HOME tạm, không cài vào tài khoản thật.

| Kiểm tra | Kết quả |
| --- | --- |
| `bash -n setup.sh` | Hợp lệ |
| `python3 -m unittest discover -s tests -v` | 9 tests, OK |
| Validator định dạng từ skill-creator | 23/23 SKILL.md hợp lệ |
| Liên kết file trong Markdown | Không có link file bị hỏng trong lần kiểm tra |
| `git diff --check` | Không có lỗi whitespace được phát hiện |

Các test ở [tests/test_setup.py](../tests/test_setup.py) kiểm: chép đúng nội dung cho ba host, cập nhật bản đã chép, gỡ cả skill cũ có dấu nhận biết, giữ file từ nguồn khác, xử lý symlink và bảo vệ repo nguồn. Chạy lại các lệnh trên nếu sửa script.

Python chỉ phục vụ test phát triển. Người dùng cài/gỡ chỉ cần Bash và các lệnh file thông thường. Bộ test của CLI quản lý cũ đã được bỏ cùng CLI đó; kết quả 40/47 test trước đây không dùng để chứng minh bản rút gọn.

[GitHub Actions](https://github.com/mowfteedev/mowftee-guild/actions) chạy cùng bộ test trên Ubuntu và macOS. Xem trạng thái từng lần push trực tiếp tại đó.

Đây là tự kiểm của người triển khai. Chất lượng nội dung cần tiếp tục thử bằng yêu cầu thật trên host; repo không tuyên bố đã benchmark độc lập hoặc chứng nhận hành vi agent.
