# Báo lỗi bảo mật

Không đưa secret, token, dữ liệu cá nhân hay payload có thể gây hại lên issue công khai. Với lỗi nhạy cảm, dùng kênh riêng mà chủ repository cung cấp trên GitHub; repo chưa công bố email tiếp nhận hoặc SLA xử lý riêng.

Báo cáo nên mô tả phiên bản, phạm vi, điều kiện khai thác, tác động và cách tái hiện tối thiểu trong môi trường test được phép. Các giả thuyết chưa kiểm chứng phải được ghi rõ.

Nếu phát hiện secret thật, báo vị trí và loại secret đã che giá trị. Xóa khỏi working tree không thay thế việc thu hồi và đánh giá lịch sử truy cập.

Installer chỉ quản lý payload dưới skill root được chọn, giữ ownership và từ chối symlink. Những kiểm soát này không tạo sandbox cho hành vi của skill trên host. Người dùng cần hiểu scope và quyền của môi trường đang sử dụng.
