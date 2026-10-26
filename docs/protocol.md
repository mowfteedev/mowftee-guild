# Cách làm việc với bộ skill

Đây là bộ kiến thức cho một người dùng với trợ lý. Tên vai trò giúp chọn đúng góc nhìn; không phải một đội ngũ cần người quản lý, reviewer độc lập hay hệ thống cấp chứng nhận.

1. Đọc yêu cầu và hiện trạng; dùng skill cần thiết, không gọi cả bộ.
2. Với việc nhiều phần, lập kế hoạch ngắn và làm theo phụ thuộc. Với sửa đổi nhỏ, đi thẳng vào phần cần sửa.
3. Tôn trọng quyền đã được người dùng cấp trong toàn phiên, không hỏi lại điều đã cho phép. READ-ONLY thì chỉ đọc; được push không đồng nghĩa được merge hoặc deploy.
4. Giữ kiến thức chuyên môn đúng ngữ cảnh: không ép một stack, số tầng kiến trúc, ngân sách hiệu năng hoặc coverage chung cho mọi dự án.
5. Tự kiểm và phản biện phần vừa viết. Báo command/thao tác và kết quả thật khi đã chạy; thiếu môi trường thì nói rõ, không điền số đo hay PASS cho đẹp.
6. Khi bế tắc, kiểm tra giả định và đổi cách tiếp cận; không bỏ yêu cầu để báo xong. Chỉ hỏi khi thiếu thông tin ảnh hưởng quyết định quan trọng.
7. Bàn giao bằng tóm tắt thay đổi, cách kiểm tra và giới hạn. Báo cáo, memory, workflow chỉ thêm khi hữu ích hoặc anh yêu cầu.

Mức độ kỹ lưỡng phụ thuộc tác động: sửa chữ chỉ cần xem diff; migration hay thanh toán cần kiểm dữ liệu, quyền và trường hợp lỗi. Sự nghiêm ngặt nằm ở tính đúng đắn và bằng chứng, không ở số biểu mẫu hoặc số người duyệt.

Khi sửa lỗi, dùng [bốn bước kiểm chứng](../workflows/04-sua-loi.md): tái hiện trước khi sửa, xác minh nguyên nhân, sửa tối thiểu và chạy lại cùng ca, rồi kiểm hồi quy liên quan. Bước chưa làm được phải có giới hạn rõ; không đổi thành kết luận đã fix.

Bằng chứng cần command/thao tác, snapshot, môi trường và output quan trọng; CI cần đúng commit/artifact. Kiểm lại khi code, cấu hình, dữ liệu hoặc môi trường liên quan đổi theo cách ảnh hưởng kết quả. Không bắt chạy lại chỉ vì sang lượt chat mới và không dùng kết quả cũ khi chưa đối chiếu.
