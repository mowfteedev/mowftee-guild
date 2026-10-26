# Runbook: Kiến trúc phần mềm

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. MVP nhỏ: cân nhắc module trong một ứng dụng trước khi chia dịch vụ.
2. Sự kiện ngoài transaction: làm rõ thời điểm commit và cơ chế outbox nếu cần độ bền.
3. Hệ thống cũ thiếu tài liệu: phân biệt kiến trúc quan sát được với kiến trúc mong muốn.
4. Hai phương án tương đương: ưu tiên phương án đội ngũ có thể vận hành.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Có thể giữ hiện trạng | Dùng phương án không đổi kiến trúc làm baseline trước khi đề xuất công nghệ mới. | So sánh chi phí, độ phức tạp và constraint đã biết. |
| Ranh giới dữ liệu | Xác định module sở hữu dữ liệu và giao tiếp công khai; mô tả chỗ cần transaction. | Sơ đồ dependency và đường đi một luồng hoàn chỉnh. |
| Dependency không ổn định | Thiết kế timeout budget, backpressure, suy giảm và phục hồi theo luồng nghiệp vụ. | Failure-mode table, điểm quan sát và cách kiểm chứng. |
| Event và side effect | Xác định ranh giới commit, durability và cơ chế retry; cân nhắc outbox khi yêu cầu bền vững. | Tình huống commit thành công nhưng publish/response thất bại. |
| Thay đổi lớn | Chia rollout tương thích và điều kiện quay lui hoặc roll-forward. | ADR với phương án loại bỏ, hệ quả và owner xem lại. |

## Đầu ra cần giữ khi liên quan

- ADR: context, constraints, alternatives, decision, consequences.
- Architecture map: module, data owner, contract, trust boundary.
- Transition plan: compatibility, failure handling và điểm dừng.

## Điều kiện dừng phần phụ thuộc

Chưa rõ owner invariant quan trọng; phương án vượt ràng buộc vận hành; hoặc thiếu thông tin quyết định làm đổi scope. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ quyết định: gửi email sau khi tạo đơn

Theo luồng thực tế từ nhận request → ghi đơn → gửi mail → trả kết quả. Xác định đơn có được coi là thành công nếu email chưa gửi, email có phải được gửi cuối cùng, và người dùng có chấp nhận thư trùng hay không.

| Phương án | Khi đáng cân nhắc | Đánh đổi cần nói rõ |
| --- | --- | --- |
| Gửi đồng bộ sau commit | Luồng nhỏ, có thể chờ và đã thống nhất cách xử lý khi mail lỗi | Request dài hơn; trả lỗi sau commit dễ khiến client hiểu nhầm đơn chưa được tạo. |
| Gửi trong tác vụ nền của tiến trình | Thư chỉ là tiện ích, chấp nhận mất tác vụ khi tiến trình dừng | Bắt lỗi không làm công việc trở nên bền vững. |
| Lưu ý định gửi cùng transaction, xử lý lại bằng worker | Cần khôi phục sau crash và theo dõi trạng thái gửi | Phải vận hành worker, retry và xử lý gửi trùng; outbox không tự bảo đảm đúng một email. |

Chọn theo yêu cầu về mất/trùng, thời gian phản hồi và khả năng vận hành, không theo xu hướng công nghệ. Nếu chọn outbox, lần theo cả trường hợp worker gửi xong rồi chết trước khi ghi nhận; nêu cách hạn chế trùng hoặc giới hạn còn lại.

ADR ngắn cho quyết định này chỉ cần: yêu cầu độ bền, phương án chọn, hai phương án loại bỏ, cửa sổ lỗi và cách chuyển đổi. Với thay đổi nội bộ nhỏ không có đánh đổi lâu dài, giải thích trong diff là đủ.
