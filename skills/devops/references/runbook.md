# Runbook: Hạ tầng và CI/CD

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Redis bật mật khẩu: healthcheck và app phải xác thực đúng.
2. DB chỉ ở internal network: app vẫn cần đường egress nếu gọi đối tác.
3. Action pinned SHA: xác minh SHA thuộc upstream cần dùng.
4. Nginx chưa có cert: ghi rõ bootstrap thay vì README hứa HTTPS chạy ngay.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Build và artifact | Giữ dependency/runtime cần thiết, quyền tiến trình phù hợp; kiểm artifact sau build. | Build log, image/package digest và smoke test. |
| Secrets và credentials | Dùng kênh cấp secret phù hợp, không bake vào layer/log; app và healthcheck phải khớp config. | Config redacted và kiểm kết nối trong môi trường thử. |
| Network | Giữ DB/cache trong phạm vi cần; app có DNS/egress cho dependency ngoài nếu dùng. | Connection matrix và ca outbound/inbound được phép. |
| CI supply chain | Giảm token permissions; pin action/dependency theo policy và verify upstream SHA. | Workflow diff, nguồn SHA và run result. |
| Rollout | Readiness/drain/rollback theo behavior thật; không coi rolling là bảo đảm zero downtime. | Runbook, health signals, điểm dừng và owner. |

## Hợp đồng đầu ra khi bàn giao

- Infrastructure diff: build, network, secrets, health và permissions.
- CI evidence: checks, artifact ID/digest và môi trường.
- Operations handoff: deploy/rollback, prerequisite và hạn chế.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Thiếu quyền hạ tầng, secret bootstrap hoặc có destructive change chưa có phương án phục hồi được chấp nhận. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
