# Chỉnh sửa bộ skill

Chỉnh trực tiếp Markdown trong `skills/<name>/SKILL.md`; giữ tên trong frontmatter khớp thư mục. Tài liệu chuyên sâu đặt trong `references/` cùng skill và link từ entrypoint.

- Mỗi skill cần có chuyên môn và tình huống sử dụng rõ, tránh trùng vai trò.
- Giữ hướng dẫn phù hợp dùng một trợ lý; không thêm quy trình quản lý, người duyệt hoặc công cụ giả định không cần thiết.
- Giữ quyền người dùng và kết quả kiểm chứng thật. Tự kiểm không phải review độc lập, nhưng không bắt buộc review độc lập cho bộ dùng cá nhân.
- Khi thêm skill, cập nhật [danh mục](docs/skills-catalog.md). Script tự đọc các thư mục, không có catalog/profile phải đồng bộ.
- Giữ nguồn tham khảo và license nếu dùng nội dung từ bên ngoài.
- Nội dung gốc dùng bản `LICENSE` ở gốc; không nhân bản vào từng skill trong repo. Script sẽ chép kèm khi cài. Nội dung bên thứ ba có thông báo riêng thì vẫn giữ theo nguồn đó.
- Workflow và mẫu ghi chú cần có mục đích cụ thể, phần kết thúc phù hợp với đầu việc; cập nhật mục lục trong thư mục khi thêm hoặc đổi tên file.
- Khi sửa quy tắc debug, rà cả triệu chứng mục tiêu và lỗi khác có thể chặn ca kiểm tra. Đừng loại một ca hợp lệ chỉ theo tên lỗi như import, timeout hoặc kết nối.

Sau khi chỉnh Markdown, đối chiếu tên trong frontmatter, đường dẫn tài liệu đi kèm và các ví dụ sử dụng với trạng thái repo. Giữ mỗi skill tự chứa phần hướng dẫn cần thiết sau khi chép. Đọc lại nội dung hoặc kiểm định dạng không được báo thành đã thử hành vi của trợ lý.

Kiểm tra khi sửa script cài/gỡ:

```bash
bash -n setup.sh
python3 -m unittest discover -s tests -v
```

Tests chỉ chép/xóa trong HOME tạm. Python là công cụ chạy test, không phải dependency cài skill. Sau khi chỉnh Markdown, cài lại bằng `./setup.sh install codex` hoặc tên host đang dùng.
