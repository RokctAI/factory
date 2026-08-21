# Part 1 — Expert

Newton's second law is easy arithmetic once every force is known; the real Grade 11 work is finding the forces. Two of them cause nearly all the casualties: the normal force, which equals the weight far less often than learners assume, and friction, which comes in two varieties with two different coefficients. This session pins both down on level ground, then tilts the entire problem onto an inclined plane, where the weight itself must be resolved into a piece along the slope and a piece pressing into it. Own this and the rest of mechanics turns into careful bookkeeping.

## Subtopic: The Normal Force and the Free-Body Diagram

The NORMAL FORCE, symbol N, is the force a surface exerts on an object in contact with it, always directed PERPENDICULAR to the surface. "Normal" is simply the geometry word for perpendicular — nothing to do with ordinary.

Start with the free-body diagram for a box on a level floor: the box collapses to a dot, the weight is an arrow pointing straight down, the normal force an arrow straight up. With nothing else acting vertically and no vertical acceleration, the two balance, and N equals m g. Memorise that as a SPECIAL CASE, never as the rule.

One added rope exposes the rule. Let a rope now pull a 40 kilogram box with 80 newtons at 25 degrees above the horizontal. The rope's upward component carries part of the box's weight, so the floor pushes less. Vertically: N plus F sine theta minus m g equals zero, so N equals m g minus F sine theta. Numbers: N equals 40 times 9,8 minus 80 times sine 25 degrees, which is 392 minus 80 times 0,423, giving 392 minus 33,8, so N equals 358,2 newtons. Angle the same rope DOWNWARD at 25 degrees instead and the component presses the box into the floor: N equals 392 plus 33,8, which is 425,8 newtons. One box, three different normal forces, depending entirely on the geometry of the pull.

Why does this matter so much? Because friction is computed FROM the normal force. An error in N infects every friction number after it, which is exactly why questions love to sneak a slanted rope into an otherwise routine setup.

Two drawing rules that markers apply strictly: every arrow leaves the dot, carries an arrowhead and a label; and only forces appear — no velocity arrows, no sketched ropes or ramps as objects.

The questions for this section are with you now: identify the normal force, and know precisely when it equals the weight and when it refuses to.

## Subtopic: Static and Kinetic Friction

Friction is the force a surface exerts parallel to itself, opposing motion or the TENDENCY toward motion. Two kinds must be kept apart.

STATIC friction, f s, acts while the object is still stationary, and it is self-adjusting. Push a cupboard with 100 newtons and static friction answers with exactly 100; push with 200 and it answers with 200 — up to a ceiling. The ceiling is the maximum static friction: f s max equals mu s times N, the coefficient of static friction multiplied by the normal force.

KINETIC friction, f k, takes over once sliding begins, and it does not adjust: f k equals mu k times N, constant while the object slides. For any surface pair, mu s exceeds mu k — the reason a heavy cupboard is hardest at the first shove and easier once it is going.

The coefficients describe only the two surfaces in contact. They carry no unit, being a force divided by a force, and they ignore contact area entirely — a brick on its narrow end grips exactly as well as the same brick lying flat.

Run the standard interrogation. A 60 kilogram crate stands on a level storeroom floor; mu s is 0,5 and mu k is 0,35. Normal force: N equals 60 times 9,8, which is 588 newtons. Ceiling of grip: f s max equals 0,5 times 588, which is 294 newtons.

Apply 250 newtons horizontally. Compare: 250 is below 294, so the crate stays put, and static friction is exactly 250 newtons — not 294. Writing 294 for a stationary crate under a 250 newton push is the single most common error in the topic.

Apply 320 newtons instead. Now 320 exceeds 294; the crate breaks loose and kinetic friction takes over: f k equals 0,35 times 588, which is 205,8 newtons. Net force: 320 minus 205,8, which is 114,2 newtons. Acceleration: 114,2 divided by 60, which is 1,9 metres per second squared in the direction of the push.

Take this section's questions now, and before choosing a friction formula, always test whether the object actually moves.

## Subtopic: Resolving Weight on an Inclined Plane

Tilt the surface and the cleanest move is to tilt your axes with it: work PARALLEL to the slope and PERPENDICULAR to the slope, instead of horizontal and vertical. Then the normal force and friction each lie neatly along an axis, and only one force needs resolving — the weight.

Draw it. A ramp rises at angle theta. On the dot representing the object: the weight, straight down, always vertical no matter how the ramp tilts; the normal force, perpendicular to the RAMP surface; friction along the ramp, opposing whichever way the object slides or tends to slide; plus any tension or applied force along the slope.

The weight splits into two components. Along the slope, pulling the object downhill: F g parallel equals m g sine theta. Into the slope, pressing the object against the surface: F g perpendicular equals m g cosine theta.

Understand the geometry rather than chanting it: the angle between the weight vector and the perpendicular-to-slope direction equals the ramp angle itself — similar triangles guarantee it. So the perpendicular component sits adjacent to theta and takes cosine, while the parallel component sits opposite theta and takes sine.

Two immediate consequences. Since nothing accelerates into or out of the surface, the perpendicular direction balances: N equals m g cosine theta. On any slope the normal force is LESS than the weight, shrinking as the slope steepens. And because friction feeds on N, friction on a slope is mu times m g cosine theta — never mu times m g.

Declare your sign convention before the first line: up-the-slope positive or down-the-slope positive, stated in words. Switching conventions halfway through a solution is how correct physics turns into a wrong answer.

The questions on this section are in front of you now: rotate the axes, split the weight, and state the normal force on a slope without reflexively writing m g.

## Subtopic: Worked Incline Problems — Sliding, Held and Pushed

A 15 kilogram toolbox rests on a steel ramp inclined at 35 degrees at a vehicle workshop. The coefficient of static friction is 0,6; the coefficient of kinetic friction is 0,25.

Components first. Weight: w equals 15 times 9,8, which is 147 newtons. Parallel component: 147 times sine 35 degrees, which is 147 times 0,574, giving 84,3 newtons down the slope. Perpendicular component: 147 times cosine 35 degrees, which is 147 times 0,819, giving 120,4 newtons. So N equals 120,4 newtons — comfortably less than the 147 newton weight.

Does it slide by itself? The grip ceiling is mu s times N: 0,6 times 120,4, which is 72,2 newtons. Gravity's downhill pull is 84,3 newtons. Since 84,3 exceeds 72,2, the toolbox slides.

How fast? Once moving, kinetic friction acts UP the slope against the downhill slide: f k equals 0,25 times 120,4, which is 30,1 newtons. Taking down-the-slope as positive: F net equals 84,3 minus 30,1, which is 54,2 newtons. Acceleration: 54,2 divided by 15, which is 3,61 metres per second squared down the incline.

Now a mechanic drags the toolbox back UP the ramp at constant velocity. Constant velocity: net force zero. The motion is now uphill, so kinetic friction flips to act DOWN the slope, siding with gravity. Formula: T equals F g parallel plus f k. Substitution: 84,3 plus 30,1. Answer: T equals 114,4 newtons up the slope. Friction changed direction, never size — its magnitude comes from mu k and N, its direction from the motion.

Four traps, by name. One: writing N equals m g on a slope, inflating every friction value downstream. Two: swapping sine and cosine, guaranteed for anyone who skips the triangle sketch. Three: assuming friction always points up the slope — it opposes motion, so it points downhill the moment the object moves uphill. Four: a drifting sign convention.

And one elegant result worth keeping. On the very point of slipping, m g sine theta equals mu s m g cosine theta; the m g cancels from both sides, leaving tangent theta equals mu s. An object slips when the tangent of the ramp angle exceeds the coefficient of static friction — no mass required. Here tangent 35 degrees is 0,700, which exceeds 0,6, confirming the slide for a toolbox of any mass whatsoever.

The final questions of this part are with you now: components, the true normal force, the slipping test, and friction aimed correctly for the described motion.

# Part 2 — Simplifier

Now the same grip and slopes as you actually meet them — a wardrobe that will not budge, and a driveway steep enough to be interesting.

## Subtopic: Grip, and Why It Runs Out

Try to slide a loaded wardrobe across a bedroom floor. First shove: nothing. Harder: still nothing. Then one more determined heave and it suddenly gives — and once moving, it slides along almost easily.

That little drama contains the whole theory. While the wardrobe stood still, friction was matching your shove exactly, newton for newton. Shove with 100, it resists with 100; shove with 200, it resists with 200. Self-matching friction is called STATIC friction, and it is why objects ignore polite pushes.

But the matching has a ceiling. Every pair of surfaces has a maximum grip, and the moment your shove exceeds it, the object tears loose. From then on a different, WEAKER friction rules — sliding friction, the kinetic kind — which is why the wardrobe feels almost cooperative once it is moving.

Both frictions are built from the same two ingredients: how grippy the surfaces are, and how hard they are pressed together. Grippiness gets a number, the coefficient, written with the Greek letter mu. Pressed-together-ness is the normal force — the floor's answering push. Multiply the two, and that is your friction.

With numbers: a 60 kilogram crate presses on the floor with 588 newtons, so the floor answers with 588. Grip coefficient 0,5 makes the ceiling 0,5 times 588, which is 294 newtons. Shove with 250 and nothing happens — and the friction at that moment is 250, matching you, not 294. Shove with 320 and it breaks free; sliding friction becomes 0,35 times 588, which is 205,8 newtons, so the leftover push is 114,2 newtons, and 60 kilograms picks up speed at a modest 1,9 metres per second squared.

Questions on this section are with you now — first ask whether the thing is moving, then pick the friction.

## Subtopic: Gravity Split into Down-the-Slope and Into-the-Slope

Now put that crate on a sloped driveway, and level-ground thinking quietly stops working.

Gravity has not changed — it still pulls straight down, slope or no slope. But on a ramp the crate can only do two things: slide along the surface, or press into it. So gravity's one downward pull gets divided between those two jobs, and the dividing is exactly the pile-sorting trick from the vectors lessons.

One share pulls the crate DOWN THE SLOPE — the share that makes trolleys roll away on hills. The other share presses the crate INTO THE SURFACE — the share the driveway must push back against.

Here is the sentence worth underlining twice: on a slope, the surface does NOT push back with the full weight. Part of the weight is busy pulling downhill, so the pressing share is smaller than the weight — which makes the surface's push smaller, which makes the GRIP smaller. Steeper slope, weaker grip. That is precisely why a steep dirt road after rain is where wheels spin and shoes slip.

The split follows the angle. Downhill share: weight times sine of the slope angle. Pressing share: weight times cosine of the slope angle. Do not memorise which is which — sketch the triangle and see which side hugs the angle.

Run the toolbox: 15 kilograms means 147 newtons of weight, on a 35 degree ramp. Downhill share: 147 times sine 35, which is 84,3 newtons. Pressing share: 147 times cosine 35, which is 120,4 newtons — so the ramp answers with 120,4 newtons, not 147.

Your questions for this part are coming to you now — two shares, and the ramp always answers with the smaller number.

## Subtopic: Will It Slide? The Quick Test

The finale is a straight contest between two numbers.

In the blue corner: the downhill share of gravity, trying to send the toolbox down the ramp — 84,3 newtons. In the red corner: the grip ceiling — the coefficient times the ramp's push, 0,6 times 120,4, which is 72,2 newtons. Bigger number wins. Gravity wins here, 84,3 against 72,2, so the toolbox slides.

Once it slides, the weaker sliding friction takes the field: 0,25 times 120,4, which is 30,1 newtons, resisting up the slope. Leftover: 84,3 minus 30,1, which is 54,2 newtons, spread over 15 kilograms — 3,61 metres per second squared, gathering speed down the ramp.

Now reverse the story: a mechanic hauls the toolbox UP the ramp at a steady pace. Steady pace means everything balances. But mind the friction — the box now moves uphill, so friction swaps sides and drags DOWNHILL, teaming up with gravity's downhill share. The mechanic must overcome both: 84,3 plus 30,1, which is 114,4 newtons. Friction changed its direction, never its size — it simply always opposes the journey.

And keep the beautiful shortcut. To know only WHETHER something will slip, the mass is irrelevant: compare the tangent of the slope angle with the grip coefficient. Tangent bigger — it slides. Tangent 35 degrees is 0,700 against a coefficient of 0,6, so it slides, and it would slide identically at 15 kilograms or 150.

The whole topic in one breath: split gravity into two shares, let the surface answer the smaller one, point friction against the motion, then hand everything to Newton's second law. The last questions of the lesson are yours now — sketch the ramp, sketch the triangle, and trust your table.
