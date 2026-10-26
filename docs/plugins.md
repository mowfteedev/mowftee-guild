# Plugin cho mowftee-guild

Plugin **mowftee-guild 0.1.0** đóng gói 24 skill và runbook hiện có. Đã thử bằng Codex CLI 0.164.0 và Antigravity CLI 1.4.7 trên Linux. Không có MCP server, hooks hoặc kết nối tài khoản đi kèm. Cách chép skill bằng `setup.sh` vẫn dùng được.

## Ba thành phần khác nhau

| Thành phần | Chứa gì | Vai trò |
| --- | --- | --- |
| Skill | `SKILL.md`, tài liệu tham chiếu và tài nguyên cần thiết | Hướng dẫn trợ lý chọn cách làm, kiểm kết quả và xử lý giới hạn. |
| Plugin | Manifest cùng các skill hoặc kết nối được đóng gói | Cho host nhận diện, cài và bật/tắt một bộ khả năng. |
| MCP server | Công cụ có schema đầu vào/đầu ra và cách truy cập dữ liệu | Cung cấp khả năng gọi dịch vụ, lấy dữ liệu hiện thời hoặc thực hiện hành động được kiểm soát. |

Plugin có thể chỉ chứa skill; MCP là phần thêm khi công việc cần công cụ/server. Bộ này được thiết kế để dùng với các công cụ sẵn có của host nên chưa cần server riêng. Đóng gói cũng không tự chứng minh trợ lý tuân thủ hướng dẫn. [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins).

## Cài trên Codex

Trong thư mục repo đã clone nhánh `main`, hoặc thư mục đã giải nén gói ZIP:

```bash
codex plugin marketplace add .
codex plugin add mowftee-guild@mowftee-guild-marketplace
codex plugin list --marketplace mowftee-guild-marketplace --json
```

Kết quả cần có plugin đúng tên/phiên bản, `installed: true`, `enabled: true`. Mở phiên mới, chọn từ `/skills` hoặc gọi tên đã có namespace:

```text
Dùng $mowftee-guild:systematic-debugging điều tra lỗi này.
Tái hiện, xác minh nguyên nhân, sửa tối thiểu rồi kiểm cùng ca và hồi quy liên quan.
```

`/plugins` mở trình quản lý; dùng lựa chọn bật/tắt của host. Muốn gỡ gói và bỏ nguồn cài của Guild:

```bash
codex plugin remove mowftee-guild@mowftee-guild-marketplace
codex plugin marketplace remove mowftee-guild-marketplace
```

Các lệnh này chỉ nhắm plugin và nguồn có tên trên, không xóa repo. Xem [OpenAI Docs: plugin packaging](https://developers.openai.com/plugins/build/plugins) và [plugin browser](https://learn.chatgpt.com/docs/plugins).

## Cài trên Antigravity

Tại thư mục repo hoặc gói đã giải nén:

```bash
agy plugin install .
agy plugin list --json
```

Danh sách cần có `mowftee-guild`, `enabled: true` và đủ 24 tên skill. Mở phiên mới và chọn skill bằng menu/autocomplete của host; hoặc yêu cầu dùng skill `systematic-debugging` của plugin `mowftee-guild`.

```bash
agy plugin disable mowftee-guild
agy plugin enable mowftee-guild
agy plugin uninstall mowftee-guild
```

Trong App, xem gói ở Customizations/Installed. Kiểm thử tự động tại đây dùng CLI, chưa xác nhận giao diện App/IDE. [Google Antigravity Docs: plugins](https://www.antigravity.google/docs/plugins?tab=cli).

## Cập nhật hoặc đổi cách cài

Host dùng bản đã cài trong cache/profile, không đọc mọi chỉnh sửa ở repo ngay lập tức. Giữ tùy chỉnh trong repo trước khi cài lại.

- Cập nhật repo bằng `git pull --ff-only` khi đang ở đúng nhánh, hoặc lấy gói ZIP mới.
- Codex: gỡ riêng plugin Guild rồi chạy lại `codex plugin add mowftee-guild@mowftee-guild-marketplace`. Nếu đổi thư mục nguồn, gỡ nguồn `mowftee-guild-marketplace` rồi đăng ký đường dẫn mới trước khi cài.
- Antigravity: gỡ riêng `mowftee-guild` rồi cài lại bằng `agy plugin install` với đường dẫn nguồn đã cập nhật.
- Mở phiên mới và kiểm lại phiên bản, trạng thái và danh sách skill. Không sửa trực tiếp file trong cache host.

Nếu đang dùng bản chép bởi `setup.sh`, giữ các tùy chỉnh cần thiết rồi gỡ bản chép của đúng công cụ trước khi chuyển sang plugin. Script giữ nguyên thư mục từ nguồn khác hoặc bản cũ không có dấu nhận biết; không tự xóa chúng chỉ để cài plugin.

## Tạo và lấy gói ZIP

Người cài từ bản clone không cần bước build. Khi muốn chia sẻ một gói gọn, dùng Python 3.9 trở lên, không cần package bổ sung:

```bash
python3 scripts/package_plugin.py
```

Đầu ra hiện tại: `dist/mowftee-guild-0.1.0.zip`. Giải nén vào một thư mục rồi dùng các lệnh cài ở trên tại đó. CI cũng tạo cùng gói: vào GitHub Actions, mở lần chạy thành công của **Check skills and plugin package**, tải artifact **mowftee-guild-plugin**; bên trong có ZIP của plugin.

Gói mang `plugin.json`, LICENSE, mục đăng ký Codex và các file của skill; loại khỏi gói `.git`, tài liệu workflow, mẫu ghi chú và công cụ build. Nội dung skill có một nguồn trong repo, không có bộ skill thứ hai để đồng bộ.

Có thể kiểm gói đã giải nén bằng `agy plugin validate /duong/dan/plugin --strict --json`. Khi kiểm trực tiếp cả repo, Antigravity có thể nhắc rằng thư mục `workflows/` không được nạp như thành phần plugin; các workflow đó là tài liệu tham khảo như đã mô tả.

## Phạm vi đã kiểm

- 13 test Python: cài/gỡ bằng Bash, nội dung ZIP, tài nguyên liên kết ngoài và việc giữ file không thuộc gói.
- Codex: cài/gỡ qua CLI; app-server trả đủ 24 skill có namespace và tài liệu cùng gói; bật/tắt qua cấu hình native trong profile tạm.
- Antigravity CLI: validate strict gói sạch, cài/gỡ, đủ 24 skill, bật/tắt và nội dung runbook.

Các kiểm tra này xác nhận đóng gói và khám phá skill. Chưa phải benchmark chất lượng trả lời của model, và chưa phát hành lên danh mục plugin công khai.
