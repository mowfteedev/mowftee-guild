# ⚔️ mowftee-guild

> **10 Đặc Nhiệm AI Tinh Nhuệ Cho Google Antigravity — 100% Tiếng Việt, Chuẩn Thực Chiến.**

[![Antigravity](https://img.shields.io/badge/Antigravity-Ready-0EA5E9?style=flat-square&logo=google)](https://github.com/mowfteedev/mowftee-guild)
[![Agents](https://img.shields.io/badge/Agents-10%20Specialists-indigo?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## ⚡ Cài Đặt Nhanh (30 Giây)

```bash
git clone https://github.com/mowfteedev/mowftee-guild.git
cd mowftee-guild
./setup.sh install
```
*(Script tự động nạp 10 chuyên gia vào `~/.gemini/config/skills/`, mở Antigravity ở bất kỳ đâu cũng dùng được).*

---

## 🏛️ Đội Ngũ 10 Cao Thủ

| @Gọi | Vai trò | Nhiệm vụ chính |
| :--- | :--- | :--- |
| **`@tech-lead`** | 🏛️ Tổng Quản Kỹ Thuật | Thiết kế kiến trúc, chia nhỏ task, quản lý `.memory/` |
| **`@frontend`** | 🎨 Kỹ Sư Giao Diện | UI Mobile-First, phản hồi <150ms, bao bọc 4 trạng thái |
| **`@backend`** | 🏗️ Kiến Trúc Sư Server | API Contract-First, chống trùng đơn `Idempotency-Key` |
| **`@database`** | 🗄️ Thần Đèn Dữ Liệu | Schema 3NF, index 100% khóa ngoại, diệt sạch lỗi N+1 |
| **`@designer`** | 🎨 Kiến Trúc Sư UI/UX | Design Tokens, lưới 8pt grid, 6 trạng thái tương tác |
| **`@code-reviewer`** | 👁️ Gác Cổng Chất Lượng | Quyền phủ quyết Veto, bắt Blocker, triệt tiêu nợ kỹ thuật |
| **`@tester`** | 🧐 Khắc Tinh Của Bug | Reality Checker, phá hoại biên dữ liệu, cấp chứng nhận |
| **`@security`** | 🔐 Vệ Sĩ An Ninh | Quét OWASP Top 10, chặn rò rỉ secret, chống IDOR/XSS |
| **`@devops`** | ⚙️ Kỹ Sư Vận Hành | Dockerfile <150MB non-root, Docker Compose, Nginx SSL |
| **`@doc-writer`** | 📚 Bậc Thầy Bàn Giao | README 5 giây, cài đặt 3 bước, API Docs có curl mẫu |

---

## 🚀 Cách Dùng Khi Tạo Dự Án Mới

```bash
# 1. Tạo dự án và nạp bộ nhớ
mkdir my-app && cd my-app
/path/to/mowftee-guild/setup.sh init .

# 2. Mở Antigravity
agy
```

```text
# 3. Ra lệnh trong khung chat:
@tech-lead Hãy đọc .memory/ và lên kế hoạch làm app [Mô tả ý tưởng ở đây].
```

---

## 🧠 Bộ Nhớ Dự Án (`.memory/`)

Giúp AI không bao giờ bị quên bối cảnh giữa các phiên làm việc:
- **`architecture.md`**: Kiến trúc & Tech Stack đã chọn.
- **`progress.md`**: Tiến độ (Đã xong / Đang làm / Việc tiếp theo).
- **`adr/`**: Biên bản lưu các quyết định kỹ thuật quan trọng.

---

## 🛠️ Bộ Lệnh `setup.sh`

```bash
./setup.sh install     # Cài đặt / đồng bộ 10 chuyên gia vào Antigravity
./setup.sh check       # Kiểm tra sức khỏe toàn bộ chuyên gia
./setup.sh init [path] # Cấp nhanh não bộ .memory/ cho dự án mới
./setup.sh uninstall   # Gỡ bỏ sạch sẽ khỏi máy
```

---

## 🎬 Kịch Bản Tác Chiến ([`workflows/`](workflows/))

- [**01. Từ Ý Tưởng Đến MVP**](workflows/01-tu-y-tuong-den-mvp.md) — 9 bước phối hợp dây chuyền từ số 0.
- [**02. Thêm Tính Năng Mới**](workflows/02-them-tinh-nang-moi.md) — Bổ sung tính năng an toàn, zero-regression.
- [**03. Tổng Vệ Sinh & Bảo Mật**](workflows/03-tong-ve-sinh-va-bao-mat.md) — Dọn nợ kỹ thuật & audit an ninh.

---

> 💡 **Tip**: Chạy `agy --dangerously-skip-permissions` để thao tác mượt mà, không bị hỏi xác nhận từng câu lệnh.
