# SKILL: MODE 3 (OUTLINE ARC)

> 🔴 **LESSONS protocol (Salah, 2026-09-24).** Read `Fixed_Assets/LESSONS.md` before starting. When any
> problem turns up — in a test, a take, a review or the edit — fix it at the source in the same sitting:
> write the rule into **every** skill that could produce it again, add a gate wherever a script can
> detect it, and add a row to `LESSONS.md`. Fixing only the kit or the clip is not a fix.


> 📂 **Inputs and output — added 2026-09-19 so each mode can run in its own chat.**
> **Reads:** `Episodes/<Guest>/PITCH.md` and `Episodes/<Guest>/CAST.md`.
> **Writes:** `Episodes/<Guest>/OUTLINE.md` — both parts, in the fixed format of *The outline file* below: acts, the hook line, every line of dialogue with its provenance tag, the toolkit tags, the context cards, pull-quotes and the Pronunciation table. Then `STORY_REVIEW.md` and `SCRIPT_READ.md` — **both parts in one review and one read**, approved by Salah before Mode 4 starts.
> **Save the output to that file before the mode ends.** Anything that lives only in chat history
> is lost to the next mode.


> 🧼 **Rerunning a guest — the clean room. Added 2026-09-23.**
> When a guest is rerun (their old work sits in `Episodes/<Guest>/_v1_archive/`), the archive is a
> **fact-check source, never a draft.** The rerun must come out of *today's* skills, so nothing creative
> from the old run may steer it.
>
> | carry in — research and assets | never carry in — creative direction |
> |---|---|
> | the guest, Likeness/Recognition tier, and the **charge Salah approved** | any **dialogue line**, including "good" ones, callbacks and the old crack |
> | the two-part rule; `CAST.md`, frames, voice, thumbnail portrait | the **hook line** — Mode 3 picks it from its own script |
> | **verified facts and corrections**, stated as *fact + source* (the carpet was a bedding sack, Plutarch *Caesar* 49) — never as the old line | the **act structure**, the order of events, where a part breaks, shot ids |
> | the pronunciation table; the audited source list | titles, working titles, the **next-part title**, thumbnail lines |
> | **lessons as principles** — *"a background act must open on a question"*, not *"move P1_018 forward"* | script decisions tied to the old script's shape (reorder X, two-up at Y) |
>
> A rerun `PITCH.md` describes each part as **questions and documented events**, with no lines, no hook
> and no titles. If a carried-in fact came from the archive, say so in one line and re-verify it where
> Mode 3 turns it into a `[D]` line. When in doubt: would a fresh run have had this without the old kit?
> If not, it stays in the archive.
> **The skill files quote old Cleopatra lines as examples of a technique** (*"Egypt did not survive
> without me."*, *"You assume those were two things…"*). They illustrate the rule; they are not material.
> On her rerun they are off-limits like any other archived line.

> 🔴 **Non-negotiable, read before writing a single line — full text at *"The standard: nothing a
> critic could call a lie"*, §Provenance.**
>
> 1. **Never write a `[D]` line from memory.** Look the fact up while the line is still text. Both
>    of Part 1's errors were confident recollection, not invention — that is the failure mode.
> 2. **No line leaves this mode with a check outstanding.** There is no VERIFY tag. Verify it, drop
>    the unverifiable precision, or retag `[D]` → `[I]` and give the claim to the guest.
> 3. **The channel's owner is not the fact-checker.** A line reaching him to verify is a process
>    failure. The burden is here.
> 4. **No phonetic junctions — a hard rule since 2026-09-20.** No word ending in a stop
>    (t, d, p, k, b, g — alone or closing a cluster like -pt, -st, -nd) may run straight into a word
>    that opens on a **stressed** vowel: *"without Egypt"*, *"Mark Antony"*, *"at Actium"*. It broke
>    lip-sync five times across every duration and position; *"without it"* was clean. Rephrase while
>    the line is still text — a pronoun for a just-named noun, a vowel-final or fricative-final word
>    before the name (*"with Antony"*, *"as Antony's"*), or a sentence break. Run
>    `python3 Fixed_Assets/tools/junction_scan.py Episodes/<Guest>/OUTLINE.md`; it must print nothing.
>    Details in Mode 4, *"Check the consonant junctions"*.
> 5. **No line ends on a stop cluster — a rule since 2026-09-24 (Salah).** A line's **last word** may not
>    end in two stops back to back — *described* (/bd/), *marked* (/kt/), *worked* (/kt/), *Egypt* (/pt/).
>    The last word of a clip is where lip-sync is weakest, and in T8 both takes strained on *"described"*.
>    Rephrase so the line ends on a vowel, nasal or fricative (*marked* → *chosen*, *worked* → *held*,
>    *leave Egypt* → *leave Egypt behind*). 🔴 **No exceptions (Salah, 2026-09-24).** Even when the word
>    *is* the line, move it off the end: *"Usually I am described."* → *"Usually, others describe me."* —
>    the idea survives, the last sound is a vowel. `TAIL-OK` is withdrawn; `lines_check.py` on the outline
>    >    **fails** every one. The same holds for the last word before a `SPLIT` seam — that is the end of
>    clip A — and the check covers it.

Before starting, view the guest's character sheet image (in `Episodes/[Guest Name]/`) and any candidate B-roll assets per `STUDIO_ASSETS.md`'s Visual Grounding Requirement, so this outline's manifest and prompts reflect how these assets actually look.
1. 2-Part Breakdown:
   - **Part 1 — The Inciting Conflict and the Compromise.** The position the guest inherited, the choice they made under it, and the modern charge laid against that choice. Ends with the charge stated and unanswered.
   - **Part 2 — The Reckoning.** The defence at full strength, the consequences, the downfall, and what the record actually supports about the legacy.
   - Include core tension and cliffhanger for each part. Do not write dialogue yet.

   **Pick the Part 1 break by finding the strongest unanswered question, not by a clock.** Break where the audience most wants the answer. The structure is fixed and repeats for every guest:

   > host asks the question → guest gives a short response that opens more than it closes → host hands off → wide, music, credits.

   The hand-off is the host's own clip and must be planned here, because the wide that follows it carries no dialogue (see **The wide never carries dialogue** below). Three clips, not two.

   **Two parts, not three.** The middle part of a three-part arc is the weakest position in the series: nobody enters there and many abandon it, and it costs exactly as much to generate as the parts people watch. Fold the turning point into Part 1 as the thing the guest is accused of, and give Part 2 the answer and the fall.

   **Part 1 must stand alone.** It is the only entry point the arc has — a browsing viewer never starts at Part 2. Part 1 has to work as a complete argument for someone who watches nothing else, with the cliffhanger as an invitation rather than a withheld ending. Part 2 is depth for people who already care, and should open by re-establishing the stakes in one exchange rather than assuming Part 1 is fresh in mind.

   Target roughly 10–12 minutes of spine per part. Runtime is the cost: on kling.ai at 1080p every extra minute of talking is **about 600 credits** (Turbo, 10 cr/s), so a part that runs long is a budget decision, not a creative one. Silent coverage is far cheaper — Standard 3.0 with audio off is 8 cr/s — which is why reaction shots and silent wides are the affordable way to give a part air.
1b. Composite episodes — different arc shape:
   - When the guest is a Fully Anonymous Composite eyewitness, the arc is not compromise-then-reckoning. **Part 1 is what he saw; Part 2 is what he understood, and when.** The turn is the moment knowledge became unavoidable, not the moment a choice was made — he mostly had no choices to make.
   - **Part 2 closes on the record, not on the character.** A named figure gets the last word in their own episode; a composite does not. Plan that final beat here as a documented fact, a card, or the host — at outline, not improvised in Mode 4.
   - Part 1's cliffhanger is a question of knowledge left open ("when did you know"), never a moral accusation left hanging — the character can only answer that with invented remorse or invented conviction, and both are fabrications.
   - Name the body of testimony the composite is assembled from and roughly how many accounts, since Mode 4 needs the number for the `BRAND_composite` card.

2. Asset Manifest:
   - State `@guest_[name]` or `@archival_[name]` — whichever Mode 2 produced for this guest.
   - List any recurring historical B-roll character tags needed (e.g., `@roman_legionary`).
   - If the outline references a real, named figure who is central to the story but isn't the interviewed guest, do not default them to off-screen or Eyewitness Substitution on the basis of fame alone. Run the full Likeness Tier check on them first (see `skill_mode1_pitch.md`'s classification guard) — a pre-photographic or otherwise non-photographed figure with no confirmed life-portrait is very likely Reconstructable, and worth casting as an on-screen B-roll character via Mode 2 rather than skipping. Only keep them off-screen if they are genuinely plain Iconic tier (a confirmed, dense documented-from-life visual record) or if a Reconstructable attempt is actually tested and blocked.
3. B-Roll Extras — wardrobe blocks, not character sheets:
   - **Anonymous b-roll extras are no longer cast as character sheets.** Two findings retired that: b-roll is charcoal and graphite drawing on toned paper, which a photoreal sheet cannot drive; and passing a reference image for anonymous crowds produced roughly twenty clone faces in testing. Extras are generated from **description alone, with no reference image**.
   - Check `STUDIO_ASSETS.md`'s Era Stock Extras list for a registered **wardrobe text block** that fits the era and role. Reuse it byte-identical, the way `LOCK` is reused.
   - For a role with no registered block, write one: a single paragraph naming garments, armour, headgear, footwear and colour, plus an explicit exclusion of the famous-but-wrong silhouette. **Run the Period Accuracy Gate from `skill_mode2_cast.md` first** and state the evidence in one line beneath the block.
   - Once the user approves a block for reuse beyond this arc, register it in `STUDIO_ASSETS.md`. A block that stays arc-specific stays in the outline.
   - **A named, individually-identifiable b-roll figure is different** — if the outline needs a specific real person on screen (a commander, a rival), that is a Mode 2 casting job with the full Likeness Tier check, not a wardrobe block.

## Direct address hands off with a turn, and the outline says so

**When a direct-address beat is followed by the same character speaking in the studio, write the
hand-off as a physical turn** — he finishes to camera, turns his head toward the guest on the last
word, and the next shot opens already facing the guest.

This is a writing decision, not a production one, because the turn has to be *motivated by the
line*. A hand-off line that ends on "Tonight she answers for herself" turns naturally; one that
ends mid-thought does not.

**The same applies going the other way** — a sign-off that turns from the guest to camera is written as a turn motivated by the line, just reversed.

⚠️ **Without it the cut is a jump.** Direct and cross seed frames share a camera, a framing and a
chair — only the eyeline differs, so a straight cut moves the eyes and nothing else. See Mode 4,
*"never cut straight from a direct-address frame to a cross-shot of the same character."*

## The hook line — the first thing anyone hears

`BRAND_opening` carries a **4.00-second hook slot, 4.00–8.00 s**, between the disclosure card and the
intro, and the line that goes in it is nominated here. *(This section used to say a 6.17 s slot with
a 2.17 s hold — superseded when the card moved inside the opening; `SERIES_FURNITURE.md` is the
authority.)*

**It is a lift, not a new line.** Mark an existing guest line in the outline as `HOOK`. Writing a
line that exists only in the teaser makes a promise the episode does not keep — the audience hears
it again in context twenty minutes later, and that second hearing is the payoff.

**Treatment (2026-09-22):** the hook is not a studio shot — the guest's face emerges from the opening's paper while the line is spoken (`SERIES_FURNITURE.md`, *The hook treatment*). Choose a take where the face is turned toward the camera side and the mouth closes cleanly after the line.

**Short, then a hold. About ten syllables.** A strike opens the slot, the line plays over the decay,
and the next strike at 8.00 opens the intro. **The best hook is usually the shortest sentence** —
settled 2026-09-21, when *"Egypt did not survive without me."* (9 syllables, 2.1 s) beat the two-
sentence line first nominated (3.9 s, no room to breathe). Aim for **2–3 s of line and 1–2 s of hold
on the guest's face**: the hold is where the line lands. The hold is **live** if the take has a clean pause
after the sentence (mouth closed, no breath for the next line), otherwise a **freeze frame** on the
last closed-mouth frame — which is a legitimate dramatic device here, not a patch.

**It is the guest's voice, not the host's.** A dead person saying something startling before any
branding *is* the premise; a host introducing the episode is narration.

**Nominate a clip, not just a line.** The slot carries picture — the edit lifts the whole shot, so
the line has to come from a **cross-shot of the guest**, never the wide, which carries no dialogue.
The line is followed by a hold on that face before the intro begins, so pick a shot whose last beat
is worth sitting on. A line that ends on a blink is a line
that dies in the hold.

**The outline's `HOOK` is a first option, not the choice — settled 2026-09-23 (Salah).** The final hook is
picked **from the finished episode**: the most shocking guest moment on screen, where line, face and
delivery work together. It may be any guest sentence in that part, still a lift. Mode 6 makes the
pick at the hook render. Mode 3 still nominates one, so the opening can be built and read.

**Nominate provisionally, confirm on the generated take.** The outline names a line; the final choice is
made by watching the clip, because delivery decides which sentence carries. Mode 4 records the in and
out points.

**Choose the line that is hardest to walk away from, not the one that summarises best.** A summary
tells the audience they already know what happens. A hook should make the rest of the episode feel
necessary.

It carries its provenance tag like any other line. A `[V]` line is the usual right answer here —
voice rather than assertion — but if the hook states a fact it must be `[D]` and it must survive
the same source check as the body.

## The Knowledge Gate — what a guest can know

Sibling to the Period Accuracy Gate in Mode 2. That gate checks what things **look** like; this one checks what a guest can **know**, and whether a described event happened the way the line says. Same class of error, different axis.

**The frame, restated from Mode 1:** the guest speaks from outside their own life, knows their whole story and what was said about them since, and answers as themselves. **The host carries posterity; the guest answers from experience.** The host puts the later claim and the modern framing; the guest never cites a source, never uses modern vocabulary, and never sounds like a historian.

For every line, check:

1. **Is this in the right mouth?** Later interpretation, scholarly framing and posterity's verdict belong to the host. The guest supplies what they did, saw and intended.
2. **Did the event happen the way the line describes it** — not just the right place and date, but the right *method*?
3. **Is a named specific available instead of a vague one?** Named places and people are better drama and easier to verify.

**Worked example, caught after it had passed every other check:**

> *"Octavian's forces have landed in the delta. They are already ashore."*

"Landed / ashore" reads as an amphibious assault. Octavian advanced on Egypt **overland from Syria, taking Pelusium** on the eastern edge of the delta; the seaborne pressure that summer came from the **west**, with Cornelius Gallus at Paraetonium. Right geography, wrong method — and the vaguer phrasing is what let it pass.

> *"Octavian has taken Pelusium. He is at the eastern edge of the delta, and he is coming."*

Accurate, and better writing.

## Source Provenance — the published list is derived from the script

Publishing a source list in the description is making a claim. So the list is **generated from the script**, never assembled beside it.

**Every line carries a tag, assigned here at outline, not retrofitted later:**

| Tag | Meaning | Requirement |
|---|---|---|
| **[D] Documented** | attested in the record | the source is named on the line |
| **[I] Inferred** | consistent with the record, a reasonable reconstruction | the basis is named |
| **[V] Voice** | connective tissue, rapport, phrasing, transitions | carries no factual claim |

**Hard rule: a [V] line may not contain a factual assertion.** This is the discipline that keeps invention out of the parts an audience will believe, and it is the whole reason the tagging is worth the effort.

### The standard: nothing a critic could call a lie — settled 2026-09-18

**This is not an academic citation exercise and must not turn into one.** The show does not need a
footnote per sentence. It needs to never say a thing that someone can demonstrate is false, and to
have something respectable behind anything it does assert. That is the whole bar.

**What creates exposure is a *falsifiable specific*** — a number, a date, a kinship or title, a
"who did what to whom", an absolute like *first*, *only*, *never*. Those are the things a critic can
look up and disprove. Texture, atmosphere, rhythm and character carry no exposure at all, and
policing them is wasted effort.

**Both of Part 1's errors were written from memory.** "A dead cousin" and "four months" *sounded*
attested because they are the shape an attested fact takes. That is the more dangerous failure than
invention, because it does not feel like guessing. So: **look it up while the line is still text.**
Minutes, and free. Never write the sentence and hunt for support afterwards — that finds
confirmation, not truth.

**The burden sits here, on the writer, and never on the person running the channel.** He is not a
historian and cannot be the check. A line reaching him for verification is a process failure.

**What counts as respectable support:** a primary text (Plutarch, Dio, Caesar, Cicero), a modern
academic book (Roller, Chauveau and their kind), or a scholarly reference work. **Wikipedia is a
finding aid, never a citation** — use it to locate the real source, then cite that. A blog, a video
or "everyone knows" is not support.

⚠️ **Widely repeated is not attested.** Much of what "everyone knows" about Cleopatra descends from
the Augustan propaganda this show exists to push back on.

### The cheapest safety valve: give it to the guest

**When a specific cannot be nailed down, move the claim into the guest's mouth as their reading — retag `[D]`
→ `[I]` and name the basis.** A character's characterisation cannot be a lie; an assertion by the
programme can. It costs nothing, needs no rewrite and no regeneration, and it is usually the better
writing, because a hostile witness is more interesting arguing than reciting.

Worked example, `P1_024`: *"My family had been killing each other for the throne for two hundred
years."* Ptolemy IV's accession purge in 222 BC is **174 years** before she speaks, and rival-brother
killing runs back further to Ptolemy II — so the figure is a fair characterisation and a false
precision at once. Tagged `[D]` it was the programme asserting a number. Tagged `[I]` it is hers.
**The line did not change.**

The other two moves, in order of preference:

1. **Drop to the level every source agrees on.** *"Four months"* → *"A winter"*. Still true, still
   hers, and it almost always reads better than the number did.
2. **State the consensus where there is one**, cited — and where the sources genuinely disagree,
   `[D]` is simply the wrong tag. Never pick one reading quietly.

⚠️ **Re-run the duration model on any line you change.** *"A winter"* is one syllable longer than
*"Four months"* and pushed a 9s clip to 10s.

### Hard rule: there is no such tag as VERIFY — settled 2026-09-18

**A line does not leave Mode 3 with a check outstanding.** Part 1 shipped two `[D]` lines carrying
"VERIFY before publication" notes, and they sat there for weeks as work parked on the one person
who cannot do it in the middle of an edit. **That is not a tag, it is a deferred decision**, and
deferring it is worse than it looks: the line is *spoken*, so by the time anyone checks it the clip
exists and a one-word fix costs a regeneration and a voice pass.

When a claim cannot be verified as you write it, take one of three exits — never a fourth:

| | |
|---|---|
| **1. Verify it now.** | Look it up while the line is still text. Minutes, and free. |
| **2. Cut the unverifiable precision.** | Keep the claim, drop the part the record does not support. *"Four months"* → *"A winter"*: still true, still hers, nothing invented. **This is usually the right answer** — precision that no source carries is decoration, and dropping it costs the line nothing. |
| **3. Retag `[D]` → `[I]` and let the guest own it.** | Put the claim in the guest's mouth as their reading rather than as the record's: *"was supposed to have willed"* rather than *"had willed"*. Often the better performance too — a hostile witness is more interesting sceptical than encyclopaedic. |

⚠️ **Check the whole line, not the doubtful word.** Part 1's flag said *"'cousin' is loose"* — the
kinship. It said nothing about the will in the same sentence being contested, which was the larger
exposure by far. **A flag records where someone felt uneasy, not the extent of what is wrong
there.** When any part of a `[D]` line is doubtful, re-read every assertion in it: name,
relationship, number, date, and the causal claim joining them.

⚠️ **Watch the syllable count when you fix one.** A one-word swap can push a clip past its duration
floor — *"A winter"* is a syllable longer than *"Four months"*, which moved a 9s clip to 10s. Re-run
the duration model on any line you change, at outline, where it costs nothing.

The description's source list is then built from the [D] and [I] tags: nothing cited that is not used, nothing claimed that is not cited. Mode 4 carries the tags into the kit and audits them before generation; Mode 6 renders the list.

Tagging at outline costs a few seconds a line. Retrofitting it to a finished kit means re-deriving the basis for every line against the sources — hours. Do it here.

## The outline file — one format, read by tools

Added 2026-09-23. **The words are settled here, before Mode 4 writes a single prompt**, so the outline is
written in one fixed format that the gates and the script read can parse. Both parts in one file.

```
# OUTLINE — <Guest>

### Pronunciation
| Word | Say it | note |
|---|---|---|
| Ptolemaic | tol-uh-MAY-ik | |

## Part 1 — <title>
### Opening
HOOK: "<one guest sentence, verbatim from this part>"
### Act A — <title>
QUESTION: <the act's question, one line>
HOST: "…" [V]
> OVERLAP guest — <the listener's physical reaction>
GUEST (dry, even): "…" [D — Plutarch, Antony 27]
> OFFMIC HOST: "In daylight." [V]
> BEAT
> BROLL — <what the viewer should see>
> CUT-IN:hold — HOST: "But he—" [V]
> SPLIT at "<the sentence where the line turns>"
> TWOUP — <the moment both faces matter>
> CARD WHO | Octavian | <8–14 word gloss> | <source> @ "Octavian"
> PULL "<key line>"
> ACTBREAK — BRAND_actbreak_vessel
### Close
## Part 2 — <title>
…
```

- **A spoken line** starts the line with `HOST` or `GUEST`, an optional delivery note in brackets, a colon, the words in straight double quotes, then the provenance tag. Interrupted words go inside the quotes as `—[the words that get cut]`.
- **A direction** starts with `> ` and a toolkit tag (below), `CARD` or `PULL`. Off-camera and interrupting lines carry their words, so they are read and gated like any other.
- `HOOK` must be a verbatim sentence of that part's guest lines — the script read flags it otherwise.
- **`> ACTBREAK — BRAND_actbreak_<vessel|stone>`** marks where each of the part's two act breaks falls (added 2026-09-23). Put it at the end of an act that closes on an open loop; the script read shows it, and Mode 4 places the fixed `BRAND_actbreak` there.

**Gates on the outline** (all read the outline format directly):

```bash
python3 Fixed_Assets/tools/junction_scan.py Episodes/<Guest>/OUTLINE.md   # must print nothing
python3 Fixed_Assets/tools/lines_check.py  Episodes/<Guest>/OUTLINE.md    # banned phrases + every rare name pronounced + no unmarked stop-cluster last word
python3 Fixed_Assets/tools/script_read.py  Episodes/<Guest> --outline     # → SCRIPT_READ.md, both parts
```

## The director's toolkit — how a real conversation moves, decided here

Added 2026-09-20. **You are the director.** Nobody downstream will ask for these moments; the
outline is where they are chosen, because only the outline sees the drama. Mode 4 builds each one
into rows, Mode 6 cuts it. Use a tool **when the moment calls for it** — the test every time is
*would two real people in this room do this here?* — never to fill a quota and never on a fixed
rhythm.

**Wording in this section is guest-neutral.** *He* is always the host (fixed for the series); the
guest is *the guest*, and their label, pronouns, register and interruption style come from the
**performance profile** in `Episodes/<Guest>/CAST.md` (Mode 2). Cleopatra lines are marked examples.

| tool | tag in the outline | reach for it when |
|---|---|---|
| Reaction on the listener | `OVERLAP` | the listener's face is the story: a claim landing, a premise being quietly refused, the beat before an answer. The speaker's voice runs on under it. **Always when a line is *about* the listener** — naming, introducing, thanking or charging them plays on *their* face. The welcome is the first case: the guest is seen being introduced before being heard. **Screen share (2026-09-24):** the guest carries ≥ 65% of the picture, so most host questions play on her listening anyway (Mode 4 builds that by rule — no tag needed); `OVERLAP host` marks the few reactions of his worth showing, which Mode 4 builds as two-ups; mark at most one or two as *full frame* (`OVERLAP host, full`). |
| Interjection on camera | `NOD` | he could not have stayed silent: *"Mm. That's fair."*, *"But you knew."* — and his face is worth seeing. |
| Interjection off camera | `OFFMIC` | the same, but the other face matters more — e.g. his *"In daylight."* heard while we watch the guest. Works in either direction. |
| Held beat | `BEAT` | a line needs air after it. Silence, no one speaks, **on one face** (name whose: `BEAT — on her`). **About 1 s after the last word** — longer reads as dead air (Salah, 2026-09-24); up to ~1.5 s only for the single biggest moment of a part. |
| Picture over a voice | `BROLL` | the words describe something the viewer should see, or a long answer needs relief. |
| Interruption | `CUT-IN:<kind>` | someone cannot let the other finish. Kinds below. |
| Both faces at once | `TWOUP` | both faces matter at the same moment **while one of them is talking** — an interruption that fails, a charge landing on the listener as it is said, an echoed line. 🔴 **Never for a silence or two people only reacting** (T6b, 2026-09-24: it reads as empty) — a silence is a `BEAT` on one face, normally hers. **Since 2026-09-24 it is also how a host reaction during the guest's speech is shown** (an `OVERLAP host` becomes a two-up in Mode 4, so she stays on screen). **At most 7 per part**, a few seconds each, never two in a row. Never for plain back-and-forth. |
| Split line | `SPLIT` | one speaker's line **turns** — its mood changes at a sentence, or a gesture must land on one word — and the moment matters: the crack, a key line, a long line with a turn. Mark the sentence where it turns. Never a default (Mode 4 §2, *One beat, one clip*). |

**Interruptions — the kind is part of the decision**, because each is performed and cut
differently (Mode 4 §8b builds them):

| kind | what happens | what the viewer sees |
|---|---|---|
| `cut` | stopped mid-flow, pressing a point, unaware until the last word | the speaker's hand moving with the point — then they **stop**: lips close, eyes to the other, the other voice already over theirs — then the interrupter |
| `seen` | the speaker sees it coming | first *the interrupter* leaning in, drawing breath; then the speaker's hand stopping mid-air, brows lifting, as the other comes in |
| `yield` | the speaker gives way | they stop, open a hand toward the other, and let them in — we stay on the one who yields |
| `hold` | the interruption **fails** | we stay on the speaker: the other's *"But—"* heard off camera, the speaker's chin lifts, they carry straight on |

Write an interrupted line **with the words that get cut off**, after an em-dash in brackets:
*"Rome never once —[acknowledged the treaty it signed]"*. The bracketed words are performed and
thrown away; nobody is ever asked to stop mid-sentence. For `hold`, nothing is cut. Write the
interrupter's line as a reply to what was actually heard.

**Choose from character, not variety — read the guest's *interruption style* in `CAST.md`.** For
example, Cleopatra does not yield to a Roman framing — `hold`, and `cut` when she is the one cutting
in, are hers; a frightened witness would `yield`, a zealot would `cut`. The host concedes easily and
never bullies — `yield` suits him, and he interrupts rarely, only to stop an evasion. A guest cutting off a leading question
before it lands is the strongest use in the format.

**Judgement, not a quota.** A tense exchange wants several tools close together; a long answer that
is holding attention wants none. As a sense of scale, a part might carry two or three `OFFMIC`,
a handful of `OVERLAP` and at most one or two `CUT-IN` — but a part with none is fine if nothing
earned them, and a whole act with no non-speaking moment at all is almost certainly wrong. Never put
a `CUT-IN` where the cut would drop the fact a `[D]` tag documents.

## The story engine — what makes the part worth watching

Added 2026-09-22. The rest of this mode makes each *line* right — true, speakable, well delivered.
This section makes the *story* right. Apply it while building the act structure, before dialogue.

1. **Every act is a question the viewer wants answered.** The act opens on it, **turns**, and closes on
   a new question the next act pays. The part as a whole answers the central question from the pitch
   (Part 1: statecraft or surrender). Write each act's question in the outline, one line.
2. **The escalation ladder.** The host's questions climb through the part: **biography → the decision →
   its cost → the charge → the thing the guest will not say.** Each act takes at least one rung. A part
   whose questions stay on the same rung feels flat however good the answers are.
3. **One myth-vs-record reversal per act.** *"What you think you know is wrong — and here is the
   source."* The strongest engine a history show has: it rewards the viewer for staying and gives
   them something to repeat. Plan it, source it (`[D]`), and give it a context card or a pull-quote if
   it earns one.
4. **One concrete image per act,** taken from the sources — a head kept at the shoreline, a harbour on
   fire, sixty ships. Abstractions (*legitimacy, position, power*) are what the image is *about*; the
   image is what the viewer remembers. It is also the obvious b-roll.
5. **One crack per part.** A single moment where the guest's composure costs them something, inside
   the *emotional ceiling* of the performance profile. Without it a composed guest reads as flat over
   ten minutes; with more than one, composure stops meaning anything.
6. **Subtext over statement.** The guest never names their own feelings. The host says the obvious
   thing so the guest can refuse it — the refusal carries the feeling.
7. **The promise and the payoff.** The title and the hook promise something; the part pays it, and the
   cliffhanger is the question the viewer actually came for, left open.
8. **Cut what does nothing.** Every line either moves the question, turns it, or earns a laugh or a
   breath. A line that only restates the previous one goes, even if it is true.

### The script review — the words are approved here, before Mode 4

Added 2026-09-22; **moved to the outline and made arc-wide 2026-09-23.** Nothing is built on the words
until they have been reviewed twice — and they are reviewed **as text, for both parts together**, before
Mode 4 turns them into ~90 prompts per part. A change marked here costs an edit; the same change marked
on a kit costs a rewrite of every row it touches.

1. **Story review (Claude)** → `Episodes/<Guest>/STORY_REVIEW.md`. Score every act of **both parts**
   against the eight points above, in a table: its question, the ladder rung, the reversal, the image,
   the turn, the open loop. Then list **lines that do nothing**, **moments a newcomer would not follow**,
   and **where a viewer is most likely to leave**. Then the two arc checks: **does Part 1 stand alone**,
   and **does Part 2 pay exactly what Part 1's cliffhanger and titles promised?** Then a **cold-reader
   pass** — read it as someone who has never seen the research, because knowing the history hides exactly
   what a newcomer will not follow.
2. **Script read (Salah)** → `python3 Fixed_Assets/tools/script_read.py Episodes/<Guest> --outline` writes
   `SCRIPT_READ.md`: both parts as a viewer would meet them — speakers, lines, delivery notes, silent
   beats, cards, pull-quotes, act breaks, and an estimated running clock per part from the duration
   model. Salah reads it as a viewer and approves or marks changes. **No audio is generated for this.**
3. Changes go back into `OUTLINE.md`, the outline gates re-run, the read is regenerated, and **only an
   approved read goes to Mode 4.**

**Decide, don't ask — added 2026-09-23 (Salah: *"update the skill to make the same decision for things like
this"*).** Some calls are craft, not taste, and Mode 3 makes them itself. It writes the decision in
`STORY_REVIEW.md`, where the script read still catches it, and never queues it as a question:
- **Newcomer clarity.** A unit, currency, office, title or practice the argument depends on, and a general
  viewer cannot picture (a *talent*, a *triumph*), gets a context card, or a one-clause gloss in the line.
- **Runtime a little under target.** A part up to ~1 minute short of 10 minutes that is tight and pays its
  promises is accepted, not padded. Lengthen only with sourced material that moves a question, never
  with restatement.
- **Cutting a line that does nothing,** when the story review names it and nothing depends on it.

What stays a question for Salah: anything that changes the charge, the arc or the crack, anything on
the sensitive-material list, and anything he has asked to decide himself.

Mode 4 can still render a read from a finished kit (`script_read.py Episodes/<Guest> <part>`) — that is a
quick check that the kit says what the approved outline says, not a second review.

## Holding attention across a part — the writing side

Added 2026-09-20 from long-form interview and retention practice, fitted to this show's fixed
studio, two singles and 10–12 minute spine. None of it adds runtime; it decides what the minutes do.

- **One question is the spine; come back to it.** Each part has a single charge (Part 1: statecraft or
  surrender). **Every act opens by reconnecting to it and ends on an open loop** — a question, a
  promise, or an answer that opens more than it closes — which the next act pays. Viewers leave at
  the seams between topics; an open loop is what carries them across. With four acts in ~11 minutes
  that is a re-hook roughly every 2–3 minutes; an act that runs past ~3 minutes gets a mid-act tease.
- **Front-load the density.** The first three minutes carry the most turns, the shortest answers and
  the most toolkit moments; later acts can hold a long answer when it earns it. Retention is steepest
  early, and a slow opening is paid for in every minute after it.
- **The second answer.** After a guarded answer the host says nothing — a `BEAT` on him — and the guest
  adds the real one, shorter and truer. Once or twice a part, at the moments that matter most. Silence
  pulls more from a witness than a follow-up question does, and it reads as confidence in the host.
- **Callbacks.** Let a later line pick up an earlier phrase (*"In daylight."*). It tells the viewer the
  conversation is listening to itself, and it rewards the ones who stayed.
- **Don't bury the payoff.** Each act's strongest line lands in the act, not in its last seconds; the
  end of the act is for the open loop.
- **Cut the goodbye.** The part ends on the tease (*"Part two, and the sixty ships."*) — no thanks, no
  pleasantries, no subscribe line in dialogue. The retention graph is already falling there.

## Writing the lines — realism rules from the original master instructions

Restated 2026-09-22 against the current pipeline, which has **no TTS stage**: Kling performs every
line, and anything written inside the quotation marks is spoken aloud.

- **Zero melodrama.** Banned outright: *tapestry, delicate dance, alas, a testament to, sands of time,
  echoes through, the annals of, stood the test of time, little did, the rest is history, delve,
  unravel, shed light, a pivotal, rich history, fabric of, beacon of* — the full list is in
  `Fixed_Assets/tools/lines_check.py`, and the gate stops any kit that uses one. Add to the list,
  never remove.
- **HBO realism.** Punchy, tense, conversational. Contractions follow the character: the host uses them
  naturally; each guest's habit is in the performance profile (Cleopatra: formal, none). Friction comes
  from the director's toolkit — interruptions, off-mic interjections, the second answer.
- **Punctuation.** An em-dash inside a line is a spoken break (it costs 1.3 s in the duration model, v4).
  **Interruptions are not written as a dash for the model to perform** — they are built in the edit
  (toolkit, `CUT-IN`). A **trailing thought (`…`)** is allowed where the character genuinely lets a
  thought go; the first time a kit uses one, check that take before writing more — how Kling performs
  `…` is untested.
- **Vocal artifacts** (*sharp inhale, sighs, clears throat*) — the master file put them in brackets in
  `tts_text`. Here a bracket inside a quote is read aloud, so they are written **as physical beats in
  the gesture paragraph** (*"he draws a breath before the last sentence"*), one per clip at most, and
  never as a blink (Mode 4 §5).
- **Pronunciation — every rare name gets one, written here.** For every proper name or term a general
  English speaker might mispronounce, add a row to the outline's **Pronunciation** table:
  `| Word | Say it |` with the stressed syllable in capitals (*Ptolemaic — tol-uh-MAY-ik*). Mode 4
  carries the table into the kit, adds a **Respell** for any word the model is likely to get wrong, and
  writes the respelling **inside the prompt's quote** (settled 2026-09-24, Mode 4 §3 3b — a separate
  pronunciation note is read aloud). This matters more than it looks: **the ElevenLabs
  voice pass cannot fix a mispronounced word** — it keeps the pronunciation of the Kling take — so a
  wrong name is baked into the clip. `lines_check.py` flags any rare name that has no entry.
  🔴 **The host's welcome names the show, every part (2026-09-28, Salah).** The title card shows it, but listeners and
  background tabs never see it. Part 1's welcome: *"Welcome to History Answers Back. <guest, styled>. Thank you for being
  here."*; later parts: *"This is History Answers Back. <guest> — welcome back."* One mention per part, in the welcome only.
  🔴 **Don't open a line on a lone word (2026-09-27, Salah, L50).** Kling read *"Allies."* — the first word of `P1_046`,
  a one-word sentence — letter by letter, as written, not as the word is said. A lone word at the top of a clip has no
  context to tell the voice how it sounds. Give it some (*"Allies, not lovers."*) or, if the beat needs the single word,
  give it a Pronunciation row. `lines_check.py` warns `OPEN1` (names, *yes/no* and table words are exempt).
  **A word that fails twice gets replaced, not respelled again.** *Allies* came out *"a-LEEZ"* three ways (alone, respelled *Allize*, and in *"Allies, not lovers"*) — in her placeless accent the word itself fails. Mode 4 proposes a same-meaning rewording to Salah (*"Not lovers. That night I became his ally."* — *ally* was said right in the same take) and the outline is changed with his OK.
  🔴 **EVERY name and place gets a row — not just the rare ones (2026-09-27, Salah, L53).** *Antony* was never in the
  table (too common to flag) and the host said *"Antony's"* as *"Antoy's"* (`P1_106`). Every person and place named in a
  spoken line gets a row, and each **possessive or plural form gets its own row** (*Antony's*, *Caesar's*, *Romans*).
  Respell (`write:`) any name whose letters don't say how it sounds — *Caesar → Seezer*, *Antony → Antonee*, *Pompey →
  Pompee*, *Cyprus → Syprus*, *Ides → Eyeds*; `plain` only where the spelling already reads right (*Rome, Egypt, Syria*).
  `lines_check.py` fails `NAME` on any name without a row.
  🔴 **Every row carries a decision in its note column (2026-09-27, Salah, L48):** `write: <respelling>` or `plain`.
  Default to `write:` for any name with a silent letter, an unusual vowel cluster or a non-English ending (*Arsinoe →
  Arsin-oh-ee*, *Ptolemies → Tolemies*, *Charmion → Karmion*); `plain` only for names an English speaker already says
  right (*Octavian, Actium, Tarsus*). **Stress homographs** — noun/verb pairs like *allies, record, present, object* —
  get a row too when they stand alone or carry the line (*"Allies."* after *"lovers"* came out wrong in `P1_046`). The
  builder respells from the `write:` column. 🔴 **A respelling is ONE plain word — no hyphens, no capitals inside (L49):** *Arsin-oh-ee* made her say the name syllable by syllable, like a correction (`P1_055`); *Meeds* and *Tolemies* (plain words) read naturally. Write *Arsinowee*, *Peloosium*, *Karmion*; `prompt_check.py` fails a raw `write:` word in a quote and a row with no decision.

## Emotion is written as restraint

Added 2026-09-20. The outline decides *what a beat feels like*; Mode 4 §4 writes it into the prompt.
Two rules carry over to the writing:
- **Give the feeling to the words, not to an adverb.** A line that is hard to say plainly carries more
  than a line delivered "bitterly". If the emotion only exists in the direction, the line is too weak.
- **Mark the ceiling, not just the beat.** When an act calls for anger, name what it stops short of —
  this show's people hold things down. That note travels into the prompt's delivery line.
- **Every answer has an arc — write it, sentence by sentence.** Added 2026-09-22. A multi-sentence
  answer is not one feeling held for twelve seconds; it *moves*. Each sentence does a different job —
  corrects, asserts, concedes, costs something, lands — and carries a slightly different temperature.
  *"You assume those were two things."* (cool correction) → *"For me they were one."* (plain statement)
  → *"Egypt did not survive without me."* (weight, pride held under) → *"And I was nothing without it."*
  (quieter, the admission). **In the outline, give every line of two or more sentences a beat map**: a
  few words per sentence naming its job and temperature. If every sentence gets the same word, the
  answer is flat — rewrite the line, not the direction. The shifts stay small and inside the guest's
  *emotional ceiling*; it is a temperature change, not a mood swing. Mode 4 §4 writes the map into one
  prompt, one delivery note per sentence, with a physical beat between sentences where the body
  should change (the default, and free); only a turn too big for one clip becomes a `SPLIT`.
  **Settled 2026-09-24 (test T2): the model plays it.** Write the map as **one note per sentence, separated
  by `→`, exactly as many notes as sentences** — Mode 4 turns a matching map into the prompt automatically
  and falls back to a single note when the counts differ. Each note is spoken as a **manner** the model can
  perform (*cool, plain, dry, quieter, with weight held under*); a job label on its own (*"the premise"*,
  *"the question"*) gives it nothing to play — pair it with a manner (*"the premise, level"*).
  **Write each note as a simple tone Kling can hear** (added 2026-09-24): *dry, plain, quiet and
  serious, low and firm, coolly polite, warm*. No "then" inside one note (that is two sentences —
  give each its own note), no metaphors (*"the ceiling holding"*). Mode 4 maps every note to a Kling
  phrase in `tone_map.py` and stops on one it has no mapping for, so a plain note saves a stop.

## Context cards — who, where, what, written with the dialogue

Added 2026-09-20. **Every person, place or event the argument depends on gets a context card on its
first mention** — a short on-screen explainer for the viewer who does not know the story. It is
written here, beside the line that mentions it, because it is a factual claim and this is where
facts are checked.

- **Default to a card for any unit, currency, office or practice the argument leans on** that a general viewer
  cannot picture (*talent* → weight in kilograms and what the sum amounts to). Decided, not asked — see
  *Decide, don't ask*. Two cards never land within ~6 s of each other; move one to a later mention.
- **Pick by need, not by capital letter.** Card what a general viewer would not know and needs to
  follow the argument: *Octavian*, *Parthia*, *the Donations of Alexandria*. Skip what everyone knows
  (*Rome*, *Egypt*) and what the line itself explains. A part carries roughly eight to twelve.
- **Four rows:** label (`WHO` / `WHERE` / `WHAT`), name, a gloss of about **8–14 words that fits
  three lines**, and a source. The gloss says what the viewer needs *for this argument*, with one
  anchor date where it helps: *"Caesar's great-nephew and adopted heir; Antony's rival. From 27 BC,
  Augustus, the first emperor."*
- **Same rigor as a `[D]` line** — rule 1 above: look it up, never write it from memory. The
  research for Part 1's cards found a `[D]` error in a spoken line (Armenia had been taken, not
  "not yet taken"). Researching the cards is also a second audit of the lines around them.
- **Don't repeat the line.** If the next line says it, the card says something else.
- Name the **exact word** it lands on. Mode 4 places it.

## The wide never carries dialogue

**Any line that must be heard is a single.** This is structural rather than stylistic: ElevenLabs speech-to-speech converts a clip to **one** voice, so a two-speaker clip comes back with both characters sounding identical. A two-shot can carry a conversation as *picture*, never as *dialogue*.

Where a beat genuinely needs both characters and their words — the closing exchange is the model case — write it as **host single + guest single + a non-talking wide**. The lines survive the voice pass because each clip has one speaker; the wide supplies the geography.

Two legitimate modes for the wide:

| Mode | Model | Rate | Use |
|---|---|---|---|
| **Silent wide** | Standard 3.0, audio off | **8 cr/s** | establishing, a beat between acts, a held moment after a hard answer. Keep to 3–5s, or lay music under it — two people visibly mid-conversation but mute reads wrong if held long in silence. |
| **Conversing wide, audio discarded** | Turbo, audio on | 10 cr/s | only where music covers it: the close and the credit roll. |

**The silent wide is the cheapest clip type in the kit**, below every talking clip. Use two-shot beats freely for pacing — an outline may now reach for one where it previously had to avoid the wide entirely — provided the words live in the singles.

**The two-shot appears once, at the close** — as the first frame of `BRAND_bumper_out`, before it turns into charcoal. It is the only thing that shows host and guest in the same room, and it costs nothing extra because that frame is already a seed frame. **Do not write an establishing wide into the cold open**: it was removed on 2026-09-18 for a figure-to-chair scale fault that rerolling cannot fix. The cold open cuts from the hook straight into the singles.

**Budget note:** splitting a two-hander into singles plus a wide is three generations where a two-shot would be one. Worth it mid-episode for drama; not worth it for a close whose lines sit under a credit roll.

The escape hatch, if a future episode genuinely needs an audible two-hander: split the clip's audio at the turn, convert each segment against its own voice, reassemble. Costly and fiddly — write the outline to avoid needing it.

## Output Convention — prompts come to the chat, not only to the file
The outline document still saves to `Episodes/[Guest Name]/`, but every prompt it
contains is **also** delivered in the chat reply as its own fenced code block,
under a `PROMPTS TO RUN` heading at the top, before the document is discussed.

- One block per asset, in the order they should be generated.
- Above each block, a single label line: the filename it produces and where it saves.
- Each block is complete and standalone — never "same as the previous one but change X".
- The reasoning, sourcing and B-roll tiering stay in the saved file. The chat carries what gets pasted.

Hunting through a saved markdown file for prompts is friction repeated once per asset
per episode, and it is the point at which a working pipeline starts feeling like homework.
