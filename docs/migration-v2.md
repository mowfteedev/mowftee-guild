# Nâng cấp từ v1 lên v2

## Thay đổi cần biết

- Giữ 10 tên skill cũ; viết lại trách nhiệm và bổ sung 13 vai trò để giảm chồng lấn. Không dùng số 10 cố định trong vòng lặp hay báo cáo.
- `./setup.sh` không argument chỉ hiện help. `install` mặc định Antigravity App/IDE với profile core 6 skill; muốn cài tất cả dùng `--profile all`.
- Python 3.9+ là prerequisite mới; không cần pip/npm để dùng CLI.
- `check`/`status` kiểm ownership, hash và drift với source; trả exit 1 khi có lỗi, không chỉ in cảnh báo với exit 0.
- Cài đặt v1 chưa có ownership manifest. V2 xem các thư mục đó là UNMANAGED và không tự ghi đè.
- Workflow hiện là tài liệu quy trình, không có công cụ invoke_subagent cố định hoặc model flash/pro hardcode. Plugin/MCP để giai đoạn khác.
- Mẫu memory bỏ stack và số liệu PASS điền sẵn. `init` giữ nguyên file đã tồn tại; không tự chuyển lịch sử v1 sang v2.

## Quy trình nâng cấp

1. Giữ bản sao skill và `.memory/` tùy chỉnh đang dùng.
2. Đọc [danh mục mới](skills-catalog.md), chọn profile hoặc tên cụ thể.
3. Chạy dry-run tới đúng skill root. Nếu thấy UNMANAGED, đối chiếu nội dung cũ trước khi chấp nhận thay.
4. Dùng `--force` khi muốn sao lưu và thay các skill được chọn. Backup ghi trong `.mowftee-guild/backups/<id>/old/` kèm manifest trước đó.
5. Chạy check; mở host và xác nhận discovery bằng một yêu cầu đơn giản.
6. Với memory cũ, đọc mẫu v2 rồi cập nhật có chọn lọc, giữ lịch sử ADR/evidence. Không dùng init để ghi đè tài liệu đang làm.

```bash
./setup.sh install --tool antigravity --profile all --force --dry-run
./setup.sh install --tool antigravity --profile all --force
./setup.sh check --tool antigravity
```

Không truyền force chỉ để bỏ qua một xung đột chưa hiểu. Restore backup theo [hướng dẫn cài đặt](installation.md); script không tự đoán phiên bản cần khôi phục.
