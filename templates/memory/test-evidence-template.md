# Bằng chứng kiểm chứng: {{PROJECT_NAME}}

> Mẫu ghi chú tùy chọn. Chỉ copy và điền phần hữu ích; không cần tạo đủ bộ để dùng skill.
Tạo: {{DATE_UTC}}. Trạng thái tổng hợp: NOT_RUN.

## Phạm vi

- AC / task / bug: chưa chọn.
- Commit, artifact digest hoặc snapshot + dirty state: chưa ghi nhận.
- OS, runtime, dependency và dữ liệu test: chưa ghi nhận.
- Người kiểm tra và cách đã thử: chưa ghi nhận.

## Kiểm tra thực tế

| ID | AC | Command / thao tác | Thời điểm | Exit code | Kết quả thực tế | Trạng thái | Artifact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chưa chạy | Chưa chọn | Chưa thực hiện | Chưa có | Chưa có | Chưa có | NOT_RUN | Chưa có |

## Giới hạn

Ghi rõ mock, dữ liệu không đại diện, check bị chặn và hành vi chưa quan sát. Test cấu trúc skill không chứng minh chất lượng hành vi của agent. Test installer không chứng minh skill đã chạy trong Antigravity/Codex.

## Evidence theo loại thay đổi

- UI: ảnh, viewport, thao tác thực, keyboard/focus khi liên quan.
- Backend: response và side effect dữ liệu, quyền, transaction, concurrency khi liên quan.
- Migration: trước/sau, chạy lại, rollback/roll-forward và tính toàn vẹn.
- Hiệu năng: baseline, workload, môi trường, raw samples, lỗi và chi phí tài nguyên.
- Tài liệu/CLI: lệnh thật, output, mã thoát và môi trường cô lập.

Chỉ thu evidence cần thiết cho phạm vi; che secret, token và dữ liệu cá nhân. Không thay log thật bằng số liệu từ ví dụ.

## Kết luận

NOT_RUN. Điền kết luận sau khi thực hiện; ghi rủi ro còn lại và điều kiện kiểm lại khi snapshot thay đổi.
