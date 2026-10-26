# Cải thiện và đánh giá skill

Làm hướng dẫn chính xác và phân biệt vai trò tốt hơn, không tích lũy prompt dài thiếu bằng chứng.

Chọn vấn đề cụ thể từ việc dùng thật hoặc đọc lại hướng dẫn: chọn nhầm vai trò, thiếu cách ra quyết định, quy tắc quá rộng hoặc thông tin đã lỗi thời.

## Gợi ý thực hiện

1. Thu ví dụ thật, xác định trigger/đầu ra và quyết định sửa, tách hoặc gộp.
2. Sửa SKILL.md và runbook đi kèm; nếu thêm vai trò thì cập nhật danh sách đọc cho người dùng.
3. Rà cả ca đúng và ca quy tắc có thể loại nhầm; kiểm frontmatter, tên và link. Thử hành vi trên host khi có điều kiện; sửa script thì kiểm cài/gỡ trong thư mục tạm.
4. Cập nhật hướng dẫn theo thay đổi thực tế. Ghi migration khi có đổi cách dùng, changelog khi cần giữ lịch sử; push khi đã được phép.

## Kiểm tra và kết thúc

Phân biệt đọc lại nội dung, kiểm định dạng, kiểm script và quan sát hành vi của trợ lý. Chỉ báo đã thử hành vi khi có yêu cầu thực thi cùng kết quả quan sát; không dùng CI cài/gỡ làm bằng chứng agent sẽ làm đúng quy trình.

[Chọn workflow khác](README.md) · [Skill skill-maintainer](../skills/skill-maintainer/SKILL.md)
