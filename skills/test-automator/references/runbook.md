# Runbook: Tự động hóa kiểm thử

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. API trả chậm: đợi điều kiện hoàn tất thay vì ngủ cố định.
2. Test pass sau retry: ghi flakiness, không gọi là ổn định tuyệt đối.
3. Không có browser cài sẵn: báo BLOCKED và giữ phần test có thể chạy.
4. Logic đơn giản, sửa tài liệu: không tự thêm suite chỉ để đủ hình thức.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Chọn mức test | Unit cho logic cô lập, integration cho boundary thực, contract cho consumer và E2E cho luồng quan trọng. | AC-to-test map cùng lý do chọn mức. |
| Dữ liệu và isolation | Test sở hữu fixture, dùng key riêng và cleanup đúng phạm vi; không dùng chung seed mutable. | Chạy test riêng, cùng suite và song song theo cấu hình dự án. |
| Chờ kết quả | Dùng điều kiện/event thật với deadline; đăng ký chờ trước trigger khi API/browser yêu cầu. | Trace hoặc assertion phản ánh trạng thái nghiệp vụ. |
| Mock boundary | Mock phần không phải đối tượng kiểm tra; thêm lớp test boundary thật khi cần. | Danh sách mock và điều chưa được chứng minh. |
| Flaky/regression | Tái hiện điều kiện lỗi, xem trace/race; không tăng retry hay đổi assertion để che bug. | Kết quả baseline, bản sửa và các lần chạy có đủ log. |

## Hợp đồng đầu ra khi bàn giao

- Test plan: AC, level, fixture và observable behavior.
- Test artifacts: source, command, exit code, report/trace.
- Limitations: mock, môi trường thiếu và flaky còn mở.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Test yêu cầu môi trường không được phép, payload có thể gây hại hoặc kết quả không thể tái lập do thiếu dữ liệu quan trọng. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
