# Part 1 — Expert

Analytical geometry takes the shapes you have been reasoning about with theorems and drops them onto a coordinate grid, so that every geometric claim becomes a calculation you can check. Three tools carry nearly the whole topic: the distance formula, the midpoint formula and the gradient. This session builds each one from first principles, practises all three on one fixed pair of points so the arithmetic becomes familiar, and then combines them to classify a quadrilateral with full justification — the skill the whole topic is really testing.

## Subtopic: The Plane, the Points, and the Distance Formula

Start with the language. A point on the Cartesian plane is an ordered pair: the x-coordinate first, measuring right or left of the origin, then the y-coordinate, measuring up or down. Our anchor points for today: A at negative one, three — one unit left, three up. And B at five, eleven — five right, eleven up.

How far apart are they? Nothing new is needed — this is the theorem of Pythagoras wearing coordinates. Run a horizontal line from A and drop a vertical line from B; they meet at a right angle, and the segment AB becomes the hypotenuse of a right-angled triangle. The horizontal leg is the difference in x-coordinates: five minus negative one. Minus a negative becomes plus, so that is five plus one — six units. That double negative is the single biggest source of lost marks in this topic, so slow down every time you see one. The vertical leg is the difference in y-coordinates: eleven minus three — eight units.

Now Pythagoras. AB squared equals six squared plus eight squared — thirty-six plus sixty-four — one hundred. AB is the square root of one hundred: ten units.

Written in general symbols, the distance between two points is the square root of the quantity x-two minus x-one, all squared, plus the quantity y-two minus y-one, all squared. In words: the square root of the change in x squared plus the change in y squared.

Two reassurances. First, the order of the points is irrelevant: negative one minus five is negative six, and negative six squared is still thirty-six. Squaring erases the sign, so AB and BA must agree — which is exactly what a distance should do. Second, a distance can never be negative, because you are square-rooting a sum of squares.

One presentation habit. When the sum is not a perfect square, leave the answer as a surd unless a decimal is demanded. From B at five, eleven, to C at ten, eight, the legs are five and negative three, so the distance is the square root of twenty-five plus nine — root thirty-four, roughly five comma eight three units.

Pause here for this section's questions — they probe the formula itself, the double-negative subtraction, and why swapping the points changes nothing.

## Subtopic: The Midpoint Formula

The midpoint is the point exactly halfway along a segment, and it is the gentlest formula of the three: you simply average the coordinates.

The rule: the midpoint of the segment joining x-one, y-one and x-two, y-two has x-coordinate equal to x-one plus x-two, all over two, and y-coordinate equal to y-one plus y-two, all over two. Add the x's and halve; add the y's and halve.

Apply it to our anchors. A is negative one, three; B is five, eleven. For x: negative one plus five is four, halved is two. For y: three plus eleven is fourteen, halved is seven. The midpoint M is two, seven.

Always sanity-check: two lies between negative one and five, and seven lies between three and eleven. A midpoint that lands outside its own segment is impossible, and when it happens the cause is almost always subtraction where addition belonged — a symptom of confusing midpoint with gradient. Fix the rule in memory now: distance subtracts, gradient subtracts, midpoint is the only one of the three that ADDS.

The formula also runs in reverse, and assessors love asking it that way. Suppose M at two, seven is the midpoint of AB and A is negative one, three — find B. Turn each coordinate into a small equation. Negative one plus x, all over two, equals two; so negative one plus x equals four; so x equals five. Three plus y, all over two, equals seven; so three plus y equals fourteen; so y equals eleven. B is five, eleven, recovered from nothing but the middle.

Where the midpoint really earns its keep: diagonals. Two diagonals of a quadrilateral bisect each other exactly when they share one and the same midpoint — so you compute both midpoints and compare, and that single comparison can prove a parallelogram.

Stop now for the questions on this section — averaging the coordinates, running the formula backwards to find a missing endpoint, and the shared-midpoint test for bisecting diagonals.

## Subtopic: Gradient — Steepness, Parallel and Perpendicular

Gradient turns steepness into a number: the rise for every unit of run. The formula is y-two minus y-one, all over x-two minus x-one — change in y divided by change in x.

On A at negative one, three, and B at five, eleven: eleven minus three is eight; five minus negative one is six. Gradient equals eight over six, which simplifies to four over three. Translate that into an instruction: for every three units you move across, the line climbs four units. The habit that protects your signs is consistency — if B supplies the top of the fraction, B supplies the left of the bottom too. Mix the order in one place only and the sign flips, turning a climbing line into a falling one.

Four cases you must name on sight. Positive gradient: the line rises from left to right. Negative: it falls. Zero: a horizontal line, because the rise is zero. And a vertical line has an UNDEFINED gradient — the run is zero, and division by zero means nothing. Undefined and zero are different answers; writing zero for a vertical line is a lost mark every single time.

Two relationships do the heavy lifting in questions. Parallel lines have EQUAL gradients. Perpendicular lines have gradients multiplying to negative one — equivalently, each is the negative reciprocal of the other: flip the fraction, switch the sign. Four over three pairs with negative three over four; their product is negative twelve over twelve, which is negative one. One warning: this product test cannot handle a horizontal line paired with a vertical one, since zero and undefined form no product — yet the pair is plainly perpendicular. State that case by inspection.

Gradient also settles collinearity — whether three points share one straight line. Take P at two, one; Q at four, seven; R at six, thirteen. Gradient PQ: six over two, which is three. Gradient QR: six over two, three again. Equal gradients through the common point Q, so P, Q and R are collinear.

Your questions for this section are ready now — rise over run with consistent order, the four gradient cases including undefined, and parallel versus perpendicular applied to actual numbers.

## Subtopic: A Quadrilateral on the Grid

Here is the classic examination task: four vertices, and you must name the quadrilateral they form, proving every property you claim. All three formulae work as a team.

The vertices, taken in order around the figure: A at negative one, three; B at five, eleven; C at ten, eight; D at four, zero.

Side lengths first. AB we know: ten units. BC: legs five and negative three, so root thirty-four. CD: from ten, eight to four, zero, the legs are negative six and negative eight — thirty-six plus sixty-four — root one hundred, ten units. DA: legs negative five and three — root thirty-four again. So AB equals CD at ten, and BC equals DA at root thirty-four. Both pairs of opposite sides equal: one sufficient condition for a parallelogram.

Confirm with gradients. Gradient AB is four over three. Gradient DC, from D at four, zero to C at ten, eight: eight over six — four over three. Equal, so AB is parallel to DC. Gradient AD: negative three over five. Gradient BC: negative three over five. Equal again, so AD is parallel to BC. Both pairs of opposite sides parallel: a second, independent proof of the parallelogram.

A third proof through the diagonals. Midpoint of AC: negative one plus ten over two, and three plus eight over two — four comma five, and five comma five. Midpoint of BD: five plus four over two, and eleven plus zero over two — four comma five, and five comma five. Identical, so the diagonals bisect each other. Three routes, one conclusion.

Now push, because the follow-up always comes. Is it a rectangle? That demands a right angle, and the only grid-proof of a right angle is a gradient product of negative one. Gradient AB times gradient AD: four over three times negative three over five — negative twelve over fifteen, which is negative four over five. Not negative one, so angle A is not ninety degrees, and the figure is no rectangle. Is it a rhombus? All four sides would need to be equal, and ten is not root thirty-four. So the verdict, fully justified: a parallelogram, and nothing more.

The error museum has four exhibits. One: the double negative — five minus negative one is six, not four. Two: a gradient built with mismatched order, arriving with the wrong sign. Three: adding inside the distance formula or subtracting inside the midpoint formula. Four: naming a rectangle because the sketch looks square-cornered — only the product of gradients proves an angle.

The closing questions of this part are with you now — the full classification, with every conclusion tied to the condition that earns it.

# Part 2 — Simplifier

Same three tools, but now from the streets you actually walk — shortcuts, meeting points and hills. That is all these formulae have ever measured.

## Subtopic: Eight Blocks Across, Six Blocks Up

Picture a suburb laid out in a neat grid of streets. You are at the school gate. The library is eight blocks east and six blocks north of you.

If you follow the streets, you walk eight plus six — fourteen blocks. But suppose the sports fields sit between you and the library, wide open, and you can walk straight across the grass. How long is the straight line?

Grade nine already taught you this, just in different clothing. Eight across and six up form the two short sides of a right-angled triangle, and your diagonal path is the long side. Eight squared is sixty-four; six squared is thirty-six; together, one hundred; square root, ten. The shortcut is ten blocks — four blocks saved.

That IS the distance formula. Coordinates merely tell you the eight and the six without you counting blocks. Our lesson's two points sat at negative one, three, and five, eleven: across is five take away negative one, and taking away a negative means adding, so six; up is eleven take away three, which is eight. Six across, eight up — the same triangle turned on its side, and the same answer: ten.

So the recipe never changes: find the across, find the up, square both, add, square root. And direction cannot matter — the grass is the same width whether you walk gate-to-library or library-to-gate. Squaring eats every minus sign, which is why a distance can never come out negative.

Quick pause — a few questions on the shortcut are with you right now. Always find the across and the up first, then let Pythagoras finish.

## Subtopic: Meeting Exactly in the Middle

Two friends live on the same long road, at number five and at number seventeen, and they agree to meet halfway. No measuring needed — average the two numbers: five plus seventeen is twenty-two, halved is eleven. They meet at number eleven.

A grid just makes you do that trick twice — once for the across numbers, once for the up numbers. From negative one, three, to five, eleven: the across pair, negative one and five, adds to four, halved is two. The up pair, three and eleven, adds to fourteen, halved is seven. Meeting point: two, seven.

Check it like you would check a real meeting spot: two lies between negative one and five; seven lies between three and eleven. If your middle lands outside the two homes, somebody walked the wrong way — and on paper, the somebody is a subtraction that should have been an addition.

That is the one rule to brand in, because it separates this formula from the other two. Finding the MIDDLE means ADD and halve. Finding distance or steepness means SUBTRACT. Middle adds; everything else takes away.

The trick reverses beautifully. Meeting point at two, seven; one friend at negative one, three; where is the other friend? The across numbers must average to two, so negative one plus something is four — the something is five. The up numbers must average to seven, so three plus something is fourteen — the something is eleven. The other friend lives at five, eleven. You located a point nobody gave you.

And here is the exam payoff. When two roads cross and each one is cut exactly in half at the crossing, both roads share the same middle point. So to prove the diagonals of a shape cut each other in half, work out each diagonal's middle and compare. Same pair of numbers, and they bisect — which is a complete proof of a parallelogram.

Your questions for this part are up now. Add and halve, then ask whether the answer truly sits between the two points.

## Subtopic: Steepness You Can Feel — and the Traps

Last tool: gradient, which is steepness with a number attached.

Think of the wheelchair ramp at the mall — it rises a little over a long run, so it feels gentle. Now think of a bakkie grinding up Sani Pass in first gear — big rise, short run, brutally steep. Gradient captures the difference: how much UP, divided by how much ACROSS. Rise over run.

From negative one, three, to five, eleven: up eight, across six. Eight over six tidies to four over three. Say the meaning out loud, because the meaning is everything: every three steps forward, this line climbs four steps up. More than one-for-one — steeper than a forty-five degree line.

Four situations, four answers. Rising as you move right: positive. Falling as you move right: negative. Dead flat, like a netball court: zero, because there is no rise. Straight up, like the wall of the school hall: UNDEFINED — there is no across at all, and dividing by nothing is meaningless. A wall's gradient is not zero. Flat is zero; wall is undefined; keep those two words apart and keep the mark.

Two facts then carry most questions. Lines are parallel when their steepness is identical — two lanes of the N3 climbing Van Reenen's side by side, never meeting. Lines meet at a right angle when one gradient is the other flipped upside down with its sign switched: four over three becomes negative three over four, and multiplying them gives negative one, every time. That negative one is a protractor made of arithmetic — it is how you prove a rectangle without measuring a single angle.

Three protective habits. Subtract in the same order on top and bottom — mixing the order flips your sign and your story. Bracket every double negative: five take away negative one is six, and the brackets in your own handwriting are what save you. And never believe the sketch: our four points looked convincingly square at the corners, yet the gradients multiplied to negative four over five, not negative one. No right angle. The numbers rule; the drawing only suggests.

The final questions of the lesson are with you now — rise over run in a consistent order, flat against wall, parallel against perpendicular. Make these three formulae automatic and the whole coordinate section of your exams opens up to you.
