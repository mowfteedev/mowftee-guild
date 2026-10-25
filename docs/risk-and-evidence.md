# Mức rủi ro và bằng chứng

Mức rủi ro mô tả hậu quả và độ khó phục hồi, không phải nhãn uy tín của người làm. Chọn mức cao nhất của phần thực sự bị tác động; không tự nâng một sửa đổi đơn giản thành audit toàn hệ thống.

| Mức | Ví dụ | Kiểm chứng và bàn giao cần cân nhắc |
| --- | --- | --- |
| R0: Nhỏ, dễ đảo ngược | Lỗi chữ, link tài liệu, thay đổi trình bày cục bộ | Đọc diff, kiểm link hoặc xem giao diện đúng phạm vi; thường tự kiểm đủ |
| R1: Hành vi thông thường | Endpoint mới, component, lỗi nghiệp vụ cục bộ | AC, baseline liên quan, kiểm thử có ý nghĩa và review khi độ phức tạp cần |
| R2: Dữ liệu hoặc quyền | Migration, thanh toán, phân quyền, API công khai | Invariant, failure/concurrency cases liên quan, consumer compatibility, phục hồi, reviewer độc lập |
| R3: Hệ thống đang vận hành | Deploy, restore, rotate key thật, destructive action | Quyền đã xác lập, runbook, snapshot/artifact, điểm dừng, quan sát sau thao tác và owner phục hồi |

R0/R1 vẫn giữ nguyên yêu cầu người dùng về quyền hoặc kiểm định. R2/R3 không tự cấp quyền thử phá hệ thống. Dry-run không chứng minh execution đã thành công.

## Chọn tiêu chí trước khi đo

- Hiệu năng: workload, phân vị, error rate, cấu hình máy, cache state và ngân sách được thống nhất.
- UI: luồng, viewport, nội dung dài và tiêu chuẩn accessibility phù hợp. Không dùng một ảnh đẹp để kết luận tương thích mọi thiết bị.
- Dữ liệu: invariant, engine/version, isolation, migration ordering, khối lượng đại diện và khả năng phục hồi.
- Bảo mật: tài sản, trust boundaries, attacker capability, điều kiện khai thác và phạm vi được phép kiểm tra.
- Test: observable behavior, dữ liệu riêng, mock boundaries và điều kiện chờ hữu hạn.
- Container/CI: runtime dependencies, permissions, healthcheck, secrets, egress và artifact định danh được.

Không áp bắt buộc chung coverage 80%, image 50 MB, API 50 ms, UUIDv7 hay connection pool theo số core. Có thể đặt ngưỡng như vậy cho một dự án nếu có yêu cầu và cơ sở đo, không coi nó là chân lý áp dụng mọi nơi.

## Evidence hợp lệ

Một bằng chứng phải liên kết được tới tiêu chí, command hoặc thao tác, snapshot, môi trường, thời điểm và kết quả thực tế. Exit code cần ghi khi công cụ có mã thoát. Log, ảnh, trace và report nằm trong phạm vi được phép lưu, đã che dữ liệu nhạy cảm.

Nếu code đang dirty, ghi base commit và diff hoặc file liên quan. Nếu evidence tạo trước một thay đổi ảnh hưởng tới kết luận, phải đánh giá lại hoặc chạy lại check cần thiết. Không dùng hash tự tính của template làm bằng chứng hành vi agent.

## Khi nào kết luận không đủ?

- Không có output: NOT_RUN hoặc BLOCKED, không phải PASS.
- Scanner không kết nối được: lỗi công cụ, không có nghĩa không có lỗ hổng.
- Test có retry mới pass: ghi nhận flakiness; không gọi ổn định tuyệt đối.
- Tự review code vừa viết: có giá trị tự kiểm nhưng chưa là review độc lập.
- Không tìm thấy bug: được báo không có finding trong phạm vi kiểm tra; không bịa bug để thể hiện nghiêm ngặt.
- Kiểm tra tĩnh skill: không chứng minh skill được chọn đúng hoặc hành xử đúng trên host.
