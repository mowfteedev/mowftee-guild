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

## Đầu ra cần giữ khi liên quan

- Schema proposal: entities, constraints, nullability và ownership.
- Query report: workload, plan, index rationale và chi phí ghi.
- Migration handoff: diff, kích thước, compatibility và invariant.

## Điều kiện dừng phần phụ thuộc

Thiếu workload hoặc engine/version để chốt hành vi; không được phép thực thi query có side effect trên môi trường thật. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ đọc workload: danh sách đơn theo khách hàng

Giả sử query phổ biến lọc `tenant_id`, `customer_id`, sắp xếp `created_at DESC, id DESC`, rồi lấy một trang nhỏ. Trước khi thêm index, xem engine/version, index hiện có, số dòng từng tenant và tỷ lệ đọc/ghi.

Một composite index bắt đầu bằng các điều kiện bằng và tiếp theo là khóa sắp xếp là ứng viên để khảo sát, không phải đáp án mặc định. So kế hoạch và thời gian thực thi trên dữ liệu đại diện; tenant lớn, customer ít đơn hoặc query bỏ một bộ lọc có thể tạo kế hoạch khác.

| Quan sát | Câu hỏi kế tiếp |
| --- | --- |
| Quét nhiều dòng rồi sort để lấy ít dòng | Index có phù hợp điều kiện lọc/thứ tự, hay query biến đổi cột khiến không dùng được đường truy cập mong muốn? |
| Query nhanh nhưng ghi chậm sau thêm index | Chi phí duy trì index, dung lượng và trùng lặp với index cũ ra sao? |
| Trang sau trùng hoặc thiếu đơn | Có thứ tự xác định khi trùng thời gian không; cursor có biểu diễn đủ khóa sort và quy tắc dữ liệu thay đổi không? |
| Môi trường thử nhanh, thực tế chậm | Phân bố dữ liệu, statistics, cache và contention có tương đương không? |

Không kết luận index thành công chỉ vì plan có chữ “Index”. Bàn giao query, điều kiện đo, kế hoạch trước/sau và chi phí ghi; đưa việc tạo index trên bảng thật sang kế hoạch migration theo engine để xét lock và tương thích.
