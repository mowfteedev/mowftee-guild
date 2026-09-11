# 🛡️ Kịch Bản Tác Chiến 03: Tổng Vệ Sinh Mã Nguồn, Tối Ưu Hiệu Năng & Bảo Mật

> **Mục tiêu**: Rà soát lại toàn bộ dự án định kỳ: Quét sạch lỗ hổng bảo mật tiềm ẩn, xóa sổ nợ kỹ thuật (code smells), tối ưu các câu truy vấn chậm và làm sạch kho lưu trữ.

---

## 📝 Các Bước Tác Chiến & Prompt Mẫu

### Bước 1: Quét Lỗ Hổng & Rà Soát Bảo Mật (`@security`)
```text
@security Hãy tiến hành một đợt kiểm tra an ninh toàn diện (Security Audit) trên toàn bộ dự án:
1. Quét tìm xem có mật khẩu, private key hoặc token nhạy cảm nào bị sót trong code hay commit history không.
2. Kiểm tra các cổng API xem có lỗ hổng IDOR (truy cập chéo dữ liệu của người khác) không.
3. Rà soát cấu hình CORS, Helmet, Cookie và Rate Limiting.
4. Xuất báo cáo các lỗ hổng kèm mức độ rủi ro (Critical, High, Medium).
```

### Bước 2: Thẩm Định Nợ Kỹ Thuật & Mùi Hôi Của Code (`@code-reviewer`)
```text
@code-reviewer Hãy rà soát toàn bộ mã nguồn để dọn dẹp nợ kỹ thuật:
1. Tìm và chỉ ra các hàm khổng lồ (God functions > 50 dòng) để chia nhỏ.
2. Làm phẳng các tầng if/else lồng sâu bằng Guard Clauses.
3. Phát hiện các vòng lặp O(n^2), Promise thả nổi (floating promises) và nguy cơ rò rỉ bộ nhớ.
4. Phân loại rõ ràng 🔴 Blocker và 🟡 Suggestion.
```

### Bước 3: Soi Kế Hoạch Truy Vấn & Tối Ưu Chỉ Mục (`@database`)
```text
@database Hãy rà soát toàn bộ các câu truy vấn cơ sở dữ liệu trong dự án:
1. Kiểm tra xem có câu truy vấn nào gây ra vấn nạn N+1 không.
2. Có bảng nào đang bị quét cạn toàn bảng (Seq Scan) do thiếu index ở cột tìm kiếm hoặc khóa ngoại không?
3. Viết migration bổ sung các Partial Index hoặc Composite Index để đưa toàn bộ truy vấn về dưới 20ms.
```

### Bước 4: Tối Ưu Giao Diện & Core Web Vitals (`@frontend`)
```text
@frontend Hãy tối ưu hóa hiệu năng phía client:
1. Rà soát bundle size, áp dụng lazy loading cho các modal và component nặng.
2. Kiểm tra lại toàn bộ hình ảnh, đảm bảo định dạng WebP/AVIF và không gây giật khung hình (CLS = 0).
3. Đảm bảo mọi thao tác click đều có phản hồi thị giác dưới 150ms.
```

### Bước 5: Thẩm Định Tái Nghiệm Thu Toàn Diện (`@tester`)
```text
@tester Hãy chạy lại toàn bộ bài kiểm thử tự động, thử tải (Stress Test) và xác nhận hệ thống sau đợt tổng vệ sinh:
1. Xác nhận 100% test chạy pass với exit code 0.
2. Ký Chứng Nhận Nghiệm Thu xác nhận hệ thống vững vàng, sạch sẽ và an toàn.
```
