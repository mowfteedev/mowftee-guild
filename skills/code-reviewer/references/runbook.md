# Runbook: Thẩm định mã nguồn

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Promise không await nhưng được cố ý background: kiểm tra ownership và error handling trước kết luận.
2. Seq scan: cần workload thay vì nhận định theo tên operator.
3. Không thấy bug: báo không có finding trong phạm vi và giới hạn review.
4. Token giả trong fixture: phân biệt placeholder với secret thật, không in lại giá trị.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Public contract | Truy caller, serializer, schema và consumer; không kết luận từ chữ ký hàm đơn lẻ. | Call path và kịch bản bị ảnh hưởng. |
| Lỗi bất đồng bộ | Kiểm owner của background work, await/catch, resource lifetime và cancellation. | Đường thực thi gây mất lỗi hoặc side effect sai. |
| Transaction/concurrency | Xác định invariant và interleaving làm vi phạm; xem constraint hoặc lock thực có. | Ca hai thao tác cạnh tranh và dữ liệu sai có thể xảy ra. |
| Review hiệu năng | Tách phỏng đoán O(n²)/N+1 với workload thật và giới hạn input. | Query/caller/data size hoặc yêu cầu đo thêm. |
| Báo cáo | Ghi finding ngắn ở vùng diff nhỏ nhất, kèm trigger và tác động; không bịa lỗi khi không tìm thấy. | Base/head, checks đã chạy, findings và giới hạn review. |

## Đầu ra cần giữ khi liên quan

- Review scope: base/head, AC và file/caller đã đọc.
- Findings: severity, location, trigger, impact và cách kiểm lại.
- Verdict: blockers còn lại, checks đã chạy và phần cần runtime validation.

## Điều kiện dừng phần phụ thuộc

Không đủ contract hoặc caller để khẳng định lỗi; báo câu hỏi thay finding chắc chắn và không tự sửa khi chỉ được review. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Đọc một bản sửa từ triệu chứng tới kết quả

1. Đối chiếu báo cáo lỗi với trigger và đường thực thi. Một diff làm mất thông báo lỗi chưa chứng minh nguyên nhân đã được xử lý.
2. Kiểm thay đổi có tác dụng ở đúng tầng gây sai; tìm caller dùng chung, dữ liệu hoặc side effect có thể bị tác động. Nếu bản vá chỉ nới assertion, mock đối tượng đang kiểm, nuốt lỗi hoặc thêm retry, yêu cầu cơ sở cho hành vi đó.
3. Đọc ca tái hiện và kết quả baseline: test phải chạm lỗi mục tiêu. Lỗi import/runner không phải bằng chứng regression; test vốn xanh trên bản lỗi không chứng minh tác dụng của bản sửa.
4. Đối chiếu cùng ca sau sửa và các kiểm tra vùng ảnh hưởng. Kết quả cần command/thao tác, snapshot, môi trường và output quan trọng; CI cần đúng commit/artifact. Đánh giá lại khi phần liên quan đổi, không đòi test lại chỉ vì sang lượt chat.

Nếu chỉ đọc code, vẫn có thể nêu lỗi có căn cứ từ contract/call path, nhưng phải ghi chưa chạy tái hiện. Thiếu bằng chứng chạy không tự biến một nghi vấn thành blocker; nêu rõ điều còn thiếu và giới hạn kết luận. Không bịa một lần fail trước hoặc pass sau để làm bản review trông đầy đủ.

## Ví dụ phân biệt finding với nghi vấn: bỏ `await`

Thấy diff đổi `await sendReceipt(order)` thành `sendReceipt(order)` chưa đủ để kết luận có bug. Lần theo caller, nơi bắt lỗi và vòng đời tiến trình:

| Dữ kiện từ code | Cách kết luận |
| --- | --- |
| Promise bị bỏ, không bắt rejection; request vẫn trả thành công trong khi contract đòi gửi xong | Có đường sai contract cụ thể; nêu trigger và tác động. |
| Công việc được giao cho hàng đợi bền vững; lỗi được xử lý ở worker | Không báo “thiếu await” chỉ từ hình thức của dòng diff. |
| Tác vụ nền có catch nhưng môi trường có thể đóng tiến trình sau response | Kiểm yêu cầu độ bền và runtime; catch không chứng minh công việc sẽ hoàn tất. |
| Chưa biết email bắt buộc hay best effort | Đặt câu hỏi có ảnh hưởng quyết định, không gán severity chắc chắn từ giả định. |

Finding đủ rõ có dạng: “Trong đường tạo đơn X, response đóng trước tác vụ Y; khi Z xảy ra, người dùng nhận A nhưng dữ liệu/side effect là B. Vị trí liên quan …; kiểm lại bằng …”. Dẫn đoạn diff nhỏ nhất và caller cần để thấy tác động.

Xếp ưu tiên theo hậu quả và khả năng xảy ra trong luồng thật. Tách góp ý đặt tên/format khỏi bug; nếu không tìm thấy lỗi thì báo đúng phạm vi đã đọc, không tạo finding để đủ số lượng.
