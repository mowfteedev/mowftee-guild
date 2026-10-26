#!/usr/bin/env bash
# Copy the Markdown skills in or remove the installed copies. No runtime manager.
set -euo pipefail
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MARKER='.mowftee-guild'
usage() {
  echo 'Cách dùng: ./setup.sh install|uninstall [codex|antigravity|antigravity-cli]'
  echo 'Mặc định: antigravity. Cài lại để cập nhật bản đã chép.'
}
ACTION="${1:-help}"
if [[ "$ACTION" == 'help' || "$ACTION" == '--help' || "$ACTION" == '-h' ]]; then
  usage
  exit 0
fi
if [[ $# -gt 2 || ( "$ACTION" != 'install' && "$ACTION" != 'uninstall' ) ]]; then
  usage >&2
  exit 2
fi
case "${2:-antigravity}" in
  codex) DEST_DIR="$HOME/.agents/skills" ;;
  antigravity) DEST_DIR="$HOME/.gemini/config/skills" ;;
  antigravity-cli) DEST_DIR="$HOME/.gemini/antigravity-cli/skills" ;;
  *) usage >&2; exit 2 ;;
esac
if [[ -L "$DEST_DIR" ]]; then
  echo "Không ghi qua symlink: $DEST_DIR" >&2
  exit 1
fi
if [[ "$ACTION" == 'install' ]]; then
  if [[ ! -f "$SOURCE_DIR/LICENSE" ]]; then
    echo "Thiếu LICENSE ở repo nguồn: $SOURCE_DIR" >&2
    exit 1
  fi
  mkdir -p "$DEST_DIR"
elif [[ ! -d "$DEST_DIR" ]]; then
  echo 'Chưa có skill nào để gỡ.'
  exit 0
fi
DEST_DIR="$(cd "$DEST_DIR" && pwd -P)"
protect_source() {
  if [[ "$SOURCE_DIR/" == "$1/"* ]]; then
    echo "Giữ nguyên repo nguồn: $1" >&2
    exit 1
  fi
}
count=0
if [[ "$ACTION" == 'install' ]]; then
  # Check collisions first, before replacing any installed skill.
  for source in "$SOURCE_DIR"/skills/*; do
    [[ -d "$source" && -f "$source/SKILL.md" ]] || continue
    target="$DEST_DIR/$(basename "$source")"
    protect_source "$target"
    if [[ -L "$target" || ( -e "$target" && ( ! -d "$target" || ! -f "$target/$MARKER" ) ) ]]; then
      echo "Giữ nguyên thư mục có sẵn, chưa cài: $target" >&2
      exit 1
    fi
  done
  for source in "$SOURCE_DIR"/skills/*; do
    [[ -d "$source" && -f "$source/SKILL.md" ]] || continue
    target="$DEST_DIR/$(basename "$source")"
    rm -rf -- "$target"
    mkdir -p "$target"
    : > "$target/$MARKER"
    cp -R "$source/." "$target/"
    if [[ ! -e "$target/LICENSE.txt" && ! -L "$target/LICENSE.txt" ]]; then
      cp "$SOURCE_DIR/LICENSE" "$target/LICENSE.txt"
    fi
    count=$((count + 1))
  done
  echo "Đã chép $count skill vào $DEST_DIR"
else
  for target in "$DEST_DIR"/*; do
    [[ -d "$target" && ! -L "$target" && -f "$target/$MARKER" ]] || continue
    protect_source "$target"
    rm -rf -- "$target"
    count=$((count + 1))
  done
  echo "Đã gỡ $count skill của mowftee-guild khỏi $DEST_DIR"
fi
