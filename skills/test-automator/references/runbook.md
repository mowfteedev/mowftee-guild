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

## Đầu ra cần giữ khi liên quan

- Test plan: AC, level, fixture và observable behavior.
- Test artifacts: source, command, exit code, report/trace.
- Limitations: mock, môi trường thiếu và flaky còn mở.

## Điều kiện dừng phần phụ thuộc

Test yêu cầu môi trường không được phép, payload có thể gây hại hoặc kết quả không thể tái lập do thiếu dữ liệu quan trọng. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Kiểm chứng ca hồi quy trước và sau bản sửa

- Giữ input và kỳ vọng từ hành vi đã thống nhất. Chạy trên bản lỗi để kiểm assertion thất bại vì triệu chứng, rồi chạy cùng ca trên bản sửa; lưu phần output quan trọng và exit code của từng lần.
- Nếu test xanh ngay trên bản lỗi, xem test có đi qua đúng nhánh, mock có che cơ chế lỗi, hoặc assertion có chỉ kiểm chi tiết không liên quan. Chỉnh ca để đo đúng hành vi; không tự tạo lỗi khác nhằm có một lần đỏ.
- Nếu không có baseline hoặc môi trường cần thiết, ghi rõ. Không ghi đè thay đổi đang có để lấy bản lỗi và không đưa một ca giả lập thành bằng chứng đã tái hiện lỗi gốc.
- Chạy tiếp các kiểm tra caller, nhánh lỗi và dữ liệu bị ảnh hưởng. Một lần xanh chưa loại trừ flaky; không bỏ các lần đỏ khỏi báo cáo hoặc tăng retry để che chúng.
- Kết quả CI dùng được khi đúng commit/artifact, môi trường và phạm vi kiểm tra liên quan. Sau thay đổi có thể tác động kết luận, chạy lại phần bị ảnh hưởng; không bắt chạy mọi test ở mỗi lượt chat.

## Ví dụ chọn test: nút “Lưu” bị gửi lặp

Tách hai yêu cầu: UI phản hồi đúng khi click nhanh, và server không tạo hai bản ghi nếu request bị gửi lại. Hai yêu cầu cần quan sát khác nhau.

| Mức kiểm tra | Điều nên khẳng định | Giới hạn |
| --- | --- | --- |
| Component/UI với request được giữ pending | Hai click nhanh không tạo hai mutation trong luồng UI đã chọn; nút/state phục hồi sau lỗi | Không chứng minh server chống retry từ client khác. |
| Integration qua API và DB thử | Cùng key/payload không tạo hai hiệu lực; khác payload không replay sai | Phải dùng DB và cơ chế idempotency thực thuộc đối tượng kiểm tra. |
| E2E luồng chính khi cần | Người dùng lưu và nhìn thấy đúng dữ liệu server đã ghi | Không thay thế các interleaving khó điều khiển bằng một luồng chậm thông thường. |

Điều khiển pending bằng promise/event/barrier của môi trường test thay vì `sleep` cố định. Với test race ở backend, cho hai request đến điểm cạnh tranh trước khi mở barrier; assertion là dữ liệu cuối cùng và kết quả từng request, không phải tên hàm nội bộ được gọi.

Một test hồi quy hữu ích phải thất bại khi tái hiện lỗi cũ trong điều kiện kiểm soát được và thành công với bản sửa. Nếu phải mock chính logic chống lặp để test xanh thì test chưa bảo vệ yêu cầu này. Không cần thêm cả ba lớp test nếu lỗi và phạm vi chỉ yêu cầu một lớp đã đủ chứng minh.
