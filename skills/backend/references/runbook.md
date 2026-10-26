# Runbook: Phát triển máy chủ

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Lock hết TTL khi xử lý chưa xong: không được cho hai tiến trình ghi trùng.
2. Cùng key khác endpoint hoặc payload: không replay kết quả sai.
3. DB commit thành công nhưng response mất: retry phải giữ bất biến nghiệp vụ.
4. Server.close treo: deadline shutdown phải bao trùm bước đóng server.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Hai request cùng ghi | Dùng invariant DB, transaction và conflict/locking phù hợp; kiểm cạnh tranh thực tế. | Ca song song và số bản ghi/số dư sau hoàn tất. |
| Idempotency | Ràng buộc key với principal, operation và fingerprint; record kết quả theo durability nghiệp vụ. | Replay, key trùng khác payload, request đang xử lý và crash giữa chừng. |
| Lease/lock hết hạn | Nếu dùng lock, kiểm ownership, expiry/renewal và quyền giải phóng; không xóa lock của tiến trình khác. | Ca xử lý lâu hơn TTL và tiến trình cũ tỉnh lại sau timeout. |
| DB commit nhưng side effect lỗi | Phân loại event nội bộ với side effect cần bền vững; dùng cơ chế sau commit có retry hoặc outbox khi cần. | Ca commit rồi mất network/publish và khả năng chạy lại không lặp nghiệp vụ. |
| Shutdown và dependency | Deadline bao trùm cả ngừng nhận request, drain và đóng resource; retry có budget và semantics an toàn. | Ca dependency treo, signal shutdown và tác vụ đang ghi dữ liệu. |

## Đầu ra cần giữ khi liên quan

- Invariant map: owner dữ liệu, transaction và constraint.
- Failure matrix: auth, validation, conflict, dependency, cancellation.
- Evidence: response, side effect DB/event và test concurrency khi liên quan.

## Điều kiện dừng phần phụ thuộc

Thiếu quy tắc nghiệp vụ hoặc quyền production; chưa có phương án bảo toàn invariant khi lỗi giữa các side effect. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ: hai request cùng mua sản phẩm cuối cùng

Invariant là tồn kho không âm và một giao dịch hợp lệ chỉ tạo hiệu lực nghiệp vụ một lần theo quy tắc đã chốt. `SELECT` kiểm còn hàng rồi `UPDATE` không có cơ chế bảo vệ chưa chứng minh invariant khi hai request chạy đồng thời.

Trước hết validate quantity theo miền nghiệp vụ, ví dụ số nguyên dương nếu bán theo chiếc. Một hướng triển khai có thể dùng cập nhật có điều kiện trong transaction: chỉ giảm tồn khi `stock >= quantity`, kiểm số dòng được đổi, rồi ghi đơn trong cùng ranh giới giao dịch nếu dữ liệu cùng DB. Đây là ý tưởng, phải đối chiếu semantics và isolation của engine đang dùng. Không tự chuyển giao dịch nhiều hệ thống thành một transaction giả.

| Thời điểm lỗi | Điều phải xác minh |
| --- | --- |
| Cả hai request tranh một sản phẩm | Tối đa số lượng tồn cho phép được bán; request còn lại nhận kết quả hết hàng/xung đột đã định nghĩa. |
| Ghi đơn lỗi sau khi giảm tồn | Thay đổi trong cùng transaction được rollback, không mất hàng vô cớ. |
| Commit xong nhưng client mất response | Retry theo cơ chế idempotency không tạo đơn mới; có cách tra lại kết quả. |
| Cùng idempotency key nhưng payload khác | Không trả kết quả của đơn trước như thể payload mới đã được xử lý. |

Kiểm bằng hai tác vụ thật chạm cùng DB và điều khiển thời điểm để có cạnh tranh; không dùng mock trả sẵn “thành công/thất bại” làm bằng chứng transaction đúng. Đối chiếu cả response, số đơn và tồn cuối cùng.

Nếu còn thanh toán bên ngoài, tách trạng thái đơn/thanh toán và cách phục hồi. Transaction DB không rollback được một khoản đã trừ ở đối tác; không retry charge mù quáng sau timeout.
