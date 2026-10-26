# Kiểm tra bản dùng cá nhân

Ngày kiểm tra: 26/10/2026, local Linux. Phạm vi: script Bash chép/gỡ, định dạng và tài liệu Markdown của bộ 24 skill. Các thao tác thử dùng HOME tạm, không cài vào tài khoản thật.

| Kiểm tra | Kết quả |
| --- | --- |
| `bash -n setup.sh` | Hợp lệ |
| `python3 -m unittest discover -s tests -v` | 11 tests, OK |
| Validator định dạng từ skill-creator | 24/24 SKILL.md hợp lệ |
| Liên kết file trong Markdown | Các đích file đều tồn tại trong lần kiểm tra |
| `git diff --check` | Không có lỗi whitespace được phát hiện |

Các test ở [tests/test_setup.py](../tests/test_setup.py) kiểm: chép đúng nội dung cho ba host, cập nhật bản đã chép, gỡ cả skill cũ có dấu nhận biết, giữ file từ nguồn khác, xử lý symlink và bảo vệ repo nguồn. Bản cài phải mang đúng LICENSE gốc, giữ license riêng nếu có, và không thay bản đã cài khi thiếu LICENSE nguồn. Chạy lại các lệnh trên nếu sửa script.

Python chỉ phục vụ test phát triển. Người dùng cài/gỡ chỉ cần Bash và các lệnh file thông thường. Kết quả của CLI quản lý đã bỏ không dùng làm bằng chứng cho bản hiện tại.

[GitHub Actions](https://github.com/mowfteedev/mowftee-guild/actions) chạy cùng bộ test trên Ubuntu và macOS. Xem trạng thái từng lần push trực tiếp tại đó.

## Các điểm đã đối chiếu trong đợt tối ưu

- Quickstart cũ clone `main`. Đã thử `./setup.sh install codex` trên snapshot `15d7332` của `origin/main`: exit code 0 nhưng chép 10 skill vào Antigravity, không có bản Codex mong đợi. Hướng dẫn hiện chỉ rõ nhánh review chứa 24 skill.
- Quy tắc loại lỗi import/runner đã được tự rà lại theo hai tình huống: nó là triệu chứng mục tiêu, hoặc là lỗi khác chặn ca kiểm tra. Việc đối chiếu này là rà nội dung, chưa phải chạy yêu cầu debug qua model độc lập.
- Workflow và mẫu ghi chú có mục lục cùng liên kết tới file hiện có. Mẫu kết quả chưa điền số đo/PASS; mục người nhận chỉ dùng khi có nhu cầu thật.
- Tài liệu plugin phân biệt phần minh họa với chức năng hiện có. Chưa có manifest, gói plugin được cài hoặc kiểm thử plugin trong đợt này.

Đây là tự kiểm của người triển khai. Kiểm định dạng và test cài/gỡ không chứng minh chất lượng hành vi của 24 skill. Các ví dụ chuyên môn là minh họa, không phải transcript đã chạy hoặc benchmark độc lập.
