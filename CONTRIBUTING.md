# Đóng góp cho mowftee-guild

## Trước khi sửa

Đọc [phân công vai trò](docs/skills-catalog.md), [quy tắc phối hợp](docs/protocol.md) và [thiết kế repo](docs/repository-design.md). Giữ yêu cầu người dùng và scope rõ ràng; công việc góp mã không tự cho phép cài skill global, liên hệ bên ngoài, merge hoặc deploy.

## Thêm hoặc tách skill

1. Chứng minh có use case và đầu ra khác vai trò hiện tại. Không tăng số skill chỉ vì có thêm tên chuyên gia.
2. Tạo entrypoint với tên lowercase-hyphen khớp thư mục, description ngắn và phân biệt; dùng `name`, `description`, `license` theo subset validator hỗ trợ.
3. Ghi đầu vào, boundary, workflow, evidence, điều kiện dừng, đầu ra. Bổ sung runbook cho tình huống thực sự cần; link chỉ trong cùng payload.
4. Thêm metadata UI có quote và default prompt chứa `$skill-name`. Giữ automatic invocation mặc định; không tự thêm MCP dependency.
5. Đồng bộ `catalog.json`, profiles cần thiết, danh mục người dùng và VERSION khi thay phiên bản. Mỗi skill có `LICENSE.txt` khớp license root.
6. Thêm scenario dương, âm hoặc áp lực liên quan. Không coi kiểm tra heading là behavioral eval.

## Kiểm tra trước khi gửi

```bash
./setup.sh validate
bash -n setup.sh
python3 -m unittest discover -s tests -v
```

Khi thay installer, kiểm thao tác trên thư mục tạm và failure paths: collision, modified files, dry-run, backup, rollback, manifest traversal và symlink. Không chạy test bằng HOME thật. Không thêm dependency runtime chỉ để parse dữ liệu tĩnh mà có thể thể hiện an toàn bằng format đơn giản hơn.

## Quy tắc review

Mô tả vấn đề, kết quả sau thay đổi và kiểm chứng thật. Ghi rõ behavioral eval hoặc host test chưa chạy. Không tự điền thành tích vào mẫu evidence. Giữ attribution khi dùng nguồn ngoài và kiểm license từng phần; thư mục tham khảo Desktop không được commit vào repo.

Thay đổi lớn nên gửi nhánh/PR có diff và tài liệu tương ứng. Main chỉ được merge theo quyền người dùng đã cấp. Xem [workflow cải thiện skill](workflows/07-cai-tien-skill.md).
