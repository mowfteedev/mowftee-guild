# Cải thiện và đánh giá skill

Làm hướng dẫn chính xác và phân biệt vai trò tốt hơn, không tích lũy prompt dài thiếu bằng chứng.

**Mức rủi ro:** R1; installer có invariant filesystem cần regression tests.

## Cách dùng

Đối chiếu [protocol](../docs/protocol.md) và [risk/evidence](../docs/risk-and-evidence.md). Bảng dưới là phân công, không tự tạo agent hay cấp quyền tool. Với việc nhỏ, gộp cổng phù hợp và ghi lý do; với R2/R3 giữ điều kiện kiểm định độc lập. Khi READ-ONLY, trả kết quả trong hội thoại và không ghi memory.

## Ma trận trách nhiệm

| Cổng | Thực thi | Phản biện | Kiểm định / tiếp nhận |
| --- | --- | --- | --- |
| 1. Chốt vấn đề | skill-maintainer | tech-lead, doc-writer | tester |
| 2. Viết và đồng bộ | skill-maintainer | Owner chuyên môn | code-reviewer |
| 3. Kiểm định | test-automator, tester | skill-maintainer | Reviewer độc lập nếu yêu cầu |
| 4. Bàn giao để duyệt | doc-writer, release-manager | tech-lead | Người dùng |

## Cổng 1: Chốt vấn đề

**Đầu vào:** Lỗi routing hoặc hành vi quan sát được.

**Thực hiện:** Thu ví dụ thật, xác định trigger/đầu ra và quyết định sửa, tách hoặc gộp.

**Điều kiện bàn giao:** Có lý do rõ cho thay đổi và ca âm tránh chồng vai trò.

**Nếu không đạt:** Không thêm skill chỉ để tăng số lượng hoặc áp một persona chung.

## Cổng 2: Viết và đồng bộ

**Đầu vào:** Use case và phạm vi.

**Thực hiện:** Viết entrypoint, runbook tự chứa, UI metadata, catalog/profile và tài liệu.

**Điều kiện bàn giao:** Link và metadata nhất quán, không tool giả hoặc quyền tự cấp.

**Nếu không đạt:** Không sao chép nguyên nội dung nguồn có license chưa đối chiếu.

## Cổng 3: Kiểm định

**Đầu vào:** Diff, source tests và scenarios.

**Thực hiện:** Chạy validate, tests script và scenario trên host khi có điều kiện; tách hai kết quả.

**Điều kiện bàn giao:** Static checks có output thật; behavioral chưa chạy được giữ NOT_RUN.

**Nếu không đạt:** Không biến grep/heading check thành chứng minh hành vi AI.

## Cổng 4: Bàn giao để duyệt

**Đầu vào:** Evidence và scope cuối.

**Thực hiện:** Viết migration/changelog, push nhánh khi được phép và đưa danh sách vai trò.

**Điều kiện bàn giao:** Người dùng xem được bản thay đổi và giới hạn; plugin còn chờ duyệt nếu được yêu cầu.

**Nếu không đạt:** Không tự merge main hoặc làm MCP trong phần đã giới hạn.

## Evidence và vòng sửa

Mỗi tiêu chí cần snapshot, lệnh/thao tác, môi trường, kết quả thật và giới hạn. Trạng thái khởi đầu NOT_RUN; FAIL khác BLOCKED. Reviewer không tự ký thay người dùng hoặc thay quyền external action. Tối đa ba vòng sửa cùng tiêu chí, hai vòng không tiến bộ thì báo owner và hướng giải quyết.

Dùng mẫu [requirements](../templates/memory/requirements-template.md), [gate](../templates/memory/gate-checklist-template.md), [evidence](../templates/memory/test-evidence-template.md) hoặc [handoff](../templates/memory/handoff-template.md) khi cần lưu và được phép. Không tạo đầy đủ hồ sơ cho tác vụ nhỏ chỉ để đủ hình thức.

## Prompt khởi đầu

```text
Dùng skill-maintainer chốt use case, phân biệt với vai trò cũ và thêm scenario kiểm định. Giữ yêu cầu người dùng ưu tiên; plugin/MCP là bước riêng được duyệt.
```

## Kết thúc đúng phạm vi

Báo phần đã làm, bằng chứng, phần chưa chạy, người nhận và bước tiếp theo. Không gọi sản phẩm production-ready, zero-regression hay an toàn tuyệt đối từ quy trình này.
