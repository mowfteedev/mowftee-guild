# Sửa lỗi từ tái hiện đến kiểm chứng

Áp dụng khi điều tra một lỗi cụ thể. Giữ thứ tự bốn bước dưới đây; phần chưa làm được phải được báo rõ. Một trợ lý thực hiện được toàn bộ, không cần người duyệt riêng hoặc tạo hồ sơ bắt buộc. Có thể gọi trực tiếp skill [systematic-debugging](../skills/systematic-debugging/SKILL.md).

## 1. Tái hiện lỗi trước khi sửa

- Ghi triệu chứng, đầu vào, hành vi mong đợi và hành vi thực tế; xác định phiên bản cùng môi trường xảy ra lỗi.
- Chọn ca nhỏ nhất còn thể hiện đúng lỗi: test có sẵn, test hồi quy mới, script hoặc thao tác thủ công. Chạy trên bản lỗi trước khi đổi logic và giữ kết quả quan trọng.
- Xác nhận ca thất bại vì triệu chứng cần sửa. Thiếu dependency, lỗi import, fixture hoặc kết nối chỉ được tính nếu đó chính là triệu chứng đang điều tra; nếu chúng chặn việc kiểm một lỗi khác thì chưa tái hiện được lỗi mục tiêu.
- Nếu chưa tái hiện được, ghi điều đã thử và điều kiện còn thiếu; tiếp tục thu bằng chứng được phép. Không ghi đè thay đổi của người dùng để lấy baseline, không tự thử lên production.

## 2. Xác minh nguyên nhân

- Theo đường thực thi từ đầu vào tới điểm sai, dùng log, trace, dữ liệu hoặc điều kiện trong code để giải thích cơ chế gây lỗi.
- Nêu giả thuyết cùng quan sát có thể xác nhận hoặc bác bỏ nó. Chọn kiểm tra phân biệt các giả thuyết; không đổi nhiều thứ cùng lúc rồi suy ra nguyên nhân từ một lần hết lỗi.
- Chỉ sửa khi có căn cứ liên hệ nguyên nhân với triệu chứng. Không tái hiện được tại local vẫn có thể điều tra bằng dữ liệu sự cố thật; phân biệt suy luận từ code với hành vi đã chạy và quan sát.
- Nếu giả thuyết bị bác, cập nhật cách giải thích và kiểm tra tiếp. Không tiếp tục chồng bản vá hoặc nới assertion để giữ phương án ban đầu.

## 3. Sửa tối thiểu và kiểm lại cùng ca

- Sửa cơ chế gây lỗi trong phạm vi đã cho phép; giữ hành vi và contract ngoài phạm vi. Không tiện thể đổi kiến trúc, nâng dependency hoặc format hàng loạt.
- Chạy lại ca ở bước 1 trên bản sửa với cùng kỳ vọng. Nếu thay input, môi trường hoặc kỳ vọng, giải thích vì sao hai kết quả vẫn có thể đối chiếu; không gọi một test khác dễ hơn là bằng chứng trước/sau.
- Không nuốt lỗi, thêm retry tùy tiện, bỏ test hoặc mock chính logic đang kiểm để lấy kết quả xanh. Thêm test hồi quy tự động khi nó bảo vệ hành vi có ý nghĩa.

## 4. Kiểm hồi quy và kết luận

- Chọn các luồng bị ảnh hưởng từ call path và loại thay đổi: luồng hợp lệ, nhánh lỗi, caller dùng chung, quyền hoặc cạnh tranh khi liên quan. Không mặc định một test xanh chứng minh toàn bộ tính năng đúng.
- Chạy các kiểm tra phù hợp; khi có lỗi, phân biệt lỗi mới với lỗi baseline bằng dữ kiện, không tự nhận mọi lỗi có sẵn đều ngoài phạm vi.
- Bàn giao ngắn: nguyên nhân và căn cứ, thay đổi, kết quả cùng ca trước/sau, hồi quy đã chạy và phần chưa xác minh. Có thể trả ngay trong hội thoại.

## Bằng chứng đủ để kết luận

Gắn kết quả với command/thao tác, phiên bản code hoặc artifact, môi trường và output quan trọng; có exit code nếu là lệnh, che secret. Kết quả CI cần link tới đúng commit/artifact. Với working tree chưa commit, nêu phần thay đổi đã có lúc chạy.

Bằng chứng còn giá trị khi code, cấu hình, dữ liệu và môi trường liên quan vẫn khớp. Sau thay đổi có thể ảnh hưởng kết quả, chạy lại phần kiểm tra đó. Không bắt chạy lại chỉ vì sang lượt chat khác; cũng không dùng kết quả cũ nếu chưa đối chiếu phiên bản.

Chỉ nói lỗi đã được xác minh là sửa xong trong phạm vi đã thử. Nếu chưa có ca tái hiện hoặc chưa chạy được bản sửa, báo thay đổi đã thực hiện và giới hạn còn lại; không thay bằng tuyên bố “đã fix”. Đọc code không đồng nghĩa đã chạy test; ca hồi quy minh họa không tự chứng minh lỗi production đã được tái hiện.

READ-ONLY chỉ điều tra và trả kết quả. Giới hạn người dùng đặt cho sửa file, push hoặc thao tác dịch vụ vẫn giữ nguyên.
