"""Batch check — one line per clip: sound, timing, loudness, camera, far corner. Mode 6 runs it once over Shots/.

  python3 Fixed_Assets/tools/batch_check.py Episodes/<Guest> [P1_007,P1_011,…] [--tests]
  (no ids = every clip in Shots/; --tests = look in Shots/_tests instead)

Flags (LESSONS): NO-AUDIO on a talking row; QUIET (mean < -45 dB, L22); LOUD-SPAN (a 3 s span > 6 LU above the take's own loudness); TIGHT (last word < 0.25 s from the end,
L21); PAUSE > 2.0 s (edit trim, L13); LEAD > 1.5 s (edit trim); camera MOVED / corner (cam_check, L18/L19).
Nothing is moved: Claude files keepers after reading this, and looks at frames only where a flag says to.
"""
import os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
argv = [a for a in sys.argv[1:] if a != '--tests']
G = argv[0]; T = os.path.join(G, 'Shots', '_tests') if '--tests' in sys.argv else os.path.join(G, 'Shots')
kit = ''.join(open(os.path.join(G, k)).read() for k in os.listdir(G) if re.match(r'P\d_kit\.md$', k))
ids = argv[1].split(',') if len(argv) > 1 else sorted(f[:-4] for f in os.listdir(T) if re.match(r'P\d_\d{3}[a-z]?\.mp4$', f))
def sh(a): return subprocess.run(a, capture_output=True, text=True)
for i in ids:
    f = os.path.join(T, i + '.mp4')
    if not os.path.exists(f): print(f'{i}  missing'); continue
    m = re.search(r'\*\*' + i + r'\*\* · (\w+)(?: · (HOST|GUEST))? · \*\*(\d+)s\*\*([^\n]*)\n`start_frame` `([^`]+)`', kit)
    typ, who, kd, hdr, st = m.groups() if m else ('?', '', '?', '', '')
    audio_only = 'picture never used' in hdr   # 720p audio-only: camera, lead and pose do not matter
    dur = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).stdout or 0)
    has_a = 'audio' in sh(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-of', 'csv=p=0', f]).stdout
    flags = []; info = f'{dur:4.1f}s (kit {kd}s)'
    talking = typ in ('INTERVIEW', 'INTERJECTION', 'NARRATION')
    if talking and not has_a: flags.append('NO-AUDIO')
    if has_a and talking:
        v = sh(['ffmpeg', '-v', 'info', '-i', f, '-af', 'volumedetect', '-f', 'null', '-']).stderr
        mean = float(re.search(r'mean_volume: ([-\d.]+)', v).group(1))
        s = sh(['ffmpeg', '-v', 'info', '-i', f, '-af', 'silencedetect=n=-40dB:d=0.25', '-f', 'null', '-']).stderr
        ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', s)]; se = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', s)]
        lead = se[0] if ss and ss[0] < 0.05 and se else 0.0
        end_sp = ss[-1] if ss and ss[-1] > lead + 0.1 and (len(se) < len(ss) or se[-1] >= dur - 0.05) else dur
        tail = dur - end_sp
        inner = [e - s_ for s_, e in zip(ss, se) if s_ > lead + 0.05 and e < end_sp - 0.05]
        info += f'  lead {lead:.1f}  tail {tail:.2f}  longest pause {max(inner) if inner else 0:.1f}  {mean:.0f} dB'
        if mean < -45: flags.append('QUIET')
        # LOUD-SPAN (2026-09-28, Salah): a sentence Kling pushed well above the take's own level — known before the mix
        eb = sh(['ffmpeg', '-v', 'info', '-i', f, '-af', 'ebur128', '-f', 'null', '-']).stderr
        st = [float(x) for x in re.findall(r' S:\s*(-?[\d.]+)', eb) if float(x) > -60]
        I_ = re.findall(r'I:\s*(-?[\d.]+) LUFS', eb)
        if st and I_ and max(st) - float(I_[-1]) > 6: flags.append(f'LOUD-SPAN +{max(st) - float(I_[-1]):.0f}LU')
        if tail < 0.25: flags.append('TIGHT')
        if inner and max(inner) > 2.0: flags.append('PAUSE>2s')
        if lead > 1.5 and not audio_only: flags.append('LEAD>1.5s')
    if audio_only:
        print(f'{i}  {typ[:5]:5s} {who[:1]}  {info}  audio-only (picture unused)  ' + ('✓' if not flags else '⚠ ' + ' '.join(flags))); continue
    side = 'H' if 'host' in st or (who == 'HOST' and 'chain' in st) else 'G'
    c = sh(['python3', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cam_check.py'), f + ':' + side]).stdout.strip()
    dpx = int(re.search(r'drift (\d+) px', c).group(1)) if re.search(r'drift (\d+) px', c) else 0
    if 'MOVED' in c: flags.append('SMALL-DRIFT (stabilise in edit?)' if dpx <= 8 else 'CAMERA-MOVED')   # L31
    if 'ENTERS' in c: flags.append('CORNER')
    drift = re.search(r'drift (\d+) px', c)
    print(f'{i}  {typ[:5]:5s} {who[:1]}  {info}  cam {drift.group(1) if drift else "?"}px  ' + ('✓' if not flags else '⚠ ' + ' '.join(flags)))
