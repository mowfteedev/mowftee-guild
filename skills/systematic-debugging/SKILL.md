---
name: systematic-debugging
description: "Điều tra và sửa lỗi hành vi, crash hoặc test thất bại: tái hiện, xác minh nguyên nhân trước khi sửa, kiểm cùng ca trước/sau và hồi quy. Không dùng cho thêm tính năng hoặc refactor thuần túy."
license: MIT
---

# Sửa lỗi theo nguyên nhân có bằng chứng

Đi từ triệu chứng tới cơ chế gây lỗi, sửa trong phạm vi nhỏ nhất và kiểm chứng kết quả. Áp dụng cho lỗi ở bất kỳ tầng nào của dự án; dùng kiến thức chuyên môn của tầng đó khi cần.

## Nguyên tắc làm việc

- Đọc yêu cầu, trạng thái code và cách chạy trước khi hỏi. Giữ quyền đã thống nhất; READ-ONLY chỉ điều tra và trả kết quả. Skill không cấp quyền thao tác dịch vụ hoặc production.
- Được đặt giả thuyết, nhưng phải phân biệt với dữ kiện. Khi chưa có căn cứ cho nguyên nhân, tiếp tục điều tra thay vì sửa theo cảm giác.
- Không tuyên bố đã tái hiện, đã chạy test hoặc đã fix nếu chưa có kết quả tương ứng. Không lấy việc sửa xong một đoạn code làm bằng chứng lỗi đã hết.

## 1. Tái hiện trước khi sửa

Xác định input, trigger, expected/actual, phiên bản và môi trường. Chọn test, script hoặc thao tác nhỏ nhất còn thể hiện lỗi; chạy trên bản lỗi trước khi đổi logic và giữ output quan trọng.

Một test đỏ phải thất bại vì hành vi cần sửa. Lỗi runner, import, fixture hoặc môi trường chưa đủ điều kiện không được tính là tái hiện lỗi đó. Giữ nguyên thay đổi hiện có của người dùng.

Nếu không tái hiện được, ghi các cách đã thử và dữ kiện còn thiếu. Có thể tiếp tục điều tra log/trace hoặc đường thực thi, nhưng phải giữ giới hạn này trong kết luận.

## 2. Xác minh nguyên nhân

Theo đầu vào qua các ranh giới tới điểm sai; đọc caller, trạng thái và dữ liệu liên quan. Nêu giả thuyết và chọn quan sát có thể phân biệt nó với cách giải thích khác.

Liên hệ rõ: trigger → đường thực thi → điều kiện sai → triệu chứng. Phân biệt điều suy ra từ code với điều đã chạy và quan sát. Chưa có căn cứ thì chưa sửa theo giả thuyết; nếu giả thuyết bị bác, đổi hướng điều tra.

## 3. Sửa tối thiểu, kiểm lại cùng ca

Sửa cơ chế gây lỗi trong phạm vi đã được phép. Không gộp refactor, đổi stack hoặc nâng dependency không liên quan vào bản vá.

Chạy lại ca ban đầu trên bản sửa, giữ kỳ vọng và điều kiện có thể so sánh. Không bỏ assertion, nuốt lỗi, tăng retry tùy tiện hoặc mock chính đối tượng đang kiểm để tạo PASS. Nếu test không bắt được bản lỗi, nó chưa chứng minh được hồi quy này.

## 4. Kiểm hồi quy trong vùng ảnh hưởng

Chọn các caller, luồng hợp lệ, nhánh lỗi và trường hợp biên bị bản sửa tác động. Chạy mức kiểm tra đủ quan sát hành vi; test tự động mới chỉ cần khi có giá trị bảo vệ lâu dài.

Đối chiếu dữ liệu và side effect quan trọng, không chỉ exit code hoặc thông báo thành công. Phân biệt lỗi baseline với lỗi mới bằng bằng chứng; nêu phần chưa chạy, flaky hoặc môi trường bị chặn.

## Điều kiện bàn giao

Trả ngắn trong hội thoại: nguyên nhân và căn cứ; thay đổi; ca trước/sau; hồi quy đã thử; giới hạn. Với mỗi kết quả cần command/thao tác, phiên bản hoặc artifact, môi trường và output quan trọng đã che secret; lệnh có exit code, CI có link đúng snapshot.

Bằng chứng phải còn khớp với code, cấu hình, dữ liệu và môi trường liên quan. Khi những phần đó đổi theo cách có thể ảnh hưởng kết quả, kiểm lại phần tương ứng. Không cần chạy lại chỉ vì sang lượt chat mới.

Nếu chưa tái hiện lỗi ban đầu hoặc chưa kiểm được bản sửa, mô tả đúng phần đã làm và phần chưa xác minh. Không kết luận lỗi ban đầu đã được chứng minh sửa xong từ một ca giả lập hoặc chỉ đọc code.

## Khi việc điều tra không đi thẳng

Đọc [runbook](references/runbook.md) khi ca tái hiện xanh trên bản lỗi, test lỗi vì môi trường, lỗi chập chờn, thiếu baseline hoặc cần đối chiếu bằng chứng CI.
