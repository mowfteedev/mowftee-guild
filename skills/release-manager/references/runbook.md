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
| Gate chất lượng | Kiểm blocker, failed/pending checks, mức độc lập và exception được duyệt. | Gate matrix và owner chấp nhận rủi ro có căn cứ. |
| Compatibility/migration | Xác định thứ tự app/schema/consumer và cửa sổ hỗ trợ. | Rollout map, backward/forward compatibility và điểm contract. |
| External action | Phân quyền push/PR/merge/tag/deploy riêng; chỉ làm phần được yêu cầu. | URL/id/SHA cùng trạng thái trả về thật. |
| Sau hành động | Kiểm remote SHA hoặc runtime signals phù hợp; giữ phần pending rõ ràng. | Remote ref, CI run hoặc smoke evidence đúng artifact. |

## Hợp đồng đầu ra khi bàn giao

- Readiness packet: scope, snapshot, evidence và open risks.
- Rollout/recovery: stages, signals, stop conditions và owner.
- Action result: quyền, URL/id/SHA, status và handoff.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Check bắt buộc chưa đạt, quyền action chưa có hoặc rollback/roll-forward chưa rõ cho bước có thể làm mất dữ liệu. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
