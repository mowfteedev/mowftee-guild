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

Trong Antigravity App dùng slash command, ví dụ `/frontend`, thay cho `$frontend`. Host cũng có thể chọn skill theo mô tả. [Danh mục skill](skills-catalog.md) giúp chọn vai trò khi cần.

## Tài liệu tùy chọn

Runbook nằm cùng từng skill, chỉ đọc phần liên quan. Các workflow trong `workflows/` là gợi ý thứ tự làm; không phải cổng duyệt bắt buộc. Nếu muốn lưu thông tin dài hạn, copy mẫu từ `templates/memory/` vào dự án và điền tay; không cần tạo đủ bộ mỗi lần.

## Skill và plugin

Skill là các file hướng dẫn để host đọc và làm theo. Bộ này không cần process hay server riêng. Plugin là cách đóng gói/phân phối thêm; MCP chỉ cần khi muốn kết nối công cụ hoặc dữ liệu qua server. Phần đó sẽ làm riêng khi được yêu cầu.
