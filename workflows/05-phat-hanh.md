# Phát hành có kiểm soát

Đảm bảo đúng artifact, đúng quyền và có tín hiệu dừng hoặc phục hồi khi phát hành.

**Mức rủi ro:** R3 nếu tác động hệ thống vận hành; push nhánh review chỉ theo scope được yêu cầu.

## Cách dùng

Đối chiếu [protocol](../docs/protocol.md) và [risk/evidence](../docs/risk-and-evidence.md). Bảng dưới là phân công, không tự tạo agent hay cấp quyền tool. Với việc nhỏ, gộp cổng phù hợp và ghi lý do; với R2/R3 giữ điều kiện kiểm định độc lập. Khi READ-ONLY, trả kết quả trong hội thoại và không ghi memory.

## Ma trận trách nhiệm

| Cổng | Thực thi | Phản biện | Kiểm định / tiếp nhận |
| --- | --- | --- | --- |
| 1. Chốt release scope | release-manager | product-analyst, doc-writer | tester |
| 2. Sẵn sàng vận hành | devops, migration-specialist khi cần | sre, security | release-manager |
| 3. Thực hiện action | release-manager hoặc owner hạ tầng | devops | Người có thẩm quyền theo yêu cầu |
| 4. Xác minh và bàn giao | sre, doc-writer | devops | release-manager |

## Cổng 1: Chốt release scope

**Đầu vào:** Yêu cầu phát hành và snapshot.

**Thực hiện:** Đối chiếu AC, artifact, thay đổi kể từ evidence và giới hạn được chấp nhận.

**Điều kiện bàn giao:** Phạm vi và phiên bản xác định, không thiếu check bắt buộc.

**Nếu không đạt:** Evidence stale cần đánh giá lại trước kết luận.

## Cổng 2: Sẵn sàng vận hành

**Đầu vào:** Artifact và môi trường được phép.

**Thực hiện:** Kiểm prerequisites, ordering, feature flags, migration và khả năng rollback hoặc roll-forward.

**Điều kiện bàn giao:** Có runbook, health signals, điểm dừng và owner.

**Nếu không đạt:** Không giả định rollback app tự hoàn tác dữ liệu.

## Cổng 3: Thực hiện action

**Đầu vào:** Quyền đã có, đúng commit và check.

**Thực hiện:** Thực hiện đúng phần được cho phép, ghi URL/SHA/id; không force-push hoặc mở rộng môi trường.

**Điều kiện bàn giao:** External state khớp action yêu cầu.

**Nếu không đạt:** Thất bại phải báo kết quả thật và cách mở chặn, không giả vờ đã push/deploy.

## Cổng 4: Xác minh và bàn giao

**Đầu vào:** Kết quả thực tế sau action.

**Thực hiện:** Kiểm remote SHA hoặc tín hiệu runtime tương ứng, cập nhật docs/notes và owner.

**Điều kiện bàn giao:** Người nhận có link, phiên bản và trạng thái chính xác.

**Nếu không đạt:** CI hoặc smoke pending vẫn pending; production chưa kiểm không được gọi đã khỏe.

## Evidence và vòng sửa

Mỗi tiêu chí cần snapshot, lệnh/thao tác, môi trường, kết quả thật và giới hạn. Trạng thái khởi đầu NOT_RUN; FAIL khác BLOCKED. Reviewer không tự ký thay người dùng hoặc thay quyền external action. Tối đa ba vòng sửa cùng tiêu chí, hai vòng không tiến bộ thì báo owner và hướng giải quyết.

Dùng mẫu [requirements](../templates/memory/requirements-template.md), [gate](../templates/memory/gate-checklist-template.md), [evidence](../templates/memory/test-evidence-template.md) hoặc [handoff](../templates/memory/handoff-template.md) khi cần lưu và được phép. Không tạo đầy đủ hồ sơ cho tác vụ nhỏ chỉ để đủ hình thức.

## Prompt khởi đầu

```text
Dùng release-manager chốt snapshot, evidence và action được phép: push, PR, merge, tag hay deploy. Chuẩn bị mọi thứ có thể kiểm tra trước bước external action.
```

## Kết thúc đúng phạm vi

Báo phần đã làm, bằng chứng, phần chưa chạy, người nhận và bước tiếp theo. Không gọi sản phẩm production-ready, zero-regression hay an toàn tuyệt đối từ quy trình này.
