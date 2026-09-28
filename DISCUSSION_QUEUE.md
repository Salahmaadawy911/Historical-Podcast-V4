# Discussion queue — points raised by Salah, 2026-09-22

**Status: saved for discussion only. Nothing below has been acted on.** Take them one by one; when a
point is settled, record the decision under it and in the relevant skill file.

Context when raised: waiting for the weekly Kling credit limit. Full regeneration of Part 1 is pending
(`Episodes/Cleopatra/ROUND1_prompts.md`); `shots/` is clean; demo of the opening with the hook is at
`Episodes/Cleopatra/DEMO_opening_with_hook.mp4`.

---

## 1. Are the modes written too specifically for Cleopatra?
> "The modes feels like it is written for a specific guest which is cleopatra, will this affect future guests?"

- [x] Discussed · **Decision 2026-09-22: generalisation pass — DONE.**
  - **Performance profile** added to each guest's `CAST.md` (Mode 2 spec + Cleopatra's filled in): prompt label, pronouns, default register, emotional ceiling, interruption style, gesture range, composite flag, duration calibration. Modes 3/4/6 read guest-specific behaviour from it.
  - **Recipes neutralised** in Modes 3, 4, 6 (*the guest*, the profile's label and pronouns); Cleopatra lines kept as marked examples. Mode 4's attribution rule no longer says *"The woman says:"*.
  - **Tools part-aware:** `chain_frames.py <ep> <part>`, `round_sheet.py … --part N`, `build_episode_cards.py … --part N` (Part 2+ renders tagged `p<N>`), `plates_build.py --part N`; gates in Mode 4 rewritten with `G/N/K` variables. `sources_audit.py` read a **hard-coded Cleopatra source list** — now reads `card_data_p<N>.json`. Pull-quotes now sit on the actual speaker's side (were always guest side).
  - **Duration re-measured per guest** (first 3–5 clips of Pass 1); Mode 4 §2 now opens with the v2 model (it still showed 3.85 syl/s); `syl.py` copied to `Fixed_Assets/tools/`.
  - Cleopatra history notes moved from the six mode headers to `DECISIONS_ARCHIVE.md`.
  - ⚠️ **Found on the way:** `junction_scan.py` had been **checking zero lines** since the inline-attribution change (2026-09-21) — fixed; it now fails if it scans fewer lines than there are talking rows. Re-run: Part 1 is genuinely clean.
  - **Dry run — a male, 19th-century composite eyewitness**, walked through every mode on paper:
    - Mode 1 ✅ composite tier and eyewitness arc already exist. Mode 2 ✅ profile gives `The man` / he, `Composite? yes`; period gate, accent rule and lower-third composite format are generic.
    - Mode 3 ✅ toolkit, interruption kinds, hook, context cards all guest-neutral; composite arc (*what he saw / what he understood*) exists.
    - Mode 4 ✅ register and label come from the profile; testimony register switches on; `--composite N` card; chains, gates and round sheets work on a test `P2_kit.md` (continuity and junction gates both fired correctly).
    - **Two things that stay manual, by design:** `sources_audit.py`'s built-in author list is Roman-world — add the new era's authors (names on the card are added automatically); and `names.dict` grows by the new era's proper names the first time the junction scanner reports them *not in dictionary*.
    - Studio, host, camera frames and brand furniture are series-fixed — correctly the same for every guest.

## 2. The original master instructions file
> "There was originally a master instructions file that i can't find now but i have an older version that i will add later just not to confuse you (tell me if you need or when you are ready to receive it), a lot was changed since then and i don't want to break anything of what we already did with the modes skill files but this one had like some governor rules for the project as a whole and it described what the modes will be used for and so on, i will paste here some parts the i am not sure if they are applied or not (very important the phonetic overrides)"

Excerpt pasted by Salah (verbatim):

```
# ROLE & SHOWRUNNER DIRECTIVE
You are the Lead Investigative Researcher, Historical Showrunner, and Asset Architect for a premium historical documentary video podcast series.

---

## 1. CORE INTERVIEW & NARRATIVE DYNAMICS
* **The Host (Modern Lens):** Objective, composed investigative journalist. Probes moral compromises, controversies, and historical consequences using a modern analytical framework.
* **The Guest (Era-Authentic):** Defends actions strictly through the worldview, survival realities, and political pressures of their historical era without modern apologetics.
* **Podcast Immersion:** Gritty, high-tension atmosphere. Maintain absolute immersion—the Host speaks to the guest as if physically sharing the studio desk. Zero fourth-wall breaks.

---

## 2. DIALOGUE & AUDIO REALISM STYLE GUIDE
* **Zero Melodrama:** Strictly ban AI clichés ("tapestry of time", "delicate dance", "alas", "a testament to").
* **HBO-Style Realism:** Punchy, tense, conversational. Use contractions, natural pauses, and conversational friction (Host and Guest occasionally speaking over or interrupting each other).
* **Punctuation Logic:** Use ellipses (`...`) for trailing thoughts; use em-dashes (`—`) for sharp interruptions.
* **Vocal Artifacts in `tts_text`:** Every dialogue block must embed physiological breathing and tension cues (e.g., `[sharp inhale]`, `[sighs]`, `[clears throat]`, `[exhales heavily]`, `[pauses]`).
* **Phonetic Overrides:** Format all ancient names, foreign locations, and archaic terms phonetically in brackets within `tts_text` (e.g., `Marcomanni [mar-ko-MAH-nee]`).
```

Salah will provide the older full version later. Receive it as a **reference to compare against**, not
to merge wholesale — check each rule against what the current modes already do.

- [x] ~~Full older file received~~ — **not needed** (Salah, 2026-09-22) · [x] **Excerpt compared rule by rule (2026-09-22)** · **Decision 2026-09-22: all applied.**
  - **Pronunciation:** Mode 3 writes a Pronunciation table for every rare name; Mode 4 §3 block 3b puts it in the prompt as its own paragraph outside the quote — **pending the A/B** (`Episodes/Cleopatra/TEST_pronunciation_P1_024.md`); fallback: respell inside the quote. Part 1 table written (Ptolemaic, Parthia, Octavian, Actium).
  - **Banned phrases:** list in Mode 3 and in the new gate `Fixed_Assets/tools/lines_check.py` (also checks pronunciation coverage). Part 1: none found.
  - **Contractions:** a field in the performance profile (Cleopatra: formal, none); host uses them naturally.
  - **Host brief** written in `STUDIO_ASSETS.md` (modern lens, interviewer not interrogator, contractions, immersion).
  - **Fourth wall:** Salah — not important, current design stands; recorded in the host brief (host speaks to camera only in the fixed slots; guest never).
  - **Vocal artifacts:** written as physical beats in the gesture paragraph (brackets inside a quote are read aloud). **Trailing `…`:** allowed; check the first take that uses one.
  - Nothing proven was changed: the only prompt change (pronunciation) waits for its test.

**Audit of the excerpt against the current modes (2026-09-22):**

| rule | status | where / why |
|---|---|---|
| Host = modern lens, objective investigative journalist | **partly** | implied (Knowledge Gate: *the host carries posterity*; Mode 4 §4 host register) but never stated as a brief in one place |
| Guest = era-authentic, no modern apologetics | ✅ applied | Mode 1 *Historical Defense*, Mode 3 Knowledge Gate, testimony register for composites |
| Immersion, zero fourth-wall breaks | ⚠️ **conflict** | the host addresses camera in the cold-open hook (P1_004) by design; the guest's frame is retrospective (*"two thousand years later, in this room"*). Needs a definition |
| Zero melodrama, banned clichés | ❌ **not in the modes** | only in the project instructions; no banned list, no check |
| HBO realism: contractions, pauses, friction | **partly** | friction ✅ (toolkit); pauses are made by the model; contractions: host 10/36 lines, guest 0/31 — deliberately formal for Cleopatra but written nowhere |
| Ellipses for trailing thoughts, em-dashes for interruptions | **superseded / untested** | interruptions are now built in the edit (never asked of the model); no line uses `…`; how Kling performs `…` is untested |
| Vocal artifacts `[sharp inhale]` in `tts_text` | **superseded** | there is no TTS stage any more: Kling performs the line and **bracketed cues inside a quote are read aloud** (Mode 4 §3). The working equivalent is a breath/settle written in the gesture paragraph |
| **Phonetic overrides** | ❌ **not working** | Mode 4 says *"note pronunciation beside the shot"* — Kling never sees that note, and ElevenLabs speech-to-speech **cannot** fix it (it keeps the source's phonetics). No mechanism controls pronunciation today |


## 3. The script and story as a whole — how to make it a good YouTube show
> "we have been testing the video generation and every other thing that it can be generated and all looks good now, we also add some "director" tools and so on, but the script itself or the story as a whole i am not sure still and i won't be able to see the whole picture until a part is fully produced, but i want you to be equipped with the creativity and techniques needed to achieve a good script (we need a good youtube show), so how would we achieve this?"

- [x] Discussed 2026-09-22 · **Proposed (awaiting Salah):** (A) a *story engine* section in Modes 1 and 3 — central question per act, escalation ladder, one myth-vs-record reversal per act, one concrete image per act, the crack, subtext rules; (B) review **before** spending Kling credits — a story review against a rubric (incl. a cold-reader pass), then a **table read + animatic**: the whole part as ElevenLabs TTS in the two real voices (~6,700 characters for Part 1) laid over the seed frames, cards and opening = a watchable rough cut at zero Kling credits; (C) run both on Part 1 before its regeneration; after publishing, the YouTube retention graph feeds Mode 3 for Part 2.
  **Decision 2026-09-22:** (A) written — *The story engine* (Mode 3) and *Story potential* (Mode 1, pitch item 8). (B) **a standing gate, without audio**: Claude's story review → `P<n>_STORY_REVIEW.md`; Salah's read of `P<n>_SCRIPT_READ.md` (new tool `script_read.py`); Mode 4's gate list requires both. ElevenLabs table read stays optional. (C) Part 1 reviewed — `Episodes/Cleopatra/P1_STORY_REVIEW.md` + `P1_SCRIPT_READ.md`; two no-cost fixes applied (Actium card re-rendered, P1_092 prompt wording); three script decisions open for Salah (Act A order, Act A ending, a Donations b-roll).
  **After publishing:** release plan undecided (one by one vs. a batch on a schedule). Recommended: build a buffer, release on a fixed schedule, keep each guest's Part 2 editable until Part 1's first-week retention is in. Revisit when the release plan is chosen.

## 4. Splitting a sentence across shots for more accurate emotion / gesture / expression
> "splitting the sentence on one shot to capture more accurate emotions/gestures/facial expressions"

- [x] **Follow-up (Salah, reviewing P1_057):** each sentence should carry its own slight emotion — made a general writing rule: Mode 3 *every answer has an arc* (beat map per sentence), Mode 4 §4 item 8 (one delivery note per sentence **and a physical beat between sentences where the body changes**, Kling multi-speaker syntax applied to one speaker, in one clip — the default and free; big turns → `SPLIT`). Untested; parsers must learn multi-segment lines before a kit uses it.
- [x] Discussed · **Decision 2026-09-22:** rule changed to **"one beat, one clip"** — a line whose mood turns at a sentence (or whose gesture must land on one word) may split into two chained clips on the same angle, marked `SPLIT` in Mode 3; Mode 4 §2 builds it (sentence breaks only, own delivery note and gesture per half, seam hiding named in the row); Mode 6 hides the seam (cutaway → punch-in → cut on the pause). The old objection (pose reset) died with chaining. **Untested — `P1_070` added to the test plan**, together with the unverified lip-sync-drift claim.

## 5. Split-screen scenes
> "the split screen scenes"

- [x] Discussed · **Decision 2026-09-22: approved — equal halves.** The two-up (`TWOUP`) replaces what the wide was for: both people together, built from the singles, so the wide's scale fault never appears. Director's tool, used where it earns its place (one or two per part). Written into Mode 3 toolkit, Mode 4 §8b, Mode 6, Mode 5 (stacks vertically in reels), `STUDIO_ASSETS.md`. Reference frame `Fixed_Assets/Branding/reference/splitscreen_reference.png`. Part 1 candidates go to the Part 1 script-decisions reminder.

## 6. Changing the intro — a zoomed face fading into the paper background
> "Intro changing (zoomed face fading in the paper background) - already i built a mockup"

Salah has a mockup; ask for it when this point comes up.

- [x] Mockup received (`Intro_test.mp4`, 19.17 s, same length as `BRAND_opening`) · [x] Discussed · Decision: **approved 2026-09-22 — built.** `Fixed_Assets/Branding/intro_source/hook_build.py` renders it for every guest/part (paper continuous with the card and intro, hand-cut polygon keeping some studio on purpose, grain through the face, voice before face, fade out before the 8.00 strike, freeze fallback). Spec in `SERIES_FURNITURE.md`; *Hook framing* added to the performance profile; Mode 3/4/6 updated. Demo: `Episodes/Cleopatra/DEMO_opening_hook_paper.mp4`.
  **Measured from the mockup:** face fades in ~4.1 → 6.3 s (linear, ~2.2 s), holds at full 6.3 → 7.5 s, fades out 7.5 → 8.0 s into the first charcoal study; soft oval mask, paper texture showing through the face (reads as a portrait printed on the page); the line (`P1_057`, *"Egypt did not survive without me."*) runs 4.0 → 6.2 s — so most of it is spoken while the face is still emerging, and she is fully visible on *"me"*.
  **Assessment:** adopt — it keeps the whole opening on one paper page (the opening's own design rule; the studio shot was the only photographic break), and it bookends the close (the opening: a face emerging from paper; the close: the studio turning into a drawing).
  **Refinements proposed:** (1) the studio leaks at the mask edge (slat wall left, dark panel right) — lift/desaturate the background inside the mask or tighten it to the head; (2) keep the voice-before-face timing (deliberate: a voice from the page, then the face) unless Salah wants her visible earlier; (3) make it a reproducible per-episode render (`hook_build.py`: clip, in/out, face centre and scale → composited into the 4–8 s slot) so every guest gets the same treatment; update `SERIES_FURNITURE.md`, Mode 3 hook section, Mode 4 opening row.

## 7. YouTube metadata / SEO in the Mode 4 kit
> "in production kits generated by mode 4 i see that we already have youtube metadata, i want just to confirm/optimize so it have all what needed so a video can be found alot (title hashtags, descriptions and so on "Youtube SEO") i want this to be a simple copy/paste for me but have the best."

- [x] Discussed 2026-09-23 · **Proposed (awaiting Salah):** replace kit §9 with a generated **`P<n>_PUBLISH.md`** — one copy-paste sheet in YouTube Studio's field order: title (+2 alternates for Test & Compare), description (hook with keywords in the first ~150 characters → 200–300-word summary → *what you may have heard vs. the record* → chapters with timecodes → sources → AI disclosure → series links → 3 hashtags), 10–15 tags, the settings checklist (**Altered or synthetic content = Yes**, category Education, language, caption file uploaded), playlist, end screen, pinned comment, thumbnail file. Mode 4 writes the words; `publish_sheet.py` assembles the sheet; Mode 6 fills the timecodes from the cut. Found: Part 1's title option 1 misquotes the line (*"There Was No Egypt That Survived Without Me"* vs. *"Egypt did not survive without me."*).
  **Decision (2026-09-23): build it; do not produce Part 1's sheet yet.** Done: Mode 4 **§15** (the fixed §9 labels and the rule for each), `Fixed_Assets/tools/publish_sheet.py` (`--words-only` for Mode 4; full sheet in Mode 6), Mode 6 *Publishing* (timecodes file → captions → run → upload in sheet order), `Fixed_Assets/publish_defaults.json` (series playlist link still `TODO`). Tested on a scratch dummy kit only — passes, and every failure case fires. `--words-only` on Part 1 (nothing written): the old-format §9 is missing 7 labels, title 1's quote fails the verbatim check, and the hook doesn't name Cleopatra in its first 150 characters — all fixed when Part 1's §9 is rewritten to §15.

---

## ⏰ REMINDER — raise after the last point is settled
> "just remind me after we finish everything to discuss about the test because maybe we will test other things in the same shot or different shots if needed"

**Plan the test takes together before any are generated.** The pronunciation A/B
(`Episodes/Cleopatra/TEST_pronunciation_P1_024.md`) is written but **not scheduled** — Salah may fold
other tests that come out of points 3–7 into the same shot, or spread them across different shots.
Collect every open test first, then design one test batch.

**What we are testing — the questions, not the shots.** (Salah, 2026-09-22: the kit will change before
the tests run, so the shot ids below are only today's candidates. When the test plan is made, pick
whichever shots in the *final* kit best qualify, using the criteria.)

| # | question the test answers | a shot qualifies if | today's candidate |
|---|---|---|---|
| T1 | Does a **Pronunciation:** paragraph make Kling say a rare name right? (else: respell inside the quote) | its line contains a rare name, ideally one with a silent letter or shifted stress | `P1_024` (*Ptolemaic*) |
| T2 | Does a **beat map** — one delivery note per sentence, gestures between sentences, one clip — give each sentence its own temperature without extra pauses or notes read aloud? | a guest line of 3+ sentences whose temperature shifts | `P1_057` |
| T3 | Does a **`SPLIT`** line (two chained clips at a sentence) read as one continuous line? And does lip-sync drift after ~5 s in the whole take? | a line ≥ 10 s whose mood turns at a sentence, ideally with something that can cover the seam | `P1_070` |
| T4 | Does a **trailing `…`** play as a thought let go, not a stop? | the first line in the kit that uses `…` | none yet |
| T5 | Does a **`CUT-IN`** stop (silent clip chained from the talking clip at the cut word) read as a real interruption, and does the open-mouth start frame stay closed? | the first `cut` / `seen` / `yield` interruption in the kit | none yet (Part 1 has only a `hold`) |
| T6 | Does a **two-up** hold up in motion — crop, eyelines, the listener clip's length? | the first `TWOUP` placed | chosen with the Part 1 decisions |

Tests can share a shot where the questions don't interfere (e.g. T1 + T2 on one line that has a rare name and a temperature shift).

Tests collected so far:
- **Pronunciation A/B** — `P1_024`, with and without the *Pronunciation:* paragraph (point 2).
- **Beat-map test** — `P1_057`, one delivery note for the whole line vs. one note per sentence (Mode 4 §4 item 8); listen for extra pauses between segments. Raised by Salah reviewing the P1_057 take (point 4 follow-up).
- **`SPLIT` test** — `P1_070`, whole take vs. split at *"He needed a foreign woman to blame."* into two chained clips; the host's failed *"But he—"* (`P1_070a`) already sits at that seam and can cover it. Also answers the unverified *lip-sync drifts after ~5 s* claim (point 4).

- [x] Discussed 2026-09-23 · Test plan: **the test batch is now a standing step — Mode 4 §0c** (after the gates, before Pass 1, Part 1 of every new guest). The T1–T6 table moved there with its criteria; shots are picked from the rerun's fresh kit, not the ids above.

## ⏰ REMINDER — Part 1 script decisions, raise after the last point is settled

> 🧼 **Superseded 2026-09-23 by the clean-room rerun.** The items below are tied to the old script (shot ids, lines). They reach the rerun only as the **lessons** written into `NEXT_STEPS.md` B5 — never as edits to carry in.
> "for the answer same applies here like the test shot, remind me after we finish all points so if anything else to be changed."

From `Episodes/Cleopatra/P1_STORY_REVIEW.md` — held until all points are done, since later points may
change the script too. Decide together with anything else that comes up:
1. **Act A's opening** — leave it / move P1_018–019 (Rome's annexation bills) to the front / add one host line pointing ahead.
2. **Act A's ending** — keep the light close (*"Most of it was reading."*) or end on an open loop.
3. **A Donations of Alexandria b-roll** for Act C (~53 cr, source to be checked).
3b. **Two-ups for Part 1** — candidates: `P1_070` (her carrying on over his *"But he—"*), `P1_073a` → `P1_074` (the second answer), `P1_085`/`P1_086` (the echoed *"In the middle of the battle."*). Pick one or two.
4. The **release plan** (one by one vs. buffer + schedule) — revisit when decided.
5. **Part 1's §9 rewritten to Mode 4 §15** (point 7) — pick the title quote (option 1 misquotes her; the hook line is *"Egypt did not survive without me."*), name Cleopatra in the hook's first 150 characters, and write the summary, heard-vs-record (the carpet `P1_042`, the library `P1_047`), tags, hashtags, pinned comment. The sheet itself waits for the cut.

- [x] Discussed 2026-09-23 · Decisions: **Cleopatra is rerun from Mode 1** (see `NEXT_STEPS.md`, B5). Items 1–3b and 5 go into the fresh Mode 3 as notes and are decided in the new `STORY_REVIEW.md` / `SCRIPT_READ.md`, not patched into the old kit. Item 4 (release plan) is deferred — Salah, *"the release plan for later"*.

