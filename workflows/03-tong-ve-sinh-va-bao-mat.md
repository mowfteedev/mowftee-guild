# Bảo trì, tối ưu và audit

Xử lý nợ kỹ thuật hoặc rủi ro theo mức ưu tiên có bằng chứng, bảo toàn nghiệp vụ đã chốt.

Chọn mục tiêu trước: lỗi đúng đắn, rủi ro bảo mật, chi phí vận hành, hiệu năng hay khả năng bảo trì. Dùng chuyên môn đúng mục tiêu thay vì tự mở rộng thành audit toàn repo.

## Gợi ý thực hiện

1. Lập findings có trigger, tác động và nguồn; phân biệt lỗi với hardening hoặc sở thích.
2. Thay đổi nhỏ theo từng mục tiêu; với bugfix theo [bốn bước sửa lỗi](04-sua-loi.md). Tách dependency upgrade và tối ưu khi cần kiểm chứng hành vi hoặc phép đo khác.
3. Kiểm lại finding, regression và so trước/sau trong điều kiện tương đương.
4. Tóm tắt mục đã xử lý, căn cứ và phần còn lại. Chỉ ghi sổ rủi ro/nợ kỹ thuật nếu dự án đang dùng hoặc cần giữ kết quả.

## Kiểm tra và kết thúc

Bugfix cần kết quả ca lỗi trước/sau, tối ưu cần phép đo tương đương, còn refactor cần căn cứ giữ hành vi. Nêu đúng loại kết quả; diff ít dòng hơn chưa đủ để kết luận nhanh hơn hoặc an toàn hơn.

[Chọn workflow khác](README.md) · [Danh mục skill](../docs/skills-catalog.md)
