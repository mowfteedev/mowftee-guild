# Cài đặt, cập nhật và gỡ skill

## Yêu cầu và nguyên tắc

Bash và Python 3.9+; CLI dùng thư viện chuẩn. `setup.sh` tìm Python qua `python3`. Có thể gọi trực tiếp `python3 scripts/guild.py`. CLI không chạy code trong skill, không cài package và không sửa cấu hình host.

Đọc [migration v2](migration-v2.md) nếu đã cài bằng script cũ. Cài v1 hoặc file copy thủ công không có manifest được xem là UNMANAGED.

## Lệnh

| Lệnh | Tác dụng | Ghi file? |
| --- | --- | --- |
| `list` | Danh mục và profile; `--json` cho output có cấu trúc | Không |
| `validate` | Kiểm source, catalog, metadata, link và định nghĩa eval | Không |
| `install` | Cài/cập nhật skill được chọn, giữ skill khác | Có; trừ `--dry-run` |
| `check`, `status` | So payload với ownership/hash và source hiện tại | Không |
| `uninstall` | Gỡ skill thuộc manifest; giữ root, backup và skill khác | Có; trừ `--dry-run` |
| `init [path]` | Tạo file memory còn thiếu cho dự án | Có; trừ `--dry-run` |

Chạy không argument hoặc `--help` chỉ hiển thị trợ giúp, không tự install. Các lệnh thực hiện validation source trước khi thao tác. Exit 0 là thành công, exit 1 là validation/ownership/I/O/check thất bại, exit 2 là lỗi cú pháp CLI hoặc phiên bản Python không hỗ trợ. Không dùng grep chuỗi thành công thay cho kiểm tra mã thoát.

## Chọn vị trí

```bash
# Global Codex
./setup.sh install --tool codex --profile core --dry-run

# Global Antigravity App/IDE (mặc định)
./setup.sh install --tool antigravity --profile web --dry-run

# Global Antigravity CLI
./setup.sh install --tool antigravity-cli --skills backend,test-automator --dry-run

# Workspace: hai host đều đọc .agents/skills theo tài liệu hiện hành
./setup.sh install --tool codex --scope workspace --workspace /path/to/project --profile web --dry-run

# Thư mục tự chọn, ví dụ để kiểm tra hoặc đóng gói nội bộ
./setup.sh install --dest /tmp/guild-demo-skills --profile quality --dry-run
```

Bỏ `--dry-run` để thực hiện vào đúng đường dẫn đã xem. `--dest` ưu tiên hơn `--tool`, `--scope`, `--workspace`. Không hỗ trợ đường dẫn đích chứa symlink; không dùng root filesystem, home root hoặc đường dẫn trong source repository làm skill destination.

[Đường dẫn mặc định theo host](usage.md). Lệnh check/gỡ cần cùng target đã cài; không tự tìm và thay đổi tất cả host.

## Chọn tập skill

Không chọn gì thì install dùng `core` (6). `--profile all` chọn toàn bộ 23; `--profile web`, `quality`, `operations`, `maintenance` chọn nhóm cụ thể. `--skills` chọn tên chính xác, phân tách dấu phẩy. Không dùng cùng `--profile` và `--skills`; tên sai, trùng hoặc rỗng bị từ chối trước khi ghi payload.

```bash
./setup.sh list --profile operations
./setup.sh list --json
./setup.sh install --tool codex --skills api-designer,backend,test-automator --dry-run
```

Install là cập nhật cộng thêm: cài profile quality sau core giữ nguyên các skill core. Không tự prune những skill ngoài profile mới. `check` không chọn profile thì kiểm toàn bộ skill manifest đã quản lý; khi chưa có manifest, kiểm core và báo MISSING/UNMANAGED. Uninstall không chọn thì gỡ toàn bộ skill thuộc manifest, không phải mọi thư mục trong root.

## Ownership và hash

Target chứa file `.mowftee-guild/manifest.json` với owner, schema version và SHA-256 từng file. Check báo:

| Trạng thái | Ý nghĩa |
| --- | --- |
| OK | Khớp manifest và source hiện tại |
| MISSING | Không có payload được yêu cầu |
| UNMANAGED | Có thư mục nhưng không thuộc manifest |
| MODIFIED | File cài khác hash hoặc tập file trong manifest |
| OUTDATED | Payload vẫn khớp bản đã cài nhưng khác source đang dùng |
| UNAVAILABLE | Manifest còn một skill mà catalog source hiện tại không cung cấp |

Symlink hoặc manifest hỏng là lỗi, không bị coi như một trạng thái lành mạnh. Hash kiểm tính nhất quán với manifest cục bộ; không phải chữ ký chứng minh nguồn tin cậy.

Install/gỡ mặc định từ chối sửa skill UNMANAGED hoặc MODIFIED. `--force` cho phép sao lưu rồi thay; uninstall vẫn từ chối tên không thuộc manifest dù dùng force. Skill không được chọn không bị tác động.

## Backup và khôi phục

```bash
./setup.sh install --tool codex --skills backend --force --dry-run
./setup.sh install --tool codex --skills backend --force
```

Khi có thư mục cũ cần giữ, force in đường dẫn `.mowftee-guild/backups/<id>/` gồm:

- `old/<skill>/`: nội dung cũ, gồm tùy chỉnh của người dùng.
- `manifest.before.json`: ownership trước thao tác.
- `journal.json`: loại thao tác và tên skill liên quan.
- `new/`: staging còn lại; sau thành công thường không còn payload trong đó.

Không có lệnh restore tự động đoán bản cần quay lui. Để khôi phục một skill, dừng thao tác host liên quan, giữ bản sao target hiện tại, đối chiếu backup, chuyển đúng `old/<skill>` về target và đối chiếu entry của skill trong manifest trước đó. Nếu backup là bản UNMANAGED, bỏ ownership của skill khôi phục thay vì gán hash bản v2. Không thay toàn bộ manifest khi các skill khác đã được cài sau snapshot backup. Chạy check để xác nhận trạng thái thực tế; file khôi phục từ bản cũ có thể đúng là OUTDATED hoặc UNMANAGED.

## Transaction và gián đoạn

CLI dựng payload trong `.mowftee-guild/transactions/<id>/new/`, chuyển payload cũ sang `old/`, thay thư mục đích rồi thay manifest bằng atomic file replace. Lỗi process thông thường trong giai đoạn commit được xử lý quay lui. Không hứa atomic toàn bộ thao tác trước kill/mất điện.

Nếu bị gián đoạn:

1. Xác nhận không còn tiến trình install/gỡ đang chạy. Không xóa lock của một tiến trình còn sống.
2. Sao lưu thư mục control và các target liên quan trước khi sửa.
3. Đọc `journal.json`, `manifest.before.json`, `old/`, `new/` và manifest hiện tại để biết thao tác đã đi đến đâu. Không xóa transaction chỉ để chạy lại.
4. Đối chiếu từng skill với snapshot mong muốn; phục hồi target cùng entry ownership tương ứng. Nếu không xác định được trạng thái, giữ evidence và yêu cầu người vận hành quyết định.
5. Sau khi trạng thái đã được phục hồi, chuyển transaction ra nơi lưu trữ phục hồi rồi bỏ lock cũ rỗng. Chạy check và dry-run trước khi mutation tiếp.

Stale lock không tự bị xóa theo tuổi file. Một interrupted transaction còn dữ liệu sẽ chặn mutation tiếp theo, không bị bỏ qua bằng force. Lỗi cleanup sau commit cũng có thể để transaction còn lại: kiểm manifest/target trước khi gọi là rollback thất bại.

## Bộ nhớ dự án

```bash
./setup.sh init /path/to/project --name "Tên dự án" --dry-run
./setup.sh init /path/to/project --name "Tên dự án"
```

Tạo 10 file còn thiếu trong `.memory/`, bao gồm ADR khởi tạo PROPOSED. Existing files được giữ nguyên; symlink bị từ chối trước khi ghi. Có thể tạo project path mới khi được chỉ định. Không sửa Git ignore của dự án đích. `init` có thể tiếp tục lần sau nếu bị gián đoạn vì không ghi đè file đã có; không có giao dịch nguyên tử cho cả bộ memory.

## Gỡ

```bash
./setup.sh uninstall --tool codex --skills backend --dry-run
./setup.sh uninstall --tool codex --skills backend
./setup.sh uninstall --tool codex --dry-run
```

Lệnh cuối liệt kê mọi skill manifest đang sở hữu. Không tự xóa `.memory/`, backup, repo clone hoặc các skill từ nguồn khác. Giữ file đã sửa bằng backup trước khi gỡ có force. Chưa có skill thuộc manifest thì gỡ là no-op.
