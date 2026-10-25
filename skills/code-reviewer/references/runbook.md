# Runbook: Thẩm định mã nguồn

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Promise không await nhưng được cố ý background: kiểm tra ownership và error handling trước kết luận.
2. Seq scan: cần workload thay vì nhận định theo tên operator.
3. Không thấy bug: báo không có finding trong phạm vi và giới hạn review.
4. Token giả trong fixture: phân biệt placeholder với secret thật, không in lại giá trị.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Public contract | Truy caller, serializer, schema và consumer; không kết luận từ chữ ký hàm đơn lẻ. | Call path và kịch bản bị ảnh hưởng. |
| Lỗi bất đồng bộ | Kiểm owner của background work, await/catch, resource lifetime và cancellation. | Đường thực thi gây mất lỗi hoặc side effect sai. |
| Transaction/concurrency | Xác định invariant và interleaving làm vi phạm; xem constraint hoặc lock thực có. | Ca hai thao tác cạnh tranh và dữ liệu sai có thể xảy ra. |
| Review hiệu năng | Tách phỏng đoán O(n²)/N+1 với workload thật và giới hạn input. | Query/caller/data size hoặc yêu cầu đo thêm. |
| Báo cáo | Ghi finding ngắn ở vùng diff nhỏ nhất, kèm trigger và tác động; không bịa lỗi khi không tìm thấy. | Base/head, checks đã chạy, findings và giới hạn review. |

## Hợp đồng đầu ra khi bàn giao

- Review scope: base/head, AC và file/caller đã đọc.
- Findings: severity, location, trigger, impact và cách kiểm lại.
- Verdict: blockers còn lại, checks đã chạy và phần cần runtime validation.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Không đủ contract hoặc caller để khẳng định lỗi; báo câu hỏi thay finding chắc chắn và không tự sửa khi chỉ được review. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
