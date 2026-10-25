# Đánh giá hành vi skill

Có 31 scenario khai báo: mỗi vai trò ít nhất một ca, cùng ca âm và áp lực về quyền, evidence, loop và scope. Chúng là định nghĩa kiểm định, không phải kết quả đã pass.

## Phân biệt ba lớp

1. `./setup.sh validate`: tên, metadata, catalog, link và hình dạng scenario hợp lệ.
2. Unit tests: CLI thực thi đúng invariant filesystem trong môi trường tạm.
3. Behavioral evaluation: host/model thực tế chọn vai trò và hành xử đúng trước một request cụ thể.

Hai lớp đầu không thay lớp thứ ba. Trạng thái scenario trong repo mặc định NOT_RUN. Không có API evaluator hoặc model runner ẩn trong CLI.

## Cách chạy một ca

1. Chọn ca từ [scenarios.json](scenarios.json), ghi commit/dirty state và chuẩn bị raw artifact cần cho request trong workspace tạm. Không dùng secret hoặc production data.
2. Xác lập quyền: chỉ đọc, sửa local hay test ở đâu; không cấp mutation ngoài phạm vi scenario.
3. Dùng host có skill cài đúng; ghi host/version/model khi host công bố. Để kiểm routing, không nhắc tên skill; để kiểm behavior, gọi skill rõ tên. Ghi rõ chế độ đang thử.
4. Nếu so baseline, dùng cùng request, artifact, quyền và môi trường trên bản trước và bản mới. Không đưa sẵn đáp án mong muốn cho model đang đánh giá.
5. Quan sát hành động, file diff, tool calls và kết luận; đối chiếu expected_observations và fail_if. Lưu transcript đã che dữ liệu nhạy cảm và evidence.
6. Điền một bản [result-template.json](result-template.json) riêng cho mỗi run. PASS cần có bằng chứng, FAIL cần trigger, BLOCKED nêu điều kiện thiếu. Không sửa scenario để khớp output vừa nhận.

## Review kết quả

Ưu tiên reviewer khác người viết khi có điều kiện và được phép. Cùng một người tự làm vẫn có giá trị, nhưng phải ghi self-evaluation. Tăng số lần chạy cho vùng có độ biến động đáng kể; báo số mẫu thật, không ngoại suy thành bảo đảm tuyệt đối.

Các ca âm phải kiểm việc skill không kéo một yêu cầu đơn giản vào quy trình nặng. Các ca chồng vai trò kiểm được người nhận trách nhiệm chính, không chỉ có nhắc tên tất cả vai trò.

## Baseline của v2

Behavioral eval trên model/host độc lập chưa chạy trong quá trình kiểm thử script nếu [báo cáo kiểm chứng](../docs/verification.md) không ghi kết quả tương ứng. Không công bố điểm cải thiện so với v1 khi chưa có baseline cùng điều kiện.
