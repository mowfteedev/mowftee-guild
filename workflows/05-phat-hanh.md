# Phát hành có kiểm soát

Đảm bảo đúng artifact, đúng quyền và có tín hiệu dừng hoặc phục hồi khi phát hành.

Xác định hành động cần làm: push nhánh để xem, tạo bản phát hành hay triển khai dịch vụ. Chọn mức kiểm tương ứng; yêu cầu push không tự bao gồm merge, tag hoặc deploy.

## Gợi ý thực hiện

1. Đối chiếu AC, artifact, thay đổi kể từ evidence và giới hạn được chấp nhận.
2. Nếu triển khai, kiểm prerequisites, thứ tự app/schema, migration và cách phục hồi. Nếu chỉ push tài liệu, kiểm nội dung, liên kết và các check liên quan của repo.
3. Thực hiện đúng phần được cho phép, ghi URL/SHA/id; không force-push hoặc mở rộng môi trường.
4. Kiểm remote SHA hoặc tín hiệu runtime tương ứng, ghi kết quả thật và việc còn chờ.

## Kiểm tra và kết thúc

Link nhánh/commit, check CI hoặc deployment phải trỏ tới đúng phiên bản đang bàn giao. CI còn chạy thì ghi đang chạy; service khởi động chưa chứng minh luồng người dùng đã phục hồi. Có lỗi cụ thể thì quay lại [điều tra nguyên nhân](04-sua-loi.md).

[Chọn workflow khác](README.md) · [Skill release-manager](../skills/release-manager/SKILL.md)
