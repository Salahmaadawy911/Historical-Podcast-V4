---
name: "history-answers-back"
description: "Run a production mode (1-6) of the History Answers Back podcast. Use when the user says 'run mode N', names a guest or part, or asks to continue the show's pipeline."
---

# History Answers Back — running a mode

The project lives in two places, kept the same:

- the GitHub repository **`salahmaadawy911/historical-podcast-v4`** — what a cloud session clones and works in;
- the user's Mac at `~/Downloads/Historical Podcast V4/`, reached through the linked-computer bridge from the desktop app.

Work where the session is. In a cloud session, work in the repository checkout and commit and push at the end. On the
desktop, if no folder is connected, ask the user to connect that folder before doing anything else. If neither is
available, stop and say so; nothing in this skill works without the project files.

The whole pipeline is mapped in the artifact **The Running Order** (https://claude.ai/artifact/L98t6WjsEfE9G2XuFiHVP7). Read it with the Artifact tool (`action: "read"`) when you need the big picture.

## Which chat runs what

- **Modes 1, 2 and 3 share one chat** for a guest — they are light, text-only, and Mode 3 needs the pitch and cast fresh in mind. For a guest whose face and voice already exist, Mode 2 is an audit only: check `CAST.md` against today's spec and regenerate nothing.
- **Mode 4 runs in its own chat, one per part** — the kit, the gates, the renders, then generation.
- **Mode 6 (assembly, the edit and the publish sheet) runs in its own chat per part; Mode 5 after it.**

Finish, save, and tell the user which chat comes next. Do not carry on past the end of a chat's modes.

## Start of every run — in this order

1. Read `NEXT_STEPS.md` — current state, what is done, what is open.
2. Read `Fixed_Assets/LESSONS.md` — every production problem so far and where it is now prevented. Only rows marked **live** (or the live part of a **partly live** row) are rules.
3. Read the mode's skill file in the project root:
   - Mode 1 `skill_mode1_pitch.md`
   - Mode 2 `skill_mode2_cast.md`
   - Mode 3 `skill_mode3_outline.md`
   - Mode 4 `skill_mode4_produce.md`
   - Mode 5 `skill_mode5_reels.md`
   - Mode 6 `skill_mode6_edit.md`
4. Read its **Inputs and output** block and its **Tested and ruled out** list, then every input file the block lists for this guest from `Episodes/<Guest>/`.
5. Read any other file the skill tells you to read before starting (for example `STUDIO_ASSETS.md`, `Fixed_Assets/VOICES.md`, `Fixed_Assets/SERIES_FURNITURE.md`).

If an input file the block lists does not exist, stop and tell the user which earlier mode has to run first. Do not reconstruct a missing pitch, cast or outline from memory.

## The order of work — where the user signs off

1. **Mode 1** → `PITCH.md`. The user approves the guest and the charge.
2. **Mode 2** → `CAST.md`, the pose library (about nine frames, made by editing the reference frame, each passing `frame_set_check.py` and an eye check), `poses.py`, the voice and its reference render, the thumbnail portrait. No wide frames. The user approves face and voice.
3. **Mode 3** → `OUTLINE.md` for **both parts**, in the fixed outline format, with a Pronunciation row (`write:` or `plain`) for every name. Run the outline gates on it (`junction_scan.py` and `lines_check.py` on `OUTLINE.md`), write `STORY_REVIEW.md` (both parts, including "does Part 2 pay what Part 1 promised"), then `script_read.py Episodes/<Guest> --outline` → `SCRIPT_READ.md`. **The user approves the words here.** Changes go back into `OUTLINE.md` and the read is rebuilt.
4. **Mode 4** → `P<n>_kit.md`, built by a script in `_kit_source/` from the approved outline only. Mode 4 never changes words — a wording change goes back to `OUTLINE.md`. Run **every** gate in the block at the top of `skill_mode4_produce.md` (a single failure stops generation), then `sources_audit.py`, `build_episode_cards.py --part N`, and `publish_sheet.py --words-only`.
5. **Test batch** (Mode 4 §0c) — Part 1 of a new guest only: pick qualifying shots from this kit by the criteria, generate them first, fold the results into the skills.
6. **Generation** (Mode 4, *Generating*) — `round_sheet.py` writes one sheet with every clip in kit order, chained clips under their sources. Clips are made through the Kling CLI in waves: Claude runs `cli_wave.py`, the user runs the one command it prints (that is the approval of the spend), the user judges the takes, and Claude files the kept ones into `Shots/<ID>.mp4`. The website is the fallback. For a new guest, the first 3–5 talking clips calibrate the duration rate. There are no per-take checks.
7. **Voice pass** — `voice_folders.py`, then ElevenLabs voice change per folder into `Voice/P<n>/done/`.
8. **Mode 6** — `batch_check.py` over the whole part first, then **assembly** (Mode 6 §3; the user signs off the cut), then the hook render, branding, masters, `P<n>_captions.srt`, `P<n>_TIMECODES.txt`, `P<n>_EDIT_NOTES.md`, and `publish_sheet.py` → `P<n>_PUBLISH.md` (exit 0 = ready). The user uploads by following the sheet.
9. **Mode 5** — reels from the clean master.

Part 2 skips 1–3 and the test batch; its Mode 4 also reads `P1_kit.md` and `P1_EDIT_NOTES.md`.

## File discipline — this has already cost the project once

- **Edit files where they live**, with a command or a short script that reads the file itself (`sed -i`, or a python read-modify-write). Never re-type a file from earlier tool output, and never edit a copy left over from earlier in the chat.
- If a file ever has to be copied between the Mac and a cloud workspace, re-stage it fresh right before, check its size against a fresh directory listing, and write back with the modification-time guard so a newer version is never overwritten.
- Never delete a user file. If something should go, move it to an archive folder or list it and let the user remove it.

A skill file was once overwritten from a stale copy and lost a third of its content. The rule above is why.

## End of every run

1. Save the mode's output to the file named in the **Writes** line of its Inputs and output block. Anything that only lives in the chat is lost to the next mode.
2. Update `NEXT_STEPS.md` with what was done and what comes next.
3. **If a problem was found**, follow the LESSONS protocol: a rule in every skill that could repeat it, a gate where a script can catch it, and a row in `LESSONS.md`. When a rule is replaced, the old one goes into that skill's **Tested and ruled out** list and its evidence into `DECISIONS_ARCHIVE.md`. Never leave the old version standing next to the new one.
4. **If the process itself changed** (a new step, gate, tool or rule), republish **The Running Order**: read it by URL, edit it, publish with that `url`, and add a line to its change log. The user asked for it to be kept current at all times.
5. In a cloud session, commit and push the changes.
6. Tell the user, in one or two sentences, what was saved and which chat comes next.

## Standing rules that apply in every mode

The mode files hold the detail; these are the ones most often broken:

- Every arc is exactly two parts. Titles carry `Part N of 2`.
- Never write a `[D]` provenance line from memory — look it up while the line is still text. No line leaves Mode 3 with a check outstanding.
- Every asset a kit names must be produced by a named mode. "It already exists" is only true for the episode that happened to make it.
- Fixes are global: a problem found in one shot is fixed in the skill or a gate, not only in that kit.
- **Before proposing a technique, check the skill's Tested and ruled out list and `LESSONS.md`.** Several plausible ideas (the camera chip, pre-lifting chain frames, a wide two-shot, a separate pronunciation paragraph, naming a blink or a nod) were tested and failed.
- When a rule looks arbitrary, check `DECISIONS_ARCHIVE.md` for the reason before changing it.
