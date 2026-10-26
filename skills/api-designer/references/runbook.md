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

## Đầu ra cần giữ khi liên quan

- Contract: endpoint, auth, schema, errors, limits.
- Compatibility report: consumer, before/after và rollout.
- Test vectors: payload tốt/xấu, conflict, pagination và từ chối quyền.

## Điều kiện dừng phần phụ thuộc

Chưa biết consumer bị ảnh hưởng hoặc chưa thống nhất hành vi public có tác động dữ liệu/tiền/quyền. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ contract: cập nhật hồ sơ từng phần

Với một API nhận `display_name` và `phone`, xác định ý nghĩa của field bị bỏ qua, giá trị `null` và chuỗi rỗng. Không gán semantics của một chuẩn PATCH cụ thể nếu API chưa dùng chuẩn đó.

Một contract minh họa đã được chủ sản phẩm đồng ý có thể là:

| Payload | Ý nghĩa |
| --- | --- |
| `{}` | Không đổi hồ sơ, theo hành vi no-op đã chọn. |
| `{"display_name": "An"}` | Chỉ đổi tên, giữ số điện thoại. |
| `{"phone": null}` | Xóa số điện thoại nếu field được phép xóa. |
| `{"display_name": null}` | Lỗi validation vì tên không được null. |
| `{"phone": ""}` | Xử lý theo quy tắc riêng đã chốt; không mặc nhiên coi giống null. |

Đối chiếu serializer và client: client có gửi null cho tất cả field chưa điền không, backend có vô tình biến field bị thiếu thành null không? Nếu có cập nhật đồng thời, quyết định có cần điều kiện phiên bản hay chấp nhận ghi đè; mô tả rõ lỗi xung đột và cách client phục hồi.

Một thay đổi từ “bỏ qua null” sang “null nghĩa là xóa” có thể xóa dữ liệu của client cũ. Vì vậy compatibility phải xem payload và consumer thật. Bàn giao các test vector trên cùng schema, quyền sửa từng field và error shape của dự án; không tự đặt mã lỗi khác hệ thống chỉ để theo ví dụ.
