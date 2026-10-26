# Plugin cho mowftee-guild

Tài liệu giới thiệu, đối chiếu OpenAI Docs ngày 26/10/2026. Repo hiện cung cấp 24 skill qua script chép/gỡ; các cấu trúc bên dưới là minh họa cho bước đóng gói sau này.

## Ba thành phần khác nhau

| Thành phần | Chứa gì | Vai trò |
| --- | --- | --- |
| Skill | `SKILL.md`, tài liệu tham chiếu và tài nguyên cần thiết | Hướng dẫn trợ lý chọn cách làm, kiểm kết quả và xử lý giới hạn. |
| Plugin | Manifest cùng các skill hoặc kết nối được đóng gói | Cho host nhận diện, cài và bật/tắt một bộ khả năng. |
| MCP server | Công cụ có schema đầu vào/đầu ra và cách truy cập dữ liệu | Cung cấp khả năng gọi dịch vụ, lấy dữ liệu hiện thời hoặc thực hiện hành động được kiểm soát. |

Plugin có thể chỉ chứa skill; MCP là phần thêm khi công việc cần công cụ/server. Bộ này được thiết kế để dùng với các công cụ sẵn có của host nên chưa cần server riêng. Đóng gói cũng không tự chứng minh trợ lý tuân thủ hướng dẫn. [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins).

## Nếu đóng gói bộ hiện tại

Giữ một nguồn `skills/`, thêm manifest nhận diện gói và mang theo LICENSE. Dùng nội dung hiện có; không nhân bản 24 skill sang một bộ khác chỉ để làm plugin. Minh họa dạng Agent Plugins portable:

```text
mowftee-guild/
├── plugin.json       # manifest sẽ bổ sung khi thực hiện đóng gói
├── LICENSE
└── skills/
    └── systematic-debugging/
        ├── SKILL.md
        └── references/runbook.md
```

OpenAI Docs hiện mô tả `plugin.json` ở gốc cho dạng portable; `.codex-plugin/plugin.json` là định dạng tương thích vẫn được hỗ trợ. Manifest mang danh tính, phiên bản và mô tả gói; cấu hình riêng cho OpenAI nằm trong phần mở rộng phù hợp. Không cần tạo cấu hình MCP rỗng cho một gói chỉ có skill. Đây là lựa chọn đóng gói cần kiểm trên host đích, chưa phải một plugin đã được dựng và thử. [Package your plugin](https://developers.openai.com/plugins/build/plugins), [Build skills](https://developers.openai.com/plugins/build/skills).

## Cách người dùng tiếp cận

Trong Codex CLI, `/plugins` mở trình duyệt plugin. Với plugin từ nguồn đã cấu hình, người dùng có thể cài, bật/tắt và gỡ theo host; sau cài, mở phiên mới để dùng skill hoặc tool đi kèm. Việc phân phối cá nhân/nhóm và đưa lên danh mục công khai là các bước khác nhau. [Plugins in ChatGPT and Codex](https://learn.chatgpt.com/docs/plugins).

Cách gọi skill vẫn theo host. Không mặc định định dạng gói hoặc quy trình cài của Codex cũng áp dụng nguyên xi cho Antigravity; khi thực hiện cần đối chiếu host đó và thử riêng.

## Lợi ích cho bộ dùng cá nhân

- Muốn giữ Markdown để sửa trực tiếp: cách clone và chạy `setup.sh` hiện tại đã đáp ứng.
- Muốn cài/bật/tắt cả bộ qua giao diện plugin: đóng gói chỉ gồm skill là bước mở rộng phù hợp.
- Khi xuất hiện nhu cầu lấy dữ liệu hoặc gọi dịch vụ mà host chưa có công cụ: mới xác định công cụ MCP cụ thể và quyền của chúng.

Bước đóng gói sau này cần kiểm việc khám phá skill, tải reference và gỡ gói trong môi trường thử. Tránh cài đồng thời hai bản cùng skill qua script và plugin; phải xác định bản đang được host sử dụng trước khi chuyển cách cài.
