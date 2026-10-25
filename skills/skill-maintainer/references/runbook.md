# Runbook: Bảo trì và đánh giá skill

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. User nói READ-ONLY: skill không được buộc ghi memory.
2. Tool host thiếu: mô tả fallback thật, không bịa lời gọi tool.
3. Hai skill luôn cùng trigger: thu hẹp scope hoặc gộp.
4. Behavioral eval chưa chạy: giữ NOT_RUN dù lint đã xanh.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Routing | Dùng trigger cụ thể và ranh giới với skill gần nhất; giữ description ngắn, phân biệt. | Ca dương/âm/chồng vai trò và expected primary owner. |
| Instruction quality | Giữ core decision rules trong entrypoint, conditional detail trong reference. | Payload tự chứa, không bắt đọc toàn bộ thư viện mỗi task. |
| Permissions/capability | Skill không cấp quyền mới; công cụ host phải thật và có fallback. | Ca READ-ONLY, missing tool và deferred plugin. |
| Static checks | Kiểm frontmatter, tên thư mục và link, chưa kết luận agent behavior. | Command, exit code và danh sách validator đã chạy. |
| Behavioral checks | Chạy request trên host/model với artifact tối thiểu và không lộ expected answer. | Transcript, actual actions, independent/self-review và limitations. |

## Hợp đồng đầu ra khi bàn giao

- Skill design: intent, boundary, inputs, outputs và stop conditions.
- Validation report: static/script/behavioral tách riêng.
- Migration/provenance: thay đổi trigger, tài nguyên, license và nguồn.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Chưa có quyền cài/kích hoạt plugin, không thể đánh giá hành vi trong môi trường hiện tại hoặc nguồn tái sử dụng chưa rõ license. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Nếu không tiến bộ, đổi cách tiếp cận và báo rõ điểm nghẽn; không bỏ yêu cầu để làm đẹp kết quả.
