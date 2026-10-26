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

## Đầu ra cần giữ khi liên quan

- Docs diff: đối tượng đọc, mục tiêu và điều thay đổi.
- Verification: commands, links và môi trường đã thử.
- Handoff notes: prerequisites, migration, limitations và owner.

## Điều kiện dừng phần phụ thuộc

Không có thông tin để khẳng định behavior; giữ unknown hoặc hỏi owner, không bịa chức năng để hoàn tất tài liệu. Tiếp tục phần độc lập; nêu rõ điểm bị chặn.

## Ví dụ sửa quickstart khi CLI đã đổi

Giả sử README còn lệnh `tool init --profile personal`, nhưng CLI hiện chỉ có `tool install codex`. Đây là ví dụ về drift tài liệu, không phải lệnh để chạy trong repo này.

1. Đọc entrypoint/help và test để xác định option, default và side effect thật. Tìm các lệnh cũ trong README, docs và ví dụ bằng tìm kiếm toàn repo.
2. Viết lại một đường đi tối thiểu từ bản clone sạch, với prerequisite và working directory rõ. Không giữ option đã bỏ dưới dạng “cách khác” nếu CLI không hỗ trợ.
3. Chạy trong môi trường tạm với HOME/đích thử khi có thao tác cài/gỡ; kiểm file tạo ra và dữ liệu được giữ, không chỉ exit code.
4. Viết phần cập nhật/gỡ theo cùng cơ chế hiện tại và nêu bản tùy chỉnh nào có thể bị thay thế. Kiểm link sau khi đổi tên hoặc xóa file.

Đầu ra mong đợi trong hướng dẫn là mô tả hành vi; transcript thực chỉ ghi môi trường đã chạy. Nếu chưa thử trên một host, đừng chép kết quả từ host khác sang.

Một tài liệu dễ dùng cần trả lời được: cần gì trước khi chạy, chạy ở đâu, kết quả nằm ở đâu, kiểm thành công thế nào, lỗi thường gặp xử lý ra sao. Không cần thêm manual cho mỗi skill nếu entrypoint và reference đã đủ.
