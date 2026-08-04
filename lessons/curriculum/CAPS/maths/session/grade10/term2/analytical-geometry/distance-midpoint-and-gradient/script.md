# Part 1 — Expert

Analytical geometry puts the Euclidean shapes onto a grid and replaces reasoning about pictures with arithmetic about coordinates. Three formulae do almost all of it: distance, midpoint and gradient. This session derives each one, works them on a single pair of points so the numbers stay familiar, and then uses all three together to classify a quadrilateral — which is exactly how Paper 2 examines the topic.

## Subtopic: The Plane, the Points, and the Distance Formula

Fix the language first. A point on the Cartesian plane is written as an ordered pair — the x-coordinate first, telling you how far right or left of the origin, then the y-coordinate, telling you how far up or down. The point A, negative three, two, sits three units left of the origin and two units up. The point B, five, eight, sits five right and eight up.

Now the distance between them. There is no new mathematics here — it is Pythagoras, dressed in coordinates. Draw a horizontal line from A and a vertical line down from B; they meet at a corner, and you have a right-angled triangle with AB as its hypotenuse. The horizontal side is the difference in the x-coordinates: five minus negative three, which is five plus three — eight units. Watch that double negative, because it is where most marks go missing. The vertical side is the difference in the y-coordinates: eight minus two — six units.

Pythagoras: AB squared equals eight squared plus six squared — sixty-four plus thirty-six — one hundred. So AB is the square root of one hundred, which is ten units.

Generalise and you have the formula: the distance between two points is the square root of the quantity x-two minus x-one, all squared, plus the quantity y-two minus y-one, all squared. Say it as "the square root of the change in x squared plus the change in y squared".

Two properties save you worry. The order of the points does not matter: negative three minus five is negative eight, and negative eight squared is still sixty-four — squaring destroys the sign, so AB and BA agree, exactly as distance should. And the answer is never negative, because a square root of a sum of squares cannot be.

One discipline on presentation. If the numbers do not give a perfect square, leave the answer as a surd unless a decimal is asked for. The distance from B, five, eight, to C, nine, three, is the square root of four squared plus negative five squared — sixteen plus twenty-five — root forty-one, about six comma four zero units.

Pause here — the questions for this section are with you now. They test the formula, the double-negative subtraction, and why the order of the two points makes no difference.

## Subtopic: The Midpoint Formula

The midpoint of a line segment is the point exactly halfway along it, and finding it is even simpler than finding the distance: you average the coordinates.

The formula: the midpoint of the segment joining x-one, y-one and x-two, y-two is the point whose x-coordinate is x-one plus x-two, all over two, and whose y-coordinate is y-one plus y-two, all over two. In words: add the x's and halve, add the y's and halve.

On our points. A is negative three, two, and B is five, eight. The x-coordinate of the midpoint: negative three plus five is two, halved is one. The y-coordinate: two plus eight is ten, halved is five. So the midpoint M is one, five.

Check it makes sense: one lies between negative three and five, and five lies between two and eight. If your midpoint falls outside the two points, you subtracted where you should have added — the single most common error here, and it comes from confusing midpoint with gradient. Burn the difference in: gradient subtracts, distance subtracts, midpoint is the only one of the three that ADDS.

The formula runs backwards too, and examiners like it that way. Suppose M, one, five, is the midpoint of AB and A is negative three, two — find B. Set each coordinate as an equation. Negative three plus x, all over two, equals one, so negative three plus x equals two, so x equals five. Two plus y, all over two, equals five, so two plus y equals ten, so y equals eight. B is five, eight.

Where midpoint earns its marks: proving that the diagonals of a quadrilateral bisect each other. Two diagonals bisect each other exactly when they share the same midpoint, so compute both and compare.

Stop for this section's questions now — the average of the coordinates, the formula run in reverse to recover a missing endpoint, and the shared-midpoint test for bisecting diagonals.

## Subtopic: Gradient — Steepness, Parallel and Perpendicular

Gradient measures steepness: how much the line rises for every unit it runs across. The formula: gradient equals y-two minus y-one, all over x-two minus x-one — the change in y divided by the change in x. Rise over run.

On A, negative three, two, and B, five, eight: eight minus two is six; five minus negative three is eight. Gradient is six over eight, which simplifies to three over four. Read it aloud as a physical instruction: for every four units across, the line climbs three units up. The discipline that prevents sign errors is to choose an order and keep it — if B's y goes on top, B's x goes underneath. Swap the order in one place only and you flip the sign, turning a rising line into a falling one.

Now the four cases you must be able to name. A positive gradient rises from left to right. A negative gradient falls from left to right. A gradient of zero means a horizontal line — no rise at all, numerator zero. And a vertical line has an UNDEFINED gradient, because the run is zero and division by zero has no meaning. Undefined is not zero; writing "gradient equals zero" for a vertical line loses the mark every time.

Two relationships carry most of the exam questions. Parallel lines have EQUAL gradients. Perpendicular lines have gradients whose PRODUCT is negative one — equivalently, one is the negative reciprocal of the other: flip the fraction, change the sign. Three over four pairs with negative four over three, and their product is negative twelve over twelve, which is negative one. Confirmed. One caution: that test fails for a horizontal and a vertical line, which are certainly perpendicular but have gradients of zero and undefined, and those do not form a product. Handle that pair by inspection.

Gradient also tests collinearity — whether three points lie on one straight line. Take P, one, two; Q, three, six; and R, five, ten. Gradient PQ is four over two, which is two. Gradient QR is four over two, which is two. Equal gradients through the shared point Q, so P, Q and R are collinear.

The questions on this section are in front of you now — rise over run computed consistently, the four cases including undefined, and the parallel and perpendicular conditions applied to real gradients.

## Subtopic: A Quadrilateral on the Grid

Here is the standard Paper 2 question: four vertices are given, and you must decide what kind of quadrilateral they form, proving every claim. All three formulae work together.

The vertices: A, negative three, two; B, five, eight; C, nine, three; D, one, negative three. Taken in that order around the figure.

Start with side lengths. AB we already have: ten units. BC: four squared plus negative five squared — sixteen plus twenty-five — root forty-one. CD: negative eight squared plus negative six squared — sixty-four plus thirty-six — root one hundred, ten units. DA: negative four squared plus five squared — root forty-one again. So AB equals CD, both ten, and BC equals DA, both root forty-one. Both pairs of opposite sides equal — a condition for a parallelogram.

Confirm with gradients. Gradient AB is three over four. Gradient DC: six over eight, which is three over four. Equal, so AB is parallel to DC. Gradient AD: negative five over four. Gradient BC: negative five over four. Equal, so AD is parallel to BC. Both pairs of opposite sides parallel — a parallelogram, proved a second way.

Confirm a third time with the diagonals. Midpoint of AC: negative three plus nine over two, and two plus three over two — three, and two comma five. Midpoint of BD: five plus one over two, and eight plus negative three over two — three, and two comma five. Identical, so the diagonals bisect each other, and the third condition gives the same conclusion.

Now push further, because the examiner will. Is it a rectangle? That needs adjacent sides perpendicular. Multiply gradient AB by gradient AD: three over four times negative five over four is negative fifteen over sixteen. Not negative one, so angle A is not a right angle. Is it a rhombus? That needs all four sides equal, and ten is not root forty-one. The figure is a parallelogram, and nothing more.

The error museum, four exhibits. One: the double negative — five minus negative three is eight, not two. Two: a gradient computed with mismatched order, giving exactly the wrong sign. Three: adding in the distance formula or subtracting in the midpoint formula. Four: claiming a rectangle because the sketch looks like one; on a grid, only the perpendicular product proves a right angle.

The final questions of this part are with you now — the classification carried out with all three formulae, and each conclusion stated with the condition that justifies it.

# Part 2 — Simplifier

Now the same three formulae from a town laid out in blocks — walking, meeting and climbing, which is all these formulae have ever measured.

## Subtopic: Eight Blocks Across, Six Blocks Up

Picture a town with streets in a neat grid, like the older parts of Kimberley or the blocks around a taxi rank. You are standing at your friend's gate. Her cousin's place is eight blocks east and six blocks north.

Walking the streets, you cover eight plus six — fourteen blocks. But suppose there is an open field between you and you can cut straight across. How long is that diagonal?

You already know this from Grade 9, wearing different clothes. Eight across and six up make a right-angled triangle with the diagonal as the long side. Eight squared is sixty-four, six squared is thirty-six, add them for one hundred, square root ten. The shortcut is ten blocks — four blocks shorter than walking around.

That is the entire distance formula. The only thing coordinates add is a way to work out the eight and the six without pacing them off. If the gate sits at negative three, two, and the cousin's place at five, eight, the across-distance is five take away negative three, and taking away a negative means adding, so eight. The up-distance is eight take away two — six. Pythagoras finishes the job.

So the recipe is three moves: find how far across, find how far up, then square both, add, and square root. Nothing more. And direction never matters — whether you walk from the gate to the cousin or back again, the field is the same width. Squaring wipes out any minus sign, so a distance can never come out negative.

Quick check before we carry on — a few questions on the walk are coming to you right now. Work out the across and the up first, then let Pythagoras do the rest.

## Subtopic: Meeting Exactly in the Middle

Two friends want to meet halfway. One lives at house number three on a street, the other at house number eleven. Where do they meet? You do not measure anything — you just average: three plus eleven is fourteen, halved is seven. House number seven.

On a grid you do the same trick twice, once for the across numbers and once for the up numbers. From negative three, two, to five, eight: the across numbers, negative three and five, add to two, halved is one. The up numbers, two and eight, add to ten, halved is five. The meeting point is one, five.

Sanity check it the way you would check a real meeting spot: one sits between negative three and five, and five sits between two and eight. If your answer lands outside the two homes, someone has walked in the wrong direction — and the usual cause is subtracting when you should have added.

That is the one thing worth branding into your memory, because it is the difference between two of the three formulae. To find the middle, you ADD and halve. To find the steepness or the distance, you SUBTRACT. Middle means add. Everything else means take away.

The trick works backwards too, which feels like magic the first time. If the meeting point is one, five, and one friend is at negative three, two, where does the other live? The across numbers must average to one, so negative three plus something equals two — the something is five. The up numbers must average to five, so two plus something equals ten — the something is eight. The other friend is at five, eight. You found a house nobody told you about.

And here is where it earns marks. If two roads cross and each is cut exactly in half at the crossing, both roads have the same middle point. So to prove two diagonals of a shape cut each other in half, work out the middle of each and see whether you get the same pair of numbers. Same answer, and they bisect — which proves the shape is a parallelogram.

Your questions for this part are up now. Add and halve, then look at your answer and ask whether it really sits between the two points.

## Subtopic: Steepness You Can Feel — and the Traps

Last piece: gradient, which is just steepness with a number attached.

Think of the ramp at the entrance to a shopping centre: it rises a little and runs a long way, so it is gentle. Now think of a road up a hill outside Mthatha in first gear — rises a lot, runs a short way, steep. Gradient puts a number on that feeling: how much it goes UP, divided by how much it goes ACROSS. Rise over run.

From negative three, two, to five, eight: up six, across eight. Six over eight tidies up to three over four. Say what that means out loud, because the meaning is the whole point: for every four steps forward, this line climbs three steps up.

Four situations, four answers. Climbing as you go right: positive gradient. Dropping as you go right: negative. Flat, like a soccer field: gradient zero, because it rises nothing. And straight up, like a wall: UNDEFINED, not zero — there is no across at all, and you cannot divide by nothing. Calling a wall's gradient zero is a guaranteed lost mark, so keep flat and wall firmly apart.

Now two facts that carry most of the questions. Two lines are parallel when they have the same steepness — two lanes of the N1 climbing the same hill side by side, never meeting. And two lines are at right angles when you take one gradient, flip it upside down, and change its sign: three over four becomes negative four over three. Multiply them and you get negative one, every time. That negative one is your proof of a right angle, and it is how you show a shape is a rectangle without ever picking up a protractor.

Three habits protect your marks. Subtract in the same order top and bottom — mix the order and your line falls when it should rise. Mind the double negatives: five take away negative three is eight, not two, so write the brackets in and let your own handwriting remind you. And never trust the sketch: our four points looked like a perfect rectangle, but the gradients multiplied to negative fifteen over sixteen instead of negative one, so those corners were not square. The numbers decide, not the drawing.

And here come the last questions of the lesson, right now: rise over run in a consistent order, flat against wall, and parallel against right-angled. Get these three formulae solid and half of Paper 2's coordinate work is already yours.
