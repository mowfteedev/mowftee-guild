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

## Hợp đồng đầu ra khi bàn giao

- Invariant map: owner dữ liệu, transaction và constraint.
- Failure matrix: auth, validation, conflict, dependency, cancellation.
- Evidence: response, side effect DB/event và test concurrency khi liên quan.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Thiếu quy tắc nghiệp vụ hoặc quyền production; chưa có phương án bảo toàn invariant khi lỗi giữa các side effect. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
