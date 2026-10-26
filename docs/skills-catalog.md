# Danh sách skill

Các skill là những góc nhìn chuyên môn để một người dùng với cùng trợ lý. Không cần gọi đủ bộ hoặc có thêm người quản lý.

## Chọn điểm bắt đầu

| Mục tiêu | Skill chính | Mở rộng khi cần |
| --- | --- | --- |
| Chưa rõ nên xây gì hoặc làm theo thứ tự nào | `product-analyst`, `tech-lead` | `software-architect`, `designer` |
| Thiết kế contract hoặc mô hình dữ liệu | `api-designer`, `database` | `migration-specialist` khi chuyển dữ liệu đang có |
| Viết phần triển khai | `frontend` hoặc `backend` | Chuyên môn liên quan tới phần đang sửa |
| Có triệu chứng sai, crash hoặc test thất bại | `systematic-debugging` | Skill triển khai của tầng gây lỗi |
| Viết test, nghiệm thu hoặc đọc diff | `test-automator`, `tester` hoặc `code-reviewer` | Chọn theo đầu ra cần nhận |
| Cải thiện bảo mật, hiệu năng hoặc cấu trúc | `security`, `dependency-auditor`, `performance`, `refactoring-specialist` | Chỉ chọn phạm vi thật sự cần kiểm |
| Triển khai, theo dõi, xử lý sự cố hoặc phát hành | `devops`, `sre`, `incident-responder`, `release-manager` | Phân biệt điều tra với hành động trên dịch vụ |
| Viết tài liệu hoặc chỉnh skill | `doc-writer`, `skill-maintainer` | Kiểm nội dung theo hành vi thực tế |

## Danh sách đầy đủ

| Tên skill | Dùng để làm gì, vai trò trong dự án |
| --- | --- |
| [accessibility](../skills/accessibility/SKILL.md) | **Khả năng tiếp cận** — Đánh giá và sửa accessibility cho giao diện web: keyboard, focus, semantic, thông báo và tương phản; không thay designer quyết định thẩm mỹ hoặc tuyên bố chứng nhận từ scanner. |
| [api-designer](../skills/api-designer/SKILL.md) | **Thiết kế hợp đồng API** — Thiết kế hoặc thay đổi API contract, schema, mã lỗi và tương thích phiên bản trước khi nối frontend với backend; không triển khai toàn bộ nghiệp vụ. |
| [backend](../skills/backend/SKILL.md) | **Phát triển máy chủ** — Triển khai hoặc sửa logic nghiệp vụ, endpoint và tích hợp máy chủ; dùng khi thay đổi hành vi server, không thay api-designer định nghĩa contract hay database thiết kế dữ liệu. |
| [code-reviewer](../skills/code-reviewer/SKILL.md) | **Thẩm định mã nguồn** — Rà soát diff và vùng ảnh hưởng để tìm lỗi đúng đắn, bảo mật hoặc bảo trì trước merge; không thay QA kiểm nghiệm runtime hoặc mở rộng thành audit toàn repo ngoài yêu cầu. |
| [database](../skills/database/SKILL.md) | **Thiết kế dữ liệu** — Thiết kế schema, ràng buộc dữ liệu, index và truy vấn theo workload thực tế; không tự chạy migration production hoặc thay migration-specialist lập kế hoạch chuyển đổi. |
| [dependency-auditor](../skills/dependency-auditor/SKILL.md) | **Kiểm toán phụ thuộc** — Kiểm kê dependency, advisory, provenance và thay đổi phiên bản khi audit hoặc nâng cấp thư viện; không tự coi mọi CVE là khai thác được hoặc nâng cấp phá vỡ API ngoài phạm vi. |
| [designer](../skills/designer/SKILL.md) | **Thiết kế UI và UX** — Thiết kế luồng trải nghiệm, hệ thống token và đặc tả thành phần cho màn hình mới hoặc thay đổi giao diện; không thay frontend triển khai hay thay accessibility kiểm định. |
| [devops](../skills/devops/SKILL.md) | **Hạ tầng và CI/CD** — Xây dựng hoặc sửa container, CI/CD, cấu hình triển khai và hạ tầng lặp lại được; không tự quyết định phát hành hoặc thực thi production khi chưa có quyền. |
| [doc-writer](../skills/doc-writer/SKILL.md) | **Tài liệu và bàn giao** — Viết hoặc cập nhật hướng dẫn sử dụng, tài liệu kỹ thuật, API và bàn giao từ hành vi thực tế; không dùng mẫu kết quả đẹp thay cho kiểm chứng. |
| [frontend](../skills/frontend/SKILL.md) | **Phát triển giao diện** — Triển khai và sửa giao diện, state, kết nối API và responsive theo design system hiện có; không tự định nghĩa lại sản phẩm hoặc thay kiểm định khả năng tiếp cận. |
| [incident-responder](../skills/incident-responder/SKILL.md) | **Ứng phó sự cố** — Điều tra và điều phối giảm thiểu một sự cố đang diễn ra hoặc viết postmortem; không dùng cho review bảo mật thường kỳ hay tự sửa production ngoài quyền hiện có. |
| [migration-specialist](../skills/migration-specialist/SKILL.md) | **Di chuyển dữ liệu** — Lập và kiểm chứng migration schema hoặc dữ liệu, backfill, cutover và phục hồi cho hệ thống đang có dữ liệu; không thay database quyết định mô hình dữ liệu. |
| [performance](../skills/performance/SKILL.md) | **Hiệu năng và đo tải** — Chẩn đoán bottleneck và kiểm chứng tối ưu CPU, bộ nhớ, query, bundle hoặc độ trễ khi có mục tiêu hiệu năng; không tự bắn tải production hoặc áp một ngân sách chung. |
| [product-analyst](../skills/product-analyst/SKILL.md) | **Phân tích yêu cầu** — Làm rõ mục tiêu sản phẩm, luồng nghiệp vụ và tiêu chí nghiệm thu trước một tính năng hoặc MVP; không chọn hạ tầng hay quyết định kiến trúc thay kỹ sư. |
| [refactoring-specialist](../skills/refactoring-specialist/SKILL.md) | **Tái cấu trúc có kiểm soát** — Tái cấu trúc code và giảm nợ kỹ thuật trong phạm vi đã chọn, giữ hành vi quan sát được; không tự thêm feature hoặc sửa API công khai ngoài scope. |
| [release-manager](../skills/release-manager/SKILL.md) | **Quản lý phát hành** — Tổng hợp điều kiện phát hành, phiên bản, rollout và rollback trước một release; không thay devops dựng pipeline hoặc tự merge/deploy ngoài yêu cầu. |
| [security](../skills/security/SKILL.md) | **Bảo mật ứng dụng** — Threat model hoặc rà soát bảo mật ứng dụng khi có yêu cầu hay thay đổi ranh giới tin cậy, xác thực, phân quyền và dữ liệu nhạy cảm; không tự làm pentest lên hệ thống thật. |
| [skill-maintainer](../skills/skill-maintainer/SKILL.md) | **Bảo trì và đánh giá skill** — Tạo, phân tách hoặc đánh giá skill và quy trình của guild khi thay đổi hành vi agent; không dùng để tự cài plugin hoặc thêm quyền thực thi. |
| [software-architect](../skills/software-architect/SKILL.md) | **Kiến trúc phần mềm** — Đánh giá và thiết kế ranh giới module, luồng dữ liệu, độ tin cậy và ADR cho thay đổi kiến trúc; không điều phối toàn bộ công việc hay ép một stack cố định. |
| [sre](../skills/sre/SKILL.md) | **Độ tin cậy và quan sát** — Thiết kế SLI/SLO, telemetry, alert, capacity và diễn tập phục hồi khi chuẩn bị hoặc cải thiện vận hành; không thay incident-responder chỉ huy sự cố đang diễn ra. |
| [systematic-debugging](../skills/systematic-debugging/SKILL.md) | **Sửa lỗi theo nguyên nhân có bằng chứng** — Tái hiện lỗi, xác minh cơ chế gây sai trước khi sửa, kiểm cùng ca trước/sau và hồi quy liên quan; không kết luận đã fix khi mới đổi code hoặc chỉ có ca giả lập. |
| [tech-lead](../skills/tech-lead/SKILL.md) | **Điều phối kỹ thuật** — Lập kế hoạch kỹ thuật và chọn góc nhìn chuyên môn cho yêu cầu nhiều phần; dùng để chia việc, quản lý phụ thuộc và tổng hợp quyết định trong dự án cá nhân. |
| [test-automator](../skills/test-automator/SKILL.md) | **Tự động hóa kiểm thử** — Thiết kế và viết unit, integration, contract hoặc E2E tests có khả năng tái hiện; không tự cấp nghiệm thu sản phẩm thay tester. |
| [tester](../skills/tester/SKILL.md) | **Nghiệm thu và kiểm thử khám phá** — Kiểm tra lại tính năng hoặc bản sửa, khám phá lỗi biên và đối chiếu tiêu chí nghiệm thu với bằng chứng; dùng khi cần xác minh kết quả triển khai. |

`test-automator` tập trung viết test; `tester` kiểm lại kết quả. `database` thiết kế dữ liệu; `migration-specialist` lo chuyển đổi dữ liệu hiện có. `devops` dựng môi trường; `sre` theo dõi độ tin cậy; `incident-responder` xử lý sự cố. Những ranh giới này giúp chọn đúng kiến thức, không tạo một bộ máy quản lý.

`systematic-debugging` dẫn đường điều tra một lỗi cụ thể qua bốn bước kiểm chứng; kiến thức của frontend/backend hoặc chuyên môn khác dùng cho phần triển khai. `test-automator` bổ sung ca hồi quy có giá trị, còn `tester` đối chiếu kết quả và giới hạn. Không cần tạo các agent riêng cho những phần đó.
