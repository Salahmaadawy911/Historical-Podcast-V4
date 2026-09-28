#!/usr/bin/env python3
"""Mode 6 assembly prep, Part 1: (1) every voice-passed MP3 -> head-trimmed (1152 samples), -19 LUFS WAV
(Mode 6 Audio rule 1-2); (2) word timings for every talking clip by forced alignment (pocketsphinx) of the
prompt's spoken words against the Kling take -> _edit/words_p1.json. Times are source seconds in Shots/<id>.mp4."""
import os, re, json, subprocess, sys
from concurrent.futures import ProcessPoolExecutor
EP = 'Episodes/Cleopatra'; ED = os.path.join(EP, '_edit')
kit = open(os.path.join(EP, 'P1_kit.md')).read()
body = kit[kit.index('## Shot list'):kit.index('## 6 · Assembly')]
rows = {}
for p in re.split(r'\n(?=\*\*P1_\d+\w?\*\* · )', body):
    m = re.match(r'\*\*(P1_\d+\w?)\*\* · (\w+)', p)
    if not m: continue
    spoken = ' '.join(re.findall(r'\): "([^"]+)"', p))
    rows[m.group(1)] = dict(type=m.group(2), spoken=spoken)

def prep_audio(i):
    src = os.path.join(EP, 'Voice/P1/done', i + '.mp3'); out = os.path.join(ED, 'audio', i + '.wav')
    if not os.path.exists(out):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-af',
            'atrim=start_sample=1152,asetpts=PTS-STARTPTS,loudnorm=I=-19:TP=-1.5:LRA=7', '-ar', '44100', '-c:a', 'pcm_s16le', out], check=True)
    return out

# the prompts' respellings (Mode 3 Pronunciation `write:`) and names cmudict lacks — phones without stress marks
EXTRA = {l.split()[0]: ' '.join(re.sub(r'\d', '', x) for x in l.split()[1:])
         for l in open('Fixed_Assets/tools/names.dict') if l.strip() and not l.startswith('#')}
EXTRA.update({'seezer': 'S IY Z ER', "seezer's": 'S IY Z ER Z', 'pompee': 'P AA M P IY', "pompee's": 'P AA M P IY Z',
    'antonee': 'AE N T AH N IY', "antonee's": 'AE N T AH N IY Z', 'tolemies': 'T AA L AH M IY Z',
    'arsinowee': 'AA R S IH N OW IY', 'meeds': 'M IY D Z', 'syprus': 'S AY P R AH S', 'eyeds': 'AY D Z',
    'seductress': 'S IH D AH K T R AH S', 'suppliant': 'S AH P L IY AH N T', 'thrones': 'TH R OW N Z',
    'cassius': 'K AE SH AH S', 'artemis': 'AA R T AH M IH S', 'parthians': 'P AA R TH IY AH N Z'})

def words_of(text):
    return [w for w in re.sub(r"[^a-z' ]", ' ', text.lower().replace('—', ' ').replace('-', ' ')).split() if w.strip("'")]

def align(i):
    from pocketsphinx import Decoder
    mp4 = os.path.join(EP, 'Shots', i + '.mp4')
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    d = Decoder(samprate=16000, bestpath=False, loglevel='FATAL')
    for w, ph in EXTRA.items():
        if d.lookup_word(w) is None: d.add_word(w, ph, False)
    ws = [w.strip("'") for w in words_of(rows[i]['spoken'])]; unaligned = []
    known = [w for w in ws if d.lookup_word(w) is not None]
    d.set_align_text(' '.join(known))
    d.start_utt(); d.process_raw(pcm, full_utt=True); d.end_utt()
    try:
        d.set_alignment(); d.start_utt(); d.process_raw(pcm, full_utt=True); d.end_utt()
        al = [(w.name, w.start, w.start + w.duration) for w in d.get_alignment()]
    except RuntimeError:   # the sub-word pass can fail; the first pass's word segmentation is enough for cut points
        al = [(s.word, s.start_frame, s.end_frame + 1) for s in (d.seg() or [])]
        n = len(known)
        while not al and n > 3:   # a word the model cannot match (a clipped or odd last word): align the longest prefix
            n -= 1; d = Decoder(samprate=16000, bestpath=False, loglevel='FATAL')
            for w, ph in EXTRA.items():
                if d.lookup_word(w) is None: d.add_word(w, ph, False)
            d.set_align_text(' '.join(known[:n])); d.start_utt(); d.process_raw(pcm, full_utt=True); d.end_utt()
            al = [(s.word, s.start_frame, s.end_frame + 1) for s in (d.seg() or [])]
        if not al: return i, dict(words=[], oov=[], failed=True)   # no alignment — assembly falls back to silencedetect
        if n < len(known): al = [a for a in al if a[0] != '<sil>' or a[1] < al[-1][1]]; unaligned = known[n:]
    al = [(re.sub(r'\(\d+\)$', '', w), round(a / 100, 2), round(b / 100, 2)) for w, a, b in al if w not in ('<s>', '</s>', '[NOISE]')]
    return i, dict(words=[a for a in al if a[0] != '<sil>'], oov=[w for w in ws if w not in known], unaligned=unaligned)

if __name__ == '__main__':
    talk = [i for i, r in rows.items() if r['type'] in ('INTERVIEW', 'INTERJECTION', 'NARRATION')]
    missing = [i for i in talk if not os.path.exists(os.path.join(EP, 'Voice/P1/done', i + '.mp3'))]
    if missing: sys.exit('no voice-passed audio: ' + ', '.join(missing))
    with ProcessPoolExecutor() as ex:
        list(ex.map(prep_audio, talk))
        res = dict(ex.map(align, talk))
    json.dump(res, open(os.path.join(ED, 'words_p1.json'), 'w'), indent=0)
    print(f'{len(talk)} talking clips: audio prepared, words aligned -> {ED}/words_p1.json')
    for i, r in res.items():
        if r.get('failed'): print(f'  {i} ALIGNMENT FAILED — speech in/out from silencedetect only')
        if r.get('unaligned'): print(f'  {i} last words not matched (clipped or odd — listen): {" ".join(r["unaligned"])}')
        if r['oov']: print(f'  {i} not in the dictionary (timed by its neighbours): {" ".join(r["oov"])}')
