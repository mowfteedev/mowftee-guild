# Giới hạn và cách hiểu kết quả

## Đã triển khai

23 skill tự chứa, metadata Codex, 7 workflow, profiles, memory templates và CLI quản lý file cục bộ. Source validation kiểm manifest, link, metadata và tính nhất quán; unit tests kiểm hành vi installer và invariant filesystem.

## Không được suy ra từ CI xanh

- Agent sẽ luôn chọn đúng skill hoặc không thể bỏ qua hướng dẫn.
- Một người đổi persona tạo được reviewer độc lập.
- UI của Codex/Antigravity đã discover và chạy thành công toàn bộ skill.
- Một sản phẩm dùng guild đã đạt production readiness, đạt WCAG, zero regression hoặc miễn nhiễm bảo mật.
- Có runtime chạy song song, enforce gate hoặc kết nối MCP.

Các [kịch bản behavioral eval](../evals/README.md) cần được chạy trên host/model thực tế và giữ transcript đã che dữ liệu nhạy cảm. Nếu chưa chạy thì trạng thái vẫn NOT_RUN. Đối chiếu [báo cáo kiểm chứng phiên bản](verification.md) để biết lệnh thực sự đã chạy.

## Installer và môi trường

CLI cần Python 3.9+, Bash cho launcher, filesystem hỗ trợ directory rename và symlink detection. CI kiểm một số tổ hợp OS/runtime; không coi đó là chứng minh mọi distro, Windows native hoặc filesystem mạng đều hỗ trợ. Có thể gọi `python3 scripts/guild.py` nếu không dùng Bash, nhưng Windows native chưa nằm trong ma trận CI.

Không hỗ trợ symlink trong payload hoặc đường dẫn đích. Không kiểm link web từ validator; chỉ kiểm link file nội bộ, không xác nhận mọi anchor. Không parse toàn bộ YAML; xem subset trong [thiết kế repo](repository-design.md).

Installer không cung cấp giao dịch bền vững trước mất điện cho nhiều thư mục. Khi có interrupted transaction, giữ nguyên journal và đọc [hướng dẫn phục hồi](installation.md). Dry-run không ghi file và cũng không chứng minh có đủ quyền ghi cho lần thực thi thật.
