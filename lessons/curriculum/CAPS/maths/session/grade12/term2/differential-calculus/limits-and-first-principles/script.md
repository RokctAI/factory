# Part 1 — Expert

Everything in mathematics so far has answered the question, how much? Calculus answers a sharper question: how FAST is it changing, right now? This session lays the two foundation stones: the limit, which lets a quantity approach a value it never quite reaches, and differentiation from first principles, which turns the limit into a machine for measuring instantaneous change. Every derivative rule used for the rest of the year is born here.

## Subtopic: The Idea of a Limit

Take the expression x squared minus nine, over x minus three, and ask for its value at x equals 3. Substitution gives zero over zero — undefined, a hole in the function. But watch the expression NEAR 3. At x equals 2,9 it gives 5,9. At 2,99 it gives 5,99. At 3,01 it gives 6,01. From both sides, the outputs crowd in on 6. We say the limit of the expression, as x approaches 3, is 6 — the value the outputs approach, whether or not the function ever gets there.

Algebra explains the pattern. The numerator factorises as a difference of two squares: x minus three, times x plus three. For every x EXCEPT 3, the factor x minus three cancels, leaving x plus three — and as x approaches 3, x plus three approaches 6. The graph of the original expression is the straight line y equals x plus 3 with a single open dot at the point three, six. The function is undefined at the hole; the limit is the value the hole surrounds.

That is the standard technique for the limits in this course: substitute first, and if substitution gives zero over zero, factorise, cancel, and substitute again. Compute the limit as x approaches 2 of x squared minus four, over x minus two: factorise to x minus two, times x plus two, over x minus two; cancel; the limit is 4.

One caution of language: writing that the function EQUALS 6 at x equals 3 is false; writing that its limit at 3 is 6 is exactly true, and the distinction is the whole point of the concept.

Pause here — the questions for this section are with you now. Substitute, and when zero over zero appears, factorise and cancel before substituting again.

## Subtopic: Average Gradient and the Shrinking Interval

Grade eleven measured the average gradient between two points on a curve: change in y over change in x. On the curve f of x equals x squared, take the points where x is 1 and x is 3. The y values are 1 and 9, so the average gradient is nine minus one, over three minus one — four. That number describes the whole interval, not any single instant, the way an average speed of 80 kilometres per hour describes a journey without telling you the speedometer reading at any moment.

Now shrink the interval. Fix the left point at x equals 1 and slide the right point closer. From 1 to 2: average gradient is four minus one over one, which is 3. From 1 to 1,5: two comma two five minus one, over nought comma five — 2,5. From 1 to 1,1: one comma two one minus one, over nought comma one — 2,1. From 1 to 1,01: 2,01. The averages are crowding in on 2 — a limit, exactly the concept from the previous section, now applied to gradients.

Geometrically, the line through two points on a curve is a secant. As the second point slides toward the first, the secant pivots, and its limiting position is the TANGENT — the line that touches the curve at that single point and matches its direction there. The gradient of the curve at a point is defined as the gradient of the tangent, and the arithmetic above says the curve y equals x squared has gradient 2 at the point where x is 1.

Stop for this section's questions now — average gradient is rise over run between two points, and the instantaneous gradient is the limit of that average as the interval shrinks to nothing.

## Subtopic: Differentiation from First Principles

The shrinking interval, written in general symbols, becomes the most important definition of the year. Take any point x, and a second point a small step h away, at x plus h. The average gradient between them is f of x plus h, minus f of x, all over h. Let h approach zero, and the average becomes instantaneous. The derivative of f is defined as: f prime of x equals the limit, as h approaches zero, of f of x plus h minus f of x, all over h.

Apply it to f of x equals x squared, at a general x this time. F of x plus h is the quantity x plus h, squared: x squared plus two x h plus h squared. Subtract f of x: two x h plus h squared. Divide by h — legal because h is approaching zero, not equal to zero — and get two x plus h. Now let h approach zero: the limit is two x. So the derivative of x squared is two x, everywhere at once. At x equals 1 the gradient is 2, matching the previous section's arithmetic; at x equals 5 it is 10; at x equals minus 3 it is minus 6.

The zero-over-zero pattern is built into the definition — the h in the denominator always cancels against an h factored from the numerator, and if it refuses to cancel, there is an algebra error upstream. Two more first-principles computations complete the toolkit. For a constant, f of x equals c: the numerator is c minus c, zero, so the derivative is zero — a flat graph has no gradient anywhere. For a straight line, f of x equals a x plus b: the numerator is a times h, dividing to a constant a — a line's gradient is its own slope, as it always was.

The questions on this section are in front of you now — write the definition down before substituting anything, expand carefully, factor the h, cancel, then send h to zero.

## Subtopic: First Principles on a x Squared and One Over x, and the Notation

Two more functions are in the syllabus for first principles, and each teaches a technique. First, f of x equals a x squared plus b, with constants along for the ride. F of x plus h is a times x squared plus two x h plus h squared, plus b. Subtracting f of x kills both the a x squared and the b, leaving a times two x h plus h squared. Divide by h: two a x plus a h. Limit: two a x. Constants added on vanish; constants multiplied stay as multipliers. For f of x equals three x squared, the derivative is six x.

Second, the reciprocal function, f of x equals one over x. The numerator is one over x plus h, minus one over x. Combine over the common denominator x times x plus h: the numerator becomes x minus the quantity x plus h, which is minus h. So the whole difference quotient is minus h, over h times x times x plus h. Cancel the h: minus one over x times x plus h. Send h to zero: minus one over x squared. The derivative of one over x is minus one over x squared — negative everywhere, matching a hyperbola that falls from left to right in each branch.

Finally, the notations, all meaning the same machine: f prime of x; d y by d x; d by d x of the expression; and D x of y. The d y by d x form is not a fraction of two numbers, but it remembers its birth as change in y over change in x, shrunk through a limit. You must read and write all four fluently — examiners rotate them freely.

The final questions of this part are with you now — added constants die, multiplied constants survive, the reciprocal needs a common denominator, and every notation names the same derivative.

# Part 2 — Simplifier

Now the same limits and first principles from a taxi's speedometer and a photograph zoom — same definitions, same answers, built from things you can picture.

## Subtopic: The Pothole in the Graph

Some functions have a pothole: one single input where they refuse to answer. The expression x squared minus nine over x minus three is a perfectly good straight line — except exactly at x equals 3, where it demands zero divided by zero and gives up. But stand NEXT to the pothole and look: at 2,9 the function says 5,9; at 2,99 it says 5,99; at 3,01 it says 6,01. Every neighbour points at the same missing value: 6.

That pointed-at value is the limit. The function never SAYS 6 at 3 — there is a hole there — but everything around the hole agrees on what belongs in it. Limits are the mathematics of what belongs in the hole.

Finding them is a two-step routine. Step one: try substituting. If a number comes out, that is the limit — most functions have no pothole. Step two: if zero over zero comes out, the top and bottom share a hidden common factor; factorise, cancel it, and substitute again. X squared minus nine is x minus three times x plus three — cancel the x minus three, substitute, and 6 appears. The cancelling is legal because near the hole, x minus three is a small number, not zero, and small numbers cancel like any others.

Quick check before we carry on — questions on limits are coming to you right now. Substitute first, and let zero over zero be your signal to factorise.

## Subtopic: The Speedometer Question

A taxi leaves the rank and covers 160 kilometres in two hours. Average speed: 80 kilometres per hour. But at any given moment the speedometer might have read 60, or 110, or zero at a stop. Average speed describes the whole trip; the speedometer answers a different question — how fast RIGHT NOW?

Here is how you could rebuild a speedometer from stopwatch data. Measure the distance covered in one full minute around the moment you care about: say 1,5 kilometres — that is 90 kilometres per hour, on average, for that minute. Too coarse. Measure over one second instead: closer. Over a tenth of a second: closer still. The shorter the interval, the less the speed can drift inside it, so the averages home in on a single number. That number — the limit of the average speed as the time interval shrinks to nothing — IS the speedometer reading. Instantaneous speed is a limit of average speeds.

Curves work identically. The average gradient between two points on a curve is a trip average: rise over run. Slide the second point toward the first, and the average homes in on the gradient at the point — the curve's own speedometer. On y equals x squared at x equals 1, the averages over shrinking intervals read 3, then 2,5, then 2,1, then 2,01 — settling on 2. The line through the two points, meanwhile, pivots into the tangent: the straight line that kisses the curve at that point and shows its direction, like a ruler laid flat against a bend in the road.

Your questions for this part are up now. Trip average is two points; speedometer is one point, reached by shrinking the trip to nothing.

## Subtopic: The Recipe Called First Principles

Everything from the speedometer, written once and for all as a recipe. Call the small step h — the shrinking minute. The average gradient from x to x plus h is: f at x plus h, minus f at x, divided by h. The derivative — said f prime of x — is what that fraction becomes as h shrinks to zero. Four steps, every time. One: write f of x plus h. Two: subtract f of x. Three: divide by h and CANCEL the h — it always cancels, because the subtraction always leaves h as a common factor. Four: let h be zero in what remains.

Run it on f of x equals x squared. Step one: x plus h squared is x squared plus two x h plus h squared. Step two: subtract x squared, leaving two x h plus h squared. Step three: divide by h — two x plus h. Step four: h to zero — two x. The answer is a formula, not a number: a speedometer for EVERY point of the curve at once. At x equals 5, gradient 10; at minus 3, gradient minus 6. Steeper as you go right, downhill on the left, flat at zero — exactly how the parabola behaves.

Two smaller machines complete the set. A constant function, f of x equals 7: subtracting gives zero on top, so the derivative is zero — a flat road has a flat speedometer. A straight line, a x plus b: the recipe returns a, the slope it always had. And one notation warning before the questions: f prime of x, d y by d x, and D x y are three name tags on the same machine — read them all as, the derivative.

And here come the last questions of the lesson, right now: four steps, the h must cancel, and if it refuses, hunt the algebra slip before blaming the recipe.
