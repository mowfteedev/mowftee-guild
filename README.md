# ⚔️ mowftee-guild

Bộ 23 skill tiếng Việt để phối hợp phát triển phần mềm với trách nhiệm rõ ràng, tiêu chí nghiệm thu và bằng chứng thực tế. Dùng dưới dạng thư mục skill cho Codex hoặc Google Antigravity; chọn một nhóm nhỏ theo đầu việc.

## Bắt đầu

Yêu cầu: Git để tải repo; Bash và Python 3.9+ để dùng CLI. CLI chỉ dùng thư viện chuẩn, không cần pip/npm. Những công cụ như browser, Docker, test runner chỉ cần khi dự án thực tế sử dụng.

```bash
git clone https://github.com/mowfteedev/mowftee-guild.git
cd mowftee-guild
./setup.sh validate
./setup.sh list
```

Xem kế hoạch cài trước khi ghi file:

```bash
./setup.sh install --tool codex --profile core --dry-run
./setup.sh install --tool codex --profile core
./setup.sh check --tool codex
```

Dùng Antigravity App/IDE thay `--tool codex` bằng `--tool antigravity`; Antigravity CLI dùng `--tool antigravity-cli`. Không truyền `--tool` thì giữ mặc định Antigravity App/IDE. Cài mặc định profile `core` gồm 6 skill; `--profile all` chọn toàn bộ 23.

Cài riêng cho một dự án:

```bash
./setup.sh install --tool codex --scope workspace --workspace /path/to/project --profile web --dry-run
./setup.sh init /path/to/project --name "Tên dự án" --dry-run
```

Bỏ `--dry-run` sau khi đã xem đúng đường dẫn và danh sách. `init` tạo bộ nhớ dự án và giữ nguyên file đã có; không tự điền PASS hay chọn stack. Chạy không có tham số chỉ hiển thị trợ giúp.

## Chọn đúng vai trò

[Danh mục đầy đủ: tên, mục đích và trách nhiệm 23 skill](docs/skills-catalog.md).

| Nhóm | Vai trò |
| --- | --- |
| Phân tích và điều phối | tech-lead, product-analyst, software-architect |
| Thiết kế và trải nghiệm | designer, accessibility |
| Triển khai | api-designer, frontend, backend, database, migration-specialist, refactoring-specialist |
| Kiểm định | test-automator, tester, code-reviewer, security, dependency-auditor, performance |
| Vận hành và phát hành | devops, sre, incident-responder, release-manager |
| Tài liệu và bảo trì skill | doc-writer, skill-maintainer |

Profile cài đặt: `core`, `web`, `quality`, `operations`, `maintenance`, `all`. Có thể chọn chính xác bằng `--skills backend,api-designer,test-automator`. Cài thêm một nhóm không gỡ nhóm đã cài trước đó.

## Cách sử dụng

Trong Codex CLI/IDE, dùng `$tech-lead`, `$backend` hoặc chọn skill từ `/skills`. Trong Antigravity App, dùng slash command như `/tech-lead`; cách hiển thị cụ thể tùy host. Skill cũng có thể được host chọn theo description. Xem [hướng dẫn host và ví dụ prompt](docs/usage.md).

Ví dụ yêu cầu:

```text
Dùng $tech-lead để phân tích yêu cầu thêm tính năng giỏ hàng vào dự án này.
Đọc hiện trạng, ghi phạm vi và AC, chọn những vai trò cần thiết.
Chỉ sửa local; chưa push, merge hoặc deploy. Báo bằng chứng và phần chưa kiểm tra.
```

Đổi `$tech-lead` thành `/tech-lead` khi dùng Antigravity App. Không cần gọi toàn bộ guild cho một sửa đổi nhỏ.

## Chất lượng được kiểm soát thế nào?

- Mỗi skill có đầu vào, ranh giới với vai trò khác, quy trình, đầu ra và điều kiện bàn giao.
- Đọc chi tiết theo nhu cầu: entrypoint gọn; tình huống biên nằm trong `references/runbook.md` tự chứa cùng skill.
- Kết quả dùng PASS / FAIL / BLOCKED / NOT_RUN / NOT_APPLICABLE; PASS cần gắn với snapshot và evidence.
- Việc nhiều rủi ro cần reviewer độc lập thực sự; tự kiểm tra không được đổi tên thành review độc lập.
- Vòng sửa có giới hạn; phần không hội tụ được báo rõ, không cắt AC để qua cổng.

[Quy tắc phối hợp và quality gates](docs/protocol.md) · [Phân loại rủi ro](docs/risk-and-evidence.md).

Đây là bộ hướng dẫn và công cụ quản lý file cục bộ. Repo không chứa runtime đa agent, không tự tạo reviewer, không tự enforce các cổng bằng một hệ thống điều phối. Chất lượng hành vi cần được đánh giá trên host thực tế. Plugin/MCP chưa được triển khai trong phiên bản này.

## Workflow

| Tình huống | Quy trình |
| --- | --- |
| Xây sản phẩm mới | [Từ ý tưởng đến MVP](workflows/01-tu-y-tuong-den-mvp.md) |
| Thêm tính năng | [Thay đổi tương thích và hồi quy](workflows/02-them-tinh-nang-moi.md) |
| Dọn nợ kỹ thuật / audit | [Bảo trì và tối ưu](workflows/03-tong-ve-sinh-va-bao-mat.md) |
| Sửa lỗi | [Tái hiện đến kiểm chứng](workflows/04-sua-loi.md) |
| Phát hành | [Review, rollout và phục hồi](workflows/05-phat-hanh.md) |
| Sự cố | [Ứng phó và postmortem](workflows/06-su-co.md) |
| Sửa bộ skill | [Phát triển và đánh giá skill](workflows/07-cai-tien-skill.md) |

Workflow và tài liệu nằm trong bản clone; lệnh `install` chỉ sao chép các thư mục skill được chọn. Mỗi skill có đủ runbook riêng để không phụ thuộc đường dẫn Desktop hay file ngoài bundle.

## CLI và kiểm tra

```bash
./setup.sh --help
./setup.sh install --help
./setup.sh validate
python3 -m unittest discover -s tests -v
./setup.sh uninstall --tool codex --dry-run
```

[Hướng dẫn cài, cập nhật, sao lưu, gỡ và xử lý sự cố](docs/installation.md) · [Nâng cấp từ v1](docs/migration-v2.md) · [Giới hạn đã biết](docs/limitations.md) · [Cách đánh giá hành vi skill](evals/README.md).

## Phát triển và nguồn tham khảo

[CONTRIBUTING](CONTRIBUTING.md) · [Changelog](CHANGELOG.md) · [Kiến trúc repo](docs/repository-design.md) · [Nguồn và provenance](docs/sources.md) · [Báo lỗi bảo mật](SECURITY.md).

Mã và nội dung gốc của dự án phát hành theo [MIT License](LICENSE). Các nguồn tham khảo được ghi công theo commit; không nhập toàn bộ kho bên thứ ba vào dự án.
