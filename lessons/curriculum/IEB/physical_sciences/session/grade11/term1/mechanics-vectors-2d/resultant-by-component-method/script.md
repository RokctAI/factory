# Part 1 — Expert

Last year every force and displacement you met lived on a single straight line, and adding them was a matter of plus and minus signs. This year the arrows escape onto the full Cartesian plane, where a vector may lean at any angle it likes. This session builds the one procedure that handles every such situation: resolve each vector into perpendicular components, add the components in separate columns, then reassemble a single resultant with Pythagoras and the inverse tangent. The same machinery carries you through Newton's laws on slopes and through electrostatics in two dimensions, so the time invested here pays off for the whole year.

## Subtopic: Resultants, Tail-to-Head and the Closed Diagram

Definitions carry marks, so state them cleanly. A VECTOR has both magnitude and direction; a SCALAR has magnitude only. The RESULTANT of two or more vectors is the single vector that has the same effect as all of them acting together.

Now build the picture. A delivery trolley at a Midrand depot is dragged by two ropes: one pulls with 45 newtons due east, the other with 60 newtons due north. In the TAIL-TO-HEAD construction you draw the first arrow, 45 newtons pointing right. From the head of that arrow — the sharp end — you begin the second arrow, 60 newtons pointing straight up. The resultant is the single arrow drawn from the tail of the very first vector to the head of the very last one: the diagonal closing the rectangle those two arrows outline. That diagonal turns out to be exactly 75 newtons, leaning up and to the right, and the fourth subtopic will prove the number.

The TAIL-TO-TAIL construction, also called the parallelogram method, starts both arrows from one shared point and completes the parallelogram. The diagonal running from the shared tail to the far corner is the resultant, and it agrees exactly with the tail-to-head answer. Two drawings, one truth.

One special construction deserves its own sentence: the CLOSED vector diagram. If three or more vectors drawn tail-to-head finish with the last arrowhead landing precisely on the first tail, the diagram is closed. A closed diagram means the resultant is zero, and an object under those forces is in EQUILIBRIUM. Reverse the idea and you get a useful definition: the single force that would close a non-zero diagram — equal in magnitude to the resultant but opposite in direction — is called the EQUILIBRANT.

Keep that vocabulary sharp, because the questions for this section are with you now: vector against scalar, the two graphical constructions, and what a closed diagram announces about the net force.

## Subtopic: Resolving a Vector into Perpendicular Components

A ruler and protractor are honest tools, but they cannot deliver three significant figures. The component method swaps drawing for arithmetic.

To RESOLVE a vector is to replace it by two perpendicular vectors — one along the x-axis, one along the y-axis — whose combined effect is identical to the original. Say the two formulae aloud as you write them. R sub x equals R cosine theta: the x-component is the magnitude multiplied by the cosine of the angle. R sub y equals R sine theta: the y-component is the magnitude multiplied by the sine of the same angle.

Everything hangs on where theta is measured from, and this is exactly where marks leak away. Those formulae assume theta sits between the vector and the x-axis. If a question quotes the angle from the VERTICAL instead, sine and cosine trade places. The protection is a sketch, every single time: draw the small right-angled triangle with the vector as its hypotenuse. The component lying ADJACENT to the marked angle takes cosine; the component OPPOSITE the marked angle takes sine. Adjacent means cosine, opposite means sine — that sentence outperforms any memorised letter pattern.

Work one through. A winch cable at a Richards Bay harbour pulls a container with 300 newtons at 40 degrees above the horizontal. Formula: F sub x equals F cosine theta. Substitution: F sub x equals 300 newtons times cosine 40 degrees, which is 300 times 0,766. Answer: 229,8 newtons, horizontally forward. Formula: F sub y equals F sine theta. Substitution: 300 newtons times sine 40 degrees, which is 300 times 0,643. Answer: 192,8 newtons, vertically upward. One slanted cable has become two straight pulls that can be treated completely separately.

Direction travels in the signs, so declare a convention before any arithmetic: east and north positive, west and south negative. A 150 newton force due west is recorded as x equals negative 150 newtons, y equals zero. The dropped minus sign is the single most expensive slip in this topic — it swings the final direction by tens of degrees.

Take this section's questions now, checking carefully which axis each angle is measured from and which components must go in as negatives.

## Subtopic: Adding the Components of Four Forces

Once every vector is resolved, addition is pure bookkeeping. The rule: the x-components add up to give R sub x, and the y-components add up to give R sub y. Sideways parts never mix with vertical parts.

Consider four forces acting on a steel anchor plate in an engineering workshop. Force one: 300 newtons at 40 degrees above the horizontal, leaning east and upward. Force two: 140 newtons due north. Force three: 150 newtons due west. Force four: 60 newtons due south.

Resolve each one into a two-column table that you physically draw. Force one, straight from the previous subtopic: x equals positive 229,8 newtons, y equals positive 192,8 newtons. Force two lies entirely on the y-axis: x equals 0, y equals positive 140 newtons. Force three lies flat on the x-axis pointing west: x equals negative 150 newtons, y equals 0. Force four points due south: x equals 0, y equals negative 60 newtons.

Now total each column. R sub x equals 229,8 plus 0 minus 150 plus 0. Answer: R sub x equals 79,8 newtons, positive, therefore east. R sub y equals 192,8 plus 140 plus 0 minus 60. Answer: R sub y equals 272,8 newtons, positive, therefore north.

Pause and read the result: four awkward arrows have collapsed into exactly two perpendicular ones — 79,8 newtons east and 272,8 newtons north. Any number of vectors reduces the same way, which is what makes this method stronger than any drawing.

Two habits protect the marks. Resolve EVERY vector, including those already lying on an axis — writing x equals 0 for the northward force is written proof that nothing was forgotten. And never round components early: carry 229,8 forward, not 230, because early rounding drifts into the final angle.

The questions for this section are in front of you now: resolve all four forces, then total the two columns without mislaying a single minus sign.

## Subtopic: Magnitude by Pythagoras, Direction by Trigonometry

Two perpendicular vectors become one through the oldest theorem you own. The magnitude of the resultant equals the square root of R sub x squared plus R sub y squared. The direction comes from the tangent ratio: tangent theta equals R sub y over R sub x, so theta is the inverse tangent of that quotient.

Finish the anchor-plate problem. Formula: R equals the square root of R sub x squared plus R sub y squared. Substitution: the square root of 79,8 squared plus 272,8 squared, which is the square root of 6 368,04 plus 74 419,84, which is the square root of 80 787,88. Answer: R equals 284,2 newtons. Formula: theta equals the inverse tangent of R sub y divided by R sub x. Substitution: the inverse tangent of 272,8 divided by 79,8, which is the inverse tangent of 3,419. Answer: theta equals 73,7 degrees. Full statement: the resultant force is 284,2 newtons at 73,7 degrees north of east. A magnitude without a direction is an incomplete answer to a vector question and is marked as incomplete.

Now confirm the depot trolley from the first subtopic: 45 squared is 2 025 and 60 squared is 3 600, which total 5 625, and the square root of 5 625 is exactly 75 newtons, at the inverse tangent of 60 over 45, which is 53,1 degrees north of east.

Three traps, named without mercy. One: a calculator in radian mode. An inverse tangent that returns 1,29 instead of 73,7 is a mode error, so confirm the display shows DEG before the first keystroke. Two: the quadrant. The inverse tangent button only ever answers between negative 90 and positive 90 degrees, so a negative R sub x forces you to add 180 degrees — or, better, state the angle relative to a named axis. Three: answer in the language the question used — "north of east", "above the horizontal", or as a bearing measured clockwise from north, in which case 73,7 degrees north of east becomes a bearing of 16,3 degrees.

That completes the method, and the final questions of this part are with you now: Pythagoras on the two column totals, the inverse tangent with its quadrant respected, and the direction stated in full.

# Part 2 — Simplifier

Now the same two-dimensional vectors on the streets around your own house, where the grid of roads has been quietly teaching you this topic your whole life.

## Subtopic: Walking to the Shop the Long Way

The streets in your neighbourhood run in only two directions: east-west and north-south. You leave your gate, walk 90 metres east down one road, then turn left and walk 120 metres north up the next. Your legs have done 210 metres of pavement. But how far are you from home?

Not 210 metres. A hadeda taking off from your roof and flying straight to where you stand would cover only 150 metres. That straight flight is the RESULTANT: the one single trip that puts you in exactly the same spot as the whole zigzag journey did. Every vector question you will ever meet is secretly asking the same thing — never mind the journey, give me the one arrow that finishes the job.

There is a way to see this with no numbers at all. Draw your first walk as an arrow. Start your second arrow where the first one's tip ends — nose to tail, like taxis queuing at a rank. Then rule one long arrow from where you began to where you ended. That long arrow is the answer, and it could not care less about the order of the walking: north first and east second delivers you to the identical corner.

And treasure the special case: if your wandering brings you back through your own gate, the final arrow has no length whatsoever. In the language of forces, everything has cancelled and nothing accelerates — the object is balanced, in equilibrium.

That is a genuine piece of physics understood without one calculation. The questions on this section are waiting for you now — think about trips, tips and tails, and the walk that ends where it started.

## Subtopic: Splitting One Push into Two Honest Pushes

Trouble arrives when a force refuses to follow the road. Picture dragging a heavy hockey bag across the school field with the strap over your shoulder — the strap slopes upward, so your pull is not fully forward and not fully upward. It is doing two jobs at once.

So do what a tuck-shop owner does at closing time with a drawer of mixed coins: sort it into piles. One pile is the FORWARD part of your pull — the part actually sliding the bag across the grass. The other pile is the UPWARD part — the part gently unloading weight off the ground. Put the two piles together and they do precisely what the slanted strap was doing. Nothing invented, nothing lost, only sorted.

How much lands in each pile? The slope of the strap decides. A strap pulled almost flat is nearly all forward motion and hardly any lift; a strap pulled almost vertical lifts plenty and drags almost nothing. The two calculator buttons that convert a slope into a share are cosine and sine.

Choosing between them is a picture, never a chant. Sketch the right-angled triangle with the slanted pull as the long side. The short side lying snug against your marked angle takes cosine; the side standing across from the angle takes sine. Snug against it: cosine. Facing it: sine.

Feed in real numbers: a 300 newton pull on a strap sloping 40 degrees up. The forward pile is 300 times cosine 40, which is 300 times 0,766, giving 229,8 newtons. The upward pile is 300 times sine 40, which is 300 times 0,643, giving 192,8 newtons. One awkward slanted pull, two obedient numbers. Final rule: anything aimed west or south wears a minus sign, exactly the way airtime you owe appears as a minus on the statement.

Your questions for this section are arriving now — practise the sorting, and guard the minus signs like money.

## Subtopic: Two Piles, One Answer

The last move is the easiest. Once every force is split into a sideways pile and an upward pile, each pile is added on its own. Sideways with sideways, upward with upward — you would never add rands to kilometres, and you never add an eastward pull to a northward one.

Run the anchor plate from the workshop. Four forces act on it. The sideways parts: 229,8 east, nothing, 150 west, nothing. Let the minus sign work: 229,8 minus 150 leaves 79,8 newtons pulling east. The upward parts: 192,8 north, 140 north, nothing, 60 south. Add: 192,8 plus 140 minus 60 leaves 272,8 newtons pulling north. Four forces have quietly become two.

Two forces at right angles is the hadeda-flight problem from the first section of this part. Square, add, root: 79,8 squared is 6 368,04; 272,8 squared is 74 419,84; the total is 80 787,88; its square root is 284,2. The plate is being pulled with 284,2 newtons. For the direction, divide the upward pile by the sideways pile — 272,8 over 79,8 gives 3,419 — and ask the inverse tangent button which angle owns that tangent. It answers 73,7 degrees. The pull is 284,2 newtons, tilted 73,7 degrees from east towards north.

Never submit the number naked. A vector answer without a direction is a taxi fare without a destination — half the information, half the marks. Size first, then where it points.

Three moves and the topic is yours: split every force into two piles, add each pile separately, rebuild one arrow at the end. Confirm the calculator says degrees, respect every minus sign, and this becomes one of the most dependable sources of marks in your exams. The last questions of the lesson are with you now — work them calmly, one pile at a time.
