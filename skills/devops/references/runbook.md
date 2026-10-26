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

## Đầu ra cần giữ khi liên quan

- Infrastructure diff: build, network, secrets, health và permissions.
- CI evidence: checks, artifact ID/digest và môi trường.
- Operations handoff: deploy/rollback, prerequisite và hạn chế.

## Điều kiện dừng phần phụ thuộc

Thiếu quyền hạ tầng, secret bootstrap hoặc có destructive change chưa có phương án phục hồi được chấp nhận. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ chẩn đoán: chạy được trên host, lỗi trong container

App trong container không kết nối được DB là một chuỗi điều kiện, không phải lý do để công khai cổng DB ngay. Đọc topology, cấu hình đã che secret và log lỗi trước.

| Dấu hiệu | Điều nên kiểm |
| --- | --- |
| Không resolve hostname | Tên service/DNS và network mà app thực sự tham gia. |
| Connection refused | Địa chỉ/port bên trong network, tiến trình DB và thứ tự sẵn sàng; `localhost` thường chỉ chính container hiện tại. |
| Authentication failed | App, DB và healthcheck có cùng nguồn cấu hình/credentials dự kiến không; không in mật khẩu để so. |
| App khỏe nhưng không gọi được dịch vụ ngoài | DNS/egress/proxy theo topology, không mở thêm inbound chỉ để chữa outbound. |

Thử kết nối từ cùng network/context của app bằng công cụ đã có hoặc môi trường tạm được phép. `healthy` của DB không chứng minh tài khoản app có quyền hay schema đã sẵn sàng.

Với bản sửa cấu hình, kiểm parse/build, khởi động sạch trong môi trường thử và một thao tác app cần DB. Ghi rõ volume nào tồn tại qua lần khởi động; lệnh reset/xóa volume không được đưa vào quickstart như một bước sửa lỗi vô hại. Thay đổi production chỉ thực thi trong phạm vi người dùng đã cấp.
