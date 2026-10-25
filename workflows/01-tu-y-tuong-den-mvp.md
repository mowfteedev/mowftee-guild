# Từ ý tưởng đến MVP

Tạo MVP có phạm vi kiểm chứng được, kiến trúc phù hợp và bàn giao có thể chạy theo tài liệu.

**Mức rủi ro:** R1 mặc định; tăng R2 cho quyền/dữ liệu/tiền, R3 chỉ khi thực sự tác động hệ thống vận hành.

## Cách dùng

Đối chiếu [protocol](../docs/protocol.md) và [risk/evidence](../docs/risk-and-evidence.md). Bảng dưới là phân công, không tự tạo agent hay cấp quyền tool. Với việc nhỏ, gộp cổng phù hợp và ghi lý do; với R2/R3 giữ điều kiện kiểm định độc lập. Khi READ-ONLY, trả kết quả trong hội thoại và không ghi memory.

## Ma trận trách nhiệm

| Cổng | Thực thi | Phản biện | Kiểm định / tiếp nhận |
| --- | --- | --- | --- |
| 1. Định hình phạm vi | product-analyst | tech-lead | tester |
| 2. Kiến trúc và nền tảng | software-architect | api-designer, database, designer | security khi có trust boundary mới |
| 3. Triển khai theo phạm vi | frontend, backend | api-designer, designer, database | code-reviewer |
| 4. Kiểm chứng sản phẩm | tester | test-automator, accessibility, performance theo rủi ro | Reviewer độc lập phù hợp mức rủi ro |
| 5. Đóng gói và bàn giao | devops, doc-writer | sre | release-manager |

## Cổng 1: Định hình phạm vi

**Đầu vào:** Ý tưởng, người dùng và constraints.

**Thực hiện:** Viết AC, happy/error path, ngoài scope và câu hỏi quan trọng.

**Điều kiện bàn giao:** AC đo được, quyền và owner rõ ràng.

**Nếu không đạt:** Trả lại yêu cầu mơ hồ; tiếp tục phần không phụ thuộc câu trả lời.

## Cổng 2: Kiến trúc và nền tảng

**Đầu vào:** AC và hiện trạng module/data/UI.

**Thực hiện:** Chọn phương án phù hợp, thiết kế contract/schema/spec, ghi ADR có đánh đổi; migration có owner riêng.

**Điều kiện bàn giao:** Đầu vào triển khai rõ, phản biện quyền và failure modes được giải quyết.

**Nếu không đạt:** Không ép một stack hoặc đưa công nghệ mới khi chưa có lý do.

## Cổng 3: Triển khai theo phạm vi

**Đầu vào:** Contract và đặc tả đã chốt.

**Thực hiện:** Chia vùng file, triển khai theo cấu trúc hiện hữu; test-automator bổ sung checks có giá trị.

**Điều kiện bàn giao:** Diff có thể review, invariant và lỗi được xử lý, kiểm tra liên quan có kết quả thật.

**Nếu không đạt:** Lỗi contract quay về đúng owner; không dùng mock để giả hoàn thành tích hợp.

## Cổng 4: Kiểm chứng sản phẩm

**Đầu vào:** Snapshot, AC và môi trường test.

**Thực hiện:** Đối chiếu AC, khám phá lỗi biên, quyền và phục hồi; chọn mức fuzz/load theo môi trường được phép.

**Điều kiện bàn giao:** Không còn blocker bắt buộc; mỗi AC có evidence hoặc còn mở rõ ràng.

**Nếu không đạt:** Trả finding với trigger/expected/actual, sửa và kiểm lại theo giới hạn vòng.

## Cổng 5: Đóng gói và bàn giao

**Đầu vào:** Snapshot đã kiểm chứng và quyền external action.

**Thực hiện:** Kiểm cách build/chạy, ghi prerequisites, rollout/rollback và giới hạn; chỉ thực hiện action đã được phép.

**Điều kiện bàn giao:** Người tiếp nhận có tài liệu và artifact đúng phiên bản; phần chưa chạy được công bố.

**Nếu không đạt:** Thiếu quyền deploy: bàn giao bản có thể review, không tự phát hành.

## Evidence và vòng sửa

Mỗi tiêu chí cần snapshot, lệnh/thao tác, môi trường, kết quả thật và giới hạn. Trạng thái khởi đầu NOT_RUN; FAIL khác BLOCKED. Reviewer không tự ký thay người dùng hoặc thay quyền external action. Tối đa ba vòng sửa cùng tiêu chí, hai vòng không tiến bộ thì báo owner và hướng giải quyết.

Dùng mẫu [requirements](../templates/memory/requirements-template.md), [gate](../templates/memory/gate-checklist-template.md), [evidence](../templates/memory/test-evidence-template.md) hoặc [handoff](../templates/memory/handoff-template.md) khi cần lưu và được phép. Không tạo đầy đủ hồ sơ cho tác vụ nhỏ chỉ để đủ hình thức.

## Prompt khởi đầu

```text
Dùng tech-lead đọc hiện trạng và cùng product-analyst chốt AC cho MVP. Chọn vai trò theo đầu ra, ghi giới hạn thực thi, chưa deploy khi chưa được phép.
```

## Kết thúc đúng phạm vi

Báo phần đã làm, bằng chứng, phần chưa chạy, người nhận và bước tiếp theo. Không gọi sản phẩm production-ready, zero-regression hay an toàn tuyệt đối từ quy trình này.
