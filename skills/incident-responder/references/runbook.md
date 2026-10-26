# Runbook: Ứng phó sự cố

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Không có quyền production: thu dữ liệu được phép và đề xuất cho owner.
2. Secret lộ: không đưa lại secret vào timeline.
3. Rollback có migration phá dữ liệu: kiểm tra tính tương thích trước.
4. Người dùng chỉ yêu cầu postmortem: không tự tác động hệ thống.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Triage | Ưu tiên user impact, start time, scope và owner; ghi confidence của giả thuyết. | Timeline có timezone và nguồn từng observation. |
| Read-only investigation | Thu log/metric/config được phép, giữ secret redacted và evidence nguyên nhân. | Query/command và snapshot trước mutation. |
| Mitigation | Chọn hành động nhỏ đảo ngược được và kiểm quyền; giảm số biến thay cùng lúc. | Decision log, người thực thi và tín hiệu sau hành động. |
| Recovery | Kiểm lại luồng người dùng và sự ổn định trong cửa sổ phù hợp. | SLI/transaction evidence, không chỉ process status. |
| Postmortem | Tách contributing factors, mitigation và root cause; follow-up cụ thể. | Timeline, lessons và action có owner/exit criteria. |

## Đầu ra cần giữ khi liên quan

- Incident record: impact, scope, permission và timeline.
- Mitigation log: hypothesis, decision, action, result.
- Postmortem: nguyên nhân có bằng chứng, follow-up và owner.

## Điều kiện dừng phần phụ thuộc

Chạm quyền chưa có, phương án không thể phục hồi an toàn hoặc dữ liệu quan trọng mâu thuẫn; chuyển owner và tiếp tục quan sát được phép. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ triage: nhiều lỗi sau một lần triển khai

Đầu tiên xác nhận lúc nào, endpoint nào, nhóm người dùng nào bị ảnh hưởng; so tín hiệu trước/sau và artifact đang chạy. “Vừa deploy nên chắc do deploy” là giả thuyết, chưa phải nguyên nhân đã xác minh.

| Quan sát | Hướng kiểm tiếp |
| --- | --- |
| Chỉ bản mới lỗi, cùng dependency/dữ liệu | So thay đổi config/code và xem phương án quay về bản cũ có tương thích schema hiện tại không. |
| Cả bản cũ và mới cùng timeout DB | Xem connection, lock, tải và thay đổi hạ tầng; rollback app có thể không giải quyết. |
| Tỷ lệ lỗi thấp nhưng queue lag tăng | Đo ảnh hưởng đầu cuối; lỗi có thể chưa biểu hiện thành HTTP error. |
| Thiếu quyền thao tác production | Tiếp tục thu dữ liệu được phép, đưa hành động cụ thể và điều kiện kiểm lại cho người có quyền. |

Với mitigation đã được phép, ghi thời điểm, hành động, điều kiện thành công và tín hiệu quan sát. Sau hành động, kiểm cả traffic thành công và backlog; process sống không đồng nghĩa dịch vụ đã hồi phục. Không thay nhiều cấu hình cùng lúc nếu không cần, vì sẽ khó biết điều gì có tác dụng.

Trong postmortem, tách nguyên nhân được chứng minh, yếu tố góp phần và phần chưa biết. Hành động theo sau phải chữa cơ chế gây lỗi hoặc giảm thời gian phát hiện/phục hồi; “cẩn thận hơn” không đủ để kiểm chứng. Không gửi thông báo cho người khác chỉ vì mẫu incident có mục liên lạc.
