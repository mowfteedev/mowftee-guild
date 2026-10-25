# Runbook: Điều phối kỹ thuật

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Chỉ sửa một lỗi chính tả: giao trực tiếp, không dựng hội đồng.
2. Hai agent đưa kết luận trái nhau: kiểm tra cùng commit và tái hiện trước khi phân xử.
3. Không có subagent: triển khai tuần tự, ghi rõ thiếu đánh giá độc lập.
4. Bị giới hạn READ-ONLY: chỉ phân tích và đề xuất, không ghi progress vào dự án.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Nhiều đầu việc độc lập | Phân ranh giới file và contract trước khi song song; chỉ chia việc nếu có lợi hơn chi phí bàn giao. | Task map có owner, dependency và output cụ thể. |
| Hai người sửa cùng file | Làm tuần tự hoặc tách vùng thay đổi; nếu cần isolation thì dùng worktree thực. | Đường dẫn workspace thực và diff từng owner. |
| Partial completion | Giữ phần thành công đã kiểm chứng, xác định phần thất bại ảnh hưởng tiêu chí nào. | Bảng AC có trạng thái riêng, không một nhãn chung che lỗi. |
| Đánh giá mâu thuẫn | So commit, môi trường và dữ liệu trước khi chọn phương án. | Hai nguồn evidence và kết quả tái hiện cùng điều kiện. |
| Reviewer chưa có | Ghi self-check hoặc pending independent review; không tự ký thay. | Hồ sơ bàn giao nêu rõ người thực hiện thật và giới hạn. |

## Hợp đồng đầu ra khi bàn giao

- Task map: owner, scope, dependency, AC, evidence.
- Decision log: dữ kiện, lựa chọn, hệ quả, người quyết định.
- Handoff: phần hoàn tất, phần chưa chạy, điều kiện mở bước sau.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Không hội tụ sau giới hạn vòng sửa; thiếu quyền bước cần thiết; hoặc contract giữa hai nhánh còn mâu thuẫn. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
