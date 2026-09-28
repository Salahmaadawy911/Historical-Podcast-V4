# Series furniture — built once, reused every episode

Everything here is **guest-agnostic**. It is made once, costs nothing per episode after that, and is pixel- and sample-identical in every part — which is most of what makes a channel look like a channel rather than a series of uploads.

**The amortisation argument is the whole point.** A closing wide generated per part costs 150 credits every part, forever, and carries the only two-character generation in the kit. A fixed outro costs one generation ever. Same for the title beat. Two assets built once remove ~200 credits a part and one class of risk permanently.

---

## The identity is the sketch

The charcoal style was chosen for a functional reason — to stop a reconstruction being mistaken for footage. Extending it to the intro, the outro and the on-screen text turns that functional choice into an **identity**, at no extra cost, and it solves a positioning problem quality alone cannot: every AI history channel reaches for the same photoreal defaults, and a charcoal-identified show is visibly not one of those inside two seconds, before anyone has judged the writing.

So the rule is: **anything the show says about itself is drawn.** B-roll, the intro, the outro, the lower thirds and the pull-quotes all sit on the same toned paper. The studio stays photoreal, because the contrast between the two is the thing that tells a viewer which is which.

---

## Placement map — where every fixed element sits in a part

| # | Element | Length | Position | Source |
|---|---|---|---|---|
| 1–3 | **`BRAND_opening`** | **19.17s** | **0:00** — the whole front of the show | **BUILT** — one file, one unbroken piece of music |
| 1 | ↳ `BRAND_disclosure` | 0.00–4.00 | **first clock strike** | motion graphics, on paper |
| 2 | ↳ the hook | 4.00–8.00 | **second strike** | **edit-only lift** of a guest clip from later in the part |
| 3 | ↳ the intro | 8.00–19.17 | **third strike** | motion graphics, no credits |
| 4 | Host direct-address hook | ~10s | — | generated, per part |
| 5 | ~~`WIDE_SILENT` establishing~~ | — | **removed 2026-09-18** | the two-shot now appears only at the close, as the first frame of `BRAND_bumper_out` |
| 5b | `BRAND_composite` | ~4s | **eyewitness episodes only** — end of cold open, immediately before the guest first appears | motion graphics |
| 6 | Welcome exchange → first question | — | — | generated, per part |
| … | `BRAND_lowerthird` ×2 | 4.5s each | host and guest first proper appearance | motion graphics |
| … | `BRAND_pullquote` ×3–4 | 4–5s each | over the silent reaction **after** its line | motion graphics |
| … | `BRAND_symbol` watermark | whole part | bottom-left on cross-shots | static overlay |
| … | `BRAND_mark` on the studio panel | every wide clip | fixed coordinates | static overlay |
| … | `BRAND_subscribe` | ~4s | once, after the strongest beat of Act B or C | motion graphics |
| … | **`BRAND_actbreak`** | **4.0s** | every act break (2 per part) | **fixed, zero cr** — study draws on the page over the theme's first 4s |
| n−1 | `BRAND_bumper_out` | 5s transform, then held | the close | **~43 cr per part** — charcoal still (3) + a generated start→end transformation (40) |
| n | `BRAND_endcard` | 20s | final card, held for YouTube end screens | motion graphics |

**Only two things in a part are generated per episode**: the dialogue and the b-roll. The outro is a three-credit still pass on a seed frame you already have, plus one transformation. Everything else in this table is furniture, made once.

---

## `BRAND_bumper_in` — the intro — **BUILT**

**Two files. `BRAND_opening.mp4` is the one the edit uses** — 19.17s, 1920×1080: a 6.17-second black slot for the hook line, then the 13-second intro, with the music unbroken from the first frame. `BRAND_bumper_in.mp4` is the 13-second intro alone, kept for any cut that does not want a hook.

**No generation per episode, no credits, no drift** — motion graphics over three charcoal draw-on clips made once, so it is byte-identical in every episode forever. Rebuildable from `intro_source/intro_build.py`.

### The opening, end to end

| time | picture | sound |
|---|---|---|
| **0.00** | **the disclosure card**, on paper | **first clock strike** |
| 0.0–4.0 | two lines and the mark, held | music decays to −47 dB |
| **4.00** | **the hook clip** — the guest, speaking | **second strike** |
| 4.0–8.0 | the line, then a hold on that face | |
| **8.00** | **the intro** — the hills study draws itself | **third strike** |
| 9.85 | it dissolves as the doorway begins | |
| 11.70 | the doorway dissolves as the hand begins | |
| 12.00 | | strike |
| 13.75–14.17 | the page clears | |
| 14.17 | **the mark alone on clean paper** | |
| 14.52 | the sand begins to fall | |
| 16.17–16.52 | sand stops, held | **the gap** |
| **16.52** | the reversal | **the downbeat** |
| 18.32 | the mark lands in the lockup | `SFX_plate` |
| 19.17 | end | decays into room tone |

**The clock counts the show in: strike, card. Strike, hook. Strike, intro.** Each of the three
openers arrives on a struck note, four seconds apart, and one continuous performance carries all
the way to the downbeat. That is why the card now sits inside this file rather than in front of it.

**This killed `MUSIC_Bed_Disclaimer`.** That cue existed only so the card would not play in true
silence. The clock does that job, in the show's own voice — the set drops from six cues to five.

⚠️ **Between strikes the music sits at −47 dB.** That is a clock in a room, not a score, which is
why unbroken music from 0:00 does not break the dry-by-default rule. A sustained bed would.

**The strikes fall at 0, 4, 8 and 12 — dead regular across the join.** That is what makes the hook
and the intro read as one piece rather than two things glued together, and it is why the slot is
6.17s rather than a round number: it is exactly one loop of the theme plus its run-in, so the clock
never breaks stride.

⚠️ **`BRAND_opening.mp4` ships with the hook slot as black — that black is a placeholder, not a
design.** The edit lays the lifted guest clip over **4.00–8.00s**. The file exists so the music,
the strikes and the intro are one fixed object that cannot drift; the picture in the slot changes
every episode.

**What fills the slot:** a short line (2–3 s) and then a hold on her face — **live** where the take
pauses cleanly after the sentence, a **freeze frame** on the last closed-mouth frame where it does not.
v1 Part 1 (archived, 2026-09-21 example only): *"Egypt did not survive without me."*, `P1_057` 5.6–9.6 s, 1.5 s live hold. The rerun picks its own hook.

### The hook treatment — the face emerging from the page (approved 2026-09-22, from Salah's mockup)

The slot is **not** a cut to the studio. It stays on **the same paper** as the card and the intro,
with the same continuous slow zoom, and the guest's face **emerges from the page**:

| | |
|---|---|
| Ground | `paper_source.png`, identical crop and zoom curve to `card_build` / `intro_build` — 0:00–0:19 is one unbroken page |
| Face | cropped from the hook clip and pushed in: crown-to-chin **650 px**, head centred at **(960, 470)**, a slow **3.5 %** push across the slot |
| Mask | a soft **hand-cut polygon** around head and shoulders that **keeps a little of the studio on purpose** — it must read as a frame lifted from the show, not a cut-out; paper above the head; the paper's grain breaks up the edge |
| Print | the paper's grain shows through the face (a portrait printed on the page) and a breath of paper tone is mixed in |
| Timing | **voice before face** — fade in from 4.05 s, full presence at the end of the line (+0.1 s); held beat on the closed-mouth face; fade back to bare paper **7.55 → 7.96 s**, before the strike at 8.00 and the first charcoal study |
| Audio | the hook clip's own voice under the clock, cut clean at the end of the slot |
| Fallback | if the take speaks again before 8.00, the frame **freezes** on the last closed-mouth frame and the audio stops there |

Built per part by `intro_source/hook_build.py <hook clip> <in s> <out.mp4> --face CX,CY,H` after
generation (the face position is the guest's *Hook framing* in `CAST.md`). Same treatment for every
guest and every part; only the clip, the in point and the framing change. Demo: `Episodes/Cleopatra/_v1_archive/DEMO_opening_hook_paper.mp4`.

⚠️ **The slot is fixed at 4.00 seconds, forever.** The clip is cut to the furniture, not the
furniture to the clip. `Fixed_Assets/Audio/teaser_bed.sh` builds a longer bed for the one episode
that genuinely needs it, but that is an exception, not a workflow.

### What happens

Toned paper, very slowly pushing in. The mark sits centred in ink, and the **only thing that moves is the sand in the hourglass.**

| | |
|---|---|
| 0.0–0.35s | the mark fades up, hourglass full |
| 0.35–2.0s | sand falls |
| 2.0–2.35s | **it stops.** A beat. |
| 2.35–3.1s | the sand runs **back up** |
| 3.2–4.15s | the symbol settles into the stacked lockup |
| 3.7–4.3s | HISTORY / ANSWERS BACK fades in beneath it |
| 4.3–5.0s | hold |

**The reversal is the whole idea.** Sand falls — time passes, the past recedes. Then it runs back up: *history answers back*. The premise of the show, stated in five seconds without a word.

**The beat before the reversal is what makes it work.** Without the pause it reads as a loop; with it, the reversal reads as a decision.

### Why nothing is generated

A video model asked to draw the mark would draw *a* microphone with *an* hourglass — close, and wrong, because a logo that is approximately right in every episode is worse than no logo. Keeping the mark a static vector overlay and animating only the sand removes that problem entirely rather than managing it.

### Two things that were got wrong first, and are worth keeping

**Ink sand in an ink microphone is invisible.** The hourglass is a counter-form — a void in the mark where the paper shows through. Filling it with ink merges it into the body around it. The sand is **lamp `#E0B071`**, the brand's warm accent, which reads against both the ink body and the paper void.

**Sand must be driven by volume, not by height.** Both bulbs are triangles, so area scales with the square of the distance from the apex. Moving the surface linearly empties the downward-pointing top bulb far too fast: measured, it was completely empty while the bottom was only 70% full, and the sand appeared to vanish mid-fall. Driving the surface by `sqrt(1-t)` conserves volume across the transfer — verified, the two bulbs sum to a constant, with a small excess mid-fall that is the falling stream itself, which is correct because that sand is in transit.

### Rebuilding it

`intro_source/intro_build.py` regenerates the whole sequence at any resolution or duration. It reads `brand_symbol_720.png`, `brand_mark_stack_900.png` and `paper_source.png` and outputs a frame sequence; ffmpeg assembles it. Nothing is hand-keyed, so a timing change is an edit to three numbers.

**Audio:** `MUSIC_Theme_Main` enters here and carries the beat alone. Cut the music so the reversal at 2.35s lands on a beat — that is the moment the idea arrives, and it should be heard as well as seen.

### Rejected

**A charcoal draw-on of the mark**, with the strokes appearing. It would have matched the b-roll, but it requires either a generation (which cannot hold the mark's exact geometry) or a hand-animated mask along every stroke path. The sand does more with less, and it says something the draw-on does not.

**Historical elements in the background.** The symbol was deliberately made era-neutral — "no columns or laurels, since the guest list runs from Cleopatra to Genghis Khan to Montezuma" — and a drawn scene would date the intro to one era and fight every guest who is not from it.

## `BRAND_actbreak` — the act break

**A study draws itself on the page, topped and tailed by the clock.** One chime opens the break,
the drawing builds, the finished page holds, and a second chime closes it — then the next act starts
clean. Fixed furniture: two clips, made once, reused in every episode forever. **Settled
2026-09-18.** Per-part cost: **zero.**

**The break is self-contained. Both chimes belong to it.** This is the whole point of the shape: the
closing chime is heard over the held drawing, not over the next act's first frame. An earlier build
cut out at 4.000 and let the next chime land on the interview — that made the break a hand-off
rather than an object, and it is wrong.

### The shape

**Length: 5.000 s.**

| time | picture | sound |
|---|---|---|
| **0.000** | hard cut from the single to the blank page | **the opening chime** — hits at 0.00, 0.50 (loudest, −4.4 dB) and 1.04 |
| 0.0–3.7 | charcoal marks accumulate into the study | the theme decays to −43 dB |
| 3.7–5.0 | the finished study holds still | |
| **4.000** | still on the held page | **the closing chime begins** — −18.9 dB |
| **4.500** | still on the held page | **its loud hit**, −9.4 dB — the one the ear reads as *the* chime |
| 4.75–5.0 | still on the held page | decaying, −28.9 dB and falling |
| **5.000** | hard cut into the next act's first single | out, in silence |

**Why the out-point is 5.000 and not 4.6 or 5.2.** The unit's strikes repeat at 4.00, 4.50 and
5.04, so 5.000 lands in the gap **immediately before the third hit** — the one natural silence
available. Cutting at 4.6 would stop just before the loudest strike, which reads as clipped; going
past 5.04 would start a third chime the break has no room to finish. A 60 ms fade sits on the tail
against a click; at −29 dB and falling it is inaudible as a fade.

**The bed is `MUSIC_Theme_teaser_loop.wav` — already built, and nothing needs editing.** Measured
2026-09-18: that file is **bit-identical to the opening's first 4.0 seconds** (max sample
difference 0.0). The opening's whole bed is that same 4.0-second unit repeated, so it starts and
ends flush by construction — which is exactly what a break bed has to do. One file, three uses:
the teaser, the opening, and now the break.

⚠️ **Three hits, not two.** The strikes inside the unit are at **0.00, 0.50 (the loudest at −4.4 dB
peak) and 1.04**, then three seconds of decay. What sounds like "a second tick at 4 seconds" is the
loop restarting. This is better than an evenly-spaced pair: the break opens with a cluster and then
empties out, so the drawing builds into silence rather than racing a metronome.

**Drop the break copy 4–6 dB under the opening's.** Same unit at the same level reads as the show
restarting; a few dB down reads as a reprise.

⚠️ **`MUSIC_Sting_Transition` is dead.** Its only job was the cut into the break. The theme's own
strike does it better — same instrument, so the break belongs to the same piece — and costs
nothing. **720 credits saved.** The two drones go back to one use each (Pompey, Actium); they do
not carry breaks.

### The clips — **BUILT 2026-09-18**

`BRAND_actbreak_vessel.mp4` and `BRAND_actbreak_stone.mp4`, both in `Fixed_Assets/Branding/`.
**5.000 s exactly**, 1916×1080, 24 fps, 120 frames (97 generated, then the last frame held for 23),
with the bed already laid in at −5 dB. They are finished files: drop one in, cut out on the last
frame, and the next act starts clean in silence. Alternate them — vessel at the first break, stone
at the second.

The paper in both was restored to the real page after generation; see **"The model changes the
paper"** in `INTRO_SKETCHES.md` for the measurement and the procedure. The worn step was dropped
after repeated failures; the grinding stone carries the same *wear* idea without the architecture.

### How they were made

**Generate at 4 seconds, not 3.** The intro studies are 3s because they are trimmed and overlapped
in a build; these are used whole. The generated clip is 4s and the last frame is then held to
**5.000 s** in the build, so the closing chime has a page to land on — the one edit these assets
get, done once. Kling 3.0 Standard, audio off, **8 cr/s = 32 cr a clip.** If a 4s option is not offered,
generate 5s and use the first 4.000 — the tail is only the finished drawing holding still.

**Prompt: the draw-on prompt in `INTRO_SKETCHES.md`, unchanged.** It names no object, so it is the
same prompt for every study. Start frame `paper_source.png`, end frame the study, camera-stationary
preset on.

**Two clips, and they are not the opening's three.** The viewer sees hills, doorway and hand thirty
seconds into every episode; seeing one again eight minutes later reads as running out of material
rather than as a motif. Breaks own their own subjects, so the two registers stay separate.

- **The vessel is already made** — `vessel.mp4`, the 3s draw-on test, and the study behind it is
  clean. It needs regenerating at 4s (32 cr) but the still costs nothing.
- **One more from the reserves** in `INTRO_SKETCHES.md` — worn step, knotted rope or worn coin.
  ~3 cr for the still, 32 cr for the clip.

**Total, once, forever: ~70 credits.** Alternate them: first break one, second break the other.

### Why fixed rather than per-act

A bespoke drawing at each break — a study of what the next act is about — was the earlier plan, and
it turns dead time into a forward pull. It was dropped for a better reason than cost. **Fixed
furniture is recognisable.** If the break is always the same two studies with the same four seconds
of clock, a viewer learns what it means inside one episode and reads every later one instantly. A
different picture every time never becomes a signal — it just looks like more b-roll, which matters
here because **all b-roll in this show is charcoal**, so a charcoal scene at a break is invisible as
a break. The page is the one register the b-roll never uses.

---

## `BRAND_bumper_out` — the outro

**The studio two-shot turns into a charcoal drawing of itself on camera, and the credits roll over the drawing.** Since 2026-09-18 this is the only place the two-shot appears anywhere in a part.

The transformation is **generated**, not cross-dissolved in the editor. Kling takes a start frame and an end frame and animates between them, so the change can be a drawing *happening* — tone washing in, the photograph falling away — rather than two images fading through each other. A cross-fade is a transition; this is an event.

**Build, per part:**

1. **Start from the outro wide** — since 2026-09-28 built per part in Seedream from three references (`cam3_wide.png` + the host's LAST-clip pose frame + the guest's last-clip pose frame), so the figures are true to scale and the host's pose matches his final line; then the mark is composited at the fixed panel coordinates → `frame_wide_[name]_outro_marked.png`. No wide clip is generated any more, so there is nothing to lift a frame from and nothing to pay for here.
2. **Charcoal pass** on that still (Kling Image 3.0, image-to-image, 2K) → the end frame. Use the canonical style block, unchanged.
3. **Generate the transformation**: start frame = the live still, end frame = the drawing, **5 seconds**, Kling 3.0 Standard with audio off — **40 cr**.
4. **Hold the last frame** as a still for about 3 seconds, clean, then cross-dissolve to the end card. There is no reason to generate seconds of a picture that has stopped changing. *(This step said "under the rest of the credit roll" until 2026-09-18. There is no credit roll — see "There is no credit roll" below. That stale phrase is what sized `MUSIC_Outro_Bed` at 60 seconds when the outro is 31.)*

**~43 credits a part**, against 150 for the per-part wide it replaces — and no two-character clip anywhere in the pipeline.

### The transformation prompt

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero
zoom. Framing, lens and composition hold exactly as the start frame for the whole clip.

The photographed room becomes a charcoal drawing of itself. The change begins at the edges of
the frame and moves inward, so the two figures are the last thing to turn. Colour drains away
to the warm grey of toned paper; shadows deepen into smudged charcoal and the paper grain
rises through the whole image.

Both people stay exactly where they are, at the same scale and in the same posture, through
the whole change. Nobody moves, enters or leaves.

Audio: quiet room tone only. No dialogue, no music, no library audio, no voiceover, no
on-screen text, no subtitles, no logo.
```

**Why the change starts at the edges and ends on the faces:** the last thing a viewer is looking at should be the last thing to transform. Turn the faces first and the rest of the frame is just catching up.

### The test — **PASSED**. Format confirmed.

Run on `frame_wide_cleopatra_marked.png`. The transformation from photograph to charcoal holds: the figures keep position, scale and posture through the change, and it lands on the drawing rather than overshooting. **This was the last unproven format in the project.** The procedure below stands as written; keep it for future guests.

#### The test as run

**It does not need a produced episode.** `Start_Frames/Cleopatra/frame_wide_cleopatra.png` already exists and is exactly the kind of frame the outro starts from. Total cost **~43 credits**.

**Step 0 — use the marked seed frame.** `frame_wide_[name]_marked.png` already carries the mark on the panel at the fixed coordinates. It used to feed the 4s establishing generation as well; that shot was removed on 2026-09-18, so the outro is now its only use. See `STUDIO_ASSETS.md` for why the blank-panel rule was revised.

**Step 1 — the end frame** — **Kling Image 3.0, 2K, 16:9, image-to-image with the marked still as the reference** (how every charcoal image in the show was made and tested; Salah, 2026-09-28). Paste as two unbroken lines:

```
A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk highlights, no metallic or gold accents.

Keep the composition, the framing and both figures exactly as they are in the source image — same positions, same postures, same scale, same size in frame.
```

**Step 2 — the transformation.** Start frame = the original wide, end frame = the drawing. **5 seconds, Kling 3.0 Standard, audio off** (40 cr).

```
The camera is stationary. Locked on a fixed tripod — zero pan, zero tilt, zero travel, zero zoom. Framing, lens and composition hold exactly as the start frame for the whole clip.

The photographed room becomes a charcoal drawing of itself. The change begins at the edges of the frame and moves inward, so the two figures are the last thing to turn. Colour drains away to the warm grey of toned paper; shadows deepen into smudged charcoal and the paper grain rises through the whole image.

Both people stay exactly where they are, at the same scale and in the same posture, through the whole change. Nobody moves, enters or leaves.

Audio: quiet room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo.
```

⚠️ **Watch the mark in the charcoal pass.** If the image model mangles it at that size, fall back to compositing it crisp onto the finished drawing — pixel-perfect, and it reads as a printed mark on a page rather than a drawn sign. A legitimate look, just less integrated.

### What to judge, in order

1. **Do the figures hold?** The real risk in start→end interpolation is the model re-posing or re-scaling the people mid-transform. Watch their shoulders and head positions across the clip, not just the first and last frames. **This is the pass/fail.**
2. **Does the change move inward from the edges,** or does the whole frame flip at once? A uniform crossfade is what the editor would have given for free; the prompt is buying a directional transformation.
3. **Does it land on the drawing and stop** — or overshoot into something that is neither photograph nor charcoal?
4. **Is the last frame usable as a held still?** It holds clean for about 3 seconds before the end card dissolves in, so it has to be a good drawing in its own right.

### If it fails

**Figures drifting** is the one failure with no prompt fix — it is what interpolation does when it has to invent a middle. Fall back to an editor cross-dissolve between the same two stills: worse, because a crossfade is a transition rather than an event, but free, certain, and still the right ending.

**A uniform flip** is worth one retry with the directional sentence strengthened. **An overshoot** means the end frame is not reading as a hard target — regenerate the charcoal still with the composition lock stated more firmly.

### Why this ending, and not an empty room

An earlier proposal was a fixed clip of the *empty* studio, generated once and reused forever. Guest-agnostic, so a true fixed asset — but it cost the part its last image of the two of them together, and it said nothing.

This says something: **the interview ends and the live picture becomes a drawing — the conversation becomes record.** For a show built on people answering across time, having the image turn into the medium we use for the past is the programme's thesis performed in five seconds. An empty room cannot do that.

⚠️ **Test the first one before committing the format.** Start/end-frame interpolation is reliable for camera and lighting changes and less reliable when it has to hold two faces steady through a full style change. The failure to watch for is the figures drifting, re-posing or changing scale mid-transform. If that happens, the fallback is the editor cross-dissolve — worse, but free and certain.

**It is guest-specific, and that is fine.** Being per-part only mattered when it cost 150 credits and carried real generation risk. At 43 credits it buys a better ending than a fixed asset would.

## Cards

All motion graphics. Same visual family: ink ground, paper type, mark small at the foot.

**`BRAND_disclosure`** — 3s at 0:00. Already specified in `skill_mode6_edit.md`; wording is byte-identical across the series and changes only for the whole series at once.

**`BRAND_composite`** — ~4s, eyewitness episodes only, at the end of the cold open. Wording fixed in shape, `[N]` filled per episode.

**`BRAND_subscribe`** — ~4s, once per part. Lower third rather than full screen, so the picture keeps running underneath. Place it **after** a strong beat, never over one. No sound effect: a whoosh on a research-led show reads as a different channel.

**`BRAND_endcard`** — 20s, held long enough for YouTube's end screens to sit on it. **A clean paper card**, cross-dissolved to from the held drawing. **BUILT 2026-09-18.**

⚠️ **The design is series-fixed; the render is per part.** The sources list and the next-part title change every time, so the finished file belongs in `Episodes/<Guest>/`, **never** in `Branding/`. Same for `BRAND_composite`, whose `[N]` is per episode. Only the builders are fixed furniture:

| | where it lives |
|---|---|
| `intro_source/endcard_build.py` | fixed — the design |
| `intro_source/composite_build.py` | fixed — the design |
| `intro_source/sources_audit.py` | fixed — the check |
| `Episodes/<Guest>/card_data_p1.json` | per part — sources and next title |
| `Episodes/<Guest>/BRAND_endcard_p1.mp4` | per part — the render |
| `Episodes/<Guest>/BRAND_composite_p1.mp4` | per part, **eyewitness episodes only** |

```bash
python3 endcard_build.py  Episodes/Cleopatra/card_data_p1.json  ecfr && \
  ffmpeg -r 24 -i ecfr/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 23 BRAND_endcard_p1.mp4
python3 composite_build.py 4 cofr     # eyewitness episodes only; 4 = the account count
```

The disclosure statement, the personal line, the signature and the mark are series-fixed and live inside the builder. They change for the whole series at once or not at all.

### The sources block is audited, not generated

`sources_audit.py` parses the part's kit and reports **what the provenance tags actually cite** against what the card lists — anything on the card that no tag supports, and anything the tags lean on that the card omits. Run it before every render.

**It audits rather than generates on purpose.** The tags name their sources in prose, inside a sentence explaining the claim — *"Roller, Cleopatra: A Biography; Chauveau"* — not as structured citations. Extracting that mechanically yields a long inconsistent list with every passing mention in it, which is not what the card is for. **The card is a curated claim; the tags are the evidence.** Automating the check is right; automating the authorship is not.

⚠️ **The first run found four sources cited in the tags and missing from the card** — Suetonius *Julius*, Horace *Odes* 1.37, Propertius, and Cicero's *De Rege Alexandrino*, all carrying the Augustan hostile-characterisation material. On a card whose whole purpose is the claim the show makes about itself, that is exactly the error worth catching. Part 1's list is now six lines, not five.

Carries, top to bottom, in one left column:

1. `AI-GENERATED DRAMATIZATION` as a walnut kicker, then **the full disclosure statement**
2. `PRIMARY SOURCES`, then the list — **generated from the part's `[D]` and `[I]` provenance tags**
3. `NEXT`, then the next part's title
4. the personal line and signature
5. **the support lines (added 2026-09-27, Salah)** — *"This series is independent — subscribing keeps it going."* / *"Who should sit in that chair next? Tell us in the comments."* Written to be true as it stands: no promise about who comes next (guests are scheduled ahead), and no apology for AI flaws (the disclosure already says what this is). Series-fixed, inside the builder.
6. the mark, bottom-left

The builder stops if the text stack runs into the mark — a part with a long sources list must shorten it (merge works by one author onto one line).

The sources are not decoration. They are the claim the show makes about itself, and this is the only place with room to make it in full.

### How the ending is structured — three beats, not one

| | |
|---|---|
| **1. The transformation, 5s** | completely clean, no text. It is the emotional ending and the show's thesis in one move; words on it while it happens undercut both. |
| **2. The drawing holds, ~3s** | still clean. Let it land. Cutting straight to text throws away what the transformation just built. |
| **3. The end card** | cross-dissolve to the paper card. |

**There is no credit roll.** A one-person channel rolling credits reads as performing a scale it does not have, and this is the one moment the show could accidentally look like that. The disclosure and the sources are the honest version of that slot — and they are the thing that differentiates the channel.

### Why a clean card and not a panel over the drawing

Both were built. A paper panel laid over the held drawing covers roughly 56% of the image the whole outro exists to produce, and it puts paper on paper.

It also fails on measurement. The charcoal drawing is **busy everywhere** — a 6×4 luminance survey of the real output gives local standard deviations of 34–39 even in its calmest zones. That is fine behind a short line and hopeless behind a paragraph, and the disclosure plus five source lines is a paragraph. **Body text on the drawing was never going to work**; it needed its own ground.

### Layout constraints

- **Keep the right third clear** — roughly x 65%–96%, y 13%–87% — for YouTube's end-screen elements. The card looks unbalanced without them and correct with them.
- Text column on the left at the standard 5.5% margin, about 52% of frame width.
- Walnut for the kickers, ink for the statement and the next-part title, a softened ink for the source list so it recedes behind the disclosure.

---

## Sound to picture — what each cue has to hit

The furniture is built now, so the audio is no longer written blind. Three cues have **specific motion to land against**, and writing them without that is how a good intro ends up with music that ignores it.

### `MUSIC_Theme_Main` — **DONE**, cut to the opening's beats

Take 01 of four. It was chosen on one measurement: its arrival is a **30 dB jump out of
near-silence**, where the other three takes peak only 8–16 dB above their own median. That is not a
quality that can be ordered in a prompt, only found — which is the argument against ever
regenerating this cue.

The finished cue runs the full 19.17s of `BRAND_opening`: clock strikes under the hook and the
studies, the page clearing into quiet, the gap at 16.15–16.50, the downbeat on the reversal, and
then a crossfade into **the take's own outro decay** rather than a fade-out. It ends rather than
stops.

**The reversal at 16.50s is the point of the whole piece.** Everything before it is approach,
everything after is consequence.

**The silence at 16.15–16.50 is doing as much work as the music.** A theme that plays through the
pause flattens the idea back into a loop. It is a real gap, not a duck.

Three derived files support the teaser bed, all from the same take:
`MUSIC_Theme_teaser_loop.wav` (4.0s, one strike and its decay, butt-joins to itself within 0.8 dB),
`MUSIC_Theme_teaser_runin.wav` (2.15s, hands off to the intro sample-continuously), and
`teaser_bed.sh`, which builds a bed of any length for the exceptional episode.

### `SFX_sand` — the intro's only effect

A dry granular trickle under the fall. Very quiet, close, no reverb — sand on paper, not an egg timer. It **stops dead at 2.0s** with the picture, and returns reversed for the run back up, which should sound subtly wrong in a way the viewer feels rather than identifies.

Do not let it read as a rainstick or a shaker. One thin stream.

### `SFX_plate` — the on-screen text

**Yes, the plates need a sound, and it is a paper sound.**

A single soft paper settle — a sheet laid down on a desk. Dry, close, no reverb, no whoosh. It plays on the **entrance only**; exits are silent, because a sound on the way out draws attention to something leaving, which is backwards.

Mix it far under dialogue. On the lower thirds it will be half-masked by speech and that is correct — it is felt, not heard. On the pull-quotes, which land over a silent reaction, it has room and will register properly.

⚠️ **Not a whoosh.** The same rule as `BRAND_subscribe`: a swoosh on a research-led show reads as a different channel. The paper identity gives a better answer than the generic one.

### `MUSIC_Outro_Bed` — under the transformation

The outro's picture is a five-second dissolve from photograph to drawing, a ~3-second clean hold, then the 20-second end card. The bed should be **already running** before the dissolve starts, so the transformation happens inside the music rather than being announced by it, and it should not resolve at the end — it decays.

**That makes the outro about 31 seconds, so the cue is 35 — not 60.** Corrected 2026-09-18. The
60-second figure was sized when this paragraph still said "a long hold under the credit roll", and
the credit roll was deleted further down this same file. **When a structural decision is reversed,
the numbers sized for it do not reverse themselves** — this cue was about to cost 750 credits for
music nobody would hear.

### What needs no sound

The reaction shots and the b-roll sit on generated ambience and the room-tone bed. Adding cues there is the reflex that makes an edit feel busy.

## `MUSIC_*` — six cues

**➤ Every prompt, with take counts and reject criteria, is in `Fixed_Assets/Audio/AUDIO_PROMPTS.md`.** That file is the one to work from at the keyboard; the table below is the summary.


**Licence is settled: ElevenLabs Starter ($6) lists "Commercial License" and "Music commercial use" as included.** Generate the whole set on that plan, in one session.

✅ **The licence survives cancellation — checked, not assumed.** ElevenLabs' own help documentation: *"Once your subscription ends, you will still have a commercial license to use whatever you generated during that subscription forever."* So the whole set can be generated on the $6 tier and the rights hold even if the plan is later paused or dropped.

⚠️ **The free tier is the opposite and the trap is permanent.** Audio generated outside a subscription *"will always require attribution"*, and ElevenLabs gives no guarantee it stays available. Nothing made on the free tier can be relicensed later — which is why the free-tier proving clip is a test artefact and must never reach a published part.

**Settled: the show runs DRY by default.** Music sits at structural points — the disclosure card, the intro, act transitions, the close — and a drone appears only where the content earns it. In a Part 1-sized part that is **two places**, both in the darkest material. Bedding every line is what the channels this show is defined against do; not doing it is a credibility signal the target audience reads immediately. If a dry stretch feels flat, that is a writing note, not a scoring one.

**Settled: low strings and struck metal.** Bowed double bass and cello holding quiet chords under a single struck metallic resonance that repeats slowly, like a clock mechanism — which also echoes the hourglass in the mark. Era-neutral by design, since the guest list runs from Cleopatra to Montezuma. Rejected: sparse piano (the default sound of documentary, reads as generic) and period instrumentation per guest (fights the deliberately era-neutral mark, and means new music for every episode instead of one fixed set).

**Rules for every cue, because they all sit under speech:**

- **No vocals. No strong melodic hook.** Anything singable competes with the dialogue for the same attention and wins.
- **No trailer percussion, no braams, no rising risers.** The show's positioning is research-led; epic scoring makes it look like the content it is trying not to be.
- **No solo piano documentary cliché either.** It is the other default and it is equally anonymous.
- **Mono-compatible.** Most of the audience is on a phone speaker.
- Generate each cue **longer than needed** and trim in the edit. Short generations loop audibly.

The palette that fits the brand — era-neutral, ink and paper, one warm accent — is **low bowed strings, a single struck metallic resonance, and air.** Nothing that places a century, because the guest list runs from Cleopatra to Montezuma.

| Cue | Length | Prompt |
|---|---|---|
| `MUSIC_Theme_Main` | 30s | *Sparse, restrained title music. Low bowed strings sustaining under a single struck metallic resonance that repeats slowly, like a clock mechanism. A sense of held breath and patience rather than drama. No percussion kit, no brass, no vocals, no melody that could be hummed. It pauses completely partway through, then returns on a single strong downbeat and resolves.* — **cut to the intro's beats, above** |
| `MUSIC_Sting_Transition` | 4s | *A single short low string swell with one struck metallic resonance over it, decaying into silence. No impact hit, no riser, no reverse cymbal. Restrained and dry.* |
| `MUSIC_Drone_Low` | 3 min | *A sustained low tension bed. Bowed double bass and cello holding a single quiet chord, almost static, with faint air movement underneath. No melody, no rhythm, no development. Designed to sit under speech without being noticed.* |
| `MUSIC_Drone_High` | 3 min | *A sustained bed of quiet tension, higher and thinner than a bass drone. Bowed strings holding a close, slightly unresolved interval, with faint metallic shimmer. No melody, no rhythm, no percussion. Unease held flat and steady, never rising to a climax.* |
| `MUSIC_Bed_Disclaimer` | 8s | *Neutral, quiet, unhurried. One sustained low string note and a single soft metallic tone, no movement, no drama, no emotion. It should sound like a room rather than like music.* |
| `MUSIC_Outro_Bed` | ~~90s~~ **35s** | *A quiet closing bed. Low bowed strings settling downward, a single struck metallic resonance fading slowly, air and space around it. Elegiac but not mournful — an ending rather than a loss. No melody, no percussion, no vocals, no swell.* |

`MUSIC_Bed_Disclaimer` matters more than its eight seconds suggest: the disclosure card must never play dramatic. A disclosure that sounds like a trailer reads as theatre about honesty rather than honesty.

---

## `SFX_*` — and the room tone that now carries the whole part

### `ROOMTONE_studio` — the most important audio asset in the project, and it is generated

**It got more important, not less.** ElevenLabs speech-to-speech resynthesises the voice rather than passing the source through, so the studio room tone **does not survive the pass** — measured, the converted floor is flat broadband dither at −86 dBFS against the source's structured −79 dBFS room. Without a continuous bed the part sounds vacuum-sealed.

**Generate it. Do not extract it.** An earlier version of this file said the opposite — extract it from real clips so it matches the studio the video model produces. That reasoning was stale, because **nothing in a finished part carries Kling's native studio tone anyway**:

| Layer | What its floor actually is |
|---|---|
| Dialogue | resynthesised by ElevenLabs — broadband dither, no room |
| Silent reactions | Standard 3.0 with audio **off** — no audio track at all |
| Silent wides | none — the wide clip was removed from the kit on 2026-09-18 |
| Generated b-roll | its own generated ambience, not the studio |

There is nothing to match. **The bed does not represent the room; it is the room.** Which means it can be generated now, on the subscription already paid for, with no dependency on having produced a part first — and it will be identical in every episode of the series instead of drifting with whatever the video model happened to produce that month.

**Prompt** (ElevenLabs Sound Effects):

```
Quiet empty interior room tone. A small carpeted room with soft furnishings and acoustic
panelling — close and dry, almost no reverb. A faint low hum of air handling underneath.
Completely steady and uneventful: no hiss, no traffic, no voices, no music, no clicks, no
movement, no birds, nothing that happens.
```

**The instruction that matters is "nothing that happens."** Any event in the bed — a click, a distant car, a creak — becomes a metronome the moment the bed loops, and a listener will find it long before they can say why the audio feels wrong.

**Build a long bed, not a short loop.** Generate **six takes at maximum duration**, discard any with an audible event, and crossfade the four cleanest into one long file:

```bash
# 4 takes -> one continuous bed with 3s crossfades
ffmpeg -i t1.wav -i t2.wav -i t3.wav -i t4.wav -filter_complex  "[0][1]acrossfade=d=3:c1=tri:c2=tri[a];   [a][2]acrossfade=d=3:c1=tri:c2=tri[b];   [b][3]acrossfade=d=3:c1=tri:c2=tri"  -ac 1 -ar 44100 ROOMTONE_studio.wav
```

Then loop *that* under the part with a long crossfade at the seam. A bed assembled this way loops far less detectably than a single short take repeated forty times.

**Level: around −60 dBFS RMS in the final mix** — roughly 40 dB below dialogue normalised to −19 LUFS. Present enough to glue the cuts, quiet enough never to read as hiss.

**The test for whether the level is right:** mute the bed and listen to a cut between two clips, then unmute it. The bed is correct when the cut stops being audible **and the bed itself still isn't**. If you can hear the bed on its own terms it is too loud; if the cut still ticks it is too quiet.

Laid under the **entire** part at a constant level, never ducking, running under held silences too — which is what makes a pause feel like a room instead of a dropout.

**Permanent asset.** Generate once, reuse in every episode forever. It is the single audio asset assembly cannot proceed without.

### The small set

Generated b-roll now runs on Turbo **with audio on**, so each cutaway carries its own ambience. That demoted most of the SFX list from required to optional.

| Asset | Status |
|---|---|
| `ROOMTONE_studio` | **required** — nothing assembles without it |
| `SFX_sand` | **required** — the intro plays without it, but thinly. See *Sound to picture*. |
| `SFX_plate` | **required** — one paper settle, used on every lower third and pull-quote entrance |
| `SFX_fire_crackle` | optional — fallback if the embers cutaway's generated track is thin |
| `SFX_wind` | optional — same, for the exterior cutaways |
| Outro dissolve | **no cue.** `MUSIC_Outro_Bed` is already running underneath; a sound on the transformation would announce it. |
| Movement foley | **do not generate.** Decision stands: generated foley varies clip to clip and is harder to cut around than silence. Place a movement sound only when a specific beat demands it. |

---

## Build order

**Nothing here is blocked on anything else.** The licence question is closed, and the room tone turned out to be generated rather than extracted, which removed the one item that had to wait for a finished part.

**Do the outro test first** (~43 cr, needs no produced episode) — it is the only item in this file whose format is unproven, and the fallback if it fails is free.

1. ~~`ROOMTONE_studio`~~ — **DONE.** Take 04, chosen by measurement, 1:48 seamless loop.
2. ~~`SFX_sand`, `SFX_plate`~~ — **DONE.**
3. ~~`MUSIC_Theme_Main`~~ — **DONE.** Take 01, cut to the opening's beats with the take's own outro
   spliced onto the end. The remaining five cues are still to make.
4. ~~`BRAND_bumper_in`~~ — **done**, and superseded by **`BRAND_opening.mp4`**.
4. The cards — motion graphics, no generation, no dependencies. Cheapest way to make an unfinished pipeline look finished.
5. The lower third and pull-quote plate — **treatment is settled and approved**; geometry, colours, texture and type sizes are all in `STUDIO_ASSETS.md`, with reference renders in `Branding/lowerthird_paper_*.png`.

`BRAND_bumper_out` is not in this list: it is built per part from a seed frame the part already has, so it belongs to production rather than to setup.

All of 1–3 are one subscription and one sitting.

**Still `PENDING` by design:** the thumbnail still prompt. Its structure is not settled and must not be invented per episode — test candidates against the criteria in the kit's Packaging section, then lock one prompt for every guest.
