# Từ ý tưởng đến MVP

Tạo MVP có phạm vi kiểm chứng được, kiến trúc phù hợp và bàn giao có thể chạy theo tài liệu.

Đây là trình tự tham khảo cho dự án cá nhân. Một trợ lý có thể lần lượt làm các phần; bỏ bước không liên quan, không cần hội đồng duyệt hoặc tạo đủ hồ sơ.

## Gợi ý thực hiện

1. Viết AC, happy/error path, ngoài scope và câu hỏi quan trọng.
2. Chọn phương án phù hợp, thiết kế contract/schema/spec, ghi ADR có đánh đổi; migration có owner riêng.
3. Chia vùng file, triển khai theo cấu trúc hiện hữu; test-automator bổ sung checks có giá trị.
4. Đối chiếu AC, khám phá lỗi biên, quyền và phục hồi; chọn mức fuzz/load theo môi trường được phép.
5. Kiểm cách build/chạy, ghi prerequisites, rollout/rollback và giới hạn; chỉ thực hiện action đã được phép.

## Kiểm tra và kết thúc

Đối chiếu kết quả với yêu cầu thật, tự phản biện các trường hợp dễ sai và chạy kiểm tra phù hợp với phần thay đổi. Ghi điều đã thử và phần chưa thử; không cần điền biểu mẫu chỉ để đủ quy trình.

Chỉ dùng [mẫu memory](../templates/memory/progress.md) nếu cần lưu ghi chú. Các [skill chuyên môn](../docs/skills-catalog.md) cung cấp chi tiết cho từng phần; không bắt buộc gọi cả bộ.
