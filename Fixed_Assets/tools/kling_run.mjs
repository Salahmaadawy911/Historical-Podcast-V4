#!/usr/bin/env node
// kling_run.mjs — generate a batch of clips from a round sheet with the Kling CLI, on Salah's Mac.
// Usage (from the project folder):
//   node Fixed_Assets/tools/kling_run.mjs Episodes/<Guest> <pass> --part <n> --ids P1_010,P1_011 [--dry]
// v2 (2026-09-27, L51/L52): reads the one-list round sheet; no chip needed; chained clips use Shots/start_frames/<ID>_start.png
// prepared by Claude (cli_wave.py). The next command is printed by cli_wave.py — copy it as is.
// Reads ROUND<pass>_prompts.md, sends each clip with the settings below, waits, downloads to
// Episodes/<Guest>/Shots/_tests/<ID>.mp4 and appends one line per clip to Shots/_tests/kling_log.tsv.
// Running it IS the approval to spend credits (Mode 4, "Generating with the Kling CLI").
// Settings are matched to Fixed_Assets/kling_caps.json (kling who_am_i, 2026-09-25).
import { execFile } from 'node:child_process';
import fs from 'node:fs'; import path from 'node:path';

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const [G, PASS] = args;
const PART = 'P' + String(opt('--part', '1')).replace(/^[Pp]/, '');
const IDS = (opt('--ids', '') || '').split(',').filter(Boolean);
const DRY = args.includes('--dry');
const CONC = Number(opt('--parallel', '2'));   // 3 at once hit Kling's rate limit (P1_027, L26)
if (!G || !PASS || (!IDS.length && !args.includes('--refetch'))) { console.log('usage: node Fixed_Assets/tools/kling_run.mjs Episodes/<Guest> <pass> --part <n> --ids P1_010,P1_011'); process.exit(1); }

const sheet = fs.readFileSync(path.join(G, `ROUND${PASS}_prompts.md`), 'utf8');
const OUT = path.join(G, 'Shots', '_tests'); fs.mkdirSync(OUT, { recursive: true });
const LOG = path.join(OUT, 'kling_log.tsv');
const KLING = process.env.KLING_BIN || 'kling';

// ---- parse the sheet (one ordered list since 2026-09-26; settings are in each header — v2 parser, 2026-09-27)
const clips = {};
const lines = sheet.split('\n');
for (let i = 0; i < lines.length; i++) {
  const L = lines[i];
  const m = L.match(/^### ((P\d)_\d{3}[a-z]?) · (\S+) (\S+)? ?· ([\d.]+)s · (.*)$/);
  if (!m) continue;
  let j = i + 1; while (j < lines.length && lines[j] !== '```') j++;
  let k = j + 1; while (k < lines.length && lines[k] !== '```') k++;
  const prompt = lines.slice(j + 1, k).join('\n').trim();
  const head = m[6];
  const chained = /↳ chained/.test(head);
  const src = chained ? ((head.match(/last frame of `([^`]+)`/) || [])[1] || '') : '';
  const start = chained ? '' : ((head.match(/start: `([^`]+)`/) || [])[1] || '');
  let end = (head.match(/END FRAME `([^`]+)`/) || [])[1] || '';
  if (/END FRAME = the same extracted frame/.test(head)) end = '@start';
  clips[m[1]] = { id: m[1], kind: m[3], dur: Math.round(Number(m[5])), start, src, end, prompt, head, chained };
}

// chained clips start from Shots/start_frames/<ID>_start.png — Claude extracts it from the source's last frame
// (ffmpeg -sseof -0.08, no scale, no lift — the same image Kling's last-frame button gives)
function frameFile(name, id, chained) {
  if (chained) return path.join(G, 'Shots', 'start_frames', `${id}_start.png`);
  const guest = path.basename(G);
  for (const p of [path.join('Start_Frames', guest, name + '.png'), path.join('Start_Frames', 'Host', name + '.png')]) if (fs.existsSync(p)) return p;
  return path.join('Start_Frames', guest, name + '.png');
}
// settings straight from the header text (L51: no chip anywhere; the v3 prompt holds the camera)
function settings(c) {
  const h = c.head;
  if (/B-roll|still/.test(c.kind)) return null;                                     // b-roll stays on the website
  if (/Standard · audio OFF/.test(h)) return { model: 'kling-video-v3_0', enable_audio: 'false', prefer_multi_shots: 'false', resolution: '1080p' };
  if (/Standard · audio ON/.test(h))  return { model: 'kling-video-v3_0', enable_audio: 'true',  prefer_multi_shots: 'false', resolution: '1080p' };
  if (/Turbo \*\*720p\*\*/.test(h))   return { model: 'kling-video-v3_0_turbo', resolution: '720p' };   // audio only, picture unused
  if (/Turbo · audio ON/.test(h))     return { model: 'kling-video-v3_0_turbo', resolution: '1080p' };  // Turbo audio is always on (CLI caps)
  return null;
}
const pick = (txt) => { const m = txt.match(/"url_?[wW]ithout_?[wW]atermark"\s*:\s*"([^"]+)"/); return m ? m[1] : null; };   // L20
const run1 = (argv) => new Promise((res) => execFile(KLING, argv, { maxBuffer: 1 << 24, timeout: 35 * 60 * 1000 },
  (err, out, errout) => res({ err, out: String(out || ''), errout: String(errout || '') })));
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
// Kling rate-limits bursts ("too many requests") — wait and retry, up to 6 times (L26)
async function run(argv) {
  for (let k = 0; ; k++) {
    const r = await run1(argv);
    if (!/too many requests|slow down/i.test(r.out + r.errout) || k >= 5) return r;
    await sleep(20000 * (k + 1));
  }
}
// upload each seed image once per run and reuse its URL — fewer requests (L26)
const uploads = {};
async function uploaded(file) {
  if (DRY) return file;
  if (!uploads[file]) uploads[file] = (async () => {
    const r = await run(['file_upload', file]);
    return ((r.out + r.errout).match(/https?:\/\/[^\s"']+/) || [])[0] || file;   // fall back to the path (CLI uploads it)
  })();
  return uploads[file];
}

async function one(id) {
  const c = clips[id]; const t0 = Date.now();
  const logl = (status, extra = '') => fs.appendFileSync(LOG, [new Date().toISOString(), id, status, c ? c.dur + 's' : '', ((Date.now() - t0) / 1000 | 0) + 's', extra.replace(/\s+/g, ' ').slice(0, 300)].join('\t') + '\n');
  if (!c) { logl('SKIP', 'not on this sheet'); return `${id} ✗ not on ROUND${PASS} sheet`; }
  const st = settings(c); if (!st) { logl('SKIP', 'website clip'); return `${id} – b-roll: made on the website`; }
  const img = frameFile(c.start, id, c.chained);
  if (!fs.existsSync(img)) { logl('FAIL', 'start frame missing ' + img); return `${id} ✗ start frame missing: ${img}`; }
  const argv = ['image_to_video', '--image', await uploaded(img), '--model', st.model, '--duration', String(c.dur), '--poll', '1800'];
  if (c.end) { const tf = c.end === '@start' ? img : frameFile(c.end, id, false); if (!fs.existsSync(tf)) { logl('FAIL', 'end frame missing'); return `${id} ✗ end frame missing`; } argv.push('--tailImage', await uploaded(tf)); }
  for (const [k, v] of Object.entries(st)) if (k !== 'model' && !k.startsWith('_')) argv.push('--' + k, v);
  let prompt = c.prompt;
  fs.mkdirSync(path.join(OUT, 'raw'), { recursive: true }); fs.writeFileSync(path.join(OUT, 'raw', `${id}.prompt.txt`), prompt);   // exactly what was sent
  argv.push(prompt);
  if (DRY) { logl('DRY', argv.slice(0, -1).join(' ')); return `${id} dry: ${argv.slice(0, -1).join(' ')} + prompt (${c.prompt.length} chars)`; }
  const r = await run(argv);
  const all = r.out + '\n' + r.errout;
  fs.mkdirSync(path.join(OUT, 'raw'), { recursive: true }); fs.writeFileSync(path.join(OUT, 'raw', `${id}.txt`), all);
  // the clean file: works[].urlWithoutWatermark (L20). Never keep the watermarked `url`.
  const url = pick(all);
  const gid = (all.match(/generation_?[iI]d"?\s*[:=]\s*"?([\w-]+)/) || [])[1] || '';
  if (!url && gid) { const q = await run(['query_tasks', gid]); const u2 = pick(q.out); if (u2) { return await save(id, c, st, gid, u2, logl); } }
  if (!url) { logl('FAIL', `gen ${gid} ` + (r.err ? String(r.err.message) : '') + ' ' + all.slice(-400)); return `${id} ✗ no video (${gid || 'no id'}) — see kling_log.tsv`; }
  return await save(id, c, st, gid, url, logl);
}
async function save(id, c, st, gid, url, logl) {
  const dst = path.join(OUT, `${id}.mp4`);
  const resp = await fetch(url); fs.writeFileSync(dst, Buffer.from(await resp.arrayBuffer()));
  logl('OK', `gen ${gid} ${st.model} ${st.resolution || ''} clean`);
  return `${id} ✓ ${c.dur}s ${st.model}${st.resolution === '720p' ? ' 720p' : ''}  → Shots/_tests/${id}.mp4`;
}
// --refetch ID:generationId,…  re-download finished jobs (clean) without generating — no credits
if (opt('--refetch')) {
  for (const pair of opt('--refetch').split(',')) {
    const [id, gid] = pair.split(':'); const q = await run(['query_tasks', gid]); const u = pick(q.out);
    if (!u) { console.log(`${id} ✗ no clean link in the reply`); continue; }
    const r2 = await fetch(u); fs.writeFileSync(path.join(OUT, `${id}.mp4`), Buffer.from(await r2.arrayBuffer()));
    fs.appendFileSync(LOG, [new Date().toISOString(), id, 'REFETCH', '', '', `gen ${gid} clean`].join('\t') + '\n');
    console.log(`${id} ✓ clean copy → Shots/_tests/${id}.mp4`);
  }
  process.exit(0);
}
const acct = async (tag) => { if (DRY) return; const r = await run(['account']); fs.appendFileSync(path.join(OUT, 'kling_account.log'), `== ${tag} ${new Date().toISOString()}\n${r.out}${r.errout}\n`); };
await acct('before ' + IDS.join(','));
const queue = [...IDS]; const results = [];
await Promise.all(Array.from({ length: Math.min(CONC, queue.length) }, async () => {
  while (queue.length) { const id = queue.shift(); const line = await one(id); console.log(line); results.push(line); }
}));
await acct('after');
console.log(`— ${results.filter(l => l.includes('✓')).length}/${IDS.length} done. Tell Claude "done".`);
