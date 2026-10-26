# Runbook: Điều phối kỹ thuật

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Chỉ sửa một lỗi chính tả: sửa trực tiếp và xem lại diff.
2. Hai cách giải thích trái nhau: kiểm tra cùng phiên bản và tái hiện để chọn cách có bằng chứng.
3. Làm một mình: chia phần hợp lý, triển khai lần lượt rồi tự kiểm kết quả.
4. Bị giới hạn READ-ONLY: chỉ phân tích và đề xuất, không ghi progress vào dự án.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Nhiều đầu việc độc lập | Phân ranh giới file và contract trước khi song song; chỉ chia việc nếu có lợi hơn chi phí bàn giao. | Task map có owner, dependency và output cụ thể. |
| Đổi nhiều phần cùng file | Chia thay đổi thành các bước nhỏ để dễ đọc diff và tìm lỗi. | Diff và kiểm tra tương ứng với từng phần. |
| Partial completion | Giữ phần thành công đã kiểm chứng, xác định phần thất bại ảnh hưởng tiêu chí nào. | Bảng AC có trạng thái riêng, không một nhãn chung che lỗi. |
| Đánh giá mâu thuẫn | So commit, môi trường và dữ liệu trước khi chọn phương án. | Hai nguồn evidence và kết quả tái hiện cùng điều kiện. |
| Cần tự phản biện | Đọc lại giả định, diff và trường hợp biên; không cần thêm người duyệt. | Phát hiện thực tế, điều đã thử và giới hạn còn lại. |

## Đầu ra cần giữ khi liên quan

- Kế hoạch ngắn khi có nhiều phần: phạm vi, phụ thuộc và cách kiểm kết quả.
- Quyết định đáng giữ lại: dữ kiện, lựa chọn và hệ quả.
- Bàn giao: phần hoàn tất, phần chưa chạy và bước tiếp theo.

## Điều kiện dừng phần phụ thuộc

Chưa xác định được nguyên nhân sau các cách đã thử; thiếu quyền bước cần thiết; hoặc contract giữa hai nhánh còn mâu thuẫn. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ: thêm tính năng xuất danh sách đơn hàng

Yêu cầu “thêm nút xuất CSV” thường chạm vào quyền đọc, bộ lọc hiện tại, dữ liệu và UI. Đọc luồng đang có để xác định phần thật sự thiếu trước khi chia việc.

| Phát hiện từ repo | Cách triển khai phù hợp |
| --- | --- |
| Đã có endpoint xuất, chỉ thiếu nút | Nối UI với contract hiện có; thử quyền, bộ lọc và trạng thái lỗi. |
| Chưa có endpoint, dữ liệu ít trong giới hạn đã biết | Cân nhắc xử lý đồng bộ; giữ cùng điều kiện lọc và phân quyền với danh sách. |
| Dữ liệu lớn hoặc vượt thời gian request thực tế | Khảo sát giới hạn và nhu cầu trước khi chọn streaming hay job nền; không tự thêm queue. |

Thứ tự hợp lý khi cần cả server và UI: chốt cột/quyền/phạm vi lọc → làm đường xuất → nối UI → đối chiếu file với dữ liệu nguồn. Không cần tổ chức các bước thành các agent riêng.

Tự phản biện bằng ba câu hỏi: file có vô tình chứa đơn ngoài tenant không; “xuất tất cả” là toàn bộ kết quả lọc hay chỉ trang đang xem; lỗi giữa lúc tải có để lại một file trông như hoàn chỉnh không? Câu hỏi làm đổi ý nghĩa sản phẩm phải được chốt, còn nhãn nút hay cách đặt helper có thể theo quy ước repo.

Kế hoạch đủ dùng cho việc nhỏ có thể chỉ là vài dòng trong hội thoại. Chỉ tạo task map hoặc decision log khi nó giúp theo dõi nhiều phần phụ thuộc.
