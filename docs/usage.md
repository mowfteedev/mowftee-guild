# Dùng skill trong dự án cá nhân

Chọn góc nhìn đúng với đầu việc. Cùng một trợ lý có thể lập kế hoạch, triển khai rồi tự kiểm; không cần mở nhiều agent hay có người duyệt riêng.

## Ví dụ

```text
Dùng $tech-lead đọc dự án và đề xuất cách thêm giỏ hàng.
Chia các phần cần làm, chỉ ra chỗ ảnh hưởng dữ liệu và API; đừng viết code vội.
```

```text
Dùng $frontend sửa form khi API lỗi làm mất nội dung đã nhập.
Giữ design system hiện có, xử lý retry và kiểm tra bố cục trên mobile.
```

```text
Dùng $code-reviewer đọc lại diff và tìm lỗi thực tế.
Với mỗi lỗi, nêu tình huống xảy ra và hậu quả; không cần bịa finding nếu không thấy.
```

```text
Dùng $tester kiểm lại luồng vừa sửa.
Cho biết đã thử gì, kết quả ra sao và phần nào chưa chạy được.
```

```text
Dùng $systematic-debugging điều tra lỗi này.
Tái hiện bằng ca nhỏ nhất trước khi sửa; xác minh nguyên nhân bằng dữ kiện,
sửa tối thiểu, chạy lại cùng ca rồi kiểm hồi quy trong vùng ảnh hưởng.
Nếu chưa tái hiện hoặc chưa chạy được, ghi rõ giới hạn thay vì báo đã fix.
```

Trong Antigravity App dùng slash command, ví dụ `/frontend`, thay cho `$frontend`. Host cũng có thể chọn skill theo mô tả. [Danh mục skill](skills-catalog.md) giúp chọn vai trò khi cần.

Các ví dụ `$tên-skill` ở trên dành cho bản chép trực tiếp. Với plugin Codex, dùng tiền tố `mowftee-guild:`, chẳng hạn `$mowftee-guild:systematic-debugging`, hoặc chọn đúng mục của plugin trong `/skills`. Xem [cài và dùng plugin](plugins.md).

## Tài liệu tùy chọn

Runbook nằm cùng từng skill, chỉ đọc phần liên quan. Chọn một [workflow](../workflows/README.md) theo đầu việc; với sửa lỗi, giữ bốn bước kiểm chứng và báo phần chưa kiểm được. Khi cần lưu kết quả, chọn một [mẫu ghi chú](../templates/memory/README.md) và điền phần hữu ích. Có thể trả kết quả ngay trong hội thoại cho tác vụ nhỏ.

## Skill và plugin

Skill là các file hướng dẫn để host đọc và làm theo. Plugin có thể đóng gói các skill đó thành một gói cài; MCP bổ sung công cụ hoặc dữ liệu qua server khi cần. Xem [giới thiệu plugin](plugins.md) để hiểu cấu trúc và phạm vi phù hợp với bộ này.
