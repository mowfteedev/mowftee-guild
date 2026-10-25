# Sử dụng guild theo tình huống

## Đường dẫn và cách gọi

| Host | Global directory CLI chọn | Workspace directory | Cách gọi thủ công tham khảo |
| --- | --- | --- | --- |
| Codex CLI/IDE | `~/.agents/skills` | `<project>/.agents/skills` | `$backend`, `/skills` |
| Antigravity App/IDE | `~/.gemini/config/skills` | `<project>/.agents/skills` | `/backend` trong App; IDE có Customizations |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills` | `<project>/.agents/skills` | `/backend` |

Đường dẫn đối chiếu [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills) và [Google Antigravity Docs](https://antigravity.google/docs/skills) ngày 26/10/2026. Host có thể thay đổi UI; dùng menu quản lý skill của host để xác nhận khả năng discover thực tế. Bộ kiểm thử repo không điều khiển GUI hai host.

## Prompt có đủ thông tin

Mẫu prompt gồm mục tiêu, hiện trạng cần đọc, phạm vi được phép và đầu ra. Không cần liệt kê toàn bộ quy trình vào mỗi prompt.

### Khảo sát chỉ đọc

```text
Dùng $software-architect đọc repo, mô tả module và đường đi dữ liệu.
READ-ONLY: không ghi file, cài package hay gọi dịch vụ có side effect.
Báo điều quan sát được, giả định và câu hỏi kiến trúc còn mở.
```

### Sửa lỗi

```text
Dùng $backend để sửa lỗi gửi lại request tạo hai đơn hàng.
Đọc contract và test hiện có, tái hiện lỗi, bảo toàn dữ liệu và kiểm chứng concurrency.
Được sửa local và chạy test trong môi trường tạm; chưa deploy.
```

### Review

```text
Dùng $code-reviewer review diff giữa main và HEAD, chỉ đọc.
Mỗi finding ghi file, vị trí, trigger, tác động và mức độ.
Báo các kiểm tra đã chạy, phần còn thiếu và không tự sửa code.
```

### Nghiệm thu

```text
Dùng $tester kiểm chứng AC trong .memory/requirements.md trên HEAD hiện tại.
Đối chiếu test, thử các luồng quan trọng trong môi trường test được phép.
Ghi rõ PASS/FAIL/BLOCKED/NOT_RUN và evidence; không tự cấp quyền deploy.
```

### Cải thiện bộ skill

```text
Dùng $skill-maintainer đánh giá ranh giới frontend, designer và accessibility.
Sửa mô tả nếu có trigger chồng lấn, bổ sung scenario kiểm định liên quan.
Tách kết quả static validation khỏi behavioral eval chưa chạy.
```

Đối với Antigravity App, thay ký hiệu `$` bằng slash command của host. Không giả định tên skill tự tạo một process hoặc người review độc lập.

## Dùng workflow và memory

Workflow trong thư mục `workflows/` là hướng dẫn tổ chức công việc, không phải plugin/slash command tự được đăng ký. Trỏ rõ file workflow từ bản clone khi cần. `init` chỉ tạo file còn thiếu; đọc và chốt AC/owner trước khi đánh dấu tiến độ. Cài skill không tự ghi bộ nhớ vào dự án đang mở.

## Giảm context

Cài profile sát nhu cầu. Description giúp host chọn skill; mỗi entrypoint dẫn tới runbook riêng. Không yêu cầu đọc cả 23 skill hoặc toàn bộ `.memory/` mỗi lần. Khi bàn giao, chuyển đường dẫn artifact và tóm tắt cùng điều kiện cần, không cắt bỏ dữ kiện ảnh hưởng kết luận.
