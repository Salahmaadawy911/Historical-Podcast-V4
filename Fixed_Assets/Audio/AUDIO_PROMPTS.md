# Audio generation — every prompt, in order

All on ElevenLabs. **Commercial rights to anything generated during a paid subscription persist after it ends**, so this whole set can be made in one sitting and the rights hold permanently.

**Generate more takes than you need and throw most away.** Every cue below has a *reject* line — that is the part worth reading twice. A near-miss kept because it was expensive to make is how a series ends up with audio nobody likes.

---

## 0 · How generation actually runs — measured 2026-09-15

Generated through the ElevenLabs MCP, on the flow **"History Answers Back — fixed audio"**.

**Rates** (measured, not quoted):

| | credits/sec | notes |
|---|---|---|
| `eleven_text_to_sound_v2` (sfx) | **10** | max duration **30s**; has a `loop` flag |
| `eleven_music_v2` (music) | **25** | max duration **600s** |

Music is **2.5× the price of sound effects per second**. Every decision below about duration is a cost decision as much as a creative one.

**Parameters that matter:**

- **`loop: true`** on a sound effect returns a seamless loop. This *replaces* the old multi-take-crossfade method for room tone — one 30s looping take is better than four stitched ones, and cheaper.
- **`instrumental: true` + `lyrics_type: "instrumental"`** on music is far more reliable than writing "no vocals" in the prompt. Set both on every cue.
- **`prompt_influence: 0.5`** on sound effects. The 0.3 default drifts off-brief; 1.0 gets literal and harsh.

**Prompt style differs by model** — this is the thing most likely to be got wrong:

- **Sound effects want SHORT prompts.** One sentence, often a fragment. Name the sound, its texture, its space. Embellishment hurts.
- **Music wants 1–3 sentences** describing *sound* — genre, mood, instruments, tempo, production. For anything over a minute, say explicitly how the energy evolves (or that it must not).

**⚠️ Files cannot be pulled down automatically.** Generated audio sits behind signed Google Storage URLs that both the cloud workspace and the local shell are blocked from reaching by egress policy. This is an Anthropic-side restriction and cannot be changed from this end.

**The route that works:** audition on the flow page, click download — the files land in `~/Downloads`, which is connected to the session — then run

```bash
./intake.sh ROOMTONE_studio      # labels and files everything downloaded in the last 90 min
```

which copies them into `_raw_takes/` under a proper name. Everything after that is automated. Only the click is manual, so generate in batches and download in one pass.

**Concurrency:** a 12-generation run partly queues and retries itself. Not an error; just wait and re-poll.

---

## 0b · What format to save

**Take WAV every time it is offered — including on looping effects.** It removes a lossy
generation before YouTube's own encode, and it removes the 1152-sample MP3 head padding, which
means no trim step and nothing to forget.

⚠️ **The documentation says WAV export is available for non-looping effects only. That is wrong.**
Verified 2026-09-17: a sound effect generated with `loop` ON offered both WAV and MP3 on download.
Where the product and the docs disagree, believe the product — and check rather than quoting.

**Music offers WAV too** — the download menu's **Advanced** submenu carries the real list:
WAV (PCM / 48 kHz), MP3 192, MP3 128, MP4 (AAC), FLAC, OPUS. **Take WAV PCM 48 kHz.** FLAC is
equally lossless but has to be decoded; MP4 is a video wrapper for the waveform visual and is of
no use here.

| | format |
|---|---|
| every sound effect, looping or not | **WAV — Advanced → PCM 48 kHz** |
| every music cue | **WAV — Advanced → PCM 48 kHz** |
| Dialogue | MP3 — no WAV below the Pro tier |

Always open **Advanced**. The top-level menu offers a plain "WAV" but the submenu is where the
sample rate and bit depth are actually stated, and stating them is what makes a choice a decision
rather than a guess.

`ROOMTONE_studio` was built from MP3 before this was known. It is fine — the padding was trimmed
and measured — but a future rebuild should take the WAV.

**WAV arrives at 48 kHz; the project runs at 44.1 kHz.** Resampling happens on the way in — one
clean conversion, no decision needed at save time.

---

## 1 · `ROOMTONE_studio` — do this first

**Sound effects · 30s · `loop: true` · `prompt_influence: 0.5` · four takes.** Nothing assembles without it.

```
Quiet empty room tone, small carpeted room with acoustic panelling, close and dry with almost no reverb, faint low air-handling hum, completely steady and uneventful.
```

**Reject any take with an event in it** — a click, a distant car, a creak, a breath. An event becomes a metronome the moment the bed loops, and a listener finds it long before they can say why the audio feels wrong. "Completely steady and uneventful" is the load-bearing instruction.

Because `loop: true` returns a seamless take, **no crossfade assembly is needed**. Extend to any length by concatenation:

```bash
# 30s seamless take -> 10 minutes
for i in $(seq 20); do echo "file 'ROOMTONE_take.wav'"; done > list.txt
ffmpeg -f concat -safe 0 -i list.txt -ac 1 -ar 44100 ROOMTONE_studio.wav
```

**Level in the mix: around −60 dBFS RMS**, roughly 40 dB below dialogue normalised to −19 LUFS. The test: mute it, listen to a cut, unmute. It is right when the cut stops being audible **and the bed itself still isn't**.

---

## 2 · The six music cues

**`eleven_music_v2` · `instrumental: true` · `lyrics_type: "instrumental"`.** The palette is fixed for the series: **low bowed strings and a single struck metallic resonance** — era-neutral, because the guest list runs from Cleopatra to Montezuma.

**Applies to every cue, because they all sit near speech:**

- **No drum kit, no percussion loop.** Eleven Music adds a beat unless told not to.
- **No melody that could be hummed.** Anything singable competes with the dialogue and wins.
- **No trailer risers, no braams, no reverse cymbals. No solo piano** — the other anonymous default.
- **Mono-compatible.** Most of the audience is on a phone speaker.

**Generate short and loop where the cue allows it.** A cue whose brief is "never develops" is by definition loopable — generating three minutes of it is paying 25 credits a second for a model to repeat itself. Only cues that genuinely evolve are generated at full length.

### `MUSIC_Theme_Main` — four takes

```
Sparse cinematic orchestral title music at a very slow tempo, quiet and restrained throughout. Start with low bowed double bass and cello sustaining one quiet chord, with a single struck metallic resonance repeating slowly underneath like a clock mechanism. Build almost imperceptibly, then arrive on one clear struck downbeat — the single strongest moment in the piece — and let the strings resolve downward from it and decay into silence. No drums, no percussion loop, no piano, no brass, no risers, no hummable melody, no vocals.
```

**Only about 5 seconds of this is ever heard.** Per `SERIES_FURNITURE.md` the theme lives entirely
inside the bumper: in at 0.0, gap at 2.0–2.35, downbeat at 2.35, resolve to 4.15, decay to 5.0. It
does not continue past it. Length is therefore only about giving the model room to build a real arc
and giving the cut a choice of downbeats — **20 seconds is plenty**, and halves what 40 costs.

⚠️ **The timing cannot come from the prompt.** No music model will place a silence at 2.0s on
request. The arc comes from the generation; the timing comes from the cut. Pick the take with the
clearest single downbeat, land it on 2.35s, and **gap the music 2.0–2.35s rather than ducking it.**

**The edit-with-prompt feature is the one real lever on a near miss.** If a take has the right
character but the downbeat is weak, or a percussion part has crept in against the brief, an edit is
far cheaper than rerolling four fresh takes and keeps the take that already works. What it cannot
do is place a beat at a named second — that is still the cut's job.

### `MUSIC_Bed_Disclaimer` — 20s, two takes

```
Neutral ambient orchestral underscore, extremely slow and completely static. One sustained low bowed string note and a single soft metallic tone, with no development and no emotional arc across the whole piece. Dry modern production; no drums, no piano, no melody.
```

**Reject anything with a sense of occasion.** This plays under the AI-disclosure card, and a disclosure that sounds dramatic reads as theatre about honesty rather than honesty. Trim to 12s.

### `MUSIC_Sting_Transition` — 12s, four takes · **720 cr**

```
A single short low bowed string swell with one struck metallic resonance over it, decaying slowly into silence. Slow, dry and restrained cinematic transition; no impact hit, no riser, no reverse cymbal, no drums, no melody.
```

Used on the cut **into** each act-break study. Trim to 3–4s in the edit; generated long so the decay is complete. Cheap enough to take four — stings vary more between takes than any other cue, and at 12 s a take costs 180 credits.

### `MUSIC_Drone_Low` — **30s**, two takes · **looped in the edit** · **900 cr**

```
A sustained low cinematic tension drone at an extremely slow tempo. Bowed double bass and cello holding one quiet chord, almost completely static across the entire piece, with faint air movement underneath. The energy must never build or change; no melody, no rhythm, no drums, no development. Designed to sit unnoticed underneath speech.
```

Used **once** in a part — under the Pompey passage, and again under each act break. **Reject any take that develops**; if you notice it, it is wrong.

**30 seconds, not 45 — trimmed 2026-09-18.** A cue whose entire brief is *never develops* is loopable by definition, so the extra 15 seconds buys nothing that a crossfade does not, and costs 225 credits a take. Extend by crossfading the take against itself:

```bash
ffmpeg -i d.wav -i d.wav -filter_complex "[0][1]acrossfade=d=8:c1=qsin:c2=qsin" -ar 44100 drone_long.wav
```

⚠️ **`qsin`, not `tri`.** An earlier version of this line said `tri`. A drone crossfaded against
itself at an 8-second offset is effectively two uncorrelated signals, and a linear fade on
uncorrelated material dips about 3 dB in the middle of the join — the same equal-power rule the
room tone was assembled under. Longer fade than the room tone's because there is no transient to
hide behind: **8 s**, and it survives being run three times to reach two minutes.

### `MUSIC_Drone_High` — **30s**, three takes · **looped in the edit** · **1,350 cr**

```
A sustained bed of quiet orchestral tension, higher and thinner than a bass drone. Bowed strings holding a close, slightly unresolved interval with a faint metallic shimmer over it, held flat and steady for the full duration. The interval never resolves and the piece never climaxes; no melody, no rhythm, no drums.
```

Used **once** in a part — through the Actium sequence. Extend it with the same `qsin` crossfade as the low drone.

⚠️ **The old reject criterion — "reject any take that resolves" — is withdrawn. The brief was wrong, not the takes.** Measured 2026-09-18 across all three: every one is built on **A440 with its partials at octaves, fourths and fifths**. Those are consonances. The model does not produce a held dissonance from this wording, three attempts running, and take 02 came back as almost a bare octave — the furthest from the brief of the three.

**The correct reject criterion is the same as the low drone's: reject any take that develops.** Dissonance is not required and should not be chased. Two reasons. First, this file already forbids risers, braams and anything with a sense of occasion, and a deliberately uneasy cue at Actium is the same error as a dramatic disclosure — it tells the viewer how to feel about material that is doing that work itself. Second, the two drones are already distinct **by register**, which is what actually separates them in the edit: measured spectral centroid **2,961 Hz against the low drone's 1,187 Hz**. A thin, high, quiet bed feels different from a low one without needing a dissonant interval.

**If a cut ever does want the tension, it costs nothing.** Mixing the take against a copy of itself detuned **+25 cents** gives beating at about **0.25 Hz** — one slow pulse every four seconds. Tested and kept as `_raw_takes/DRONE_HIGH_detune_test.wav` (as generated, then +25, +50 and +100 cents). It was **not** used: judged by ear, the plain take reads as calm and the detuned ones read as out of tune rather than uneasy. The trick stays on the shelf, reversible, needing no credits.

### `MUSIC_Outro_Bed` — **35s**, **two takes** · **not looped** · **1,050 cr**

```
A quiet elegiac orchestral closing bed at a very slow tempo. Low bowed strings settling downward, a single struck metallic resonance fading slowly, with air and space around it. The energy decays gradually across the whole piece rather than building, and it fades out rather than resolving; no swell, no climax, no drums, no melody.
```

**Two takes, not three.** It is the one cue whose brief is unambiguous — decay, don't resolve — so the third take was buying choice rather than insurance, at 900 credits. It is also the one cue that genuinely evolves, so it is generated at length rather than looped. It must be **already running** before the outro transformation begins, so the change happens inside the music rather than being announced by it, and it **decays rather than resolving** — it carries the held drawing and the end card after it.

**35 seconds, not 60. Trimmed 2026-09-18 — 750 credits.** The outro is about **31 seconds**
end to end: the bed already running before the dissolve ~3s, the transformation 5s, the drawing
holding clean ~3s, the end card 20s. The 60-second figure was sized for a **credit roll**, and the
credit roll was later deleted (`SERIES_FURNITURE.md`: a one-person channel rolling credits reads as
performing a scale it does not have). The cue length outlived the structure it was written for.

**Why 35 and not 30.** Thirty leaves nothing on a 31-second requirement and no freedom about where
in the take to start; four seconds of headroom costs 60 credits. Anything longer is paying for
music nobody hears.

⚠️ **A 35s take decays faster than a 60s one.** Same brief, less time to spend it in, so the
settling is audible rather than imperceptible. For an ending that is probably an improvement — but
it is a genuine change of character, and the takes should be judged on it.

⚠️ **Two stale "credit roll" references survive in `SERIES_FURNITURE.md`** (in the `BRAND_bumper_out`
build steps and its test criteria). They are what made this figure wrong. Fixed 2026-09-18 — but the
lesson stands: when a structural decision is reversed, the numbers sized for it do not reverse
themselves.

---

## 3 · The two effects

### `SFX_sand` — sound effects, **12s, `loop` ON**, prompt influence 0.6, four takes

```
A thin steady stream of fine dry sand pouring onto paper, close-mic, granular and continuous, very quiet, no reverb.
```

**Reject anything that sounds like a rainstick, a shaker, or rain.** One thin stream, not a mass of grains. Close, not in a space.

⚠️ **`loop` must be ON, and this is not about looping.** A normal generation arrives with silence at the head and its own fade in and out — `SFX_plate` came back with **1.15 seconds of silence before the sound**. This cue has to start on an exact frame and stop dead on another, so what is needed is a *continuous texture with no beginning and no end*, which is precisely what the loop flag produces. Generate long and cut the piece you need out of the middle.

**Word the prompt as a state, not an event.** "A stream pouring" is a texture; "sand falling onto paper" invites the model to write a little scene with a start and a finish. That difference is the whole reason for the reject rule below.

---

## The intro bumper, sound to picture

Timings read straight off `intro_source/intro_build.py`, so they are exact rather than eyeballed. Total 5.00s at 24 fps.

| time | picture | sound |
|---|---|---|
| 0.00–0.35 | symbol fades up | music only |
| **0.35** | sand begins to fall | **`SFX_sand` in**, no fade — it is already running |
| 0.35–2.00 | the fall, 1.65s | steady stream |
| **2.00** | sand stops, held full | **hard cut. No fade.** Music gaps here too |
| 2.00–2.35 | the hold, 0.35s | **nothing.** This silence is the whole effect |
| **2.35** | the reversal | **music's swell lands · `SFX_sand` reversed, in** |
| 2.35–3.10 | sand runs back up, 0.75s | reversed stream |
| **3.10** | sand gone, top bulb full | reversed stream cuts off |
| 3.20–4.15 | symbol shrinks into the lockup | — |
| **4.15** | it lands | **`SFX_plate`**, well under the music |
| 3.70–4.30 | wordmark fades in | silent — fading type must not tick |
| 5.00 | end | |

**The return is faster than the fall** — 0.75s against 1.65s. Cut a different slice for it rather than reversing the same one; the same texture backwards at the same speed reads as a tape trick, a fresh slice reads as sand.

**Nothing extra marks the reversal at 2.35s.** It is tempting to put a thud or a riser there. It already carries the music's only swell, the return of the sand, and 0.35 seconds of prepared silence in front of it — a fourth element would be the one that turns a held breath into a stinger.

**`SFX_plate` does the landing at 4.15s.** It is the same paper-settle used on the lower thirds, which is the point: the brand's sound vocabulary is paper, and hearing it here and again on every name card is what makes it a vocabulary rather than a collection of noises.

### `SFX_plate` — sound effects, 3s, four takes

```
A single sheet of paper laid flat onto a wooden desk, one soft settle, close-mic and dry, no reverb.
```

**Entrance only** — lower thirds and pull-quotes. **Exits are silent**: a sound on the way out draws attention to something leaving, which is backwards.

⚠️ **Not a whoosh.** A swoosh on a research-led show reads as a different channel entirely. **Reject any take with movement through air in it** — this is a settle, not a slide. Mix far under dialogue; on the lower thirds it will be half-masked by speech and that is correct.

---

## 4 · Optional, only if a beat needs it

Generated b-roll now carries its own ambience on Turbo, so these are fallbacks rather than requirements. **Do not generate them speculatively** — wait until a specific cutaway comes back thin.

**`SFX_fire_crackle`**

```
Close fire embers crackling and settling, low and irregular, no roar and no wind, quiet and intimate, no reverb.
```

**`SFX_wind`**

```
Steady low wind across open ground, continuous and even, no gusting, no whistling, no trees, no voices.
```

**Movement foley: do not generate.** It varies clip to clip and is harder to cut around than silence. Place a movement sound only when a specific beat demands it.

---

## Order of work

1. **`ROOMTONE_studio`** — **DONE 2026-09-17.** Take 04 chosen by measurement, not by ear.

   All four takes were indistinguishable to listen to — which is correct, a room tone that is
   audible in isolation is too loud. They were separated on numbers instead:

   | take | level | sharp transients | drift over 30s | shape |
   |---|---|---|---|---|
   | 01 | −59.1 dB | 60 | −1.1 dB | dips hard at the end |
   | 02 | −62.8 dB | 94 | −0.9 dB | 3.7 dB quieter than the rest |
   | 03 | −59.1 dB | 43 | **+1.7 dB** | rises steadily — bad to loop |
   | **04** | **−59.5 dB** | **27** | **−0.4 dB** | **flat, no trend** |

   "Sharp transients" counts 20 ms windows jumping more than 8 dB — the events that become a
   metronome once a bed loops. Take 04 has less than half of what any other take has, and the
   least drift, so its loop point is the least conspicuous.

   **The asset:** `ROOMTONE_studio.wav` — mono, 44.1 kHz, **1:48**, level −59.6 dBFS. Built as a
   27 s seamless unit repeated four times, so the file loops end-to-end as well as internally.
   The head padding was trimmed before assembly and the joins are equal-power crossfades: measured
   sample step at each join is 2 counts against a typical 1, so there is no click.
   Raw takes kept in `_raw_takes/`.
2. **`SFX_plate` — DONE.** Take 3 chosen. Raw in `_raw_takes/`, working asset `SFX_plate.wav`:
   mono, 44.1 kHz, **0.75 s**, peak −9.8 dBFS, transient at the head.
   ⚠️ The raw take had **1.15 seconds of silence before the sound**. Every generated effect must be
   checked for this and trimmed to its transient — an entrance cue whose hit is a second late is
   useless, and the delay is invisible until measured. This is what the `loop` flag on the sand is
   there to prevent.

3. **`SFX_sand` — DONE 2026-09-17.** Take 02, chosen by measurement.

   | take | level | wobble | macro span | loop seam |
   |---|---|---|---|---|
   | 01 | −30.4 dB | 3.11 dB | 7.15 dB | +0.11 dB — collapses 5.4 dB at the end |
   | **02** | **−28.2 dB** | **1.13 dB** | **2.57 dB** | **+0.06 dB** |
   | 03 | −32.9 dB | 3.49 dB | 9.17 dB | +2.92 dB — swells 8 dB at the start |
   | 04 | −35.7 dB | 2.80 dB | 5.73 dB | −0.04 dB |

   "Macro span" is the spread across 1.5 s blocks — how much shape the texture has of its own. Take
   02 is three times flatter than anything else and has the tightest loop seam, which is exactly
   what a cue that gets cut at two exact frames needs. L/R correlation **+0.998**, so it is a point
   source rather than a diffuse field — close-mic, as asked — and folding to mono loses nothing.

   **`SFX_sand.wav`** — mono, 44.1 kHz, 6 s cut from the flattest stretch (4.5–10.5 s). The
   general-purpose source.

   **`BUMPER_sand.wav`** — mono, 44.1 kHz, **exactly 5.00 s, laid to the bumper**: silent to 0.35,
   fall to 2.00, dead stop, silent to 2.35, reversed return to 3.10, silent to the end. Drop it at
   0.00 and it lines up. Verified by measuring the finished file, not by trusting the arithmetic.

   Two things done deliberately: the fall and the return are cut from **different stretches** of
   the take — the same texture backwards at the same speed reads as a tape trick — and every edge
   carries a **3 ms fade**, short enough to still read as a dead stop, long enough to stop a noise
   texture clicking when it is cut mid-waveform.
4. **The music cues — ALL DONE 2026-09-18.** Six were specced; four were built and two were killed
   (`MUSIC_Bed_Disclaimer`, `MUSIC_Sting_Transition`), each replaced by something the theme was
   already doing. **The audio set is complete.**

   **`MUSIC_Theme_Main` — DONE 2026-09-17.** Take 01. Also yields `MUSIC_Theme_teaser_loop.wav`,
   the 4.0 s unit that now carries the opening, the teaser *and* the act break.

   **`MUSIC_Drone_Low` — DONE. Take 01, and it was not close.**

   | take | flat-window sd | span | slope | fundamental | interval |
   |---|---|---|---|---|---|
   | **01** | **1.70 dB** | **5.98 dB** | **−0.16 /10s** | **82 Hz, wanders 21 cents** | **stable fifth, sd 7 cents** |
   | 02 | 4.32 dB | 20.01 dB | **+3.50 /10s** | 74 Hz | jumps, sd 164 cents |

   Take 02 rises three and a half decibels every ten seconds, which is the reject criterion in
   plain sight: it develops. **Asset:** 24 s unit cut 2.5–26.5 s, normalised to −30 dBFS RMS, plus
   a 72 s `_long` version built with the 8 s `qsin` crossfade.

   **`MUSIC_Drone_High` — DONE. Take 03**, chosen on the lowest periodic pulsing (0.127 against
   0.178 and 0.170) and the steadiest partials. **Asset:** 24 s unit cut 4.0–28.0 s, normalised to
   −30 dBFS RMS so it sits at the same working level as the low drone despite arriving 24 dB
   quieter, plus a 72 s `_long`. See the withdrawn reject criterion above — this cue is consonant
   by decision now, not by accident.

   **`MUSIC_Outro_Bed` — DONE. Take 01.** Take 02 has no shape at all (−48, −36, −32, −38, −25 …).
   Take 01 has exactly the arc the outro needs: a slow rise to a centre at 14–16 s, then a clean
   monotonic decay to nothing. **Asset:** cut in at source 10.0 s and run to the end — 25 s, peak
   −6 dBFS, profile −22 → −16 at the centre → −66 at the tail.

   ⚠️ **The in-point is load-bearing.** Cutting at 10.0 s puts the cue's loudest moment **1–3
   seconds into the transformation**, which is where the show's thesis lands. Move the in-point and
   the peak drifts onto the end card instead. Consequence to know: the **last ~6 s of the 20 s end
   card sit in silence**, which is intended — the show ends and the card holds for the end screens.
   If that ever feels wrong, trim the card to ~15 s rather than re-cutting the music.

5. Nothing else unless a specific beat asks for it.

**Keep every raw take**, not just the chosen one. If a cue is ever re-cut, the alternates are worth more than the prompt.

## Batch processing once files are downloaded

```bash
# strip ElevenLabs' 1152-sample MP3 head padding, normalise, convert
for f in *.mp3; do
  ffmpeg -i "$f" -af "atrim=start_sample=1152,asetpts=PTS-STARTPTS,\
loudnorm=I=-19:TP=-1.5:LRA=7" -ar 44100 -c:a pcm_s16le "${f%.mp3}.wav"
done
```

Music and effects are **not** loudnorm'd to −19 — that value is for dialogue. Beds and effects are levelled by ear against the dialogue bus.
