# Changelog

## Bổ sung chiều sâu nội dung — 2026-10-26

- Thêm ví dụ xử lý cụ thể cho cả 23 chuyên môn: dữ kiện cần đọc, cách chọn phương án, lỗi dễ gặp và cách kiểm lại.
- Rút quy tắc chung lặp trong entrypoint; chỉ dẫn rõ tình huống nào nên mở runbook. Không thêm bước quản lý hay công cụ cài đặt.
- Giữ một LICENSE gốc trong repo; script chép kèm vào bản cài, giữ license riêng nếu skill có. Khi chép/chia sẻ bằng tay cần mang theo license.
- Kiểm bản cài có nội dung license đúng; thiếu license nguồn thì dừng trước khi thay bản đã cài.

## Bản dùng cá nhân — 2026-10-26

- Giữ 23 skill chuyên môn, mỗi skill có hướng dẫn và runbook tự chứa.
- Rút phần cài/gỡ về một script Bash chép/xóa thư mục, hỗ trợ Codex và Antigravity.
- Bỏ CLI Python, catalog, profile, manifest, hash, transaction và dịch vụ quản lý không cần thiết.
- Bỏ metadata UI tùy chọn và bộ đăng ký behavioral eval. Không tuyên bố skill đã được benchmark độc lập.
- Diễn đạt lại vai trò cho một người dùng với cùng trợ lý; bỏ yêu cầu reviewer riêng, cổng duyệt và số vòng sửa cứng.
- Giữ workflow và mẫu memory dưới dạng tài liệu tùy chọn.
- Script giữ thư mục từ nguồn khác, không ghi qua symlink và không thay hoặc gỡ chính repo nguồn.

## Bản mở rộng ban đầu

Mở từ 10 lên 23 góc nhìn chuyên môn: phân tích, kiến trúc, API, UI/UX, lập trình, dữ liệu, kiểm thử, bảo mật, hiệu năng, vận hành và tài liệu. Nội dung tham khảo được ghi ở [sources](docs/sources.md).
