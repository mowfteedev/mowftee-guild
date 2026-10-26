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

## Đầu ra cần giữ khi liên quan

- Refactor plan: pain point, scope và observable invariants.
- Diff rationale: boundary/coupling/testability cải thiện chỗ nào.
- Verification: baseline, regression và behavior change được chấp nhận.

## Điều kiện dừng phần phụ thuộc

Không có cơ sở bảo toàn public behavior hoặc thay đổi cần vượt scope đã cho phép; đề xuất chia nhỏ trước khi sửa tiếp. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ refactor: tách tính tổng tiền khỏi endpoint

Mục tiêu là làm logic dễ đọc/thử hơn, chưa phải thay quy tắc tính giá. Trước khi tách, ghi hành vi quan sát: cách làm tròn, thứ tự giảm giá/thuế, tiền tệ, dữ liệu thiếu và lỗi; đọc caller có phụ thuộc vào thứ tự xử lý hay không.

1. Chọn các ví dụ đại diện từ yêu cầu và dữ liệu thử: giỏ rỗng, nhiều dòng, giảm giá, giá trị cần làm tròn và đầu vào không hợp lệ. Không tự biến hành vi tình cờ thành yêu cầu nếu nó mâu thuẫn nghiệp vụ; đánh dấu điểm đó riêng.
2. Di chuyển phép tính thành hàm/module có ranh giới rõ, giữ kiểu dữ liệu và thứ tự thao tác; tránh tiện thể đổi dependency hoặc toàn bộ cấu trúc thư mục.
3. So đầu ra và lỗi trước/sau theo cùng input; kiểm endpoint vẫn kiểm quyền và ghi dữ liệu ở đúng transaction như trước.
4. Truy caller, export công khai, job và test trước khi xóa helper cũ; tìm kiếm văn bản có thể bỏ sót tên được tạo động hoặc cấu hình.

Nếu phát hiện quy tắc làm tròn cũ sai, mô tả bug và phạm vi sửa riêng. Không giấu thay đổi số tiền trong diff mang tên “chỉ refactor”; dùng quyền và yêu cầu hiện có để quyết định phần sửa đó đã được cho phép chưa.

Kết luận refactor nên chỉ ra cấu trúc nào dễ thay/thử hơn và hành vi nào đã đối chiếu. Giảm số dòng hoặc đổi tên hàm không tự chứng minh hiệu năng tốt hơn.
