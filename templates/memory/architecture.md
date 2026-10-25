# Kiến trúc: {{PROJECT_NAME}}

> Mẫu ghi chú tùy chọn. Chỉ copy và điền phần hữu ích; không cần tạo đủ bộ để dùng skill.
Cập nhật: {{DATE_UTC}}. Owner: software-architect. Trạng thái: DRAFT.

## Mục tiêu và ràng buộc

- Người dùng, luồng quan trọng và phạm vi: chưa xác định.
- Ngân sách, tải, thời hạn và môi trường: chưa xác định.
- SLI/SLO và cách đo: chưa thống nhất; không dùng một ngưỡng mặc định làm cam kết.

## Hiện trạng và quyết định

| Thành phần / dữ liệu | Owner | Contract / phụ thuộc | Nguồn bằng chứng | Trạng thái |
| --- | --- | --- | --- | --- |
| Chưa khảo sát | Chưa phân công | Chưa xác định | Chưa có | NOT_RUN |

## Luồng dữ liệu và trust boundaries

Ghi đường đi request, lưu trữ, dịch vụ ngoài và nơi kiểm tra quyền. Chỉ ghi công nghệ thực tế đã chọn; không điền sẵn stack.

## Failure modes và phục hồi

Với mỗi dependency: timeout, retry budget, backpressure, trạng thái suy giảm và tín hiệu phục hồi. Ghi rollback hoặc roll-forward theo ảnh hưởng dữ liệu.

## ADR liên quan

Chưa có ADR được chấp thuận. ADR khởi tạo là bản đề xuất, không phải quyết định đã duyệt.

## Câu hỏi còn mở

Ghi câu hỏi, tác động, owner và điều kiện cần để chốt.
