# Kiểm chứng phiên bản 2.0.0

Ngày thực hiện: 26/10/2026. Môi trường local: Linux, Python 3.14.8, Bash. Phạm vi: source v2 trên nhánh `feat/guild-v2-specialized-skills` trước khi commit; lệnh chỉ thay đổi thư mục tạm trong các kiểm thử cài/gỡ. Báo cáo được đưa cùng commit với source đã kiểm tra; không tự ghi một SHA chưa tồn tại.

## Các kiểm tra đã thực hiện

| Kiểm tra | Kết quả quan sát được | Phạm vi chứng minh |
| --- | --- | --- |
| `./setup.sh validate` | Exit 0: 23 skill, 6 profile | Catalog, tên, metadata, local links và định nghĩa scenario nhất quán |
| `bash -n setup.sh` | Exit 0 | Cú pháp Bash launcher |
| `python3 -m unittest discover -s tests -v` | 40 tests, OK; 5.128 giây trong lần chạy cuối trước khi ghi báo cáo | Hành vi CLI và bảo toàn filesystem trong môi trường tạm |
| Validator `skill-creator/scripts/quick_validate.py` | 23/23 skill hợp lệ | Frontmatter, tên và scaffold theo validator của skill-creator đang có trên máy |
| Parse `agents/openai.yaml` và CI YAML bằng PyYAML 6.0.3 | 23 metadata và workflow parse thành công | YAML hợp lệ; không thay thế kiểm chứng discovery trên host |
| `git diff --check` | Exit 0 trước commit | Không có lỗi whitespace được Git phát hiện trong diff |

PyYAML chỉ được cài vào virtualenv tạm để chạy validator bổ sung; không là dependency của CLI trong repo. Validator của skill-creator là tài nguyên môi trường local, không được đóng gói thành dependency bắt buộc cho người dùng.

## Hành vi CLI được kiểm chứng

- Cài toàn bộ payload tự chứa; cài cộng thêm và cài lại không đổi dữ liệu ngoài lựa chọn.
- Dry-run không tạo thư mục; tên sai/trùng/rỗng bị từ chối trước mutation.
- Giữ file UNMANAGED/MODIFIED trừ khi force rõ ràng; force có backup.
- Gỡ đúng ownership, giữ skill khác và tùy chỉnh trong backup.
- Phát hiện thiếu file, source drift và manifest hỏng.
- Chặn traversal, symlink root/control/manifest/payload và special file.
- Lock hoặc interrupted transaction chặn mutation tiếp theo.
- Mô phỏng lỗi ghi manifest sau khi di chuyển payload: khôi phục toàn bộ payload đã di chuyển và manifest trước đó.
- Init có thể chạy lại, giữ nguyên file cũ, preflight symlink và hỗ trợ dry-run.
- Đường dẫn có khoảng trắng, các target host trong HOME tạm và workspace scope.

Các kiểm thử và fixture có thể xem ở [tests/test_guild.py](../tests/test_guild.py). Đây là self-check của người triển khai, chưa phải review độc lập bởi một người/model khác.

## Smoke theo luồng README

Đã chạy launcher Bash từ ngoài repo với HOME và project tạm: validate → list core → install dry-run → install core Codex → check → init project → uninstall dry-run → uninstall. Tất cả command exit 0. Xác nhận tạo đủ 10 file memory và gỡ payload thuộc ownership. Không cài bộ skill vào HOME thật của người dùng.

## CI và giới hạn

[Workflow CI](../.github/workflows/validate.yml) định nghĩa 4 tổ hợp: Ubuntu/macOS × Python 3.9/3.14. Kết quả mỗi lần chạy remote xem trực tiếp tại [GitHub Actions](https://github.com/mowfteedev/mowftee-guild/actions); bảng local phía trên không tự khẳng định trạng thái của các lần chạy remote.

31 [behavioral scenario](../evals/scenarios.json): **NOT_RUN** trên host/model độc lập. Discovery và chạy thực tế bằng giao diện Codex/Antigravity: **NOT_RUN**. Benchmark so với v1: **NOT_RUN**. Không có tuyên bố về điểm chất lượng, production readiness hay tương thích host đã được kiểm chứng đầu cuối. Plugin/MCP chưa triển khai theo phạm vi người dùng chốt.
