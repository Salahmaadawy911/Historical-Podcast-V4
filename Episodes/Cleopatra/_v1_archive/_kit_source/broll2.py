# -*- coding: utf-8 -*-
SKETCH=("A charcoal and graphite drawing on toned grey paper. Forms built from tone rather than outline - broad "
"washes and smudged shading, edges appearing where two tones meet rather than being drawn. Heavy tonal contrast, deep "
"shadow, visible paper grain and tooth. Monochrome apart from the faint warmth of the paper. No outlining, no chalk "
"highlights, no metallic or gold accents.")
PERSIST=(SKETCH+" It stays a drawing for every frame of the clip; the tone and the paper grain remain visible "
"throughout, and it never resolves into photographic footage.")
LEGION=("Roman legionaries of the late Republic: knee-length chain mail shirts over off-white wool tunics, plain bronze "
"helmets with a small flared neck guard and hinged cheek pieces, deep red wool cloaks, wide leather belts with hanging "
"studded straps, heavy open-laced leather sandals. No metal shin guards. No plate or banded armour.")
def A(txt): return ("Audio: "+txt+" No music, no dialogue, no voiceover, no on-screen text, no subtitles, no logo.")

# id -> (still_subject, move, motion, audio, note)
ROWS = {
"P1_013":(LEGION+" A body of them on dry open ground, seen from behind, one rank behind another and receding into the distance, dust hanging low around their legs. Drawn from knee height looking along the ranks.",
 "The camera pushes in very slowly along the ranks.",
 "The ranks advance away from the camera at a steady walking pace, shoulders and cloaks swinging slightly with the stride, dust stirring around their legs as they go.",
 A("low dust and wind, the muffled tread of many feet, distant and unemphatic."),
 "**armour corrected.** The original read *segmented iron armour* — lorica segmentata, Imperial kit from the first century **AD**, roughly fifty years after Cleopatra died. Replaced with the registered `legionary_late_republic` wardrobe block: mail, not plate. **Crowd described by arrangement, not by count** — \"a column\" previously rendered as a line abreast."),

"P1_017":("A scatter of worn coins on dark stone, close, lit hard from one side so the relief on each face catches the light. No hands, no figures.",
 "The camera drifts slowly sideways across the coins.",
 "Only the light moves — the highlights on the raised relief shift and travel across each face as the angle changes. The coins themselves are still.",
 A("near silence, faint room air, a single soft metallic settle."), None),

"P1_043":("A lamplit stone corridor at night, flames in wall niches, long shadows thrown across worn flagstones, the corridor running away from the viewer into darkness. Empty — no figures.",
 "The camera moves slowly forward down the corridor.",
 "The flames waver in their niches and the shadows they throw stretch and contract along the walls and floor as the view advances.",
 A("low flame flicker, faint echo of distant movement, quiet air."), None),

"P1_051":("A single small oil lamp burning in a shallow clay dish on a stone ledge, deep shadow beyond it, the flame the only light in the frame.",
 "The camera pushes in very slowly on the lamp.",
 "The flame wavers and leans, brightening and dimming slightly, and the shadow it throws behind the dish shifts with it. Nothing else moves.",
 A("faint flame, very quiet room air."), None),

"P1_058":("A vast still expanse of open river water at dusk under a low flat band of sky, reeds along the near bank, the far bank a thin dark line. No boats, no figures, no buildings.",
 "The camera drifts slowly sideways across the water.",
 "The reeds in the foreground bend and recover in the wind, and the surface of the water carries a slow continuous ripple across it.",
 A("slow water lapping, distant night birds, faint wind through reeds."), None),

"P1_061":("A Roman commander of the late Republic standing over a low table spread with maps and wax tablets in lamplight, seen from behind and slightly to one side with his head lowered toward the table, one hand flat on it. A sculpted leather cuirass with bronze fittings over a wool tunic, a deep red cloak over one shoulder. His face is not visible.",
 "The camera pushes in very slowly toward the table.",
 "His shoulders rise and fall with his breathing and his hand shifts across the map; the lamplight wavers over the surface of the table.",
 A("quiet room air, faint lamp flame, the small sound of a hand moving on parchment."),
 "**changed:** the `@antony` character sheet is retired — b-roll is charcoal, which a photoreal sheet cannot drive. The figure is now **drawn from behind with his face not visible**, so the shot carries no likeness claim about a real named person and needs no sheet. The cuirass is described rather than referenced; a sculpted leather cuirass on a Roman commander c. 40–30 BC is defensible, but it was never verified and the framing no longer depends on it."),

"P1_071":(LEGION+" One of them standing at rest before a rough plastered wall in hard light, cloak hanging still, helmet held under one arm. Tight, drawn from slightly below.",
 "The camera pushes in very slowly.",
 "He shifts his weight once and settles again; the cloak stirs slightly. The wall behind him is still.",
 A("quiet outdoor air, faint wind, one small shift of equipment."),
 "**armour corrected** — mail, not banded plate. See P1_013. The reference tag is dropped: identity comes from the wardrobe block, and passing a reference for anonymous extras produced rows of clone faces in testing."),

"P1_083":("Open sea under a low overcast sky, a heavy swell running, no land and no vessels anywhere in the frame, spray torn off the wave crests. Wide.",
 "The camera pulls back very slowly.",
 "The swell rises and falls across the whole frame continuously, crests forming and collapsing, spray driving off them in the wind.",
 A("heavy water, sustained wind, no gulls."), None),

"P1_087":("The wake of a vessel seen from astern — a widening trail of disturbed water receding toward an empty horizon at dusk. No boat visible in the frame.",
 "The camera drifts slowly backward, away from the wake.",
 "The wake spreads and flattens as it recedes, the disturbed water settling behind it toward the horizon.",
 A("water displaced and settling, low wind."), None),

"P1_091":("A worn silver coin lying on dark stone, close and filling much of the frame, struck with two facing profile portraits — a man and a woman — and worn lettering around the rim. Lit hard from one side so the relief throws shadow. No hands, no figures.",
 "The camera pushes in very slowly on the coin.",
 "Only the light moves — the highlights travel across the two raised profiles and the worn lettering as the angle shifts. The coin itself is still.",
 A("near silence, faint room air."),
 "**replaced.** The original showed legionaries wading ashore, which covered the old *\"landed in the delta\"* line — a line that has been deleted for being both outside the retrospective frame and factually wrong (Octavian advanced overland and took Pelusium; there was no amphibious landing). The new host line asks about Antony, so the cutaway is now the joint coinage the two of them actually issued: documented, an object rather than a person, and it makes no likeness claim about either.")
}
