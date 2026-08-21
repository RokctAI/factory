# Part 1 — Expert

Grade eleven treated functions as pictures to sketch. Grade twelve demands precision: what exactly IS a function, and under what conditions can one run in reverse? Four pieces of equipment by the end: the formal definition that divides functions from mere relations, the swap-and-solve routine that constructs an inverse, the reflection picture across the line y equals x, and the discipline of restricting a domain so that an inverse earns the title function.

## Subtopic: The Formal Definition of a Function

A relation is any rule pairing input numbers with output numbers. A function is a relation carrying one extra guarantee: every input in the domain is matched with EXACTLY one output. One in, one out, without exception. The rule y equals 3 x minus 5 is a function — feed it 2 and the only possible result is 1. The rule y squared equals x is not a function, because the input 16 yields two outputs, 4 and minus 4, and a function is forbidden to offer choices.

On a graph the guarantee becomes the vertical line test. Every input is the position of a vertical line, so sweep vertical lines across the picture: if any vertical line meets the graph more than once, some input owns two outputs and the relation fails. A parabola lying sideways, opening rightward, fails at once; a straight line, or an ordinary parabola opening upward, passes cleanly.

Mark carefully what the definition does NOT outlaw. Two different inputs may lawfully share one output. The rule y equals x squared sends both 4 and minus 4 to 16, and remains a perfectly respectable function — many-to-one is permitted, one-to-many is not. That one-way asymmetry plants the seed for everything else in this lesson.

Pause here — the questions for this section are with you now. One input, one output, and let the vertical line deliver the verdict.

## Subtopic: Building the Inverse by Swapping x and y

The inverse of a function undoes every pairing: if the function carries 2 to 1, the inverse carries 1 back to 2. Inputs and outputs exchange roles, and algebra performs the exchange in a single move: swap x and y in the equation, then solve for y again.

Take y equals 3 x minus 5. Swap: x equals 3 y minus 5. Solve: 3 y equals x plus 5, so y equals the quantity x plus 5, over 3. That is the inverse. Now certify it with a genuine pairing, because the certificate costs seconds: the original sends 2 to 1, so the inverse must send 1 back to 2, and one plus five over three is indeed 2. Run that check every single time — a pairing that fails to reverse exposes an algebra slip immediately.

The routine digests any straight line y equals a x plus q. Take y equals 2 x plus 8. Swap: x equals 2 y plus 8. Solve: y equals the quantity x minus 8, over 2, which tidies to a half x minus 4. The original had gradient 2; the inverse has gradient a half. A line's inverse always carries the reciprocal gradient, because a line climbing 2 for every 1 across must, once reversed, climb 1 for every 2 across.

Notation earns one careful sentence. The inverse of f is written f with a small minus one raised beside it, read f inverse. That minus one is NOT an exponent — f inverse of x does not mean one over f of x. It is purely a label for the reversed function.

Stop for this section's questions now — swap the letters, solve for y, and certify the result with one reversed pairing.

## Subtopic: The Reflection in the Line y Equals x

Swapping x and y carries a picture with it. Each point of the original graph, say the point 2 and 1, becomes the point 1 and 2 on the inverse. Swapping a point's coordinates reflects it across the line y equals x, the forty-five degree diagonal through the origin. So the inverse's graph is the original's mirror image in that diagonal — every function and its inverse hang in perfect symmetry about y equals x.

This yields a rapid sketching method. To draw the inverse of y equals 2 x plus 8, mark convenient points of the original — the intercepts are cheapest, 0 and 8, and minus 4 and 0 — swap each pair into 8 and 0, and 0 and minus 4, and rule the line through the swapped points. Under reflection the intercepts trade jobs: the x intercept of the original becomes the y intercept of the inverse.

Domain and range swap for the same reason. The set of inputs the original accepted becomes the outputs the inverse produces, and the other way round. A function with domain all real x and range y greater than 0 has an inverse with domain x greater than 0 and range all real y. Writing that swapped pair down is frequently a mark by itself.

One geometric bonus to keep: any point where a graph crosses the line y equals x reflects onto itself, so the inverse passes through the identical point.

Quick pause — the questions on reflection are with you now. Swap the coordinates, swap domain and range, and keep the diagonal mirror in sight.

## Subtopic: Restricting the Domain So the Inverse Is a Function

Now the favourite trap of every examiner. Take y equals x squared and run the routine: swap into x equals y squared, solve into y equals plus or minus the square root of x. Two outputs for a single input — the inverse relation exists, but it is NOT a function. The reflected graph fails the vertical line test, and the words plus or minus are the written confession.

Why the failure? Because the original was many-to-one: 4 and minus 4 both landed on 16, so the reversed rule cannot decide which to send back. An inverse qualifies as a function only when the original never repeats an output — when it is one-to-one. The screening test on the original graph is the horizontal line test: if every horizontal line crosses at most once, the inverse will be a function.

The repair is domain restriction. Keep only the right arm of the parabola by imposing x greater than or equal to 0: now y equals x squared is one-to-one, and its inverse is y equals the positive square root of x, a proper function. Keep the left arm instead, x less than or equal to 0, and the inverse becomes y equals negative square root of x. Both restrictions are legitimate; the question normally chooses one for you.

Worked case with a coefficient. Take y equals 3 x squared with domain x less than or equal to 0. Swap: x equals 3 y squared. Solve: y squared equals x over 3, so y equals plus or minus the square root of x over 3 — and now the restriction selects the sign. The original's domain was x less than or equal to 0, and that domain becomes the RANGE of the inverse, so the inverse's outputs must be zero or negative: y equals negative square root of x over 3. Certify with a pairing: the original sends minus 2 to 12, and negative square root of twelve over three is negative square root of 4, which is minus 2. The pairing reverses without complaint.

The final questions of this part are with you now — screen with a horizontal line, restrict to one arm, and let the old domain dictate the sign of the root.

# Part 2 — Simplifier

Now the same functions and inverses again, built from vending machines and mirrors — same rules, same answers.

## Subtopic: One Ticket, One Prize

Picture a vending machine. Punch in a code and exactly one snack falls. That is a function: each input earns exactly one output, no exceptions, no moods. A machine that sometimes dropped two different snacks for one code would be faulty — and that faulty machine is precisely what mathematicians call a relation that is not a function. The rule y squared equals x is the faulty machine: punch in 16 and both 4 and minus 4 clatter into the tray.

On a graph the fault shows up under a vertical line. One vertical line is one single input; slide it across the picture, and if it ever touches the graph in two places, that input has two outputs and the machine is faulty. Sideways parabola: faulty. Ordinary straight line: working.

Now the twist that pays off later. Two DIFFERENT codes may drop the SAME snack. Punch 4 or punch minus 4 into the machine y equals x squared and each drops a 16. Still a working machine — the guarantee is one snack per code, never one code per snack. Keep straight which direction the guarantee points.

Quick check before we carry on — questions on spotting a true function are coming to you right now. One code, one snack, and slide the vertical line across the whole picture.

## Subtopic: Running the Machine Backwards

An inverse is the machine thrown into reverse: you hold the snack and demand to know which code produced it. If the machine y equals 3 x minus 5 turns the code 2 into the snack 1, the reverse machine must turn 1 back into 2.

The algebra of reversing is a swap. Trade the letters x and y, then tidy by solving for y. For y equals 3 x minus 5: trade into x equals 3 y minus 5, tidy into y equals x plus 5, all over 3. Read the reversed machine aloud and it narrates the undoing: the original multiplied by 3 and then subtracted 5, so the reverse adds 5 back and then divides by 3 — opposite operations, opposite order, like unlocking a door you just locked and stepping back out.

Always trial the reversed machine with one real snack. The original sent 2 to 1; feed 1 into x plus 5 over 3 and out comes 2. Any other result means an algebra step wobbled, and the trial catches it while it is still free to fix.

Your questions for this part are up now. Trade the letters, undo the operations in reverse order, and trial the machine with a pairing you already trust.

## Subtopic: The Mirror on the Diagonal and the Machine That Cannot Decide

Reversing pairings has a picture: the point 2 and 1 turns into the point 1 and 2, and swapping a point's coordinates flips it across the forty-five degree line y equals x. The whole inverse graph is the original viewed in a mirror lying along that diagonal. Sketching an inverse is pure reflection: swap the coordinates of the intercepts and redraw through them.

But throw y equals x squared into reverse and trouble knocks. You hold the snack 16 and ask which code bought it — and the machine stalls: maybe 4, maybe minus 4. A reverse machine that cannot decide is not a function. The early-warning test is a horizontal line on the ORIGINAL graph: if some horizontal line touches twice, two codes share one snack, and the reversal is doomed to stall.

The fix is honest surgery: disconnect half the machine. Permit only codes x greater than or equal to 0 and just the right arm of the parabola survives — every snack now traces back to exactly one code, and the reverse machine y equals the square root of x answers instantly. Keep the left arm instead, x less than or equal to 0, and the reverse answers with negative square root of x. One arm at a time, the parabola becomes reversible — and the surviving set of codes decides whether the root wears a plus or a minus.

And here come the last questions of the lesson, right now: mirror across the diagonal, horizontal line to predict the stall, and keep one arm so the reverse machine always knows its answer.
