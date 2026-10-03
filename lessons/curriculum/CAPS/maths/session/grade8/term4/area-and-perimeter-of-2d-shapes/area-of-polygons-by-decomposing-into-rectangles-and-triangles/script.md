# Part 1 — Expert

This session calculates areas of polygons to at least two decimal places by decomposing them into rectangles and triangles. A polygon is split by straight cuts into pieces whose areas are known — rectangles, at length times breadth, and triangles, at half base times perpendicular height — and the pieces are added. Alternatively the polygon is enclosed in a rectangle and the pieces outside it are subtracted. Missing dimensions of the pieces come from the given measurements by adding or subtracting lengths. Calculations are kept unrounded until the final answer, which is rounded to two decimal places. The anchor shapes are an L-shape inside an 8 by 6 rectangle, a trapezium with parallel sides 10 and 6 and height 4, and a house-shaped pentagon 6,25 metres wide.

## Subtopic: Splitting and Adding: The L-Shape

A polygon with no formula of its own can almost always be cut into rectangles and triangles. The area of the whole is the sum of the areas of the pieces, because the pieces cover the shape exactly once, with no gaps and no overlaps.

Start with an L-shape. Picture a rectangle 8 metres wide and 6 metres tall with a corner piece 3 metres wide and 2 metres tall cut out of the top right. The outline has six sides: along the bottom 8, up the right side 4, across to the left 3, up 2, across the top 5, and down the left side 6.

Method one: split and add. Draw a horizontal cut across the shape at the level where the notch begins, 4 metres up. Below the cut is a rectangle 8 by 4, area 32 square metres. Above the cut is a rectangle 5 by 2, area 10 square metres. Total: 42 square metres.

Method two: split the other way. Draw a vertical cut where the notch begins, 5 metres from the left. To the left is a rectangle 5 by 6, area 30. To the right is a rectangle 3 by 4, area 12. Total: 42 square metres again.

Method three: enclose and subtract. The L-shape sits inside the full rectangle 8 by 6, area 48. The missing notch is 3 by 2, area 6. Subtract: 48 minus 6 is 42 square metres.

Three methods, one answer. That is the strongest check available: if two decompositions disagree, a dimension has been misread.

The skill that takes practice is finding the dimensions of each piece, because the diagram often labels only the outer sides. Use the fact that opposite sides of the whole must balance: the horizontal sides going right must total the horizontal sides going left, and the same for the vertical sides. Along the top, 5 plus the notch width 3 must equal the bottom 8. Up the right, 4 plus the notch height 2 must equal the left side 6. Missing lengths are found by adding or subtracting the labelled ones.

Draw the cuts on the diagram, label every piece with its dimensions and its area, then add. A clear layout — piece one, piece two, total — earns the method marks even if an arithmetic slip creeps in.

Note that perimeter does not work by adding pieces: the cuts are inside the shape and are not part of its edge. The perimeter of the L-shape is the six outer sides, 8 plus 4 plus 3 plus 2 plus 5 plus 6, which is 28 metres — the same as the perimeter of the full 8 by 6 rectangle, as it happens, because the notch moved two edges inward without changing their total length. Questions on splitting and adding follow now.

## Subtopic: Rectangles and Triangles Together: Trapeziums, Parallelograms and Kites

Many polygons have slanting sides, and then triangles join the rectangles.

A trapezium has one pair of parallel sides. Take one with parallel sides 10 and 6 centimetres, 4 centimetres apart, with the shorter side centred above the longer. Drop two perpendicular lines from the ends of the top side down to the bottom. They cut off a rectangle in the middle, 6 by 4, area 24 square centimetres. On each side is a right-angled triangle. The bottom is 10 and the rectangle uses 6, so the two triangles share the remaining 4, 2 each. Each triangle has base 2 and height 4, area 4. Total: 24 plus 4 plus 4, which is 32 square centimetres.

There is a shortcut that the decomposition explains: the area of a trapezium is half the sum of the parallel sides times the height. Half of 10 plus 6 is 8, times 4 is 32. The decomposition shows why it works, and it works even when the top is not centred, because the two triangles' bases always add to the difference of the parallel sides.

A parallelogram with base 7 metres and perpendicular height 3 metres: cut a right-angled triangle off one end and slide it to the other, and the shape becomes a rectangle 7 by 3. Area: 21 square metres. The slanting side's length is not needed for the area, only for the perimeter.

A kite or rhombus is split along one diagonal into two triangles. A kite with diagonals 8 and 6 centimetres, the long diagonal cutting the short one in half: split along the long diagonal and each triangle has base 8 and height 3, area 12, total 24 square centimetres. The shortcut is half the product of the diagonals: half of 8 times 6 is 24.

A general quadrilateral can be split along a diagonal into two triangles. If the diagonal is 9,6 metres and the perpendicular heights from the other two corners to the diagonal are 3,25 metres and 4,15 metres, the two triangles have areas half of 9,6 times 3,25 and half of 9,6 times 4,15. Adding: half of 9,6 times 7,4, which is 35,52 square metres.

For every triangle, the height must be perpendicular to the base chosen. When the triangle comes from cutting along a diagonal, the base is the diagonal and the heights are the perpendicular distances from the opposite corners to it. Questions on trapeziums, parallelograms and kites follow now.

## Subtopic: Decimal Dimensions and Rounding to Two Decimal Places

Real measurements are rarely whole numbers, and the syllabus asks for areas to at least two decimal places. The rule for accuracy is simple: keep every intermediate answer exact, or at full calculator precision, and round only the final total.

Take a house-shaped pentagon: a rectangle 6,25 metres wide and 4,8 metres tall with a triangular roof on top, whose peak is 2,35 metres above the top of the rectangle. Rectangle: 6,25 times 4,8, which is 30 square metres exactly. Triangle: half of 6,25 times 2,35. 6,25 times 2,35 is 14,6875, and half of that is 7,34375. Total: 30 plus 7,34375, which is 37,34375. Rounded to two decimal places: 37,34 square metres.

Now see what early rounding does. If the triangle's area is rounded to 7,3 before adding, the total is 37,30, which is wrong in the second decimal place. If the triangle is rounded to 7,34, the total is 37,34 — correct this time, but only by luck. The safe habit is to carry all the digits.

To round to two decimal places, look at the third decimal digit. If it is 5 or more, increase the second digit by one; otherwise leave it. 37,34375: the third digit is 3, so 37,34. 19,845: the third digit is 5, so 19,85. 4,995: the third digit is 5, which carries all the way: 5,00. Keep the trailing zeros when two places are asked for: 5,00, not 5.

Decimal multiplication benefits from an estimate. 6,25 times 4,8 is a little more than 6 times 5, which is 30, minus a bit — so 30 exactly is believable. 6,25 times 2,35 is about 6 times 2,4, which is 14,4; 14,6875 is close. An answer like 1,46875 or 146,875 would be spotted at once as a decimal-point slip.

Another example: a shape made of a rectangle 5,4 by 2,75 and a triangle on top of it with base 5,4 and height 1,85. Rectangle: 14,85. Triangle: half of 5,4 times 1,85, which is half of 9,99, which is 4,995. Total: 19,845, which rounds to 19,85 square metres. Rounding the triangle first to 5,00 would give 19,85 too, but rounding it to 5,0 and the rectangle to 14,9 would give 19,9 — accurate to only one decimal place.

Write the unrounded total and then the rounded answer, with the approximately equal sign between them, so the marker sees both. Questions on decimal dimensions follow now.

## Subtopic: Polygons on a Grid: Enclose and Subtract

When a polygon is drawn on a grid or given by the coordinates of its vertices, its slanting sides make splitting awkward. The enclose-and-subtract method handles it neatly.

Take the quadrilateral with vertices at 1 semicolon 2, 4 semicolon 1, 6 semicolon 4 and 3 semicolon 6. None of its sides is horizontal or vertical. Draw the smallest rectangle around it with sides along the grid lines: from x equal to 1 to x equal to 6, and from y equal to 1 to y equal to 6. That rectangle is 5 by 5, area 25 square units.

Each vertex of the quadrilateral touches a different side of the rectangle, so the parts of the rectangle outside the quadrilateral are four right-angled triangles, one at each corner.

Bottom-left corner, at 1 semicolon 1: the triangle runs up 1 to the vertex 1 semicolon 2 and across 3 to the vertex 4 semicolon 1. Area: half of 1 times 3, which is 1,5.

Bottom-right corner, at 6 semicolon 1: across 2 from 4 semicolon 1 and up 3 to 6 semicolon 4. Area: half of 2 times 3, which is 3.

Top-right corner, at 6 semicolon 6: down 2 to 6 semicolon 4 and across 3 to 3 semicolon 6. Area: 3.

Top-left corner, at 1 semicolon 6: across 2 to 3 semicolon 6 and down 4 to 1 semicolon 2. Area: half of 2 times 4, which is 4.

The four triangles total 1,5 plus 3 plus 3 plus 4, which is 11,5. The quadrilateral's area is 25 minus 11,5, which is 13,5 square units.

Read the triangle legs from the coordinates, not by counting carefully on the drawing: horizontal legs are differences in x, vertical legs are differences in y.

A caution. If a vertex does not touch the rectangle, or two vertices touch the same side, the outside region at a corner may be a triangle plus a rectangle, or some other shape. Sketch the outside regions, and split any that are not right-angled triangles into ones that are. Missing a small square at a corner is the usual error.

The method also works for triangles on a grid with no horizontal side. A triangle with vertices 0 semicolon 0, 4 semicolon 1 and 1 semicolon 3 sits in a 4 by 3 rectangle, area 12; the three outside triangles are half of 4 times 1, half of 3 times 2 and half of 1 times 3 — 2, 3 and 1,5 — totalling 6,5; the triangle's area is 5,5 square units.

On a grid, a quick count of whole and half squares gives an estimate to check against. Questions on polygons on a grid follow now.

# Part 2 — Simplifier

Now the same method as stories about a homeowner who paved an irregular yard and checked the supplier's sums, a kite built for a beach festival, and a learner who measured her bedroom floor in four pieces — stories about the area of a shape that no formula sheet lists.

## Subtopic: Paving the Irregular Yard

A homeowner in Soshanguve wants to pave the yard behind her house. The yard is almost a rectangle, 12,5 metres long and 8,4 metres wide, but one corner is cut off at an angle by a neighbour's wall, leaving a pentagon. Along the edges at that corner, the cut-off piece measures 3,2 metres along one side and 2,5 metres along the other, with a right angle between them where the old corner used to be.

A paving supplier quotes for 105 square metres of pavers, plus a 5 percent allowance for cutting at the edges. The homeowner suspects the quote is for the full rectangle and checks.

She uses enclose and subtract. The full rectangle is 12,5 times 8,4, which is 105 square metres — the supplier's figure exactly. The missing corner is a right-angled triangle with legs 3,2 and 2,5, area half of 3,2 times 2,5, which is half of 8, which is 4 square metres. The yard is 105 minus 4, which is 101 square metres.

With the 5 percent allowance, she needs 101 times 1,05, which is 106,05 square metres, not 105 times 1,05, which is 110,25. The difference is 4,2 square metres of pavers.

She double-checks with a split-and-add decomposition. Cut the yard with a line parallel to the short side where the slanted wall begins. One piece is a full rectangle: 12,5 minus 3,2, which is 9,3, by 8,4, area 78,12 square metres. The other piece, 3,2 metres long, is a trapezium with parallel sides 8,4 and 8,4 minus 2,5, which is 5,9. Its area is half of 8,4 plus 5,9, times 3,2: half of 14,3 is 7,15, times 3,2 is 22,88. Total: 78,12 plus 22,88, which is 101 square metres. The same answer, so she trusts it.

The pavers cost R185 per square metre. The supplier's figure would have cost 110,25 times R185, about R20 396; her figure costs 106,05 times R185, about R19 619. She saves close to R780 by subtracting one triangle.

The supplier's estimator agrees once he sees the sketch: he had taken the dimensions from the title deed, which gave the outer length and width, without noticing the corner. He revises the quote and asks if he can keep a copy of her method for training new staff. Questions on the paved yard follow.

## Subtopic: The Festival Kite and the Bedroom Floor

A Grade 8 class in Cape Town builds kites for a kite-flying day at Muizenberg beach. Each kite is a kite shape in the geometric sense: two sticks crossing at right angles, a vertical spine 90 centimetres long and a crossbar 60 centimetres long, fixed 25 centimetres below the top of the spine. The crossbar is cut in half by the spine; the spine is not cut in half by the crossbar.

They need to know how much fabric to buy. One learner splits the kite along the crossbar into two triangles. The top triangle has base 60 — the crossbar — and height 25, the part of the spine above it: area half of 60 times 25, which is 750 square centimetres. The bottom triangle has base 60 and height 90 minus 25, which is 65: area half of 60 times 65, which is 1 950. Total: 2 700 square centimetres.

Another learner splits it along the spine into a left and a right triangle, each with base 90 and height 30, half the crossbar: each half of 90 times 30, which is 1 350, total 2 700. A third uses the shortcut, half the product of the diagonals: half of 90 times 60 is 2 700. Three decompositions, one answer.

For a class of 32 kites they need 32 times 2 700, which is 86 400 square centimetres of fabric, before allowing for hems. The fabric is 1,5 metres wide, and 86 400 square centimetres is 8,64 square metres, so about 5,76 metres of the roll — but the kites cannot be packed without waste, so the teacher orders 7 metres.

One of the learners, back home, uses the same thinking on her bedroom floor, which she wants to cover with a mat. The room is not a rectangle: it is 3,6 metres deep, 4,15 metres wide at the door end, and 7,35 metres wide at the window end, because one wall slants. She measures carefully and confirms that the door wall and the window wall are parallel. So the floor is a trapezium.

She splits it into a rectangle 4,15 by 3,6 and a right-angled triangle with base 7,35 minus 4,15, which is 3,2, and height 3,6. Rectangle: 14,94 square metres. Triangle: half of 3,2 times 3,6, which is 5,76. Total: 20,7 square metres. Check with the trapezium shortcut: half of 7,35 plus 4,15, times 3,6, is half of 11,5 times 3,6, which is 20,7. Written to two decimal places, 20,70 square metres.

A rectangular mat of 4 by 3 metres covers 12 of those 20,70 square metres, about 58 percent of the floor. She decides it is enough. Questions on the kite and the floor follow.

## Subtopic: Method Summary and Examination Technique

The method for the area of a polygon. One: sketch the shape and decide how to decompose it — split into rectangles and triangles and add, or enclose in a rectangle and subtract the outside pieces. Two: draw the cuts and find every piece's dimensions, using the fact that opposite sides balance and that missing lengths are sums or differences of given ones. Three: for each triangle, use a perpendicular height. Four: calculate each piece's area without rounding, label it, and add or subtract. Five: round the total to two decimal places and give the unit. Six: check with a second decomposition, a shortcut formula, or an estimate.

Shortcut formulae that decomposition justifies. Trapezium: half the sum of the parallel sides times the height. Parallelogram: base times perpendicular height. Kite or rhombus: half the product of the diagonals.

A typical examination item shows a composite shape with labelled outer dimensions and asks for its area. Show the cuts, label the pieces, present the sum.

Another gives a polygon on a grid or by coordinates. Enclose and subtract, reading the legs from coordinate differences.

Another adds a cost or a quantity: pavers per square metre, paint per square metre, seed per square metre. Find the area first, then multiply by the rate, applying any percentage allowance afterwards.

Another asks for the area of a shaded region between two shapes, such as a frame around a picture. Outer area minus inner area.

Errors to avoid. Misreading a missing dimension. Using a slanting side as a height. Forgetting the half for triangles. Counting a region twice where two pieces overlap, or leaving a gap. Rounding pieces before adding. Missing a small rectangle in a corner region of an enclose-and-subtract diagram. Adding the cut lines into a perimeter.

Presentation earns marks. A labelled sketch and a line for each piece — piece one, rectangle, 9,3 times 8,4, which is 78,12; piece two, trapezium, 22,88; total 101 — lets the marker award method marks even if one multiplication goes wrong.

Looking ahead: circles cannot be split into rectangles and triangles exactly, and the next lesson explores why the circle needs pi; after that, problems combine polygons and circles, such as a rectangle with semicircular ends. Final questions follow.
