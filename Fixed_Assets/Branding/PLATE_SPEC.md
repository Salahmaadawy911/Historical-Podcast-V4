# Lower third / pull-quote plates — fixed assets

**The plate is built once. Only the text changes per guest.** Four PNGs with alpha, at a 3840×2160 reference so they scale down to 1080p cleanly:

| File | Size | Use |
|---|---|---|
| `BRAND_lowerthird_plate_R.png` | 1612 × 270 | name banner, **guest** (sits screen-right) |
| `BRAND_lowerthird_plate_L.png` | 1612 × 270 | name banner, **host** (sits screen-left) |
| `BRAND_pullquote_plate_R.png` | 2112 × 334 | pull-quote, guest side |
| `BRAND_pullquote_plate_L.png` | 2112 × 334 | pull-quote, host side |
| `BRAND_context_plate_L.png` | 1382 × 540 | context card, sits **screen-left** — used when the **guest** speaks (opposite her) |
| `BRAND_context_plate_R.png` | 1382 × 540 | context card, sits **screen-right** — used when the **host** speaks |

⚠️ **The context plates are named by screen side, not by speaker** — the opposite of the other two pairs, because the card sits *opposite* the speaker. Built by `intro_source/context_build.py plates`; full spec in `STUDIO_ASSETS.md`, *Context card*.

The walnut margin rule is baked in. The paper texture, the torn edge and the rule are all part of the asset — nothing about them is decided per episode.

⚠️ **The current plates carry a procedurally generated paper texture and are placeholders.** Synthetic noise reads as digital grain rather than paper fibre once it is on screen at full size. They are being rebuilt on a **generated** paper photograph — same geometry, same rule, same tear, real stock. See `PAPER_SOURCE.md`.

## Placement

- **Outer edge flush to the frame edge**, so the plate bleeds off. A plate with a gap on both sides reads as a detached box sitting on the picture.
- **Bottom edge at 90% of frame height.** The lower 10% stays clear — that is where the player's own controls and captions live.
- **The side follows the speaker.** Guest screen-right → `_R`. Host screen-left → `_L`. This holds even when the speaker's side is the busier half of the frame: association with the person beats a cleaner background.

## Text

Positions are given as x-offsets **inside the plate**, at the 3840-wide reference. Scale proportionally.

| | `_R` (left-aligned from) | `_L` (right-aligned to) |
|---|---|---|
| Lower third | x = 166 | x = 1446 |
| Pull-quote | x = 166 | x = 1946 |

| Element | Font | Size | Top, as a fraction of plate height | Colour |
|---|---|---|---|---|
| Name | Anton | 44% of plate height | 15.5% | ink `#12161C` |
| Second line | Libre Baskerville Regular | 16% | 70% | `#463C38` |
| Pull-quote | Playfair Display Italic | 28.5% | two lines, 17% and 54.5% | ink `#12161C` |

**On the host side the type right-aligns to the text edge. It never mirrors** — the plate flips, the words do not.

## Drop shadow

Applied in the editor, not baked into the asset, so it can sit correctly over whatever is behind it: offset 4px right / 6px down at 4K, 9px blur, ~60% opacity. Enough to read as a card lying on the picture rather than a graphic pasted onto it.

## What is decided per episode

Only the words, and which shot each plate opens over — both of which come from the kit's **§12 · On-screen text**, never invented at the edit. The kit names the exact shot for each of the two lower thirds and each of the three or four pull-quotes, because the pull-quotes are chosen from the part's Key Lines and have to land over picture that carries no dialogue.

## What is fixed forever

Everything else. If any of it changes, it changes for the whole series at once.
