# Runbook: Độ tin cậy và quan sát

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Queue lag tăng nhưng CPU bình thường: theo dõi SLI luồng người dùng.
2. Restore mới chạy trên dữ liệu nhỏ: không hứa RTO cho toàn bộ production.
3. Lỗi dependency: alert có hướng xác minh downstream.
4. Chưa có on-call: ghi khoảng trống trách nhiệm, không bịa người nhận.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| SLI/SLO | Chọn tín hiệu từ user journey và thống nhất cửa sổ/error budget. | Định nghĩa numerator/denominator, dữ liệu và owner mục tiêu. |
| Telemetry | Liên kết metrics/logs/traces, hạn chế cardinality và dữ liệu nhạy cảm. | Dashboard/query, sampling và correlation example. |
| Alert | Mỗi alert có mức ưu tiên, owner, trigger và hành động rõ. | Ca trigger trong môi trường thử cùng runbook tương ứng. |
| Capacity/backpressure | Đo saturation, queue, dependency và giới hạn tài nguyên theo workload. | Load/capacity evidence và điều kiện mở rộng. |
| Recovery | Diễn tập restore/failover theo quyền, đo RPO/RTO thay vì hứa từ cấu hình. | Drill timeline, data integrity và phần chưa thử. |

## Hợp đồng đầu ra khi bàn giao

- Service objectives: user journey, SLI, SLO và owner.
- Observability/alert map: tín hiệu, action và runbook.
- Recovery report: scenario, actual RPO/RTO, integrity và residual risk.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Chưa có mục tiêu kinh doanh để cam kết SLA; diễn tập ảnh hưởng hệ thống thật ngoài quyền được cấp. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
