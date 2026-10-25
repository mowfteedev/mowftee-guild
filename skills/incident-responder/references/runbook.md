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

## Hợp đồng đầu ra khi bàn giao

- Incident record: impact, scope, permission và timeline.
- Mitigation log: hypothesis, decision, action, result.
- Postmortem: nguyên nhân có bằng chứng, follow-up và owner.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Chạm quyền chưa có, phương án không thể phục hồi an toàn hoặc dữ liệu quan trọng mâu thuẫn; chuyển owner và tiếp tục quan sát được phép. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
