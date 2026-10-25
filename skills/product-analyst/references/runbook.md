# Runbook: Phân tích yêu cầu

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Đề bài mơ hồ về màu sắc: ghi lựa chọn có thể đảo ngược, không chặn toàn bộ.
2. Checkout thiếu quy tắc hoàn tiền: đánh dấu câu hỏi nghiệp vụ quan trọng.
3. Tính năng chỉ dành cho admin: có AC cho người dùng thường bị từ chối.
4. Người dùng yêu cầu bỏ một phần: cập nhật AC, không âm thầm giữ scope cũ.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Tiêu chí mơ hồ | Đổi nhanh/đẹp/ổn định thành hành vi quan sát hoặc chỉ số có cách đo đã thống nhất. | AC có tiền đề, hành động và kết quả. |
| Quyền người dùng | Lập ma trận subject/action/resource, gồm từ chối quyền. | Ví dụ người dùng hợp lệ và không hợp lệ cho cùng tài nguyên. |
| Hành vi tiền tệ | Chốt đơn vị, precision, quy tắc làm tròn, hủy và hoàn trả với owner nghiệp vụ. | Ví dụ số cụ thể đã xác nhận, không tự suy đoán. |
| Tính năng kéo thêm scope | Tách bắt buộc, tùy chọn và ngoài phạm vi; ghi tác động deadline hoặc dependency. | Scope diff và quyết định người có thẩm quyền. |
| AC thay đổi sau triển khai | Đánh giá lại phần code/test/docs bị ảnh hưởng; không sửa AC để hợp thức lỗi. | Lịch sử AC và lý do thay đổi. |

## Hợp đồng đầu ra khi bàn giao

- Spec: người dùng, vấn đề, phạm vi và AC.
- Business rules: quyền, trạng thái, rounding/timezone khi có.
- Open questions: tác động, owner và phần có thể tiếp tục.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Thiếu quy tắc làm thay đổi kết quả nghiệp vụ quan trọng; các bên chưa thống nhất AC bắt buộc. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
