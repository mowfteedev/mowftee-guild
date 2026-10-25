# Thêm tính năng và kiểm soát hồi quy

Thêm hành vi mới theo AC mà vẫn giữ các contract/hành vi cũ thuộc phạm vi hỗ trợ.

Đây là trình tự tham khảo cho dự án cá nhân. Một trợ lý có thể lần lượt làm các phần; bỏ bước không liên quan, không cần hội đồng duyệt hoặc tạo đủ hồ sơ.

## Gợi ý thực hiện

1. Ghi AC và vùng ảnh hưởng; phân loại lỗi baseline tồn tại trước thay đổi.
2. Thực hiện thay đổi; migration-specialist quản lý expand/backfill/cutover khi cần.
3. Chạy checks vùng ảnh hưởng, kiểm tương thích consumer và hành vi mới; điều tra retry/flaky thật.
4. Cập nhật docs/API/changelog/memory được phép; push/merge/deploy theo quyền riêng.

## Kiểm tra và kết thúc

Đối chiếu kết quả với yêu cầu thật, tự phản biện các trường hợp dễ sai và chạy kiểm tra phù hợp với phần thay đổi. Ghi điều đã thử và phần chưa thử; không cần điền biểu mẫu chỉ để đủ quy trình.

Chỉ dùng [mẫu memory](../templates/memory/progress.md) nếu cần lưu ghi chú. Các [skill chuyên môn](../docs/skills-catalog.md) cung cấp chi tiết cho từng phần; không bắt buộc gọi cả bộ.
