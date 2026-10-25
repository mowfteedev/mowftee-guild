# Runbook: Tái cấu trúc có kiểm soát

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. forEach async đang lỗi: sửa thành await có thể đổi hành vi, ghi rõ đây là bugfix.
2. Dependency injection làm số file tăng: giải thích lợi ích test hoặc boundary.
3. Module có dynamic import: kiểm tra cấu hình trước khi xóa.
4. Baseline cũ đang đỏ: phân loại lỗi cũ, không quy kết mọi lỗi cho refactor.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Khoanh hành vi | Ghi public API, error, ordering, side effects và concurrency cần giữ. | Callers/contract map và characterization tests khi cần. |
| Thay cấu trúc | Thay từng bước nhỏ, tránh format/rename hàng loạt ngoài scope. | Diff có thể review và mục tiêu bảo trì cụ thể. |
| Dead code | Kiểm dynamic import, config, reflection hoặc đăng ký gián tiếp trước xóa. | Nguồn gọi ngoài tìm kiếm văn bản đơn thuần. |
| Bugfix trong refactor | Tách rõ hành vi được sửa và xin chốt phạm vi nếu chưa có. | AC hoặc finding giải thích semantics thay đổi. |
| Đánh giá kết quả | Chạy regression liên quan; lợi ích hiệu năng cần phép đo riêng. | Before/after structure, tests và phần nợ còn lại. |

## Hợp đồng đầu ra khi bàn giao

- Refactor plan: pain point, scope và observable invariants.
- Diff rationale: boundary/coupling/testability cải thiện chỗ nào.
- Verification: baseline, regression và behavior change được chấp nhận.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Không có cơ sở bảo toàn public behavior hoặc thay đổi cần vượt scope đã cho phép; đề xuất chia nhỏ trước khi sửa tiếp. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
