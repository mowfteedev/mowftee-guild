# Từ ý tưởng đến MVP

Tạo MVP có phạm vi kiểm chứng được, kiến trúc phù hợp và bàn giao có thể chạy theo tài liệu.

Đầu vào cần rõ: người sử dụng, vấn đề, phần tối thiểu phải làm được và ràng buộc hiện có. Dùng `product-analyst` cho yêu cầu, `software-architect` cho đánh đổi và chuyên môn triển khai tương ứng.

## Gợi ý thực hiện

1. Viết AC, happy/error path, ngoài scope và câu hỏi quan trọng.
2. Chọn phương án phù hợp, thiết kế contract/schema/spec; chỉ ghi ADR khi có quyết định đáng giữ. Nếu có dữ liệu đang dùng, xem riêng việc chuyển đổi và phục hồi.
3. Chia vùng file, triển khai theo cấu trúc hiện hữu; test-automator bổ sung checks có giá trị.
4. Đối chiếu tiêu chí, thử lỗi biên, quyền và phục hồi theo tác động. Có lỗi cụ thể thì theo [workflow sửa lỗi](04-sua-loi.md), không sửa bằng phỏng đoán.
5. Kiểm cách build/chạy, ghi prerequisites, rollout/rollback và giới hạn; chỉ thực hiện action đã được phép.

## Kiểm tra và kết thúc

Một người khác phải hiểu cách chạy, luồng cốt lõi nào đã được thử và phần nào còn thiếu. Bản chưa nối dịch vụ thật cần nói rõ mock; không gọi giao diện mẫu là một MVP đã chạy đầu cuối.

[Chọn workflow khác](README.md) · [Danh mục skill](../docs/skills-catalog.md)
