# Voice Registry — ElevenLabs

> 📚 Cleanup 2026-09-28: current registry and settings. The two corrected rules below (accent, host similarity) keep
> their short history on purpose — both were intuitive, both were wrong, and both cost a round of testing.

Voice is created once per character and never re-created. The ElevenLabs **voice ID** is the
canonical identity; the prose description in `STUDIO_ASSETS.md` now only shapes the *source*
performance Kling generates, which speech-to-speech then re-timbres.

**Create every voice on the paid plan.** Free-tier output carries no commercial licence and
cannot be relicensed later.

Record the voice ID here the moment a voice is accepted. A voice without its ID recorded is a
voice that will be re-created differently in six months.

| Character | Voice ID | Status |
|---|---|---|
| Host | `FgXTns6rcAlMbBOnz3nB` | **DONE.** Permanent, series-wide — instant clone, recorded in Egyptian Arabic. Settings settled 2026-09-18, same as every other voice. |
| Cleopatra VII | `xMytukqVLj8LlL1L1sOo` | **DONE 2026-09-18.** Fixed from Mode 2 casting through both parts. Seed not recorded — the web UI does not expose it; see below. |

---

## Host — how to record the clone

**Decided:** the host is an **instant clone of your own voice, recorded speaking Egyptian Arabic**,
then used normally to speak English. The design prompt below is kept only as a fallback if the
clone is ever abandoned.

What to record:

- **1 to 2 minutes. Never more than 3** — longer recordings make the clone *worse*, not better.
- **Speak Egyptian Arabic.** A clone carries the colouring of whatever language it was recorded in,
  and that colouring is the point.
- **Export MP3 at 192 kbps or higher.** WAV gives no improvement.
- **Level it to roughly −20 dB RMS, peaks no higher than −3 dB.** This is the one number worth
  getting right.
- One consistent tone all the way through — the way you would actually host, not a performance.
  The model copies everything it hears, breathing and mouth clicks included.
- Nothing else in the recording: no music, no second voice, no long gaps.

Say ordinary connected sentences, not a word list. Content does not matter; consistency does.

~~Then in `voice settings`, similarity has to be tuned by ear on a test clip.~~ **No tuning needed.
Tested 2026-09-18 and the result was null — see "The host is not an exception after all" below.
The host uses the same settings as every other voice.**

## Host — design prompt (fallback only)

Permanent for the life of the series. Everything else is replaceable; this is not.

```
Native English, neutral international — not placeable as British or American. Male, early forties. Perfect audio quality.
Persona: curious interviewer, thinking aloud. Emotion: warm, measured, unhurried.
A warm mid-baritone sitting low and even, with a dry edge and a little gravel at the bottom of
the register that shows on longer vowels. Conversational rather than broadcast-polished —
comfortable with pauses, never announcing, no radio gloss, no smile in the voice, no upward
inflection at the ends of sentences.
```

⚠️ The language and regional variant lead this prompt deliberately. ElevenLabs' documentation is
explicit that stating them late lets the voice drift mid-generation — see `skill_elevenlabs.md`
§3a. Do not move them to the end for readability.

**Judge it on:** does it sound like a person interested in the answer, or like a presenter?
The whole show rests on the first one.

## Cleopatra VII — design prompt

Fixed from casting through both parts.

**Paste as one block. 559 characters — inside the 20–1000 limit.**

```
Native English, placeless and formal — neither British nor American, not placeable to any country. Female, mid-thirties. Perfect audio quality.
Persona: royal diplomat, trained orator. Emotion: composed, wry, watchful.
A low even alto, precise and economical, with very little movement in pitch and a dry edge under the composure. Measured, deliberate delivery that closes each clause fully — the cadence of someone accustomed to being listened to and never hurried. Controlled and authoritative rather than warm; never breathy, never pleading, never girlish.
```

⚠️ **One fault fixed, 2026-09-18: the dialect had drifted to the last line.** The previous version
ended *"Placeless formal English, neither British nor American."* The docs are explicit that naming
the language or variant late makes the voice **drift mid-generation** — the model weights what it
reads first. It is now in the opening sentence, where it belongs, and the trailing line is gone.

### Preview text

**283 characters — so one generate call costs 283 credits and returns three previews.** Over the
100 minimum by a comfortable margin, and cheap enough that a reroll is not a decision.

```
You assume those were two things. For me they were one. Egypt did not survive without me, and I was nothing without it. I was not a girl who charmed a general. I was a head of state with one army, one harvest and a great many creditors, and I spent all three the way any ruler would.
```

It opens on `P1_057`, the line the whole part turns on, so the audition tests the exact thing that
has to work rather than a neutral sample. The rest gives her a longer breath, a list to keep flat,
and a dry close — all things the description claims and none of them labels. **Preview text is a
performance script, not a restatement of the description.**

### Settings for the call

| setting | value | why |
|---|---|---|
| `guidance_scale` | **leave at the default (5)** | The description is long and specific, which is exactly what low guidance wants. High guidance makes voices sound artificial, and that would be baked into 30+ clips permanently. Raise it in steps **only** if all three previews ignore the description. |
| `loudness` | **default, ignore it** | Erased downstream — the pass lands ~10 LUFS low and Mode 6 normalises every clip. |
| `quality` | **default for the first call** | Higher quality means **less variety between the three previews**, and those three are the whole audition. Raise it only once one preview is nearly right. |
| `seed` | ~~write it down~~ **not available** | The API exposes it; **the web Voice Design UI does not.** Checked 2026-09-18 — do not go hunting for it again. See the note below on what that costs. |
| `model_id` | `eleven_multilingual_ttv_v2` (default) | `eleven_ttv_v3` exists and is untested; a once-only permanent asset is a bad place to try an unknown. |

### No seed — what that actually costs, and the mitigation

The web UI does not show the seed, so **this voice cannot be regenerated from parameters.** It
exists only as the saved voice in the account. That is a smaller problem than it sounds, because
the voice ID is the durable handle and the ID is recorded — but it does mean the failure mode is
**deletion, not drift**.

Three things follow:

1. **Never delete the voice**, and never "clean up" the voice library to free a slot. A deleted
   designed voice with no seed is unrecoverable, and it carries both parts of this arc.
2. **Keep a reference render.** Generate the preview paragraph once in the finished voice and store
   it as `Episodes/Cleopatra/VOICE_cleopatra_reference.mp3` (**done 2026-09-23**, 12.1 s; per-guest assets live in the guest's folder). If the voice is ever lost,
   that file is the only way to judge whether a re-design lands in the same place — and it turns an
   unanswerable question into an A/B.
3. **The description and preview text above are the re-design recipe.** They are recorded verbatim
   for exactly this reason. A re-design from them will not be identical, but it will be close, and
   without them it would be a fresh casting session.

**Use the API instead of the web UI for any future guest**, if the seed matters enough. It returns
the seed; the UI does not. That is the one concrete reason to prefer the API for voice design.

**Accent decision, defended.** Placeless formal English, deliberately. Two defaults rejected:
a modern Egyptian voice is simply wrong — she was Ptolemaic Greek, and the Egypt she ruled was
not the Egypt of today; and clipped Received Pronunciation is the documentary cliché that makes
every ancient figure sound like the same BBC narrator. Placeless is the honest answer and needs
no apology.

**Judge it on:** could this voice deliver *"You assume those were two things. For me they were
one."* without either pleading or sneering? That is the register the whole part turns on.

---

## Rules

- **One voice per character, created once.** Re-creating a voice mid-series is the drift the
  whole pipeline was built to prevent.
- ⚠️ **Accents live in the KLING prompt, not here. This rule was backwards — corrected
  2026-09-18.** It used to read "accents live here, not in the Kling prompt." The host test
  disproved it: accent is carried by phonetics — vowel targets, consonant realisations, rhythm —
  and speech-to-speech takes all of those from the **source read**, which is the Kling clip. The
  ElevenLabs voice contributes timbre. That is precisely why a clone recorded in Egyptian Arabic
  returns native English: the source read was native English.

  **So whatever accent Kling generates is the accent that reaches the cut.** The design prompt
  still describes the voice's colouring, because it shapes timbre and costs nothing to state — but
  it cannot override the source.

  ✅ **Resolved 2026-09-18 — placeless wins, and it now lives in the Kling prompt.** The Part 1
  shot prompts used to carry `Voice: … A light classical Mediterranean colouring over otherwise
  clear English`, which contradicted this file's defended accent decision. Under the corrected rule
  the Kling line is what reaches the cut, so the kit would have produced the very accent the
  decision rejects — a modern-Egyptian-adjacent colouring for a Ptolemaic Greek ruler — and
  "classical Mediterranean" is also the kind of vague descriptor §3a of `skill_elevenlabs.md` lists
  as damaging.

  **All 32 of Cleopatra's `Voice:` blocks in `P1_kit.md` now read:**

  ```
  Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.
  ```

  The host's 34 blocks were already correct — *"Clear neutral international English, no regional
  accent"* — and were not touched. The wording now matches the ElevenLabs design description word
  for word, which is the point: **the Kling block decides the accent, the design description decides
  the timbre, and they must never disagree.**
- **Every talking clip goes through the pass** — audio-only (720p) clips included; ~90 in a Part 1-sized part.
  Reactions are silent and skip it; b-roll has no dialogue. Folders: `voice_folders.py` (Mode 6).
- **Keep the unprocessed generation.** Store the raw Kling clip alongside the voice-changed
  one. If a voice is ever re-designed, the raw clips can be re-processed; a discarded original
  means regenerating video.
- **Pace belongs here, not in the Kling prompt.** ElevenLabs' Voice Design format includes
  pacing as an attribute and uses it well. The prose description in `STUDIO_ASSETS.md` must
  still carry **no** pace language, because there it would fight the clip duration for control
  of the same thing and the duration is exact. Same voice, two artefacts, opposite rules.
- **The designed voice is a voice-changer TARGET, never a text-to-speech source.** Generating a
  line as TTS discards the Kling performance and the lip-sync with it.

---

## Locked settings

Applied to every conversion. Recorded here so a clip generated in six months matches one
generated today.

| Setting | Value | Why |
|---|---|---|
| Model | **Eleven Multilingual v2** | Tested against English v2 on the host clone: **no audible difference.** Multilingual wins the tiebreak because the scripts are full of non-English proper nouns — Ptolemy, Actium, Pompey, Montezuma — and an English-only model is likeliest to mangle exactly those. That is a reasoned tiebreak, not a measured result. |
| Stability | high | 65+ clips have to match each other |
| Style Exaggeration | **0–10** | speech-to-speech already carries an approved performance; style invents delivery on top of it and is the documented source of instability |
| Similarity | **high — for every voice, host included** | see below; the host exception was tested and did not exist |
| Remove Background Noise | OFF | nothing to preserve either way — see the room-tone measurement below |
| Speaker Boost | ON | Tested on and off: **no audible difference.** Left on because the file already said so and nothing argues against it. |
| Output format | **MP3 44.1 kHz 128 kbps** — the only option on the Starter tier | WAV/PCM is not available here, so the head-padding artefact below is unavoidable and **the 1152-sample trim is a required step, not a fallback**. Accept one lossy generation before YouTube's encode; at 128 kbps on speech it is not the weak link. |

### The host is not an exception after all — **tested 2026-09-18, result null**

This file used to say the host needed a lower Similarity than the guests, because his clone was
recorded in Egyptian Arabic and Similarity would drag that accent through with the timbre.

**Tested across Similarity settings, Speaker Boost on and off, and both Multilingual v2 and
English v2: no audible difference on any axis.** In every combination the English reads as native
and the voice is still recognisably his — which is the wanted outcome, at every setting.

**The prediction was wrong, and this is the second time the same prediction has failed.** The first
was the assumption that an Egyptian-Arabic source recording would colour the English output; it did
not. Same underlying error both times, and the mechanism is now clear enough to state properly:

> **Accent lives in phonetics — vowel targets, consonant realisations, rhythm — and
> speech-to-speech takes all of those from the source read. The target voice contributes timbre.
> Similarity moves timbre, so it cannot move accent.** The old reasoning had the slider controlling
> something it does not touch.

⚠️ **Do not re-derive the old rule.** It is intuitive, it sounds mechanically plausible, and it has
now cost two rounds of testing. The host uses the same settings as everyone else.

| | Similarity |
|---|---|
| Designed guest voices | high |
| Host clone | **high — same as the guests.** Settled by test, not by tuning. |

---

## Measured behaviour of the pass

All three measured on a real Kling clip against its converted output. They are properties of
the tool, not of one clip, and Mode 6 acts on all three in a single batch step.

**Timing: the speech is sample-aligned. The apparent offset is a container artefact — and on this tier it is permanent.**
The MP3 export runs **exactly 1152 samples long — one MP3 granule, 26.1 ms** — written as head
padding without gapless flagging, so decoders play it as leading silence. Strip those samples
and the lag is **exactly 0 ms**, with envelope correlation unchanged (0.887 → 0.888, nothing
clipped off the speech). Control: round-tripping the source through identical MP3 settings in
ffmpeg shifts by 0 ms, so this is specific to how ElevenLabs writes the file. Deterministic on
every clip regardless of length or content. **Do not slip clips on the timeline** — that would
be treating a file-format quirk as a performance problem, 66 times over.

**The Starter tier offers MP3 44.1 kHz 128 kbps and nothing else**, so there is no WAV escape
hatch: every clip arrives with the padding, every time. The trim is therefore a standing
pipeline step in Mode 6, not a conditional one. It costs nothing — it rides in the same ffmpeg
pass as the loudness normalisation.

**Level: about 10 LUFS below source.** Source −23.6 LUFS / −5.1 dBTP; converted −34.0 LUFS /
−15.6 dBTP, with Speaker Boost already on. Headroom rather than a fault, but the offset is not
guaranteed constant across clips, so Mode 6 normalises rather than applying a fixed gain.

**Room tone does not survive the pass.** Speech-to-speech resynthesises the voice; it never
passes the source signal through, which is why "Remove Background Noise: off" preserves
nothing — there is nothing to preserve. Source floor −79 dBFS, centroid 950 Hz, 58% of energy
in 120–500 Hz: a structured room. Converted floor −86 dBFS, flat at 17–22% across every band,
centroid 3417 Hz: broadband dither. Both are below audibility, so there is no pumping at the
cuts — but it means **no clip has an acoustic floor at all**, which is why the room-tone bed in
Mode 6 runs under everything rather than only under the joins.
