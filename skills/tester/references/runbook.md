# Runbook: Nghiệm thu và kiểm thử khám phá

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Không có lỗi trong phạm vi đã kiểm tra: báo đúng kết quả và giới hạn.
2. Thiếu browser: không cấp PASS cho AC cần tương tác UI.
3. Sửa lỗi ở commit mới: bằng chứng commit cũ không tự chuyển sang bản mới.
4. Luồng thanh toán: kiểm chứng cả dữ liệu được ghi, không chỉ toast thành công.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| AC traceability | Mỗi AC bắt buộc có cách quan sát và kết quả riêng; NOT_APPLICABLE có lý do. | AC matrix, command/manual steps và evidence. |
| Khám phá lỗi | Chọn dữ liệu biên theo validation, quyền, concurrency và recovery thực tế. | Reproduction steps, expected/actual và hậu quả. |
| Phân loại finding | Blocker cần tác động đáng kể và trigger; không nâng style thành lỗi nghiêm trọng. | Vị trí, dữ liệu gây lỗi và phạm vi ảnh hưởng. |
| Kiểm lại snapshot | Thay code/config/data liên quan làm evidence cần đánh giá lại. | Commit, dirty state hoặc artifact digest trước/sau. |
| Kết luận | PASS chỉ bao phủ phần đã thử; thiếu browser, reviewer hoặc dependency phải nêu rõ. | Kết luận có scope, independent/self-check và rủi ro còn lại. |

## Hợp đồng đầu ra khi bàn giao

- Acceptance matrix: AC, trạng thái, evidence, giới hạn.
- Defect report: trigger, expected/actual, severity và owner.
- Verdict: snapshot, phạm vi đã thử, phần còn mở và bước tiếp.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Thiếu môi trường cho AC bắt buộc; không xác minh được snapshot; hoặc yêu cầu cấp chứng nhận khi chưa có evidence. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
