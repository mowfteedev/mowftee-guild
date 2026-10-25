# Runbook: Thiết kế dữ liệu

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. EXPLAIN ANALYZE trên UPDATE: đây là thực thi thật, cần môi trường được phép.
2. Seq scan trên bảng nhỏ: có thể hợp lý, không tự coi là lỗi.
3. RLS và connection pool: context người dùng phải đúng vòng đời transaction.
4. Xóa dữ liệu cá nhân: xem cả bản sao, cache và retention đã thống nhất.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Chọn khóa và kiểu dữ liệu | Dựa vào cardinality, phân bố ghi, range scan, precision và nhu cầu phân tán. | Schema rationale và dữ liệu đại diện. |
| Chọn index | Gắn mỗi index với query/workload; xem selectivity, sort, write amplification và dung lượng. | Query plan, mẫu dữ liệu và trước/sau trong cùng điều kiện. |
| Đọc query plan | Phân biệt estimate với execution; thao tác ANALYZE có thể thực thi query thật. | Command và môi trường cho phép; không chạy DML thật chỉ để xem plan. |
| Connection pool | Đo contention, latency, query mix và tài nguyên; xem session state với pool mode. | Số connection, queue, timeout và tải tương ứng. |
| RLS/retention | Kiểm role/bypass và vòng đời tenant context; xác định xóa, lưu giữ và audit theo yêu cầu. | Ca user/tenant khác nhau và trạng thái dữ liệu sau xóa. |

## Hợp đồng đầu ra khi bàn giao

- Schema proposal: entities, constraints, nullability và ownership.
- Query report: workload, plan, index rationale và chi phí ghi.
- Migration handoff: diff, kích thước, compatibility và invariant.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Thiếu workload hoặc engine/version để chốt hành vi; không được phép thực thi query có side effect trên môi trường thật. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
