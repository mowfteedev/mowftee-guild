# Runbook: Di chuyển dữ liệu

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Khóa chính UUID: không dùng ví dụ backfill cộng BIGINT.
2. Timeout khi tạo index: kiểm tra index không hợp lệ và kế hoạch xử lý.
3. Cột mới cần NOT NULL: xác minh dữ liệu cũ trước enforce.
4. Đổi cột phá dữ liệu: ưu tiên kế hoạch restore hoặc roll-forward đã kiểm chứng.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Expand | Thêm cấu trúc tương thích để bản app hiện tại vẫn chạy; kiểm lock theo engine/version. | Schema diff, phiên bản runner và đo thời gian lock trên môi trường thử. |
| Backfill | Chọn khóa ổn định, batch giới hạn, checkpoint và commit đúng; hỗ trợ retry/resume. | Ca dừng giữa batch, chạy lại và đối chiếu số record/invariant. |
| Validate và cutover | Xác nhận dữ liệu và app đọc/ghi mới trước chuyển luồng; quan sát lỗi/lag. | Data checks, client compatibility và tín hiệu cutover. |
| Contract | Chỉ bỏ cấu trúc cũ sau cửa sổ tương thích và quyền đã chốt. | Danh sách consumer cũ, điều kiện dừng dùng và phê duyệt phạm vi. |
| Phục hồi | Phân biệt rollback schema, restore dữ liệu và roll-forward; thử phương án phù hợp. | Kết quả drill, mất dữ liệu có thể xảy ra và owner thực thi. |

## Đầu ra cần giữ khi liên quan

- Migration plan: từng bước, lock/time budget, dependency và quyền.
- Data verification: invariant, sample, counts/checksums phù hợp.
- Recovery runbook: điều kiện dừng, rollback/roll-forward và evidence.

## Điều kiện dừng phần phụ thuộc

Dữ liệu có thể mất mà chưa có phương án phục hồi; timeout/lock chưa hiểu; hoặc bước thực thi vượt quyền môi trường. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ expand/contract: chuyển `full_name` thành `display_name`

Đầu tiên xác nhận đây là đổi tên giữ nguyên nghĩa hay là thay đổi cách biểu diễn dữ liệu. Nếu đổi nghĩa, backfill bằng phép chép đơn giản có thể sai. Giả sử giữ nguyên nghĩa và app cũ phải cùng chạy trong một giai đoạn:

1. **Expand:** thêm cột mới theo cách đã kiểm lock với engine/version thực. App cũ vẫn dùng được schema sau bước này.
2. **Chuyển ghi:** triển khai cơ chế giữ dữ liệu mới nhất ở cả hai biểu diễn trong cửa sổ tương thích. Xác định có còn writer cũ không; chỉ dual-write ở app mới không bao phủ writer cũ. Tùy hệ thống, chọn bản app trung gian bao phủ mọi writer, cơ chế đồng bộ ở DB hoặc cửa sổ ngừng ghi đã được chấp nhận trước khi backfill.
3. **Backfill:** dùng điều kiện tránh ghi đè giá trị mới bằng snapshot cũ. Checkpoint chỉ tiến sau khi batch đã commit; chọn khóa/cursor thật của bảng, không giả định khóa là số tăng dần.
4. **Validate và đổi đọc:** đối chiếu các hàng thiếu/sai, kiểm app cũ/mới và writer đồng thời; chuyển đọc khi điều kiện đã đạt.
5. **Contract:** bỏ cột cũ sau khi không còn consumer cần nó và hết cửa sổ phục hồi đã thống nhất. Tách khỏi lần triển khai thêm cột nếu chưa đủ căn cứ.

Thử dừng sau một batch, chạy lại và cập nhật tên trong lúc backfill. Ca quan trọng là tên vừa được người dùng sửa không bị chép đè bằng tên cũ. Đếm số hàng bằng nhau thôi chưa chứng minh giá trị đúng.

Trước khi cutover, ghi rõ app cũ đọc được schema nào và dữ liệu đã ghi theo schema mới có chuyển ngược được không. Rollback binary không tự khôi phục dữ liệu đã mất; nếu cần restore, phải chỉ rõ điểm phục hồi và phần ghi mới có thể mất. Đây là kế hoạch minh họa, chưa phải script được phép chạy lên DB thật.
