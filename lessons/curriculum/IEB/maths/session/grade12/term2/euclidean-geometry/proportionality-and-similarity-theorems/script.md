# Part 1 — Expert

Last year's geometry lived inside the circle. This year steps outside and studies shape itself: when are two triangles the same shape at different sizes, and what does a parallel line do to the sides of a triangle it crosses? Four pillars hold up the topic: the proportionality theorem with its area-based proof, the craft of using it in numbered figures, the two similarity theorems, and the crowning application — a proof of the Theorem of Pythagoras built from nothing but similar triangles.

## Subtopic: The Proportionality Theorem and Its Proof

Begin with the statement. A line drawn parallel to one side of a triangle, cutting the other two sides, divides those sides proportionally. Hold the standard figure in your head: triangle A B C, with D a point on side A B and E a point on side A C, and the line D E parallel to B C. The claim: A D over D B equals A E over E C.

The proof is examinable, and it rests on one modest fact: a triangle's area is half base times height, so two triangles sharing the SAME height have areas in the ratio of their bases. The construction is two lines: join B to E, and join C to D. First comparison: triangle A D E against triangle B D E. Viewing A D and D B as their bases, both triangles use the identical height from E perpendicular to the line A B, so area A D E over area B D E equals A D over D B. Second comparison: triangle A D E against triangle C E D. With bases A E and E C they share the height from D to the line A C, so area A D E over area C E D equals A E over E C. Now the pivot of the whole proof: triangles B D E and C E D have EQUAL areas. Both stand on the same base D E, and their apexes B and C lie on a line parallel to D E — and parallel lines keep a constant distance, so the two heights match on the shared base. Equal denominators below, the very same triangle above: A D over D B equals A E over E C. Complete.

The converse is equally serviceable: a line dividing two sides of a triangle proportionally must be parallel to the third side. And the midpoint theorem you met in grade ten is simply the special case where the ratio is one to one.

Pause here — the questions for this section are with you now. Same height means areas as bases, same base between parallels means equal areas, and the ratio statement drops out.

## Subtopic: Working with Ratios in Figures

Knowing a theorem and swinging it accurately under time pressure are two different muscles, so this section is technique. First: the theorem issues its ratios in several equivalent costumes. From A D over D B equals A E over E C you may equally write A D over A B equals A E over A C — when parts are proportional, each part is proportional to its own whole. Pick the costume holding three known lengths and one unknown.

Worked case. In triangle A B C with D E parallel to B C: A D is 8, D B is 6, A E is 12, find E C. Write A D over D B equals A E over E C: eight over six equals twelve over E C. Cross-multiply: eight E C equals seventy-two, so E C is 9. Then run the whole-side check: A B is 14 and A C is 21, and eight over fourteen equals twelve over twenty-one — both reduce to four sevenths. Consistent.

Second: guard against mixing a part with a whole. Eight over six is part-to-part; twelve over twenty-one is part-to-whole. Setting them equal is the single most common error in the topic. Before writing any equation, name each segment aloud — part or whole — and keep the same pattern on both sides of the equals sign.

Third: parallels can strike twice. When one parallel line cuts two different transversals, apply the theorem inside each triangle separately, then connect the two results through the segment they share. And when the task reads, prove that D E is parallel to B C, deploy the converse: compute both ratios, show they agree, and conclude parallelism — reason stated as, line divides two sides of a triangle in proportion.

Stop for this section's questions now — part with part, wholes for the check, and the converse whenever parallelism itself is the thing to prove.

## Subtopic: Equiangular Triangles Are Similar

Two triangles are similar when they carry the same shape: every pair of matching angles equal, every pair of matching sides in one shared ratio. Triangles hold a privilege no other polygon has: for them, either condition compels the other. Two rectangles — one square-ish, one long and thin — have all angles equal with no shared side ratio, but triangles permit no such loophole.

Theorem one: if two triangles are equiangular, their matching sides are in proportion, and the triangles are similar. The proof works by transplant. Given triangle A B C and triangle D E F with angle A equal to angle D, angle B equal to angle E, and angle C equal to angle F, mark the point H on A B so that A H equals D E, and the point K on A C so that A K equals D F. Triangles A H K and D E F are congruent — side angle side, hinging on the equal angles at A and D. Hence angle A H K equals angle E, which equals angle B. But angle A H K and angle B are corresponding angles for the lines H K and B C, forcing H K parallel to B C. The proportionality theorem now takes over: A H over A B equals A K over A C. Substitute the transplanted lengths: D E over A B equals D F over A C. Rerun the argument from a second vertex and all three ratios fall into line. Equal angles have manufactured proportional sides.

Theorem two is the converse: if the three pairs of matching sides are in proportion, the triangles are equiangular and hence similar. Together they mean a single test settles similarity — angles alone, or sides alone; never both required.

Notation is where the marks hide. Writing triangle A B C similar to triangle D E F declares the pairing: A with D, B with E, C with F — the ORDER is the mathematics. Every ratio then reads directly off the ordered letters: A B over D E equals B C over E F equals A C over D F. Scrambled letters generate scrambled ratios and vanished marks, so pair the equal angles first, then write the vertices in that pairing's order.

The questions on this section are in front of you now — two equal angle pairs make triangles equiangular, order the letters by the equal angles, and read every ratio from the ordering.

## Subtopic: Pythagoras by Similar Triangles

The most ancient theorem in the syllabus, proved this year with its newest machinery. Take triangle A B C, right-angled at A, and drop the altitude from A onto the hypotenuse, meeting B C at D. That single altitude slices the big triangle into two smaller ones — and the decisive claim is that each small triangle is similar to the original.

Compare triangle A B D with triangle C B A. Each holds a right angle — at D in the small one, at A in the large one — and both contain the angle at B. Two pairs of angles equal, so the third pair is automatic: equiangular, therefore similar. Read the ratio off the ordered letters, hypotenuse over the side opposite the shared angle: A B over C B equals B D over B A. Cross-multiplying: A B squared equals B D times B C. Mirror the argument on the far side — triangle A C D against triangle B C A, sharing the angle at C — and it yields A C squared equals C D times C B.

Add the two conclusions. A B squared plus A C squared equals B D times B C, plus C D times B C. Factor out B C: it equals B C times the quantity B D plus D C. And B D plus D C is precisely B C, the full hypotenuse. Therefore A B squared plus A C squared equals B C squared. Pythagoras, assembled entirely from similarity.

The two stepping stones earn questions in their own right: A B squared equals B D times B C says each leg squared equals the hypotenuse times that leg's projection onto it. A third relation, proved the same way, measures the altitude: A D squared equals B D times D C. Numeric versions appear often: with B D equal to 9 and D C equal to 16, A D squared is one hundred and forty-four, so the altitude is 12.

The final questions of this part are with you now — right angle plus shared angle makes each small triangle similar to the whole, squares arise from cross-multiplied ratios, and the two projections rejoin into the hypotenuse.

# Part 2 — Simplifier

Now the same theorems from ladders, photographs and a folded corner — same statements, same proofs, hung on pictures you can hold.

## Subtopic: The Ladder Against the Wall

Prop a ladder against a wall on a sunny afternoon and watch its shadow stretch along the ground. The sun's rays sweep past every rung along parallel lines. The rung a quarter of the way up the ladder throws its mark a quarter of the way along the shadow; the rung two thirds up marks two thirds along. Parallel rays play no favourites — whatever fraction of the ladder you have climbed, exactly that fraction of the shadow lies behind you. That is the proportionality theorem in working clothes: a line parallel to one side of a triangle divides the other two sides in the same ratio.

Why is it inescapable? The lesson's proof runs on areas, and its core fits into one sentence: two triangles standing on the same base, with their tips on one line parallel to that base, enclose the same area — same floor, same ceiling height, same room inside. With those two helper triangles equal, the two upstairs ratios have no choice but to agree.

Applying the theorem is a matter of honest matching. Cut the ladder at a rung: upper piece to lower piece must equal upper shadow to lower shadow. Part against part, whole against whole — never eight over six on one side and twelve over twenty-one on the other, because the first is part-to-part and the second part-to-whole. Announce what each length is before building the fraction, and the topic's favourite mark-eater starves.

Quick check before we carry on — questions on the parallel cut are coming to you right now. Same fraction up the ladder as along the shadow, and match like with like.

## Subtopic: The Photograph and Its Enlargement

Photograph a triangle and print an enlargement. Every angle survives untouched — enlarging turns nothing — while every side stretches by one common factor. That pair of properties IS similarity: same shape, equal angles, sides in a single shared ratio. Today's theorem promises something stronger, and only triangles can promise it: match the angles of two triangles, and the sides are ALREADY in proportion. No second check needed; for triangles, equal angles guarantee the enlargement factor exists.

The proof is a photocopier manoeuvre. Given two equiangular triangles, copy the small one into a corner of the big one: mark the small triangle's side lengths along two edges of the big triangle and join the marks. The joining line runs parallel to the third side — the equal corresponding angles insist on it — and the ladder theorem from the previous section immediately hands over the matching ratios. Each theorem stands on the one before: that is the architecture of this whole topic.

Similarity fills ordinary life. A streetlight and a passer-by: pole and its shadow make one triangle, person and theirs another, with equal angles at the ground because light travels straight. If a person one comma eight metres tall throws a shadow of two comma four metres while the pole throws eight metres, the pole stands six metres — the ratio one comma eight to two comma four, applied to eight. Every map scale, architect's model and zoomed image is this theorem earning its keep.

One expert discipline survives even in the picture world: list matching corners in matching ORDER. Person, feet, shadow-tip against pole, base, shadow-tip, and every ratio reads straight off the letters. Scramble the order and the ratios start lying.

Your questions for this part are up now. Equal angles mean an enlargement factor exists, extract it from one known pair, and keep the corners in matching order.

## Subtopic: The Folded Corner — Pythagoras Rebuilt

Now the most celebrated theorem in mathematics, rebuilt with the photograph idea. Take a right-angled triangle and drop a line from the right angle perpendicularly onto the longest side — like folding that corner flat against the hypotenuse. The fold splits the big triangle into two smaller ones, and each small one is a photograph of the whole. Inspect the left-hand piece: it owns a right angle where the fold meets the hypotenuse, and it shares one of the big triangle's corner angles. Two matching angles — the enlargement guarantee from the previous section — so small and large are the same shape.

Same shape delivers matching ratios, and a single cross-multiplication converts a ratio into a square: the left leg squared equals the whole hypotenuse times the piece of hypotenuse lying beneath that leg. The right-hand piece tells the mirrored story: right leg squared equals hypotenuse times the remaining piece. Add the two stories together. Leg squared plus leg squared equals hypotenuse times one piece, plus hypotenuse times the other — and the two pieces, side by side, ARE the hypotenuse. Legs squared, summed, equal hypotenuse squared. Pythagoras, born of two photographs and one addition.

A bonus waits at the crease. The fold itself satisfies: fold squared equals the product of the two hypotenuse pieces. Pieces of 9 and 16 give a fold of 12 — the number whose square is one hundred and forty-four. Surveyors once exploited exactly this relation to raise a true perpendicular from a measured baseline.

And here come the last questions of the lesson, right now: each small triangle is a photograph of the whole, each leg squared is hypotenuse times its own piece, and the two pieces reassemble into the hypotenuse to close the proof.
