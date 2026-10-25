# Thiết kế repository

## Thành phần

```text
catalog.json              Danh mục, phiên bản, nhóm và profiles
VERSION                   Phiên bản khớp catalog
skills/<name>/SKILL.md     Entry point và frontmatter theo Agent Skills
skills/<name>/references/  Runbook có thể đi cùng bản cài độc lập
skills/<name>/agents/      Metadata UI Codex, không chứa dependency MCP
skills/<name>/LICENSE.txt  License đi cùng payload cài đặt
workflows/                Quy trình theo tình huống cho người dùng/agent
scripts/guild.py          CLI Python standard library
setup.sh                  Bash launcher, không tự install khi thiếu argument
templates/memory/         Mẫu chưa kiểm chứng, không điền sẵn PASS
tests/                    Kiểm thử filesystem và CLI trong thư mục tạm
evals/                    Kịch bản đánh giá hành vi và mẫu ghi nhận
.github/workflows/        Kiểm tra nguồn và unit tests trên CI
```

## Quyết định thiết kế

- Tách 23 vai trò theo quyết định và đầu ra, không theo số lượng cố định. Skill mới chỉ có ích nếu có trigger và trách nhiệm riêng.
- Payload tự chứa: mỗi skill chỉ link tài nguyên nằm trong cùng thư mục. Tài liệu chung không là dependency bắt buộc của payload đã cài.
- `catalog.json` quản lý tên/profile; description phải khớp entrypoint. Validator phát hiện drift, không tự sửa.
- Flat frontmatter subset: `name`, `description`, `license`. Description dùng JSON string, cũng là YAML string hợp lệ. Validator nội bộ cố ý không là parser YAML tổng quát; thêm cấu trúc YAML phải đổi validator và test trước.
- Metadata `agents/openai.yaml` dùng ba trường interface dạng chuỗi có quote. Không khóa automatic invocation, không cấp tool hay thêm plugin.
- Python 3.9+ thay shell logic phức tạp để có xử lý đường dẫn, JSON, hashing và unit tests không cần dependency runtime ngoài.
- Installer lưu ownership/hash từng file, từ chối symlink và xung đột không rõ sở hữu. `--force` giữ backup trước replacement/removal.
- Staging toàn bộ payload trước commit; lỗi process thông thường được quay lui. Mất điện/kill giữa nhiều directory replace không được tuyên bố atomic: journal được giữ và lần mutation sau yêu cầu kiểm tra thủ công.
- Gỡ chỉ áp dụng skill do manifest quản lý; không xóa toàn bộ skill root, backup hay dữ liệu dự án.

## Ranh giới phiên bản này

Không có MCP server, plugin manifest, dịch vụ mạng, agent runtime hay lệnh deploy. Không tự thay cấu hình host hoặc cài vào môi trường thật trong quá trình kiểm thử repo. [Giới hạn](limitations.md) ghi các kiểm tra chưa được thực hiện.
