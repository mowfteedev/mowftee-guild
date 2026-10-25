# Runbook: Kiểm toán phụ thuộc

## Ma trận kiểm chứng theo tình huống

Các tình huống dưới đây là gợi ý kiểm chứng, không phải yêu cầu chạy tất cả cho mọi thay đổi.

1. Advisory chỉ ảnh hưởng feature chưa bật: ghi điều kiện và bằng chứng.
2. Không có lockfile: công bố giới hạn tái lập.
3. Repo có nhiều loại license: ghi từng phần liên quan.
4. Scanner trả exit nonzero: phân biệt phát hiện lỗ hổng với lỗi mạng hoặc công cụ.

## Ma trận quyết định chuyên môn

| Tình huống | Cách quyết định | Evidence cần tìm hoặc tạo |
| --- | --- | --- |
| Inventory | Dùng manifest + lockfile + runtime thực; tách trực tiếp/bắc cầu/build-only. | Package, resolved version, source và dependency path. |
| Advisory | Đọc advisory upstream/OSV/NVD phù hợp, ghi khoảng phiên bản và ngày đối chiếu. | URL, advisory ID và phần phiên bản thực tế bị ảnh hưởng. |
| Reachability | Đánh giá feature, cấu hình và môi trường cần cho khai thác; không tự hạ severity thiếu bằng chứng. | Call/config path và residual risk. |
| Upgrade | Chọn thay đổi nhỏ, đọc release notes, cập nhật lockfile bằng package manager chuẩn. | Before/after versions, runtime compatibility và tests. |
| Provenance/license | Đọc license file và nguồn từng phần được dùng; badge tổng hợp không đủ. | File nguồn, commit, license text reference và attribution cần giữ. |

## Hợp đồng đầu ra khi bàn giao

- Inventory: package, version, source, dependency chain.
- Assessment: advisory, reachability, priority và quyết định.
- Upgrade/exception plan: owner, kiểm thử, lý do và ngày xem lại.

Hồ sơ đủ lớn để lưu cần snapshot/commit hoặc dirty state, môi trường, command/thao tác, exit code khi có và artifact đã che dữ liệu nhạy cảm. Với việc nhỏ, hội thoại có thể đủ; không tự tạo hồ sơ ngoài quyền ghi.

## Điều kiện dừng phần phụ thuộc

Không kết nối advisory source hoặc thiếu lockfile; ghi giới hạn thay vì tuyên bố không có rủi ro. Vẫn tiếp tục phần độc lập được phép. Ghi NOT_RUN/BLOCKED và owner bước tiếp theo, không tự đổi thành PASS.

## Kiểm tra lại sau sửa

Kiểm lại tiêu chí lỗi và regression trong vùng ảnh hưởng. Khi snapshot, dữ liệu hoặc cấu hình tác động kết luận thay đổi, đánh giá lại evidence cũ. Tối đa ba vòng cùng tiêu chí; hai vòng không tiến bộ thì báo điểm nghẽn cùng hướng xử lý, giữ nguyên AC bắt buộc.
