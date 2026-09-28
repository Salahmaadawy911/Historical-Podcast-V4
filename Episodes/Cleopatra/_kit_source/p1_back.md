## 6 · Assembly

Done here (Mode 4 §9b), not handed off. Drop each clip into `Episodes/Cleopatra/shots/` named exactly by its id (`P1_014.mp4`); the filename is the only link to its row.

1. **Voice pass first** on all talking clips, before trimming; keep the raw Kling clips beside the converted ones.
2. **Strip 1152 samples from the head of every converted clip and loudness-normalise it** — ElevenLabs' MP3 carries one granule (26.1 ms) of head padding; the pass returns ~10 LUFS low. Both are measured properties of the pass, not per-clip judgements:
   ```bash
   ffmpeg -i in.mp3 -af "atrim=start_sample=1152,asetpts=PTS-STARTPTS,loudnorm=I=-19:TP=-1.5:LRA=7" -ar 44100 -c:a pcm_s16le out.wav
   ```
3. Probe every clip: duration, `silencedetect` at −38 dB for speech in/out, the noise floor.
4. Trim heads and tails **in silence**, never mid-phoneme. Close gaps to ~0.3 s inside an utterance, more at a genuine turn. A pause over ~1.2 s that is not a written `BEAT` is trimmed and hidden (punch, reaction, card or b-roll).
5. Lay reactions, b-roll and two-ups at the points their `edit_placement` names; J-cut speaker changes (the incoming voice leads the picture by a few frames).
6. **Level every chained join** with the per-clip gain in `shots/_measure/JOIN_GRADES.md` (`chain_frames.py` writes it after Pass 2). Normalise each b-roll clip against its own first frame (b-roll warms and darkens across a clip).
7. **`ROOMTONE_studio` under the entire part**, constant, never ducking — the voice pass strips the studio floor out of every clip.
8. Subtitles from the **Subtitle** fields; on-screen source credits on `[D]` lines only (a context card's source line *is* the credit when both would show at once).
9. **Finish twice:** a clean master (no text of any kind — Mode 5 cuts reels from it) and the titled master that is published.

What assembly cannot judge is a performance. If a take is clean and the read is wrong, the line goes back to `OUTLINE.md`, never rewritten here.

## 7 · Primary sources

- Plutarch, *Life of Antony* — the principal narrative (Tarsus, the Donations, the will, Actium), written over a century later from hostile Augustan material; used for events, not motive.
- Plutarch, *Life of Caesar* (the bedding sack, the ring, the fire, the Ides) and *Life of Crassus* (the attempt to annex Egypt, 65 BC).
- Caesar, *Civil War*, Book 3 — the contemporary Roman account of Pompey's death and Caesar in Alexandria.
- Cassius Dio, *Roman History*, Books 42–50 — the siege, Arsinoe proclaimed and led in triumph, Cleopatra in Rome, the war declared on her.
- Suetonius, *Julius* (the six thousand talents; Caesarion) and *Augustus*.
- Appian, *Civil Wars* 5.9, and Josephus, *Jewish Antiquities* 15.89 — Arsinoe's death at Ephesus.
- Horace, *Odes* 1.37 — the "fatal monster", written soon after her death.
- Modern: Duane Roller, *Cleopatra: A Biography*.

No verbatim quotation of Cleopatra survives. Her lines are reconstructed from documented actions and the sources above; `[I]` lines are her reading, and say so in their tags.

**Corrections the part makes on purpose** (named in the description, §9): the carpet (`[[B1]]`, a bedding sack per Plutarch), the Library (`[[B11]]`, books burned by the docks, scale disputed), and Tarsus as seduction (`[[C7]]`, a summons to answer a charge).

## 8 · Trust disclaimer

**On screen** — the first four seconds of `BRAND_opening` (`[[OPEN]]`), fixed wording, byte-identical in every episode: *AI-GENERATED DRAMATIZATION / Historical reconstruction, not a recording. / A conversation I wanted to hear.* The host does not say it aloud.

**In the description and on the end card** — the full statement:

> This programme is an AI-voiced dramatization. The guest is a historical reconstruction, not a recording. Dialogue is built from documented actions, primary sources, and academic consensus.

Studio's **Altered or synthetic content → Yes**, every part. Short version for reels: *"AI dramatization. Historical reconstruction, not a recording."* The on-screen guest is a direct AI portrayal built from coin portraiture and period evidence, not the cinematic image (`CAST.md`).

## 9 · YouTube metadata

**Titles** (Test & Compare set — the first is the primary)
1. Cleopatra: "They Wrote About My Bed" [Part 1 of 2]
2. Why Rome Declared War on Cleopatra, Not Antony [Part 1 of 2]
3. Cleopatra Answers for Caesar and Antony [Part 1 of 2]

**Description hook.** Rome declared war on Cleopatra, not on the Roman beside her — and the winners wrote her story. In Part 1, Cleopatra VII answers the charge that she seduced Rome.

**Summary.** Cleopatra VII sits down with History Answers Back to answer the word Rome gave her: seductress. In Part 1 of 2 she takes the charge apart from the beginning. Her family were Macedonian Greeks who had ruled Egypt for nearly three hundred years, and she was the first of them to learn Egyptian. Her kingdom was the richest in the Mediterranean and could not defend itself: her father paid Julius Caesar and Pompey nearly six thousand talents to be recognised as king. She tells how Pompey was killed on the shore at Pelusium and his head handed to Caesar; how she reached Caesar in Alexandria carried in a bedding sack, not rolled in a carpet; the siege of the palace quarter and the fire by the docks; her sister Arsinoe paraded in chains in Caesar's triumph; and Caesarion, the son she named Caesar. With Mark Antony the story moves from Tarsus, where she was summoned to answer a charge and arrived as Aphrodite, to the Donations of Alexandria, where Antony gave her children kingdoms Rome saw as its own. She answers for her sister's death, asked of Antony while Arsinoe was a suppliant in the temple of Artemis at Ephesus. Then Octavian takes Antony's will from the Vestal Virgins, reads it to the Senate, and Rome declares war on her, not on him. The part ends in 31 BC at the Battle of Actium, with the question the record leaves open: did she run? Every claim is tagged to Plutarch, Cassius Dio, Caesar, Suetonius, Appian, Josephus and Horace; her lines are a reconstruction.

**Heard vs the record.**
- *Heard:* she was smuggled to Caesar rolled in a carpet. *Record:* Plutarch says a bedding sack tied with a cord; the carpet came later. (`[[B1]]`)
- *Heard:* Caesar burned the Library of Alexandria. *Record:* the fire of 48 BC reached books by the docks; how many, and whether the Library itself, is still argued. (`[[B11]]`)
- *Heard:* Tarsus was the great seduction. *Record:* Antony summoned her to answer a charge of funding his enemy; she turned the hearing into a state visit. (`[[C7]]`)

**Tags.** Cleopatra, Cleopatra VII, Kleopatra, Julius Caesar, Mark Antony, Octavian, Ptolemaic Egypt, Arsinoe IV, Donations of Alexandria, Battle of Actium, ancient Egypt, Roman Republic, historical interview, history podcast, AI history

**Hashtags.** #Cleopatra #AncientRome #History

**Pinned comment.** She says "seductress" is what Rome calls a kingdom without an army staying alive. Statecraft or surrender — where do you land, and why?

**Playlists.** History Answers Back — the series playlist; Cleopatra — both parts in order.

**End screen.** Cleopatra, Part 2 of 2, and subscribe.

**Series index:** `[Part 1 of 2]`

⚠️ The quote in title 1 is her line in `[[A2]]`, verbatim. The primary title names the guest in its first word. `publish_sheet.py --words-only` checks both, and the three angles differ (quote / charge / event).

## 10 · Soundscape

**Dry by default.** Voice and `ROOMTONE_studio` carry the part; music sits at structural points only.

| Cue | Where |
|---|---|
| `ROOMTONE_studio` | under the whole part, constant, never ducking |
| `MUSIC_Theme_Main` | inside `BRAND_opening` and both `BRAND_actbreak` files — nothing to place |
| `MUSIC_Drone_Low` | enters under `[[A19]]` (Pompey killed, the head handed over), out across `[[A22r]]` — the darkest passage of Acts A–C |
| `MUSIC_Drone_High` | enters under `[[D1]]` (the will), rises through the war and peaks under `[[E2]]` (the sixty ships), out on `[[E4]]`'s last word |
| `MUSIC_Outro_Bed` | already running before `[[BUMP]]`'s transformation; decays under the drawing and the end card |
| `SFX_plate` | one soft paper settle on every lower-third, pull-quote and context-card entrance; exits are silent |

**Everywhere else is dry — including the Arsinoe crack (`[[C9]]`–`[[C14]]`).** The two-up and the silence carry it; a bed there would tell the viewer what to feel. B-roll arrives with its own ambience, ducked under any dialogue it covers. No movement foley.

## 11 · Packaging

**Chapter titles** — Mode 6 fills the timecodes into `P1_TIMECODES.txt` from the cut.

| chapter | starts at |
|---|---|
| Seductress, or a verdict? | `0:00` — the opening |
| A kingdom that paid to exist | `[[A1]]` |
| Carried in to Caesar | `[[B1]]` |
| Lover, or policy | `[[C1]]` |
| A war declared on her | `[[D1]]` |

**Thumbnail overlay lines** — 3–5 words, all caps, her own words where possible; not the title's words:
1. **"THEY CAME FOR MY TREASURY"** — the other half of the title's quote; the two read as one sentence across title and thumbnail without repeating.
2. **ROME DECLARED WAR ON HER** — the charge, for pairing with title 3.
3. **"A KINGDOM WITHOUT AN ARMY"** — her thesis (`[[D11b]]`), for pairing with title 2.

**Thumbnail** — built in Mode 6 from `thumb_portrait_cleopatra.png` by `Fixed_Assets/Branding/THUMBNAIL_SYSTEM.md`: kicker `CLEOPATRA VII · PART 1`, statement from the list above, output `THUMB_cleopatra_p1.png`. ⚠️ The file of that name in the folder today is the **v1** thumbnail (kept for comparison, `CAST.md`); the rerun's statement is new, so the thumbnail is rebuilt before publishing — `publish_sheet.py` would otherwise find the old file and pass.

## 12 · On-screen text

Placed here, rendered by `build_episode_cards.py`, never invented at the edit. One piece of text on screen at a time.

### Lower thirds — two, that is all

| | Opens over | Reads |
|---|---|---|
| Host | `[[A1]]` — his first cross-shot question | SALAH ALMAADAWY / *History Answers Back* |
| Guest | `[[W1]]` — her first appearance, the reaction as he names her | CLEOPATRA VII / *Last queen of Ptolemaic Egypt · 51–30 BC* |

Not over the hook or the direct address (frontal — no side to enter from). The host's welcome plays mostly on her face, so his banner waits for his first question.

### Key lines — three pull-quotes, and a fourth line for thumbnail and reels

| Line | Said in | Pull-quote lands over |
|---|---|---|
| "They came for my treasury. They wrote about my bed." | `[[A2]]` | `[[LA3]]` — her held face, after the line |
| "Rome does not thank you. It judges you." | `[[A22]]` | `[[LA23]]` — her held face, after the line |
| "A queen does not arrive at a trial as the accused." | `[[C7]]` | `[[LC8]]` — her held face, after the line |

Key line 4, **no pull-quote** (no silent beat follows it, and her thesis should not be interrupted by a card): *"Rome calls that seduction. It is what a kingdom without an army does, if it wants to stay a kingdom."* (`[[D11b]]`) — for the thumbnail and Mode 5.
⚠️ Pull-quote 01 is also the hook's first option. **If Mode 6 keeps it as the hook, drop `BRAND_pullquote_01`** — the same sentence three times is wallpaper.

### Context cards — who, where, what, on first mention

Opposite the speaker, upper band, 5.5 s, entering **as the word is said**: `L` when she speaks, `R` when he speaks. Glosses are Mode 3's, sourced like `[D]` lines. **A card never rides onto the other person's face** — each placement below was checked against the rows around it, and three cards moved from the host's mention to hers a second later for that reason (03, 07) or got a cover (05, 06, 08).

| # | Lands on | Word | Side | Label | Name | Gloss | Source |
|---|---|---|---|---|---|---|---|
| 01 | `[[A6]]` | My family | L | WHAT | THE PTOLEMIES | Macedonian Greek dynasty founded by Alexander's general Ptolemy; ruled Egypt 305–30 BC. | Roller, *Cleopatra* |
| 02 | `[[A12]]` | talents | L | WHAT | TALENT | Greek unit of weight: about 26 kg of silver. Six thousand is about 155 tonnes. | Suetonius, *Julius* 54; Britannica, "Attic talent" |
| 03 | `[[A19]]` | Pompey | L | WHO | POMPEY | Roman general, Caesar's great rival in the civil war of 49–48 BC. | Caesar, *Civil War* 3 |
| 04 | `[[B13]]` | Arsinoe | L | WHO | ARSINOE IV | Cleopatra's sister, proclaimed queen against her in Alexandria in 48 BC. | Cassius Dio 42.39 |
| 05 | `[[C1]]` | Tarsus | R | WHERE | TARSUS | City in Cilicia, southern Asia Minor, where Antony summoned Cleopatra in 41 BC. | Plutarch, *Antony* 25–26; Roller |
| 06 | `[[C21]]` | thrones | R | WHAT | DONATIONS OF ALEXANDRIA | 34 BC ceremony: Antony proclaimed Cleopatra and her children rulers of eastern kingdoms. | Plutarch, *Antony* 54 |
| 07 | `[[C27]]` | Octavian | L | WHO | OCTAVIAN | Julius Caesar's adopted heir and Antony's rival; later Augustus, Rome's first emperor. | Suetonius, *Augustus* |
| 08 | `[[D1]]` | Vestal | R | WHAT | THE VESTAL VIRGINS | Priestesses of Vesta in Rome, who held Antony's will in trust. | Plutarch, *Antony* 58 |
| 09 | `[[E1a]]` | Actium | R | WHERE | ACTIUM | Promontory in western Greece; the sea battle off it in 31 BC decided the war. | Plutarch, *Antony* 62–66 |

**How each clears a face:** 01, 02, 03, 04, 07 sit over her own long line (≥ 5.5 s of it left after the word; 04 rides on over `[[B14]]`). 05 holds over the host through `[[C1r]]`, a chained reaction covering her first sentence. 06 and 08 ride over b-roll (`[[C22]]`, `[[D2]]`), which cuts back to her only after the card has gone. 09 sits over him and runs on over `[[E2]]`. None overlaps a lower third or a pull-quote.

## 13 · Still outstanding for Part 1

- **The test batch** (§4b) — six questions; T4 has no qualifying line here and stays open.
- **The hook** — first option only; re-picked by Mode 6 from the finished part.
- **The thumbnail** — rebuild with the new statement (§11) before publishing.
- **`publish_defaults.json`** still has the series playlist as `TODO` — blocks the publish sheet, not generation.
- **ElevenLabs** on the paid tier for every published clip (free-tier output cannot be relicensed).
- **Credits** — record the actual Part 1 spend, retakes included (NEXT_STEPS A5).
