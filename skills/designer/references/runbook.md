# Runbook: Thiết kế UI và UX

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Bảng dữ liệu dày trên mobile: chọn ưu tiên cột hoặc cách cuộn có chỉ dẫn.
2. Lỗi validation: liên kết thông báo với trường và cách sửa.
3. Chỉ sửa giao diện sẵn có: giữ ngôn ngữ thương hiệu của dự án.
4. Đề xuất animation: có hành vi khi reduced motion bật.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Thiết kế mới trong sản phẩm cũ | Tái sử dụng token và pattern hiện có trước khi đề xuất khác biệt. | Component spec có token và lý do ngoại lệ. |
| Nút có side effect | Đặc tả pending, disabled, thành công, lỗi, retry và hủy nếu có. | State table với hành động và phản hồi người dùng. |
| Form validation | Chỉ rõ thời điểm lỗi, vị trí thông báo, dữ liệu giữ lại và hướng sửa. | Ví dụ input lỗi và trạng thái sau submit. |
| Responsive và nội dung dài | Chọn ưu tiên nội dung, wrapping, overflow có chủ đích và hành vi zoom. | Spec ở viewport mục tiêu cùng dữ liệu dài. |
| Hiệu ứng chuyển động | Có reduced-motion và tránh làm mất nội dung hoặc focus. | Thông số tương tác và cách đối chiếu trên bản chạy. |

## Hợp đồng đầu ra khi bàn giao

- UX flow: mục tiêu, nhánh lỗi/hủy/retry.
- Component spec: tokens, states, responsive và nội dung dài.
- Handoff: ví dụ có dữ liệu đại diện và tiêu chí đối chiếu.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Thiếu quyết định sản phẩm chặn luồng; token đề xuất không khả thi; hoặc chưa được phép đổi ngôn ngữ thiết kế toàn hệ thống. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
