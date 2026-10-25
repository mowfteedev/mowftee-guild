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

## Hợp đồng đầu ra khi bàn giao

- Audit scope: tiêu chuẩn, component, browser/assistive tech.
- Findings: tác động người dùng, reproduction và remediation.
- Evidence: automated/manual tách riêng, phần chưa thử.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Không có điều kiện kiểm tra một tiêu chí bắt buộc; không suy scanner pass thành chứng nhận accessibility toàn diện. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
