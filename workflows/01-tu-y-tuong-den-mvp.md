# 🚀 Kịch Bản Tác Chiến 01: Từ Ý Tưởng Thô Đến Sản Phẩm MVP Chạy Thực Tế

> **Mục tiêu**: Điều phối dây chuyền 10 chuyên gia của `mowftee-guild` trong Antigravity để biến một ý tưởng sơ khai thành một sản phẩm chạy mượt mà, an toàn, có kiểm thử phá hoại và tài liệu bàn giao chỉn chu.

---

## 🗺️ Bản Đồ Phối Hợp Dây Chuyền

```text
[Ý tưởng của Bang chủ]
         │
         ▼
 1. @tech-lead       ──▶ Thiết lập Kiến trúc & Bộ nhớ .memory/
         │
         ├──────────────────────────┐
         ▼                          ▼
 2. @database (Schema & Index)    3. @designer (Design Tokens & UI)
         │                          │
         ▼                          │
 4. @backend (API & Auth)           │
         │                          │
         └───────────┬──────────────┘
                     ▼
             5. @frontend (Ghép UI & Gọi API)
                     │
                     ▼
             6. @code-reviewer (Bắt lỗi Blocker & Clean Code)
                     │
                     ▼
             7. @security (Quét OWASP, IDOR & Khóa bí mật)
                     │
                     ▼
             8. @tester (Phá hoại dữ liệu biên & Cấp chứng nhận)
                     │
                     ▼
             9. @devops (Đóng gói Docker & Nginx Reverse Proxy)
                     │
                     ▼
            10. @doc-writer (Viết README 5 giây & Bàn giao)
```

---

## 📝 Các Bước Tác Chiến & Lệnh Prompt Mẫu Trong Antigravity

### Bước 1: Khởi Tạo Kiến Trúc & Bộ Nhớ Dự Án (`@tech-lead`)
Mở Antigravity trong thư mục dự án và gửi prompt:

```text
@tech-lead Tôi muốn xây dựng dự án [Tên Dự Án] với ý tưởng: [Mô tả chi tiết ý tưởng của bạn].
Hãy phân tích ranh giới nghiệp vụ, lựa chọn Tech Stack phù hợp nhất, khởi tạo bộ nhớ dự án trong .memory/ (architecture.md, progress.md) và phân chia công việc cho các thành viên trong guild.
```

### Bước 2: Thiết Kế Cơ Sở Dữ Liệu & Chỉ Mục (`@database`)
Sau khi Tech Lead chốt kiến trúc, gửi tiếp:

```text
@database Dựa trên architecture.md do @tech-lead vừa định nghĩa, hãy thiết kế Lược đồ cơ sở dữ liệu (PostgreSQL) đạt chuẩn 3NF:
1. Đầy đủ ràng buộc khóa ngoại, timestamp và soft delete.
2. Đánh index 100% cho các khóa ngoại và partial index cho các trường trạng thái.
3. Cung cấp file migration SQL có thể chạy ngay.
```

### Bước 3: Định Hình Hệ Thống Thiết Kế (`@designer`)
Song song với database, định hình giao diện:

```text
@designer Hãy xây dựng bộ Design Tokens (bảng màu, thang lưới 8pt spacing, typography scale) và đặc tả các thành phần giao diện chính (Buttons, Cards, Inputs với đủ 6 trạng thái) cho dự án này để chuẩn bị bàn giao cho @frontend.
```

### Bước 4: Xây Dựng Hệ Thống Máy Chủ & API (`@backend`)
Sau khi có schema từ database:

```text
@backend Hãy triển khai hệ thống máy chủ và các API theo chuẩn Clean Architecture:
1. Hợp đồng API minh bạch, kiểm tra DTO với Zod.
2. Hỗ trợ header Idempotency-Key cho các thao tác tạo mới nhạy cảm.
3. Cấu trúc phản hồi lỗi chuẩn (Error Envelope) kèm request_id.
4. Có sẵn 2 endpoint /healthz và /readyz.
```

### Bước 5: Ghép Giao Diện Người Dùng Mobile-First (`@frontend`)
Sau khi có API và Design Tokens:

```text
@frontend Hãy xây dựng giao diện ứng dụng kết nối với API của @backend theo chuẩn Mobile-First:
1. Đảm bảo hiển thị hoàn hảo trên màn hình 375px trở lên, điểm chạm nút bấm tối thiểu 44px.
2. Bao bọc trọn vẹn 4 trạng thái: Skeleton Loading, Empty State, Error State (kèm nút Retry), và Success State.
3. Không để xảy ra bất kỳ lỗi console đỏ nào.
```

### Bước 6: Thẩm Định Mã Nguồn & Rà Soát Bảo Mật (`@code-reviewer` + `@security`)
Trước khi cho chạy thử nghiệm:

```text
@code-reviewer và @security Hãy tiến hành thẩm định toàn bộ mã nguồn vừa viết:
- @code-reviewer: Bắt sạch các lỗi race conditions, N+1 queries, bẫy boolean, và đánh dấu rõ 🔴 Blocker / 🟡 Suggestion / 💭 Nit.
- @security: Quét sạch nguy cơ rò rỉ khóa bí mật, kiểm tra phân quyền IDOR và cấu hình tiêu đề Helmet / CORS an toàn.
```

### Bước 7: Phá Hoại Thực Chiến & Nghiệm Thu (`@tester`)
Sau khi các lỗi Blocker được sửa:

```text
@tester Hãy đóng vai Reality Checker phá hoại cực hạn tính năng này:
1. Thử nghiệm bơm chuỗi 10.000 ký tự, số âm, ký tự đặc biệt, click đúp liên tục (rage clicks) và ngắt mạng giữa chừng.
2. Chạy kịch bản tự động hóa Playwright không sleep.
3. Nếu phát hiện lỗi thì từ chối nghiệm thu; nếu đạt hãy cấp Chứng Nhận Nghiệm Thu (Production Ready).
```

### Bước 8: Đóng Gói Docker & Cấu Hình Hạ Tầng (`@devops`)
Sau khi tester đã ký nghiệm thu:

```text
@devops Hãy đóng gói toàn bộ dự án để sẵn sàng chạy thực tế:
1. Dockerfile đa tầng siêu nhẹ (<150MB) chạy non-root user.
2. docker-compose.yml hoàn chỉnh tích hợp App, Postgres, Redis và Nginx (cô lập mạng nội bộ).
3. Cấu hình Nginx reverse proxy ép HTTPS và ẩn server_tokens.
```

### Bước 9: Đóng Gói Tài Liệu & Bàn Giao (`@doc-writer`)
Bước cuối cùng để hoàn tất dự án:

```text
@doc-writer Dự án đã hoàn thành và sẵn sàng bàn giao! Hãy xuất hiện và biên soạn:
1. File README.md vượt qua bài kiểm tra 5 giây với hướng dẫn cài đặt 3 bước (Copy-Paste Quickstart).
2. Bảng chú thích toàn diện các biến môi trường trong .env.example.
3. Đặc tả API hoàn chỉnh kèm lệnh curl chạy được ngay.
```
