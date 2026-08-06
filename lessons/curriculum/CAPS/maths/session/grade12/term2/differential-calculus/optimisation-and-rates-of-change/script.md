# Part 1 — Expert

Sketching cubics was practice; this session is what calculus is FOR. The derivative measures rate of change, and setting it to zero finds the best possible value of anything expressible as a formula — the biggest enclosure, the cheapest box, the moment a moving object stops. Four movements: calculus of motion, the optimisation recipe, volume and surface problems, and the judgment that turns a calculus answer into a real-world one.

## Subtopic: Rates of Change and Motion

Wherever a quantity depends on time, its derivative with respect to time is its rate of change — and the first application is motion. If s of t gives the distance of an object from a fixed point at time t, then the derivative s prime of t is its VELOCITY, and the derivative of velocity is its ACCELERATION. Position, velocity, acceleration: each is the rate of change of the one before.

Worked case. A particle moves so that its distance in metres after t seconds is s of t equals two t cubed, minus nine t squared, plus twelve t. Velocity: six t squared, minus eighteen t, plus twelve. Factorise: six times t minus one, times t minus two. The velocity is zero at t equals 1 and t equals 2 — the particle is momentarily at rest at those instants. Between them the velocity is negative: the particle moves backwards from second one to second two, then forward again. Acceleration: differentiate again — twelve t minus eighteen, which is zero at t equals one comma five: the moment the deceleration turns into acceleration.

Read the language carefully, because the words map to calculus one to one. At rest, or momentarily stationary: velocity equals zero. Maximum height of a projectile: the height's derivative equals zero. Rate of change of anything at a given instant: differentiate, then substitute the instant. Initial velocity: substitute t equals zero into the velocity, giving twelve here.

One distinction protects marks: speed is the size of velocity. A velocity of minus three metres per second is a speed of three metres per second, direction reversed.

Pause here — the questions for this section are with you now. Differentiate for velocity, again for acceleration, and translate at rest into velocity equals zero before doing anything else.

## Subtopic: The Optimisation Recipe

Every maximisation and minimisation problem in this course surrenders to one recipe. Step one: name the variables and write the quantity to be optimised as a formula. Step two: use the constraint — the fixed perimeter, the fixed volume, the fixed total — to eliminate all variables but one. Step three: differentiate and set the derivative to zero. Step four: solve, check the candidate is genuinely a maximum or minimum, and answer the ACTUAL question asked.

The classic. A farmer has 120 metres of fencing and builds a rectangular camp against an existing straight wall, so only three sides need fence: two widths and one length. Let the width be x; then the length is 120 minus two x, and the area is A of x equals x times the quantity 120 minus two x, which is 120 x minus two x squared. Differentiate: A prime of x is 120 minus four x. Set to zero: x is 30. The camp is 30 metres wide and 60 metres long, area 1800 square metres. Confirm the maximum: the area function is a frowning parabola — negative squared coefficient — or note A double prime is minus four, negative, concave down. Maximum certified.

Two structural observations transfer to every such problem. The constraint is where the second variable dies: without the fixed 120, the area would grow without bound and the question would be meaningless. And the candidate from the derivative must be interpreted: x equals 30 is not the answer to every phrasing — the question might want the dimensions, the maximum area itself, or the length specifically. Read what is asked, answer what is asked.

Stop for this section's questions now — formula, constraint, differentiate, interpret: four steps, in that order, every time.

## Subtopic: Boxes, Volumes and Minimum Material

The three-dimensional family: a container must hold a fixed volume — what shape minimises the material? These questions marry the volume formula to the surface formula through the recipe.

Worked case. An open-topped box has a square base of side x and height h, and must hold 500 cubic centimetres. Minimise the material — the base plus four sides, with no lid. Volume constraint: x squared times h equals 500, so h equals 500 over x squared. Surface: S equals x squared plus four x h. Substitute the constraint: S of x equals x squared plus four x times 500 over x squared — which is x squared plus 2000 over x. One variable; the recipe may proceed. Differentiate, writing the quotient as a power first: S prime of x equals two x minus 2000 over x squared. Set to zero: two x equals 2000 over x squared, so x cubed equals 1000 and x is 10. Then h is 500 over 100 — 5 centimetres — and the minimum material is 100 plus 2000 over 10: 300 square centimetres.

Confirm it is a minimum: S double prime is two plus 4000 over x cubed, positive for positive x — concave up everywhere on the sensible domain, so the candidate is the genuine minimum. Notice the shape of the answer: the height is half the base side. Open-top square boxes always minimise at h equal to x over two — a pattern worth recognising, never worth assuming without proof.

The negative-exponent differentiation is where the marks leak: 2000 over x is 2000 x to the minus one, whose derivative is MINUS 2000 x to the minus two. Sign first, then power.

The questions on this section are in front of you now — constraint kills a variable, surface gets differentiated, and the derivative of one over x carries a minus sign.

## Subtopic: Interpreting the Answer — Domains, Endpoints and Sense

Calculus proposes; the context disposes. A derivative-zero candidate is only an answer if it survives three interrogations. First: is it inside the sensible domain? Lengths must be positive; a width of minus 30 solves the same equation and means nothing. State the domain early — here zero strictly less than x strictly less than 60, since 120 minus two x must stay positive — and reject outsiders in writing. Second: is it the right TYPE of extremum? A zero derivative can mark a minimum when a maximum is wanted; classify with the second derivative or a sign check, one line. Third: does the question ask for the location, the optimal value, or a consequence? The x, the A of x, or something built from them.

A worked interpretation. Suppose profit in rand from selling n hundred vetkoek is modelled by P of n equals minus two n cubed plus thirty n squared minus ninety n for n between zero and twelve. P prime of n is minus six n squared plus sixty n minus ninety — set to zero and divide by minus six: n squared minus ten n plus fifteen equals zero. The formula gives n equals five plus or minus the square root of ten — about one comma eight four and eight comma one six. Both lie in the domain; the second derivative, minus twelve n plus sixty, is positive at the smaller root and negative at the larger: the smaller is a local MINIMUM of profit, the larger the local maximum. The answer to, what sales level maximises profit, is about eight hundred and sixteen vetkoek — the other root, though it also zeroes the derivative, answers nothing that was asked.

Endpoints matter too: on a closed bracket of allowed values, the best value can sit at the boundary with no zero derivative at all — check the ends whenever the domain has them.

The final questions of this part are with you now — domain first, classify the candidate, and let the question's own wording choose what number you finally report.

# Part 2 — Simplifier

Now the same optimisation and rates from a kraal, a tuckshop cash tin and a bakkie's dashboard — same recipe, same answers, built from things you can picture.

## Subtopic: The Dashboard and the Handbrake

A bakkie drives away from a farm gate. Its distance from the gate keeps changing, and the dashboard tells the story of that change: the odometer shows POSITION, the speedometer shows how fast position is changing — that is the derivative of position — and the push in your back when the driver floors it is ACCELERATION, how fast the speed itself is changing. Differentiate once for speed, once more for acceleration. Three gauges, each the rate of change of the last.

Now the phrase every exam uses: momentarily at rest. Picture the bakkie rolling forward, stopping, reversing to the gate, stopping again, pulling forward. At each stop the speedometer touches zero for an instant — that is the handbrake moment, and in symbols it is simply velocity equals zero. Given distance two t cubed minus nine t squared plus twelve t, differentiate to six t squared minus eighteen t plus twelve, factorise, and the handbrake moments are t equals 1 and t equals 2. Between those seconds the velocity runs negative — the bakkie is reversing — and afterwards positive again.

One dashboard subtlety: the speedometer never shows a minus sign, but velocity does. Velocity minus three means speed three, backwards. Exam wording chooses its gauge deliberately — when asked for speed, strip the sign; when asked for velocity, keep it, direction and all.

Quick check before we carry on — questions on the moving bakkie are coming to you right now. Position, then speed, then push: differentiate once per gauge, and at rest always means speedometer zero.

## Subtopic: The Biggest Kraal on a Fixed Roll of Fence

You have one roll of fencing, 120 metres, and a long farm wall to build against. Fence out a skinny sliver two metres wide and it holds nothing; fence a strip so deep it uses all the wire on the two sides and none is left for the front — also nothing. Somewhere between the extremes hides the best kraal, and calculus finds it without trial and error.

Set it up like a story with one unknown. Call the width x. The wall covers one long side free of charge, so the fence must supply two widths and one front: the front gets 120 minus two x. Area: x times 120 minus two x. That formula is a frowning parabola — zero area at both silly extremes, biggest somewhere between — and the top of the frown is where the slope of the area graph is zero. Differentiate: 120 minus four x. Set to zero: x is 30. Width 30, front 60, area 1800 square metres. No guessing, no table of attempts: the derivative walked straight to the top of the hill.

The shape of the reasoning is the recipe you will reuse forever. Write the thing you want as a formula. Use the fixed total — the roll of fence — to get down to ONE letter. Differentiate, set to zero, solve. Then stand back and make sure the number is sensible: a width of 30 fits the roll, leaves a positive front, and beats its neighbours — try 29 or 31 and watch the area dip.

Your questions for this part are up now. One letter before differentiating, zero slope at the best design, and always ask whether your answer would survive on an actual farm.

## Subtopic: The Cheapest Tin That Holds Enough

Flip the last question inside out. There, the material was fixed and the space was maximised. Here, the SPACE is fixed — a tin must hold 500 cubic centimetres — and the material is minimised, because on a real production line, material is money. Same recipe, opposite direction.

The open-topped square tin: base side x, height h, no lid. The holding requirement chains the two letters together: x squared times h must be 500, so the height is forced to be 500 over x squared — a wide tin is automatically a shallow one. Material: the base, x squared, plus four walls, four x h — and substituting the forced height turns everything into one letter: x squared plus 2000 over x.

Feel the tug of war before calculating. Wide tin: enormous base, tiny walls. Tall skinny tin: tiny base, endless walls. The cheapest design balances the two costs, and the balance point is where the material graph runs flat. Differentiate — careful with the fraction: 2000 over x is 2000 x to the minus one, derivative MINUS 2000 over x squared — set two x minus 2000 over x squared to zero, and x cubed is 1000. Base 10 by 10, height 5, material 300 square centimetres. The winning tin is half as tall as it is wide — squat, like most real tins on a spaza shelf, and now you know why.

And here come the last questions of the lesson, right now: fixed space forces the height, one letter enters the derivative, the fraction's minus sign survives, and the flattest point of the cost curve is where the factory saves its money.
