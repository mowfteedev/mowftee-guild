# Ứng phó sự cố và postmortem

Giảm tác động trong quyền đã có, giữ bằng chứng và xác định việc cần làm để tránh tái diễn.

Xác định hệ thống, phạm vi ảnh hưởng và quyền thao tác trước. Ưu tiên khôi phục hành trình người dùng; mitigation có tác dụng chưa đồng nghĩa đã tìm được nguyên nhân.

## Gợi ý thực hiện

1. Đo ảnh hưởng người dùng, thu dữ liệu an toàn và ghi giả thuyết có thể kiểm chứng.
2. Chọn hành động nhỏ có thể đảo ngược, ghi trước/sau và điểm dừng; thay một biến khi có thể.
3. Kiểm user journey và độ ổn định trong cửa sổ phù hợp, giữ residual risk.
4. Ghi yếu tố góp phần, điều hiệu quả và việc cần sửa. Với bản sửa lâu dài, dùng [bốn bước debug](04-sua-loi.md) theo dữ kiện sự cố; nếu chưa tái hiện local thì giữ giới hạn đó.

## Kiểm tra và kết thúc

Kiểm lại ảnh hưởng và luồng người dùng sau hành động, giữ timeline có nguồn. Bàn giao phần đã phục hồi, giả thuyết chưa xác minh và bước tiếp; không đánh dấu đã fix nguyên nhân chỉ vì restart làm hết triệu chứng.

[Chọn workflow khác](README.md) · [Skill incident-responder](../skills/incident-responder/SKILL.md)
