# ElevenLabs — the working manual for this series

Everything the show needs to know about ElevenLabs, in one place. Read this before designing a
voice, generating audio, or changing the account tier. Researched against the official docs
2026-09-15; measured figures come from this project's own runs and are marked **[measured]**.

Where the docs contradict themselves — and they do, in several places — that is flagged rather
than smoothed over. Where a number is not published anywhere, that is flagged too. **Do not
invent a figure to fill a gap here.**

---

## 1 · The tier decides more than the budget

| Tier | Price | Credits/mo | What it unlocks |
|---|---|---|---|
| Free | $0 | 10,000 | **No commercial licence.** Unusable for this. |
| **Starter** | **$6** | **30,000** | Commercial licence. **MP3 128 kbps max.** |
| Creator | $22 | 121,000 | MP3 192 kbps. 1 Professional clone slot. |
| Pro | $99 | 600,000 | **44.1 kHz PCM/WAV** — the first lossless tier. |

**This project is on Starter, and that is why the MP3 trim rule exists.** Lossless output starts
at Pro ($99). At Starter every asset arrives as a 128 kbps MP3, which means every asset carries
LAME encoder padding, which is the **1152-sample head offset** already measured and corrected
for in Mode 6. That rule is not a workaround for a bug — it is the permanent consequence of the
tier, and it disappears only at Pro.

**⚠️ Starter includes only ~3 minutes of music generation per month.** The series' music set is
**complete** (five cues; `NEXT_STEPS.md` A9) — the masters and every alternate take are archived in
`Fixed_Assets/Audio/` and `_raw_takes/`. Never regenerate a cue casually.

**Commercial rights survive cancellation.** Official: "you will still have a commercial license
to use whatever you generated during that subscription forever." The licence attaches to the
moment of generation, not to the current plan. Two consequences:

1. Anything generated **outside** a subscription period requires attribution forever. Never let
   the subscription lapse mid-production and keep generating.
2. ElevenLabs does **not** guarantee permanent hosting. **Download and archive every master.**
   The canvas is not storage.

---

## 2 · Credit rates — measure, don't quote

**Plan with the rates shown in the account's own generation screens.** These are the numbers that
match what actually gets deducted:

| | **Account rate — use this** | Documented | `estimate_only` said |
|---|---|---|---|
| **Music** | **900 credits/min = 15/sec** | not published | 25/sec |
| **Sound effects** | **12 credits/sec** | 40/sec | 10/sec |
| TTS | 1 credit/character | 1/character | — |
| Speech-to-speech | 1,000 chars per minute of audio | — | — |
| **Voice design** | **charged once per design, on the preview text** | 1 credit/char | — |

⚠️ **Three sources give three different numbers and the discrepancy is unexplained.** ElevenLabs
says API generations are discounted against website generations but never publishes the factor.
Until that is pinned down: **budget with the account rate** (the highest realistic figure), treat
`estimate_only` as a sanity check rather than a quote, and ignore the documented 40/sec entirely —
nothing observed has come close to it.

The operative facts:

- **Music costs about 1.25× what sound effects cost, per second** — and music cues are far longer
  than effects, so music is where the budget actually goes. Every duration decision is a cost
  decision.
- **Voice design is cheap and once-only.** One call returns three previews for a single charge
  based on the preview text, so a 400-character preview costs roughly 400 credits per guest —
  a rounding error against a 30,000-credit month. There is no reason to skimp on preview length,
  and every reason not to: longer previews produce more stable voices.
- **`estimate_only` prices a run for free.** Always run it before spending, but read it as a rough
  floor, not a promise.

---

## 3 · Voices

### 3a · Voice Design — how guests are cast

Guests are **designed, never cloned.** This is a legal position as much as a creative one; see §7.

*(Every voice now exists — host and Cleopatra are done; this section is the method for the next guest.)*

**Hard limits from the API, and they bite:**

- `voice_description`: **20–1000 characters**
- **preview text: 100–1000 characters — there is a 100-character minimum.** A short preview line
  will be rejected, and short previews also produce less stable voices. Write a real paragraph.
- One generate call returns **three previews and is charged once**, priced on the preview text.
  Audition all three before saving. Saving consumes a voice slot.

⚠️ **The preview text length *is* the price — 1 credit per character.** A 900-character preview is
900 credits for one call; a 250-character one is 250 credits and returns the same three previews.
So the length of that paragraph decides how many auditions the budget buys, which is the opposite
of how it reads. **Write ~250–350 characters**: comfortably over the 100 minimum, since very short
previews produce less stable voices, and cheap enough that a reroll is not a decision.

**The prompt template the docs endorse:**

```
Native <Language + regional variant>. <Gender>, <Age range>. <Quality level>.
Persona: <2-5 words>. Emotion: <2-3 adjectives>.
<1-2 sentences on timbre, pacing, delivery>
```

**⚠️ Language and dialect go in the FIRST sentence.** The docs are explicit that stating them
late causes the voice to **drift mid-generation**. This is the same failure pattern as the
thumbnail prompt that centred the subject because the framing instruction trailed: the model
weights what it reads first. Any voice prompt in `VOICES.md` that names the language at the end
is wrong and must be rewritten.

**Four things that actively damage a voice prompt:**

1. **The word "accent" used to mean intonation.** It drags the model toward a regional accent.
   Say "intonation" or "emphasis".
2. **Any effects vocabulary** — reverb, echo, telephone, tape. The model does not apply effects;
   it just degrades the voice trying.
3. **Preview text that contradicts the description.** It must complement it — it is a performance
   script, not a label.
3b. **Vague descriptors** — "foreign", "exotic". They give the model nothing to aim at.
4. **Omitting audio quality.** "Poor quality" is a real instruction that will be obeyed. Always
   write "perfect audio quality" or "studio quality" unless lo-fi is wanted.

**The four settings, checked against the API reference 2026-09-18.** An earlier version of this
file said the docs' worked examples sit around guidance 20–40. **That was wrong** — the documented
default is 5, and the docs' own advice is the opposite of raising it.

| setting | range | default | what it does |
|---|---|---|---|
| `guidance_scale` | 0–100 | **5** | How closely the model follows the prompt. Low gives it freedom; **high forces it to stick to the prompt and can make the voice sound artificial or robotic.** The docs recommend a **long, detailed prompt at a low scale** rather than a short one at a high scale. |
| `loudness` | −1 to 1 | 0.5 | Volume of the generated voice. 0 ≈ −24 LUFS. |
| `quality` | −1 to 1 | — | Higher gives better output **but less variety**. |
| `seed` | 0–2,147,483,647 | — | **Same seed + same inputs reproduces the same voice.** |

**Leave `loudness` alone.** It is irrelevant to this pipeline: speech-to-speech output lands about
10 LUFS below source and Mode 6 normalises every clip anyway, so whatever loudness is set at design
time is erased downstream. Spending a decision on it is spending it on nothing.

**Bias `guidance_scale` low, and the reason is that the risk is asymmetric.** Too low and a preview
ignores part of the description — recoverable, because one call returns three previews for a single
charge and rerolling costs one more. Too high and the artificiality is baked into a voice that then
carries 30+ clips across both parts, and it is **permanent**, because the voice is saved and reused.
Start at or near the default; raise it in steps only if all three previews drift from the
description, never as an opening move.

**The `seed` is not exposed in the web Voice Design UI** (checked 2026-09-18). So a voice designed on the
web cannot be regenerated from parameters: **the saved voice is the asset — never delete it**, and keep a
reference render (`VOICES.md`). If the seed matters for a future guest, design through the API, which returns it,
and record it in `VOICES.md` beside the ID.

**`quality` interacts with how casting actually works.** Three previews per charge is the whole
audition mechanism, and higher quality means less variety between them — so a high quality setting
on the first call buys a better voice and less choice at once. Leave it at default for the first
generation, which is a search; if one preview is nearly right, that is when quality is worth
raising. Note that changing any input can move the result even with the same seed, so a
quality-raised regeneration is a new audition, not a polish of the same voice.

**`model_id`** is `eleven_multilingual_ttv_v2` by default, with `eleven_ttv_v3` as the alternative.
Untested here. Multilingual is the right family regardless — the guest list is full of non-English
proper nouns — and a once-only permanent asset is a bad place to try an unknown.

### 3b · Cloning the host voice

| | Instant (IVC) | Professional (PVC) |
|---|---|---|
| Audio | **1–2 min.** Never exceed 3 — more is *detrimental* | 30 min minimum, 2–3 h optimal |
| Tier | any | Creator+ |
| Training | instant | 3–6 h, plus ownership verification |

**Recording spec, and these numbers are exact:**

- **MP3 at 192 kbps or higher.** WAV is accepted but does not improve the clone.
- **−23 to −18 dB RMS, true peak −3 dB.** This is the single most actionable number ElevenLabs
  publishes.
- XLR mic into an interface, pop filter, mouth about two fists from the mic, treated room.
- One consistent tone throughout. The model mimics **everything** it hears — breathing, pace,
  mouth clicks. Consistency beats range for a narration clone.
- No music, no second speaker, no singing, no long silences.

**⚠️ Professional clones are currently NOT optimised for Eleven v3** — official, and
counter-intuitive: the expensive clone is the worse fit for the newest model. For v3 work
ElevenLabs recommends instant clones or designed voices. Given Starter has no PVC slot anyway,
**IVC is the right call for the host** and happens also to be the recommended one.

### 3c · Settings

Defaults: stability 0.5 · similarity 0.75 · style 0 · speaker boost on · speed 1.0.

- **Stability** — low gives range and random bad takes; high gives consistency and monotony.
- **Similarity** — **the setting that punishes a bad recording.** At high values with imperfect
  source audio the model faithfully reproduces the *artifacts and room noise* of the clip. If the
  host clone sounds noisy, lower similarity before re-recording.
- **Style exaggeration — the docs say keep it at 0 at all times.** It costs latency and
  destabilises the model. Put drama in the writing, not here.
- **Speed** — 0.7–1.2 only.

**Eleven v3 replaces the numeric stability slider with three named modes:** Creative (expressive,
*prone to hallucination*), Natural (closest to the source recording), Robust (stable, deliberately
less responsive to tags). **For this show: Natural.** Robust when a take keeps over-acting.

⚠️ The numeric values behind these three modes are **not published**. The 0.0/0.5/1.0 mapping
repeated across the internet is community lore. Do not write it into a script as fact.

### 3d · Keep every generation under 800–900 characters

Official troubleshooting guidance: long passages **drift or switch language and accent
mid-generation**. Shot-level lines are far under this, so the show is safe by construction — but
never batch a whole act into one request to save calls.

---

## 4 · Arabic — read this before promising Egyptian

**The only Arabic variants named anywhere in official documentation are Saudi Arabia and UAE —
Gulf.** Eleven v3 lists "Arabic (ara)" with no dialect breakdown at all. The Voice Design guide's
own Arabic worked example uses "soft Gulf (UAE) accent influence."

**Egyptian Arabic is not documented as a supported variant.** There is a marketing blog post
about Egyptian accents; there is nothing in the docs that commits to it. Treat Egyptian as
**achievable but unproven**, and budget testing time rather than assuming.

Two facts that decide the approach:

1. **A clone carries its source language's accent into other languages.** Official: a voice not
   native to the target language "might have an accent from the original language and might
   mispronounce words." Default library voices are primarily English and carry an English accent
   in Arabic.
2. The documented fix is to **clone a voice actually speaking the target language**.

**DECIDED — this is settled, do not re-open it.** The host voice is an **instant clone of the
creator's own voice, recorded in Egyptian Arabic**, then used normally to speak English. Tested in
this project: an Egyptian Arabic source voice speaks English well. The programme itself stays in
**English**, and guest voices stay native-English by design, exactly as Mode 2 specifies — so the
undocumented state of Egyptian Arabic as a *synthesis* dialect does not affect this show. The
Arabic is in the source recording, not in the output.

The accent-carry rule is what makes this work rather than a problem: the clone keeps the colouring
of the language it was recorded in, which is the intended character of the host.

Also: write numbers, symbols and acronyms out as words. Latin-script acronyms embedded in Arabic
text are reliably mispronounced.

---

## 5 · Speech-to-speech (the voice pass)

**Model: `eleven_multilingual_sts_v2`. Set it explicitly.** The API default is
`eleven_english_sts_v2` — English only — which is a silent trap on any Arabic material.

**What it keeps from the source:** tone, emotion, cadence, timing, and **the accent and language
of the performance**. Delivery comes from the performance, not the model.
**What it replaces:** the vocal timbre alone.

This is why the existing rule holds: the Kling clip supplies the *performance*, ElevenLabs
supplies the *identity*, and the two are not interchangeable.

**Limits:** 5 minutes / 300 seconds per segment, 50 MB per file. Billed at 1,000 characters per
minute of audio.

**`remove_background_noise` exists** — a boolean, default off, running the audio-isolation model.
Worth knowing, but it is built for noise, and the docs make **no claim** that it separates music
or a second speaker.

**⚠️ Multi-speaker behaviour is undocumented.** ElevenLabs does not state anywhere what happens
when a clip contains two voices. This project's standing rule — **a two-speaker clip cannot pass
the voice pass** — is based on how the model works, not on a documented statement, and it should
stay in force. There is a separate **Voice Isolator** product if a source ever needs cleaning
before conversion.

---

## 6 · Music and sound effects

### 6a · Music

**Use `music_v2_5`.** The API still defaults to `music_v1`, which is being phased out.

**Duration: the docs contradict themselves** — one page says 5 minutes, another says 10. The API
is unambiguous at **3 s – 600 s**. Treat 10 minutes as the ceiling and verify before relying on
anything over 5.

`force_instrumental: true` is documented to *guarantee* an instrumental result. Use the flag; do
not rely on writing "no vocals" in the prompt.

**Composition plans — the feature that solves this show's timing problem.** `POST /v1/music/plan`
builds an editable plan **free of charge**, which can then be generated from:

- up to **30 sections**, each **3 s – 2 min**
- per-section styles, negative styles, and duration
- **"The styles of the first chunk are the most important"** — they set the whole piece

And **inpainting**: generate with `store_for_inpainting: true`, then regenerate any single
section while keeping the rest, mixing generated chunks with kept audio (max 30 s of reference).

This matters directly for `MUSIC_Theme_Main`. The note in `AUDIO_PROMPTS.md` says a music model
will not place a swell at a requested time, so the timing must come from the edit. **That is true
of a plain prompt but not of a composition plan** — sections give real control over where the
swell sits. Worth trying before falling back to cutting by hand.

**Prompting**: name genre, mood, instrumentation, tempo and production era. Anything left open is
answered with the most statistically average choice. Narrate the arrangement chronologically —
*start / just / then* carry weight. Studio vocabulary works: "tape saturation", "plate reverb".
Rule: constrain what matters, leave space everywhere else. Prompt limit 4,100 characters.

**⚠️ Contractual limit on prompts:** you may not submit any artist's real or stage name, any song
title, or any substantial portion of lyrics. "In the style of [artist]" is not permitted.

### 6b · Sound effects

**`eleven_text_to_sound_v2`. Max 30 seconds.** Prompts should be short — one sentence or a
fragment. Name the sound, its texture, its space. Embellishment hurts.

`prompt_influence` 0–1, default 0.3. `loop: true` produces a seamless bed and is explicitly
recommended for ambience and background texture.

**⚠️ Looping output is MP3 only.** WAV 48 kHz export is available *only for non-looping* effects.
So the room tone bed — which must loop — is MP3, which means **the 1152-sample trim applies to it
too.**

For anything longer than 30 s the documented approach is exactly what this project does: one
looped bed, separate one-shots for events, assembled on a timeline. Layer separately rather than
asking for a complex scene in one prompt.

---

## 7 · Rights, policy, and the thing that could get an account banned

**Voice Design is what keeps this show inside the rules.** The Prohibited Use Policy bans
replicating "the voice of another person" without consent, and bans impersonation "in a manner
intended to deceive others about whether the voice was generated by artificial intelligence."

A **designed** voice for an ancient figure replicates nobody — there is no recording of Cleopatra
to impersonate. That is a categorically different act from cloning, and it is why designing
guests rather than cloning them is the correct policy as well as the correct aesthetic.

**⚠️ Two live risks, both unresolved in the docs:**

1. The policy bans impersonating "political candidates or elected government officials,
   **regardless of whether authorization was obtained**." As written there is no *living*
   qualifier. Whether it reaches historical heads of state is **not addressed anywhere**. Ancient
   rulers were not elected, which is probably the saving distinction — but this is genuinely
   ambiguous and is the largest policy exposure this format carries.
2. **No-Go Voices** is an unpublished blocklist of prominent figures. Whether it covers historical
   people is not stated. Expect some well-known names to be blocked without warning.

**The moment a guest is modern enough to have real recordings, both risks change character.** A
20th-century guest is a different legal question from Cleopatra, and must be reconsidered rather
than waved through on precedent.

**Publishing:**

- YouTube requires disclosure for "the likeness of a realistic person". Use the *altered or
  synthetic content* flag in the upload flow **as well as** the on-screen disclosure card. The
  card is not sufficient on its own, and the flag is not sufficient on its own.
- Music on every self-serve tier permits online commercial use **except film, TV and radio**.
  YouTube is fine; a broadcast licence is not included at any price below Enterprise.
- **YouTube Content ID: ElevenLabs says nothing.** No indemnity, no statement. Combined with their
  own warning that output "may not be unique and may be similar or identical to Output returned to
  other users", there is a real unquantified exposure. Not a reason to stop; a reason not to claim
  the music is safe.

---

## 8 · Working through the MCP

**Results come back into the chat with a download button on each take.** That is the delivery
mechanism — not the flow page, and not the Assets library.

## ⚠️ ONE CUE PER RUN. Never batch.

This is the single most important operational rule on this page, and it was learned the hard way:
the first run generated three different sounds in one call, and all twelve takes arrived in the
chat as one undifferentiated pile with no way to tell room tone from sand from paper.

**Each `run_flow_nodes` call takes exactly one node.** One cue, its four takes, shown on its own,
labelled. Then the next. A run that batches cues is unusable no matter how good the audio is,
because nobody can tell which take belongs to which sound.

Two supporting habits:

- **Label every node before running it** (`update_node` with `label`). An unlabelled node shows as
  "New sfx node", which defeats the point.
- **`show_flow_results` can re-show any past run**, filtered to one node's session IDs. That is how
  a batched run gets untangled after the fact — it costs nothing and generates nothing.

## The rest of it

Two things the flow is *not*: connector-made flows **do not appear in the account's Flows list**
(confirmed 2026-09-15 — same account, reachable by direct link, absent from the list), and their
output **never reaches the Assets library** (`creative_get_available_assets` returns empty). So the
chat is the only place the takes appear. Download them as they arrive rather than trusting the
canvas to still be findable later.

**⚠️ Files cannot be pulled down automatically.** Output sits behind signed Google Storage URLs,
and the session environments were blocked from that host by egress policy (as of 2026-09-15).
**The route that works:** download from the ElevenLabs page in the browser, which lands the files
in `~/Downloads`; `Fixed_Assets/Audio/intake.sh <name>` then files them into the project. Only the click is manual.

Other practicalities:

- `generations_count` maxes at **4** per run.
- A large run partly queues and **retries itself** — "concurrency limit" is not an error.
- Concurrency on Starter: 3 standard TTS, 6 Flash, **2 music**.
- Setting model parameters needs the three-step path: `add_flow_node` → `update_node` →
  `run_flow_nodes`. Always call `get_model_schema` first; invented parameter names fail
  validation rather than being coerced.

---

## 9 · Deliberately unresolved

Do not let a later session quietly turn any of these into a stated fact:

1. Numeric values behind v3's Creative/Natural/Robust modes — unpublished.
2. Voice-changer behaviour with multiple speakers or music in the source — undocumented.
3. Egyptian Arabic **as a synthesis dialect** — undocumented. (Not used by this show: the host clone is *recorded* in Egyptian Arabic and speaks English — decided and tested, §4.)
4. Music credits per second — unpublished; plan with the account rate in §2 (15/sec), not the `estimate_only` figure (25/sec).
5. Whether the political-figure ban and No-Go list reach historical people — unaddressed.
6. YouTube Content ID exposure — no official statement.
7. Maximum music length, 5 min vs 10 min — the docs disagree with each other.

**Verify pricing at the point of purchase.** The tier tables change, and ElevenLabs' own pricing
pages do not reconcile with each other.
