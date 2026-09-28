# POSE LIBRARY — Host, permanent

Generated once, reused for the life of the series. Never regenerated for a later
episode, never generated mid-production to fit a line.

Structure is the confirmed working two-input prompt used for guest seed frames
(see `skill_mode2_cast.md`): `host_base.png` supplies identity and wardrobe,
`cam1_host.png` supplies the room and camera. Only the PLACEMENT paragraph changes
between variants — everything else is byte-identical.

Substitute the platform's real asset ids for `@host_base` (`host_base.png`) and
`@cam1_host` (`cam1_host.png`). Never leave the placeholders in.

The finished host frames live in **`Start_Frames/Host/`** (moved 2026-09-26).

## Template

```
Generate a still photograph of the man from @host_base seated in the room from @cam1_host, taken from that exact camera position.

@host_base is a four-panel character reference sheet: take his face from the close-up panel and his wardrobe from the full-body panels. The output is a single photograph of him in the room — not a panel sheet, and none of the light gray studio backdrop from the sheet appears anywhere.

KEEP IDENTICAL from @cam1_host: every material, colour and fixture — the dark charcoal panel wall behind the chair, the floor lamp with the warm shade, the vertical walnut slat wall filling the right of the frame, the round walnut table edge and the black microphone on its short stand at the lower right, the second microphone stand at the lower right corner, the woven rug, the light oak floor, the warm 2700K practical lighting, the colour grade, film grain and lens character, and the exact camera position and framing. Do not reframe, zoom, or change focal length. No furniture is added or removed: the room contains exactly what @cam1_host shows, and no second chair appears.

KEEP IDENTICAL from @host_base: his face, short dark hair receding at the temples, short greying beard and stubble, plain black crew-neck t-shirt, dark indigo jeans, black low-top sneakers.

PLACEMENT: [one variant below]

LIGHTING: lit only by the room's existing warm practical lighting, matching its direction and warmth, no new light source introduced.

Photorealistic still, 16:9, same grain and grade as cam1_host. He is the only person in frame.
```

## PLACEMENT variants — `frame_host` set

Every variant opens "seated in the armchair" and closes with this paragraph, pasted
unchanged:

> His body is angled slightly toward the right edge of the frame and his eyes look off-camera to the right, toward someone sitting across from him who is outside the frame. Head level, mouth closed, calm attentive expression. Seated at natural human scale for that chair, fully in contact with the seat.

- **`frame_host`** — settled back with both forearms resting along the armrests, hands relaxed. *(matches the existing file; regenerate only if the set needs to be rebuilt)*
- **`frame_host_b`** — leaning forward slightly, back off the chair back, both elbows resting on his thighs and his hands loosely clasped between his knees.
- **`frame_host_c`** — settled well back with one ankle crossed over the opposite knee, one hand resting on that ankle and the other forearm along the armrest.
- **`frame_host_d`** — one elbow on the armrest at the right of the frame, that hand raised so his knuckles rest lightly against his jaw, the other hand resting on his thigh.
- **`frame_host_e`** — forearms off the armrests, both hands loosely clasped in his lap, shoulders square, settled back into the chair.
- **`frame_host_f`** — one arm draped along the top of the chair back at the left of the frame, the other hand flat on his thigh, torso open a little further toward the right of the frame. ⚠️ *As generated, the frame-left arm is draped over the front of the armrest, not the chair back — prompts follow the image (`tools/poses.py`).*

## PLACEMENT variants — `frame_host_direct` set

Same template, same plate. Only the closing paragraph changes — he addresses the lens
instead of the guest:

> His body faces slightly toward the right edge of the frame but his head is turned to camera and his eyes look directly into the lens. Head level, mouth closed, calm and direct expression. Seated at natural human scale for that chair, fully in contact with the seat.

- **`frame_host_direct`** — settled back with both forearms resting along the armrests, hands relaxed. ⚠️ *As generated, both hands rest on his thighs — prompts follow the image (`tools/poses.py`).*
- **`frame_host_direct_b`** — leaning forward slightly, forearms on his thighs, hands loosely clasped.
- **`frame_host_direct_c`** — forearms off the armrests, both hands loosely clasped in his lap, shoulders square.

## Prompt wording — `Fixed_Assets/tools/poses.py`

How each frame is written into a Kling prompt (its hold, the hand-off-the-jaw entry for `frame_host_d`,
its one-way gestures) lives in `tools/poses.py`, next to the gates that check it. A new or changed
variant here gets its entry there in the same sitting (Mode 4 §5).

## Acceptance check

Open each finished variant next to `cam1_host.png` and `frame_host.png` before registering it:
- the armchair sits in the same place in the frame, at the same size
- the microphone, its stand, and the second stand have not moved or changed scale
- the floor lamp, the charcoal wall and the slat wall are unchanged
- the face reads as the same man; t-shirt, jeans and sneakers identical to the sheet
- mouth closed, eyes open, eyeline off-frame right (or into the lens, for the direct set)
- the armchair still reads visibly wider than him, upholstery showing either side of the torso

Any variant failing one of these is regenerated, not kept.
