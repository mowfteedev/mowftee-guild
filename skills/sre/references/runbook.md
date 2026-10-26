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

## Đầu ra cần giữ khi liên quan

- Service objectives: user journey, SLI, SLO và owner.
- Observability/alert map: tín hiệu, action và runbook.
- Recovery report: scenario, actual RPO/RTO, integrity và residual risk.

## Điều kiện dừng phần phụ thuộc

Chưa có mục tiêu kinh doanh để cam kết SLA; diễn tập ảnh hưởng hệ thống thật ngoài quyền được cấp. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ chọn SLI cho tác vụ xuất báo cáo nền

HTTP `202 Accepted` chỉ xác nhận đã nhận việc; nếu job treo thì người dùng vẫn chưa có báo cáo. Chọn tín hiệu theo kết quả đầu cuối, dựa trên nhu cầu thật đã thống nhất.

| Tín hiệu | Định nghĩa cần chốt |
| --- | --- |
| Tỷ lệ hoàn tất đúng hạn | Số job hợp lệ hoàn tất trong hạn / số job hợp lệ đã đến hạn đánh giá; định nghĩa job hủy/lỗi đầu vào. |
| Thời gian chờ và xử lý | Mốc enqueue/start/finish, cùng job ID; phân biệt queue delay với execution time. |
| Độ trễ quan sát | Telemetry đến muộn hoặc mất phải hiện là khoảng trống, không tự tính như không có lỗi. |

Không lấy số job kết thúc trong một cửa sổ chia cho số job tạo cùng cửa sổ nếu hai nhóm không khớp. Quy định cohort/cửa sổ để job chưa đủ tuổi không bị tính sai, đồng thời không bỏ quên job bị treo.

Alert cần dẫn đến hành động: xác định queue/dependency nào, backlog có tăng, worker còn tiến triển và ảnh hưởng job nào. CPU thấp không loại trừ nghẽn do chờ DB hoặc dịch vụ ngoài. Với hệ thống cá nhân, chỉ thiết lập kênh nhận và mức phức tạp mà người dùng thực sự cần; không bịa đội on-call.

Nếu diễn tập phục hồi, đo từ mốc sự cố đã định nghĩa đến khi báo cáo có thể tạo/tải lại và kiểm tính toàn vẹn. Chỉ thấy worker khởi động không đủ để kết luận đã khôi phục hành trình người dùng.
