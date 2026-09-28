#!/bin/bash
# Build the teaser music bed for a given teaser length, so the music runs unbroken
# from the teaser straight into BRAND_bumper_in.
#
#   ./teaser_bed.sh 27.4        -> TEASER_bed.wav, 27.4s, ending exactly where the bumper begins
#
# How it works: the loop unit is one clock strike and its decay (source 3.50-7.50s of
# take 01). Its start and end floors match within 0.8 dB, so it butt-joins cleanly.
# The run-in is source 3.50-5.65, and the bumper's own cue starts at source 5.65 —
# so the hand-off is sample-continuous, not a crossfade.
set -euo pipefail
L="${1:?usage: teaser_bed.sh <teaser length in seconds>}"
D="$(cd "$(dirname "$0")" && pwd)"
LOOP="$D/MUSIC_Theme_teaser_loop.wav"; RUNIN="$D/MUSIC_Theme_teaser_runin.wav"
R=$(python3 -c "print(max(0.0, $L - 2.15))")
N=$(python3 -c "print(int($R // 4.0))")
HEAD=$(python3 -c "print(round($R - 4.0*$N, 3))")
TMP=$(mktemp -d); LIST="$TMP/l.txt"; : > "$LIST"
if (( $(python3 -c "print(1 if $HEAD > 0.05 else 0)") )); then
  ffmpeg -v error -i "$LOOP" -af "atrim=start=$(python3 -c "print(4.0-$HEAD)"),asetpts=PTS-STARTPTS,afade=t=in:d=0.30" -c:a pcm_s16le "$TMP/head.wav" -y
  echo "file '$TMP/head.wav'" >> "$LIST"
fi
for ((i=0;i<N;i++)); do echo "file '$LOOP'" >> "$LIST"; done
echo "file '$RUNIN'" >> "$LIST"
ffmpeg -v error -f concat -safe 0 -i "$LIST" -c copy "$D/TEASER_bed.wav" -y
rm -rf "$TMP"
echo "TEASER_bed.wav  $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$D/TEASER_bed.wav")s  (${N} loops + ${HEAD}s head + 2.15s run-in)"
