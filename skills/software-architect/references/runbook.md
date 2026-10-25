# Runbook: Kiến trúc phần mềm

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. MVP nhỏ: cân nhắc module trong một ứng dụng trước khi chia dịch vụ.
2. Sự kiện ngoài transaction: làm rõ thời điểm commit và cơ chế outbox nếu cần độ bền.
3. Hệ thống cũ thiếu tài liệu: phân biệt kiến trúc quan sát được với kiến trúc mong muốn.
4. Hai phương án tương đương: ưu tiên phương án đội ngũ có thể vận hành.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Có thể giữ hiện trạng | Dùng phương án không đổi kiến trúc làm baseline trước khi đề xuất công nghệ mới. | So sánh chi phí, độ phức tạp và constraint đã biết. |
| Ranh giới dữ liệu | Xác định module sở hữu dữ liệu và giao tiếp công khai; mô tả chỗ cần transaction. | Sơ đồ dependency và đường đi một luồng hoàn chỉnh. |
| Dependency không ổn định | Thiết kế timeout budget, backpressure, suy giảm và phục hồi theo luồng nghiệp vụ. | Failure-mode table, điểm quan sát và cách kiểm chứng. |
| Event và side effect | Xác định ranh giới commit, durability và cơ chế retry; cân nhắc outbox khi yêu cầu bền vững. | Tình huống commit thành công nhưng publish/response thất bại. |
| Thay đổi lớn | Chia rollout tương thích và điều kiện quay lui hoặc roll-forward. | ADR với phương án loại bỏ, hệ quả và owner xem lại. |

## Hợp đồng đầu ra khi bàn giao

- ADR: context, constraints, alternatives, decision, consequences.
- Architecture map: module, data owner, contract, trust boundary.
- Transition plan: compatibility, failure handling và điểm dừng.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Chưa rõ owner invariant quan trọng; phương án vượt ràng buộc vận hành; hoặc thiếu thông tin quyết định làm đổi scope. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
