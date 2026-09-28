#!/bin/bash
# Moves the cleanup-pass files into _to_delete/ — nothing is erased.
# Review _to_delete/ in Finder, then empty it yourself when you are happy.
set -e
cd "$(dirname "$0")"
D="_to_delete"
mkdir -p "$D/Claude_outputs" "$D/tests" "$D/branding_experiments" "$D/branding_screenshots" "$D/misc"

mv -n "Claude outputs"                        "$D/Claude_outputs/"            2>/dev/null || true
mv -n "Episodes/Cleopatra/tests"              "$D/tests/"                     2>/dev/null || true
mv -n "Episodes/Cleopatra/_kit_source/__pycache__" "$D/misc/"                 2>/dev/null || true
mv -n "Fixed_Assets/Audio/AUDIO_PROMPTS.md.bak"    "$D/misc/"                 2>/dev/null || true
mv -n "_PENDING_CHANGES.md"                   "$D/misc/"                      2>/dev/null || true

for f in ACTBREAK_clock_test.mp4 ACTBREAK_look.mp4 ACTBREAK_v2.mp4; do
  mv -n "Fixed_Assets/Branding/$f" "$D/branding_experiments/" 2>/dev/null || true
done

for f in lowerthird_paper_options.png lowerthird_paper_sizes.png lowerthird_paper_sides.png \
         lowerthird_mockup.png plate_placement_guide.png panel_mark_check.png paper_check.png \
         endcard_guide.png cam3_wide_branded_reference.png; do
  mv -n "Fixed_Assets/Branding/$f" "$D/branding_screenshots/" 2>/dev/null || true
done
mv -n "Fixed_Assets/Branding/intro_source/intro_keyframes.png" "$D/branding_screenshots/" 2>/dev/null || true

echo
echo "Moved. Nothing deleted. Review:"
du -sh "$D" 2>/dev/null
find "$D" -type f | wc -l | xargs echo "files in _to_delete:"
echo
echo "NOT touched, on purpose: _raw_takes/, the draw-on clips, stone_4s/vessel_4s,"
echo "intro_source scripts, seed frames, DECISIONS_ARCHIVE.md, KLING_MIGRATION.md."
