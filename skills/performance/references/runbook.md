# Runbook: Hiệu năng và đo tải

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Máy laptop khác cấu hình CI: không so latency như cùng môi trường.
2. Cache ấm và cache lạnh: tách hai kịch bản.
3. Response nhanh vì lỗi 500: không ghi là cải thiện.
4. Memory tăng trong warm-up: cần quan sát dài hơn trước kết luận leak.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Thiết kế phép đo | Chốt workload, dataset, warm-up, cache, máy và cửa sổ đo trước tối ưu. | Benchmark recipe và cấu hình có thể tái lập. |
| Bottleneck | Dùng profiler, trace, query plan hoặc browser metrics để chọn giả thuyết. | Raw capture và đường chiếm tài nguyên/latency. |
| Concurrency và throughput | Phân biệt số kết nối, người dùng ảo, request rate và độ dài queue. | Load profile, achieved rate, timeout và dropped requests. |
| So trước/sau | Giữ điều kiện tương đương; báo phân vị, error rate, resource và độ nhiễu. | Raw samples, summary và đúng snapshot. |
| Kết luận | Chấp nhận hoặc bác giả thuyết theo budget đã chọn; nêu giới hạn ngoại suy. | Delta có cơ sở cùng correctness/regression results. |

## Đầu ra cần giữ khi liên quan

- Experiment plan: hypothesis, metric, workload và stop condition.
- Measurements: before/after, samples, environment và errors.
- Decision: benefit, cost, regression và uncertainty.

## Điều kiện dừng phần phụ thuộc

Môi trường không được phép load/profile; phép đo không so sánh được; hoặc correctness lỗi làm vô nghĩa con số latency. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ điều tra: danh sách tải chậm sau khi thêm thông tin khách

Trước khi thêm cache, ghi đường đo từ request UI đến response và render. Giả thuyết có thể là N+1 query, API đối tác chậm hoặc render quá nhiều; chọn theo trace thay vì đoán từ triệu chứng “chậm”.

| Bước | Dữ liệu cần giữ |
| --- | --- |
| Baseline | Commit, máy/runtime, dữ liệu và phân bố, bộ lọc, số dòng trả về, cache nóng/lạnh, lỗi và timeout. |
| Kiểm giả thuyết N+1 | Query count tăng thế nào khi số mục tăng; thời gian nằm ở DB, network hay phần khác. |
| Thử một thay đổi | Giữ nguyên kết quả/quyền/phân trang, tránh join làm nhân số dòng hoặc tải thừa dữ liệu. |
| So sánh | Cùng workload và điều kiện; xem phân vị latency, throughput đạt được, lỗi và tài nguyên. |

Đo nhiều quan sát đủ để thấy độ nhiễu theo mục tiêu, không lấy một lần nhanh nhất làm kết quả. Nếu tập dữ liệu sau sửa nhỏ hơn hoặc nhiều response lỗi hơn thì phép so sánh chưa tương đương.

Kết luận nên nói “giảm phần thời gian/query nào trong điều kiện đã thử”, kèm dữ liệu thô khi có. Không biến tỷ lệ cải thiện trên laptop thành cam kết production. Nếu đo bác giả thuyết N+1, giữ kết quả đó và chuyển sang đường chậm đã quan sát, không tiếp tục thêm cache chỉ vì đã dự định.
