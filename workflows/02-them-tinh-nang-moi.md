# ⚡ Kịch Bản Tác Chiến 02: Bổ Sung Tính Năng Mới (Zero-Regression Workflow)

> **Mục tiêu**: Bổ sung một tính năng mới vào hệ thống đang chạy mượt mà mà không làm gãy các tính năng cũ (Không phát sinh lỗi hồi quy - Zero Regression).

---

## 🗺️ Quy Trình Tác Chiến

```text
1. Đọc Bộ nhớ .memory/  ──▶  2. Lập kế hoạch ADR  ──▶  3. Migration DB An Toàn
        (@tech-lead)               (@tech-lead)                (@database)
                                                                    │
                                                                    ▼
7. Bàn giao & Changelog ◀──  6. Nghiệm thu thực tế ◀──  4. API & UI Mới
        (@doc-writer)               (@tester)              (@backend + @frontend)
                                                                    ▲
                                                                    │
                                                        5. Soát lỗi & Bảo mật
                                                        (@code-reviewer + @security)
```

---

## 📝 Các Bước Tác Chiến & Prompt Mẫu

### Bước 1: Đọc Bộ Nhớ & Đánh Giá Bán Kính Ảnh Hưởng (`@tech-lead`)
```text
@tech-lead Hãy đọc các file trong .memory/ (architecture.md và progress.md).
Chúng ta cần bổ sung tính năng: [Mô tả tính năng mới cần thêm].
Hãy đánh giá bán kính ảnh hưởng (Blast Radius): Tính năng này có làm thay đổi bảng dữ liệu cũ hay gãy API cũ không? Hãy viết 1 bản kế hoạch ADR ngắn gọn để triển khai.
```

### Bước 2: Di Chuyển Schema An Toàn Không Khóa Bảng (`@database`)
```text
@database Dựa trên kế hoạch của @tech-lead, hãy viết file Migration để thêm bảng/cột mới cho tính năng này.
Yêu cầu:
- Tuyệt đối không khóa bảng đọc/ghi (dùng CREATE INDEX CONCURRENTLY).
- Viết đủ 2 chiều UP và DOWN để sẵn sàng rollback nếu có sự cố.
```

### Bước 3: Mở Rộng API & Kết Nối Giao Diện (`@backend` & `@frontend`)
```text
@backend và @frontend Hãy phối hợp triển khai tính năng mới:
- @backend: Viết endpoint mới theo chuẩn Contract-First, kiểm tra DTO đầu vào và bảo đảm quyền sở hữu dữ liệu.
- @frontend: Dựng UI mới trên màn hình di động 375px, xử lý đủ 4 trạng thái (Loading, Empty, Error, Success).
```

### Bước 4: Thẩm Định Lỗi Hồi Quy (`@code-reviewer` & `@tester`)
```text
@code-reviewer và @tester Hãy kiểm tra xem việc bổ sung tính năng mới này có làm hỏng các tính năng cũ không:
- @code-reviewer: Soát lại git diff, kiểm tra xem có hàm cũ nào bị sửa đổi tham số mà chưa cập nhật các nơi gọi cũ không.
- @tester: Chạy lại toàn bộ test suite cũ (Regression Testing) và kiểm thử phá hoại tính năng mới.
```

### Bước 5: Cập Nhật Tài Liệu & Ghi Chú Phát Hành (`@doc-writer`)
```text
@doc-writer Tính năng mới đã hoàn tất và vượt qua kiểm thử! Hãy cập nhật:
1. Ghi chú vào CHANGELOG.md theo chuẩn Keep a Changelog mục [Added].
2. Bổ sung tài liệu mô tả endpoint mới vào README.md.
```
