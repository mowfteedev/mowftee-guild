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

## Hợp đồng đầu ra khi bàn giao

- Migration plan: từng bước, lock/time budget, dependency và quyền.
- Data verification: invariant, sample, counts/checksums phù hợp.
- Recovery runbook: điều kiện dừng, rollback/roll-forward và evidence.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Dữ liệu có thể mất mà chưa có phương án phục hồi; timeout/lock chưa hiểu; hoặc bước thực thi vượt quyền môi trường. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
