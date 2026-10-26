# Runbook: Phân tích yêu cầu

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Đề bài mơ hồ về màu sắc: ghi lựa chọn có thể đảo ngược, không chặn toàn bộ.
2. Checkout thiếu quy tắc hoàn tiền: đánh dấu câu hỏi nghiệp vụ quan trọng.
3. Tính năng chỉ dành cho admin: có AC cho người dùng thường bị từ chối.
4. Người dùng yêu cầu bỏ một phần: cập nhật AC, không âm thầm giữ scope cũ.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Tiêu chí mơ hồ | Đổi nhanh/đẹp/ổn định thành hành vi quan sát hoặc chỉ số có cách đo đã thống nhất. | AC có tiền đề, hành động và kết quả. |
| Quyền người dùng | Lập ma trận subject/action/resource, gồm từ chối quyền. | Ví dụ người dùng hợp lệ và không hợp lệ cho cùng tài nguyên. |
| Hành vi tiền tệ | Chốt đơn vị, precision, quy tắc làm tròn, hủy và hoàn trả với owner nghiệp vụ. | Ví dụ số cụ thể đã xác nhận, không tự suy đoán. |
| Tính năng kéo thêm scope | Tách bắt buộc, tùy chọn và ngoài phạm vi; ghi tác động deadline hoặc dependency. | Scope diff và quyết định người có thẩm quyền. |
| AC thay đổi sau triển khai | Đánh giá lại phần code/test/docs bị ảnh hưởng; không sửa AC để hợp thức lỗi. | Lịch sử AC và lý do thay đổi. |

## Đầu ra cần giữ khi liên quan

- Spec: người dùng, vấn đề, phạm vi và AC.
- Business rules: quyền, trạng thái, rounding/timezone khi có.
- Open questions: tác động, owner và phần có thể tiếp tục.

## Điều kiện dừng phần phụ thuộc

Thiếu quy tắc làm thay đổi kết quả nghiệp vụ quan trọng; các bên chưa thống nhất AC bắt buộc. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ: biến “cho phép hủy đơn” thành yêu cầu làm được

Đừng tự suy ra đơn nào cũng được hủy. Đọc trạng thái đơn, quyền hiện tại và cách thanh toán trước; nếu thiếu quy tắc hủy sau khi giao hàng hoặc hoàn tiền, đó là câu hỏi nghiệp vụ cần trả lời.

Giả sử người dùng đã xác nhận phạm vi: khách được hủy đơn của mình khi chưa giao cho vận chuyển; việc hủy và hoàn tiền là hai trạng thái riêng. Khi đó có thể mô tả:

| Tiền đề | Hành động | Kết quả cần quan sát |
| --- | --- | --- |
| Đơn của mình còn được hủy | Xác nhận hủy | Trạng thái hủy được lưu; UI phản ánh kết quả server. |
| Đơn đã hủy | Gửi lại thao tác | Không lặp hoàn kho hoặc tạo thêm yêu cầu hoàn tiền. |
| Đơn thuộc khách khác | Gọi trực tiếp API hủy | Bị từ chối theo quy ước của hệ thống, dữ liệu không đổi. |
| Đơn vừa chuyển sang đang giao | Gửi yêu cầu hủy từ màn hình cũ | Server quyết định theo trạng thái hiện tại; UI giải thích và tải lại dữ liệu. |

Đây là ví dụ giả định, không phải quy tắc áp cho mọi cửa hàng. Cần tách việc “đã hủy đơn” với “đã hoàn tiền”; không cho một toast thành công đại diện cả hai nếu hệ thống xử lý bất đồng bộ.

Đầu ra đủ dùng: phạm vi hủy, bảng hành vi trên, các quyết định còn thiếu và điều không làm trong lần này. Dùng mã AC khi cần truy vết nhiều tiêu chí; một yêu cầu nhỏ không cần biểu mẫu dài.
