# Chuyển sang bản dùng cá nhân

Bản đầu của v2 đã thêm quá nhiều quản lý quanh một bộ file Markdown. Theo nhu cầu dùng một mình, repo đã được rút gọn:

- Bản hiện tại có 24 skill và runbook đi kèm, gồm `systematic-debugging` bổ sung sau lần rút gọn.
- Chỉ dùng `setup.sh install [tool]` và `setup.sh uninstall [tool]`.
- Bỏ CLI Python, catalog/profile, manifest/hash, transaction, bộ đăng ký đánh giá và metadata UI tùy chọn.
- Không bắt buộc reviewer khác, quality gate, bộ hồ sơ dự án hoặc số vòng sửa cố định.

Ví dụ: `./setup.sh install codex`. Cài lại để cập nhật; không cần chọn profile hoặc force.

Nếu đã copy/cài bằng script cũ, thư mục skill có thể chưa có tệp nhận biết `.mowftee-guild`. Script mới giữ nguyên bản đó và báo trùng tên. Tự xem lại, giữ nội dung tùy chỉnh cần thiết rồi bỏ hoặc đổi tên bản cũ trước khi cài. Metadata của bộ quản lý cũ, nếu có, không còn được đọc hay sửa bởi script này.

Lần rút gọn ban đầu chỉ chép/gỡ skill. Bản hiện tại bổ sung [plugin 0.1.0](plugins.md) dùng chung nội dung, có thể cài qua host; cách cài Bash vẫn giữ nguyên. Không cần MCP server cho bộ skill này.
