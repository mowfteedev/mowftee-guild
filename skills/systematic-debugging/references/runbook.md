# Runbook: điều tra lỗi và đối chiếu bằng chứng

## Phân biệt bằng chứng với dấu hiệu

| Tình huống | Cách xử lý | Giới hạn kết luận |
| --- | --- | --- |
| Test đỏ vì import hoặc thiếu dependency | Sửa điều kiện chạy trong phạm vi được phép rồi chạy lại ca lỗi. | Chưa tái hiện được lỗi mục tiêu. |
| Ca hồi quy xanh ngay trên bản lỗi | Kiểm input, đường thực thi, fixture và assertion; thử xem ca có thực sự chạm điều kiện lỗi không. | Ca này chưa chứng minh được tác dụng của bản sửa. |
| Ca ban đầu xanh sau sửa, luồng hợp lệ khác đỏ | Truy vùng ảnh hưởng và so baseline của luồng đó. | Chưa thể kết luận bản sửa đạt yêu cầu liên quan. |
| Chỉ có log/trace từ môi trường xảy ra lỗi | Theo dữ kiện tới code tương ứng; kiểm điều kiện gây lỗi và giữ phần còn chưa tái hiện. | Không gọi phân tích log là đã chạy tái hiện local. |
| Lỗi chập chờn hoặc race | Điều khiển thứ tự/event khi có thể; ghi số lần, điều kiện và cả lần thất bại. | Một lần xanh hoặc retry che lỗi chưa chứng minh ổn định. |
| Kết quả CI có sẵn | Kiểm commit/artifact, phạm vi check và môi trường trước khi dùng. | CI đúng commit không tự bao phủ những ca không được chạy. |
| Bằng chứng ở working tree chưa commit | Ghi trạng thái lúc chạy và kiểm các diff phát sinh sau đó. | Không gán kết quả cho commit cuối nếu code liên quan đã đổi. |

## Ví dụ: thao tác lưu bị thực hiện hai lần

Giả sử yêu cầu đã chốt rằng một lần lưu không được tạo hai bản ghi. Người dùng báo thấy bản ghi lặp, nhưng nguyên nhân có thể ở UI gửi hai request, client retry sau mất response hoặc server xử lý lại cùng yêu cầu.

1. **Quan sát trước:** tìm thao tác, request và dữ liệu tương ứng trong môi trường được phép. Hai dòng trong UI chưa chứng minh DB có hai bản ghi; một request trong UI chưa loại trừ retry ở tầng khác.
2. **Tái hiện:** chọn đúng điều kiện được quan sát, chẳng hạn gửi lại cùng request sau khi kết quả đầu đã được lưu. Ca thất bại phải chỉ ra hiệu lực nghiệp vụ bị lặp, không chỉ hàm được gọi hai lần.
3. **Phân biệt giả thuyết:** đối chiếu request identity, log và dữ liệu để xác định tầng tạo hiệu lực lặp. Chặn click ở UI không giải quyết được retry trực tiếp đến API; cũng không tự thêm idempotency phía server nếu dữ kiện chỉ ra lỗi render hai lần cùng một record.
4. **Sửa và kiểm:** chạy cùng ca trước/sau, kiểm số bản ghi và kết quả trả về; kiểm tiếp một thao tác mới hợp lệ vẫn tạo được bản ghi riêng. Không sửa bằng cách chặn mọi lần lưu sau lần đầu.

Đây là ví dụ điều tra, không phải log hay kết quả test đã chạy. Tên lệnh và cách chọn fixture phải theo dự án thật.

## Khi đã sửa code rồi mới nhớ lấy baseline

Không tự reset, checkout đè hoặc xóa thay đổi đang có để tái tạo bản lỗi. Nếu có điều kiện so sánh bằng một bản sao tách biệt, dùng cùng ca và input ở đó trong phạm vi được phép. Nếu không có baseline phù hợp, giữ thiếu sót này trong kết luận; không dựng output đỏ cho đủ quy trình.

Với ca không thể tái hiện ở môi trường hiện tại, một test thu nhỏ có thể kiểm cơ chế được suy luận từ code, nhưng phải ghi nó chứng minh điều gì và còn thiếu điều kiện nào so với lỗi gốc.

## Bàn giao đủ để người đọc kiểm lại

Chỉ cần nêu thông tin liên quan, không phải tạo file báo cáo:

- **Nguyên nhân:** trigger, đường gây sai và dữ kiện hỗ trợ; phần nào còn là giả thuyết.
- **Trước/sau:** cùng ca hoặc thao tác nào, snapshot và môi trường nào, output quan trọng và exit code nếu có. Không ghi số hoặc PASS khi chưa chạy.
- **Hồi quy:** phạm vi đã chọn, kết quả và điều chưa thử; CI có link tới đúng commit/artifact.
- **Kết luận:** phần được xác minh và phần chưa thể xác minh. Một bản vá đã viết nhưng chưa chạy được phải được mô tả như vậy.
