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

## Đầu ra cần giữ khi liên quan

- UX flow: mục tiêu, nhánh lỗi/hủy/retry.
- Component spec: tokens, states, responsive và nội dung dài.
- Handoff: ví dụ có dữ liệu đại diện và tiêu chí đối chiếu.

## Điều kiện dừng phần phụ thuộc

Thiếu quyết định sản phẩm chặn luồng; token đề xuất không khả thi; hoặc chưa được phép đổi ngôn ngữ thiết kế toàn hệ thống. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ đặc tả: hộp thoại xóa một tài liệu

Trước khi vẽ, xác định thao tác có đảo ngược được không, tài liệu có đang được dùng chung không, và UI có cần giải thích tác động cho người dùng. Dùng token, kiểu dialog và cách viết thông báo hiện có.

| Trạng thái | Nội dung và tương tác cần xác định |
| --- | --- |
| Mở xác nhận | Tên tài liệu, tác động xóa, nút hủy và nút xác nhận có nhãn rõ. |
| Đang gửi | Hiển thị tiến độ phù hợp, tránh gửi lặp; quy định việc đóng dialog trong lúc chờ. |
| Xóa thành công | Đóng dialog và cập nhật danh sách; đặt focus vào vị trí còn tồn tại, hợp lý. |
| Bị từ chối hoặc đang có người sử dụng | Giải thích nguyên nhân từ server, giữ ngữ cảnh để người dùng chọn bước tiếp. |
| Mất mạng, chưa biết kết quả | Không khẳng định chưa xóa; cho kiểm tra lại trạng thái trước khi thử lại. |

Nếu đóng dialog không hủy được request phía server, không đặt tên thao tác đó là “hủy xóa”. Nội dung dài cần wrap mà vẫn giữ được tên tài liệu và nút hành động trong viewport mục tiêu.

Bàn giao gồm state table, nội dung thông báo, vị trí focus khi mở/đóng và cách bố trí trên màn hình nhỏ. Một ảnh trạng thái mặc định chưa mô tả đủ tương tác để frontend triển khai.
