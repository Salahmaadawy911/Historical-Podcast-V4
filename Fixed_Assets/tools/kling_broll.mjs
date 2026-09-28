#!/usr/bin/env node
// kling_broll.mjs — b-roll through the Kling CLI, in two steps (2026-09-27, Salah, L54). Runs on the Mac, from the project folder.
//   node Fixed_Assets/tools/kling_broll.mjs Episodes/<Guest> stills P1_031,P1_050   → Shots/stills/<ID>.png  (Kling image 3.0, 16:9, 2k)
//   node Fixed_Assets/tools/kling_broll.mjs Episodes/<Guest> video  P1_031,P1_050   → Shots/_tests/<ID>.mp4  (Turbo 1080p, from the still)
// Salah looks at the stills before the videos are made. Prompts come from the round sheet's two b-roll sections.
// Running it IS the approval to spend credits. Add --dry to print the calls only.
import { execFile } from 'node:child_process';
import fs from 'node:fs'; import path from 'node:path';
const [G, STEP, IDLIST] = process.argv.slice(2); const DRY = process.argv.includes('--dry');
if (!G || !['stills', 'video'].includes(STEP) || !IDLIST) { console.log('usage: node Fixed_Assets/tools/kling_broll.mjs Episodes/<Guest> stills|video P1_031,P1_050 [--dry]'); process.exit(1); }
const IDS = IDLIST.split(',');
const sheet = fs.readFileSync(path.join(G, 'ROUND1_prompts.md'), 'utf8');
const s1 = sheet.split('## B-roll step 1')[1]?.split('## B-roll step 2')[0] || '';
const s2 = sheet.split('## B-roll step 2')[1] || '';
const STILL = {};
for (const m of s1.matchAll(/^### (P\d_\d{3}[a-z]?) · still\n```\n([\s\S]*?)\n```/gm)) STILL[m[1]] = { prompt: m[2].trim() };
const VIDEO = {}; for (const m of s2.matchAll(/^### (P\d_\d{3}[a-z]?) · ([\d.]+)s · [^\n]*\n```\n([\s\S]*?)\n```/gm)) VIDEO[m[1]] = { dur: Math.round(+m[2]), prompt: m[3].trim() };
const KLING = process.env.KLING_BIN || 'kling';
const run1 = (argv) => new Promise((res) => execFile(KLING, argv, { maxBuffer: 1 << 24, timeout: 35 * 60 * 1000 }, (e, o, er) => res({ e, all: String(o || '') + '\n' + String(er || '') })));
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
async function run(argv) { for (let k = 0; ; k++) { const r = await run1(argv); if (!/too many requests|slow down/i.test(r.all) || k >= 5) return r; await sleep(20000 * (k + 1)); } }
const clean = (t) => (t.match(/"url_?[wW]ithout_?[wW]atermark"\s*:\s*"([^"]+)"/) || [])[1] || (t.match(/"(?:url|image_?[uU]rl)"\s*:\s*"(https[^"]+)"/) || [])[1];
const stillsDir = path.join(G, 'Shots', 'stills'); const tests = path.join(G, 'Shots', '_tests');
fs.mkdirSync(stillsDir, { recursive: true }); fs.mkdirSync(path.join(tests, 'raw'), { recursive: true });
async function one(id) {
  if (STEP === 'stills') {
    const c = STILL[id]; if (!c) return `${id} ✗ no still prompt on the sheet`;
    const argv = ['text_to_image', '--model', 'kling-image-v3_0', '--aspect_ratio', '16:9', '--img_resolution', '2k', '--poll', '1800', c.prompt];
    if (DRY) return `${id} dry: ${argv.slice(0, -1).join(' ')} + prompt (${c.prompt.length} chars)`;
    const r = await run(argv); fs.writeFileSync(path.join(tests, 'raw', `${id}.still.txt`), r.all);
    const u = clean(r.all); if (!u) return `${id} ✗ no image — see Shots/_tests/raw/${id}.still.txt`;
    fs.writeFileSync(path.join(stillsDir, `${id}.png`), Buffer.from(await (await fetch(u)).arrayBuffer()));
    return `${id} ✓ still → Shots/stills/${id}.png`;
  }
  const c = VIDEO[id]; if (!c) return `${id} ✗ no video prompt on the sheet`;
  const img = path.join(stillsDir, `${id}.png`); if (!fs.existsSync(img)) return `${id} ✗ make the still first (Shots/stills/${id}.png)`;
  const argv = ['image_to_video', '--image', img, '--model', 'kling-video-v3_0_turbo', '--duration', String(c.dur), '--resolution', '1080p', '--poll', '1800', c.prompt];
  if (DRY) return `${id} dry: ${argv.slice(0, -1).join(' ')} + prompt (${c.prompt.length} chars)`;
  const r = await run(argv); fs.writeFileSync(path.join(tests, 'raw', `${id}.txt`), r.all);
  const u = clean(r.all); if (!u) return `${id} ✗ no video — see Shots/_tests/raw/${id}.txt`;
  fs.writeFileSync(path.join(tests, `${id}.mp4`), Buffer.from(await (await fetch(u)).arrayBuffer()));
  return `${id} ✓ ${c.dur}s → Shots/_tests/${id}.mp4`;
}
const q = [...IDS]; await Promise.all([0, 1].map(async () => { while (q.length) console.log(await one(q.shift())); }));
console.log(`— done. Tell Claude "done".`);
