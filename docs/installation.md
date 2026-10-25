# Cài, cập nhật và gỡ

## Cách dùng

```bash
./setup.sh install codex
./setup.sh uninstall codex

./setup.sh install antigravity
./setup.sh uninstall antigravity

./setup.sh install antigravity-cli
./setup.sh uninstall antigravity-cli
```

Chạy không tham số hoặc `--help` để xem cách dùng. Không truyền tên công cụ thì mặc định Antigravity App/IDE. Không có profile, dry-run, init hoặc CLI riêng.

## Các thư mục được chép tới

| Công cụ | Nơi cài |
| --- | --- |
| Codex | `~/.agents/skills/` |
| Antigravity App/IDE | `~/.gemini/config/skills/` |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills/` |

Đối chiếu [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills) và [Google Antigravity Docs](https://antigravity.google/docs/skills). Script chép mỗi thư mục trong `skills/` vào nơi tương ứng, giữ `SKILL.md` và runbook đi kèm. Chép xong có thể gọi skill theo cách của host.

## Cập nhật

Chỉnh nội dung ở bản repo rồi chạy lại `install`. Bản đã chép sẽ được thay thế, gồm cả tài liệu đi kèm. Nếu cần tùy chỉnh, sửa ở repo để lần cài sau giữ đúng nội dung anh muốn.

Mỗi thư mục do script chép có một tệp trống `.mowftee-guild` để nhận biết khi gỡ. Đây chỉ là dấu đánh dấu cục bộ; không có registry, hash hay trạng thái cần quản lý. `uninstall` gỡ những thư mục có dấu này, kể cả skill đã bỏ khỏi repo sau một lần cập nhật. Các thư mục khác được giữ nguyên.

Nếu có thư mục trùng tên nhưng không có dấu nhận biết, script dừng trước khi thay skill nào và báo đường dẫn. Anh có thể tự kiểm tra bản cũ trước khi xóa hoặc đổi tên. Script không ghi qua symlink và không thay hoặc gỡ chính repo nguồn.

## Giới hạn đơn giản

Đây là thao tác chép/xóa thông thường: không tự backup, không rollback nguyên tử khi máy tắt giữa chừng. Nếu chép lỗi, lệnh trả lỗi; sửa nguyên nhân rồi cài lại hoặc gỡ bản đang chép dở. Không tự cài package, sửa cấu hình host hay tạo file trong dự án đang làm.

Các workflow và mẫu memory vẫn nằm trong bản clone, chỉ dùng khi cần; chúng không được tự đăng ký như plugin hoặc slash command.
