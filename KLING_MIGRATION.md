# Kling.ai — what changes, what to test, what not to touch

Notes from Kling's Video 3.0 and Element Library user guides, read against the pipeline
as it already stands. Kept out of the skill files until the platform decision is made.

## 0. Commercial use — RESOLVED, granted for paid members

The **Paid Services Agreement** settles it explicitly:

> KLING AI members' use of the Output for commercial purposes is not restricted … for any
> commercial purpose (except for the purposes of developing or offering competitive products
> or services of KLING AI).

And their FAQ Q8 says the same in plain language: paid subscribers may lawfully use,
reproduce, distribute, modify and create derivative works for commercial purposes.

**How this fits the general Terms of Service.** §4.6 restricts commercial use "without our
written permission". The Paid Services Agreement *is* that permission, and it is the more
specific document governing paid members. §4.6 is the default for non-paying users. There is
no conflict once both are read together — which is why the membership page and the ToS both
turned out to be accurate.

**The only carve-out is irrelevant to us:** output may not be used to build products or
services competing with Kling AI. A history documentary channel is not that.

**Watermarks and the §4.5 branding line.** The payment policy states non-member accounts
cannot remove watermarks, which implies paid members can. Read alongside the commercial
grant, §4.5 is best understood as "do not strip or tamper with Kling identifiers where they
appear" rather than a duty to put Kling branding on your own show. The FAQ frames labelling
as *our* obligation under applicable law and platform policy — which is the AI-disclosure we
already do several times over, not Kling attribution. Confirm watermark-free output on the
chosen tier at first generation; otherwise treat this as settled.

### One action item remains, and it is not about licensing

The Video Element notice grants other users the right to reuse content **published on Kling
AI** — images, prompts, video clips — through "One-Click Recreate" and similar, with their
derivatives publishable and downloadable. For a channel whose identity rests on one recurring
host, that is a brand risk worth closing. It appears scoped to content published to their
gallery, so simply not publishing there may avoid it. The notice provides an email opt-out at
support@klingai.com — take it in writing anyway.

Also standing: §1.1 warrants that uploads infringe no voice rights. A voice bound from one of
our own generated clips is synthetic and nobody's likeness. **Never bind a voice from a real
recording.**

### Privacy and data — what the policy actually says

Checked against `kling.ai/docs/privacy-policy` directly.

- **Training.** The privacy policy does **not** address model training at all, and offers no
  opt-out. The general Terms of Service do: §4.7.3(f) permits inputs and outputs to be used
  to create, test, improve, train and develop their models. **Higgsfield does the same**
  (§4.4), with training exemption reserved for enterprise agreements. So this is not a
  differentiator — on either consumer platform, the host character and the voices go into a
  training set. There is no version of this pipeline that avoids it short of an enterprise
  contract.
- **Private content.** The policy distinguishes public from private but does **not** spell
  out protections for unpublished work. In practice content is not published unless you
  publish it, and the Element notice's reuse grant is scoped to content published to their
  gallery — both consistent with unpublished work staying private. It is a reasonable
  inference, not a stated guarantee.
- **Deletion.** They reserve the right to delete data without notice and owe no compensation.
  Retention is "as long as necessary", varying by jurisdiction.
- **Storage.** Servers in Singapore, with international transfer to group entities under
  contractual safeguards.

**The one operational consequence: never treat either platform as storage.** Generated clips
are the raw material of the episode, and both platforms reserve the right to delete without
notice — quite apart from what happens to a lapsed account. Download every accepted
generation into the episode folder the day it is made. This is already the habit; it is now
a rule.

### Where this leaves the platform comparison

The terms are now broadly equivalent — both platforms grant commercial use to paying
customers. The earlier conclusion that Higgsfield was decisively better on terms **no longer
holds**. The decision returns to price and pipeline:

| | Kling | Higgsfield |
|---|---|---|
| Commercial use | granted to paid members | granted outright |
| Unit price, 1080p + audio | **$0.0615/s** | $0.0833/s |
| Crossover | cheaper above ~2.55 parts/month | cheaper below it |
| Stills (Seedream 5.0) | not available | starter plan, confirmed |
| Existing calibration | would need re-validating | already validated |

Kling wins on price at volume; Higgsfield holds the stills leg and the tested settings. The
hybrid already sketched — write kits continuously, cheap Higgsfield plan for Seedream, Kling
in bursts for video — remains the strongest shape.

## 1. Voice binding — the reason to consider moving

This is the significant find. Kling character elements can carry a **bound voice**:

- A **video character element** takes a 3–8 second clip and *"automatically extracts the
  character's appearance and native voice to generate a reusable video element asset."*
- A **multi-image element** (2–4 images) can also have *"a unique voice bound"* to it.
- The guide then says: *"Elements can include pre-bound voice tones; avoid re-specifying
  tone in prompt if already bound."*

**Why this matters more than anything else here.** Vocal identity is currently held by a
prose description pasted byte-identical into all 86 clips, with a speech-to-speech repair
pass as the fallback when it drifts. Binding replaces a *description of a voice* with
*the voice itself*. Consistency stops being something maintained and becomes something
structural.

And we already have the source material: clean generated clips of both the host and
Cleopatra with voices that were accepted. A 3–8s extract from one of those becomes the
element.

**Two unknowns to settle before relying on it:**

- The guide lists **Voice Control at 2 credits/second additional**. Whether that applies to
  element-bound voices or is a separate feature is not stated. If it applies, dialogue goes
  from 10 to 12 cr/s — a 20% increase that changes every budget figure. Check this first;
  it may cancel the platform's cost advantage outright.
- *"Avoid re-specifying tone in prompt if already bound"* is ambiguous between **voice
  identity** (block 5, which would be removed) and **per-shot register** (block 2, which
  must stay — it is the single most important rule in Mode 4). Test which one it means.

**Test:** build an element from an accepted host clip, then generate `P1_054` with block 5
removed and block 2 intact. Compare against the existing take. Watch for: does the voice
match, and does the register direction still land?

---

## 2. Element syntax differs

Kling references elements as **`[@ElementName]`** — bracketed. Higgsfield uses a bare
`@tag`. Every asset reference in `STUDIO_ASSETS.md` and the kits would need reformatting.

Limits are not a constraint for us: Video 3.0 allows a start frame plus up to 3 additional
elements, and we use one character per clip. Element storage is 150 on Pro, 500 on Ultra.

---

## 3. Accents are supported, and phrased in-prompt

Native audio covers English among others, and dialect or accent is specified in the prompt
directly — the guide's examples are *"in Cantonese"*, *"with an Indian accent"*. This was
an open question for non-native-English guests. Note the accent belongs in the **voice
block**, not the register block, and once bound to an element it should not be repeated.

---

## 4. Do not change these

The prompt structure is producing near-perfect results. Changes below are documented so
nobody re-derives them later, not because they should be made.

- **Dialogue format.** ⚠️ **Re-read 2026-09-20 against the current audio guide** — the syntax is
  *"put each speaker's name, line, and delivery note close together"*, the delivery note **inside**
  the attribution (*"the male lead says in a relaxed tone, '…'"*), ambience named in the same prompt,
  up to four speakers, accents and dialects stated in the prompt, simple grammar, and the speaking
  face kept readable. Two candidate optimisations — the inline delivery note, and a temporal marker
  (*"Immediately"*) to kill the 0.7–1.0 s lead-in silence — are specced for an A/B on one Act A clip
  in `skill_mode4_produce.md` §3. Until that test, the format below stands. Kling documents `Character (tone descriptor): dialogue` — e.g.
  *"Mom (softly, in a surprised tone): Wow, I didn't expect this plot at all."* Our format
  is a register paragraph followed by `The host says: "…"`. Kling's is arguably a tighter
  version of the same idea, and §3's rule 2b already came from their guidance about keeping
  the speaker close to the line. **Leave it.** It is validated, it works, and this is the
  highest-risk change available for the least demonstrated need. Reconsider only if
  something actually breaks.
- **One utterance, one clip, one angle.** Multi-shot exists and takes custom per-shot
  durations (`"Shot 1, […]. Shot 2, […]"`). It stays reserved for b-roll sequences, never
  for interview clips.
- **The camera lock paragraph.** Already updated to open with Kling's own canonical
  phrasing. Their guide otherwise talks in movement terms — *"tracking shot"*, *"push in"*,
  *"orbits"* — which is the opposite of what these shots need.

---

## 5. Worth testing later, low priority

Kling 3.0 *"preserves text in uploaded images (signs, logos, captions)"*. The brand sign is
currently composited onto the wide in Mode 6 precisely because a generated sign re-rolls
every episode. If text in a start frame genuinely survives, the branded wide plate could
carry the sign natively and skip a compositing step. The post route is safer and already
works, so this is a convenience test, not a fix.
