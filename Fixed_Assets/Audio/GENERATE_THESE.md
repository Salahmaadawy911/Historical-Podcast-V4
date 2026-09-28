# Generate these — **nothing left. The audio set is complete.**

**Closed 2026-09-18.** Every cue and effect this show needs is built and sitting in
`Fixed_Assets/Audio/`. Keep this file as the record of what was made and what was killed; the
prompts, measurements and reject criteria live in `AUDIO_PROMPTS.md`.

## What exists

| asset | source | note |
|---|---|---|
| `ROOMTONE_studio.wav` | take 04 | mono, 1:48, −59.6 dBFS, seamless |
| `SFX_sand.wav` | take 02 | 6 s, the flattest stretch |
| `SFX_plate.wav` | take 3 | 0.75 s, trimmed to its transient |
| `MUSIC_Theme_Main.wav` | take 01 | the title music |
| `MUSIC_Theme_teaser_loop.wav` | cut from the above | **4.0 s.** Carries the opening, the teaser *and* the act break |
| `MUSIC_Drone_Low.wav` + `_long` | take 01 | 24 s unit, −30 dBFS RMS |
| `MUSIC_Drone_High.wav` + `_long` | take 03 | 24 s unit, −30 dBFS RMS |
| `MUSIC_Outro_Bed.wav` | take 01 | 25 s, peak −6 dBFS, in-point is load-bearing |

## What was killed, and what replaced it

**`MUSIC_Bed_Disclaimer`** — the disclosure card sits on the theme's own decay between clock
strikes. A second cue under it was fighting the first.

**`MUSIC_Sting_Transition` — 720 credits saved.** Its only job was the cut into the act break, and
the break now opens and closes on the theme's own strikes. Same instrument, so the break belongs to
the same piece instead of sounding like a cue laid over it.

**Both were replaced by something the theme was already doing** — which is the pattern worth
remembering. Twice, a cue specced as a separate generation turned out to be a cut of one that
already existed. Before commissioning a new cue, check what the theme already contains.

## What the spend actually was

Specced at nine items. Six music cues at full length would have run **~9,800 credits**; the set as
built came in at **~4,300**, and two of the cues that survived were shortened after their runtime
was checked against the picture rather than assumed. **The drones were specced at 45 s and the outro
bed at 60 s** — the drones because "never develops" is loopable by definition, the outro because it
was sized for a credit roll that had been deleted elsewhere in the docs.

⚠️ **The standing lesson: when a structural decision is reversed, the numbers sized for it do not
reverse themselves.** Both of those overruns were stale figures, not bad judgement, and neither
looked wrong on its own.

## If a cue is ever re-cut

**Every raw take is kept in `_raw_takes/`**, including the rejected ones — the alternates are worth
more than the prompt. Also there: `DRONE_HIGH_detune_test.wav`, an unused, zero-credit way to put
beating into the high drone if a cut ever wants tension it currently does not have.

**Extending the drones:**

```bash
ffmpeg -i d.wav -i d.wav -filter_complex "[0][1]acrossfade=d=8:c1=qsin:c2=qsin" -ar 44100 drone_long.wav
```

`qsin`, not `tri`: at an 8-second offset a drone against itself is effectively uncorrelated, and a
linear fade on uncorrelated material dips about 3 dB in the middle of the join. Same equal-power
rule the room tone was assembled under. Run it three times over to reach two minutes.
