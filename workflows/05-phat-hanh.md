# Phát hành có kiểm soát

Đảm bảo đúng artifact, đúng quyền và có tín hiệu dừng hoặc phục hồi khi phát hành.

Đây là trình tự tham khảo cho dự án cá nhân. Một trợ lý có thể lần lượt làm các phần; bỏ bước không liên quan, không cần hội đồng duyệt hoặc tạo đủ hồ sơ.

## Gợi ý thực hiện

1. Đối chiếu AC, artifact, thay đổi kể từ evidence và giới hạn được chấp nhận.
2. Kiểm prerequisites, ordering, feature flags, migration và khả năng rollback hoặc roll-forward.
3. Thực hiện đúng phần được cho phép, ghi URL/SHA/id; không force-push hoặc mở rộng môi trường.
4. Kiểm remote SHA hoặc tín hiệu runtime tương ứng, cập nhật docs/notes và owner.

## Kiểm tra và kết thúc

Đối chiếu kết quả với yêu cầu thật, tự phản biện các trường hợp dễ sai và chạy kiểm tra phù hợp với phần thay đổi. Ghi điều đã thử và phần chưa thử; không cần điền biểu mẫu chỉ để đủ quy trình.

Chỉ dùng [mẫu memory](../templates/memory/progress.md) nếu cần lưu ghi chú. Các [skill chuyên môn](../docs/skills-catalog.md) cung cấp chi tiết cho từng phần; không bắt buộc gọi cả bộ.
