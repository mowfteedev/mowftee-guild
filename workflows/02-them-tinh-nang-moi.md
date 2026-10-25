# Thêm tính năng và kiểm soát hồi quy

Thêm hành vi mới theo AC mà vẫn giữ các contract/hành vi cũ thuộc phạm vi hỗ trợ.

**Mức rủi ro:** R1 hoặc R2 theo dữ liệu, quyền và public contract.

## Cách dùng

Đối chiếu [protocol](../docs/protocol.md) và [risk/evidence](../docs/risk-and-evidence.md). Bảng dưới là phân công, không tự tạo agent hay cấp quyền tool. Với việc nhỏ, gộp cổng phù hợp và ghi lý do; với R2/R3 giữ điều kiện kiểm định độc lập. Khi READ-ONLY, trả kết quả trong hội thoại và không ghi memory.

## Ma trận trách nhiệm

| Cổng | Thực thi | Phản biện | Kiểm định / tiếp nhận |
| --- | --- | --- | --- |
| 1. Scope và baseline | product-analyst, tech-lead | api-designer, code-reviewer | tester |
| 2. Triển khai tương thích | backend, frontend | database, designer | code-reviewer, security theo rủi ro |
| 3. Hồi quy và nghiệm thu | test-automator, tester | accessibility, performance khi cần | Reviewer độc lập cho R2 |
| 4. Tài liệu và bàn giao | doc-writer | tech-lead | release-manager khi phát hành |

## Cổng 1: Scope và baseline

**Đầu vào:** Yêu cầu mới, hiện trạng và test cũ.

**Thực hiện:** Ghi AC và vùng ảnh hưởng; phân loại lỗi baseline tồn tại trước thay đổi.

**Điều kiện bàn giao:** Có phạm vi, baseline và kế hoạch tương thích.

**Nếu không đạt:** Baseline đỏ phải được phân loại, không tự sửa test cũ để xanh.

## Cổng 2: Triển khai tương thích

**Đầu vào:** AC và contract diff.

**Thực hiện:** Thực hiện thay đổi; migration-specialist quản lý expand/backfill/cutover khi cần.

**Điều kiện bàn giao:** Client cũ và mới có kế hoạch hoạt động; schema và quyền đúng.

**Nếu không đạt:** Breaking change chưa được chấp nhận thì dừng phần phụ thuộc, đề xuất lộ trình khác.

## Cổng 3: Hồi quy và nghiệm thu

**Đầu vào:** Snapshot và test baseline.

**Thực hiện:** Chạy checks vùng ảnh hưởng, kiểm tương thích consumer và hành vi mới; điều tra retry/flaky thật.

**Điều kiện bàn giao:** AC mới được kiểm chứng; regression trong phạm vi được xử lý hoặc ghi rõ blocker.

**Nếu không đạt:** Không tăng retry, xóa test hoặc bỏ AC để qua cổng.

## Cổng 4: Tài liệu và bàn giao

**Đầu vào:** Evidence và scope cuối cùng.

**Thực hiện:** Cập nhật docs/API/changelog/memory được phép; push/merge/deploy theo quyền riêng.

**Điều kiện bàn giao:** Tài liệu khớp code; người duyệt xem được diff và giới hạn.

**Nếu không đạt:** CI pending được báo pending, không coi là pass.

## Evidence và vòng sửa

Mỗi tiêu chí cần snapshot, lệnh/thao tác, môi trường, kết quả thật và giới hạn. Trạng thái khởi đầu NOT_RUN; FAIL khác BLOCKED. Reviewer không tự ký thay người dùng hoặc thay quyền external action. Tối đa ba vòng sửa cùng tiêu chí, hai vòng không tiến bộ thì báo owner và hướng giải quyết.

Dùng mẫu [requirements](../templates/memory/requirements-template.md), [gate](../templates/memory/gate-checklist-template.md), [evidence](../templates/memory/test-evidence-template.md) hoặc [handoff](../templates/memory/handoff-template.md) khi cần lưu và được phép. Không tạo đầy đủ hồ sơ cho tác vụ nhỏ chỉ để đủ hình thức.

## Prompt khởi đầu

```text
Dùng tech-lead và product-analyst đánh giá tính năng mới, đọc baseline, khoanh vùng consumer và AC. Không gọi kết quả là zero regression tuyệt đối chỉ từ một suite test.
```

## Kết thúc đúng phạm vi

Báo phần đã làm, bằng chứng, phần chưa chạy, người nhận và bước tiếp theo. Không gọi sản phẩm production-ready, zero-regression hay an toàn tuyệt đối từ quy trình này.
