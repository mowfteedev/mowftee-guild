# Bảo trì, tối ưu và audit

Xử lý nợ kỹ thuật hoặc rủi ro theo mức ưu tiên có bằng chứng, bảo toàn nghiệp vụ đã chốt.

Đây là trình tự tham khảo cho dự án cá nhân. Một trợ lý có thể lần lượt làm các phần; bỏ bước không liên quan, không cần hội đồng duyệt hoặc tạo đủ hồ sơ.

## Gợi ý thực hiện

1. Lập findings có trigger, tác động và nguồn; phân biệt lỗi với hardening hoặc sở thích.
2. Thay đổi nhỏ theo từng mục tiêu; tách bugfix, dependency upgrade và tối ưu nếu semantics khác.
3. Kiểm lại finding, regression và so trước/sau trong điều kiện tương đương.
4. Cập nhật risk/debt ledger, giữ lịch sử mục đã xử lý và kế hoạch phần còn lại.

## Kiểm tra và kết thúc

Đối chiếu kết quả với yêu cầu thật, tự phản biện các trường hợp dễ sai và chạy kiểm tra phù hợp với phần thay đổi. Ghi điều đã thử và phần chưa thử; không cần điền biểu mẫu chỉ để đủ quy trình.

Chỉ dùng [mẫu memory](../templates/memory/progress.md) nếu cần lưu ghi chú. Các [skill chuyên môn](../docs/skills-catalog.md) cung cấp chi tiết cho từng phần; không bắt buộc gọi cả bộ.
