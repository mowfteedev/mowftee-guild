# 🏛️ Kiến Trúc Hệ Thống: [Tên Dự Án]

> *Tài liệu này là nguồn chân lý kỹ thuật (Single Source of Truth) do `@tech-lead` quản lý. Mọi thay đổi kiến trúc lớn phải được thảo luận và cập nhật tại đây.*

## 1. Tổng Quan & Mục Tiêu Kỹ Thuật
- **Mục tiêu sản phẩm**: [Mô tả ngắn gọn 1-2 câu về bài toán cốt lõi]
- **Kiến trúc chủ đạo**: Monolith tinh gọn / Modular Monolith / Microservices
- **Môi trường hoạt động**: Node.js / Python / Go / Docker / VPS Linux

## 2. Công Nghệ Sử Dụng (Tech Stack)
- **Frontend**: [React / Next.js / Vue / Tailwind CSS]
- **Backend**: [Node.js + Express/NestJS / Python + FastAPI / Go]
- **Database**: [PostgreSQL / MySQL / Redis cho Cache]
- **DevOps & Hạ tầng**: [Docker / Docker Compose / Nginx / GitHub Actions]

## 3. Ranh Giới Nghiệp Vụ & Cấu Trúc Module
- **Module Auth / Identity**: Đăng ký, đăng nhập, cấp JWT / Refresh token.
- **Module Core Business**: Logic nghiệp vụ trung tâm.
- **Module Data / Storage**: Truy vấn DB, quản lý file upload.

## 4. Quy Chuẩn Kỹ Thuật Bắt Buộc (Guild Standards)
1. **API Contract**: Chuẩn RESTful, trả về mã lỗi kèm `request_id`, hỗ trợ `Idempotency-Key` cho các thao tác ghi quan trọng.
2. **Database**: Chuẩn hóa 3NF, index 100% các cột Khóa ngoại, không để xảy ra N+1 queries.
3. **Frontend**: Chuẩn Mobile-First, phản hồi tương tác dưới 150ms, bao bọc đủ 4 trạng thái (Loading, Empty, Error, Success).
4. **Bảo mật**: Không commit `.env` vào git, kiểm tra IDOR ở tầng Service, có Rate Limiting cho các cổng nhạy cảm.
5. **Kiểm thử**: Mọi PR phải có ít nhất 1 bài test kiểm tra luồng chính và ca lỗi biên do `@tester` chứng nhận.
