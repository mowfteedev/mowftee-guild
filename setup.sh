#!/usr/bin/env bash
# Thin launcher; payloads are copied as data, never executed.
set -euo pipefail
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if ! command -v python3 >/dev/null 2>&1; then
  echo 'mowftee-guild requires Python 3.9 or later.' >&2
  exit 2
fi
exec python3 "$SOURCE_DIR/scripts/guild.py" "$@"
