# Part 1 — Expert

An algebraic equation like two x minus one equals zero has one answer. A trigonometric equation like two cosine x minus one equals zero has infinitely many, because the trigonometric functions repeat forever. This session builds the tool that captures all of them in one line — the general solution — then shows how to harvest the particular answers an interval demands, and how to crack the equation that is secretly a quadratic in disguise.

## Subtopic: Why One Equation Has Infinitely Many Answers

Solve sine x equals zero comma five, thinking only of angles from zero to three hundred and sixty degrees. The calculator's inverse sine gives thirty degrees — but that is one answer, not the answer. Sine is positive in two quadrants, the first and the second, so a second solution hides at one hundred and eighty minus thirty: one hundred and fifty degrees. Check it against the reduction formulae: sine of one eighty minus theta equals sine theta, so sine of one fifty is sine of thirty. Two solutions in the first turn: thirty and one hundred and fifty degrees.

Now remove the fence. Turn past three hundred and sixty degrees and the wheel repeats: three hundred and ninety degrees points exactly where thirty pointed, so sine of three ninety is also zero comma five. Subtract a turn instead and minus three hundred and thirty degrees works too. Every full turn of three hundred and sixty degrees, forwards or backwards, reproduces both solutions. Infinitely many answers, and no list could ever hold them.

The method that organises this is fixed, and you should run it the same way every time. Step one: find the reference angle — the acute angle whose ratio matches the size of the given value, ignoring its sign. Step two: use the sign of the value to choose the two quadrants. Step three: write the solutions in the first turn. Step four: add k full periods, where k is any integer — positive, negative or zero.

The single idea underneath: the calculator answers once; the quadrants double it; the period multiplies it forever.

Pause here — the questions for this section are with you now. They probe why inverse sine alone is never the full answer, and where the second quadrant solution comes from.

## Subtopic: The General Solution for Sine and Cosine

Write the machinery of the last section as formulae. If sine x equals a value whose reference angle is alpha, and the value is positive, the general solution is: x equals alpha plus k times three hundred and sixty degrees, or x equals one hundred and eighty degrees minus alpha plus k times three hundred and sixty degrees, with k an integer. Two families, each repeating every full turn.

For cosine the two quadrants sit symmetrically above and below the x-axis, so the two families collapse into a plus-minus: if cosine x equals a value with reference angle alpha, then x equals plus or minus alpha, plus k times three hundred and sixty degrees.

Work one of each. Two cosine x minus one equals zero. Isolate first: cosine x equals zero comma five. The reference angle is sixty degrees, and the value is positive, so x equals plus or minus sixty degrees plus k times three sixty. Test a few: sixty works; minus sixty, which is the same direction as three hundred degrees, works because cosine is positive in the fourth quadrant; four hundred and twenty works.

Now a negative value, where the sign discipline earns its keep. Solve two sine x plus one comma two equals zero. Isolate: sine x equals minus zero comma six. Reference angle: inverse sine of plus zero comma six is thirty-six comma eight seven degrees. Sine is negative in the third and fourth quadrants. Third quadrant: one eighty plus the reference, two hundred and sixteen comma eight seven degrees. Fourth quadrant: three sixty minus the reference, three hundred and twenty-three comma one three degrees. General solution: x equals two sixteen comma eight seven plus k three sixty, or x equals three twenty-three comma one three plus k three sixty.

The classic error is feeding the minus into the calculator. Inverse sine of minus zero comma six returns minus thirty-six comma eight seven degrees, and learners then bolt quadrant rules onto an already-negative angle and double-count the sign. Keep the roles separate: the calculator finds the size using the positive value; the quadrants place the sign. Never both at once.

Stop for this section's questions now — isolate the ratio first, take the reference angle from the positive value, and let the quadrants do the placing.

## Subtopic: Tangent, and Equations That Need Tidying First

Tangent repeats faster than the other two. Its period is one hundred and eighty degrees, not three hundred and sixty — the reduction formula for one eighty plus theta says tangent keeps both its size and its sign after half a turn. So tangent needs only one family: if tangent x equals a value with reference angle alpha, then x equals alpha plus k times one hundred and eighty degrees when the value is positive, and x equals one eighty minus alpha plus k times one eighty when the value is negative.

Work both flavours. Tangent x equals one: reference angle forty-five, positive value, so x equals forty-five plus k times one eighty. That single line already contains forty-five and two hundred and twenty-five degrees inside the first turn. Tangent x equals minus two comma five: reference angle is inverse tangent of two comma five, sixty-eight comma two degrees. Tangent is negative in the second quadrant: one eighty minus sixty-eight comma two is one hundred and eleven comma eight degrees. General solution: x equals one eleven comma eight plus k times one eighty.

Now the tidying. Most examination equations do not arrive as a bare ratio equals a number; they need one legal move first. Watch this one: sine x equals cosine x. Divide both sides by cosine x, and the left side becomes tangent x, giving tangent x equals one, so x equals forty-five plus k one eighty. But dividing by something that might be zero needs a defence, and here it exists: if cosine x were zero, then sine x would be plus or minus one, and the equation would read plus or minus one equals zero — impossible. So cosine x is not zero for any solution, the division is safe, and no answers were lost. Write that sentence in your solution; it is the mark that separates the top scripts.

The general warning generalises from the previous topic: never divide an equation by sine x, cosine x, or any expression in x, unless you first show it cannot be zero — or factorise instead, so the factor delivers its own solutions.

The questions for this section arrive now — remember the short period of tangent, and defend every division before you make it.

## Subtopic: Specific Intervals and the Hidden Quadratic

The general solution is an infinite net; an interval question asks you to land only the fish inside a stretch of river. The technique: write the general solution, then substitute integer values of k — minus two, minus one, zero, one, two — and keep every result inside the interval, discarding the rest.

Take sine x equals zero comma five on the interval from minus three sixty to three sixty degrees. General solution: x equals thirty plus k three sixty, or x equals one fifty plus k three sixty. First family: k equals zero gives thirty; k equals one gives three ninety — outside, discard; k equals minus one gives minus three thirty — inside, keep. Second family: k equals zero gives one fifty; k equals minus one gives minus two ten — inside, keep. Four solutions: minus three thirty, minus two ten, thirty, and one fifty degrees. Count them against a mental sketch of the sine wave: two crossings per full turn, two full turns in the interval, four crossings. The sketch confirms the count, and examiners award method marks for exactly that check.

Now the heavyweight: the trigonometric equation that is secretly a quadratic. Solve two sine squared x minus sine x minus one equals zero, for x from zero to three sixty. Substitute: let s stand for sine x. The equation reads two s squared minus s minus one equals zero. Factorise: two s plus one, times s minus one. So s equals minus a half, or s equals one.

Each value becomes its own small equation. Sine x equals minus a half: reference angle thirty, sine negative in the third and fourth quadrants — two hundred and ten, and three hundred and thirty degrees. Sine x equals one: a boundary value, sitting at the top of the wheel — ninety degrees, no second quadrant partner because it is its own mirror image. Full answer on the interval: ninety, two hundred and ten, and three hundred and thirty degrees.

Two disciplines close the topic. First, if the substitution ever produces a value outside minus one to one for sine or cosine, reject it in writing — those functions never leave that range, and the written rejection earns its mark. Second, boundary values — zero, one, and minus one — deserve a sketch rather than the quadrant machine, because they sit on the axes where the quadrants meet.

The final questions of this part are with you now — harvest the interval with integer values of k, factorise the disguised quadratic, and reject impossible values out loud.

# Part 2 — Simplifier

Now the same solving, told through a taxi timetable and a hall with two doors — same rules, same answers, and a way of seeing why the answers never run out.

## Subtopic: The Taxi on a Loop

A taxi runs a fixed loop through town, and you spot it passing your gate at seven in the morning. If the loop takes exactly one hour, when else will it pass? Eight, nine, ten — and it also passed at six, and at five. One sighting plus the loop time gives you every sighting, past and future: seven o'clock plus k hours, where k is any whole number, positive for the future, negative for the past.

That is precisely what a general solution is. The equation sine x equals zero comma five is the question: when does the wheel's north-south share equal a half? You catch one moment — thirty degrees — and because the wheel repeats every three hundred and sixty degrees, thirty plus k three sixty catches every moment of that kind forever. The letter k is not a mystery variable; it is a counter for how many full loops you fast-forward or rewind.

Tangent's loop is shorter — one hundred and eighty degrees, half a turn — because tangent is the ratio of the two shares, and half a turn flips the sign of both, top and bottom, leaving the fraction unchanged. Same taxi, tighter loop, so its k counts halves.

One habit follows immediately: never stop at the calculator's single answer. The calculator tells you one time the taxi passed. The timetable — the general solution — is what the question wants.

Quick check before we carry on — questions on this section come to you now. For each, ask: what is the loop time, and what is the one sighting I anchor to?

## Subtopic: Two Doors Into the Hall

There is a second complication the taxi misses: within each loop, sine usually hits a value twice. Picture the big wheel at a fun fair. On the way up, your height above the axle passes the halfway mark once — and on the way down it passes the same height again. Same height, two moments. That is why sine x equals zero comma five has two families: thirty degrees on the way up, and one hundred and eighty minus thirty — one fifty — on the way down. Two doors into the same hall, and the general solution must list both, each with its own plus k three sixty.

Cosine's two doors sit symmetrically left and right — a positive angle and its negative twin — which is why its general solution compresses to plus or minus the reference angle, plus k three sixty.

Negative values just move the doors. Sine x equals minus zero comma six means the seat is below the axle, which happens in the third and fourth quarters of the turn. The routine stays calm and identical: get the size of the angle from the positive value — thirty-six comma eight seven degrees — then place it: one eighty plus it for the third quarter, three sixty minus it for the fourth. Size from the calculator, placing from the wheel. The moment you type the minus into the calculator, the machine places the angle for you, in its own favourite spot, and your quadrant work doubles up on the sign.

The very top and bottom of the wheel are special: at the peak — sine equal to one — the way up and the way down meet, the two doors become one, and the equation has a single family: ninety plus k three sixty.

Your questions for this part are up now. Find the size, then choose the doors — and remember the peak and the floor have only one door each.

## Subtopic: Harvesting the Stretch You Were Given

An interval question is a fishing permit: the river is infinite, but you may only keep what you catch between two markers. The general solution is your net for the whole river; the harvesting is substitution.

Say the timetable reads thirty plus k three sixty, or one fifty plus k three sixty, and your permit covers minus three sixty to three sixty. Run k through small integers, family by family, and test each catch. Thirty: inside, keep. Three ninety: past the marker, throw back. Minus three thirty: inside, keep. One fifty: keep. Minus two ten: keep. The haul: minus three thirty, minus two ten, thirty, one fifty. Four fish. And you can predict the count before you fish — the wave crosses any middle height twice per loop, and the permit covers two loops, so four crossings. If your list has three or five, something fell out of the net.

The disguised quadratic works like a locked toolbox with an ordinary padlock. Two sine squared x minus sine x minus one looks frightening until you give sine x a nickname — call it s — and the line becomes two s squared minus s minus one, homework from last term. It factorises into two s plus one, times s minus one, so s is minus a half or one. Swap the nickname back and you hold two small equations, each solved with the doors and the timetable from before.

One last guard at the gate: sine and cosine live between minus one and one, always — the seat on the wheel cannot be further from the axle than the wheel is wide. If the nickname hands you sine x equals two, reject it in writing and move on. That written rejection is not an apology; it is mathematics, and it is worth a mark.

And here come the last questions of the lesson, right now: write the timetable, run the counter through the permit, and turn every scary quadratic into last term's homework with a nickname.
