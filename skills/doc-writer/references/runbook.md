# Runbook: Tài liệu và bàn giao

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. CLI đổi option: cập nhật tất cả quickstart liên quan.
2. Chưa test trên macOS: nêu giới hạn, không quảng cáo đã hỗ trợ đầy đủ.
3. Mẫu test report: không điền sẵn PASS hoặc số phần trăm.
4. Link trỏ file chưa có: tạo nội dung có ích hoặc bỏ liên kết.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Quickstart | Ghi prerequisite, command thật, path và đầu ra; chạy trong môi trường tạm. | Transcript command/exit code đúng phiên bản. |
| Reference | Đối chiếu CLI help/schema, flags, defaults và errors. | Bảng option/API khớp implementation. |
| Migration | Ghi breaking change, dữ liệu cần giữ, backup và cách quay lui. | Before/after usage và hướng dẫn bảo toàn tùy chỉnh. |
| Examples/evidence | Ví dụ ghi rõ là minh họa; template mặc định NOT_RUN; secret chỉ placeholder. | Mẫu không có số đo giả hoặc credential thật. |
| Handoff | Kết nối artifact, version, limitations, owner và troubleshooting. | Link tồn tại, phạm vi đã test và câu hỏi còn mở. |

## Hợp đồng đầu ra khi bàn giao

- Docs diff: đối tượng đọc, mục tiêu và điều thay đổi.
- Verification: commands, links và môi trường đã thử.
- Handoff notes: prerequisites, migration, limitations và owner.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Không có thông tin để khẳng định behavior; giữ unknown hoặc hỏi owner, không bịa chức năng để hoàn tất tài liệu. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
