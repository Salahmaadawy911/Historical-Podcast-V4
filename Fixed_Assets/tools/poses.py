"""Pose prompt table — how every seed frame is written into a Kling prompt.

One entry per seed frame. The builder reads this; `pose_check.py` gates the kit against it.
Host poses live here (permanent, like POSE_LIBRARY.md). Guest poses live in
Episodes/<Guest>/poses.py as GUEST = {...}, written in Mode 2 when the pose set is registered.

Every entry is written FROM THE IMAGE, not from the placement prompt that made it — two host frames
(frame_host_f, frame_host_direct) came out differently from their POSE_LIBRARY wording (found 2026-09-24).

Fields
  desc     what the frame shows (from POSE_LIBRARY.md / CAST.md)
  hold     the pose, held — inserted into every silent reaction that starts from this frame.
           Posture only, no gaze (the eyeline sentence carries that).
  entry    optional. Written directly before the first spoken words of a TALKING clip that starts from
           this frame (in the register paragraph Kling played it in the first pause — P1_084), and the
           builder adds 0.7 s for it. Required when a hand is at the face: the hand comes down as he begins and stays down
           (a jaw moving against resting knuckles is a lip-sync risk — Mode 4 §5).
  settle / advance   the one gesture a talking clip may carry, anchored on a word ("On "{w}" …").
           A ONE-WAY move into a position that then holds. Never a move that goes and comes back
           (nod, open-and-close, lift-and-settle-back): Kling loops those (P1_009, 2026-09-24).
  avoid    words that must not appear in a prompt starting from this frame — body contacts this pose
           does not have (e.g. 'armrest' for a hands-in-lap pose). pose_check.py fails on them; a
           hand-written gesture that names the wrong contact is how a prompt fights its own start frame.
  still    the talking clip's pose hold when it carries no gesture. If `entry` exists, describe the
           pose AFTER the entry.
Rules are in skill_mode2_cast.md (The pose register) and skill_mode4_produce.md §5.
"""
import importlib.util, os

HOST = {
 'frame_host': dict(
    avoid=['thigh', 'lap', 'knuckles', 'chair back'],
    desc='settled back, both forearms along the armrests, hands relaxed',
    hold='He stays settled back, his forearms resting along the armrests.',
    settle='On "{w}" one hand turns slightly open on the armrest and rests there.',
    advance='On "{w}" he shifts his weight a little forward in the chair, forearms staying on the armrests.',
    still='He stays settled back, forearms along the armrests, and holds still after the last word.'),
 'frame_host_b': dict(
    avoid=['armrest', 'knuckles', 'chair back'],
    desc='leaning forward slightly, elbows on his thighs, hands loosely clasped between his knees',
    hold='He stays leaning forward, elbows on his thighs, hands loosely clasped between his knees.',
    settle='On "{w}" his clasped hands loosen a little and stay loosely together; he stays leaning in.',
    advance='On "{w}" he leans in a fraction further, hands staying clasped between his knees.',
    still='He stays leaning forward, hands clasped between his knees, and holds her gaze to the end.'),
 'frame_host_c': dict(
    avoid=['knuckles', 'chair back'],
    desc='settled well back, one ankle crossed over the opposite knee, the frame-left hand resting on that shin, the other forearm along the armrest',
    hold='He stays settled back, one ankle crossed over his knee, one hand resting on his shin.',
    settle='On "{w}" the hand on his shin loosens and rests there.',
    advance='On "{w}" he tips his head slightly toward the right of the frame, where the person opposite him sits, the hand staying on his shin.',
    still='He stays easy in the chair, ankle crossed over his knee, and holds her gaze to the end.'),
 'frame_host_d': dict(
    avoid=['chair back', 'lap'],
    desc='elbow on the frame-right armrest, knuckles resting against his jaw, other hand on his thigh',
    hold='His elbow stays on the armrest and his knuckles stay resting against his jaw; his other hand stays on his thigh.',
    entry='He lowers the hand from his jaw and rests it on the armrest, where it stays.',
    settle='On "{w}" he settles back a fraction, the lowered hand resting on the armrest.',
    advance='On "{w}" he leans in a fraction, the lowered hand staying on the armrest.',
    still='The lowered hand stays on the armrest and he holds her gaze to the end.'),
 'frame_host_e': dict(
    avoid=['armrest', 'knuckles', 'chair back', 'thigh'],
    desc='settled back, forearms off the armrests, hands loosely clasped in his lap, shoulders square',
    hold='He stays settled back, hands loosely clasped in his lap, shoulders square.',
    settle='On "{w}" his clasped hands loosen slightly and rest in his lap.',
    advance='On "{w}" he sits up a fraction, hands staying clasped in his lap.',
    still='He stays settled back, hands clasped in his lap, and holds her gaze to the end.'),
 'frame_host_f': dict(
    avoid=['knuckles', 'lap', 'chair back'],
    desc='AS GENERATED (checked on the image 2026-09-24): the frame-left arm draped over the front of the armrest, hand hanging loose; the frame-right hand on his thigh; torso open',
    hold='One arm stays draped over the front of the armrest, the hand hanging loose, and his other hand stays on his thigh.',
    settle='On "{w}" the hand hanging over the armrest turns slightly open and stays there.',
    advance='On "{w}" the hand hanging over the armrest lifts and opens outward toward the right of the frame, and stays open.',
    still='He stays easy in the chair, one arm over the front of the armrest, and holds her gaze to the end.'),
 'frame_host_h': dict(   # redone 2026-09-27 (L47): Seedream edit of frame_host, one hand changed; Salah approved by eye; written from the image
    rank=5, use='mid-explanation; his longer questions; laying out a premise',
    avoid=['knuckles', 'clasped', 'lap', 'chest'],
    desc='settled back, his frame-left hand resting over the front of the armrest, his frame-right hand open, palm up, resting by his thigh',
    hold='He stays settled back, one hand over the front of the armrest, the other open, palm up, by his thigh.',
    settle='On "{w}" his open hand turns a little further up and rests there.',
    advance='On "{w}" his open hand moves a little toward the right of the frame and stays there.',
    still='He stays settled back, one hand open by his thigh, and holds her gaze.'),
 'frame_host_i': dict(   # added 2026-09-27 (L47): Seedream edit of frame_host_b, colour-matched, frame-set PASS; written from the image
    rank=8, use='pressing a hard question; leaning in on a challenge',
    avoid=['armrest', 'clasped', 'knuckles', 'chair back'],
    desc='leaning well forward, forearms on his thighs, both hands apart and open between his knees',
    hold='He stays leaning forward, forearms on his thighs, hands apart and open between his knees.',
    settle='On "{w}" his open hands turn a little further up and stay there.',
    advance='On "{w}" he leans a fraction further toward the right of the frame, where the person opposite him sits, and holds.',
    still='He stays leaning forward, hands open between his knees, his gaze on her.'),
 'frame_host_direct': dict(
    avoid=['knuckles', 'lap', 'chair back'],
    desc='AS GENERATED (checked on the image 2026-09-24): to the lens; settled back, both hands resting on his thighs',
    hold='He stays settled back, both hands resting on his thighs.',
    settle='On "{w}" one hand turns slightly open on his thigh and rests there.',
    advance='On "{w}" he shifts his weight a little forward, hands staying on his thighs.',
    still='He stays settled back, hands on his thighs, looking into the lens.'),
 'frame_host_direct_b': dict(
    avoid=['armrest', 'knuckles', 'chair back'],
    desc='to the lens; leaning forward slightly, forearms on his thighs, hands loosely clasped',
    hold='He stays leaning forward, forearms on his thighs, hands loosely clasped.',
    settle='On "{w}" his clasped hands loosen a little and stay loosely together.',
    advance='On "{w}" he leans in a fraction toward the lens.',
    still='He stays leaning forward, forearms on his thighs and hands clasped, looking into the lens.'),
 'frame_host_direct_c': dict(
    avoid=['armrest', 'knuckles', 'chair back', 'thigh'],
    desc='to the lens; forearms off the armrests, hands loosely clasped in his lap, shoulders square',
    hold='He stays settled back, hands loosely clasped in his lap, shoulders square.',
    settle='On "{w}" his clasped hands loosen slightly and rest in his lap.',
    advance='On "{w}" he sits up a fraction, hands staying clasped in his lap.',
    still='He stays settled back, hands clasped in his lap, looking into the lens.'),
}

# held-position wording for a clip chained from another clip's last frame (pose unknown in advance)
CHAINED = {'HOST': dict(settle='On "{w}" one hand turns slightly open and rests there.',
                        advance='On "{w}" he leans in a fraction.',
                        still='He holds the position he is already in and keeps his gaze on her.',
                        hold='He holds the position he is already in.'),
           'GUEST': dict(settle='On "{w}" one hand turns slightly open and rests there.',
                         advance='On "{w}" her chin lifts a fraction.',
                         still='She holds the position she is already in, her gaze on him.',
                         hold='She holds the position she is already in.')}

REQUIRED = ('desc', 'hold', 'settle', 'advance', 'still')
REPEATABLE = r'blink|\bnods?\b|nodding|shakes? (his|her) head|then back|then lowers|briefly|(and|to|it) settles? back|close again|come back together|back where it was'

def load(guest_dir):
    """HOST + the guest's poses. Stops if the guest has no pose table or an entry is incomplete."""
    p = os.path.join(guest_dir, 'poses.py')
    if not os.path.exists(p):
        raise SystemExit(f'STOP — no pose table at {p}. Mode 2 writes it with the pose register.')
    spec = importlib.util.spec_from_file_location('guest_poses', p); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    allp = {**HOST, **m.GUEST}
    for k, v in allp.items():
        miss = [f for f in REQUIRED if not v.get(f)]
        if miss: raise SystemExit(f'STOP — pose {k} is missing {miss} in its pose table.')
    return allp
