# Part 1 — Expert

Analytical geometry so far has been a straight-line story: gradients, midpoints, distances, inclinations. Grade twelve adds the one curved character in the cast — the circle — and then makes the two shake hands, with the tangent line that touches a circle at exactly one point. Four pieces of equipment by the end: the centre-radius equation of a circle, completing the square to unmask a disguised circle, the perpendicularity of radius and tangent, and the full routine for finding a tangent's equation.

## Subtopic: The Circle as a Distance Statement

A circle is not a new formula — it is the old distance formula wearing a promise. Fix a centre point, say a and b, and a radius r. A point x and y lies on the circle exactly when its distance to the centre is r. Write the distance formula and square both sides: x minus a, squared, plus y minus b, squared, equals r squared. That is the equation of every circle in the plane.

Read one fluently: x minus 3, all squared, plus y plus 2, all squared, equals 25. The centre is 3 and minus 2 — note the sign flip, because y plus 2 means y minus negative 2 — and the radius is the square root of 25, which is 5. The two classic misreads are both here: taking the centre as 3 and positive 2, and taking the radius as 25 instead of root 25.

When the centre is the origin, the equation collapses to x squared plus y squared equals r squared. And membership testing is substitution: does the point 6 and 2 lie on our circle? Six minus three is 3, squared is 9; two plus two is 4, squared is 16; and 9 plus 16 is 25. Exactly on the circle. A total under 25 would put the point strictly inside; over 25, outside — the equation is a distance meter, and comparing to r squared prices any point's position.

Pause here — the questions for this section are with you now. Flip the signs for the centre, root the right side for the radius, and substitute to test membership.

## Subtopic: Completing the Square

Exams rarely serve the circle pre-assembled. They hand over x squared plus y squared minus 6 x plus 4 y minus 12 equals 0 and ask for centre and radius. The tool is completing the square, run twice — once on the x terms, once on the y terms.

Group first: x squared minus 6 x, together, and y squared plus 4 y, together, with the loose minus 12 moved across as plus 12. Complete each square: half of minus 6 is minus 3, squared is 9, so x squared minus 6 x becomes x minus 3, all squared, minus 9. Half of 4 is 2, squared is 4, so y squared plus 4 y becomes y plus 2, all squared, minus 4. Assemble: x minus 3 squared, plus y plus 2 squared, equals 12 plus 9 plus 4, which is 25. The disguise falls away: centre 3 and minus 2, radius 5 — the very circle from before.

The bookkeeping rule: whatever is added inside to complete a square must be balanced on the other side. Losing one of those balancing numbers is the classic error, and it silently changes the radius. Check the arithmetic by expanding back, or by testing a known point.

One structural warning: a genuine circle equation has x squared and y squared with EQUAL coefficients and no x y term. If a coefficient sits in front of both squares, divide it out first; if the right side comes out zero or negative after completing the square, the equation describes a single point or nothing at all, and saying so is the answer.

Stop for this section's questions now — group, halve, square, balance both sides, and unmask the centre and radius.

## Subtopic: Radius Meets Tangent at Ninety Degrees

A tangent is a line that touches the circle at exactly one point, the point of tangency. Cut a circle with a random line and you get two crossing points; slide the line outward and the two points merge into one at the moment of touching. The geometric fact that powers every calculation: the radius drawn to the point of tangency is PERPENDICULAR to the tangent. The wheel-and-road picture holds it: a wheel touches a flat road at one point, and the spoke to that point stands square to the road.

Perpendicularity converts to algebra through gradients: two perpendicular lines have gradients that multiply to minus 1. So the tangent's gradient is the negative reciprocal of the radius gradient at the touching point. Radius gradient 4 over 3 forces tangent gradient minus 3 over 4. Radius gradient minus 2 forces tangent gradient a half.

This single fact settles several question types before any heavy algebra. Asked whether a line could be tangent at a given point: compare its gradient with the radius gradient there and check the product is minus 1. Asked for the shortest distance from the centre to a tangent: it is the radius itself, along that perpendicular spoke. Asked how many tangents pass through an external point: two, symmetric about the line joining the point to the centre.

Quick pause — the questions on the radius-tangent relationship are with you now. One touching point, one perpendicular spoke, gradients multiplying to minus 1.

## Subtopic: The Tangent Equation Routine

Everything assembles into one four-step routine. Find the tangent to the circle x minus 3 squared plus y plus 2 squared equals 25, at the point 6 and 2.

Step one: confirm the point sits on the circle — done earlier; 9 plus 16 is 25. Never skip this; a tangent at a point not on the circle is a contradiction, and examiners plant such traps. Step two: the radius gradient, centre 3 and minus 2 to point 6 and 2: change in y is 2 minus negative 2, which is 4; change in x is 6 minus 3, which is 3; gradient 4 over 3. Step three: the tangent gradient is the negative reciprocal, minus 3 over 4. Step four: a line with known gradient through a known point — y minus 2 equals minus 3 over 4, times x minus 6. Expand: y equals minus 3 over 4 x, plus 18 over 4, plus 2, which is y equals minus 3 over 4 x plus 13 over 2.

Certify the answer in seconds: the touching point must satisfy the line — minus 3 over 4 times 6 is minus 4,5, plus 6,5 is 2. Correct.

The origin-centred version runs even faster. Tangent to x squared plus y squared equals 25 at the point 3 and 4: radius gradient 4 over 3 straight from the origin, tangent gradient minus 3 over 4, line y equals minus 3 over 4 x plus 25 over 4. Notice the pattern worth remembering: for origin circles, the tangent at the point x one and y one always has gradient minus x one over y one.

The final questions of this part are with you now — point on circle, radius gradient, negative reciprocal, point-gradient form, and the ten-second certificate.

# Part 2 — Simplifier

Now the same circles and tangents from a goat on a rope and a bicycle wheel — same rules, same answers.

## Subtopic: Every Point the Rope Can Reach

Tie a goat to a peg with a rope of length 5, pulled taut. Walk the goat all the way around: the path it traces is every point at distance exactly 5 from the peg. That path is the circle, and its equation is nothing but the distance formula holding the rope taut: x minus a, squared, plus y minus b, squared, equals 5 squared, where a and b mark the peg.

Read the equation like a farm record. In x minus 3 squared plus y plus 2 squared equals 25, the peg stands at 3 and minus 2 — the signs flip, because the equation records the SUBTRACTION that measures distance, so y plus 2 is really y minus a peg coordinate of minus 2. The rope is root 25, which is 5 — the equation stores the rope SQUARED, so root it before answering.

The equation also answers where any point stands relative to the fence line. Substitute the point 6 and 2: the left side totals exactly 25 — the goat can just reach it, rope taut; it is ON the circle. A total below 25 means inside comfortable reach; above 25, beyond the rope. One substitution, three possible verdicts.

Quick check before we carry on — questions on reading the circle are coming to you right now. Peg from the flipped signs, rope from the square root, and substitute to hear the verdict.

## Subtopic: The Circle in Disguise

Sometimes the record book is a mess: x squared plus y squared minus 6 x plus 4 y minus 12 equals 0. Same farm, same goat — the equation has just been multiplied out and shuffled. Completing the square is the tidy-up that recovers the peg and the rope.

Work like sorting a drawer: x items together, y items together, loose numbers across the equals sign. Then the halving trick, twice. X squared minus 6 x: take half of 6, which is 3, and write x minus 3 squared — but that bundle sneaks in an extra 9, so record the 9 on the other side too. Y squared plus 4 y: half of 4 is 2, write y plus 2 squared, record the extra 4. The right side gathers 12 plus 9 plus 4, which is 25. Peg at 3 and minus 2, rope of 5 — recovered.

The whole skill is honest bookkeeping: every number the squaring sneaks in must be declared across the equals sign. Drop one, and the rope changes length silently — the farm record now describes a different goat. When in doubt, expand the tidy version back out and watch it match the messy original, term for term.

Your questions for this part are up now. Sort, halve, square, and declare every sneaked-in number on both sides.

## Subtopic: Where the Wheel Kisses the Road

A bicycle wheel rolling on a flat tar road touches it at exactly one point. That is a tangent: the road is tangent to the wheel. And look at the spoke running from the hub straight down to the touching point — it stands dead square to the road, 90 degrees exactly. Hub, spoke, road: centre, radius, tangent. The perpendicular spoke is the one geometric fact the whole topic runs on.

In coordinates, perpendicular means gradients multiplying to minus 1: the tangent's gradient is the flipped-and-negated version of the spoke's. Spoke gradient 4 over 3? Road gradient minus 3 over 4. So finding a tangent's equation is a four-stop ride. Stop one: check the touching point really lies on the wheel — substitute it into the circle equation. Stop two: gradient of the spoke, from hub to touching point, using rise over run. Stop three: flip and negate for the road's gradient. Stop four: one line through a known point with a known gradient — the equation writes itself.

For the wheel with hub at 3 and minus 2 touching the point 6 and 2: spoke climbs 4 for every 3 across, road drops 3 for every 4 across, and the road's equation lands at y equals minus 3 over 4 x plus 13 over 2. Final courtesy: substitute the touching point back in, watch it balance, and sign the answer off.

And here come the last questions of the lesson, right now: one kiss point, one square spoke, flip and negate, and let the point-gradient form do the writing.
