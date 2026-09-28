# The paper — one generated texture, used everywhere

One image, generated once, is the ground for **every** paper surface in the series: the lower-third plate, the pull-quote plate, the cards, the intro, and any future furniture. Generating it once is what keeps them all the same sheet rather than four different papers that happen to be beige.

## Generation prompt

```
A flat sheet of toned grey drawing paper photographed straight down, filling the entire frame.
Warm mid-grey stock, the kind used as a ground for charcoal drawing. Visible tooth and fibre,
a faint irregular mottling in the surface, a few darker specks in the pulp. Evenly lit corner
to corner, completely flat, no shadows and no falloff. Nothing else in the frame: no edges, no
corners, no objects, no writing, no drawing.
```

**What each constraint is preventing:**

| Phrase | The failure it blocks |
|---|---|
| *photographed straight down* | a perspective sheet, which cannot be cropped into a strip |
| *filling the entire frame* | a sheet floating on a background, so most of the image is unusable |
| *evenly lit, no shadows, no falloff* | a lighting gradient baked into the plate, which shows as a bright or dark end once it is a long thin strip |
| *no edges, no corners* | a visible paper edge crossing the middle of a crop |
| *no writing, no drawing* | the model helpfully adding a sketch to the drawing paper |

Generate at the largest size available, 16:9. Take **two or three** and keep the flattest — an even one is worth more than a characterful one, because unevenness repeats identically on every plate in every episode and becomes a signature nobody chose.

## What happens to it

The plate geometry, torn leading edge, walnut margin rule and alpha are applied to crops of this image. Different crops are taken for the name plate and the pull-quote plate so the two do not read as the same piece of paper twice.

Save as `Fixed_Assets/Branding/paper_source.png`.
