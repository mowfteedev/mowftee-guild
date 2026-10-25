# Ứng phó sự cố và postmortem

Giảm tác động trong quyền đã có, giữ bằng chứng và biến sự cố thành hành động cải thiện rõ owner.

**Mức rủi ro:** R3; khảo sát read-only vẫn không cấp quyền mutation.

## Cách dùng

Đối chiếu [protocol](../docs/protocol.md) và [risk/evidence](../docs/risk-and-evidence.md). Bảng dưới là phân công, không tự tạo agent hay cấp quyền tool. Với việc nhỏ, gộp cổng phù hợp và ghi lý do; với R2/R3 giữ điều kiện kiểm định độc lập. Khi READ-ONLY, trả kết quả trong hội thoại và không ghi memory.

## Ma trận trách nhiệm

| Cổng | Thực thi | Phản biện | Kiểm định / tiếp nhận |
| --- | --- | --- | --- |
| 1. Xác nhận và khoanh vùng | incident-responder | sre | Owner hệ thống |
| 2. Giảm tác động | Owner có quyền thực thi | devops, database, security theo tình huống | incident-responder |
| 3. Xác minh phục hồi | sre | tester khi phù hợp | incident-responder |
| 4. Postmortem và follow-up | incident-responder, doc-writer | sre, tech-lead | Owner tiếp nhận |

## Cổng 1: Xác nhận và khoanh vùng

**Đầu vào:** Triệu chứng, thời gian và quyền.

**Thực hiện:** Đo ảnh hưởng người dùng, thu dữ liệu an toàn và ghi giả thuyết có thể kiểm chứng.

**Điều kiện bàn giao:** Tác động và owner rõ, timeline có timezone.

**Nếu không đạt:** Không gọi một log lẻ là root cause.

## Cổng 2: Giảm tác động

**Đầu vào:** Phương án và quyền tương ứng.

**Thực hiện:** Chọn hành động nhỏ có thể đảo ngược, ghi trước/sau và điểm dừng; thay một biến khi có thể.

**Điều kiện bàn giao:** Tác động giảm có bằng chứng hoặc biết cần rollback/chuyển owner.

**Nếu không đạt:** Không disable bảo vệ hoặc xóa dữ liệu ngoài scope.

## Cổng 3: Xác minh phục hồi

**Đầu vào:** Tín hiệu sau mitigation.

**Thực hiện:** Kiểm user journey và độ ổn định trong cửa sổ phù hợp, giữ residual risk.

**Điều kiện bàn giao:** Có bằng chứng phục hồi thực tế, không chỉ process sống.

**Nếu không đạt:** Nếu chỉ giảm triệu chứng, ghi mitigation còn root cause chưa xử lý.

## Cổng 4: Postmortem và follow-up

**Đầu vào:** Timeline và evidence đã che secret.

**Thực hiện:** Ghi yếu tố góp phần, điều hiệu quả, việc cần sửa và kiểm chứng tái diễn.

**Điều kiện bàn giao:** Follow-up có owner, ưu tiên và tiêu chí hoàn thành.

**Nếu không đạt:** Không đổ lỗi cá nhân hoặc tự gửi thông báo ra ngoài.

## Evidence và vòng sửa

Mỗi tiêu chí cần snapshot, lệnh/thao tác, môi trường, kết quả thật và giới hạn. Trạng thái khởi đầu NOT_RUN; FAIL khác BLOCKED. Reviewer không tự ký thay người dùng hoặc thay quyền external action. Tối đa ba vòng sửa cùng tiêu chí, hai vòng không tiến bộ thì báo owner và hướng giải quyết.

Dùng mẫu [requirements](../templates/memory/requirements-template.md), [gate](../templates/memory/gate-checklist-template.md), [evidence](../templates/memory/test-evidence-template.md) hoặc [handoff](../templates/memory/handoff-template.md) khi cần lưu và được phép. Không tạo đầy đủ hồ sơ cho tác vụ nhỏ chỉ để đủ hình thức.

## Prompt khởi đầu

```text
Dùng incident-responder ghi tác động, timeline và quyền hiện có. Thu dữ liệu read-only trước; không reboot, rotate key, gửi thông báo hoặc restore khi chưa được phép.
```

## Kết thúc đúng phạm vi

Báo phần đã làm, bằng chứng, phần chưa chạy, người nhận và bước tiếp theo. Không gọi sản phẩm production-ready, zero-regression hay an toàn tuyệt đối từ quy trình này.
