# Runbook: Phát triển giao diện

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. API trả mảng rỗng: hiển thị trạng thái trống có ý nghĩa.
2. Mạng mất giữa submit: giữ thông tin phục hồi, không tự báo thành công.
3. Tên sản phẩm rất dài: bố cục không che thao tác chính.
4. Optimistic update lỗi: rollback có xét các cập nhật đồng thời.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Dữ liệu bất đồng bộ | Tách loading ban đầu, refetch, stale, empty, error và partial result khi sản phẩm có. | Ca kiểm chứng API chậm, rỗng, lỗi và dữ liệu thay đổi. |
| Submit hoặc retry | Giữ dữ liệu nhập, phản hồi pending, chặn click lặp và phối hợp key server. | Network trace và side effect quan sát được, không chỉ toast. |
| Optimistic update | Giữ rollback theo mutation và xử lý cập nhật đồng thời; tránh ghi đè dữ liệu mới hơn. | Ca request lỗi, phản hồi đảo thứ tự và mutation liên tiếp. |
| Layout và lifecycle | Tìm phần tử gây tràn; xử lý cleanup, cancellation và stale result theo framework. | Ảnh viewport, console và test khi unmount/đổi route. |
| Quyền và dữ liệu | Ẩn UI chỉ là trải nghiệm; backend vẫn phải kiểm quyền và đầu vào. | Ca người dùng khác, server rejection và không lộ dữ liệu qua cache. |

## Đầu ra cần giữ khi liên quan

- UI diff: component, state và contract liên quan.
- Verification: viewport/keyboard/console/network đúng snapshot.
- Boundary report: mock nào dùng, browser nào thử và phần chưa chạy.

## Điều kiện dừng phần phụ thuộc

Contract chưa rõ hoặc API không có điều kiện test; ghi giới hạn thay vì thay bằng mock rồi cấp PASS tích hợp. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Chẩn đoán cụ thể: kết quả tìm kiếm bị trả sai thứ tự

Người dùng gõ `ca`, rồi `cat`; request thứ hai hoàn tất trước request thứ nhất. Nếu mọi response đều ghi vào cùng state, kết quả cho `ca` có thể đè kết quả mới.

1. Tái hiện bằng cách điều khiển độ trễ hai request; kiểm input đang hiển thị và query gắn với response, không chỉ nhìn spinner.
2. Xem thư viện fetch/cache hiện có: query key có chứa toàn bộ filter liên quan không; response cũ có đang ghi vào state ngoài cache không?
3. Dùng cơ chế của framework/thư viện để chỉ nhận kết quả cho query hiện tại. Nếu quản lý thủ công, kiểm request identity trước khi cập nhật cả data, error và loading; abort có thể giúp tiết kiệm tài nguyên nhưng không thay kiểm tra response cũ.
4. Thử xóa input, đổi filter, chuyển route và request cũ lỗi sau request mới. Kết quả và thông báo phải thuộc truy vấn hiện tại; không để lỗi cũ che kết quả mới.

Ca kiểm tra quan trọng là hoàn tất B trước A rồi xác nhận UI vẫn hiển thị B. Test chỉ gõ chậm rồi chờ mỗi request xong sẽ bỏ qua lỗi này.

Với optimistic mutation, kiểm tra tương tự theo từng mutation: rollback một request lỗi không được khôi phục toàn bộ danh sách về snapshot cũ nếu thao tác khác đã thành công. Nếu logic rollback quá khó chứng minh, cân nhắc đợi server hoặc refetch thay vì thêm state phức tạp.
