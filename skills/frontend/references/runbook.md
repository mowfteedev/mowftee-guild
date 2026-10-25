# Runbook: Phát triển giao diện

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. API trả mảng rỗng: hiển thị trạng thái trống có ý nghĩa.
2. Mạng mất giữa submit: giữ thông tin phục hồi, không tự báo thành công.
3. Tên sản phẩm rất dài: bố cục không che thao tác chính.
4. Optimistic update lỗi: rollback có xét các cập nhật đồng thời.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Dữ liệu bất đồng bộ | Tách loading ban đầu, refetch, stale, empty, error và partial result khi sản phẩm có. | Ca kiểm chứng API chậm, rỗng, lỗi và dữ liệu thay đổi. |
| Submit hoặc retry | Giữ dữ liệu nhập, phản hồi pending, chặn click lặp và phối hợp key server. | Network trace và side effect quan sát được, không chỉ toast. |
| Optimistic update | Giữ rollback theo mutation và xử lý cập nhật đồng thời; tránh ghi đè dữ liệu mới hơn. | Ca request lỗi, phản hồi đảo thứ tự và mutation liên tiếp. |
| Layout và lifecycle | Tìm phần tử gây tràn; xử lý cleanup, cancellation và stale result theo framework. | Ảnh viewport, console và test khi unmount/đổi route. |
| Quyền và dữ liệu | Ẩn UI chỉ là trải nghiệm; backend vẫn phải kiểm quyền và đầu vào. | Ca người dùng khác, server rejection và không lộ dữ liệu qua cache. |

## Hợp đồng đầu ra khi bàn giao

- UI diff: component, state và contract liên quan.
- Verification: viewport/keyboard/console/network đúng snapshot.
- Boundary report: mock nào dùng, browser nào thử và phần chưa chạy.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Contract chưa rõ hoặc API không có điều kiện test; ghi giới hạn thay vì thay bằng mock rồi cấp PASS tích hợp. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
