# Nguồn tham khảo và provenance

Nội dung v2 được viết lại bằng tiếng Việt theo yêu cầu dự án. Các nguồn sau dùng để đối chiếu cấu trúc và ý tưởng; không nhập toàn bộ mã, prompt hay script bên thứ ba vào repository. Commit dưới đây là snapshot đã đọc, không phải yêu cầu phải cài chúng.

| Nguồn | Snapshot đã khảo sát | Phần dùng để tham khảo |
| --- | --- | --- |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | [`b37b5bb33b78`](https://github.com/msitarzewski/agency-agents/tree/b37b5bb33b78f2c1d6567d98e25ca818e3259219) | Đối chiếu bộ vai trò chuyên gia gần với ý tưởng mowftee-guild, cách bàn giao và workflow MVP. |
| [obra/superpowers](https://github.com/obra/superpowers) | [`2ce8aa15d05b`](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) | Tham khảo quy trình lập kế hoạch, debug có hệ thống, review và xác minh bằng chứng trước khi báo hoàn thành. |
| [anthropics/skills](https://github.com/anthropics/skills) | [`dbd4588f9e10`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44) | Học cách viết SKILL.md có phạm vi rõ ràng, tách tài liệu hỗ trợ và đánh giá chất lượng skill. |
| [wshobson/agents](https://github.com/wshobson/agents) | [`0874a27b17a2`](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06) | Tham khảo chuyên môn backend/database, phối hợp nhóm agent và cách đóng gói plugin cho nhiều công cụ. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | [`90606c8315ee`](https://github.com/affaan-m/ECC/tree/90606c8315ee09cafc303515c5f33024db6b9882) | Tham khảo vòng xác minh, đánh giá chất lượng, quản lý context và các ví dụ hooks. |
| [openai/plugins](https://github.com/openai/plugins) | [`0722921d5542`](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a) | Nguồn ví dụ plugin Codex hiện tại: manifest, skill đi kèm, marketplace và cấu hình kết nối. |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | [`e8d346bcb691`](https://github.com/sickn33/agentic-awesome-skills/tree/e8d346bcb691225fb6ae51a49c353bcedb2ef61d) | Tra cứu skill theo chuyên môn và cách tổ chức catalog/bundle để chọn đúng nhóm cần dùng. |
| [openai/skills](https://github.com/openai/skills) | [`49f948faa925`](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431) | Đối chiếu mẫu skill Codex đời trước; chỉ dùng để tham khảo lịch sử. |

## Giới hạn tái sử dụng

Các repo tổng hợp có thể có nguồn trùng nhau; không coi số repo là số bằng chứng độc lập. Anthropic Skills có license khác nhau theo skill; các tài liệu DOCX/PDF/PPTX/XLSX không được nhập vào bản này. OpenAI Skills thông báo deprecated và trỏ sang OpenAI Plugins. Đọc license file cụ thể khi muốn tái sử dụng nội dung ở giai đoạn sau.

## Tài liệu sơ cấp đã đối chiếu ngày 26/10/2026

- [Agent Skills specification](https://agentskills.io/specification): frontmatter, tên và cấu trúc thư mục.
- [OpenAI Docs: Build skills](https://learn.chatgpt.com/docs/build-skills): discovery, local paths và metadata.
- [OpenAI Docs: Plugin skills](https://developers.openai.com/plugins/build/skills): ranh giới skill và plugin, reference theo nhu cầu.
- [Google Antigravity Docs: Agent skills](https://antigravity.google/docs/skills): App/IDE/CLI paths và cách gọi theo host.

Các đường dẫn và cách gọi là thông tin host có thể đổi theo phiên bản. Cần đối chiếu lại tài liệu chính thức trước khi thay cơ chế cài hoặc làm plugin/MCP.
