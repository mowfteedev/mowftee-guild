# Ứng phó sự cố và postmortem

Giảm tác động trong quyền đã có, giữ bằng chứng và biến sự cố thành hành động cải thiện rõ owner.

Đây là trình tự tham khảo cho dự án cá nhân. Một trợ lý có thể lần lượt làm các phần; bỏ bước không liên quan, không cần hội đồng duyệt hoặc tạo đủ hồ sơ.

## Gợi ý thực hiện

1. Đo ảnh hưởng người dùng, thu dữ liệu an toàn và ghi giả thuyết có thể kiểm chứng.
2. Chọn hành động nhỏ có thể đảo ngược, ghi trước/sau và điểm dừng; thay một biến khi có thể.
3. Kiểm user journey và độ ổn định trong cửa sổ phù hợp, giữ residual risk.
4. Ghi yếu tố góp phần, điều hiệu quả, việc cần sửa và kiểm chứng tái diễn.

## Kiểm tra và kết thúc

Đối chiếu kết quả với yêu cầu thật, tự phản biện các trường hợp dễ sai và chạy kiểm tra phù hợp với phần thay đổi. Ghi điều đã thử và phần chưa thử; không cần điền biểu mẫu chỉ để đủ quy trình.

Chỉ dùng [mẫu memory](../templates/memory/progress.md) nếu cần lưu ghi chú. Các [skill chuyên môn](../docs/skills-catalog.md) cung cấp chi tiết cho từng phần; không bắt buộc gọi cả bộ.
