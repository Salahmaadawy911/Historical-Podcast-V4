# -*- coding: utf-8 -*-
# The five former Pexels rows, converted to generated charcoal b-roll.
from newshots import SKETCH
SILENT_BR = ("Audio: ambience only, quiet and low. No music, no dialogue, no voiceover, no on-screen text, "
             "no subtitles, no logo.")

def row(move, subject, motion, audio, still_subject):
    return dict(
      still="\n\n".join([SKETCH, still_subject,
        "Wide still image, nothing in motion, no figures. Composition balanced and simple, with clear empty space for on-screen text."]),
      video="\n\n".join([move, SKETCH + " It stays a drawing for every frame of the clip; the stroke texture and paper grain "
        "remain visible throughout, and it never resolves into photographic footage.", motion, audio]))

CONVERT = {}

CONVERT["P1_003"] = dict(dur=5, desc="Low light breaking on moving dark water.", **row(
  "The camera drifts slowly sideways across the water, a single steady lateral move, nothing else.",
  None,
  "The broken bands of light on the surface shift and reform continuously as the water moves beneath them. The far shoreline holds still.",
  SILENT_BR,
  "A wide expanse of open water at low light, the surface broken into long horizontal bands of reflected light, a thin dark shoreline far off at the top of the frame. No boats, no figures, no buildings."))

CONVERT["P1_009"] = dict(dur=5, desc="Standing grain moving in wind.", **row(
  "The camera pushes in very slowly toward the standing grain.",
  None,
  "The heads of grain bend and recover in a slow travelling wave as the wind crosses the field, the nearest stalks moving most.",
  SILENT_BR,
  "A dense field of tall ripe grain filling the frame, heads heavy at the top of each stalk, a low flat horizon behind. No figures, no buildings, no machinery."))

CONVERT["P1_031"] = dict(dur=6, desc="Deep-cut hieroglyphs, raking light — act transition.", **row(
  "The camera drifts slowly sideways along the carved wall, a single steady lateral move.",
  None,
  "Only the light moves: the shadows inside the cut grooves lengthen and shorten very slightly as the angle shifts across the surface. The stone itself is still.",
  SILENT_BR,
  "A weathered stone wall covered in deep-cut carved figures and symbols in ordered vertical columns, lit hard from one side so every groove throws a shadow. No modern objects, no people."))

CONVERT["P1_034"] = dict(dur=6, desc="Waves breaking on a shoreline in low light.", **row(
  "The camera pulls back very slowly from the water's edge.",
  None,
  "A wave gathers, breaks along the shoreline and draws back, then another behind it. The foam spreads and thins across the wet sand each time.",
  SILENT_BR,
  "A low shoreline seen close to the waterline, a wave curling and breaking across the frame, wet sand catching the light in the foreground. No figures, no boats, no buildings."))

CONVERT["P1_047"] = dict(dur=6, desc="Embers and sparks drifting against darkness.", **row(
  "The camera tilts slowly upward, following the embers as they rise.",
  None,
  "Embers lift and drift upward across the frame, wandering as they go, some fading out before they leave the top of the frame. The darkness behind them is still.",
  SILENT_BR,
  "Scattered points of ember light drifting against a deep dark ground, brightest low in the frame and thinning toward the top, with faint smoke shapes between them. No fire source visible, no figures, no buildings."))
