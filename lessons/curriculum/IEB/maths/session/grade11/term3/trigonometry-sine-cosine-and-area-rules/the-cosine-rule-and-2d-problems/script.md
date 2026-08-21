# Part 1 — Expert

The sine rule has a blind spot. Hand it two sides with the angle squeezed between them, or all three sides with no angle at all, and it stalls — no complete side-and-opposite-angle pair exists, so its ratio cannot be set. Those two situations are exactly what the cosine rule was invented for. This session proves the rule, drills both of its directions, and then sets both rules loose on the two-dimensional story problems that finish every trigonometry section: campsites, cell towers and triangles that share a side.

## Subtopic: The Cosine Rule and Where It Comes From

The cosine rule states: a squared equals b squared plus c squared, minus two b c cosine A. Learn its anatomy before its proof. On the left stands one side, squared. On the right stand the other two sides, squared and added, followed by a correction: minus twice their product times the cosine of the angle OPPOSITE the left-hand side. The squared side on the left and the angle inside the cosine always face each other across the triangle — that pairing is the rule's fingerprint.

Now the proof. In triangle ABC, drop a perpendicular from C onto side AB, landing at D. Inside the right-angled triangle ACD, the height CD is b sine A and the base AD is b cosine A. The remainder of AB is DB, which is c minus b cosine A. Apply Pythagoras in triangle CDB: a squared equals CD squared plus DB squared. Substituting: a squared equals b squared sine squared A, plus c squared minus two b c cosine A plus b squared cosine squared A. Gather the two b squared terms: b squared times the bracket sine squared A plus cosine squared A — and that bracket equals exactly 1, by the fundamental identity. What survives is a squared equals b squared plus c squared minus two b c cosine A. Proved.

One special case locks the formula into memory. Set angle A to 90 degrees. Cosine of 90 is zero, the correction vanishes, and the rule shrinks to a squared equals b squared plus c squared — Pythagoras itself. The cosine rule IS Pythagoras extended to every triangle, with a correction that measures how far the angle leans away from 90 degrees.

Pause here — the questions for this section are with you now. They probe the anatomy and the proof: the squared side and the cosine angle must face each other, and the identity is what fuses the b squared terms.

## Subtopic: Finding a Side — Two Sides and the Included Angle

The cosine rule delivers a side when you hold the other two sides and the angle between them. A clean start: in triangle ABC, b is 8 centimetres, c is 3 centimetres, and angle A is 60 degrees. Then a squared equals 64 plus 9, minus two times 8 times 3 times cosine 60. Cosine 60 is a half, so the correction is minus 48 times a half, which is minus 24. So a squared equals 73 minus 24, which is 49, and a is 7 centimetres. The square root is the final move, every time — an answer left as 49 is a sentence without its full stop.

Now the case that trips half the class: an obtuse included angle. In triangle PQR, p is 7 centimetres, r is 8 centimetres, and the included angle Q is 120 degrees. Then q squared equals 49 plus 64, minus two times 7 times 8 times cosine 120. Cosine of 120 degrees is NEGATIVE — exactly minus a half — because 120 lies in the second quadrant. The correction becomes minus 112 times minus a half, which is PLUS 56. Two minuses make a plus, so q squared equals 113 plus 56, which is 169, and q is 13 centimetres.

Read the geometry inside that sign change. An angle wider than 90 degrees shoves the far side out longer than Pythagoras would predict, so the correction adds; an angle tighter than 90 pulls it in shorter, so the correction subtracts. If your obtuse-angle answer arrives SHORTER than the right-angle value — here, shorter than the square root of 113, about 10,6 — a sign was fumbled, usually by typing the minus twice or not at all. Enter the entire right-hand side in one line, cosine in brackets, and let the calculator govern the signs.

Stop for this section's questions now — watch the sign of the cosine, and square root as the closing move.

## Subtopic: Finding an Angle — Three Sides, No Angle

Rearranged for angle-hunting, the rule reads: cosine A equals b squared plus c squared minus a squared, all over two b c. The pattern to hold onto: the angle you are hunting faces the side that gets SUBTRACTED upstairs, while the two sides hugging the angle sit downstairs, doubled.

Worked example. A triangle has sides of 4, 7 and 9 centimetres. Find the largest angle. First decision: the largest angle faces the longest side, so the target is the angle opposite the 9. Call it theta. Cosine theta equals 16 plus 49 minus 81, all over two times 4 times 7. The top is minus 16, the bottom 56, so cosine theta equals minus 0,2857. Inverse cosine delivers theta equal to 106,6 degrees to one decimal.

Notice what the negative cosine announced before any button was pressed: the angle is obtuse. Cosine is positive for acute angles and negative for obtuse ones, so the SIGN of the fraction names the angle's type instantly. And here lies the cosine rule's deep advantage for angles: unlike inverse sine, inverse cosine separates acute from obtuse on its own — no second suspect lurks at 180 minus the answer, because cosine of 180 minus theta carries the OPPOSITE sign rather than the same value. Whenever an angle might be obtuse and three sides are known, the cosine rule is the ambiguity-free instrument. Close with sense checks: 106,6 is the largest angle and faces the largest side, and the finished triangle's three angles must still total 180.

The questions on this section are in front of you now — subtract the square of the side facing your angle, and read the sign of the cosine before pressing inverse.

## Subtopic: Two-Dimensional Problems — Harbours, Bearings and Shared Sides

Story problems in two dimensions follow a fixed discipline: draw, label, name the triangle that holds the question, then let your inventory of known pieces choose the rule.

Worked example. Two boats leave a harbour H at the same moment. Boat one sails on a bearing of 040 degrees for 5 kilometres to point P; boat two sails on a bearing of 105 degrees for 7 kilometres to point Q. The angle P H Q between their courses is the difference of the bearings: 105 minus 40, which is 65 degrees — that subtraction is how bearings turn into triangle angles. First: how far apart are the boats? In triangle H P Q we hold two sides and the included angle — cosine rule territory. P Q squared equals 25 plus 49, minus two times 5 times 7 times cosine 65. That is 74 minus 70 times 0,4226, which is 74 minus 29,58, giving 44,42. So P Q is the square root: 6,66 kilometres.

Second: the angle H P Q — the angle at boat one between the harbour and boat two. Three sides are now known, and a complete pair also exists, so both rules could run. Choose the cosine rule for safety, since the angle at P could conceivably be obtuse. Cosine of P equals 25 plus 44,42 minus 49, all over two times 5 times 6,66. The top is 20,42, the bottom 66,65, so cosine P equals 0,3064, and P equals 72,2 degrees — acute after all. The angle at Q then finishes the triangle at about 42,8 degrees.

The habits that scale to every such story: translate the words into a labelled sketch before touching a formula; announce the triangle you are working in; audit what you hold in THAT triangle — two sides with the included angle summons the cosine rule, a complete opposite pair invites the sine rule; and carry unrounded values forward, rounding only what you report. Many stories hang two triangles on one shared side — solve the first triangle for that side, then walk it into the second triangle as known information.

The final questions of this part are with you now — sketch first, audit what you hold, and let the inventory pick the rule.

# Part 2 — Simplifier

The same rule again — as a corner with attitude, a toolbox inventory, and a bridge between two triangles.

## Subtopic: Pythagoras with an Attitude Adjustment

Two friends leave the same gate along two straight paths — one walks 7 metres, the other 8. How far apart do they finish? Everything depends on the attitude of the corner between the paths. If the corner is a perfect 90 degrees, Pythagoras settles it: 49 plus 64 is 113, square root, about 10,6 metres. But real corners are rarely square.

The cosine rule is Pythagoras with an attitude adjustment. It opens identically — square both paths and add — then it corrects: minus twice the product of the paths, times the cosine of the corner. Corner tighter than 90? Cosine is positive, the correction subtracts, and the friends finish closer than the square-corner answer. Corner wider than 90 — say 120 degrees? Cosine turns negative, minus times minus becomes plus, and the friends finish further apart: 113 plus 56 is 169, and the square root is a full 13 metres. And at exactly 90 the correction is zero — cosine of 90 is nothing — and the rule quietly becomes the Pythagoras you have trusted since grade eight.

That geometry is also your alarm system. A wider corner must mean a longer distance. If a 120-degree corner produces a shorter answer than the square corner would, a minus went missing at the calculator — nearly always from typing the correction term separately. Enter the whole line at once and press equals a single time.

Quick check before we carry on — questions on this are with you right now. Before computing any corner, say it aloud: wider than 90, so further apart; tighter than 90, so closer.

## Subtopic: The Toolbox Question

Every triangle question at this level secretly asks one thing before all else: what do you HOLD? Not what you want — what you hold. Open the toolbox only after the stocktake.

Holding two sides and the angle pinched between them? That is Side-Angle-Side, and only the cosine rule fits — the sine rule stalls, since no known side faces a known angle. Holding all three sides and no angle? Side-Side-Side: cosine rule again, in its rearranged angle-hunting form. Holding a side together with its opposite angle — a complete pair? The sine rule wakes up, and being the lighter tool, it should carry the next side or angle. Wanting an area while holding two sides that embrace an angle? The area rule from last lesson, straight away.

The stocktake even settles ties. When both rules could reach an angle, remember their characters. Inverse sine is the witness who cannot tell twins apart: an acute angle and its 180-minus partner produce identical sines, so a verification is always owed. Inverse cosine identifies the twins on sight, because an obtuse angle stamps a negative sign onto its cosine. So whenever the hunted angle might be obtuse, reach for the cosine rule and the ambiguity never exists.

Speak your stocktake at the top of the written answer — in triangle C A B, two sides and the included angle are known, so the cosine rule applies. Five seconds of writing, a method mark banked, and the wrong formula never gets started.

Your questions for this part are up now — stocktake first, tool second, and give the ambiguous witness no stand.

## Subtopic: One Story, Two Triangles

The longest story questions look monstrous because the picture carries two triangles at once — a cell tower watched from two streets, two boats and a harbour, a plot split by a fence line. The secret is that the two triangles always share exactly one side, and that shared side is the bridge the answer must cross.

The method: solve the FIRST triangle — the one where your stocktake is complete — perhaps two sides and an included angle for the cosine rule, or two angles and a side for the sine rule. What you solve for is the bridge, the shared side. Then cross: inside the second triangle, the bridge now counts as known information, and the second triangle typically falls to one more application of either rule.

In the harbour story, triangle H P Q produced the boats' separation, 6,66 kilometres. If the question now raises a lighthouse visible from both boats, standing on a new triangle built over P Q, you carry 6,66 across the bridge and work the new triangle with it. One warning about the crossing: carry the FULL calculator value, never the rounded 6,66. Rounding at the bridge seeds an error that the second triangle then grows, and the drift costs accuracy marks. Store the exact value in memory, report the rounded one, and compute with the stored one.

Plan the crossing before any arithmetic: circle the shared side on the sketch and note which triangle supplies it and which triangle spends it. Once the bridge is named, a two-triangle monster is only two ordinary questions standing in a queue.

And here come the last questions of the lesson, right now — find the shared side, name the bridge, cross it with the unrounded value, and finish the second triangle like the first.
