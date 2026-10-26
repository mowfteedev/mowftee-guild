# Runbook: Khả năng tiếp cận

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Nút chỉ có icon: cần accessible name đúng chức năng.
2. Modal đóng: focus trở về điểm hợp lý.
3. Chữ lớn và chữ thường: chọn ngưỡng đúng, không áp máy móc.
4. Không có screen reader: báo chưa kiểm tra thay vì suy diễn PASS.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Keyboard/focus | Đi qua luồng không dùng chuột; kiểm order, visible focus, trap và return focus. | Danh sách bước, browser và kết quả từng interaction. |
| Name/role/state | Kiểm semantic HTML và accessible name/state theo hành vi; tránh ARIA che semantics sai. | Accessibility tree hoặc thao tác screen reader nếu có. |
| Form/errors | Liên kết label/help/error, hỗ trợ correction và thông báo thay đổi quan trọng. | Ca dữ liệu lỗi và cách công nghệ hỗ trợ nhận biết. |
| Visual/reflow | Chọn tiêu chuẩn áp dụng, phân loại text/UI cho contrast; kiểm zoom/reflow/reduced motion. | Số đo hoặc ảnh ở điều kiện cụ thể, không badge chứng nhận. |
| Tool coverage | Kết hợp scanner và manual; ghi assistive tech nào chưa chạy. | Tool/version, findings, manual coverage và residual limitations. |

## Đầu ra cần giữ khi liên quan

- Audit scope: tiêu chuẩn, component, browser/assistive tech.
- Findings: tác động người dùng, reproduction và remediation.
- Evidence: automated/manual tách riêng, phần chưa thử.

## Điều kiện dừng phần phụ thuộc

Không có điều kiện kiểm tra một tiêu chí bắt buộc; không suy scanner pass thành chứng nhận accessibility toàn diện. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ kiểm thủ công: dialog xác nhận xóa

Đi theo thao tác người dùng bằng bàn phím, rồi đối chiếu name/role/state của dialog và nút. Không bắt đầu bằng thêm ARIA khi semantic HTML hoặc component sẵn có đã hỗ trợ đúng.

1. Focus nút mở và kích hoạt bằng bàn phím. Khi dialog xuất hiện, xác định điểm focus ban đầu phù hợp với nội dung và mức nguy hiểm của hành động.
2. Di chuyển bằng Tab/Shift+Tab. Với modal, focus không đi vào nội dung nền không tương tác; vòng di chuyển vẫn có cách hủy/đóng theo thiết kế.
3. Kiểm tên dialog, nội dung xác nhận và nhãn nút trong accessibility tree; nếu có screen reader thì thử luồng trên công nghệ hỗ trợ được chỉ định.
4. Hủy dialog và kiểm focus quay về vị trí hợp lý. Nếu xác nhận xóa làm nút mở biến mất, phải có đích focus còn tồn tại, không đặt vào node đã bị gỡ.
5. Làm nội dung dài và zoom theo phạm vi hỗ trợ; vẫn tiếp cận được nội dung và thao tác, focus nhìn thấy được.

Lỗi “focus rơi về đầu trang sau xóa” cần kèm bước tái hiện, browser/assistive tech đã dùng và tác động cho người chỉ dùng bàn phím. Scanner có thể không phát hiện đầy đủ chuỗi tương tác này.

Nếu chưa có screen reader, ghi đã kiểm bàn phím/tree và chưa kiểm trải nghiệm đọc thực. Không suy một dialog đạt thành toàn ứng dụng đạt tiêu chuẩn; mỗi kết luận gắn với phạm vi và tiêu chí đã đối chiếu.
