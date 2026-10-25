# Runbook: Điều phối kỹ thuật

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Chỉ sửa một lỗi chính tả: giao trực tiếp, không dựng hội đồng.
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

## Hợp đồng đầu ra khi bàn giao

- Task map: owner, scope, dependency, AC, evidence.
- Decision log: dữ kiện, lựa chọn, hệ quả, người quyết định.
- Handoff: phần hoàn tất, phần chưa chạy, điều kiện mở bước sau.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Chưa xác định được nguyên nhân sau các cách đã thử; thiếu quyền bước cần thiết; hoặc contract giữa hai nhánh còn mâu thuẫn. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
