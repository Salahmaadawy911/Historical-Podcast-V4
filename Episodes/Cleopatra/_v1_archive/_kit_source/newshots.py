# -*- coding: utf-8 -*-
LOCK=("The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. "
"Framing, lens, lighting and background hold exactly as the start frame for the whole clip. All movement in the shot "
"belongs to the person; the camera contributes none.")
AUDIO=("Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library "
"audio, no added voiceover, no on-screen text, no subtitles, no logo.")
SILENT=("Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no "
"on-screen text, no subtitles, no logo.")
VH=("Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. "
"Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone "
"thinking aloud, not presenting.")
VG=("Voice: female, mid-30s. Low even alto, composed and precise. A light classical Mediterranean colouring over "
"otherwise clear English — present but never heavy. Controlled and authoritative rather than warm — never breathy, "
"never pleading.")
SKETCH=("A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline - broad "
"washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep "
"shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk "
"highlights, no metallic or gold accents.")

# ---- full replacement bodies, keyed by ORIGINAL id -------------------------
REWRITE = {}

REWRITE["P1_006"] = dict(
 header="INTERJECTION · GUEST · **7s**",
 meta="`start_frame` `frame_cleopatra_c` · 16 syllables · floor 6.7s",
 prompt="\n\n".join([LOCK,
  "The woman answers evenly, courteous but not warm, with the faintest dryness under it. Her tone stays low and level throughout.",
  'The woman says: "You have questions. Ask them plainly — I have heard the polite versions."',
  "She holds his gaze, hands folded in her lap, and blinks once at the end.",
  VG, AUDIO]),
 subtitle="You have questions. Ask them plainly — I have heard the polite versions.",
 sfx="studio room tone only.",
 note=("**changed:** the original ran *\"Ask them while I still have the time\"*, which put a clock on her life and "
       "belongs to the live-event frame this series does not use. The replacement establishes in her first line that "
       "she has been asked before — which is the retrospective frame stated in her own voice."))

REWRITE["P1_089"] = dict(
 header="INTERVIEW · HOST · **12s**",
 meta="`start_frame` `frame_host_d` · 33 syllables · floor 11.1s",
 prompt="\n\n".join([LOCK,
  "The host asks it lightly, almost as an afterthought, and lets the last question sit. His tone stays level and does not press.",
  'The host says: "One more thing before we break. Most people, if they know one thing about you, know that you loved Mark Antony. Was that what it was?"',
  "He settles back, one hand resting on the armrest, and holds her gaze.",
  VH, AUDIO]),
 subtitle="One more thing before we break. Most people, if they know one thing about you, know that you loved Mark Antony. Was that what it was?",
 sfx="studio room tone only.",
 note=("**changed:** the original ran *\"Octavian's forces have landed in the delta. They are already ashore\"* — live "
       "news arriving mid-interview, which contradicts the retrospective frame, and factually wrong besides: Octavian "
       "advanced overland from Syria and took Pelusium; the seaborne pressure that summer came from the west with "
       "Gallus at Paraetonium. Replacing the line removes the error rather than correcting it. The new question is the "
       "Part 2 hook."))

REWRITE["P1_092"] = dict(
 header="INTERVIEW · GUEST · **9s**",
 meta="`start_frame` `chain from P1_091` · 28 syllables · floor 8.8s",
 prompt="\n\n".join([LOCK,
  "The woman takes the question without defending against it — composed, unhurried, faintly amused at the last clause. Her tone stays low and even.",
  'The woman says: "It was a treaty first. Whether it became more than that is a question no one has ever asked me honestly."',
  "She settles upright, hands folded in her lap, and holds his gaze.",
  VG, AUDIO]),
 subtitle="It was a treaty first. Whether it became more than that is a question no one has ever asked me honestly.",
 sfx="studio room tone only.",
 note=("**changed:** the original ran *\"I have very little time left\"* — the clock again. The replacement answers the "
       "new question, opens more than it closes, and hands Part 2 its subject."))

REWRITE["P1_093"] = dict(
 header="WIDE_CREDITS · **15s**",
 meta="`start_frame` `frame_wide_cleopatra_c`",
 prompt="\n\n".join([LOCK.replace("belongs to the person","belongs to the people"),
  "The two of them are mid-conversation and it continues easily for the whole clip. They take turns: one speaks while the other listens and gives small acknowledgements — a nod, a slight shift of weight, a brief smile — then the turn passes back. Two or three turns across the clip, unhurried and low-key throughout. Small natural hand gestures from the man as he talks; her gestures stay minimal.",
  "Both stay seated in their chairs for the whole clip, holding the same distance from each other and from the camera. When one is listening, their hands come to rest.",
  AUDIO]),
 subtitle="—",
 sfx="generated track is DISCARDED — MUSIC_Outro_Bed and the credit roll run over the picture.",
 placement=("closing credits — generate with audio, then DISCARD the audio track entirely and run MUSIC_Outro_Bed and the "
  "credit roll over the picture. **Candidate for replacement by a fixed series outro** built once and reused for every "
  "guest, which would take this shot out of the per-part budget permanently."),
 note=("**changed:** the scripted exchange and both `Voice:` blocks are gone. They existed to drive voice attribution "
  "that is thrown away, and two voice blocks in one prompt is a failure mode bought for nothing. Start frame moved to "
  "`_c`, which `CAST.md` designates for openings and closings. Wardrobe, room, lighting and seating are not described — "
  "the start frame carries them — and the shot stays free of negations."))

# ---- brand new shots -------------------------------------------------------
NEW_WIDE = dict(
 after="P1_004", kind="WIDE_SILENT", header="WIDE_SILENT · **4s**",
 meta="`start_frame` `frame_wide_cleopatra`",
 prompt="\n\n".join([LOCK.replace("belongs to the person","belongs to the people"),
  "The two of them are settled and waiting to begin. Small natural stillness — a slow blink, a shift of weight, a hand resettling on an armrest. Neither speaks at any point in the clip.",
  "Both stay seated in their chairs for the whole clip, holding the same distance from each other and from the camera. Their mouths stay closed, the lips resting lightly together, the jaw relaxed and still.",
  SILENT]),
 subtitle="—",
 sfx="clip is SILENT — room tone bed carries it; MUSIC_Theme_Main is still running from P1_003 and resolves under this shot.",
 placement=("establishing, after the host's hook and before the welcome exchange. **This is the only shot in the part that "
  "puts host and guest in the same frame** — without it the episode is two singles intercut that never prove they share a "
  "room. Cut straight out of it into the singles for the welcome."),
 note=("**new shot.** Standard 3.0 with audio off — 8 cr/s, the cheapest clip type in the kit, and removing the audio "
  "channel removes the cause of invented mouth movement rather than arguing with it in the prompt. Kept to 4s: two people "
  "visibly together but silent reads wrong if held longer without music."))

NEW_HANDOFF = dict(
 after="P1_092", kind="INTERVIEW", header="INTERVIEW · HOST · **6s**",
 meta="`start_frame` `frame_host_b` · 16 syllables · floor 5.7s",
 prompt="\n\n".join([LOCK,
  "The host closes it warmly and without ceremony, as someone ending a session rather than a broadcast. His tone lifts very slightly on the last phrase.",
  'The host says: "Then that’s where we’ll pick it up. Part two, and the sixty ships."',
  "He gives a small nod and holds, hands still clasped between his knees.",
  VH, AUDIO]),
 subtitle="Then that’s where we’ll pick it up. Part two, and the sixty ships.",
 sfx="studio room tone only.",
 tag=("V",""),
 placement="the hand-off. Last spoken line of the part; the wide follows it under music.",
 note=("**new shot.** The wide that follows carries no dialogue, so the hand-off needs its own clip — the structure is "
  "question → short guest response → host hands off → wide. Names the Part 2 subject explicitly, calling back to the "
  "sixty ships from P1_083."))
