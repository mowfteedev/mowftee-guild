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

## Đầu ra cần giữ khi liên quan

- Skill design: intent, boundary, inputs, outputs và stop conditions.
- Validation report: static/script/behavioral tách riêng.
- Migration/provenance: thay đổi trigger, tài nguyên, license và nguồn.

## Điều kiện dừng phần phụ thuộc

Thiếu dữ kiện làm thay đổi phạm vi skill hoặc nguồn tái sử dụng chưa rõ license thì giữ phần đó để làm rõ. Nếu chưa có môi trường thử hành vi, vẫn chỉnh và kiểm cấu trúc phần độc lập; ghi chưa chạy đánh giá hành vi. Không coi thiếu bước đánh giá tùy chọn là lý do dừng toàn bộ việc chỉnh Markdown.

## Ví dụ đánh giá chiều sâu mà không tăng thủ tục

Một skill “database” chỉ nói “thiết kế schema tốt, tối ưu index, viết test” chưa thay đổi đáng kể quyết định của trợ lý. Một hướng dẫn hữu ích hơn là chỉ ra cách gắn index với workload, xem chi phí ghi và không coi seq scan trên bảng nhỏ là lỗi mặc định.

Kiểm từng đoạn bằng câu hỏi: bỏ đoạn này đi thì trợ lý có dễ chọn sai trong tình huống nào? Nếu không trả lời được, cân nhắc bỏ hoặc rút ngắn. Độ dài và số heading không thay cho giá trị chuyên môn.

| Vấn đề quan sát | Cách sửa phù hợp |
| --- | --- |
| Hai description đều hút mọi việc API | Tách thiết kế contract và triển khai hành vi; cho ví dụ trigger của mỗi bên. |
| Runbook lặp entrypoint | Giữ nguyên tắc ở entrypoint, chuyển reference thành ví dụ quyết định hoặc ca chẩn đoán. |
| Thiếu hướng dẫn khi có hai phương án đều hợp lệ | Thêm điều kiện chọn, đánh đổi và dữ kiện cần xem; không chốt một stack chung. |
| Có nhiều dòng về báo cáo hơn chuyên môn | Thu gọn quy tắc chung; giữ đầu ra theo quy mô tác vụ. |

Thử routing bằng yêu cầu như “thiết kế request/response cập nhật hồ sơ” và “sửa xử lý cập nhật hồ sơ đang bỏ qua null”. Sau đó thử một yêu cầu không thuộc skill để xem description có quá rộng không. Đọc file và dự đoán routing chỉ là tự đánh giá nội dung; chỉ gọi là thử hành vi khi đã thực thi request trên host và quan sát kết quả.

Mỗi skill giữ được hướng dẫn độc lập sau khi chép. Repo này dùng một LICENSE gốc, script mang bản đó theo lúc cài; không tạo cơ chế kế thừa instruction hoặc yêu cầu tải toàn bộ guild cho một đầu việc.
