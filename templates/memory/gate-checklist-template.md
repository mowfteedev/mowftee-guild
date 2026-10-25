# Biên bản cổng: {{PROJECT_NAME}}

- Tạo: {{DATE_UTC}}.
- Gate / workflow / task ID: chưa chọn.
- Snapshot và môi trường: chưa ghi nhận.
- Người thực hiện / reviewer thực tế: chưa phân công.
- Kết luận: NOT_RUN.

## Tiêu chí được chọn trước khi kiểm tra

| AC / invariant | Bắt buộc? | Cách kiểm chứng | Trạng thái | Evidence | Owner |
| --- | --- | --- | --- | --- | --- |
| Chưa xác định | Chưa xác định | Chưa xác định | NOT_RUN | Chưa có | Chưa phân công |

Trạng thái: PASS, FAIL, BLOCKED, NOT_RUN, NOT_APPLICABLE. NOT_APPLICABLE cần lý do và người chịu trách nhiệm chấp nhận phạm vi; không dùng để bỏ qua yêu cầu bắt buộc.

## Checklist lựa chọn theo rủi ro

- [ ] AC và snapshot đã chốt.
- [ ] Các kiểm tra bắt buộc đã chạy, có kết quả thực và giới hạn.
- [ ] Findings được phân loại; không còn blocker trong phạm vi bắt buộc.
- [ ] Tương thích contract và dữ liệu đã được xem xét khi liên quan.
- [ ] Reviewer độc lập hoặc giới hạn tự kiểm đã được ghi rõ.
- [ ] Quyền cho bước tiếp theo được đối chiếu với yêu cầu người dùng.

Các ô trên chưa được thực hiện. Chỉ đánh dấu khi có evidence tương ứng.

## Quyết định

Ghi APPROVED hoặc REJECTED sau đánh giá; hiện tại NOT_RUN. Nêu lý do, phần chưa kiểm chứng, owner và bước sửa. Qua cổng chất lượng không tự cấp quyền merge, deploy hay sửa production.
