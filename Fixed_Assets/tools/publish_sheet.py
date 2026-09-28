#!/usr/bin/env python3
"""YouTube publish sheet — one copy-paste file per part, in YouTube Studio's field order.

Usage:
  python3 Fixed_Assets/tools/publish_sheet.py Episodes/<Guest> [--part N]            # build P<n>_PUBLISH.md
  python3 Fixed_Assets/tools/publish_sheet.py Episodes/<Guest> [--part N] --words-only  # Mode 4: check §9 only

Reads (nothing is typed twice):
  P<n>_kit.md §9   the words: titles, description hook, summary, heard-vs-record, tags, hashtags,
                   pinned comment, playlists, end screen, series index           (Mode 4 writes)
  P<n>_kit.md §11  chapter titles + the shot each starts at                      (Mode 4 writes)
  P<n>_kit.md §8   the full AI-disclosure statement                               (fixed wording)
  card_data_p<n>.json   the source list and the next-part line (already audited by sources_audit.py)
  P<n>_TIMECODES.txt    one line per chapter shot: `P1_008 1:12`, plus `end 11:48`  (Mode 6 writes)
  Fixed_Assets/publish_defaults.json   channel-level settings (playlist URL, category, language…)

Writes Episodes/<Guest>/P<n>_PUBLISH.md. Prints every check; exits 1 if anything blocks publishing
(the sheet is still written, headed NOT READY, with the blockers listed at the top).
"""
import re, sys, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LABELS = ['Titles', 'Description hook', 'Summary', 'Heard vs the record', 'Tags', 'Hashtags',
          'Pinned comment', 'Playlists', 'End screen', 'Series index']
ID = r'P\d+_\d+[a-z]?'

def section(kit, num):
    m = re.search(r'^## %d ·.*?$(.*?)(?=^## \d+ ·|\Z)' % num, kit, re.M | re.S)
    return m.group(1) if m else ''

def blocks(sec):
    """Bold-label blocks. A block runs until the next bold line, heading, or ⚠️ note."""
    out, cur = {}, None
    for ln in sec.split('\n'):
        m = re.match(r'^\*\*([^*]+?)\*\*[.:]?\s*(.*)$', ln)
        if m or ln.startswith('#') or ln.startswith('⚠️'):
            cur = None
            if m:
                name = m.group(1).strip().rstrip('.:')
                hit = next((L for L in LABELS if name.lower().startswith(L.lower())), None)
                if hit:
                    cur = hit; out[cur] = [m.group(2)]
            continue
        if cur: out[cur].append(ln)
    return {k: '\n'.join(v).strip() for k, v in out.items()}

def items(txt):
    return [re.sub(r'^\s*(?:\d+[.)]|[-*•])\s+', '', l).strip() for l in txt.split('\n')
            if re.match(r'^\s*(?:\d+[.)]|[-*•])\s+', l)]

def norm(s):
    s = s.lower().replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', re.sub(r"[^a-z0-9' ]", ' ', s)).strip()

def secs(tc):
    p = [int(x) for x in tc.split(':')]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]

def main():
    a = sys.argv[1:]
    words_only = '--words-only' in a
    part = int(a[a.index('--part') + 1]) if '--part' in a else 1
    ep = [x for x in a if not x.startswith('--') and not x.isdigit()][0].rstrip('/')
    guest = os.path.basename(ep)
    P = 'P%d' % part
    kit_path = os.path.join(ep, '%s_kit.md' % P)
    kit = open(kit_path, encoding='utf-8').read()
    err, warn = [], []

    # ---------- the words (§9) ----------
    b = blocks(section(kit, 9))
    print('§9 labels found: %s' % (', '.join(b) or 'NONE'))
    for L in LABELS:
        if L not in b or not b[L]: err.append('§9 is missing **%s**' % L)
    titles = items(b.get('Titles', ''))
    index = re.sub(r'[`\[\]]', '', b.get('Series index', '')).strip()      # "Part 1 of 2"
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import outline_lines as O
    spoken = norm(' '.join(O.kit_spoken(kit)))   # every beat-map segment counts for the quote check
    print('titles: %d · spoken text scanned: %d words' % (len(titles), len(spoken.split())))
    if not spoken: err.append('no spoken lines found in the kit — quote check could not run')
    if len(titles) != 3:
        err.append('need exactly 3 titles (the primary + 2 for Test & Compare), found %d' % len(titles))
    for i, t in enumerate(titles, 1):
        if len(t) > 100: err.append('title %d is %d chars — YouTube max is 100' % (i, len(t)))
        elif len(t) > 70: warn.append('title %d is %d chars — cut off on phones past ~70' % (i, len(t)))
        if '<' in t or '>' in t: err.append('title %d contains < or > — YouTube rejects them' % i)
        if index and index.lower() not in t.lower(): err.append('title %d lacks the series index "%s"' % (i, index))
        for q in re.findall(r'["“](.+?)["”]', t):
            if norm(q) not in spoken:
                err.append('title %d quotes "%s" — not in any spoken line. A quote must be verbatim.' % (i, q))
    if titles and guest.lower() not in titles[0].lower():
        warn.append('primary title does not name %s — the name is the search term' % guest)
    hook = b.get('Description hook', '')
    if hook and guest.lower() not in hook[:150].lower():
        err.append('description hook does not name %s in its first 150 chars (the part shown above "more")' % guest)
    nw = len(b.get('Summary', '').split())
    if b.get('Summary') and not 150 <= nw <= 350: warn.append('summary is %d words — aim for 200–300' % nw)
    heard = items(b.get('Heard vs the record', ''))
    if 'Heard vs the record' in b and not 1 <= len(heard) <= 4:
        warn.append('heard-vs-record has %d items — 1 to 3 is the useful range' % len(heard))
    for h in heard:
        for sid in re.findall(ID, h):
            if not re.search(r'^\*\*%s\*\* ·' % sid, kit, re.M): err.append('heard-vs-record cites %s — no such shot' % sid)
    tags = [t.strip() for t in b.get('Tags', '').replace('\n', ',').split(',') if t.strip()]
    tag_chars = sum(len(t) + (2 if ' ' in t else 0) for t in tags) + max(len(tags) - 1, 0)
    if tags and not 10 <= len(tags) <= 15: warn.append('%d tags — aim for 10–15' % len(tags))
    if tag_chars > 500: err.append('tags total %d chars — YouTube max is 500' % tag_chars)
    tags_line = ', '.join(tags)
    tags_bad = [t for t in tags if '<' in t or '>' in t]
    if tags_bad: err.append('tags contain < or >: %s' % tags_bad)
    hashtags = re.findall(r'#\S+', b.get('Hashtags', ''))
    if b.get('Hashtags') and len(hashtags) != 3:
        err.append('%d hashtags — use exactly 3 (YouTube shows the first 3 above the title)' % len(hashtags))
    if words_only:
        report(err, warn); sys.exit(1 if err else 0)

    # ---------- the assembly ----------
    defaults = json.load(open(os.path.join(ROOT, 'Fixed_Assets', 'publish_defaults.json'), encoding='utf-8'))
    for k, v in defaults.items():
        if isinstance(v, str) and 'TODO' in v: err.append('publish_defaults.json: %s is still TODO' % k)
    card_path = os.path.join(ep, 'card_data_p%d.json' % part)
    card = json.load(open(card_path, encoding='utf-8')) if os.path.exists(card_path) else {}
    sources = card.get('sources', [])
    if not sources: err.append('no sources — card_data_p%d.json missing or empty' % part)
    m = re.search(r'full statement.*?\n\s*\n((?:>.*\n?)+)', section(kit, 8), re.S)
    disclosure = ' '.join(l.lstrip('> ').strip() for l in m.group(1).split('\n') if l.strip()) if m else ''
    if not disclosure: err.append('§8 full AI-disclosure statement not found')

    chapters = []
    for row in re.findall(r'^\|(.+)\|$', section(kit, 11), re.M):
        cells = [c.strip() for c in row.split('|')]
        if len(cells) < 2 or set(cells[0]) <= set('-: ') or cells[0].lower() == 'chapter': continue
        sid = re.search(ID, cells[1]); z = '0:00' in cells[1]
        if sid or z: chapters.append([cells[0], '0:00' if z else sid.group(0)])
    if len(chapters) < 3: err.append('%d chapters in §11 — YouTube needs at least 3' % len(chapters))
    if chapters and chapters[0][1] != '0:00': err.append('first chapter must start at 0:00')
    tc_path = os.path.join(ep, '%s_TIMECODES.txt' % P)
    tc = {}
    if os.path.exists(tc_path):
        for ln in open(tc_path, encoding='utf-8'):
            p = ln.split('#')[0].split()
            if len(p) >= 2: tc[p[0]] = p[1]
    else: err.append('%s_TIMECODES.txt not written yet — Mode 6 fills it from the cut' % P)
    times = []
    for ch in chapters:
        t = ch[1] if ch[1] == '0:00' else tc.get(ch[1])
        if t is None:
            if tc: err.append('no timecode for %s (chapter "%s")' % (ch[1], ch[0]))
            t = '[m:ss]'
        ch.append(t)
        if t != '[m:ss]': times.append(secs(t))
    if len(times) == len(chapters) and times:
        ends = times[1:] + ([secs(tc['end'])] if 'end' in tc else [])
        for i, e in enumerate(ends):
            if e - times[i] < 10: err.append('chapter "%s" is %ds — YouTube needs ≥10 s' % (chapters[i][0], e - times[i]))
        if 'end' not in tc: warn.append('no `end m:ss` line — last chapter length unchecked')

    nxt = card.get('next', '')
    nx = [x.strip() for x in nxt.split('·')] if nxt else []
    nx = [x.title() if x.isupper() else x for x in nx]
    series = '%s. Next — %s' % (index or P, ': '.join(nx)) if nx else (index or P)
    series += '\nThe whole series, in order: %s' % defaults.get('series_playlist_url', '')
    desc = [hook, '', b.get('Summary', '')]
    if heard: desc += ['', 'WHAT YOU MAY HAVE HEARD — AND WHAT THE RECORD SAYS'] + \
        ['• ' + re.sub(r'\s*\(`?%s`?\)' % ID, '', h) for h in heard]
    desc += ['', 'CHAPTERS'] + ['%s %s' % (c[2], c[0]) for c in chapters]
    desc += ['', 'SOURCES'] + sources + ['', 'ABOUT THIS PROGRAMME', disclosure, '', series, '', ' '.join(hashtags)]
    desc = '\n'.join(desc)
    desc = re.sub(r'[*`]', '', desc)
    if len(desc) > 5000: err.append('description is %d chars — YouTube max is 5000' % len(desc))
    if '<' in desc or '>' in desc: err.append('description contains < or > — YouTube rejects them')
    thumb = 'THUMB_%s_p%d.png' % (guest.lower(), part)
    if not os.path.exists(os.path.join(ep, thumb)): err.append('%s not found' % thumb)
    srt = '%s_captions.srt' % P
    if not os.path.exists(os.path.join(ep, srt)): warn.append('%s not found — upload captions or YouTube auto-captions the names wrong' % srt)

    status = 'READY' if not err else 'NOT READY — %d blocker(s)' % len(err)
    F = lambda s: '```\n%s\n```' % s
    out = ['# %s %s — publish sheet' % (guest, P), '',
           '> Generated by `publish_sheet.py` — **do not edit here.** Change the kit (§8, §9, §11), `card_data_p%d.json`,' % part,
           '> `%s_TIMECODES.txt` or `publish_defaults.json`, then re-run.' % P, '',
           '**Status: %s**' % status, '']
    out += ['- ⛔ ' + e for e in err] + ['- ⚠️ ' + w for w in warn] + ['']
    out += ['## 1 · Details', '', '**Title** (%d chars)' % len(titles[0] if titles else ''), F(titles[0] if titles else ''), '',
            '**Description** (%d chars — the first ~150 show above "more")' % len(desc), F(desc), '',
            '**Thumbnail** — upload `%s`' % thumb, '',
            '**Playlists** — %s' % b.get('Playlists', ''), '',
            '**Audience** — No, it is not made for kids', '',
            '## 2 · Show more', '',
            '- **Altered or synthetic content → Yes.** Realistic synthetic people and voices. Required, every part.',
            '- **Paid promotion** → No (unless this part carries one)',
            '- **Automatic chapters** → off (ours are in the description)',
            '- **Tags** (%d, %d/500 chars):' % (len(tags), tag_chars), F(tags_line),
            '- **Language / caption certification** → %s / None' % defaults.get('language', ''),
            '- **Recording date** → leave blank',
            '- **License** → Standard YouTube License · **Allow embedding** on',
            '- **Category** → %s' % defaults.get('category', ''),
            '- **Comments** → On', '',
            '## 3 · Video elements', '',
            '- **Subtitles** → upload `%s` (%s)' % (srt, defaults.get('language', '')),
            '- **End screen** → %s' % b.get('End screen', ''),
            '- **Cards** → none by default', '',
            '## 4 · Test & compare (titles)', '',
            'Add all three. YouTube picks the winner on watch time, not clicks.', '']
    out += ['%d. %s' % (i, F(t)) for i, t in enumerate(titles, 1)]
    out += ['', '## 5 · After it is live', '', '**Pinned comment** — post from the channel account, then pin:',
            F(b.get('Pinned comment', '')), '',
            '**Schedule** — see the release plan in `NEXT_STEPS.md`.', '']
    open(os.path.join(ep, '%s_PUBLISH.md' % P), 'w', encoding='utf-8').write('\n'.join(out))
    print('wrote %s_PUBLISH.md · description %d chars · %d chapters' % (P, len(desc), len(chapters)))
    report(err, warn); sys.exit(1 if err else 0)

def report(err, warn):
    for w in warn: print('WARN  ' + w)
    for e in err: print('FAIL  ' + e)
    print('publish sheet: ' + ('READY' if not err else 'NOT READY (%d)' % len(err)))

if __name__ == '__main__':
    main()
