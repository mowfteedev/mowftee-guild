# Thêm tính năng và kiểm soát hồi quy

Thêm hành vi mới theo AC mà vẫn giữ các contract/hành vi cũ thuộc phạm vi hỗ trợ.

Đọc yêu cầu mới cùng hành vi đang được hỗ trợ trước khi đổi code. Xác định caller, contract, dữ liệu và cách kiểm vùng ảnh hưởng.

## Gợi ý thực hiện

1. Ghi AC và vùng ảnh hưởng; phân loại lỗi baseline tồn tại trước thay đổi.
2. Thực hiện thay đổi; migration-specialist quản lý expand/backfill/cutover khi cần.
3. Chạy checks vùng ảnh hưởng, kiểm tương thích consumer và hành vi mới. Nếu phát hiện lỗi, dùng [workflow sửa lỗi](04-sua-loi.md); tách lỗi baseline với lỗi mới bằng dữ kiện.
4. Cập nhật hướng dẫn hoặc contract thực sự đổi; chỉ lưu ghi chú khi hữu ích. Push/merge/deploy theo phạm vi đã được cấp.

## Kiểm tra và kết thúc

Đối chiếu tiêu chí mới và các hành vi cũ chịu tác động, ghi kết quả theo phiên bản đã thử. Bước chưa nối hoặc chưa chạy cần được nêu trong bàn giao; không đổi kỳ vọng để hợp thức regression.

[Chọn workflow khác](README.md) · [Danh mục skill](../docs/skills-catalog.md)
