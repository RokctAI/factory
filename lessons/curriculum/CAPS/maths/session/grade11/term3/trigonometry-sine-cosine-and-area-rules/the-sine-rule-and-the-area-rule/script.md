# Part 1 — Expert

Until now, trigonometry has lived inside right-angled triangles. This session breaks it out. The area rule and the sine rule work in ANY triangle — no right angle required — and between them they price the area of a farm shaped like a wedge, the distance across a river nobody can swim, and half of Paper Two's trigonometry section. Everything rests on one labelling convention and two formulae, both of which you will prove, because the proofs themselves are examinable.

## Subtopic: Labelling Triangles and the Area Rule

First, the convention the whole topic depends on. In triangle ABC, the capital letters A, B and C name the angles at the three vertices, and the small letters a, b and c name the sides — with small a always opposite capital A, small b opposite capital B, small c opposite capital C. Every formula in this topic assumes that pairing. Mislabel one side and every mark after that line is gone, so make the labelling a deliberate first step, never an afterthought.

Now the area rule. From grade ten, area equals half base times perpendicular height. The problem is that examiners almost never give the perpendicular height. The area rule manufactures it. Take triangle ABC and drop a perpendicular from B onto the side b. That little right-angled triangle at vertex C has hypotenuse a, so the height h equals a sine C. Substitute into the old formula: area equals half times b times a sine C — usually written as half a b sine C.

Read the structure of that formula carefully: two sides, times the sine of the angle BETWEEN them — the included angle. Half a b sine C works because C is wedged between sides a and b. The same pattern gives half b c sine A and half a c sine B. Three versions, one rule: two sides and the included angle.

Worked example. In triangle PQR, PQ is 7 centimetres, QR is 9 centimetres, and the angle at Q is 50 degrees. The two given sides meet at Q, so Q is included, and the rule applies directly: area equals half times 7 times 9 times sine 50 degrees. Half of 63 is 31,5, sine of 50 degrees is 0,7660, and the product is 24,13. The area is 24,13 square centimetres, to two decimal places — and the unit is squared, always, because area lives in square units.

Pause here — the questions for this section are with you now. They test the opposite-side convention and the included angle: check which angle sits between the two given sides before you touch the calculator.

## Subtopic: Proving and Using the Sine Rule

The sine rule falls straight out of the area rule, and the proof is short enough to memorise. The three versions of the area rule all measure the same triangle, so they are all equal: half b c sine A equals half a c sine B equals half a b sine C. Divide every part by half a b c. The first fraction loses b and c, leaving sine A over a. The second loses a and c, leaving sine B over b. The third leaves sine C over c. So sine A over a equals sine B over b equals sine C over c — the sine rule. It can also be written upside down, a over sine A equals b over sine B equals c over sine C, and the upside-down version is the one to use when a SIDE is the unknown, because it puts the unknown on top.

When does it apply? The sine rule connects a side with the angle opposite it. You need one complete opposite pair — a side and its opposite angle both known — plus one more piece. Given two angles and any side, the sine rule finds the remaining sides.

Worked example. In triangle ABC, angle A is 40 degrees, angle B is 65 degrees, and side b is 12 centimetres. Find side a. The complete pair is b with B. Write the rule with the unknown on top: a over sine A equals b over sine B, so a equals 12 times sine 40 degrees, divided by sine 65 degrees. Sine 40 is 0,6428 and sine 65 is 0,9063. Twelve times 0,6428 is 7,7135, and dividing by 0,9063 gives 8,51. Side a is 8,51 centimetres.

One calculator discipline: keep the full value on screen and round only at the final line. Rounding sine 40 to 0,64 before dividing shifts the answer, and accuracy marks go with it.

Stop for this section's questions now — write the complete opposite pair down first, put the unknown on top, and round last.

## Subtopic: Finding Angles with the Sine Rule

To find an angle, flip the rule back so the sines sit on top. In triangle ABC, side a is 10 centimetres, side b is 7 centimetres, and angle A is 42 degrees. Find angle B. Sine B over b equals sine A over a, so sine B equals 7 times sine 42 degrees, divided by 10. Sine 42 is 0,6691, so sine B equals 0,4684. Now the inverse move: B equals inverse sine of 0,4684, which is 27,93 degrees — 27,9 degrees to one decimal. The third angle costs nothing: C equals 180 minus 42 minus 27,93, which is 110,07, so 110,1 degrees.

But there is a subtlety here, and it is worth two marks whenever it appears. The calculator's inverse sine only ever answers with an acute angle, yet sine is also positive in the second quadrant. Sine of 152,07 degrees is ALSO 0,4684, because 152,07 is 180 minus 27,93. So in principle angle B has two candidates: 27,93 degrees and 152,07 degrees. Test the second one against the angle sum: 152,07 plus the given 42 already exceeds 180 degrees, so no triangle can hold it, and it is rejected — with that reason written down. Sometimes, though, the obtuse candidate DOES fit, and then two different triangles satisfy the given information; a full answer presents both.

The habit to build: every time inverse sine produces an angle, compute 180 minus that angle, test whether it survives the angle sum, and state the conclusion either way.

The questions on this section are in front of you now — find the acute answer, test its 180-minus partner, and write the reason for keeping or rejecting it.

## Subtopic: Multi-Step Problems — Chaining the Two Rules

Examination questions rarely ask for one application; they chain them. The strategy is always the same: list what is known, find the complete pairs, and plan a route from given to goal before calculating anything.

Worked example. In triangle ABC, angle A is 52 degrees, angle B is 63 degrees, and side c, the side AB, is 15 centimetres. Find the area of the triangle. Look at what the area rule needs: two sides and the included angle. We have one side and no pair of sides — so the area rule cannot fire yet, and the sine rule must build the missing side first.

Step one: the third angle. C equals 180 minus 52 minus 63, which is 65 degrees. Now c and C form a complete pair. Step two: find side a with the sine rule. a equals 15 times sine 52 degrees over sine 65 degrees. Sine 52 is 0,7880, so the numerator is 11,8202, and dividing by 0,9063 gives 13,04 centimetres. Step three: the area. Sides a and c are now known, and the angle between them is B, which is 63 degrees. Area equals half times 13,04 times 15 times sine 63 degrees. Half of 195,6 is 97,8, sine 63 is 0,8910, and the product is 87,15. The area is 87,15 square centimetres.

Notice the two disciplines that carried that solution. The angle sum of a triangle is a tool, not trivia — it completes pairs for free. And the included angle for the final step was chosen by looking at the sketch, not by guessing: a and c meet at vertex B, so B is the angle between them. Draw the triangle, label it fully, and the route usually announces itself.

The final questions of this part are with you now — find the free angle first, build the missing side, and confirm on your sketch which angle is truly included before the area line.

# Part 2 — Simplifier

Now the same two rules from a street market and a taxi rank — same formulae, same answers, with a picture behind each one.

## Subtopic: The Squashed Gate

Picture a security gate — the trellis kind that concertinas open and closed. Take one parallelogram cell of it, with two arms hinged at a corner. When the arms stand at 90 degrees to each other, the cell traps the biggest possible space. As the gate squashes closed, the arms stay exactly the same length but the space between them shrinks, until fully closed the space is nothing at all.

That is the area rule talking. Half a b sine C says: multiply the two arms, take half, and then multiply by sine of the angle between them — and sine is the squash factor. At 90 degrees, sine is 1, no squash, maximum area, and the formula collapses into the old half base times height. At smaller or bigger angles, sine drops below 1 and the area shrinks with it. At 0 or 180 degrees the arms lie flat, sine is 0, and there is no triangle left.

So when a question gives two sides of a plot of land and the angle where they meet, you do not need any perpendicular height. The two sides and the squash factor between them ARE the area: half, times side, times side, times sine of the wedged-in angle. The only thing that can go wrong is grabbing an angle that is not between the two sides — that is like measuring the squash of a different cell of the gate. Touch the two given sides on your sketch and take the angle where your fingers meet.

Quick check before we carry on — questions on this are with you right now. In each one, ask first: is this angle truly wedged between the two sides I was given?

## Subtopic: Fair Trade at the Triangle Market

Here is the deal every triangle honours: the bigger the angle, the bigger the side facing it. The biggest angle always faces the longest side, the smallest angle faces the shortest side. The sine rule sharpens that from a vague feeling into an exact exchange rate: side over sine of its opposite angle is the SAME number all the way around the triangle. Like a market where the price per kilogram is fixed — bags of different sizes, different totals at the till, but one rate for everybody.

Once you see it as an exchange rate, using it is ordinary shop arithmetic. You need one complete pair — one side together with its opposite angle — to fix the rate. In our example, side b was 12 and its opposite angle B was 65 degrees, so the rate was 12 over sine 65. After that, every other side is bought at the same rate: side a equals sine 40, its own opposite angle, times that rate. Answer: 8,51.

And the writing-down trick that saves errors: put the thing you are hunting on TOP of the fraction. Hunting a side, write sides on top. Hunting an angle, flip it and write sines on top. Then the last line is a multiplication instead of an awkward rearrangement.

One warning from the last section carries a picture too. When you find an angle from its sine, the calculator gives the acute suspect, but there is a second suspect hiding at 180 minus that answer — same sine, completely different angle. Check both against the fact that a triangle's angles must total 180. Usually the second suspect has an alibi problem and gets thrown out; occasionally it fits, and then the question truly has two triangles.

Your questions for this part are up now — fix the rate with the complete pair, buy the missing piece at the same rate, and always interrogate the second suspect.

## Subtopic: Planning the Route Before You Drive

A taxi driver working two towns apart does not start the engine and hope; the route is chosen before the wheels move. Multi-step trigonometry is exactly that. Before any calculating, take stock: which sides do I know, which angles, which pairs are complete, and what does the final formula need?

The area rule is the destination in most of these problems, and its ticket price is fixed: two sides plus the angle between them. If the question hands you two angles and one side, you cannot pay yet. So the route plans itself backwards: the area rule needs a second side, the sine rule builds sides, and the sine rule itself may first need the third angle — which is free, because the three angles always total 180.

That was the whole story of our worked example: 180 minus 52 minus 63 gave the 65, the sine rule turned 15 into a second side of 13,04, and the area rule closed the trip at 87,15 square centimetres. Three legs, planned in reverse, driven forward.

Two habits make the plan reliable. Sketch and label every triangle, even when the question supplies a diagram — YOUR labels, small letters opposite capitals, are what make the formulae safe to use. And at every step, say which rule you are using and why it applies: a complete pair for the sine rule, two sides embracing an angle for the area rule. Markers reward the reason, and writing it forces the check.

And here come the last questions of the lesson, right now — take stock, claim the free angle, plan backwards, then drive the route one rule at a time.
