# Sửa lỗi từ tái hiện đến kiểm chứng

Khắc phục nguyên nhân có bằng chứng trong phạm vi nhỏ nhất và tránh regression liên quan.

**Mức rủi ro:** Chọn theo hậu quả thực tế của lỗi.

## Cách dùng

Đối chiếu [protocol](../docs/protocol.md) và [risk/evidence](../docs/risk-and-evidence.md). Bảng dưới là phân công, không tự tạo agent hay cấp quyền tool. Với việc nhỏ, gộp cổng phù hợp và ghi lý do; với R2/R3 giữ điều kiện kiểm định độc lập. Khi READ-ONLY, trả kết quả trong hội thoại và không ghi memory.

## Ma trận trách nhiệm

| Cổng | Thực thi | Phản biện | Kiểm định / tiếp nhận |
| --- | --- | --- | --- |
| 1. Tái hiện | Owner module | test-automator | tester |
| 2. Sửa nguyên nhân | Owner module | software-architect nếu boundary liên quan | code-reviewer |
| 3. Kiểm chứng | test-automator, tester | security hoặc performance theo tác động | Reviewer độc lập khi R2 |
| 4. Bàn giao | Owner module, doc-writer | tech-lead | Người tiếp nhận |

## Cổng 1: Tái hiện

**Đầu vào:** Bug report, snapshot, dữ liệu và môi trường.

**Thực hiện:** Ghi bước tái hiện và kiểm tra hành vi trên baseline; phân biệt giả thuyết và quan sát.

**Điều kiện bàn giao:** Có ca lỗi hoặc giới hạn tái hiện rõ ràng.

**Nếu không đạt:** Thiếu production access không cho phép tự lấy dữ liệu thật.

## Cổng 2: Sửa nguyên nhân

**Đầu vào:** Invariant và ca lỗi.

**Thực hiện:** Sửa nhỏ nhất, giữ contract và lỗi ngoài phạm vi; thêm regression test khi có giá trị.

**Điều kiện bàn giao:** Nguyên nhân được giải thích, không chỉ che triệu chứng.

**Nếu không đạt:** Không thêm silent catch, global overflow hoặc retry vô hạn để che lỗi.

## Cổng 3: Kiểm chứng

**Đầu vào:** Bản sửa và baseline.

**Thực hiện:** Chạy ca tái hiện, regression vùng ảnh hưởng và các nhánh phục hồi quan trọng.

**Điều kiện bàn giao:** Bug không còn tái hiện trong điều kiện đã chọn; evidence khớp snapshot.

**Nếu không đạt:** Ca chưa chạy giữ NOT_RUN/BLOCKED; không tự báo đã fix trên môi trường chưa thử.

## Cổng 4: Bàn giao

**Đầu vào:** Diff và evidence.

**Thực hiện:** Tóm tắt trigger, thay đổi, tests, giới hạn và bước phát hành nếu được yêu cầu.

**Điều kiện bàn giao:** Người dùng có bản reviewable và kết luận có phạm vi.

**Nếu không đạt:** Không tự merge/deploy khi người dùng chỉ yêu cầu sửa local.

## Evidence và vòng sửa

Mỗi tiêu chí cần snapshot, lệnh/thao tác, môi trường, kết quả thật và giới hạn. Trạng thái khởi đầu NOT_RUN; FAIL khác BLOCKED. Reviewer không tự ký thay người dùng hoặc thay quyền external action. Tối đa ba vòng sửa cùng tiêu chí, hai vòng không tiến bộ thì báo owner và hướng giải quyết.

Dùng mẫu [requirements](../templates/memory/requirements-template.md), [gate](../templates/memory/gate-checklist-template.md), [evidence](../templates/memory/test-evidence-template.md) hoặc [handoff](../templates/memory/handoff-template.md) khi cần lưu và được phép. Không tạo đầy đủ hồ sơ cho tác vụ nhỏ chỉ để đủ hình thức.

## Prompt khởi đầu

```text
Dùng owner frontend hoặc backend tái hiện lỗi và chốt expected/actual trước khi sửa. Đọc callers và tests; không triển khai tính năng khác trong cùng diff.
```

## Kết thúc đúng phạm vi

Báo phần đã làm, bằng chứng, phần chưa chạy, người nhận và bước tiếp theo. Không gọi sản phẩm production-ready, zero-regression hay an toàn tuyệt đối từ quy trình này.
