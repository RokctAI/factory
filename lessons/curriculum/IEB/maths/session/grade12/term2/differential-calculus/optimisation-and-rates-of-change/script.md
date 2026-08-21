# Part 1 — Expert

Sketching cubics was the training ground; this session is the purpose. The derivative measures rate of change, and setting it to zero locates the best possible value of anything a formula can describe — the largest enclosure, the cheapest container, the instant a moving object halts. Four movements today: the calculus of motion, the optimisation recipe, volume-and-material problems, and the judgment that converts a calculus answer into a real-world one.

## Subtopic: Rates of Change and Motion

Whenever a quantity depends on time, its derivative with respect to time is its rate of change — and motion is the flagship application. If s of t records an object's distance from a fixed point at time t, then s prime of t is its VELOCITY, and the derivative of velocity is its ACCELERATION. Position, velocity, acceleration: a chain in which each link is the rate of change of the one before it.

Worked case. A particle moves so that its distance in metres after t seconds is s of t equals two t cubed, minus fifteen t squared, plus twenty-four t. Velocity: six t squared, minus thirty t, plus twenty-four. Factorise: six times t minus one, times t minus four. Velocity is zero at t equals 1 and t equals 4 — at those instants the particle is momentarily at rest. Between them the velocity runs negative: from second one to second four the particle travels backwards, then forwards again. Acceleration: differentiate once more — twelve t minus thirty, zero at t equals two comma five: the instant the slowing-down flips into speeding-up.

Learn the phrase book, because the words translate to calculus one for one. At rest, or momentarily stationary: velocity equals zero. Maximum height of a projectile: the height's derivative equals zero. Rate of change of anything at a stated instant: differentiate, then substitute that instant. Initial velocity: substitute t equals zero into the velocity — twenty-four here.

One guarded distinction: speed is the magnitude of velocity. A velocity of minus five metres per second is a speed of five metres per second with the direction reversed.

Pause here — the questions for this section are with you now. Differentiate for velocity, again for acceleration, and translate at rest into velocity equals zero before touching anything else.

## Subtopic: The Optimisation Recipe

Every maximising and minimising problem in this course falls to one recipe. Step one: name your variables and express the quantity being optimised as a formula. Step two: deploy the constraint — the fixed fencing, the fixed volume, the fixed total — to eliminate every variable but one. Step three: differentiate and set the derivative to zero. Step four: solve, verify the candidate really is the maximum or minimum wanted, and answer the question ACTUALLY asked.

The classic. A farmer has 160 metres of fencing and lays out a rectangular camp against an existing straight wall, so only three sides need fencing: two widths and one length. Let the width be x; the length is then 160 minus two x, and the area is A of x equals x times the quantity 160 minus two x, which is 160 x minus two x squared. Differentiate: A prime of x is 160 minus four x. Set to zero: x is 40. The camp measures 40 metres by 80 metres, area 3200 square metres. Confirm the maximum: the area function is a frowning parabola — negative squared coefficient — or observe that A double prime is minus four, negative, concave down. Maximum certified.

Two structural lessons carry into every such problem. The constraint is where the second variable dies: without the fixed 160 metres, the area could grow forever and the question would collapse. And the derivative's candidate still needs interpreting: x equals 40 does not answer every phrasing — the question may want the dimensions, the maximum area itself, or the length alone. Read what is asked; report what is asked.

Stop for this section's questions now — formula, constraint, differentiate, interpret: four steps, in that order, always.

## Subtopic: Boxes, Volumes and Minimum Material

The three-dimensional family: a container must hold a fixed volume — which shape spends the least material? These problems marry the volume formula to the surface formula through the recipe.

Worked case. An open-topped box has a square base of side x and height h, and must hold 108 cubic centimetres. Minimise the material — one base and four walls, no lid. Volume constraint: x squared times h equals 108, so h equals 108 over x squared. Surface: S equals x squared plus four x h. Substitute the constraint: S of x equals x squared plus four x times 108 over x squared — which is x squared plus 432 over x. One variable remains; the recipe may fire. Differentiate, dressing the fraction as a power first: S prime of x equals two x minus 432 over x squared. Set to zero: two x equals 432 over x squared, so x cubed equals 216 and x is 6. Then h is 108 over 36 — 3 centimetres — and the minimum material is 36 plus 432 over 6: 108 square centimetres.

Confirm the minimum: S double prime is two plus 864 over x cubed, positive for every positive x — concave up across the whole sensible domain, so the candidate is the genuine minimum. Notice the answer's proportions: the height is half the base side. Open-topped square boxes always minimise at h equal to x over two — a pattern worth recognising, never worth assuming without proof.

The negative-exponent differentiation is where the marks leak away: 432 over x is 432 x to the minus one, whose derivative is MINUS 432 x to the minus two. Sign first, then power.

The questions on this section are in front of you now — the constraint kills a variable, the surface gets differentiated, and the derivative of one over x arrives with a minus sign.

## Subtopic: Interpreting the Answer — Domains, Endpoints and Sense

Calculus proposes; the context decides. A zero-derivative candidate becomes an answer only after surviving three interrogations. First: does it live in the sensible domain? Lengths must be positive; a width of minus 40 solves the same equation and means nothing on a farm. Declare the domain early — here zero strictly less than x strictly less than 80, because 160 minus two x must stay positive — and reject trespassers in writing. Second: is it the right KIND of extremum? A zero derivative can flag a minimum when a maximum was wanted; classify with the second derivative or a one-line sign check. Third: does the question want the location, the optimal value, or something built from them? The x, the A of x, or a consequence.

A worked interpretation. Suppose the profit in rand from selling n hundred koeksisters is modelled by P of n equals minus n cubed plus twelve n squared minus twenty-one n, for n between zero and ten. P prime of n is minus three n squared plus twenty-four n minus twenty-one — set to zero and divide by minus three: n squared minus eight n plus seven equals zero, factorising to n minus one, times n minus seven: n equals 1 or 7. Both sit inside the domain. The second derivative, minus six n plus twenty-four, is positive at n equals 1 and negative at n equals 7: the smaller root is a local MINIMUM of profit, the larger the local maximum. The answer to, what sales level maximises profit, is seven hundred koeksisters — the other root, though it too zeroes the derivative, answers nothing that was asked.

Endpoints deserve their own glance: on a closed range of allowed values, the best value can sit on the boundary with no zero derivative anywhere near it — inspect the ends whenever the domain has them.

The final questions of this part are with you now — domain first, classify the candidate, and let the question's own wording pick the number you finally report.

# Part 2 — Simplifier

Now the same rates and optimisation from a delivery bakkie's dashboard, a kraal beside a farm wall, and a tin on a shop shelf — same recipe, same answers, built from pictures.

## Subtopic: The Dashboard and the Handbrake

A bakkie pulls away from a depot gate. Its distance from the gate is always changing, and the dashboard reports on that change in layers: the odometer holds POSITION, the speedometer holds how quickly position is changing — the derivative of position — and the shove into your seat when the driver flattens the pedal is ACCELERATION, how quickly the speed itself is changing. Differentiate once for speed, once again for acceleration. Three gauges, each one the rate of change of the gauge before.

Now for the phrase every question loves: momentarily at rest. Picture the bakkie driving out, stopping, reversing back toward the gate, stopping again, then heading out for good. At each stop the speedometer needle kisses zero for one instant — the handbrake moment — and in symbols it is nothing more than velocity equals zero. Given distance two t cubed minus fifteen t squared plus twenty-four t, differentiate to six t squared minus thirty t plus twenty-four, factorise, and the handbrake moments land at t equals 1 and t equals 4. Between those seconds the velocity is negative — the bakkie is reversing — and after the second stop it runs positive again.

One dashboard subtlety: a speedometer never displays a minus sign, but velocity carries one. Velocity minus five means speed five, travelling backwards. Question wording picks its gauge on purpose — asked for speed, drop the sign; asked for velocity, keep it, direction included.

Quick check before we carry on — questions on the moving bakkie are coming to you right now. Position, then speed, then shove: one differentiation per gauge, and at rest always means the needle on zero.

## Subtopic: The Biggest Kraal on a Fixed Roll of Fence

One roll of fencing, 160 metres, and a long farm wall to borrow as a free side. Fence off a narrow ribbon two metres deep and it holds nearly nothing; sink all the wire into two enormous sides with barely a front left — nothing again. Somewhere between the two silly designs waits the best kraal, and calculus walks straight to it, no trial and error required.

Frame it as a story with one unknown. Call the width x. The wall supplies one long side for free, so the roll must cover two widths and one front: the front receives 160 minus two x. Area: x times 160 minus two x. That formula is a frowning parabola — zero area at both ridiculous extremes, its best somewhere between — and the crown of the frown sits where the slope of the area graph is zero. Differentiate: 160 minus four x. Set to zero: x is 40. Width 40, front 80, area 3200 square metres. No guessing, no table of tries: the derivative climbed directly to the top of the hill.

The reasoning's skeleton is the recipe you will reuse for the rest of your life. Write the thing you want as a formula. Spend the fixed total — the roll of fence — to get down to ONE letter. Differentiate, set to zero, solve. Then step back and check the number breathes: a width of 40 fits the roll, leaves a positive front, and beats its neighbours — try 39 or 41 and watch the area sag.

Your questions for this part are up now. One letter before differentiating, zero slope at the best design, and always ask whether your answer would survive on an actual farm.

## Subtopic: The Cheapest Tin That Holds Enough

Turn the last problem inside out. There the material was fixed and the space was maximised. Here the SPACE is fixed — the tin must hold 108 cubic centimetres — and the material is minimised, because on a production line, material is money. Same recipe, opposite direction of travel.

The open-topped square tin: base side x, height h, no lid. The holding requirement shackles the two letters together: x squared times h must equal 108, so the height is forced to 108 over x squared — widen the tin and it automatically grows shallower. Material: one base, x squared, plus four walls, four x h — and substituting the forced height collapses everything to one letter: x squared plus 432 over x.

Feel the tug of war before any algebra. A wide tin: huge base, short cheap walls. A tall narrow tin: modest base, endless expensive walls. The cheapest design is the truce between the two costs, and the truce is signed where the material graph runs flat. Differentiate — respect the fraction: 432 over x is 432 x to the minus one, derivative MINUS 432 over x squared — set two x minus 432 over x squared to zero, and x cubed is 216. Base 6 by 6, height 3, material 108 square centimetres. The winning tin stands half as tall as it is wide — squat, like most tins on a shop shelf, and now you know the reason.

And here come the last questions of the lesson, right now: fixed space forces the height, one letter enters the derivative, the fraction's minus sign survives, and the flattest point of the cost curve is where the factory keeps its money.
