# Thumbnail — the system

Three layers, and each one has a different job and a different lifespan.

| Layer | What it is | Changes |
|---|---|---|
| **The figure** | the guest, **photoreal**, softly lit for paper, placed whole and unfaded | per guest |
| **The ground** | **toned paper** — the same stock as the lower-third plates | **never** — one fixed asset, `paper_source.png` |
| **The words** | kicker + 3–5 word statement, Anton caps, in the dark left third | per part |

**The figure is real and the world is drawn.** That is the show's premise as a picture: the person is present and speaking; the past around them is a reconstruction. It is the same idea as the outro dissolve, arriving first instead of last.

## The strength of the drawn world — measured, not guessed

Tested at four strengths against real YouTube feed sizes (360px desktop, 210px mobile):

| Drawn world | Result at 210px |
|---|---|
| 0% (plain black) | cleanest face separation, no identity |
| **20–25%** | **the sweet spot** — the drawing registers as texture and identity, the face still separates fully |
| 45% | background begins competing with the face |
| 85% | face loses separation, tile reads as busy |

**Lock it at 20–25%.** The whole job of a thumbnail is one face and a few words at maximum separation, and anything that steals contrast from the face costs clicks. At a quarter strength the drawn world does its identity work for free.

The **fully drawn** thumbnail — charcoal figure as well as charcoal world — was tested and rejected: at 210px a charcoal face stops reading as a specific person, which is the one thing the thumbnail is selling. Measured, the style sits at 0.236 saturation and 0.471 value, i.e. low-contrast and mid-bright, exactly wrong for a small tile.

## The ground is paper, and the portrait is lit for it

**The thumbnail sits on the same toned paper as the lower-third plates** — `paper_source.png`, the single stock used everywhere in the series. Dark ink type, warm accent kicker, the mark in ink.

### Two rejected grounds, and why

**A per-episode drawn scene** (ships for Actium, legionaries for an invasion) failed on its own numbers: at the ~22% strength that avoids competing with the face, the background cannot be read at all, so a scene strong enough to identify is also strong enough to eat the face's separation. The two requirements are in direct conflict.

**A dark ground** works and tested well — but in a feed of overwhelmingly dark tiles, a light one is the one that stops the scroll. That advantage does not show up in any contrast measurement and it is the strongest argument in the system.

### The contrast worry was wrong, and the reason is worth keeping

Paper was argued against on the grounds that warm skin on warm paper is the weakest possible pairing. **That reasoning was about mid-tone against mid-tone in the abstract and it does not survive the actual tile.** The face occupies roughly 40% of the frame and carries its own dark anchors — hair, brows, eyes. When a face is that large, contrast *within* the face does the work; contrast against the ground barely matters.

**The rule that follows:** judge a thumbnail by whether the features read at 210px, never by the tonal relationship between subject and background.

### The portrait must be lit for paper

A portrait lit against black has a **black shadow side**. On a dark ground that reads as chiaroscuro; on paper it either gets cut away or becomes a hard silhouette edge. Neither is recoverable in compositing.

So the portrait is generated **for** the paper: soft even light, a shadow under the jaw for separation, no deep shadow on the face, and **a flat pale warm-grey background matching the paper's tone** — which means there is no cutout at all. The two grounds are tone-matched and blended.

### The fade — tested, and not used

**The setting is CLEAN: no fade.** The portrait sits whole on the paper.

A fade at the portrait's periphery — hair, shoulder, the far edge of the jaw dissolving into the page — was built and tested at two strengths. It is a real idea and it says something true about the show: the record is partial, and so is the reconstruction. It was not chosen; clean reads stronger at 210px and a thumbnail's first job is the face.

Recorded because it may be worth revisiting, and because the rule it produced still governs anything that ever partially obscures a guest:

⚠️ **The eyes, the brows and the line from nose to mouth never dissolve.** Break up only what a drawing plausibly runs out of. The moment a feature that makes the guest a specific person breaks up, it stops signalling *incomplete record* and starts signalling *broken image*, and people scroll past. The strong-fade version failed exactly here — the face washed out at feed size.

If it is ever revisited: the fade must be **directional**, strongest at the frame edges and away from the type, thinning across the face, masked by the paper's own grain so it reads as the drawing running out rather than as damage. Never random, never centred on the face.

## Layout## Layout## Layout

- **Figure on the right**, head and shoulders, filling roughly the right 40% of the frame.
- **Gaze off the left edge**, never at the lens — it leads the eye into the text, and it matches the episode, where she never looks at the audience.
- **Left 60% falls to near-black**, with the drawn world faintly present in it. Text needs a flat ground or it turns to mush at 210px.
- **Kicker line** above the headline: guest name and part, one line, in lamp `#E0B071`, Anton caps at ~4.4% of frame height with generous letter-spacing — `CLEOPATRA VII · PART 1`.
- **Headline** two lines, Anton caps, cap height ~13.2% of frame height, starting ~5.5% in from the left.
- **Channel mark** bottom-left, the **full `brand_mark`** (symbol + wordmark), **white at 8.5%** of frame height. Tested against slate grey, lamp gold and a larger 10.5%: slate all but disappears at 210px, gold duplicates the kicker's colour and dilutes it, and 10.5% begins taking attention from the statement. ⚠️ The shipped `brand_mark_1600.png` is the **ink** version — recolour it or export from the `_light.svg`, or it is invisible on the dark third.

### Why the guest name is on the thumbnail, against the usual rule

Standard packaging advice is to keep the name off the thumbnail because the title already carries it, and for **click-through** that is right — the two are read together and duplicating wastes half the space.

It is wrong for a **series**, and the reason is the channel page. A grid of twenty tiles that all carry only a statement is unnavigable; a viewer cannot find the Genghis Khan episode at a glance. The name is not selling the click, it is indexing the library — and that value grows with every episode added.

**Merge the name and the part into one kicker line.** Tested against the alternative of name above and part badge below: stacking three text elements around the headline crowds it and the part badge turns to mush at 210px. One kicker carries both facts, the headline keeps its full weight, and nothing is competing.

At 210px the kicker sits at the edge of legibility. That is acceptable and intended — it does its work on desktop and on the channel page, and at phone-feed size the headline carries alone.

**Title and thumbnail must not say the same thing.** The viewer reads both at once; duplicating wastes half the space. The title carries the subject, the thumbnail carries the provocation.

## The recipe — follow this, do not redesign it

Every value below is fixed. **The only decisions per part are the kicker and the statement**; the only decision per guest is the portrait. Everything else is arithmetic.

### What changes, and how often

| | Changes | Comes from |
|---|---|---|
| Photoreal portrait | **once per guest** | Mode 2 casting, generated from the character sheet |
| Kicker + statement | **once per part** | the kit's Key Lines (§12) |
| Paper ground | **never** | one fixed asset, `paper_source.png` — the same stock as the plates |
| Everything else | **never** | this file |

**For a second part of the same guest, two lines of text change and nothing else.** For a new guest, one portrait is generated. There is no other decision.

### Step 1 — Pick the statement, before any image exists

Take it from the part's **Key Lines** in the kit. It is 3–5 words, all caps, and it must survive being read by someone who knows nothing. The kit already identifies these lines and uses them for pull-quotes and reel hooks, so the thumbnail is not a separate writing job.

**The title and the statement must not say the same thing.** The title carries the subject; the statement carries the provocation.

### Step 2 — Generate the portrait (once per guest)

**Inputs: the guest's character sheet (`Episodes/<Guest>/guest_<guest>.png`) attached as the only reference image, plus the prompt below.** The prompt's *"the woman from the reference"* points at the sheet; change *woman* to match the guest's prompt label. Don't use a seed frame or a plate, because they bring the studio in with them. This is how Cleopatra's approved portrait was made. **Lit for paper, not for black** — see above for why that is not optional.

⚠️ **Paste this as three unbroken lines.** Kling strips newlines without inserting a space, so a hard-wrapped prompt arrives with words fused at every line break (`frame.Soft`). Every prompt in this project is written unwrapped for that reason; never reflow one to make it look tidier.

```
Her head positioned in the right third of the frame, the entire left half of the frame empty background. A tight three-quarter portrait of the woman from the reference, head and shoulders, her body angled inward, her gaze directed off the left edge of frame past the camera.

Soft even daylight from the front and slightly above. Gentle modelling on the cheek and jaw and a soft shadow beneath the jaw to separate her from the background, but no deep shadow anywhere on the face and no dark side — the contrast comes from her dark hair, brows and eyes, not from shadow.

Plain flat background in a warm pale grey, the tone of toned drawing paper, evenly lit corner to corner with no vignette and no shadow cast onto it. Cream linen drapery, thin gold diadem. No microphone, no chair, no table, no furniture of any kind. 16:9.
```

⚠️ **The wardrobe words are guest-specific** (added 2026-09-23). *"Cream linen drapery, thin gold diadem"* is Cleopatra's. For any other guest, replace them with the garment and headwear from that guest's `CAST.md` *Wardrobe*, headwear named on its own as Mode 2 requires. Everything else in the prompt stays the same. Record the exact prompt used in the guest's `CAST.md` under *Thumbnail portrait*.

**Lead with the framing.** Cleopatra's approved portrait (`thumb_portrait_cleopatra.png`) was made with the earlier ordering and came back with her head near the centre. Step 4 cuts out the figure and places it anyway, so a centred portrait is usable; the reordering only saves a crop. An earlier version of this prompt opened with "a tight three-quarter portrait" and put the framing after it; the model centred her every time. Naming the empty half first is what puts her on the right.

**Judge candidates on the hair and brows**, not the skin. They are carrying all the contrast — a generation that comes back with soft, low-contrast hair has no shape at 210px and should be discarded. The cream drapery *will* merge into the paper; let it. That is the figure fading into the page, and it is on-brand. The face is what must hold.

### Step 3 — The ground: already exists, do not regenerate

`paper_source.png`. The same stock as the lower-third plates. **Skip this step entirely.**

### Step 4 — Composite

| Element | Value |
|---|---|
| Canvas | 1280 × 720 minimum; build at 2560 × 1440 and scale down |
| Ground | `paper_source.png`, full strength |
| Figure | cut out, placed right, occupying roughly the right 40% |
| Portrait blend | tone-match the portrait's flat background to the paper, then blend the seam across ~30% of frame width |
| Left margin for all type | **5.5%** of frame width |
| Kicker | Anton caps, **4.4%** of frame height, letter-spaced ~0.75% of frame height, walnut `#9C6B3F` — `GUEST NAME · PART N` |
| Gap under kicker | 1.9 × kicker size |
| Statement | Anton caps, **13.2%** of frame height, two lines, line spacing 1.02, ink `#12161C` |
| Text block | vertically centred, then raised by 4.5% of frame height |
| Mark | **`brand_mark_trimmed.png`** in ink, **8.5%** of frame height, bottom-left on the same 5.5% margin, centred at 86.5% of frame height. Use the trimmed file — the 1600x560 original has 41px of empty canvas at the bottom and none at the top, which renders the mark small and high. |

### Step 5 — Check at 360px and 210px, every time

Not optional and not a formality. Scale the finished tile to 360px and 210px wide and look at both. **Three failure modes, all invisible at full size:**

- the face loses separation from the background
- the statement stops reading in one glance
- the fade has eaten a feature, or the portrait has drifted left into the type

If any of those happen, the fix is the fade strength or the portrait's position — **never** shrinking the statement.

## How to build it

**Composite, do not generate as one image.** Asking one prompt for "photoreal person on a drawn ground" invites the model to blend the two styles across the whole frame, which produces neither. Compositing keeps each layer at full quality and lets the portrait be regenerated without touching anything else.

⚠️ **The reference mockups in this folder fake the cutout** from image luminance, so the drawn world ghosts faintly through her face. That is an artefact of the mockup, not of the design — a real cutout or a generated-with-alpha figure has no such bleed.
