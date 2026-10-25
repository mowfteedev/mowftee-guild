# Runbook: Thiết kế hợp đồng API

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Thêm enum mới: xác nhận consumer cũ có xử lý giá trị lạ.
2. Gửi lại cùng key khác payload: quy định xung đột thay vì replay nhầm.
3. Tài nguyên của người khác: thống nhất cách trả lỗi theo mô hình quyền.
4. Request quá lớn: có giới hạn phía server và phản hồi phù hợp.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Đổi request/schema | Đối chiếu optional, nullable, default, enum và giới hạn với consumer thật. | Contract diff và mẫu payload hợp lệ/không hợp lệ. |
| Idempotency public | Định nghĩa principal/tenant, operation, key, payload fingerprint và replay window. | Ca same key/same payload và same key/different payload. |
| Pagination và filtering | Chọn thứ tự ổn định, semantics cursor/offset, giới hạn và hành vi khi dữ liệu đổi. | Ví dụ nhiều trang với dữ liệu trùng sort key. |
| Error và retry | Tách lỗi client, conflict, rate limit, dependency và lỗi nội bộ; tránh lộ tài nguyên nhạy cảm. | Error schema, status mapping và retry guidance. |
| Rollout nhiều client | Kiểm client cũ trong thời gian chuyển đổi; có deprecation hoặc version strategy khi breaking. | Consumer contract tests và migration note. |

## Hợp đồng đầu ra khi bàn giao

- Contract: endpoint, auth, schema, errors, limits.
- Compatibility report: consumer, before/after và rollout.
- Test vectors: payload tốt/xấu, conflict, pagination và từ chối quyền.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Chưa biết consumer bị ảnh hưởng hoặc chưa thống nhất hành vi public có tác động dữ liệu/tiền/quyền. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
