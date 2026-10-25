# Sửa lỗi từ tái hiện đến kiểm chứng

Khắc phục nguyên nhân có bằng chứng trong phạm vi nhỏ nhất và tránh regression liên quan.

Đây là trình tự tham khảo cho dự án cá nhân. Một trợ lý có thể lần lượt làm các phần; bỏ bước không liên quan, không cần hội đồng duyệt hoặc tạo đủ hồ sơ.

## Gợi ý thực hiện

1. Ghi bước tái hiện và kiểm tra hành vi trên baseline; phân biệt giả thuyết và quan sát.
2. Sửa nhỏ nhất, giữ contract và lỗi ngoài phạm vi; thêm regression test khi có giá trị.
3. Chạy ca tái hiện, regression vùng ảnh hưởng và các nhánh phục hồi quan trọng.
4. Tóm tắt trigger, thay đổi, tests, giới hạn và bước phát hành nếu được yêu cầu.

## Kiểm tra và kết thúc

Đối chiếu kết quả với yêu cầu thật, tự phản biện các trường hợp dễ sai và chạy kiểm tra phù hợp với phần thay đổi. Ghi điều đã thử và phần chưa thử; không cần điền biểu mẫu chỉ để đủ quy trình.

Chỉ dùng [mẫu memory](../templates/memory/progress.md) nếu cần lưu ghi chú. Các [skill chuyên môn](../docs/skills-catalog.md) cung cấp chi tiết cho từng phần; không bắt buộc gọi cả bộ.
