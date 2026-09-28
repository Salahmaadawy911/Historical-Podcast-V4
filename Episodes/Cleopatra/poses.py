"""Cleopatra pose table — how each seed frame is written into a prompt. Fields and rules:
Fixed_Assets/tools/poses.py. Descriptions from CAST.md (Pose Register)."""
GUEST = {
 'frame_cleopatra': dict(
    rank=3, use='listening; straightforward answers with no particular weight',
    avoid=['armrest'],
    desc='upright and composed, back against the chair, hands resting in her lap',
    hold='She stays upright, back against the chair, hands resting together in her lap.',
    settle='On "{w}" one hand turns slightly open in her lap and rests there.',
    advance='On "{w}" her chin lifts a fraction.',
    still='She stays upright, hands resting together in her lap, her gaze on him.'),
 'frame_cleopatra_b': dict(
    rank=5, use='following a line of questioning closely; attentive listening',
    avoid=['armrest'],
    desc='upright, hands folded to one side of her lap, torso turned a little further toward the left of the frame',
    hold='She stays upright and turned a little toward the left of the frame, hands folded to one side of her lap.',
    settle='On "{w}" her folded hands loosen slightly and rest.',
    advance='On "{w}" she turns a fraction further toward the left of the frame, where the person opposite her sits.',
    still='She stays upright and turned a little toward the left of the frame, hands folded, her gaze on him.'),
 'frame_cleopatra_c': dict(
    rank=9, use='explains a distinction; her most engaged answers',
    desc='one forearm along the armrest nearer the camera, the other hand open and slightly raised in her lap',
    hold='Her forearm stays along the armrest and her other hand rests open in her lap.',
    settle='On "{w}" the open hand in her lap turns a little further open and rests.',
    advance='On "{w}" the open hand in her lap turns a little toward the left of the frame and stays there.',
    still='Her forearm stays along the armrest and her open hand rests in her lap; her gaze stays on him.'),
 'frame_cleopatra_e': dict(
    rank=2, use='declines a premise; a short answer; withholding',
    avoid=['armrest'],
    desc='settled back, hands loosely clasped in her lap, chin a fraction higher',
    hold='She stays settled back, hands loosely clasped in her lap, chin a fraction high.',
    settle='On "{w}" she settles a little further back into the chair, hands staying clasped.',
    advance='On "{w}" her chin lifts a fraction higher.',
    still='She stays settled back, hands loosely clasped in her lap, chin a fraction high, her gaze on him.'),
}


# ---- Part 2 additions (2026-09-27, L47) — Seedream edits of frame_cleopatra_b, colour-matched, frame-set check PASS
# (_i: FURNITURE flag is her two arms covering both armrests — chair back unchanged, checked by eye). Written from the images.
GUEST.update({
 'frame_cleopatra_f': dict(rank=1, use='sitting back, guarded; a loss stated plainly; holding something back',
    avoid=['armrest'],
    desc='sitting back, legs crossed, hands resting one over the other on her upper knee, shoulders relaxed',
    hold='She stays sitting back, legs crossed, hands resting one over the other on her knee.',
    settle='On "{w}" her upper hand settles flatter over the other on her knee and rests.',
    advance='On "{w}" her chin lifts a fraction.',
    still='She stays sitting back, hands resting on her knee, her gaze on him.'),
 'frame_cleopatra_g': dict(rank=4, use='personal loss; grief held in (Antony); something that costs her to say',
    avoid=['armrest'],
    desc='upright, one hand resting flat just below her collarbone, the other hand in her lap',
    hold='She stays upright, one hand resting flat below her collarbone, the other in her lap.',
    settle='On "{w}" the hand below her collarbone presses a little flatter and rests there.',
    advance='On "{w}" her chin lowers a fraction and stays there.',
    still='She stays upright, one hand below her collarbone, her gaze on him.'),
 'frame_cleopatra_h': dict(rank=6, only='react', use='weighing a hard question in silence',
    desc='elbow on the armrest nearer the camera, fingertips resting at her temple, the other hand in her lap',
    hold='She stays with her elbow on the near armrest, fingertips resting at her temple, other hand in her lap.',
    entry='She lowers the hand from her temple and rests her forearm along the armrest, where it stays.',
    settle='On "{w}" her fingertips settle against her temple and rest.',
    advance='On "{w}" her gaze sharpens on him and holds.',
    still='She stays with her fingertips at her temple, her gaze on him.'),
 'frame_cleopatra_i': dict(rank=8, use='statements of authority (took over from the retired _d); confrontation; refusing Octavian; controlled defiance',
    avoid=['in her lap'],
    desc='shoulders square and turned a little toward the left of the frame, both arms out along the armrests, hands over the ends',
    hold='She stays square in the chair, turned a little toward the left of the frame, both arms along the armrests.',
    settle='On "{w}" the fingers of her near hand spread over the end of the armrest and rest.',
    advance='On "{w}" she turns a fraction further toward the left of the frame, where the person opposite her sits, and holds.',
    still='She stays square, arms along the armrests, her gaze on him.'),
})

# frame_cleopatra_d RETIRED 2026-09-28 (Salah: a mistake in the pose) — replaced everywhere by frame_cleopatra_i (same pose).
