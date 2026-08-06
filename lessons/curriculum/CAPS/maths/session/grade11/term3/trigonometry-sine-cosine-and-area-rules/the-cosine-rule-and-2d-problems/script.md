# Part 1 — Expert

The sine rule has a blind spot. Give it two sides and the angle between them, or all three sides and no angle at all, and it stalls — no complete opposite pair exists, so the rate cannot be fixed. Those are exactly the situations the cosine rule was built for. This session proves the rule, drills its two directions, and then puts both rules to work on the two-dimensional problems that close every trigonometry section in Paper Two: harbours, bearings and triangles that share a side.

## Subtopic: The Cosine Rule and Where It Comes From

The cosine rule states: a squared equals b squared plus c squared, minus two b c cosine A. Study its anatomy before its proof. On the left sits one side, squared. On the right sit the other two sides, squared and added, then a correction term: minus twice their product times the cosine of the angle OPPOSITE the left-hand side. The side on the left and the angle in the cosine always face each other — that pairing is the rule's signature.

Now the proof. In triangle ABC, drop a perpendicular from C onto side AB, meeting it at D. In the right-angled triangle ACD, the height CD equals b sine A, and the base AD equals b cosine A. The rest of AB is DB, which equals c minus b cosine A. Now apply Pythagoras in triangle CDB: a squared equals CD squared plus DB squared. Substitute: a squared equals b squared sine squared A, plus c squared minus two b c cosine A plus b squared cosine squared A. Group the two b squared terms: b squared times sine squared A plus cosine squared A — and that bracket is exactly 1, by the identity from term one. What remains is a squared equals b squared plus c squared minus two b c cosine A. Proved.

One observation cements the formula. Let angle A be 90 degrees. Cosine of 90 is zero, the correction term dies, and the rule collapses into a squared equals b squared plus c squared — Pythagoras. The cosine rule IS Pythagoras, generalised to every triangle, with a correction term that measures how far the angle strays from 90 degrees.

Pause here — the questions for this section are with you now. They probe the anatomy and the proof: the squared side and the cosine angle must face each other, and the identity is what makes the b squared terms merge.

## Subtopic: Finding a Side — Two Sides and the Included Angle

The cosine rule finds a side when you hold the other two sides and the angle between them. Start clean. In triangle ABC, b is 8 centimetres, c is 5 centimetres, and angle A is 60 degrees. Then a squared equals 64 plus 25, minus two times 8 times 5 times cosine 60. Cosine 60 is a half, so the correction term is minus 80 times a half, which is minus 40. So a squared equals 89 minus 40, which is 49, and a is 7 centimetres. Square root at the end, always — leaving the answer as 49 is an unfinished sentence.

Now the case that catches half the class: an obtuse included angle. In triangle PQR, p is 6 centimetres, r is 9 centimetres, and the included angle Q is 110 degrees. Then q squared equals 36 plus 81, minus two times 6 times 9 times cosine 110. Cosine of 110 degrees is NEGATIVE — minus 0,3420 — because 110 lives in the second quadrant. So the correction term is minus 108 times minus 0,3420, which is PLUS 36,94. The two minuses become a plus, and q squared equals 117 plus 36,94, which is 153,94. Square rooting gives q equal to 12,41 centimetres.

Read the geometry in that sign change. An angle beyond 90 degrees pushes the far side longer than Pythagoras would predict, so the correction adds; an angle under 90 pulls it shorter, so the correction subtracts. If your obtuse-angle answer comes out SHORTER than the Pythagoras value, the sign was mishandled — usually by typing the minus into the calculator twice or not at all. Type the whole right-hand side in one go, brackets around the cosine, and let the machine manage the signs.

Stop for this section's questions now — watch the sign of the cosine, and square root as the final move.

## Subtopic: Finding an Angle — Three Sides, No Angle

Rearrange the rule to hunt angles: cosine A equals b squared plus c squared minus a squared, all over two b c. The pattern to memorise: the angle you want sits opposite the side that gets SUBTRACTED on top, and the two sides that embrace the angle sit downstairs, doubled.

Worked example. A triangle has sides of 5, 7 and 10 centimetres. Find the largest angle. First decision: the largest angle faces the longest side, so we want the angle opposite the 10. Call it theta. Cosine theta equals 25 plus 49 minus 100, all over two times 5 times 7. The top is minus 26, the bottom is 70, so cosine theta equals minus 0,3714. Inverse cosine gives theta equal to 111,80 degrees — 111,8 to one decimal.

Notice what the negative cosine did: it announced the obtuse angle before the inverse button was ever pressed. Cosine is positive for acute angles and negative for obtuse ones, so the SIGN of the fraction tells you the type of angle immediately. And this is the deep advantage of the cosine rule for angles: unlike inverse sine, inverse cosine distinguishes acute from obtuse on its own — there is no second suspect at 180 minus the answer, because cosine of 180 minus theta has the OPPOSITE sign, not the same value. When an angle might be obtuse and you have all three sides, the cosine rule is the ambiguity-free tool. Check the answer against sense: 111,8 is the biggest angle and faces the biggest side, and the three angles of any triangle you finish should still total 180.

The questions on this section are in front of you now — subtract the square of the side facing your angle, and read the sign of the cosine before pressing inverse.

## Subtopic: Two-Dimensional Problems — Harbours, Bearings and Shared Sides

Examination two-dimensional problems tell a story, and the method is fixed: draw, label, identify which triangle holds the question, then let the given information choose the rule.

Worked example. Two boats leave a harbour H at the same time. Boat one sails 4 kilometres to point P; boat two sails 6 kilometres to point Q. The angle P H Q between their courses is 70 degrees. First: how far apart are the boats? In triangle H P Q we hold two sides and the included angle — cosine rule territory. P Q squared equals 16 plus 36, minus two times 4 times 6 times cosine 70. That is 52 minus 48 times 0,3420, which is 52 minus 16,42, giving 35,58. So P Q is the square root, 5,97 kilometres.

Second: the angle H P Q, the angle at boat one between the harbour and boat two. Now three sides are known, or alternatively a complete pair exists — both rules could run. Choose the cosine rule for safety, since the angle at P could conceivably be obtuse. Cosine of P equals 16 plus 35,58 minus 36, all over two times 4 times 5,97. The top is 15,58, the bottom 47,76, so cosine P equals 0,3262, and P equals 70,96 degrees — about 71 degrees, acute after all, and the angle at Q must then be about 39 degrees to complete 180.

The habits that scale to every such problem: convert the story into a labelled sketch before any formula; name the triangle you are working in; count what you hold in THAT triangle — two sides plus included angle demands the cosine rule, a complete opposite pair invites the sine rule; and carry unrounded values forward, rounding only what you report. Many stories hang two triangles on one shared side — solve the first triangle for the shared side, then walk it into the second triangle as known information.

The final questions of this part are with you now — sketch first, count what you hold, and let the inventory pick the rule.

# Part 2 — Simplifier

Now the same rule from a shortcut across a field and a taxi rank inventory — same formulae, same answers, with a picture for each move.

## Subtopic: Pythagoras with an Attitude Adjustment

Two friends walk from the same corner along two straight paths — one walks 8 metres, the other 5. How far apart do they end up? It depends entirely on the attitude of the paths — the angle at the corner. If the corner is exactly 90 degrees, Pythagoras answers: 64 plus 25, square root, done. But corners in real fields are rarely square.

The cosine rule is Pythagoras with an adjustment for attitude. It starts exactly the same — square the two paths and add — and then corrects: minus twice the product of the paths, times cosine of the corner. Corner tighter than 90 degrees? Cosine is positive, the correction subtracts, the friends end up closer than the square-corner answer. Corner wider than 90? Cosine goes negative, the two minuses become a plus, and the friends end up further apart than Pythagoras would say. And at exactly 90 the correction is zero — cosine of 90 is nothing at all — and the rule quietly becomes the Pythagoras you have used since grade eight.

That is also your error alarm. Wide corner must mean longer distance. If you compute a 110-degree corner and get a shorter answer than the 90-degree version would give, a minus sign got lost at the calculator, almost always by typing the correction term separately. Type the whole line in one go and press equals once.

Quick check before we carry on — questions on this are with you right now. For each corner, first say out loud: wider than 90, so further apart, or tighter than 90, so closer.

## Subtopic: The Toolbox Question

Every triangle question at this level is really asking one thing first: what do you hold? Not what do you want — what do you HOLD. Open the toolbox only after the inventory.

Hold two sides and the angle squeezed between them? That is Side-Angle-Side, and only the cosine rule fits — the sine rule stalls because no side faces a known angle. Hold all three sides and no angle? Side-Side-Side, cosine rule again, in its rearranged angle-hunting form. Hold a side with its opposite angle — a complete pair? The sine rule is awake, and it is the lighter tool: use it for the next side or angle. Want an area and hold two sides embracing an angle? The area rule from last lesson, directly.

The inventory even breaks ties. When both rules could find an angle, remember their characters. Inverse sine is the witness who cannot tell twins apart: an acute angle and its 180-minus partner give identical sines, so a check is always owed. Inverse cosine tells them apart instantly, because obtuse angles carry a negative sign into the cosine. So when the angle you are hunting might be obtuse, prefer the cosine rule and skip the ambiguity entirely.

Say the inventory in words at the start of your written answer — in triangle H P Q, two sides and the included angle are known, so the cosine rule applies. That sentence costs five seconds, earns the method mark, and stops the wrong formula before it starts.

Your questions for this part are up now — inventory first, tool second, and give the ambiguous witness no chance.

## Subtopic: One Story, Two Triangles

The longest questions in the paper look frightening because the picture holds two triangles at once — a cell tower seen from two streets, two boats and a harbour, a field split by a fence. The trick is that the two triangles always share one side, and that shared side is the bridge the answer walks across.

The method: solve the FIRST triangle, the one where you hold enough — perhaps two sides and an included angle, cosine rule, or two angles and a side, sine rule. What you solve for is the bridge, the shared side. Then cross over: in the second triangle the bridge is now known information, and the second triangle usually surrenders to one more application of either rule.

In the harbour story, triangle H P Q gave the distance between the boats, 5,97 kilometres. If the question then adds a lighthouse and a new triangle standing on the side P Q, you carry 5,97 across the bridge and work the new triangle with it. One warning about the crossing: carry the FULL calculator value across, not the rounded 5,97. Rounding at the bridge poisons every number in the second triangle, and examiners deduct for the drift. Store the exact value in calculator memory, report the rounded one, and calculate with the stored one.

Plan the crossing before you compute anything: circle the shared side on your sketch and write which triangle gives it and which triangle needs it. Once the bridge is named, a two-triangle monster is just two ordinary questions in a queue.

And here come the last questions of the lesson, right now — find the shared side, name the bridge, cross it with the unrounded value, and finish the second triangle like the first.
