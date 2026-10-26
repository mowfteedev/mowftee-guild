# Changelog

## Thống nhất repo và hướng dẫn sử dụng — 2026-10-26

- Sửa quickstart để clone đúng nhánh review đang chứa 24 skill, tránh chạy script cũ từ `main`.
- Đồng bộ cách ghi bằng chứng trong các skill; nối quy trình debug vào frontend/backend và làm rõ import/runner chỉ là lỗi chặn nếu không thuộc triệu chứng đang điều tra.
- Thêm bảng chọn skill theo mục tiêu, mục lục workflow và mẫu ghi chú; thay đoạn kết lặp bằng tiêu chí theo từng đầu việc.
- Rút các mẫu về thông tin dùng cá nhân, bỏ cột phân vai/reviewer và vòng sửa không cần thiết; đổi `gate-checklist-template.md` thành `self-check-template.md`.
- Viết tài liệu giới thiệu skill, plugin và MCP dựa trên OpenAI Docs; chưa thêm manifest hoặc cài plugin.

## Sửa lỗi có bằng chứng — 2026-10-26

- Thêm skill `systematic-debugging`, đưa tổng số lên 24; chỉ dẫn bốn bước: tái hiện, xác minh nguyên nhân, sửa tối thiểu và kiểm cùng ca, hồi quy liên quan.
- Viết lại workflow sửa lỗi; không tính lỗi môi trường là tái hiện triệu chứng và không dùng ca giả lập để tuyên bố đã xác minh lỗi gốc.
- Thống nhất tester, code-reviewer và test-automator về bằng chứng trước/sau, snapshot và giới hạn kết luận. CI đúng phiên bản dùng được; không bắt chạy lại test ở mọi lượt chat.
- Giữ phần cài/gỡ như hiện tại; thay đổi trong đợt này là nội dung Markdown.

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
