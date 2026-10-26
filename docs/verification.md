# Kiểm tra bản dùng cá nhân

Ngày kiểm tra: 26/10/2026, local Linux. Phạm vi: script Bash chép/gỡ và cấu trúc file Markdown. Các thao tác thử dùng HOME tạm, không cài vào tài khoản thật.

| Kiểm tra | Kết quả |
| --- | --- |
| `bash -n setup.sh` | Hợp lệ |
| `python3 -m unittest discover -s tests -v` | 11 tests, OK |
| Validator định dạng từ skill-creator | 24/24 SKILL.md hợp lệ |
| Liên kết file trong Markdown | Không có link file bị hỏng trong lần kiểm tra |
| `git diff --check` | Không có lỗi whitespace được phát hiện |

Các test ở [tests/test_setup.py](../tests/test_setup.py) kiểm: chép đúng nội dung cho ba host, cập nhật bản đã chép, gỡ cả skill cũ có dấu nhận biết, giữ file từ nguồn khác, xử lý symlink và bảo vệ repo nguồn. Bản cài phải mang đúng LICENSE gốc, giữ license riêng nếu có, và không thay bản đã cài khi thiếu LICENSE nguồn. Chạy lại các lệnh trên nếu sửa script.

Python chỉ phục vụ test phát triển. Người dùng cài/gỡ chỉ cần Bash và các lệnh file thông thường. Bộ test của CLI quản lý cũ đã được bỏ cùng CLI đó; kết quả 40/47 test trước đây không dùng để chứng minh bản rút gọn.

[GitHub Actions](https://github.com/mowfteedev/mowftee-guild/actions) chạy cùng bộ test trên Ubuntu và macOS. Xem trạng thái từng lần push trực tiếp tại đó.

Đây là tự kiểm của người triển khai. Chất lượng nội dung cần tiếp tục thử bằng yêu cầu thật trên host; repo không tuyên bố đã benchmark độc lập hoặc chứng nhận hành vi agent.

Đợt bổ sung chiều sâu đã đọc lại entrypoint/runbook của 23 skill, rút phần hướng dẫn chung lặp và thêm ví dụ riêng cho từng vai trò. Ví dụ nêu dữ kiện cần xem, cách chọn phương án và cách kiểm kết quả; đây là minh họa chuyên môn, chưa phải transcript thực thi hay kết quả đánh giá hành vi.

Đợt sửa lỗi có bằng chứng thêm `systematic-debugging`, đưa bộ skill lên 24 và đồng bộ workflow, tester, code-reviewer, test-automator. Đã kiểm định dạng 24 skill, liên kết file và chạy lại 11 test cài/gỡ với bộ skill hiện tại. Việc đọc lại hướng dẫn trước/sau và giới hạn kết luận là tự rà nội dung; chưa phải thử hành vi trên một yêu cầu debug thực tế.
