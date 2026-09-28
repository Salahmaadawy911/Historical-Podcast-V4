#!/bin/bash
# Pull freshly-downloaded ElevenLabs audio out of ~/Downloads into _raw_takes/.
#
#   ./intake.sh ROOMTONE_studio        # files every audio file touched in the last 90 min
#   ./intake.sh SFX_sand 30            # ...or in the last 30 min
#
# Copies rather than moves — clear ~/Downloads yourself afterwards.
set -euo pipefail
LABEL="${1:?usage: intake.sh <label> [minutes, default 90]}"
MINS="${2:-90}"
DL="$HOME/mnt/Downloads"
DEST="$(cd "$(dirname "$0")" && pwd)/_raw_takes"
mkdir -p "$DEST"
n=0
while IFS= read -r -d '' f; do
  n=$((n+1))
  ext="${f##*.}"
  printf -v out "%s/%s_%02d.%s" "$DEST" "$LABEL" "$n" "$ext"
  cp -n "$f" "$out"
  echo "  $(basename "$f")  ->  $(basename "$out")"
done < <(find "$DL" -maxdepth 1 -type f \( -iname '*.mp3' -o -iname '*.wav' \) -mmin "-$MINS" -print0 | sort -z)
echo "$n file(s) filed as $LABEL in _raw_takes/"
