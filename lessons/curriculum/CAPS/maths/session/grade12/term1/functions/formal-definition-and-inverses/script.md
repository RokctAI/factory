# Part 1 — Expert

Grade eleven treated functions as graphs to sketch. Grade twelve asks a sharper question: what exactly IS a function, and when can one be run backwards? Four pieces of equipment by the end: the formal definition that separates functions from mere relations, the swap-and-solve routine that builds an inverse, the reflection picture in the line y equals x, and the discipline of restricting a domain so that an inverse deserves the name function.

## Subtopic: The Formal Definition of a Function

A relation is any rule that pairs input numbers with output numbers. A function is a relation with one extra promise: every input in the domain is paired with EXACTLY one output. One in, one out, every time. The rule y equals 2 x plus 3 is a function — feed it 1 and the only possible answer is 5. The rule y squared equals x is not a function, because the input 9 produces two outputs, 3 and minus 3, and a function is never allowed to hesitate.

On a graph the promise becomes the vertical line test. Each input is a vertical line's position, so draw vertical lines across the picture: if any vertical line cuts the graph more than once, some input has two outputs and the relation fails. A parabola lying on its side, opening to the right, fails instantly; a straight line or an ordinary parabola opening upwards passes.

Notice what the definition does NOT forbid. Two different inputs may share an output. The rule y equals x squared sends both 3 and minus 3 to 9, and it is still a perfectly good function — many-to-one is legal, one-to-many is not. That asymmetry is the seed of everything that follows in this lesson.

Pause here — the questions for this section are with you now. One input, one output, and let the vertical line be the judge.

## Subtopic: Building the Inverse by Swapping x and y

The inverse of a function reverses every pairing: if the function sends 1 to 5, the inverse sends 5 back to 1. Inputs and outputs trade places. That trade is carried out algebraically in one move: swap x and y in the equation, then solve for y again.

Take y equals 2 x plus 3. Swap: x equals 2 y plus 3. Solve: 2 y equals x minus 3, so y equals the quantity x minus 3, over 2. That is the inverse. Test it on a real pairing, because the test costs seconds: the original sends 1 to 5, so the inverse must send 5 to 1, and five minus three over two is indeed 1. Run that check every time — a swapped pair that fails means an algebra slip.

The same routine handles any straight line y equals a x plus q. Take y equals 3 x minus 6. Swap: x equals 3 y minus 6. Solve: y equals the quantity x plus 6, over 3, which simplifies to one third x plus 2. The original had gradient 3; the inverse has gradient one third. Inverses of straight lines always flip the gradient to its reciprocal, because a line that climbs 3 for every 1 across must, when reversed, climb 1 for every 3 across.

Notation deserves one careful sentence. The inverse of f is written f with a small minus one above it, spoken f inverse. The minus one is NOT a power — f inverse of x does not mean one over f of x. It is a label meaning the reversed function, nothing more.

Stop for this section's questions now — swap the letters, solve for y, and certify the result with one reversed pair.

## Subtopic: The Reflection in the Line y Equals x

Swapping x and y has a picture. Every point on the original graph, say the point 1 and 5, becomes the point 5 and 1 on the inverse. Swapping the coordinates of a point reflects it across the line y equals x, the forty-five degree diagonal through the origin. So the graph of the inverse is the mirror image of the original graph, reflected in that diagonal — every function and its inverse hang symmetrically about y equals x.

This gives a fast sketching method. To draw the inverse of y equals 3 x minus 6, mark two or three points of the original — the intercepts are the easiest, 0 and minus 6, and 2 and 0 — swap each pair to get minus 6 and 0, and 0 and 2, and draw the line through the swapped points. Intercepts trade jobs under reflection: the x intercept of the original becomes the y intercept of the inverse.

Domain and range trade places for the same reason. Whatever set of inputs the original accepted becomes the set of outputs the inverse produces, and vice versa. If a function has domain all real x and range y greater than 0, its inverse has domain x greater than 0 and range all real y. Writing the swapped domain and range is usually a mark on its own.

One geometric fact to keep: if a graph crosses the line y equals x at some point, its inverse passes through the same point, because a point on the mirror reflects to itself.

Quick pause — the questions on reflection are with you now. Swap the coordinates, swap domain and range, and keep the diagonal mirror in view.

## Subtopic: Restricting the Domain So the Inverse Is a Function

Now the exam's favourite trap. Take y equals x squared and run the routine: swap to get x equals y squared, solve to get y equals plus or minus the square root of x. Two outputs for one input — the inverse relation exists, but it is NOT a function. The vertical line test fails on the reflected graph, and the words plus or minus are the confession.

Why did it fail? Because the original was many-to-one: both 3 and minus 3 went to 9, so the reversed rule cannot know which one to return to. An inverse can only be a function when the original never repeats an output — when it is one-to-one. On the original graph that is the horizontal line test: if every horizontal line cuts the graph at most once, the inverse will be a function.

The repair is to restrict the domain. Keep only the right arm of the parabola by demanding x greater than or equal to 0: now y equals x squared is one-to-one, and its inverse is y equals the positive square root of x, a clean function. Keep only the left arm instead, x less than or equal to 0, and the inverse is y equals negative square root of x. Either restriction is legal; the question usually dictates which.

Worked case with a coefficient. Take y equals 2 x squared with domain x less than or equal to 0. Swap: x equals 2 y squared. Solve: y squared equals x over 2, so y equals plus or minus the square root of x over 2 — and now choose the sign using the restriction. The original domain was x less than or equal to 0, and that domain becomes the RANGE of the inverse, so the inverse's outputs must be negative or zero: y equals negative square root of x over 2. Check with a pairing: the original sends minus 2 to 8, and negative square root of eight over two is negative square root of 4, which is minus 2. The pairing reverses perfectly.

The final questions of this part are with you now — test one-to-one with a horizontal line, restrict to a single arm, and let the old domain choose the sign of the root.

# Part 2 — Simplifier

Now the same functions and inverses again, built from lockers, vending machines and mirrors — same rules, same answers.

## Subtopic: One Ticket, One Prize

Picture a vending machine. You press a code, exactly one snack drops. That is a function: every input gets exactly one output, no exceptions. A machine that sometimes dropped two different snacks for the same code would be broken — and that broken machine is what mathematicians call a relation that is not a function. The rule y squared equals x is that broken machine: press 9 and both 3 and minus 3 tumble out.

On a graph you check for the broken machine with a vertical line. A vertical line is one single input; slide it across the picture, and if it ever touches the graph twice, that input has two outputs and the machine is broken. Sideways parabola: broken. Ordinary straight line: working.

Here is the twist that matters later. Two DIFFERENT codes are allowed to drop the SAME snack. Press 3 or press minus 3 on the machine y equals x squared and both drop a 9. Still a working machine — the promise is one snack per press, not one press per snack. Remember which direction the promise runs.

Quick check before we carry on — questions on spotting a true function are coming to you right now. One press, one snack, and slide the vertical line across the whole picture.

## Subtopic: Running the Machine Backwards

An inverse is the machine run in reverse: you hold the snack and ask which code produced it. If the machine y equals 2 x plus 3 turns the code 1 into the snack 5, the reverse machine must turn 5 back into 1.

The algebra of reversing is a swap. Trade the letters x and y, then tidy up by solving for y. For y equals 2 x plus 3: trade to get x equals 2 y plus 3, tidy to get y equals x minus 3, all over 2. Read the reversed machine as instructions and it even sounds like undoing: the original multiplied by 2 then added 3, so the reverse subtracts 3 then divides by 2 — the opposite operations in the opposite order, exactly like taking off shoes and socks.

Always trial the reversed machine with one real snack. The original sent 1 to 5; feed 5 into x minus 3 over 2 and out comes 1. If your reversed machine returns anything else, an algebra step slipped, and the trial catches it before the marker does.

Your questions for this part are up now. Trade the letters, undo the operations in reverse order, and trial the machine with a pairing you already know.

## Subtopic: The Mirror on the Diagonal and the Machine That Cannot Decide

Reversing pairings has a picture: the point 1 and 5 becomes the point 5 and 1, and swapping a point's coordinates flips it across the forty-five degree line y equals x. So the whole inverse graph is the original seen in a mirror lying along that diagonal. Sketching an inverse is nothing more than reflecting: swap the coordinates of the intercepts and redraw.

But run y equals x squared backwards and trouble arrives. You hold the snack 9 and ask which code produced it — and the machine shrugs: it could have been 3, it could have been minus 3. A reverse machine that cannot decide is not a function. The test for future trouble is the horizontal line drawn on the ORIGINAL: if some horizontal line touches the graph twice, two codes share a snack, and the reversal will shrug.

The fix is honest and simple: unplug half the machine. Allow only codes x greater than or equal to 0, and the right arm of the parabola remains — now every snack has exactly one code, and the reverse machine y equals the square root of x answers without hesitating. Choose the left arm instead, x less than or equal to 0, and the reverse answers with negative square root of x. One arm at a time, the parabola becomes reversible — and the old set of allowed codes tells you whether the root takes the plus sign or the minus sign.

And here come the last questions of the lesson, right now: mirror across the diagonal, horizontal line to predict the shrug, and keep one arm so the reverse machine can always decide.
