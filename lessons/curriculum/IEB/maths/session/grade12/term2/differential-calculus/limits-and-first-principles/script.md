# Part 1 — Expert

Up to now, every branch of mathematics you have met answers some version of the question, how much? Calculus asks something sharper: how fast is this changing, at this precise instant? Two foundation ideas make that question answerable. The limit allows a quantity to approach a value without ever needing to arrive, and differentiation from first principles converts the limit into a machine that measures instantaneous change. Every differentiation rule for the rest of the year traces its birth certificate back to this lesson.

## Subtopic: The Idea of a Limit

Consider the expression x squared minus sixteen, over x minus four, and demand its value at x equals 4. Substitution delivers zero over zero — undefined, a gap in the function. Now stop demanding and start watching. At x equals 3,9 the expression gives 7,9. At 3,99 it gives 7,99. At 4,01 it gives 8,01. From the left and from the right, the outputs squeeze in on 8. We say the limit of the expression, as x approaches 4, is 8 — the value the outputs home in on, regardless of whether the function ever produces it.

The algebra behind the squeeze: the numerator is a difference of two squares, x minus four times x plus four. For every input EXCEPT 4, the factor x minus four cancels, leaving simply x plus four — and as x approaches 4, that approaches 8. Graphically, the original expression draws the straight line y equals x plus 4 with one open dot punched out at the point four, eight. The function has no value at the gap; the limit is the value the gap is shaped around.

That is the working method for every limit in this course: substitute first, and if substitution returns zero over zero, factorise, cancel the shared factor, and substitute again. Try the limit as x approaches minus 3 of x squared minus nine, over x plus three: factorise into x minus three times x plus three, over x plus three; cancel; what remains is x minus three, and the limit is minus 6.

Mind your language throughout: saying the function EQUALS 8 at x equals 4 is false — nothing exists there. Saying its limit at 4 is 8 is exactly true. Holding those two sentences apart is the entire concept.

Pause here — the questions for this section are with you now. Substitute, and treat zero over zero as the instruction to factorise and cancel before substituting again.

## Subtopic: Average Gradient and the Shrinking Interval

Last year you measured the average gradient between two points of a curve: change in y over change in x. On f of x equals x squared, take the points at x equals 2 and x equals 4. The y values are 4 and 16, so the average gradient is sixteen minus four, over four minus two — six. That six belongs to the interval as a whole, not to any single point on it, just as an average speed of 70 kilometres per hour summarises a journey without revealing any one speedometer reading.

Now squeeze the interval. Anchor the left point at x equals 2 and drag the right point inward. From 2 to 3: nine minus four over one — 5. From 2 to 2,5: six comma two five minus four, over nought comma five — 4,5. From 2 to 2,1: four comma four one minus four, over nought comma one — 4,1. From 2 to 2,01: 4,01. The averages are converging on 4 — a limit, the identical concept from the previous section, now acting on gradients instead of function values.

Give the geometry its names. A line through two points of a curve is a secant. As the second point slides into the first, the secant swings, and the position it settles into is the TANGENT — the line that touches the curve at that one point and points the way the curve is heading there. The gradient of a curve at a point is DEFINED as the gradient of its tangent there, and our table of shrinking averages announces that y equals x squared has gradient 4 at the point where x is 2.

Stop for this section's questions now — average gradient is rise over run between two points; the instantaneous gradient is the limit of those averages as the second point slides home.

## Subtopic: Differentiation from First Principles

Write the shrinking interval in general symbols and you obtain the most important definition of the year. Stand at any point x, and place a second point a small step h further along, at x plus h. The average gradient between them is f of x plus h, minus f of x, all divided by h. Let h approach zero and the average sharpens into the instantaneous. The derivative is defined as: f prime of x equals the limit, as h approaches zero, of f of x plus h minus f of x, all over h.

Run the definition on f of x equals x squared at a general x. F of x plus h is the quantity x plus h, squared: x squared plus two x h plus h squared. Subtract f of x and the x squared terms annihilate, leaving two x h plus h squared. Divide by h — permitted, since h approaches zero without ever being zero — to get two x plus h. Finally let h approach zero: the limit is two x. The derivative of x squared is two x, valid at every point simultaneously. At x equals 2 the gradient is 4, confirming the previous section's table; at x equals 6 it is 12; at x equals minus 4 it is minus 8.

Notice the definition manufactures its own zero-over-zero: the h below must always cancel against an h factored out above, and an h that refuses to cancel is a symptom of an expansion error further up the page. Two quick computations round out the basics. A constant, f of x equals c: the numerator is c minus c, which is zero, so the derivative is zero — a horizontal graph climbs nowhere. A straight line, f of x equals a x plus b: the numerator collapses to a times h, the division leaves the constant a — a line's gradient is its slope, exactly as before.

The questions on this section are in front of you now — state the definition first, expand with care, factor out the h, cancel it, then let h go to zero.

## Subtopic: First Principles on a x Squared and One Over x, and the Notation

The syllabus asks for first principles on two further functions, and each one teaches its own technique. Take f of x equals a x squared plus b, constants included. F of x plus h is a times x squared plus two x h plus h squared, plus b. The subtraction wipes out both the a x squared and the b, leaving a times two x h plus h squared. Divide by h: two a x plus a h. Take the limit: two a x. The moral: a constant ADDED disappears; a constant MULTIPLIED rides through to the answer. For f of x equals four x squared, the derivative is eight x.

Then the reciprocal, f of x equals one over x. The numerator is one over x plus h, minus one over x — two fractions demanding a common denominator, namely x times x plus h. Adjust the numerators: x minus the quantity x plus h, which collapses to minus h. The full difference quotient is therefore minus h, over h times x times x plus h. Cancel the h: minus one over x times x plus h. Send h to zero: minus one over x squared. So the derivative of one over x is minus one over x squared — negative for every allowed x, which matches a hyperbola sliding downhill on both of its branches.

Close with the notations, four costumes on one machine: f prime of x; d y by d x; d by d x of the expression; and D x of y. The d y by d x symbol is not a genuine fraction, but it wears its history — change in y over change in x, refined through a limit. Read and write all four without hesitation; question setters switch between them freely.

The final questions of this part are with you now — added constants vanish, multiplied constants survive, the reciprocal wants a common denominator, and all four notations name the same derivative.

# Part 2 — Simplifier

Now the same two ideas from a bus trip and a gap in the road — same definitions, same answers, built from pictures you already carry.

## Subtopic: The Pothole in the Graph

Some functions carry a pothole: one single input where they refuse to answer. The expression x squared minus sixteen over x minus four is honestly just a straight line — except at exactly x equals 4, where it demands zero divided by zero and goes silent. But stand beside the pothole and listen to the neighbours. At 3,9 the function says 7,9. At 3,99 it says 7,99. At 4,01 it says 8,01. Every neighbour, on both sides, points at the same missing number: 8.

That pointed-at number is the limit. The function never actually SAYS 8 at 4 — there is a hole there — but the whole neighbourhood agrees on what the hole is shaped like. Limits are the mathematics of what belongs in the hole.

The routine has two steps. Step one: substitute. If an ordinary number comes out, that number is the limit — most functions have no pothole at all. Step two: if zero over zero comes out, the top and bottom are hiding a common factor; factorise, cancel it, substitute again. X squared minus sixteen is x minus four times x plus four — cancel the x minus four, substitute, and 8 steps forward. The cancelling is legitimate because just NEXT to the hole, x minus four is a tiny non-zero number, and tiny non-zero numbers cancel like any others.

Quick check before we carry on — questions on limits are coming to you right now. Substitute first, and read zero over zero as the signal to factorise.

## Subtopic: The Speedometer Question

A bus leaves the terminus and covers 210 kilometres in three hours. Average speed: 70 kilometres per hour. Yet at any particular moment the speedometer could have shown 55, or 100, or zero at a stop. The average describes the whole trip; the speedometer answers a completely different question — how fast, right NOW?

Suppose you had to rebuild the speedometer using only a stopwatch and the odometer. Measure the distance covered during one full minute around the moment you care about: say 1,2 kilometres — an average of 72 kilometres per hour across that minute. Still coarse. Measure across one second: closer to the truth. Across a tenth of a second: closer still. The shorter the window, the less the speed can wander inside it, so the averages funnel down onto a single number. That number — the limit of the average speeds as the window shrinks to nothing — IS the speedometer reading. Instantaneous speed is a limit of average speeds; there is no other honest way to define it.

Curves behave the same way. The average gradient between two points is a trip average: rise over run. Slide the second point toward the first and the averages funnel down to the gradient at the point — the curve's own speedometer reading. On y equals x squared at x equals 2, the shrinking-window averages run 5, then 4,5, then 4,1, then 4,01 — settling on 4. Meanwhile the line through the two points swings into the tangent: the straight line that rests against the curve at that single point, like a ruler held flush against a bend.

Your questions for this part are up now. Trip average needs two points; the speedometer needs one, reached by shrinking the trip to nothing.

## Subtopic: The Recipe Called First Principles

Everything the speedometer taught us, written once as a recipe. Name the small step h — the shrinking window. The average gradient from x to x plus h is f at x plus h, minus f at x, divided by h. The derivative — read it as f prime of x — is what that fraction turns into as h shrinks to zero. Four steps, in the same order, every time. One: write out f of x plus h. Two: subtract f of x. Three: divide by h and CANCEL it — it always cancels, because the subtraction always leaves h as a common factor. Four: let h be zero in whatever remains.

Watch it run on f of x equals x squared. Step one: x plus h squared is x squared plus two x h plus h squared. Step two: subtract x squared, keeping two x h plus h squared. Step three: divide by h — two x plus h. Step four: h to zero — two x. Note what came out: a formula, not a single number — a speedometer for every point of the curve at once. At x equals 6 the gradient is 12; at minus 4 it is minus 8; at zero it is flat. Steeper to the right, downhill on the left — precisely how the parabola actually behaves.

Two miniature machines finish the set. A constant function, f of x equals 12: the subtraction gives zero on top, so the derivative is zero — a flat road, a resting speedometer. A straight line, a x plus b: the recipe hands back a, the slope the line always carried. And a final label warning: f prime of x, d y by d x, and D x of y are three name tags tied to the same machine — read every one of them simply as, the derivative.

And here come the last questions of the lesson, right now: four steps, the h must cancel, and if it will not, go hunting for the algebra slip before doubting the recipe.
