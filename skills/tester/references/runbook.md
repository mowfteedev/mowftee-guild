# Runbook: Nghiệm thu và kiểm thử khám phá

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Không có lỗi trong phạm vi đã kiểm tra: báo đúng kết quả và giới hạn.
2. Thiếu browser: không cấp PASS cho AC cần tương tác UI.
3. Sửa lỗi ở commit mới: đối chiếu thay đổi với phạm vi bằng chứng cũ; kiểm lại phần có thể bị ảnh hưởng.
4. Luồng thanh toán: kiểm chứng cả dữ liệu được ghi, không chỉ toast thành công.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| AC traceability | Mỗi AC bắt buộc có cách quan sát và kết quả riêng; NOT_APPLICABLE có lý do. | AC matrix, command/manual steps và evidence. |
| Khám phá lỗi | Chọn dữ liệu biên theo validation, quyền, concurrency và recovery thực tế. | Reproduction steps, expected/actual và hậu quả. |
| Phân loại finding | Blocker cần tác động đáng kể và trigger; không nâng style thành lỗi nghiêm trọng. | Vị trí, dữ liệu gây lỗi và phạm vi ảnh hưởng. |
| Kiểm lại snapshot | Thay code/config/data liên quan làm evidence cần đánh giá lại. | Commit, dirty state hoặc artifact digest trước/sau. |
| Kết luận | PASS chỉ bao phủ phần đã thử; thiếu browser hoặc dependency thì nêu rõ phần chưa thử. | Kết luận có scope, independent/self-check và rủi ro còn lại. |

## Đầu ra cần giữ khi liên quan

- Acceptance matrix: AC, trạng thái, evidence, giới hạn.
- Defect report: trigger, expected/actual, severity và owner.
- Verdict: snapshot, phạm vi đã thử, phần còn mở và bước tiếp.

## Điều kiện dừng phần phụ thuộc

Thiếu môi trường cho AC bắt buộc; không xác minh được snapshot; hoặc yêu cầu cấp chứng nhận khi chưa có evidence. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Đối chiếu bằng chứng của bản sửa

| Bằng chứng nhận được | Cần đối chiếu | Kết luận phù hợp |
| --- | --- | --- |
| “Test đã pass” | Command/thao tác, phiên bản, môi trường và output; test có chạm triệu chứng không? | Chưa đủ căn cứ nếu chỉ có lời tự báo. |
| Cùng ca fail trước, pass sau | Lý do fail ban đầu và kỳ vọng giữ nguyên; điều kiện so sánh có khớp không? | Xác nhận ca đó được sửa; kiểm tiếp vùng ảnh hưởng trước kết luận rộng hơn. |
| Test đỏ vì thiếu dependency rồi xanh sau cài dependency | Thiếu dependency có phải triệu chứng đang điều tra và thuộc môi trường hỗ trợ không, hay chỉ chặn kiểm một lỗi khác? | Chỉ chứng minh sửa lỗi dependency tương ứng; chưa đủ để kết luận một lỗi khác đã được sửa. |
| Ca giả lập pass, chưa tái hiện lỗi gốc | Giả lập bao phủ cơ chế nào, thiếu điều kiện nào so với báo cáo thật? | Chỉ kết luận trong phạm vi giả lập; lỗi gốc chưa được xác minh. |
| CI từ lần trước | Có đúng commit/artifact, cấu hình, dữ liệu và phạm vi check đang đánh giá không? | Dùng được khi còn khớp; kiểm lại phần đã đổi liên quan. |

Không đòi transcript toàn bộ hoặc chạy lại mọi test chỉ để có output ở lượt chat mới. Giữ phần output đủ để người đọc kiểm lại, exit code nếu có và link kết quả thật. Không lấy thời điểm mới chạy làm lý do chấp nhận một test không đúng hành vi.

## Tổng hợp kết luận nghiệm thu

Chọn AC bắt buộc theo phạm vi đã thống nhất trước khi kiểm tra. Phân biệt kết quả từng check với kết luận toàn bộ: có một check PASS không chứng minh toàn bộ tính năng đã đúng.

| Trạng thái tiêu chí bắt buộc | Kết luận toàn bộ |
| --- | --- |
| Có FAIL | FAIL; ghi lỗi và owner sửa |
| Không có FAIL nhưng còn điều kiện kiểm thử bị chặn | BLOCKED |
| Không có FAIL/BLOCKED nhưng còn NOT_RUN | NOT_RUN |
| Mọi điều kiện bắt buộc đã PASS, phạm vi không áp dụng được giải thích hợp lệ | PASS trong phạm vi đã chọn |
| Chưa chốt AC/phạm vi | NOT_RUN, chưa đủ cơ sở nghiệm thu |

NOT_APPLICABLE không được dùng để bỏ một yêu cầu đã chốt. Bản nháp có thể được push để review theo quyền đã có; đó không phải chứng nhận sẵn sàng phát hành.

## Phiên khám phá: form lưu địa chỉ giao hàng

Mục tiêu là xác nhận người dùng biết địa chỉ nào đã được lưu và không mất dữ liệu đang nhập khi lỗi. Bắt đầu bằng một luồng hợp lệ, rồi chọn biến thể theo code và rủi ro thực:

- Gửi thiếu trường bắt buộc: thông báo gắn đúng trường, giữ phần đã nhập và cho sửa bằng bàn phím.
- Server từ chối quyền sau khi session thay đổi: không thông báo đã lưu, không để lộ địa chỉ của tài khoản trước.
- Lưu xong ở server nhưng response bị mất: tải lại để kiểm trạng thái trước khi kết luận “không lưu”; thử lại không tạo địa chỉ lặp nếu quy tắc yêu cầu chống lặp.
- Đổi route lúc request chờ rồi quay lại: dữ liệu và trạng thái tải thuộc lần mở hiện tại, không bị response cũ ghi đè.

Một defect có thể ghi: “Khi request lưu trả lỗi validation, form bị reset nên mất các trường hợp lệ đã nhập; tái hiện bằng các bước …; mong đợi giữ dữ liệu theo yêu cầu …”. Tách lỗi quan sát được khỏi giả thuyết về nguyên nhân trong code.

Nếu chỉ có test API mà chưa có browser, kết luận phần API đã kiểm riêng; các tiêu chí giữ input, focus và bố cục vẫn chưa được thử. Mẫu kết luận cho tình huống này không phải chứng nhận toàn bộ form đã đạt.
