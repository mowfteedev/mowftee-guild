# Bảo trì, tối ưu và audit

Xử lý nợ kỹ thuật hoặc rủi ro theo mức ưu tiên có bằng chứng, bảo toàn nghiệp vụ đã chốt.

**Mức rủi ro:** R1; R2 khi thay dữ liệu/quyền, R3 khi tác động vận hành.

## Cách dùng

Đối chiếu [protocol](../docs/protocol.md) và [risk/evidence](../docs/risk-and-evidence.md). Bảng dưới là phân công, không tự tạo agent hay cấp quyền tool. Với việc nhỏ, gộp cổng phù hợp và ghi lý do; với R2/R3 giữ điều kiện kiểm định độc lập. Khi READ-ONLY, trả kết quả trong hội thoại và không ghi memory.

## Ma trận trách nhiệm

| Cổng | Thực thi | Phản biện | Kiểm định / tiếp nhận |
| --- | --- | --- | --- |
| 1. Khảo sát và ưu tiên | tech-lead | security, dependency-auditor, database, performance theo scope | code-reviewer |
| 2. Khắc phục có kiểm soát | refactoring-specialist hoặc owner phù hợp | backend, frontend, migration-specialist | code-reviewer |
| 3. Kiểm lại và đo | tester, test-automator | performance, sre khi cần | Reviewer độc lập cho R2 |
| 4. Ghi nhận và bàn giao | doc-writer | tech-lead | Owner tiếp nhận |

## Cổng 1: Khảo sát và ưu tiên

**Đầu vào:** Phạm vi audit và dữ liệu quan sát được.

**Thực hiện:** Lập findings có trigger, tác động và nguồn; phân biệt lỗi với hardening hoặc sở thích.

**Điều kiện bàn giao:** Danh sách ưu tiên có owner và cách kiểm chứng.

**Nếu không đạt:** Không dùng mọi code smell làm blocker hoặc kết luận CVE không có điều kiện khai thác.

## Cổng 2: Khắc phục có kiểm soát

**Đầu vào:** Finding và baseline.

**Thực hiện:** Thay đổi nhỏ theo từng mục tiêu; tách bugfix, dependency upgrade và tối ưu nếu semantics khác.

**Điều kiện bàn giao:** Diff giải quyết finding và giữ phần nghiệp vụ ngoài scope.

**Nếu không đạt:** Đổi hành vi chưa chấp thuận phải được tách và chốt lại.

## Cổng 3: Kiểm lại và đo

**Đầu vào:** Snapshot sau sửa, dữ liệu và workload đại diện.

**Thực hiện:** Kiểm lại finding, regression và so trước/sau trong điều kiện tương đương.

**Điều kiện bàn giao:** Evidence chứng minh đúng mục tiêu; lỗi, timeout và giới hạn được ghi.

**Nếu không đạt:** Không ngoại suy load nhỏ thành sức chịu tải lớn hoặc gọi scanner lỗi là sạch.

## Cổng 4: Ghi nhận và bàn giao

**Đầu vào:** Kết quả đo và quyết định còn mở.

**Thực hiện:** Cập nhật risk/debt ledger, giữ lịch sử mục đã xử lý và kế hoạch phần còn lại.

**Điều kiện bàn giao:** Mỗi mục đóng có evidence; mục mở có owner và điều kiện xem lại.

**Nếu không đạt:** Không xóa dấu vết nợ cũ chỉ để báo đã sạch hoàn toàn.

## Evidence và vòng sửa

Mỗi tiêu chí cần snapshot, lệnh/thao tác, môi trường, kết quả thật và giới hạn. Trạng thái khởi đầu NOT_RUN; FAIL khác BLOCKED. Reviewer không tự ký thay người dùng hoặc thay quyền external action. Tối đa ba vòng sửa cùng tiêu chí, hai vòng không tiến bộ thì báo owner và hướng giải quyết.

Dùng mẫu [requirements](../templates/memory/requirements-template.md), [gate](../templates/memory/gate-checklist-template.md), [evidence](../templates/memory/test-evidence-template.md) hoặc [handoff](../templates/memory/handoff-template.md) khi cần lưu và được phép. Không tạo đầy đủ hồ sơ cho tác vụ nhỏ chỉ để đủ hình thức.

## Prompt khởi đầu

```text
Dùng tech-lead khoanh phạm vi bảo trì, chọn refactoring-specialist, dependency-auditor, security hoặc performance theo vấn đề thật. Bắt đầu bằng khảo sát và baseline.
```

## Kết thúc đúng phạm vi

Báo phần đã làm, bằng chứng, phần chưa chạy, người nhận và bước tiếp theo. Không gọi sản phẩm production-ready, zero-regression hay an toàn tuyệt đối từ quy trình này.
