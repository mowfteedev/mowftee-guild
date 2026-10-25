# Changelog

## 2.0.0 — 2026-10-26

### Added

- 13 vai trò mới: product-analyst, software-architect, api-designer, migration-specialist, test-automator, dependency-auditor, accessibility, performance, sre, incident-responder, release-manager, skill-maintainer, refactoring-specialist.
- Runbook tự chứa và metadata Codex cho toàn bộ 23 skill; catalog cùng 6 profile.
- CLI quản lý cài/check/gỡ theo ownership/hash, dry-run, backup khi force, staging và phục hồi lỗi thông thường.
- Đích Codex, Antigravity App/IDE, Antigravity CLI và workspace; chọn skill chính xác.
- Memory templates cho requirements, handoff, risk, release và incident; tổng cộng 10 mẫu.
- Workflow sửa lỗi, phát hành, sự cố, cải thiện skill; kịch bản behavioral eval; test CLI và CI.
- Tài liệu sử dụng, nâng cấp, provenance, giới hạn và kiểm chứng phiên bản.

### Changed

- Viết lại 10 skill cũ theo trách nhiệm và evidence; bỏ persona phóng đại và tool/model giả định.
- Tách tiêu chí theo rủi ro; không áp stack, số đo hay tỷ lệ test tuyệt đối cho mọi dự án.
- Mọi mẫu kiểm chứng bắt đầu NOT_RUN; không có số liệu PASS minh họa dễ nhầm với kết quả thật.
- Không argument hiển thị help; install mặc định core thay vì cài toàn bộ. Check có mã thoát thất bại khi phát hiện sai lệch.

### Compatibility

Đọc [migration-v2](docs/migration-v2.md) trước khi thay bản v1 không có manifest. Cài đặt thật trên máy và plugin/MCP không tự được kích hoạt khi cập nhật repo. Không tuyên bố behavioral eval hoặc GUI host đã chạy chỉ vì CI tĩnh thành công.
