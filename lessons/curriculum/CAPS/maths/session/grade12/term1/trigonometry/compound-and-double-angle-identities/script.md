# Part 1 — Expert

Grade eleven trigonometry ended with reduction formulae and general solutions. Grade twelve adds the last major tools of the identity toolbox: formulae for the sine and cosine of a SUM or DIFFERENCE of two angles, and their most famous special case, the double angle. Four pieces of equipment by the end: the four compound-angle identities, the technique of exact values without a calculator, the double-angle identities including the three faces of cos of 2 alpha, and the use of double angles inside proofs and equations.

## Subtopic: The Compound-Angle Identities

First, a warning shot. Sine of a sum is NOT the sum of the sines. Test it: sine of 90 degrees is 1, but sine of 60 degrees plus sine of 30 degrees is about 0,87 plus 0,5, which is 1,37. Distributing a trig function over a plus sign is the single most punished error in this topic. The true expansions are richer.

Here they are, spoken carefully. Sine of alpha plus beta equals sine alpha cos beta plus cos alpha sine beta. Sine of alpha minus beta equals sine alpha cos beta minus cos alpha sine beta. Cosine of alpha plus beta equals cos alpha cos beta MINUS sine alpha sine beta. Cosine of alpha minus beta equals cos alpha cos beta PLUS sine alpha sine beta.

Two patterns carry all four. For sine, the functions mix — sine cos, cos sine — and the sign in the middle matches the sign in the bracket. For cosine, the functions stay in pairs — cos cos, sine sine — and the sign FLIPS: a plus in the bracket gives a minus between the terms. In the CAPS scheme, cosine of alpha minus beta is the parent identity, derived from the distance formula on the unit circle, and the other three follow by substituting minus beta or using co-functions. Know that derivation exists; know the four results cold.

Pause here — the questions for this section are with you now. Sine mixes and keeps the sign; cosine pairs up and flips it.

## Subtopic: Exact Values Without a Calculator

The first job of the compound identities is manufacturing exact values for angles that are not special, out of angles that are. The special angles 30, 45 and 60 degrees carry known values: sine of 30 is a half, cos of 30 is root 3 over 2, sine and cos of 45 are both root 2 over 2, sine of 60 is root 3 over 2, cos of 60 is a half.

Now take 15 degrees, which is 45 minus 30. Cosine of 15 equals cos 45 cos 30 plus sine 45 sine 30. Substitute: root 2 over 2, times root 3 over 2, plus root 2 over 2, times a half. That is root 6 over 4 plus root 2 over 4, giving root 6 plus root 2, all over 4. As a decimal that is about 0,97, and the calculator agrees — but the exam wants the surd form, and the identity is the only road there.

The same machine handles 75 degrees, which is 45 plus 30. Sine of 75 equals sine 45 cos 30 plus cos 45 sine 30, which gives the identical surd, root 6 plus root 2 over 4 — no coincidence, since sine of 75 and cos of 15 are co-functions of complementary angles. Questions also run this backwards: recognise sine 40 cos 10 minus cos 40 sine 10 as the expansion of sine of 40 minus 10, which is sine 30, which is a half. Compressing an expansion back into a single sine or cosine is worth as many marks as expanding.

Stop for this section's questions now — split the awkward angle into two special ones, expand, substitute the known surds, and be ready to run the identities in reverse.

## Subtopic: Double Angles and the Three Faces of cos 2 Alpha

Set beta equal to alpha in the sum identities and the double angles fall out. Sine of 2 alpha equals 2 sine alpha cos alpha. Cosine of 2 alpha equals cos squared alpha minus sine squared alpha — and this one has two further costumes, courtesy of the Pythagorean identity sine squared plus cos squared equals 1. Replace sine squared: cos of 2 alpha equals 2 cos squared alpha minus 1. Replace cos squared: cos of 2 alpha equals 1 minus 2 sine squared alpha. Three faces, one identity, and choosing the convenient face is the actual skill.

Worked case. Given sine alpha equals 3 over 5, with alpha between 90 and 180 degrees, find sine of 2 alpha and cos of 2 alpha. First recover cos alpha: from the Pythagorean identity, cos squared alpha is 1 minus 9 over 25, which is 16 over 25, so cos alpha is plus or minus 4 over 5 — and in the second quadrant cosine is negative, so cos alpha equals minus 4 over 5. Draw the triangle in the correct quadrant if that sign call feels shaky. Now sine of 2 alpha is 2 times 3 over 5 times minus 4 over 5, which is minus 24 over 25. And cos of 2 alpha, using the face that needs only sine, is 1 minus 2 times 9 over 25, which is 7 over 25. Notice the checks: both results are legal values between minus 1 and 1, and since sine 2 alpha is negative while cos 2 alpha is positive, the angle 2 alpha lands in the fourth quadrant — consistent with alpha being just over 90 degrees.

Quick pause — the questions on double angles are with you now. Two sine cos for sine; pick the face of cos 2 alpha that matches the information you hold.

## Subtopic: Double Angles in Identities and Equations

Proving identities is assembling faces. Prove that 1 minus cos 2 alpha, over sine 2 alpha, equals tan alpha. Work the left side: choose the face 1 minus 2 sine squared alpha for cos 2 alpha, so the numerator becomes 1 minus 1 plus 2 sine squared alpha, which is 2 sine squared alpha. The denominator is 2 sine alpha cos alpha. Divide: sine alpha over cos alpha, which is tan alpha. The face was chosen so the 1 would cancel — that is the strategy in almost every such proof: pick the face of cos 2 alpha that kills the constant or matches the squared function present.

Equations follow the same logic. Solve cos 2 x plus sine x equals 0 for x in 0 to 360 degrees. A double and a single angle cannot talk to each other, so convert the double: choose 1 minus 2 sine squared x, since the other term is a sine. The equation becomes 1 minus 2 sine squared x plus sine x equals 0, and multiplying through by minus 1: 2 sine squared x minus sine x minus 1 equals 0. Factorise like a quadratic in sine x: 2 sine x plus 1, times sine x minus 1, equals 0. So sine x equals minus a half, or sine x equals 1. Sine x equals 1 gives x equals 90 degrees. Sine x equals minus a half is negative in quadrants three and four, reference angle 30 degrees: x equals 210 degrees or 330 degrees. Three solutions: 90, 210 and 330. Substitute one back to certify: at 210 degrees, cos of 420 equals cos of 60, a half, and sine of 210 is minus a half — sum zero. Correct.

The final questions of this part are with you now — convert the double angle to match the single one, factorise the quadratic, and solve each simple equation in its quadrants.

# Part 2 — Simplifier

Now the same identities from ladders, ramps and a folded piece of paper — same rules, same answers.

## Subtopic: Why the Shortcut Fails

Here is the tempting shortcut: sine of 60 plus 30 should surely be sine 60 plus sine 30. Try it with real numbers. Sine of 90 is exactly 1. Sine 60 plus sine 30 is roughly 0,87 plus 0,5 — about 1,37. Not close. The shortcut overshoots, and here is the picture of why: angles combine by rotation, not by stacking rulers. Tilting a ramp by 30 degrees and then by another 30 does not double its height gain — the second tilt starts from an already-tilted position, so part of its effort goes sideways.

The genuine expansions respect that geometry. Sine of a sum is a blend of BOTH functions of BOTH angles: sine alpha cos beta plus cos alpha sine beta — each angle contributes its sine, scaled by how upright the other angle leaves things, which is its cosine. Cosine of a sum pairs the functions instead — cos cos minus sine sine — and carries a sign flip: rotating further can only erode the horizontal reach, so a plus inside becomes a minus outside.

Two memory hooks and no more. Sine mixes the functions and keeps the bracket's sign. Cosine pairs the functions and flips it.

Quick check before we carry on — questions on the expansions are coming to you right now. Never distribute over the bracket; blend for sine, pair and flip for cosine.

## Subtopic: Making 15 Degrees From Scratch

The angles 30, 45 and 60 are old friends with exact surd values. But a question asks for cos of 15 degrees, exactly — no decimals. The move: build 15 from friends. Fifteen is 45 minus 30, so cos 15 is cos of 45 minus 30, and the difference identity opens it up: cos 45 cos 30 plus sine 45 sine 30.

Now it is a substitution exercise with surds. Root 2 over 2 times root 3 over 2 gives root 6 over 4. Root 2 over 2 times a half gives root 2 over 4. Add: root 6 plus root 2, all over 4. That expression IS cos 15 — exact, calculator-free, and worth full marks where 0,97 earns none. The construction is like mixing paint: you cannot buy fifteen-degree paint, but the shop stocks 45 and 30, and the identity is the recipe for combining them.

The reverse skill matters just as much: recognising a finished mixture. Meet sine 40 cos 10 minus cos 40 sine 10 in an exam and read it as a recipe already written out — it is exactly sine of 40 minus 10, which is sine 30, which is a half. Spotting that a four-term surd expression collapses to a single special angle turns a messy-looking question into one line.

Your questions for this part are up now. Split the strange angle into two friendly ones, follow the recipe, and learn to read a recipe backwards.

## Subtopic: One Angle, Folded Double

Set both angles in the sum identities to the same alpha and the compound formulae fold into the double-angle formulae. Sine of 2 alpha is 2 sine alpha cos alpha — the two identical terms of the blend merge. Cosine of 2 alpha is cos squared minus sine squared — and because sine squared plus cos squared is always 1, this one face can be rewritten twice: 2 cos squared alpha minus 1, or 1 minus 2 sine squared alpha. Think of one actor with three costumes: same identity underneath, dressed for different scenes.

Which costume? Match the scene. Holding only sine alpha — say sine alpha is 3 over 5 in the second quadrant? For cos 2 alpha, wear 1 minus 2 sine squared: 1 minus 18 over 25 is 7 over 25, no cosine needed. For sine 2 alpha there is no avoiding cos alpha, so fetch it from the Pythagorean identity — 16 over 25, square root, and CHOOSE the sign by quadrant: second quadrant, cosine negative, minus 4 over 5. Then sine 2 alpha is minus 24 over 25.

In equations, the costume is chosen to match the other term on stage. Cos 2 x plus sine x equals zero: the other term is a sine, so cos 2 x wears 1 minus 2 sine squared x, and the whole equation becomes a quadratic in sine x — factorise, solve sine x equals 1 or minus a half, and read the quadrants: 90, 210, 330 degrees. The double angle never fights the single angle; it changes costume to join it.

And here come the last questions of the lesson, right now: fold the compound identities to get the doubles, keep all three faces of cos 2 alpha ready, and dress the double angle to match whatever stands beside it.
