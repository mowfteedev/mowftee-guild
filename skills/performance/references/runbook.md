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

## Hợp đồng đầu ra khi bàn giao

- Experiment plan: hypothesis, metric, workload và stop condition.
- Measurements: before/after, samples, environment và errors.
- Decision: benefit, cost, regression và uncertainty.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Môi trường không được phép load/profile; phép đo không so sánh được; hoặc correctness lỗi làm vô nghĩa con số latency. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
