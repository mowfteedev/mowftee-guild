# Runbook: Quản lý phát hành

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Người dùng yêu cầu push xem trước: push nhánh review, không merge.
2. CI đang chạy: báo pending, không báo đã pass.
3. Tag đã tồn tại: không ghi đè tag mà chưa có yêu cầu.
4. Lỗi blocking chưa sửa: bàn giao trạng thái chưa đủ điều kiện phát hành.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Chốt snapshot | Ràng buộc scope với commit/artifact; xem thay đổi kể từ evidence. | Head SHA, digest, AC và check results. |
| Kiểm tra liên quan | Đối chiếu lỗi còn mở và check bắt buộc của repo; chọn mức kiểm theo hành động thực tế. | Kết quả check đúng commit và phần chưa chạy. |
| Compatibility/migration | Xác định thứ tự app/schema/consumer và cửa sổ hỗ trợ. | Rollout map, backward/forward compatibility và điểm contract. |
| External action | Phân quyền push/PR/merge/tag/deploy riêng; chỉ làm phần được yêu cầu. | URL/id/SHA cùng trạng thái trả về thật. |
| Sau hành động | Kiểm remote SHA hoặc runtime signals phù hợp; giữ phần pending rõ ràng. | Remote ref, CI run hoặc smoke evidence đúng artifact. |

## Đầu ra cần giữ khi liên quan

- Phạm vi thực hiện: commit/artifact, kết quả kiểm tra và điểm còn mở.
- Rollout/recovery: stages, signals, stop conditions và owner.
- Action result: quyền, URL/id/SHA, status và handoff.

## Điều kiện dừng phần phụ thuộc

Check bắt buộc chưa đạt, quyền action chưa có hoặc rollback/roll-forward chưa rõ cho bước có thể làm mất dữ liệu. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ phạm vi: “push lên cho anh xem”

Đây là yêu cầu đưa thay đổi lên remote để xem. Kiểm nhánh và remote hiện tại, đọc diff, chạy các kiểm tra liên quan và commit phạm vi đã làm. Sau push, đối chiếu remote ref với commit local; xem check của chính commit đó nếu repo có CI.

| Trạng thái thực | Cách báo |
| --- | --- |
| Push thành công, CI còn chạy | Có link nhánh/commit, CI đang chạy; chưa kết luận check đạt. |
| Check thất bại | Nêu job/lỗi, sửa trong phạm vi và kiểm lại; không gộp CI cũ thành kết quả của bản mới. |
| Branch chứa thay đổi ngoài đầu việc | Đọc và bảo toàn thay đổi của người dùng; không đưa vào commit một cách vô tình. |
| User chưa yêu cầu merge/tag/deploy | Hoàn tất bản để xem; những hành động đó có tác động riêng, không suy ra từ lệnh push. |

Không áp cả một hồ sơ phát hành production cho việc push tài liệu. Kết quả đủ dùng là link, commit, nội dung đổi và kết quả kiểm tra thật.

Nếu yêu cầu là deploy, mới bổ sung artifact/môi trường, tương thích schema, tín hiệu sau triển khai và điều kiện phục hồi phù hợp. Với migration phá dữ liệu, quay lại binary cũ chưa chắc là phương án rollback hợp lệ. Dùng quyền đã cấp xuyên suốt phiên, không hỏi lại từng bước đã được cho phép.
