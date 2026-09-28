# Cleopatra — clip ledger

Which generated clips are used. **A kept clip lives at `Shots/<ID>.mp4`** (its kit id, nothing else in
the name); a clip that is not used goes to `Shots/_tests/_not_used/`. `clip_status.py` reads this file,
the kit and the folder together — run it after every generation session:

    python3 Fixed_Assets/tools/clip_status.py Episodes/Cleopatra/P1_kit.md

## Part 1 — kept (in `Shots/`)

| id | from | note |
|---|---|---|
| P1_002 | Pass 1 | cold-open narration; pauses 1.4 / 1.9 / 0.8 / 0.9 s — the 1.9 s one is trimmed in the edit |
| P1_006 | Pass 1 (regen) | new line *"Usually, others describe me."*; 2.0 s pause after *"Thank you."* — trim or keep by ear |
| P1_008 | T6a | first clip with the simple tones; 2.4 s pause between sentences, covered in the two-up |
| P1_009 | T6a (2nd take) | regenerated after the nod rule |
| P1_005 | CLI batch 1 | first CLI reaction: Kling 3.0, end frame, 1080p, clean copy (refetch) |
| P1_007 | CLI batch 2 | 2.4 s pause — trim in the edit |
| P1_011 | CLI batch 2 | audio-only 720p; 2.1 s pause — trim |
| P1_013 | CLI batch 2 | the "Meeds" line; hand comes down first (pose entry); ends ~0.25 s before the clip end |
| P1_014 | CLI batch 2 | reaction, end frame |
| P1_016 | CLI batch 1 | Turbo via CLI, audio ✓; last word ends 0.15 s before the clip end — tight but whole (duration rounding fixed, L21) |
| P1_017 | CLI batch 2 | ✓ |
| P1_018 | Kling 3.0 + audio + end frame (retake) | Turbo take drifted 39 px; this one 0 px; queued 17 min; 108 cr |
| P1_019 | T2 (3rd take) | beat map; stationary preset |
| P1_020 | T2 | 9 s (kit now 10 s): last word ends 0.25 s before the clip end — kept (Salah/Claude 2026-09-24): the next shot is his 3-syllable interjection, so a tight cut on her last word suits it; 100 cr saved |
| P1_021 | CLI batch 2 | ✓ |
| P1_022 | CLI batch 2 | first clip from the regenerated `frame_cleopatra_c` ✓ |
| P1_023 | CLI batch 1 | audio-only 720p ✓ |
| P1_025 | CLI batch 2 retake | audio-only 720p. The first take was fine — its camera flag was wrong, the picture is never used (batch_check fixed) |
| P1_027 | CLI batch 3 | first try refused (rate limit, no charge), second ✓ |
| P1_028 | lock-v3 test (Turbo, camera wording at the end only) | 0 px; 2.7 s pause — trim |
| P1_029 | CLI batch 3 | ✓ |
| P1_030 | lock-v3 test | 3 px (held); 2.1 s pause — trim |
| P1_032 | CLI batch 3 | audio-only ✓ |
| P1_033 | CLI batch 3 | 14 s, held on Turbo; 2.8 s pause — trim |
| P1_034 | CLI batch 1 (retake) | first take had her knee in the corner (L19); retake clean, corner check passes |
| P1_037 | CLI batch 1 (retake) | *"Yes."* — quiet (−54 dB mean), judged good by ear (Salah): raise the level in the edit |
| P1_036 | CLI batch 3 | ✓ |
| P1_039 | CLI batch 3 | audio-only; last word ends 0.2 s before the end, complete |
| P1_041 | CLI batch 3 | ✓ |
| P1_042 | CLI batch 4 | ✓ |
| P1_048 | CLI batch 4 | audio-only ✓ |
| P1_051 | CLI batch 4 | 2.9 s pause — trim |
| P1_052 | CLI batch 4 | ✓ |
| P1_054 | CLI batch 4 | audio-only ✓ |
| P1_044 | T5 | his cut-in line; cut at the end of *"Caesar"* = **2.98 s** (on the /b/ of *became*). The thigh hand stayed still — Kling moved the free hand over the armrest instead, mid-gesture at the cut, which is what the stop needs |
| P1_045 | T5 | the stop; from `start_frames/P1_045_start.png` (P1_044 at 2.98 s); mouth closed by ~0.4 s |
| P1_046 | T5 | her reply; 3.2 s silent lead-in before *"Allies"* — trimmed at the cut, delivery good (Salah) |
| P1_059 | CLI batch 4 | audio-only ✓ |
| P1_061 | CLI batch 4 | audio-only ✓ |
| P1_063 | CLI batch 4 | reaction, end frame ✓ |
| P1_064 | CLI batch 4 | ✓ |
| P1_066 | CLI batch 5 | ✓ |
| P1_069 | CLI batch 5 | reaction ✓ |
| P1_070 | CLI batch 5 | 2.2 s pause — trim |
| P1_073 | CLI batch 5 | 2.2 s pause — trim |
| P1_074 | CLI batch 5 | 1.5 s pause mid-sentence and a tight last word — judged good by ear (Salah) |
| P1_077 | CLI batch 5 | ✓ |
| P1_079 | CLI batch 5 | reaction ✓ |
| P1_082 | CLI batch 5 | ✓ |
| P1_083 | T6b | ends on its seed frame; joins P1_084 exactly |
| P1_084 | T6b | hand lowered late (after the first sentence) — accepted; "In a sanctuary" plays over P1_086 |
| P1_058 | lock-v2 test | first clip with camera lock v2 — background drift ≤ 2 px |
| P1_089 | CLI batch 5 | ✓ |
| P1_092 | CLI batch 5 | audio-only ✓ |
| P1_086 | end-frame test (`P1_086_end`) | ends on `frame_cleopatra_b`; use its end, ~1 s beat |
| P1_087 | T3 | split A (old tone wording) — accepted by ear |
| P1_088 | T3 | split B; 6–7 dB louder than A, levelled in the edit |

| P1_094 | CLI batch 6 | ✓ |
| P1_100 | CLI batch 6 | audio-only; ends 0.2 s before the end, complete |
| P1_102 | CLI batch 6 | reaction ✓ |
| P1_110 | CLI batch 6 | audio-only ✓ |
| P1_112 | CLI batch 6 | ✓ |
| P1_114 | CLI batch 6 | reaction ✓ |
| P1_116 | CLI batch 6 | audio-only ✓ |
| P1_119 | CLI batch 6 | reaction ✓ |
| P1_122 | CLI batch 6 | audio-only, interrupted line ✓ |
| P1_123 | CLI batch 6 | 1.6 s lead — trim |
| P1_124 | CLI batch 6 | flag was a false alarm (hair in the check box) — held |
| P1_126 | CLI batch 6 | reaction ✓ |
| P1_131 | CLI batch 6 | reaction ✓ |
| P1_132 | CLI batch 6 | ✓ |

## Part 1 — generated, not used (in `Shots/_tests/_not_used/`) → REGEN where the row stays in the kit

| file | why | action |
|---|---|---|
| T1_A | `Pronunciation:` paragraph read aloud | none — test only |
| T1_B | a test of P1_013's line (the "Meeds" respelling) — never P1_013 itself: 8 s ran to its last frame, knuckles on his jaw | none — P1_013 is generated in Pass 1 as normal |
| P1_006_described | T8 B (`T_008_B`), the old words — replaced by the new P1_006 (2026-09-25) | done |
| T_008_A | old `says` attribution | none — test only |
| P1_043_cli_drift | CLI take drifted 32 px + corner (L30) | **REGEN-WEB P1_043** |
| P1_085 | the shared-silence two-up — failed T6b; row retired | none — id left empty |

## Edit notes — clips made from the OLD `frame_cleopatra_c` (replaced 2026-09-26)
P1_022, P1_041, P1_052, P1_069, P1_070: the room sits **5 px left and ~0.4 % zoomed** against her other poses. In the edit, nudge +5 px and scale 99.6 % so the room lines up on cuts (Mode 6). Clips made from the new frame need nothing.

## 2026-09-27 — small-chair clips pulled (L41)
P1_017, P1_046, P1_082, P1_131, P1_132 were made from the small-chair `frame_cleopatra`. Moved to `Shots/_old_chair/`; REGEN P1_017 REGEN P1_046 REGEN P1_082 REGEN P1_131 REGEN P1_132 once the new big-chair `frame_cleopatra` (edited from `_b`) passes.

## 2026-09-27 — old-`_c` clips pulled too (L41)
P1_022, P1_041, P1_052, P1_069, P1_070 were made from the replaced old `_c`, whose chair also differs from the set (armrests 38–78 px off). Moved to `Shots/_old_chair/`; REGEN P1_022 REGEN P1_041 REGEN P1_052 REGEN P1_069 REGEN P1_070 from the new `_c`. The earlier edit note (nudge +5 px, 99.6 %) is void.

| P1_003a | — | **copy of P1_126** (kept `_b` reaction); use 0.0–1.5 s only. Four generated takes on `frame_cleopatra` had the host pushing into the bottom-left corner (in `Shots/_tests/_rejected/`). |

| P1_047 | L45 test | (in `_tests`, new wording) start = P1_046 last frame, end = `frame_cleopatra`. 0–0.4 s mouth closing from mid-word; 0.5–1.7 s her eyes lower and come back up; settled on the seed from 1.8 s. **Edit:** trim the first ~0.4 s; join P1_046→P1_047 with a short Smooth Cut (4–6 frames) to hide the small face change; lay P1_048 (host speech 1.2–2.6 s of its file) so *"It didn't keep you safe"* runs over her lowered eyes, ending as she looks back up; hold ~1 s, then P1_049. |
| P1_049 | — | started from `frame_cleopatra` (the image P1_047 ends on) instead of P1_047's extracted last frame — same picture, so the P1_047→P1_049 join is a plain cut. P1_047 kept as made. |
| P1_054 | — | host says *Arsinoe* wrong — **kept on purpose** (Salah): her *"Arsin-oh-ee."* in P1_055 plays as correcting him. |
| P1_055 | L49 | made with the hyphen respelling *Arsin-oh-ee* — said deliberately, like a correction; **kept** (fits after P1_054). Later names use one-word respellings. |
| P1_017, P1_023 | L50 | open on a lone word (*"Macedonian."*, *"Charming."*) — checked by ear 2026-09-27, both said right; kept. |
| P1_046 | L50 | line changed with Salah 2026-09-27: *"Allies, not lovers. …"* (both *"Allies."* and *"Allize."* were read as spelled). 13 s (one second over the model — the old 12 s take ended tight). |
| P1_046 | L50 | *Allies* failed 3× ("a-LEEZ") → line now *"Not lovers. That night I became his ally. …"* (Salah to OK). |
| P1_106 | L48 | CLI wave 2 take said *"Antoy's"* → table row Antony's · write: Antonee's; retake in the next wave. P1_127 gets the same respelling. |
| P1_090, 091, 093 | — | 090 had camera movement (not noticed until later); 091 and 093 chain from it → all three remade (old takes in `_tests/_rejected/`). |
| P1_050 still | L55 | v1 and v2 both drew later ships (cabins, two masts, a funnel) — per the fail-twice rule the picture changed: the quay with amphorae and smoke, **no ships in frame**. |
| P1_050 | L55 | **retired** — four stills (wide ×3, close ×1) all came back with a 19th-c. port behind (chimneys, gabled roofs, schooners). *"And the harbour burned"* now plays on her face in P1_049. |
| P1_028, 037, 038, 073, 095, 119, 120, 121 | — | 2026-09-28 (Salah): `frame_cleopatra_d` had a pose mistake → retired; all eight remade from `frame_cleopatra_i` (same pose). Old takes in `_tests/_rejected/`, old voice files in `Voice/P1/_replaced/`. |
| P1_004 | — | 2026-09-28 (Salah): welcome line now names the show — *"Welcome to History Answers Back. Cleopatra, …"*; 12 s; old take in `_tests/_rejected/`. |
