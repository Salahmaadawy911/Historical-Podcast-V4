#!/usr/bin/env python3
"""Builds Episodes/Cleopatra/P1_kit.md — Mode 4, B5 rerun, 2026-09-23.

Built from OUTLINE.md (words approved in SCRIPT_READ.md 2026-09-23) and CAST.md only. Words are copied
verbatim from the outline; nothing here rewrites a spoken line. Durations come from syl.dur2 (v2 model).
Run from the project root:  python3 Episodes/Cleopatra/_kit_source/build_p1_kit.py
"""
import os, sys, re, math
ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, 'Fixed_Assets', 'tools'))
import syl

# ------------------------------------------------------------------ locked blocks (byte-identical)
# camera lock v2 (2026-09-25, P1_058): positive only, no camera-move words even negated (LESSONS L18)
# camera lock v1 + chip (2026-09-26, L33) — superseded 2026-09-27 by structure v3 below (L51).
LOCK = ("Camera: locked-off static shot. Movement: hold one fixed camera position for the full clip. Speed: still and steady. "
        "Framing: keep the same angle, height, lens distance and composition. End: finish with the same framing and camera position.")
ONE = "Only one person is in the frame."        # L19 kept (Salah)
CONT = ("Maintain absolute visual continuity. The lighting direction, color palette, exposure, and brightness must remain completely "
        "fixed and identical to the initial starting frame throughout the entire video. No flashing, shifting, or new light sources.")
# camera + lighting structure v3 (2026-09-27, Salah, L51): tested on ~15 clips with the chip OFF — camera held on all.
# Replaces lock v1 + chip. Layout: camera paragraph · one paragraph (ONE + direction + lines + gestures) · Voice · Audio · CONT.
VOICE = {
 'HOST': "Voice: male, early 40s. Warm mid-baritone with a slightly dry edge and a little gravel in the lower register. Clear neutral international English, no regional accent. Conversational rather than broadcast-polished — someone thinking aloud, not presenting.",
 'GUEST': "Voice: female, mid-30s. Low even alto, composed and precise. Placeless formal English — neither British nor American, not placeable to any country. Controlled and authoritative rather than warm — never breathy, never pleading.",
}
AUDIO_TALK = "Audio: quiet studio room tone, dialogue clean and prominent, ambience minimal. No music, no library audio, no added voiceover, no on-screen text, no subtitles, no logo."
AUDIO_SILENT = "Audio: quiet studio room tone only. No dialogue, no music, no library audio, no voiceover, no on-screen text, no subtitles, no logo."
STYLE = ("A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline — broad washes "
         "and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep "
         "shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no "
         "chalk highlights, no metallic or gold accents.")
PERSIST = ("It stays a drawing for every frame of the clip; the tone and the paper grain remain visible throughout, "
           "and it never resolves into photographic footage.")
CROWD_ALEX = ("A crowd of Alexandrians of the late Ptolemaic period seen from behind: men in knee-length undyed linen and wool tunics, some with a pale mantle over one shoulder, a few with shaven heads in plain white linen; women in long pale chitons with a mantle drawn over the head. Bare feet or simple leather sandals. No Egyptian headdresses, no nemes, no gold collars, no armour.")
CROWD_ROME = ("A Roman street crowd of the late Republic seen from behind and in half-shadow: men in plain off-white wool tunics, a few wrapped in heavy off-white togas; women in long dark stolas with a mantle over the head. Leather sandals and closed shoes. No armour, no plate, no laurel wreaths on the crowd, no purple.")
LABEL = {'HOST': 'The host', 'GUEST': 'The woman'}

# ------------------------------------------------------------------ pose register (checked by eye 2026-09-23,
# montage in _kit_source/grounding_*.jpg). Gesture sentences describe the frame as it is.
sys.path.insert(0, os.path.join(ROOT, 'Fixed_Assets', 'tools'))
import poses as _poses
POSE = _poses.load(os.path.join(ROOT, 'Episodes', 'Cleopatra'))   # pose table: Fixed_Assets/tools/poses.py + Episodes/Cleopatra/poses.py
CHAINED = _poses.CHAINED
HOST_FRAMES = ['frame_host', 'frame_host_b', 'frame_host_c', 'frame_host_d', 'frame_host_e', 'frame_host_f']
GUEST_FRAMES = ['frame_cleopatra', 'frame_cleopatra_b', 'frame_cleopatra_c', 'frame_cleopatra_i', 'frame_cleopatra_e']

# ------------------------------------------------------------------ provenance helper
ABBR = [('Plutarch, Antony', 'Plutarch, *Life of Antony*'), ('Plutarch, Caesar', 'Plutarch, *Life of Caesar*'),
        ('Plutarch, Crassus', 'Plutarch, *Life of Crassus*'), ('Caesar, Civil War', 'Caesar, *Civil War*'),
        ('Suetonius, Julius', 'Suetonius, *Julius*'), ('Suetonius, Augustus', 'Suetonius, *Augustus*'),
        ('Appian, Civil Wars', 'Appian, *Civil Wars*'), ('Josephus, Antiquities', 'Josephus, *Jewish Antiquities*'),
        ('Horace, Odes', 'Horace, *Odes*'), ('Roller, Cleopatra', 'Roller, *Cleopatra: A Biography*')]
def prov(tag, text=''):
    for a, b in ABBR: text = text.replace(a, b)
    text = re.sub(r'\bDio (\d)', r'Cassius Dio, *Roman History* \1', text)
    name = {'D': 'Documented', 'I': 'Inferred', 'V': 'Voice'}[tag]
    return f'`[{tag}]` {name}' + (f' — {text}' if text else '')

# ------------------------------------------------------------------ rows. k = my label; ids assigned in order.
R = []
def row(**kw): R.append(kw); return kw
def talk(k, who, line, note, reg, gest=None, start=None, pref=None, typ=None, p=None, place=None, sub=None,
         extra=0.0, notes='', test=None, blocks_extra=None, pron=None, beatmap=None, spoken=None):
    return row(k=k, kind='talk', who=who, line=line, note=note, reg=reg, gest=gest, start=start, pref=pref,
               typ=typ, prov=p, place=place, sub=sub, extra=extra, notes=notes, test=test,
               blocks_extra=blocks_extra, pron=pron, beatmap=beatmap, spoken=spoken)
def react(k, who, body, dur, place, start=None, pref=None, notes='', test=None):
    return row(k=k, kind='react', who=who, body=body, dur=dur, place=place, start=start, pref=pref, notes=notes, test=test)
def broll(k, desc, still, move, motion, audio, dur, place, notes=''):
    return row(k=k, kind='broll', desc=desc, still=still, move=move, motion=motion, audio=audio, dur=dur,
               place=place, notes=notes)

# ============================== OPENING ==============================
row(k='OPEN', kind='opening')
talk('N1a', 'HOST', "Rome once declared war on a woman — not on the Roman beside her. Then the winners wrote her story. Seductress. Monster.",
     'level, and harder on the two names without ever becoming a verdict',
     "The host, direct to camera, level — he lays out the charge without endorsing it. The two names land a little harder and stop short of scorn.",
     gest=('still', ''), start='frame_host_direct_b', typ='NARRATION',
     p=prov('D', 'war declared on her: Plutarch, Antony 60; Dio 50.4. "Monster": Horace, Odes 1.37 (*fatale monstrum*). The hostile tradition is Augustan.'),
     place='the host\'s only direct address. Hard cut in on the first strike after `BRAND_opening`. No lower third (frontal frame). `SPLIT` A — the whole line needs 15.8 s, past the 15 s cap, so it is split at the sentence where it turns quieter. Seam into [[N1b]]: a plain cut on the pause (Mode 4 §2, fix c) — no cutaway exists this early and a `PUNCH` is never used on direct address; the chained pose and the join grade carry it.')
talk('N1b', 'HOST', "Every word of it came from the side that won. She's sitting across from me.",
     'quieter, an introduction rather than a flourish',
     "The host, still to camera, quieter now — a plain statement, then an introduction rather than a flourish.",
     start=('chain', 'N1a'), typ='NARRATION',
     p=prov('D', 'the surviving narrative sources are Roman and post-Actium: Plutarch, Antony; Dio 50; Horace, Odes 1.37.'),
     place='`SPLIT` B. He turns to her on the last sentence; cut to [[W0]] as the turn lands (on *"me"* or just after) — never hold on the end of the turn.',
     notes='**Turbo, no end frame, and the turn always ends on a cut to her** (Salah, 2026-09-27). Standard + end frame failed twice, and on Turbo the turn goes the right way but its end point is luck (it overshoots). So nothing chains from this clip: the edit cuts to [[W0]] on her face as the turn lands, and [[N2]] comes back to him from the built seed `frame_host_b`, whose eyeline is right. The turn only has to head toward her.')
R[-1]['gest_text'] = 'He stays leaning forward, hands clasped, and says the first sentence to the lens. Without a pause he begins "She\'s sitting across from me", and his head makes a small, slow turn toward the right side of the frame, just past his microphone, taking the whole sentence; his eyes come to rest level, at seated head height, on the woman in the armchair opposite him, and stay there. His hands and shoulders stay where they are.'
react('W0', 'GUEST', "The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. Her chin lifts a fraction; otherwise she is still.",
      3, 'the cut out of the host\'s turn: on *"me"* at the end of [[N1b]], about 1.5 s of her face, then [[N2]] on him from the seed. **Her first appearance in the studio — his introduction lands on her face, seen before she is heard.** This cut is what hides the difference between where the turn ended and `frame_host_b`.',
      pref=['frame_cleopatra_b'],
      notes='**Not generated — cut from `P1_126` (0.0–1.5 s), a kept silent reaction on `_b`** (2026-09-27, L43): four takes on `frame_cleopatra` all had a blurred shape (the host) push into the bottom-left corner. `_b` also keeps her in the same pose either side of his line, since [[W1]] is on `_b`. `Shots/P1_003a.mp4` is a copy of `P1_126`; the edit uses its first 1.5 s. **added 2026-09-27 (Salah).** A turn clip never hands straight to the same speaker\'s next clip: a short guest reaction sits between them, so the host comes back on a built seed with the right eyeline.')
talk('N2', 'HOST', "Welcome to History Answers Back. Cleopatra, seventh of the name, last queen of the Ptolemies. Thank you for being here.",
     'warm and formal, then plain', "The host, now turned to her, warm and formal as he names her, then plain and simple for the thanks. A greeting, not a build — his tone stays level and easy.",
     start='frame_host_b', typ='INTERJECTION', gest=('still', ''),
     p=prov('D', 'last reigning Ptolemaic monarch, 51–30 BC: Roller, Cleopatra.'),
     place='on picture for *"Welcome to History Answers Back. Cleopatra, seventh of the name,"* only — then [[W1]] covers him from *"last queen of the Ptolemies"* to the end. The title and the thanks play on **her** face.')
react('W1', 'GUEST', "The woman sits in composed silence while she is introduced. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She receives it with composure, courteous but not warm: her chin lifts a fraction, then her gaze settles on him and holds there, on the point of answering.",
      5, 'covers [[N2]] from *"last queen of the Ptolemies"* to its end, then holds a beat after he finishes. Her lower third opens here (her first look, [[W0]], is too short to carry it). She is still seen before she is heard. [[G1]] chains from this clip.',
      start='frame_cleopatra_b')
talk('G1', 'GUEST', "Thank you. It is rare that I am asked. Usually, others describe me.",
     'with cool courtesy, and dry by the last sentence',
     "The woman answers with cool courtesy — polite, never warm — and the last sentence turns dry. Her tone stays low and level throughout.",
     start=('chain', 'W1'), typ='INTERJECTION', gest=('still', ''), p=prov('V'))

# ============================== ACT A ==============================
row(k='ACT_A', kind='head', title='Act A — The word',
    q='Is "seductress" a description of her — or a verdict somebody needed?')
talk('A1', 'HOST', "Then let's start with the description. Seductress. Is any of it true?",
     'direct and light, then plain on the question',
     "The host, direct and light, opening the questioning. He places the word plainly and asks the real question openly, his voice lifting at the end — curious, never mocking.",
     gest=('settle', 'Seductress'), pref=['frame_host_c', 'frame_host_f'], p=prov('V'),
     place='his first proper cross-shot appearance — **the host\'s lower third opens here**.')
talk('A2', 'GUEST', "They came for my treasury. They wrote about my bed.",
     'coolly correcting him, the weight held under',
     "The woman corrects the premise coolly. The second sentence is plain, with the weight held underneath it — she does not raise her voice or underline it.",
     gest=('advance', 'bed'), pref=['frame_cleopatra_e'], p=prov('I', 'Suetonius, Julius 54; Plutarch, Antony 25, 56: the Romans who came to her came for money.'),
     place='**HOOK, first option** — Mode 6 re-picks the hook from the finished part. Key line 1.')
react('A2r', 'HOST', "The host holds her look. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He takes it in, his head steady and his shoulders settled; he stays that way.",
      4, 'covers the tail of [[A2]] from *"They wrote about my bed"*, then holds a beat. **Pull-quote 01 lands here**, after the line has finished. [[A3]] chains from this clip.',
      pref=['frame_host_e'])
talk('A3', 'HOST', "But the beauty. That's the part people know.", 'curious, pressing lightly',
     "The host, curious, pressing lightly — he offers the popular version rather than endorsing it. His tone stays easy.",
     start=('chain', 'A2r'), gest=('settle', 'beauty'), p=prov('V'))
talk('A4', 'GUEST', "I was never the most beautiful woman at my own table. I was the one worth talking to. And I could do it in the other man's language.",
     'dry, with a faint pride kept under',
     "The woman, dry and plain. A faint pride comes in on the last sentence and stays kept under — never boastful.",
     gest=('settle', 'worth talking to'), pref=['frame_cleopatra_c'],
     p=prov('D', 'Plutarch, Antony 27: her beauty "not altogether incomparable"; "converse with her had an irresistible charm"; many languages.'))
talk('A5', 'HOST', "The sources name seven peoples you spoke to without an interpreter. Hebrews, Arabs, Medes, Parthians.",
     'checking a fact, even through the list',
     "The host, checking a fact. He reads the list evenly, one name after another, without performing it.",
     gest=('advance', 'Hebrews'), pref=['frame_host_d'], p=prov('D', 'Plutarch, Antony 27.'))
talk('A6', 'GUEST', "And Egyptian. My family had been kings of Egypt for nearly three hundred years. I was the first of us who bothered to learn it.",
     'plain, a little cooler on the point',
     "The woman, plain. The last sentence is the point, and she makes it a little cooler — never scornful.",
     gest=('settle', 'the first of us'), pref=['frame_cleopatra_i'],
     p=prov('D', 'Plutarch, Antony 27; Ptolemy I king from 305 BC: Roller, Cleopatra.'),
     place='**Context card 01** (the Ptolemies) enters on *"My family"*.')
talk('A7', 'HOST', "Hold on. You're not Egyptian?", 'surprised and quick, then a genuine question',
     "The host, surprised and quick, then genuinely asking — his voice lifts at the end. Never incredulous.",
     typ='INTERJECTION', gest=('advance', 'Hold on'), pref=['frame_host', 'frame_host_e'], p=prov('V'))
talk('A8', 'GUEST', "Macedonian. My ancestor was one of Alexander's generals. We came to Egypt as its conquerors.",
     'even and factual, dry at the end',
     "The woman, even and factual, dry on the last sentence. Her tone stays low and level.",
     gest=('still', ''), pref=['frame_cleopatra', 'frame_cleopatra_b'], p=prov('D', 'Plutarch, Antony 27; Roller, Cleopatra.'))
talk('A9', 'HOST', "Then here's what I don't understand. The richest kingdom in the world. Why does it need Rome?",
     'puzzled and slower, then asking it plainly',
     "The host, puzzled, working it out slower. He sets out the premise and asks the question plainly, his voice lifting at the end — curious, not a challenge.",
     gest=('settle', 'the richest kingdom'), pref=['frame_host_e', 'frame_host_b'], p=prov('I'))
talk('A10', 'GUEST', "Because it had no army that Rome could not beat, and Rome knew it. My father knew it best. He paid Rome to call him king.",
     'flatly, the cost held under, dry at the end',
     "The woman states it flatly. The cost sits under the second sentence; the last is dry. Her voice stays low and never hardens.",
     gest=('advance', 'He paid Rome'), pref=['frame_cleopatra_e'],
     p=prov('D', 'Suetonius, Julius 54.'), test='T2',
     beatmap=[('flatly', "Because it had no army that Rome could not beat, and Rome knew it."),
              ('with the cost held under it', "My father knew it best."),
              ('dry', "He paid Rome to call him king.")])
talk('A11', 'HOST', "Paid how much?", 'short and plain', "The host, short and plain — a follow-up, not a challenge.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_b', 'frame_host_d'], p=prov('V'))
talk('A12', 'GUEST', "Nearly six thousand talents, to Caesar and Pompey. In Rome you pay first. Then they decide whether you exist.",
     'level, the number left to do the work, dry at the end',
     "The woman, level — she lets the number do the work and does not stress it. The last sentence is dry, never bitter.",
     gest=('settle', 'In Rome'), pref=['frame_cleopatra_c', 'frame_cleopatra_i'], extra=1.0,
     p=prov('D', 'Suetonius, Julius 54 ("nearly six thousand talents", in his own name and Pompey\'s).'),
     place='**Context card 02** (talent) enters on *"talents"*. +1 s of tail so [[A13]] has room under her.')
talk('A13', 'HOST', "Charming.", 'dry, low, almost to himself', "The host, dry and low, almost to himself. No emphasis.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_f', 'frame_host'], p=prov('V'),
     place='audio only, under the tail of [[A12]] after *"whether you exist"* — `OFFMIC`. Picture discarded; we stay on her.')
talk('A14', 'HOST', "Did Rome ever just try to take it?", 'pressing, curious', "The host, pressing — curious rather than accusing. His voice lifts at the end.",
     gest=('advance', 'take it'), pref=['frame_host_b', 'frame_host'], p=prov('V'))
talk('A15', 'GUEST', "When I was a child, a Roman censor tried to make my country pay tribute to Rome. He lost the argument. Somebody always tries again.",
     'plain and exact, dry on the last sentence',
     "The woman, plain and exact. The last sentence is dry — a fact of life, not a complaint.",
     gest=('settle', 'He lost'), pref=['frame_cleopatra_b', 'frame_cleopatra'],
     p=prov('D', 'Plutarch, Crassus 13 (65 BC); the last sentence is `[I]`, her reading.'))
talk('A16', 'HOST', "And when your father died?", 'moving on, level', "The host, moving the story on, level and simple.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_e', 'frame_host_c'], p=prov('V'))
talk('A17', 'GUEST', "He left the kingdom to me and to my brother, and he made Rome swear to see it done. Within three years my brother's men had driven me out of my own city.",
     'plain, an edge coming in on the last sentence',
     "The woman, plain. An edge comes into the last sentence and stays under control — no heat.",
     gest=('advance', 'driven me out'), pref=['frame_cleopatra_i', 'frame_cleopatra'],
     p=prov('D', 'Caesar, Civil War 3.103, 3.108.'))
talk('A18', 'HOST', "Which is where Rome arrives. Pompey first.", 'setting the scene, then plain',
     "The host, setting the scene, then plain on the name.",
     gest=('settle', 'Pompey'), pref=['frame_host_d', 'frame_host_c'], p=prov('D', 'Caesar, Civil War 3.103.'))
talk('A19', 'GUEST', "Pompey came running from Caesar and landed below my brother's camp. They killed him on the shore. When Caesar arrived, they handed him the head.",
     'cool narration, colder on the last sentence',
     "The woman tells it as cool narration. The last sentence is colder and lower, and it does not break.",
     gest=('still', ''), pref=['frame_cleopatra_e', 'frame_cleopatra'],
     p=prov('D', 'Caesar, Civil War 3.103–104; Plutarch, Caesar 48.'),
     place='**Context card 03** (Pompey) enters on her *"Pompey"* — moved from the host\'s *"Pompey first."*, where a card on his side (R) would ride onto her face at the cut. `MUSIC_Drone_Low` enters under this line. [[A20]] covers from *"they handed him the head"*.')
broll('A20', 'A signet ring in an open palm, cut off at the wrist.',
      "A man's open palm held out toward us, seen close and cut off at the wrist, a heavy signet ring lying loose in the middle of the palm, drawn in the same charcoal greys as everything else. At the wrist, the loose draped fold of a plain wool tunic sleeve. Nothing else in frame, no face. No colour anywhere; no cuff, no buttons, no knitted or tailored sleeve.",
      'The camera pushes in very slowly toward the ring.',
      'The fingers close a fraction around the ring and stop. Nothing else moves.',
      'Audio: ambience only — a faint wash of sea on a shore, quiet and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.',
      6, 'covers [[A19]] from *"they handed him the head"*, runs under [[A21]] (his *"And Caesar?"* is heard, not seen), and cuts back to her on the first word of [[A22]]. The head is never shown; the ring stands for it (Plutarch, *Life of Caesar* 48).')
talk('A21', 'HOST', "And Caesar?", 'quietly', "The host, quietly. A prompt, nothing more.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host', 'frame_host_e'], p=prov('V'),
     place='picture replaced by [[A20]] — his voice runs under the b-roll.')
talk('A22', 'GUEST', "He turned from the head. He took the ring, and wept. My brother had expected thanks. Rome does not thank you. It judges you.",
     'level, drier toward the end, the principle stated plainly',
     "The woman, level. She grows drier through the middle, and the last two sentences are stated as a plain principle — not bitter, not raised.",
     gest=('settle', 'Rome does not thank you'), pref=['frame_cleopatra_c', 'frame_cleopatra_b'],
     p=prov('D', 'Plutarch, Caesar 48; Caesar, Civil War 3.107 (Caesar claims to arbitrate).'),
     place='Key line 2: *"Rome does not thank you. It judges you."*')
react('A22r', 'HOST', "The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He goes still where he is, his gaze on her.",
      4, 'covers the tail of [[A22]] from *"It judges you"*, then holds a beat. **Pull-quote 02 lands here.** `MUSIC_Drone_Low` fades out across it. [[A23]] chains from this clip.',
      pref=['frame_host_b', 'frame_host_f'])
talk('A23', 'HOST', "So the judge is in your palace, and you're outside the city, with your brother's army between you.",
     'putting it together, level', "The host, putting the geography together for himself, level and exact.",
     start=('chain', 'A22r'), gest=('settle', 'between you'), p=prov('D', 'Caesar, Civil War 3.103, 3.107.'))
talk('A24', 'GUEST', "Yes.", 'plainly', "The woman, plain. One word, nothing added.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_cleopatra_i', 'frame_cleopatra'], p=prov('V'))
react('A24r', 'HOST', "The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He shifts his weight a little forward in the chair, looking at her.",
      3, 'plays between [[A24]] and [[A25]], soundscape only — the `BEAT`. [[A25]] chains from this clip.',
      pref=['frame_host'])
talk('A25', 'HOST', "So how do you get in?", 'leaning in, curious', "The host, leaning in, genuinely curious. The voice lifts at the end.",
     start=('chain', 'A24r'), typ='INTERJECTION', gest=('still', ''), p=prov('V'),
     place='the act\'s open loop — cut straight to the act break.')
row(k='BRK1', kind='actbreak', file='BRAND_actbreak_vessel.mp4')

# ============================== ACT B ==============================
row(k='ACT_B', kind='head', title='Act B — Caesar', q='Did she seduce Caesar — or recruit him?')
talk('B1', 'GUEST', "In a sack for bedding. Tied with a cord, and carried in through the doors to Caesar.",
     'dry and exact, a flicker of pride', "The woman, dry and exact. A flicker of pride shows on the last words and is not indulged.",
     gest=('settle', 'carried in'), pref=['frame_cleopatra_c', 'frame_cleopatra'], p=prov('D', 'Plutarch, Caesar 49.'),
     place='answers [[A25]] across the break.')
talk('B2', 'HOST', "Not in a carpet.", 'amused', "The host, amused, checking the famous version. Light, never mocking.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_c', 'frame_host_f'], p=prov('D', 'Plutarch, Caesar 49.'))
talk('B3', 'GUEST', "The carpet came later, from people who were not there.", 'dry, with a trace of amusement',
     "The woman, dry, with a trace of amusement she keeps small.", gest=('still', ''),
     pref=['frame_cleopatra_e', 'frame_cleopatra_b'], p=prov('D', 'Plutarch, Caesar 49.'))
talk('B4', 'HOST', "And that night, you and Caesar became lovers.", 'leading, a smile under it',
     "The host, leading her on, a smile under it. His tone stays light and never leering.",
     gest=None, pref=['frame_host_f'], spoken='And that night, you and Caesar —', test='T5',
     p=prov('V'), place='interrupted by [[B6]] after *"Caesar"* — cut. `CUT-IN` A: the whole line is generated so the model never has to stop; **the subtitle and the cut stop at *"Caesar"***.')
R[-1]['gest_text'] = 'On "you and Caesar" the hand on his thigh lifts and turns outward toward the right of the frame, still moving as he goes on.'
react('B5', 'HOST', "His lips close in the first moment and stay gently closed, his jaw still. His hands stay where they are and his eyes go to her.",
      3, 'follows [[B4]] at the cut, [[B6]]\'s audio over it. `CUT-IN` B, the stop.', start=('chaincut', 'B4', 'Caesar', 2.95), test='T5')
talk('B6', 'GUEST', "Not lovers. That night I became his ally. The rest followed the alliance. Not the other way round.",
     'cutting in, cool and exact', "The woman comes in over him, cool and firm but not loud. She is plain in the middle and exact on the last sentence.",
     gest=None, pref=['frame_cleopatra_i', 'frame_cleopatra'], test='T5',
     p=prov('I', 'Caesar, Civil War 3.107–108 and Plutarch, Caesar 49: Caesar takes up her claim to the throne.'),
     place='enters over [[B5]] — interruption, audio overlaps ~0.3 s before the cut. Trim her lead-in: the first word must land on the cut.', extra=0.5)
R[-1]['gest_text'] = 'From her first word she turns a fraction toward the left of the frame, where the person opposite her sits, and stays turned — already moving as she speaks, no pause before it.'   # pose-free: the start frame is chosen later (fixed 2026-09-24)
talk('B7', 'HOST', "It didn't keep you safe.", 'pressing', "The host, pressing — a plain observation, not an accusation.",
     gest=('still', ''), typ='INTERJECTION', pref=['frame_host_d', 'frame_host'], p=prov('I', 'Dio 42.38–39.'))
talk('B8', 'GUEST', "No. My brother's people shut us inside the palace quarter for a winter. They made my sister queen. And the harbour burned.",
     'plain narration, colder at the end', "The woman, plain narration. She grows colder toward the last sentence and stays level.",
     gest=('settle', 'my sister'), pref=['frame_cleopatra_e', 'frame_cleopatra_b'],
     p=prov('D', 'Dio 42.39 (Arsinoe declared queen); Plutarch, Caesar 49; Dio 42.38 (the fire).'))
# B9 (P1_050, harbour-fire b-roll) retired 2026-09-27 (L55): four stills, each drawn as a later port — the line plays on her face.
talk('B10', 'HOST', "And the Library of Alexandria went with it. That's the story.", 'the famous version, a small challenge',
     "The host offers the famous version, with a small challenge in it. Level, never scoring a point.",
     gest=('settle', "That's the story"), pref=['frame_host_e', 'frame_host_c'], p=prov('D', 'Plutarch, Caesar 49; Dio 42.38.'))
talk('B11', 'GUEST', "Books burned, in the fire by the docks. How many, and whose, your scholars are still arguing.",
     'even, letting posterity keep its argument', "The woman, even. She leaves the argument to posterity and does not take a side.",
     gest=('settle', 'your scholars'), pref=['frame_cleopatra_c', 'frame_cleopatra'],
     p=prov('I', 'Plutarch, Caesar 49 and Dio 42.38 both report the fire reaching the library; its scale is a modern debate.'))
talk('B12', 'HOST', "Your sister. Arsinoe.", 'turning, the name placed gently', "The host turns the subject and places the name gently. Quiet, not probing.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host', 'frame_host_b'], p=prov('V'))
talk('B13', 'GUEST', "Arsinoe. When it was over, Caesar took her to Rome and led her through the streets in chains, in his triumph.",
     'level, cooler and exact', "The woman, level. She grows cooler and exact on the triumph, and does not dwell.",
     gest=('still', ''), pref=['frame_cleopatra_b', 'frame_cleopatra_i'], p=prov('D', 'Dio 43.19.'), test='T1',
     pron=[('Arsinoe', 'ar-SIN-oh-ee')],
     place='**Context card 04** (Arsinoe IV) enters on her *"Arsinoe"*. [[B14]] covers from *"led her through the streets"*; the card rides over it.')
broll('B14', 'A captive walked through a Roman street in chains, seen from behind a crowd.',
      "A narrow Roman street seen from behind the crowd lining it.\n\n" + CROWD_ROME + "\n\nBeyond their heads, down the middle of the street, a young woman walks away from us in a plain long dress, her wrists bound in front of her with a chain, small in frame, her face not visible.",
      'The camera pushes in very slowly over the heads of the crowd.',
      'The crowd shifts and turns to watch; the young woman walks slowly on, away from us.',
      'Audio: ambience only — a murmuring street crowd, distant and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.',
      6, 'covers [[B13]] from *"led her through the streets"* to its end, then cuts to the host on [[B15]]. Arsinoe is seen from behind only — no likeness claim.',
      notes='**added in Mode 4.** The outline registers `roman_crowd_late_republic` *"for the triumph row (Arsinoe)"* but marks no `BROLL` for it; the drama asks for the picture (the act\'s image, per the outline\'s arc table), so the row is added here.')
talk('B15', 'HOST', "And you were in Rome that year.", 'quietly', "The host, quietly — laying the fact beside the last one, not accusing.",
     gest=('still', ''), typ='INTERJECTION', pref=['frame_host_e', 'frame_host_d'], p=prov('D', 'Dio 43.27.'))
talk('B16', 'GUEST', "I was living in his house.", 'plainly', "The woman, plain. She adds nothing to it.",
     gest=('still', ''), typ='INTERJECTION', pref=['frame_cleopatra_e', 'frame_cleopatra'], extra=1.0,
     p=prov('D', 'Dio 43.27.'), place='+1 s of tail so [[B17]] has room under her.')
talk('B17', 'HOST', "In his house.", 'low, repeating it', "The host repeats it low, thinking aloud. No emphasis.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_c', 'frame_host'], p=prov('V'),
     place='audio only, under the tail of [[B16]] — `OFFMIC`. Picture discarded.')
react('B16r', 'GUEST', "The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds the position she is in, entirely composed; her gaze stays on him and she is otherwise still.",
      4, 'plays between [[B16]] and [[B18]], soundscape only — the `BEAT` after his echo. Chained from [[B16]], so her pose carries straight on.',
      start=('chain', 'B16'))
talk('B18', 'HOST', "Did you watch?", 'gently', "The host, gently. A real question, quietly asked, never prosecuting.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_b', 'frame_host_f'], p=prov('V'))
talk('B19', 'GUEST', "The crowd pitied her. That much I know.", 'even, a fraction lower', "The woman, even. The second sentence is a fraction lower, and her voice stays steady.",
     gest=('still', ''), pref=['frame_cleopatra_i', 'frame_cleopatra_c'], p=prov('D', 'Dio 43.19.'))
react('B19r', 'HOST', "The host waits. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He does not move to ask again; his hands stay where they are, and his gaze stays on her.",
      4, 'covers the tail of [[B19]] from *"That much I know"*, then holds — he does not ask again. [[B20]] chains from this clip.',
      pref=['frame_host_e', 'frame_host'])
talk('B20', 'HOST', "You gave Caesar a son.", 'moving on, level', "The host moves on, level and plain.",
     start=('chain', 'B19r'), typ='INTERJECTION', gest=('still', ''), p=prov('D', 'Suetonius, Julius 52.'))
talk('B21', 'GUEST', "I gave him a son, and I gave the boy his name. Caesar. I knew what that name was worth when I chose it.",
     'plain, then deliberate', "The woman, plain, then deliberate on the last sentence — a decision owned, not a boast.",
     gest=('advance', 'I knew'), pref=['frame_cleopatra_b', 'frame_cleopatra'],
     p=prov('D', 'Suetonius, Julius 52; Plutarch, Caesar 49.'),
     place='the callback Part 2 pays (*"I gave him the name that killed him"*).')
talk('B22', 'HOST', "And then the Ides of March.", 'turning', "The host turns the story, plain and quiet.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_d', 'frame_host_c'], p=prov('V'))
talk('B23', 'GUEST', "Twenty-three wounds, at the foot of Pompey's statue. The man who stood between Rome and my throne was dead, and I was a foreign queen living in his house.",
     'cool and exact, the cost held under', "The woman, cool and exact. The cost sits under the second sentence and stays held — never raised.",
     gest=('settle', 'a foreign queen'), pref=['frame_cleopatra_e', 'frame_cleopatra'],
     p=prov('D', 'Plutarch, Caesar 66; Dio 43.27.'))
talk('B24', 'HOST', "Rome was about to tear itself apart again. Who did you back?", 'the stakes, then pressing',
     "The host lays out the stakes, then presses. His voice lifts on the question; he never prosecutes.",
     gest=('advance', 'Who did you back'), pref=['frame_host_b', 'frame_host_f'],
     p=prov('I', 'the civil wars after Caesar\'s death.'))
talk('B25', 'GUEST', "Whoever was going to win. It took me some time to learn who that was.", 'flat, then dry',
     "The woman, flat, then dry on the second sentence. Nothing apologetic in it.",
     gest=('still', ''), pref=['frame_cleopatra_c', 'frame_cleopatra_i'], p=prov('I'),
     place='end of Act B. `BRAND_subscribe` may go over her held tail here (Mode 6).')

# ============================== ACT C ==============================
row(k='ACT_C', kind='head', title='Act C — Antony', q='Was Antony a lover — or a policy?')
talk('C1', 'HOST', "Which brings us to Tarsus. Antony summons you.", 'brightening, then plain on the summons',
     "The host brightens as the story moves, then plain on the summons.",
     gest=('settle', 'Antony'), pref=['frame_host_c', 'frame_host'], p=prov('D', 'Plutarch, Antony 25–26.'),
     place='**Context card 05** (Tarsus) enters on *"Tarsus"* — side R, over him. [[C1r]] holds his face through her first sentence so the card never rides onto hers.')
react('C1r', 'HOST', "The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He holds the position he is in and keeps his gaze on her, with the ghost of a smile.",
      4, 'covers [[C2]] from its first word (J-cut: her voice over his face) to *"to his enemy"* — cut to her on *"to his enemy, Cassius"*, after context card 05 (side R) has gone. Chained from [[C1]]. It exists so the card finishes over his side of the room.',
      start=('chain', 'C1'))
talk('C2', 'GUEST', "To answer a charge. He had heard that I gave money to his enemy, Cassius.", 'dry, then exact',
     "The woman, dry, then exact on the detail. Her tone stays low.", gest=('settle', 'Cassius'),
     pref=['frame_cleopatra_i', 'frame_cleopatra'], p=prov('D', 'Plutarch, Antony 25.'))
talk('C3', 'HOST', "You were summoned to answer a charge.", 'echoing it, amused', "The host echoes it back, amused. Light, never sarcastic.",
     gest=('still', ''), typ='INTERJECTION', pref=['frame_host_f', 'frame_host_e'], p=prov('V'))
talk('C4', 'GUEST', "I was. So I came up the river in a barge with a gilded stern and purple sails, rowed with silver oars, dressed as Aphrodite. Nobody mentioned the charge again.",
     'the faintest smile held under, dry at the end',
     "The woman, the faintest smile held under the words. Exact through the list, dry on the last sentence, and never boastful.",
     gest=('settle', 'Nobody mentioned'), pref=['frame_cleopatra_c', 'frame_cleopatra_b'],
     p=prov('D', 'Plutarch, Antony 26; the last sentence is `[I]`.'))
broll('C5', 'The barge on the river, a crowd along the bank.',
      "An ancient royal river barge of the 1st century BC seen from the bank at water level: a long low open hull, one mast with a single square sail, a stern post curving high and ending in a carved lotus flower, a long bank of oars dipping, and a cloth canopy on slender posts over the rear deck with a figure seated beneath it, too small to read as a face. A crowd of small anonymous figures in plain tunics and draped mantles, bareheaded, stands along the near shore watching it pass. No cabin, no deckhouse, no funnel, no hats, no modern clothing.",
      'The camera drifts slowly sideways along the bank, keeping pace with the barge.',
      'The oars dip and rise together; the sail stirs; the figures on the shore turn to follow it.',
      'Audio: ambience only — oars in water, wind in the sail, a murmur from the shore, quiet and low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.',
      7, 'covers [[C4]] from *"So I came up the river"* to *"dressed as Aphrodite"*; cut back to her for *"Nobody mentioned the charge again."*')
talk('C6', 'HOST', "That's the most famous seduction in history.", 'offering the myth', "The host offers the myth plainly, as the version everyone knows.",
     gest=('settle', 'seduction'), pref=['frame_host_d', 'frame_host'], p=prov('V'))
talk('C7', 'GUEST', "It was a state visit. A queen does not arrive at a trial as the accused. She arrives as a goddess, and the trial becomes a dinner.",
     'coolly correcting, a quiet edge at the end', "The woman corrects the premise coolly, then plainly; a quiet edge comes into the last sentence and stays quiet.",
     gest=('advance', 'A queen'), pref=['frame_cleopatra_i', 'frame_cleopatra_e'], p=prov('I', 'Plutarch, Antony 26.'),
     place='Key line 3: *"A queen does not arrive at a trial as the accused."*')
react('C7r', 'HOST', "The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. His eyes crease with a silent laugh and stay creased; his head stays steady.",
      4, 'covers the tail of [[C7]] from *"and the trial becomes a dinner"*, then holds a beat. **Pull-quote 03 lands here.** [[C8]] chains from this clip.',
      pref=['frame_host_e', 'frame_host_f'])
talk('C8', 'HOST', "And your sister. Arsinoe was still alive, in a temple of Artemis.", 'quieter, the fact laid down',
     "The host, quieter now. He lays the fact down plainly and does not press it.",
     start=('chain', 'C7r'), gest=('still', ''),
     p=prov('D', 'Appian, Civil Wars 5.9; Josephus, Antiquities 15.89.'))
talk('C9', 'GUEST', "I asked him for her death. He gave it to me.", 'level, flat, no apology',
     "The woman, level and flat. No apology and no emphasis; her voice stays low and does not waver.",
     gest=('still', ''), pref=['frame_cleopatra_e', 'frame_cleopatra'],
     p=prov('D', 'Appian, Civil Wars 5.9; Josephus, Antiquities 15.89.'),
     place='**the crack** — Part 1\'s one.')
react('C9r', 'HOST', "The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. His jaw sets and stays set; his gaze stays on her.",
      4, 'covers the tail of [[C9]] from *"He gave it to me"*, then holds. [[C10]] chains from this clip.',
      pref=['frame_host_e', 'frame_host_d'], test='T6')
talk('C10', 'HOST', "She was a suppliant. In a sanctuary.", 'plainly, not accusing, lower on the second',
     "The host, plain — he states it, he does not accuse. The second sentence drops lower.",
     start=('chain', 'C9r'), p=prov('D', 'Appian, Civil Wars 5.9.'), test='T6',
     place='full frame for *"She was a suppliant."*, then cut to her ([[C12]]) — *"In a sanctuary"* plays off screen over her face. Trim the pause between his two sentences to ~0.5 s under the cut.')
react('C12', 'GUEST', "The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds his gaze, steady; her hands stay where they are and she is otherwise still.",
      6, 'full frame on her from *"In a sanctuary"* (his words off screen), then the `BEAT` — about 1 s of silence after his last word, no longer — then [[C13]]. Use the clip\'s **end** (it ends on its seed frame, so [[C13]] joins exactly).',
      pref=['frame_cleopatra_e'], test='T6')
talk('C13', 'GUEST', "In my family, the danger to a queen sat at her own table.", 'quieter, the ceiling holding',
     "The woman speaks quietly and seriously, steady and unhurried.",
     start=('chain', 'C12'), gest=('still', ''), p=prov('I', 'her reading of the dynasty; Dio 42.39, 43.19.'), test='T3',
     place='`SPLIT` A — continues on her from [[C12]] (exact join). Seam into [[C14]]: `PUNCH` on the seam, held to the end of [[C14]] (Mode 4 §2, fix b).')
talk('C14', 'GUEST', "Rome had already used her against me once. I would not leave it a second chance.", 'personal, then the decision stated',
     "The woman, the personal now — still low. The last sentence is the decision, stated, not defended.",
     start=('chain', 'C13'), gest=('advance', 'I would not'), p=prov('I', 'her reading of the dynasty; Dio 42.39, 43.19.'), test='T3',
     place='`SPLIT` B — punch-in at *"Rome had already used her"* (the seam), held to the end of the clip.')
talk('C15', 'HOST', "Then there's Antony. Three children.", 'letting it go, moving on', "The host lets it go and moves on, plain and level.",
     gest=('settle', 'Three children'), pref=['frame_host_c', 'frame_host'], p=prov('D', 'Plutarch, Antony 36, 54.'))
talk('C16', 'GUEST', "Twins first, a boy and a girl. The Sun and the Moon. Then another son. And with them, cities, coastlines, kingdoms.",
     'even and exact', "The woman, even and exact — a list of facts, weighed but not dwelt on.",
     gest=('settle', 'kingdoms'), pref=['frame_cleopatra_c', 'frame_cleopatra_b'], p=prov('D', 'Plutarch, Antony 36, 54.'), extra=1.0,
     place='+1 s: the line ends on a comma list (Mode 4 §2).')
talk('C17', 'HOST', "Was it love?", 'plainly, so she can refuse it', "The host asks the obvious question plainly, so she can refuse it. Never teasing.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_b', 'frame_host_f'], p=prov('V'))
talk('C18', 'GUEST', "You would like me to say yes.", 'dry', "The woman, dry — amused only in the words, not the voice.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_cleopatra_e', 'frame_cleopatra'], p=prov('V'),
     place='the callback Part 2 pays (*"You keep handing me that word"*).')
talk('C19', 'HOST', "I'd like you to say what it was.", 'not letting go, level', "The host, not letting go — level, patient, not pushing harder.",
     gest=('still', ''), pref=['frame_host_d', 'frame_host_e'], typ='INTERJECTION', p=prov('V'))
talk('C20', 'GUEST', "It was the only Roman army in the East, and it was loyal to him. I needed it. He needed my grain and my gold to pay for it.",
     'plain and exact, cooler at the end', "The woman, plain and exact, cooler on the last sentence. A transaction described, not confessed.",
     gest=('settle', 'I needed it'), pref=['frame_cleopatra_i', 'frame_cleopatra'], p=prov('I', 'Plutarch, Antony 56 (her ships and money).'))
talk('C21', 'HOST', "Then Alexandria, thirty-four BC. The gymnasium. A silver stage, two golden thrones.",
     'reaching for the picture', "The host reaches for the picture — the place, then the image — even and unhurried in manner, never grand.",
     gest=('settle', 'two golden thrones'), pref=['frame_host_e', 'frame_host'], p=prov('D', 'Plutarch, Antony 54.'),
     place='[[C22]] covers from *"A silver stage"*. **Context card 06** (Donations) enters on *"thrones"*, over the b-roll.')
broll('C22', 'A raised platform with two thrones in a colonnaded hall, a packed crowd.',
      "A raised platform in a colonnaded hall, two thrones on it with seated figures too small to read as faces; a packed crowd in the foreground.\n\n" + CROWD_ALEX,
      'The camera pulls back slowly from the platform over the heads of the crowd.',
      'The crowd shifts; a few heads turn; the seated figures stay still.',
      'Audio: ambience only — a large crowd murmuring in a stone hall, low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.',
      8, 'covers [[C21]] from *"A silver stage"* and runs under the start of [[C23]]; **cut back to her only after context card 06 has left** (it sits on her side, R), around *"with Caesar\'s son beside me"*.')
talk('C23', 'GUEST', "Antony named me Queen of Egypt, Cyprus, Libya and part of Syria, with Caesar's son beside me. Our own sons, he called Kings of Kings.",
     'exact, with weight', "The woman, exact, with weight on the titles — stated, never proud.",
     gest=('advance', 'Kings of Kings'), pref=['frame_cleopatra_b', 'frame_cleopatra_c'], p=prov('D', 'Plutarch, Antony 54.'))
talk('C24', 'HOST', "In Rome, that looked like a Roman giving Rome's lands away.", 'giving Rome\'s view, level',
     "The host gives Rome's view, level and attributed — not his own verdict.",
     gest=('settle', "Rome's lands"), pref=['frame_host_c', 'frame_host_f'], p=prov('I', 'Plutarch, Antony 54 (Roman disapproval).'))
talk('C25', 'GUEST', "Some of it was not his to give. He gave my son Parthia, which had just beaten him.", 'dry, then the barb',
     "The woman, dry. The barb in the second sentence is delivered flat, not relished.",
     gest=('still', ''), pref=['frame_cleopatra_e', 'frame_cleopatra_i'],
     p=prov('D', 'Plutarch, Antony 54 (Parthia among the gifts); 37–51 (the failed Parthian campaign).'))
react('C25r', 'HOST', "The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. His eyes crease with a laugh he holds in, a smile settled at the corners of his closed mouth; his hands stay where they are.",
      4, 'covers the tail of [[C25]] from *"which had just beaten him"*, then holds a beat. [[C26]] chains from this clip.',
      pref=['frame_host_d', 'frame_host'])
talk('C26', 'HOST', "And Octavian was listening.", 'sobering', "The host, sobering — quieter, the lightness gone.",
     start=('chain', 'C25r'), typ='INTERJECTION', gest=('still', ''), p=prov('V'))
talk('C27', 'GUEST', "Octavian was always listening. He needed Rome to hear it his way.", 'cool, then drier',
     "The woman, cool, then drier on the second sentence. Her tone stays low and even.",
     gest=('advance', 'his way'), pref=['frame_cleopatra', 'frame_cleopatra_c'], p=prov('I'), extra=1.0,
     place='**Context card 07** (Octavian) enters on her *"Octavian"* — moved from his, for the same reason as card 03. +1 s of tail so the card has left before the act break. The act\'s open loop — hold the clip to its end, then the break.')
row(k='BRK2', kind='actbreak', file='BRAND_actbreak_stone.mp4')

# ============================== ACT D ==============================
row(k='ACT_D', kind='head', title='Act D — The charge', q='Why did Rome declare war on her, and not on Antony?')
talk('D1', 'HOST', "So he goes to the Vestal Virgins for Antony's will.", 'laying it out', "The host lays it out plainly, a step in the story.",
     gest=('settle', 'will'), pref=['frame_host_b', 'frame_host_d'], p=prov('D', 'Plutarch, Antony 58.'),
     place='`MUSIC_Drone_High` enters here. [[D2]] covers from *"Vestal Virgins"*; **context card 08** enters on *"Vestal"*, over the b-roll.')
broll('D2', 'A sealed scroll drawn from a niche in a small shrine, a fire on the hearth.',
      "A small round shrine: a low fire burning on a stone hearth, and in a niche in the wall behind it, sealed scrolls laid side by side. A man's hand in the fold of a heavy wool sleeve reaches into the niche. No faces.",
      'The camera pushes in slowly toward the niche.',
      'The hand draws one sealed scroll out of the niche; the fire moves on the hearth.',
      'Audio: ambience only — a low fire in a quiet stone room. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.',
      7, 'covers [[D1]] from *"Vestal Virgins"* and runs under [[D3]] through *"because they refused him"*; cut back to her on *"Then he read the Senate"* — after context card 08 (side R) has left.',
      notes='**added in Mode 4.** Act D had no picture in the outline; the will seized from the Vestals is the act\'s key political event (a lesson carried in from v1: *give the key political event a picture*), and it gives card 08 somewhere to sit that is not her face.')
talk('D3', 'GUEST', "Goes to them, and takes it, because they refused him. Then he read the Senate the parts he had chosen.",
     'exact, then dry', "The woman, exact on the seizure, then dry on the reading. Her tone stays low.",
     gest=('settle', 'the parts he had chosen'), pref=['frame_cleopatra_c', 'frame_cleopatra_b'], p=prov('D', 'Plutarch, Antony 58.'))
talk('D4', 'HOST', "And the part that mattered?", 'plainly', "The host, plainly — a prompt.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_e', 'frame_host_c'], p=prov('V'))
talk('D5', 'GUEST', "That when he died, he wished to be sent to me. In Egypt. Even if he died in Rome.", 'level, a thin edge',
     "The woman, level. A thin edge comes in on the last sentence and stays thin.",
     gest=('still', ''), pref=['frame_cleopatra_i', 'frame_cleopatra_e'], p=prov('D', 'Plutarch, Antony 58.'),
     place='the callback Part 2 pays (*"So Antony\'s will got its way after all"*).')
talk('D6', 'HOST', "And Rome declared war.", 'the charge, plainly', "The host states the charge plainly, low.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host', 'frame_host_f'], p=prov('D', 'Plutarch, Antony 60.'))
talk('D7', 'GUEST', "On me. Not on him.", 'flat, then exact', "The woman, flat, then exact on the second sentence. Nothing raised.",
     typ='INTERJECTION', gest=('advance', 'Not on him'), pref=['frame_cleopatra', 'frame_cleopatra_c'], p=prov('D', 'Plutarch, Antony 60; Dio 50.4.'))
react('D7r', 'HOST', "The host sits in silence. His lips stay gently closed and his jaw stays still the whole time; he breathes slowly and quietly through his nose. His eyes stay on the person sitting opposite him, off frame to the right. He lets it land, entirely still, his gaze on her.",
      4, 'covers the tail of [[D7]] from *"Not on him"*, then holds a beat. [[D8]] chains from this clip.',
      pref=['frame_host_d', 'frame_host_e'])
talk('D8', 'HOST', "Why you?", 'the real question', "The host asks the real question, quiet and direct.",
     start=('chain', 'D7r'), typ='INTERJECTION', gest=('still', ''), p=prov('V'))
talk('D9', 'GUEST', "Because a Roman cannot march in triumph over Romans. Over a foreign queen, he can march as often as he likes.",
     'coolly correcting, the barb held under', "The woman corrects the premise coolly, then plainly; the barb at the end stays held under.",
     gest=('settle', 'a foreign queen'), pref=['frame_cleopatra_b', 'frame_cleopatra_e'],
     p=prov('I', 'Dio 50.4–6 (war declared on her, so Antony\'s side could desert him as patriots).'))
talk('D10', 'HOST', "Then the case against you, the way Rome would put it: Egypt stayed free because you sold it, one Roman at a time. Caesar, then Antony. Answer that.",
     'attributed and level, plain on the challenge',
     "The host puts Rome's case, attributed and level — he is quoting the charge, not making it. He reads the two names evenly and makes the challenge plainly, never hardening into accusation.",
     gest=('advance', 'Answer that'), pref=['frame_host_b', 'frame_host_c'], p=prov('I', 'the Augustan account, put as Rome\'s case.'))
react('D10r', 'GUEST', "The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She lets him finish; her chin lifts a fraction and she holds his gaze.",
      4, 'covers the tail of [[D10]] from *"Caesar, then Antony"*, then holds a beat — the charge plays on **her** face. [[D11a]] chains from this clip.',
      pref=['frame_cleopatra_i', 'frame_cleopatra'])
talk('D11a', 'GUEST', "Egypt had grain, gold, and no army that could stop Rome. So I made myself the one thing each of them could not do without.",
     'plain, then asserting',
     "The woman, plain, then asserting on the second sentence. Her voice stays low and never rises.",
     start=('chain', 'D10r'), gest=('settle', 'the one thing'), p=prov('I', 'Suetonius, Julius 54; Plutarch, Antony 56.'),
     place='`SPLIT` A — her thesis needs 15.0 s whole, at the cap; split where the weight comes on. Seam into [[D11b]]: `PUNCH` exactly on the seam (Mode 4 §2, fix b), held to the end of [[D11b]].')
talk('D11b', 'GUEST', "Rome calls that seduction. It is what a kingdom without an army does, if it wants to stay a kingdom.",
     'with weight, then quieter on the admission',
     "The woman puts weight on the first sentence; the last is quieter — an admission, not a plea. Her voice stays low and never rises.",
     start=('chain', 'D11a'), gest=('advance', 'Rome calls that seduction'), p=prov('I', 'Suetonius, Julius 54; Plutarch, Antony 56.'),
     place='`SPLIT` B, and `CUT-IN:hold` A — [[D12]] sits under her at *"Rome calls that seduction"*, ~3 dB down; she does not stop. **Stay on her**; punch-in at *"Rome calls that seduction"*, held to the end. Her thesis — key line 4 (thumbnail and reels, no pull-quote).')
talk('D12', 'HOST', "But that's not how Rome told it.", 'starting to come in, firm but not loud',
     "The host starts to come in over her, firm but not loud, as though he has an objection ready. His tone stays level and never becomes a raised voice.",
     typ='INTERJECTION', gest=('advance', 'But'), pref=['frame_host_b', 'frame_host_e'], spoken="But that's—",
     p=prov('V', 'an attempt, not a claim; only "But that\'s" is heard.'),
     place='audio only, under [[D11b]] at *"Rome calls that seduction"* — the failed attempt of a `CUT-IN:hold`. **Cut the audio after "But that\'s"**; she carries on over it. Picture discarded.',
     notes='The outline gives the heard words, *"But that\'s—"*. The run-on words are generated only so the model is never asked to stop mid-sentence (Mode 4 §8b); they are never heard and carry no claim.')
talk('D13', 'HOST', "And it held.", 'quietly', "The host, quietly — conceding the point plainly.",
     typ='INTERJECTION', gest=('still', ''), pref=['frame_host_f', 'frame_host'], p=prov('V'))
talk('D14', 'GUEST', "For twenty years.", 'even', "The woman, even. Nothing added.", typ='INTERJECTION', gest=('still', ''),
     pref=['frame_cleopatra_e', 'frame_cleopatra_c'], p=prov('I', 'her reign, 51–31 BC.'))
talk('D15', 'HOST', "Until the war. How much of it was yours?", 'turning, then plain on the question',
     "The host turns it, then asks plainly. His voice lifts at the end; never accusing.",
     gest=('settle', 'How much'), pref=['frame_host_c', 'frame_host_d'], p=prov('V'))
talk('D16', 'GUEST', "Two hundred of Antony's ships, and twenty thousand talents. I paid for a good part of it.", 'exact, then dry',
     "The woman, exact on the numbers, then dry. She does not stress them.",
     gest=('settle', 'I paid'), pref=['frame_cleopatra_i', 'frame_cleopatra_b'], p=prov('D', 'Plutarch, Antony 56.'))

# ============================== CLOSE ==============================
row(k='CLOSE', kind='head', title='Close', q='')
talk('E1a', 'HOST', "Actium. Thirty-one BC. The middle of the battle, and your sixty ships raise their sails and go straight through the fighting.",
     'slow on the scene',
     "The host sets the scene slowly and evenly — no drama in the voice.",
     gest=('still', ''), pref=['frame_host_e', 'frame_host_b'], p=prov('D', 'Plutarch, Antony 64–66.'),
     place='`SPLIT` A — the whole line needs 15 s under duration model v3, at the cap. **Context card 09** (Actium) enters on *"Actium"*, over him. [[E2]] covers from *"and your sixty ships"* across the seam into [[E1b]] (Mode 4 §2, fix a). `MUSIC_Drone_High` peaks under the b-roll.')
talk('E1b', 'HOST', "Antony leaves his fleet and follows you. Did you run?",
     'the question landing plain',
     "The host asks the question plainly — no drama in the voice, and never an accusation.",
     start=('chain', 'E1a'), gest=('advance', 'Did you run'), p=prov('D', 'Plutarch, Antony 64–66.'),
     place='`SPLIT` B — [[E2]] runs on over *"Antony leaves his fleet and follows you"*; [[E3]] covers *"Did you run?"* and the silence after — the question plays on her face.')
broll('E2', 'Sixty ships raising sail through the battle line, seen from the water.',
      "The battle of Actium, 31 BC, seen from low on the water: a line of ancient oared war galleys — long low hulls, banks of oars, a bronze ram at the waterline, one mast each — hoisting single square sails and pulling away through a gap between other galleys locked together in the middle distance; smoke from burning ships drifting low across the water. No faces. No cannon or gun smoke, no tall sterns or towering hulls, no ships with more than one mast, no rigging of later sailing ships.",
      'The camera drifts slowly to the left, following the ships.',
      'The sails rise and fill; the ships pull away through the gap; smoke drifts across the water.',
      'Audio: ambience only — wind, oars and water, distant shouting, low. No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.',
      7, 'covers [[E1a]] from *"and your sixty ships"* to [[E1b]]\'s *"follows you"* — it also hides the split seam; context card 09 rides over its start.',
      notes='**added in Mode 4.** The outline names *"sixty ships through the line"* as Act D\'s image but marks no `BROLL`; this is that picture. Seen from the water, never from above (the aerial-subject failure).')
react('E3', 'GUEST', "The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. She holds his eyes; nothing else moves.",
      5, 'covers [[E1b]] from *"Did you run?"* to its end, then holds the silence. [[E4]] chains from this clip.',
      pref=['frame_cleopatra_e', 'frame_cleopatra'])
talk('E4', 'GUEST', "Everyone who wrote that battle down was watching from the other side.", 'level, opening more than it closes',
     "The woman, level. It opens more than it closes — no defence in it, and no appeal.",
     start=('chain', 'E3'), gest=('still', ''), p=prov('I'))
talk('E5', 'HOST', "Then next time, you tell it from yours.", 'quiet, to her',
     "The host hands it to her, quiet and warm, speaking to her rather than to the audience.",
     gest=('settle', 'you tell it'), pref=['frame_host_b', 'frame_host_c'], p=prov('V'),
     place='the hand-off; nothing after it but the close. No goodbye.')
row(k='BUMP', kind='bumper')

# ------------------------------------------------------------------ beat maps from the outline (T2 settled 2026-09-24)
# A line whose outline note has one '→'-separated delivery per sentence gets a beat map: one delivery per sentence,
# in one clip. Where the counts differ, or the line was split by Mode 4, the single delivery note stays.
sys.path.insert(0, os.path.join(ROOT, 'Fixed_Assets', 'tools'))
import outline_lines as _O
_OUT = {l: n for _, _, n, l in _O.spoken(open(os.path.join(ROOT, 'Episodes', 'Cleopatra', 'OUTLINE.md'), encoding='utf-8').read())}
for r in R:
    if r.get('kind') != 'talk' or r.get('beatmap') or r.get('spoken'): continue
    note = _OUT.get(r['line'])
    if not note or '→' not in note: continue
    notes = [x.strip(' ;,') for x in note.split('→')]
    sents = [x for x in re.split(r'(?<=[.?!])\s+', r['line']) if x]
    if len(notes) == len(sents) >= 2:
        r['beatmap'] = list(zip(notes, sents))

# ------------------------------------------------------------------ picture plan — Screen share (Mode 4 §8b), 2026-09-24
# The guest carries >= 65% of the studio picture. His questions play on her listening (a guest REACTION her
# answer chains from); his reactions during her lines are two-ups; at most two full-frame host reactions.
# Every talking row gets `scr` (what is on screen, by word); reactions get `span` (what they cover) and `beat`
# (screen time outside speech). The builder turns these into `screen:` lines for screen_share.py.
def _i(k): return next(i for i, r in enumerate(R) if r.get('k') == k)
def upd(k, **kw): R[_i(k)].update(kw)
def after(k, r): R.insert(_i(k) + 1, r)
def drop(k): R.pop(_i(k))
LISTEN_NOTE = "The woman sits in composed silence. Her lips stay gently closed and her jaw stays still the whole time; she breathes slowly and quietly through her nose. Her eyes stay on the person sitting opposite her, off frame to the left. "
def listen(k, after_k, covers, word=None, beat=0.3, body='', start=None, pref=None, place='', test=None):
    after(after_k, dict(k=k, kind='react', who='GUEST', body=LISTEN_NOTE + body, dur=None, span=(covers, word),
                        beat=('G', beat), start=start, pref=pref or ['frame_cleopatra_b', 'frame_cleopatra', 'frame_cleopatra_e'],
                        place=place, notes='', test=test))
def under(k, lk):   # a host line that runs entirely under her listening clip
    r = R[_i(k)]; r['start'] = None; r['pref'] = r.get('pref') or ['frame_host']
    r['place'] = f'audio only, under [[{lk}]] — his line runs over her listening (Screen share, Mode 4 §8b); his picture is discarded.' + (' ' + r['place'] if r.get('place') else '')
    r['scr'] = [('G', None)]

# --- opening
upd('N2', scr=[('H', None), ('G', 'last queen')])
upd('W1', beat=('G', 1.5))
upd('G1', notes='**T8 settled on this row (2026-09-24):** Kling\'s label form won the A/B (`shots/_tests/T_008_A.mp4` vs `T_008_B.mp4`) — clearer change of delivery between sentences, visible in her face. Keep `T_008_B` as `P1_006`. Both takes strain on the last word *"described"* (a /skr/ cluster and a final /bd/) — a word-final stop cluster as a clip\'s last word; hide it with the cut, or Kling\'s lip-sync tool.')
# --- Act A
upd('A2', scr=[('G', None), ('2UP', 'They came')], twoup=1, test='T6',
    place='**HOOK, first option** — Mode 6 re-picks the hook from the finished part. Key line 1. **Two-up #1** with [[A2r]] from *"They came for my treasury"* to ~1.5 s after her last word — his nod beside her, not instead of her.')
upd('A2r', span=('A2', 'They came'), beat=('2UP', 1.5), test='T6',
    place='**the host\'s half of two-up #1** (left), beside [[A2]] (right) from *"They came for my treasury"* to ~1.5 s after her line. Not on screen alone.')
listen('LA3', 'A2r', 'A3', None, 3.0, 'She holds the position she is in, composed and unhurried; her gaze stays on him, and she is otherwise still.',
       start=('chain', 'A2'), place='her held face after [[A2]]: **pull-quote 01 lands here** (a 3 s beat), then [[A3]] runs under her. [[A4]] chains from this clip.')
under('A3', 'LA3')
upd('A4', start=('chain', 'LA3'))
upd('A5', scr=[('H', None), ('G', 'Hebrews')], extra=1.0,
    place='on picture to *"without an interpreter."*, then [[LA5]] takes the picture for the list — her languages, on her face. **+1 s:** the line ends on a comma list of names (Mode 4 §2, measured on this clip in T1: the 8 s take ran its speech to the last frame).',
    notes='**T1 settled 2026-09-24 on this row:** a separate `Pronunciation:` paragraph was read aloud (*"Medes"* said twice, `shots/_tests/T1_A.mp4`); the respelling *"Meeds"* inside the quote was right (`T1_B.mp4`, 8 s — regenerate at 9 s for a clean tail). The prompt now carries the respelling; the subtitle keeps *Medes*.')
listen('LA5', 'A5', 'A5', 'Hebrews', 0.5, 'Her head rests tilted very slightly to one side and stays there; her gaze stays on him.',
       place='covers [[A5]] from *"Hebrews"* to its end. [[A6]] chains from this clip.')
upd('A6', start=('chain', 'LA5'))
upd('A9', scr=[('H', None), ('G', 'Why does')], place='on picture to *"in the world."*, then [[LA9]] for *"Why does it need Rome?"*')
listen('LA9', 'A9', 'A9', 'Why does', 0.3, 'Her chin lifts a fraction; otherwise she is still.', test='T2',
       place='covers [[A9]] from *"Why does it need Rome?"*. [[A10]] chains from this clip.')
upd('A10', start=('chain', 'LA9'))
upd('A13', scr=[('G', None)])
listen('LA14', 'A13', 'A14', None, 0.3, 'She holds his gaze, entirely composed, the faintest dryness at the corner of her mouth.',
       start=('chain', 'A12'), place='chained from [[A12]]: carries the tail of her line (with [[A13]]\'s *"Charming."* under it) and [[A14]]. [[A15]] chains from this clip.')
under('A14', 'LA14')
upd('A15', start=('chain', 'LA14'))
upd('A19', scr=[('G', None), ('BROLL', 'they handed')])
upd('A20', beat=('BROLL', 1.0))
upd('A21', scr=[('BROLL', None)])
upd('A22', scr=[('G', None), ('2UP', 'Rome does not')], twoup=2,
    place='Key line 2: *"Rome does not thank you. It judges you."* **Two-up #2** with [[A22r]] from *"Rome does not thank you"* to ~1 s after her line.')
upd('A22r', span=('A22', 'Rome does not'), beat=('2UP', 1.0),
    place='**the host\'s half of two-up #2** beside [[A22]], from *"Rome does not thank you"*. `MUSIC_Drone_Low` fades out across it.')
listen('LA23', 'A22r', None, None, 3.5, 'She holds the position she is in, perfectly still, her gaze level on him.',
       start=('chain', 'A22'), place='her held face after [[A22]]: **pull-quote 02 lands here** (a 3.5 s beat, soundscape only). Then cut to him for [[A23]].')
upd('A23', start=None, pref=['frame_host_d', 'frame_host_e'])
drop('A24r')
listen('LA25', 'A24', 'A25', None, 1.5, 'She holds his gaze and lets the silence sit; nothing else moves.',
       start=('chain', 'A24'), place='the `BEAT` after her *"Yes."* on her face, then [[A25]] under it — the act\'s open loop plays on her. Cut straight to the act break.')
under('A25', 'LA25')
# --- Act B
upd('B5', beat=('H', 0.5))
listen('LB7', 'B6', 'B7', None, 0.3, 'She takes the point without moving, her gaze steady on him.',
       start=('chain', 'B6'), place='chained from [[B6]]: carries [[B7]]. [[B8]] chains from this clip.')
under('B7', 'LB7')
upd('B8', start=('chain', 'LB7'), scr=[('G', None), ('BROLL', 'And the harbour')])
listen('LB12', 'B11', 'B12', None, 0.5, 'At her sister\'s name her gaze holds on him a moment longer; nothing else moves.',
       start=('chain', 'B11'), place='chained from [[B11]]: the name lands on **her** face. [[B13]] chains from this clip.')
under('B12', 'LB12')
upd('B13', start=('chain', 'LB12'), scr=[('G', None), ('BROLL', 'led her')], test=None, pron=None)
upd('B17', scr=[('G', None)])
upd('B16r', span=('B18', None), beat=('G', 2.5), place='chained from [[B16]]: the `BEAT` after his echo, soundscape only, then [[B18]] under it — the question plays on her. [[B19]] chains from this clip.')
under('B18', 'B16r')
upd('B19', start=('chain', 'B16r'), scr=[('G', None), ('2UP', 'The crowd')], twoup=3,
    place='**Two-up #3** with [[B19r]] from *"The crowd pitied her"* to ~2 s after her line — he waits, he does not ask again.')
upd('B19r', span=('B19', 'The crowd'), beat=('2UP', 2.0),
    place='**the host\'s half of two-up #3** beside [[B19]]. [[B20]] chains from this clip, full frame.')
upd('B24', scr=[('H', None), ('G', 'Who did')], place='on picture to *"apart again."*, then [[LB24]] for *"Who did you back?"*')
listen('LB24', 'B24', 'B24', 'Who did', 0.3, 'Her chin lifts a fraction.',
       place='covers [[B24]] from *"Who did you back?"*. [[B25]] chains from this clip.')
upd('B25', start=('chain', 'LB24'))
# --- Act C
upd('C1r', span=('C2', 'to his enemy'), beat=('H', 0.0))
upd('C2', scr=[('H', None), ('G', 'to his enemy')])
upd('C4', scr=[('G', None), ('BROLL', 'So I came'), ('G', 'Nobody')])
upd('C7', scr=[('G', None), ('2UP', 'She arrives')], twoup=4,
    place='Key line 3: *"A queen does not arrive at a trial as the accused."* **Two-up #4** with [[C7r]] from *"She arrives as a goddess"* to ~1 s after her line — his silent laugh beside her.')
upd('C7r', span=('C7', 'She arrives'), beat=('2UP', 1.0), place='**the host\'s half of two-up #4** beside [[C7]].')
listen('LC8', 'C7r', None, None, 3.5, 'She holds the position she is in, composed, the faintest satisfaction held still.',
       start=('chain', 'C7'), place='her held face after [[C7]]: **pull-quote 03 lands here** (a 3.5 s beat). Then cut to him for [[C8]].')
upd('C8', start=None, pref=['frame_host_e', 'frame_host'])
upd('C9', scr=[('G', None), ('H', 'He gave')])
upd('C9r', beat=('H', 1.5), place='**full-frame host reaction 1 of 2** — the crack: covers the tail of [[C9]] from *"He gave it to me"*, then holds. [[C10]] chains from this clip.')
upd('C10', scr=[('H', None), ('G', 'In a sanctuary')])   # T6b 2026-09-24: the silence goes on her face, not a two-up
upd('C12', beat=('G', 1.0), test='T3 · end-frame test', notes='**End-frame test (Salah\'s idea, 2026-09-24) — generate this clip with the end-frame slot set to the same seed frame as its start (`frame_cleopatra_b` → `frame_cleopatra_b`), Standard, audio off, stationary preset on.** Judge: does she drift naturally and come back, or does it read as a loop / a rushed return in the last half-second? **If it passes:** [[C13]] starts from `frame_cleopatra_b` itself instead of this clip\'s last frame — a pixel-identical join with no extraction and no grade — and the kit is rebuilt so every listening reaction that is followed by its speaker\'s answer works this way (most of Pass 2 disappears). **If it fails:** keep the chain; [[C13]] starts from this clip\'s last frame as written.')
listen('LC17', 'C16', 'C17', None, 0.3, 'She hears the question without a flicker; her gaze stays level on him.',
       start=('chain', 'C16'), place='chained from [[C16]]: carries [[C17]] — the question plays on her. [[C18]] chains from this clip.')
under('C17', 'LC17')
upd('C18', start=('chain', 'LC17'))
upd('C21', scr=[('H', None), ('BROLL', 'A silver stage')])
upd('C23', scr=[('BROLL', None), ('G', "with Caesar's")])
listen('LC24', 'C23', 'C24', None, 0.3, 'She lets him finish, entirely still, the faintest dryness at the corner of her mouth.',
       start=('chain', 'C23'), place='chained from [[C23]]: carries [[C24]]. [[C25]] chains from this clip.')
under('C24', 'LC24')
upd('C25', start=('chain', 'LC24'), scr=[('G', None), ('2UP', 'He gave my son')], twoup=6,
    place='**Two-up #6** with [[C25r]] from *"He gave my son Parthia"* to ~1 s after her line — his laugh escapes beside her.')
upd('C25r', span=('C25', 'He gave my son'), beat=('2UP', 1.0), place='**the host\'s half of two-up #6** beside [[C25]]. [[C26]] chains from this clip, full frame.')
# --- Act D
upd('D1', scr=[('H', None), ('BROLL', 'Vestal')])
upd('D3', scr=[('BROLL', None), ('G', 'Then he read')])
listen('LD4', 'D3', 'D4', None, 0.3, 'She holds his gaze, composed.',
       start=('chain', 'D3'), place='chained from [[D3]]: carries [[D4]]. [[D5]] chains from this clip.')
under('D4', 'LD4')
upd('D5', start=('chain', 'LD4'))
upd('D7', scr=[('2UP', None)], twoup=7, place='**Two-up #7** with [[D7r]] for the whole line and ~1.5 s after — he lets it land, beside her.')
upd('D7r', span=('D7', None), beat=('2UP', 1.5), place='**the host\'s half of two-up #7** beside [[D7]].')
listen('LD8', 'D7r', 'D8', None, 0.3, 'She meets the question without moving, her chin a fraction high.',
       start=('chain', 'D7'), place='chained from [[D7]] (full frame again after the two-up): carries [[D8]]. [[D9]] chains from this clip.')
under('D8', 'LD8')
upd('D9', start=('chain', 'LD8'))
upd('D10', scr=[('H', None), ('G', 'Egypt stayed')],
    place='on picture to *"the way Rome would put it:"*, then [[D10r]] from *"Egypt stayed free"* — the charge plays on her face.')
upd('D10r', span=('D10', 'Egypt stayed'), beat=('G', 1.0),
    place='covers [[D10]] from *"Egypt stayed free"* to its end, then holds a beat. [[D11a]] chains from this clip.')
upd('D12', scr=[('G', None)])
upd('D15', scr=[('H', None), ('G', 'How much')], place='on picture for *"Until the war."*, then [[LD15]] for the question.')
listen('LD15', 'D15', 'D15', 'How much', 0.3, 'Her gaze stays on him; nothing moves.',
       place='covers [[D15]] from *"How much of it was yours?"*. [[D16]] chains from this clip.')
upd('D16', start=('chain', 'LD15'))
# --- close
upd('E1a', scr=[('H', None), ('BROLL', 'and your sixty')])
upd('E1b', scr=[('BROLL', None), ('G', 'Did you run')])
upd('E3', span=('E1b', 'Did you run'), beat=('G', 2.0))

# ------------------------------------------------------------------ end-frame rule (settled 2026-09-24, P1_086 test)
# A silent reaction that starts from a SEED frame and is followed by its own speaker's clip ends on that same seed
# frame (Standard's end-frame slot); the following clip then starts from the seed frame itself — an exact join, no chain.
_ENDF = set()
def _apply_endframes():
    by = {r['k']: r for r in R if r.get('k')}
    for r in R:
        if r.get('kind') != 'talk' or not isinstance(r.get('start'), tuple) or r['start'][0] != 'chain': continue
        src = by[r['start'][1]]
        if src['kind'] == 'react' and isinstance(src.get('start'), str) and src['who'] == r['who']:
            _ENDF.add(src['k']); r['start'] = src['start']; r['after_endframe'] = src['k']

# ------------------------------------------------------------------ assign ids, poses, durations
# retired ids: a dropped row keeps its number empty so clips already generated keep their names
RETIRED = {'C12': 'P1_085', 'B10': 'P1_050'}   # B10 follows the retired B9 b-roll (P1_050)
# added ids: a row inserted after clips exist takes its neighbour's number + a letter, so nothing downstream renumbers
ADDED = {'W0': 'P1_003a'}   # guest cut-away after the host's turn, added 2026-09-27   # the host's half of the shared-silence two-up, dropped 2026-09-24 (T6b)
ids = {}; n = 0
for r in R:
    if r['kind'] in ('head',): continue
    if r.get('k') in ADDED: r['id'] = ADDED[r['k']]; ids[r['k']] = r['id']; continue
    if r.get('k') in RETIRED: n += 1; assert f'P1_{n:03d}' == RETIRED[r['k']], (r['k'], n)
    n += 1; r['id'] = f'P1_{n:03d}'; ids[r['k']] = r['id']
def refs(s):
    return re.sub(r'`?\[\[(\w+)\]\]`?', lambda m: f'`{ids[m.group(1)]}`', s or '')

hist = {'HOST': [], 'GUEST': []}; pose_of = {}
for r in R:
    if r['kind'] not in ('talk', 'react'): continue
    who = r['who']; st = r.get('start')
    if st is None:
        opts = HOST_FRAMES if who == 'HOST' else GUEST_FRAMES
        recent = hist[who][-3:]
        pref = r.get('pref') or []
        cand = [p for p in pref if p not in recent] + [p for p in opts if p not in recent and p not in pref]
        r['start'] = cand[0]; r['auto_pose'] = cand[0] not in pref
    st = r['start']
    if isinstance(st, str):
        pose_of[r['k']] = st
    else:
        pose_of[r['k']] = pose_of[st[1]]
    if r['kind'] == 'talk' and r.get('prov') is None: raise SystemExit('no provenance ' + r['k'])
    # an OFFMIC row's picture is discarded — it is not an appearance
    if not (r['kind'] == 'talk' and 'audio only, under' in (r.get('place') or '')):
        hist[who].append(pose_of[r['k']])

_apply_endframes()
def chained(r): return not isinstance(r.get('start'), str)
TALK_RATE, REACT_RATE, BROLL_RATE = 10, 8, 10
for r in R:
    if r['kind'] == 'talk':
        ent = 0.7 if isinstance(r.get('start'), str) and POSE.get(r['start'], {}).get('entry') else 0.0   # hand comes down first
        s, need, d = syl.dur2(r['line'], chained=chained(r), extra=r['extra'] + ent)
        r['syl'], r['need'], r['dur'] = s, need, d
        r['cr'] = d * (12 if r.get('turn_end') else TALK_RATE)   # Kling 3.0 Standard + audio for an end-frame turn
        if r['typ'] is None: r['typ'] = 'INTERVIEW'
    elif r['kind'] == 'broll': r['cr'] = r['dur'] * BROLL_RATE + 3

# ---- screen accounting (speech-model seconds on screen), Mode 4 §8b Screen share
def seg_secs(t):
    t = t.strip()
    if not re.search(r'[A-Za-z]', t): return 0.0
    return syl.count(t)[0] / syl.RATE + syl.BREAK * syl.breaks_in(t)
def spoken_of(r): return (r.get('spoken') or r['line']).rstrip(' —')
def after_word(r, word):
    t = spoken_of(r)
    if word is None: return t
    i = t.find(word); assert i >= 0, (r['k'], word); return t[i:]
BYK = {r['k']: r for r in R if r.get('k')}
for r in R:
    if r['kind'] == 'react':
        if r.get('span') and r['span'][0]:
            src = BYK[r['span'][0]]
            r['dur'] = min(15, max(3, math.ceil(seg_secs(after_word(src, r['span'][1])) + (r.get('beat') or ('G', 0))[1] + 0.8)))
        elif r.get('dur') is None:
            r['dur'] = max(3, math.ceil((r.get('beat') or ('G', 0))[1] + 0.8))
        r['cr'] = r['dur'] * REACT_RATE
def screen(r):
    v = {'G': 0.0, 'H': 0.0, '2UP': 0.0, 'BROLL': 0.0}
    if r['kind'] == 'talk':
        t = spoken_of(r)
        scr = r.get('scr') or ([('G', None)] if 'audio only, under' in (r.get('place') or '') else [('G' if r['who'] == 'GUEST' else 'H', None)])
        cuts = [(0 if w is None else t.find(w), b) for b, w in scr]
        for (a, b), nxt in zip(cuts, cuts[1:] + [(len(t), None)]):
            assert a >= 0, (r['k'], scr)
            v[b] += seg_secs(t[a:nxt[0]])
    elif r['kind'] in ('react', 'broll') and r.get('beat'):
        v[r['beat'][0]] += r['beat'][1]
    return v

# ---- 720p for audio-only talking clips (Salah, 2026-09-24): a clip whose picture is never used — his line under her
# listening, an off-mic interjection, a line under b-roll — is generated at 720p, Turbo 8 cr/s instead of 10.
LOWRES_RATE = 8
for r in R:
    if r['kind'] == 'talk':
        v = screen(r); own = v['H'] if r['who'] == 'HOST' else v['G']
        audio_only = ('audio only, under' in (r.get('place') or '')) or (own == 0 and v['2UP'] == 0)
        if audio_only:
            r['lowres'] = True; r['cr'] = r['dur'] * LOWRES_RATE

# ------------------------------------------------------------------ writers
def para(*ps):
    ps = [p for p in ps if p]
    if ps[0] != LOCK: return '\n\n'.join([ps[0]] + [' ' + p for p in ps[1:]])
    body = ps[1:]; voice = [p for p in body if p.startswith('Voice:')]; audio = [p for p in body if p.startswith('Audio:')]
    mid = [p for p in body if p not in voice and p not in audio]
    return '\n\n'.join([LOCK, ' '.join([ONE] + mid)] + voice + audio + [CONT])
def start_txt(r):
    st = r['start']
    if isinstance(st, str): return f'`{st}`'
    if st[0] == 'chain': return f'`chain from {ids[st[1]]}`'
    if len(st) > 3:   # timed on the generated clip
        return f'`chain from {ids[st[1]]} at {st[3]:.2f}s` — the frame at the end of *"{st[2]}"* (timed on the take); in Kling, set the start frame from `{ids[st[1]]}` at this time'
    return f'`chain from {ids[st[1]]} at cut` (the cut word *"{st[2]}"* — time it after `{ids[st[1]]}` is generated, then write `at <seconds>s`)'
def gesture(r):
    if r.get('gest_text'): return r['gest_text']
    g = r.get('gest')
    if g is None: return ''
    kind, w = g
    tmpl = (CHAINED[r['who']] if chained(r) else POSE[r['start']])[kind]
    return tmpl.format(w=w)
from tone_map import tone   # shared across guests: Fixed_Assets/tools/tone_map.py
# Mode 4 §3 3b: written as it sounds, inside the quote; subtitles keep the true spelling.
# L48 (2026-09-27): read from the outline's Pronunciation table — every row says `write: X` or `plain`.
def _respell_table():
    o = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'OUTLINE.md'), encoding='utf-8').read()
    sec = o[o.index('### Pronunciation'):]; sec = sec[:sec.index('\n## ')]
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\| ([A-Z][\w'’]+) \|[^|\n]*\|[^|\n]*?write: ([^|·\n]+?)\s*\|", sec, re.M)}
RESPELL = _respell_table()
def respell(t):
    for a, b in RESPELL.items(): t = re.sub(r'\b' + re.escape(a) + r'(?![\w])', b, t)
    return t
def with_hold(r):
    """A silent reaction from a seed frame names the pose, held (pose table `hold`), after the eyeline sentence."""
    st = r.get('start'); body = r['body']
    if not (isinstance(st, str) and st in POSE): return body
    hold = POSE[st]['hold']
    m = re.search(r'off frame to the (?:left|right)\. ', body)
    return body[:m.end()] + hold + ' ' + body[m.end():] if m else body + ' ' + hold
# L57 (2026-09-28, Salah): P1_028 looked into the lens on its last sentence. Only 16 of 93 talking prompts named where
# the eyes go; a line with "an edge in the last sentence" got delivered to camera. Every talking prompt now ends its
# action paragraph with the eyeline, positively (never "does not look at the lens" — naming it invites it, as with blinks).
def eyeline(r):
    st = r.get('start'); seed = st if isinstance(st, str) else ''
    if 'direct' in seed or r.get('k') in ('N1a', 'N1b'): return ''   # direct address / the turn clip carry their own
    side = 'left' if r['who'] == 'GUEST' else 'right'
    pro, poss = ('She', 'Her') if r['who'] == 'GUEST' else ('He', 'His')
    other = 'him' if r['who'] == 'GUEST' else 'her'
    return f"{poss} eyes stay on the person sitting opposite {pro.lower() if False else ('her' if r['who']=='GUEST' else 'him')}, off frame to the {side}, from the first word to the last."
def talk_prompt(r, beat=False):
    lab = LABEL[r['who']]
    st = r.get('start')
    entry = POSE[st]['entry'] + ' ' if isinstance(st, str) and POSE.get(st, {}).get('entry') else ''
    # pose entry (hand off the jaw) sits directly before the first words, in sequence — at the end of the
    # register paragraph Kling played it in the first pause instead (P1_084, 2026-09-24)
    if beat and r.get('beatmap'):
        segs = r['beatmap']
        # the physical beat: the row's gesture, without its quoted anchor (quotes would be read as speech),
        # placed just before the segment that holds the anchor word (after the first, if it is there)
        g = gesture(r); at = 1; beat_txt = ''
        m = re.match(r'On "([^"]+)" (.+)$', g or '')
        if m:
            beat_txt = ' ' + m.group(2)[0].upper() + m.group(2)[1:]
            k = next((i for i, (_, t) in enumerate(segs) if m.group(1) in t), 1)
            at = max(1, k)
        body = entry + f'{lab} ({tone(segs[0][0])}): "{respell(segs[0][1])}"'      # label form, T8 settled 2026-09-24; Kling tone words
        for i, (n_, t) in enumerate(segs[1:], 1):
            body += (beat_txt if i == at else '') + f' {lab} ({tone(n_)}): "{respell(t)}"'
        hold = '' if m else (g or '')     # a pose hold with no anchor word stays in the prompt (fixed 2026-09-24)
        return para(LOCK, r['reg'], body, hold, eyeline(r), VOICE[r['who']], AUDIO_TALK)
    say = entry + f'{lab} ({tone(r["note"])}): "{respell(r["line"])}"'      # label form, T8 settled 2026-09-24; Kling tone words
    pron = ' '.join(f'Pronunciation: "{w}" is said {p}.' for w, p in (r.get('pron') or []))
    return para(LOCK, r['reg'], say, pron, gesture(r), eyeline(r), VOICE[r['who']], AUDIO_TALK)

out = []
def w(s=''): out.append(s)
def hdr(r):
    if r['kind'] == 'talk':
        who = r['who']
        if r.get('lowres'):
            return f"**{r['id']}** · {r['typ']} · {who} · **{r['dur']}s** · Kling 3.0 Turbo **720p**, audio on · 8 cr/s · **{r['cr']} cr** · audio only — picture never used"
        if r.get('turn_end'):
            return f"**{r['id']}** · {r['typ']} · {who} · **{r['dur']}s** · Kling 3.0 Standard, audio ON · 12 cr/s · **{r['cr']} cr** · end frame pins the turn"
        return f"**{r['id']}** · {r['typ']} · {who} · **{r['dur']}s** · Kling 3.0 Turbo, audio on · 10 cr/s · **{r['cr']} cr**"
    if r['kind'] == 'react':
        return f"**{r['id']}** · REACTION · {r['who']} · **{r['dur']}s** · Kling 3.0 Standard, audio OFF · 8 cr/s · **{r['cr']} cr**"
    if r['kind'] == 'broll':
        return f"**{r['id']}** · BROLL_GEN · **{r['dur']}s** · Kling 3.0 Turbo, audio on · 10 cr/s · **{r['cr'] - 3} cr** + 3 cr still"

def scr_line(r):
    v = screen(r)
    return '**screen:** ' + ' · '.join(f'{k} {v[k]:.1f}' for k in ('G', 'H', '2UP', 'BROLL'))
def emit_row(r):
    k = r['kind']
    if k == 'head':
        w(f"### {r['title']}"); w()
        if r['q']: w(f"*Question: {r['q']}*"); w()
        return
    if k == 'opening':
        w(f"**{r['id']}** · BRAND_OPENING · **19.17s** · FIXED SERIES ASSET · **0 cr**"); w()
        w("`Fixed_Assets/Branding/BRAND_opening.mp4` — one built file, byte-identical in every episode (spec in `Fixed_Assets/SERIES_FURNITURE.md`): the disclosure card 0.00–4.00, **the hook slot 4.00–8.00**, the intro 8.00–19.17, one unbroken piece of music with a clock strike opening each beat.")
        w()
        w(f"**edit_placement:** opens the video at 0:00. The nominated line is **`{ids['A2']}`, the whole line: *\"They came for my treasury. They wrote about my bed.\"*** — **a first option only** (Salah, 2026-09-23): Mode 6 re-picks the hook from the finished part as its most shocking guest moment, then renders it with `hook_build.py … --face 1365,180,240` (face emerging from the paper; framing from `CAST.md`). Her audio only, no host, no added music. If a take has no clean closed-mouth pause after the line, freeze on the last closed-mouth frame for the rest of the slot.")
        w("**Subtitle:** the card's wording is burned into the asset; the hook keeps its own subtitle.")
        w("**SFX:** nothing to add — music, strikes, `SFX_sand` and `SFX_plate` are inside the file."); w()
        return
    if k == 'actbreak':
        w(f"**{r['id']}** · BRAND_ACTBREAK · **5.0s** · FIXED SERIES ASSET · **0 cr**"); w()
        w(f"`Fixed_Assets/Branding/{r['file']}` — fixed furniture, zero credits.")
        prev = [x for x in R if x.get('id') and x['id'] < r['id'] and x['kind'] in ('talk', 'react', 'broll')][-1]
        nxt = [x for x in R if x.get('id') and x['id'] > r['id'] and x['kind'] in ('talk', 'react', 'broll')][0]
        w(f"**edit_placement:** plays between `{prev['id']}` and `{nxt['id']}`. Hard cut in, hard cut out at **5.000** — a finished object, never trimmed.")
        w("**Subtitle:** —"); w("**SFX:** inside the file."); w()
        return
    if k == 'bumper':
        w(f"**{r['id']}** · BUMPER_OUT · **5s transform, then held** · Kling 3.0 Standard, audio OFF · 8 cr/s · **40 cr** + 3 cr still"); w()
        w("`BRAND_bumper_out` — the studio two-shot turns into a charcoal drawing of itself on camera. The only place the two-shot appears. Format tested and approved (`SERIES_FURNITURE.md`)."); w()
        # L59 (2026-09-28): the outro wide is built per part from three references, so the figures are true to scale and
        # each person sits in the pose of their LAST clip (the host speaks last — a pose jump on the cut showed).
        def _last_seed(who):
            for q in reversed(R):
                if q.get('kind') in ('talk', 'react') and q.get('who') == who and q.get('id'):
                    st = q.get('start')
                    while isinstance(st, tuple): st = next((z.get('start') for z in R if z.get('k') == st[1]), None)
                    if isinstance(st, str) and 'direct' not in st: return st
            return None
        hs, gs = _last_seed('HOST'), _last_seed('GUEST')
        hdesc, gdesc = POSE.get(hs, {}).get('desc', ''), POSE.get(gs, {}).get('desc', '')
        w(f"**STEP 1 — the outro wide** (Seedream, three reference images, in this order): 1 `Fixed_Assets/cam3_wide.png` (the empty studio) · 2 `Start_Frames/Host/{hs}.png` (his last clip's pose) · 3 `Start_Frames/Cleopatra/{gs}.png` (her last clip's pose). Make 3–4, keep the best, save as `Start_Frames/Cleopatra/frame_wide_cleopatra_outro.png`. **No character sheet** — the pose frames gave the better likeness (tested 2026-09-28)."); w()
        w('```'); w("Keep image 1 exactly as it is — the same room, the same two armchairs at exactly the same size and position, the same table, microphones, lamp, shelves, blank panel, framing, lens, lighting, colour grade and film grain. "
                    f"Seat the man from image 2 in the armchair on the left and the woman from image 3 in the armchair on the right, each exactly as they appear in their own image: same face, hair, clothing and posture. "
                    f"He is {hdesc}, looking at her. She is {gdesc}, looking at him. "
                    "Both are life-size adults sitting deep in the armchairs: the chairs stay the size they are in image 1, their seated bodies fill the seats the way real people do, their hips at the back of the seat, the chair backs rising to their shoulder blades. Neither person is enlarged. The camera does not move closer. Only these two people are in the room. Photorealistic still, 16:9."); w('```'); w()
        w("**STEP 2 — the mark:** Claude runs `python3 Fixed_Assets/tools/outro_mark.py Start_Frames/Cleopatra/frame_wide_cleopatra_outro.png` → `…_outro_marked.png` (fixed panel coordinates; stops if the framing moved)."); w()
        w("**STEP 3 — the charcoal end frame:** Kling Image 3.0, 2K, 16:9, image-to-image from the marked wide — save as `…_outro_charcoal.png`:"); w()
        w('```'); w(para(STYLE, "Keep the composition, the framing and both figures exactly as they are in the source image — same positions, same postures, same scale, same size in frame.")); w('```'); w()
        w(f"**STEP 4 — the transformation** → `Shots/{r['id']}.mp4`: start = the marked wide, end = the charcoal still, **5 s, Kling 3.0 Standard, audio off, chip off**. Camera paragraph first; no lighting paragraph (the look is meant to change):"); w()
        w('```'); w('\n\n'.join([LOCK,
                        "The photographed room becomes a charcoal drawing of itself. The change begins at the edges of the frame and moves inward, so the two figures are the last thing to turn. Colour drains away to the warm grey of toned paper; shadows deepen into smudged charcoal and the paper grain rises through the whole image. Both people stay exactly where they are, at the same scale and in the same posture, through the whole change. Nobody moves, enters or leaves.",
                        AUDIO_SILENT.replace('quiet studio room tone only', 'quiet room tone only')])); w('```'); w()
        w(f"**STEP 5 — hold** the last frame ~3 s, clean, then cross-dissolve to `BRAND_endcard_p1.mp4`."); w()
        w(f"**edit_placement:** the close, straight after the host's hand-off in `{ids['E5']}`. `MUSIC_Outro_Bed` already running before the transformation begins; it decays, it does not resolve.")
        w("**Subtitle:** —"); w("**SFX:** room tone under the music."); w()
        return
    w(hdr(r))
    if k == 'broll':
        w(); w(f"> {r['desc']}"); w()
        w("**STEP 1 — still** (Kling image generation on kling.ai, 16:9, no reference image — as tested):"); w()
        w('```'); w(para(STYLE, *r['still'].split('\n\n'), "Wide still image, nothing in motion. Composition balanced and simple.")); w('```'); w()
        w("**STEP 2 — video**, image-to-video from that still:"); w()
        w('```'); w(para(r['move'], STYLE + ' ' + PERSIST, r['motion'], r['audio'])); w('```'); w()
        w(f"**edit_placement:** {refs(r['place'])}")
        w("**Subtitle:** — (the covered line's subtitle continues)")
        w("**SFX:** its own generated ambience, ducked under the dialogue it covers.")
        w(scr_line(r))
        if r.get('notes'): w(); w(refs(r['notes']))
        w(); return
    if k == 'react':
        if isinstance(r.get('start'), str):   # L44: EVERY seeded silent reaction ends on its own start frame
            nxt = '; the next clip starts from it' if r['k'] in _ENDF else ''
            w(f"`start_frame` {start_txt(r)} · `end_frame` `{r['start']}` — **the same seed frame** (Standard's end-frame slot){nxt}"); w()
        else:
            w(f"`start_frame` {start_txt(r)}"); w()
        w('```'); w(para(LOCK, with_hold(r), AUDIO_SILENT)); w('```'); w()
        w(f"**edit_placement:** {refs(r['place'])}")
        w("**Subtitle:** —")
        w(scr_line(r))
        if r.get('test'): w(f"**test:** `{r['test']}` (see §4b)")
        if r.get('notes'): w(); w(refs(r['notes']))
        w(); return
    # talk
    info = f" · {r['syl']} syllables · needs {r['need']}s (duration model v4{', +' + str(r['extra']) + ' s room' if r['extra'] else ''})"
    te = f" · `end_frame` `{r['turn_end']}` — the guest-facing pose (Kling 3.0 Standard's end-frame slot); the next clip starts from it" if r.get('turn_end') else ''
    w(f"`start_frame` {start_txt(r)}{te}{info}"); w()
    if r['k'] == 'N2': w(f"*Starts from the built seed `frame_host_b`, not from {ids['N1b']}: the guest cut-away {ids['W0']} sits between them, so wherever the turn ended never shows.*"); w()
    if r.get('after_endframe'): w(f"*Starts from the seed frame that `{ids[r['after_endframe']]}` ends on (end-frame rule, Mode 4 §7) — an exact join, not a chain.*"); w()
    if r.get('beatmap'):
        w('```'); w(talk_prompt(r, beat=True)); w('```'); w()
    elif r.get('respell'):
        w("**T1 variant A — separate `Pronunciation:` paragraph** (generate both, same seed frame, same settings; save as `shots/_tests/T1_A.mp4` and `T1_B.mp4`):"); w()
        w('```'); w(talk_prompt(r)); w('```'); w()
        w("**T1 variant B — respelled inside the line, no paragraph.** Kling's own guides say nothing about pronunciation (checked 2026-09-24: the Kling 3.0 user guide, the native-audio lip-sync guide, fal's Kling 3.0 guide); spelling a word as it sounds is the usual technique for speech models. The subtitle keeps the true spelling."); w()
        w('```'); w(talk_prompt(dict(r, line=r['respell'], pron=None))); w('```'); w()
        w("**Judge:** *Medes* must be one syllable, *Parthians* stressed on the first. The winner is copied to `shots/P1_013.mp4` and becomes the rule for every rare name; if both pass, **B wins** — simpler, and it does not depend on Kling reading an instruction."); w()
    else:
        w('```'); w(talk_prompt(r)); w('```'); w()
    w(f"**Subtitle:** {r.get('spoken') or r['line']}")
    w(f"**provenance:** {r['prov']}")
    if r.get('place'): w(f"**edit_placement:** {refs(r['place'])}")
    if r.get('test'): w(f"**test:** `{r['test']}` (see §4b)")
    w("**SFX:** studio room tone only.")
    w(scr_line(r))
    if r.get('twoup'): w(f"**twoup:** #{r['twoup']}")
    if r.get('notes'): w(); w(refs(r['notes']))
    w()

# ------------------------------------------------------------------ totals
talks = [r for r in R if r['kind'] == 'talk']; reacts = [r for r in R if r['kind'] == 'react']; brolls = [r for r in R if r['kind'] == 'broll']
offmic = [r for r in talks if 'audio only, under' in (r.get('place') or '')]
t_s = sum(r['dur'] for r in talks); r_s = sum(r['dur'] for r in reacts); b_s = sum(r['dur'] for r in brolls)
t_c = sum(r['cr'] for r in talks); r_c = sum(r['cr'] for r in reacts); b_c = sum(r['dur'] for r in brolls) * 10
total = t_c + r_c + b_c + 3 * len(brolls) + 43
chains = [r for r in R if r['kind'] in ('talk', 'react') and chained(r)]

def share_table():
    tot = {'G': 0.0, 'H': 0.0, '2UP': 0.0, 'BROLL': 0.0}
    for r in R:
        if r['kind'] in ('talk', 'react', 'broll'):
            for k_, v_ in screen(r).items(): tot[k_] += v_
    st = tot['G'] + tot['H'] + tot['2UP']
    mm = lambda x: f'{int(x // 60)}:{int(round(x % 60)):02d}'
    n2 = sum(1 for r in R if r.get('twoup'))
    return '\n'.join(['| | on screen | share of studio picture |', '|---|---|---|',
        f"| **Guest, full frame** | {mm(tot['G'])} | {tot['G'] / st:.0%} |",
        f"| **Two-up** ({n2}; counts as hers) | {mm(tot['2UP'])} | {tot['2UP'] / st:.0%} |",
        f"| **Host, full frame** | {mm(tot['H'])} | {tot['H'] / st:.0%} |",
        f"| B-roll (not in the share) | {mm(tot['BROLL'])} | — |",
        '', f"**Guest share: {(tot['G'] + tot['2UP']) / st:.0%}** (target ≥ 65%). Speech-model seconds — the cut trims lead-ins and pauses, so the edit lands a little shorter but in the same proportion."])
FRONT = open(os.path.join(ROOT, 'Episodes', 'Cleopatra', '_kit_source', 'p1_front.md'), encoding='utf-8').read()
BACK = open(os.path.join(ROOT, 'Episodes', 'Cleopatra', '_kit_source', 'p1_back.md'), encoding='utf-8').read()
def fill(s):
    s = refs(s)
    rep = {
      '{{TALK_N}}': str(len(talks)), '{{TALK_S}}': str(t_s), '{{TALK_MS}}': f'{t_s // 60}m {t_s % 60:02d}s', '{{TALK_CR}}': f'{t_c:,}',
      '{{REACT_N}}': str(len(reacts)), '{{REACT_S}}': str(r_s), '{{REACT_CR}}': f'{r_c:,}',
      '{{BROLL_N}}': str(len(brolls)), '{{BROLL_S}}': str(b_s), '{{BROLL_CR}}': f'{b_c:,}', '{{STILLS_CR}}': str(3 * len(brolls)),
      '{{GEN_N}}': str(len(talks) + len(reacts) + len(brolls) + 1), '{{GEN_S}}': str(t_s + r_s + b_s + 5),
      '{{TOTAL_CR}}': f'{total:,}', '{{RETRY_CR}}': f'{round(t_c / 6, -1):,.0f}', '{{PLAN_CR}}': f'{total + round(t_c / 6, -1):,.0f}',
      '{{OFFMIC_N}}': str(len(offmic)), '{{OFFMIC_S}}': str(sum(r['dur'] for r in offmic)),
      '{{VOICE_N}}': str(len(talks)),
      '{{SHARE_TABLE}}': share_table(),
      '{{PROV_D}}': str(sum(1 for r in talks if r['prov'].startswith('`[D]`'))),
      '{{PROV_I}}': str(sum(1 for r in talks if r['prov'].startswith('`[I]`'))),
      '{{PROV_V}}': str(sum(1 for r in talks if r['prov'].startswith('`[V]`'))),
      '{{TEST_CR}}': f"{sum(r['cr'] for r in R if r.get('test')):,}",
      '{{TEST_IDS}}': ', '.join(f"`{r['id']}`" for r in R if r.get('test')),
      '{{GUEST_ON}}': f"{19.17 + next(r for r in R if r.get('k')=='N1a')['dur'] + next(r for r in R if r.get('k')=='N1b')['dur'] - 0.3 + 2.0:.0f}",
      '{{T3_CONTROL}}': talk_prompt(dict(who='GUEST', reg="The woman speaks quietly and seriously, steady and unhurried; the last sentence is low and firm.",
            note='quieter, then personal, the ceiling holding',
            line="In my family, the danger to a queen sat at her own table. Rome had already used her against me once. I would not leave it a second chance.",
            start=('chain', 'C12'), gest=('still', ''))),
      '{{T3_CONTROL_DUR}}': str(syl.dur2("In my family, the danger to a queen sat at her own table. Rome had already used her against me once. I would not leave it a second chance.", chained=True)[2]),
      '{{HOST_POSES}}': ', '.join(f'`{p}`' for p in sorted({pose_of[r['k']] for r in R if r['kind'] in ('talk','react') and r['who']=='HOST'})),
      '{{GUEST_POSES}}': ', '.join(f'`{p}`' for p in sorted({pose_of[r['k']] for r in R if r['kind'] in ('talk','react') and r['who']=='GUEST'})),
    }
    for a, b in rep.items(): s = s.replace(a, b)
    # chain table
    rows_ = []
    for r in chains:
        st = r['start']; src = next(x for x in R if x.get('k') == st[1])
        stype = src['typ'] if src['kind'] == 'talk' else 'REACTION'
        if st[0] == 'chaincut': frm = f"`{ids[st[1]]}` **at the cut word** *\"{st[2]}\"*" + (f" — **{st[3]:.2f} s**" if len(st) > 3 else '')
        else: frm = f"`{ids[st[1]]}`"
        rows_.append(f"| `{r['id']}` | {frm} | {stype} | `shots/start_frames/{r['id']}_start.png` |")
    s = s.replace('{{CHAIN_TABLE}}', '\n'.join(rows_))
    srcs = sorted({ids[r['start'][1]] for r in chains})
    s = s.replace('{{CHAIN_SOURCES}}', ', '.join(f'`{x}`' for x in srcs))
    s = s.replace('{{CHAINED}}', ', '.join(f'`{r["id"]}`' for r in chains))
    return s

w(fill(FRONT).rstrip()); w()
w('## Shot list'); w()
w('### Opening'); w()
for r in R: emit_row(r)
w(fill(BACK).rstrip()); w()
path = os.path.join(ROOT, 'Episodes', 'Cleopatra', 'P1_kit.md')
open(path, 'w', encoding='utf-8').write('\n'.join(out))

# ------------------------------------------------------------------ report
print(f'wrote {path}')
print(f'talking {len(talks)} clips {t_s}s {t_c} cr | reactions {len(reacts)} {r_s}s {r_c} cr | broll {len(brolls)} {b_s}s | total ~{total} cr')
print(f'on-picture spine ≈ {t_s - sum(r["dur"] for r in offmic)} s generated talking; chained rows {len(chains)}')
for r in R:
    if r['kind'] == 'talk':
        flag = ' <-- over 12s' if r['dur'] > 12 else ''
        flag += ' <-- CAP' if r['need'] > 15 else ''
        print(f"  {r['id']} {r['k']:5s} {r['who'][0]} {r['typ'][:5]} {r['dur']:>2}s need {r['need']:>4} {str(r['start'])[:32]:32s}{' AUTO' if r.get('auto_pose') else ''}{flag}")
    elif r['kind'] == 'react':
        print(f"  {r['id']} {r['k']:5s} {r['who'][0]} REACT {r['dur']:>2}s          {str(r['start'])[:32]:32s}{' AUTO' if r.get('auto_pose') else ''}")
    elif r.get('id'):
        print(f"  {r['id']} {r['k']:5s} {r['kind']}")
run = 0
for r in R:
    if r['kind'] == 'talk' and r['typ'] == 'INTERVIEW': run += 1
    elif r['kind'] in ('talk', 'react', 'broll', 'actbreak'): run = 0
    if run > 3: print('  FLAG: >3 consecutive INTERVIEW rows ending', r['id'])
