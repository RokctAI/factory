# Part 1 — Expert

A torch with an old cell can read a healthy voltage on a meter and still barely glow. The contradiction is not in the bulb or the wiring — it hides inside the cell itself. Every real battery resists the very current it drives, and that hidden resistance is the idea that lifts circuit work from Grade 11 revision into proper Grade 12 physics. This session rebuilds the two rules for combining resistors, defines emf and internal resistance with care, runs the complete circuit routine on a mixed network, and closes with the straight-line graph and the power calculations that let you diagnose a battery from its behaviour.

## Subtopic: Series and Parallel Networks

Two combination rules carry every network you will meet, so grind them until they are reflex. Resistors in SERIES stand in single file on one path: one current threads through all of them, their voltages stack up to the supply, and their resistances add directly — R total equals R one plus R two plus R three. Each extra series resistor RAISES the total, because the same current now has more material to force its way through.

Resistors in PARALLEL stand shoulder to shoulder between the same two nodes: every branch feels the identical voltage, the branch currents pool into the total, and the resistances combine through reciprocals — one over R total equals one over R one plus one over R two. For a pair, use the shortcut: product over sum. Each extra parallel resistor LOWERS the total, because a fresh branch is a fresh route — every new route relieves the others. And a built-in error alarm comes free: a parallel combination is always smaller than its smallest branch. If your parallel answer is not smaller than every branch in it, the arithmetic is wrong; no need to hunt, just redo it.

Practise the collapse once, cleanly. A 12 ohm and a 6 ohm resistor in parallel: product over sum is 12 times 6 over 12 plus 6 — 72 over 18 — 4 ohms. Smaller than 6, so the alarm stays silent. Wire that pair in series with a 5 ohm resistor and the network becomes 5 plus 4 — 9 ohms. That two-move pattern is the universal opening: melt every parallel cluster down to its single equivalent, then add along the series backbone.

This section's questions are with you now — series stacks, parallel splits, and a parallel result must always undercut its smallest member.

## Subtopic: EMF and Internal Resistance

Time to look inside the battery. The emf, symbol epsilon, is the energy the battery's chemistry gives to each coulomb of charge — in volts — and it appears on a voltmeter only when the battery is delivering NO current at all. Because the electrolyte, plates and terminals inside the battery also resist current, every real cell behaves as an ideal source in series with a small hidden resistor: the internal resistance, symbol r.

Here is the equation the entire topic hangs from: epsilon equals I times R external, plus I times r. Treat it as a strict energy budget. Every volt the chemistry raises is spent in exactly one of two places — outside the battery, across the external circuit, or inside it, across r. The external spending, I times R external, is the TERMINAL VOLTAGE: the reading of a voltmeter across the battery while current flows. The internal spending, I times r, is the LOST VOLTS: energy converted to heat inside the casing, never seen by the circuit.

Put figures to it. A cell of emf 9 volts with internal resistance 0,5 ohms drives a 4 ohm external resistor. Total resistance in the loop: 4 plus 0,5 — 4,5 ohms. Current: 9 divided by 4,5 — 2 amperes. Terminal voltage: 2 times 4, which is 8 volts. Lost volts: 2 times 0,5 — 1 volt. Audit the budget: 8 plus 1 is 9, the emf, to the cent. Now reason the open switch: zero current makes the lost volts zero, so the terminal reading rises to the full emf. Closed switch, the reading sags below the emf — and the sag IS I times r. One battery, two readings, and the difference measures what the inside is costing you.

Questions on this section reach you now — emf is the full budget, terminal voltage is the take-home amount, and the lost volts warm the battery from within.

## Subtopic: Full Circuit Problems

The classic examination task marries the two ideas: a real battery, internal resistance included, feeding a mixed resistor network. One routine dispatches every version of it. Step one: collapse the external network to a single equivalent R external. Step two: apply epsilon equals I into R external plus r — bracket first, then divide — to get the main current. Step three: re-enter the network and distribute voltages and currents branch by branch, finishing with a junction audit.

Watch the routine work. A battery of emf 18 volts and internal resistance 1 ohm feeds a 2 ohm resistor in series with a parallel pair of 10 ohms and 15 ohms. Step one: the pair collapses by product over sum — 150 over 25 — to 6 ohms, so the external network is 2 plus 6, which is 8 ohms. Step two: the whole loop resists 8 plus 1 — 9 ohms; the main current is 18 divided by 9 — 2 amperes. Step three: terminal voltage is 18 minus 2 times 1 — 16 volts. The 2 ohm series resistor claims 2 times 2 — 4 volts — leaving 16 minus 4, which is 12 volts across the parallel pair, and both branches feel that full 12. Branch currents: 12 over 10 gives 1,2 amperes; 12 over 15 gives 0,8 amperes. The audit: 1,2 plus 0,8 equals 2 amperes — the main current, recovered exactly.

Never treat that audit as optional polish. Currents at a junction must reconcile; voltages around the loop must sum back to the emf. When the books refuse to balance, some earlier line is broken, and finding it yourself costs thirty seconds — far cheaper than what the marker will charge.

This section's questions arrive now — collapse, one bracketed equation, walk back in, and audit the junction before you move on.

## Subtopic: Graphs, Switches and Power

Calculation alone does not finish this topic; the syllabus also tests behaviour, and three behaviours do the heavy lifting. First, the graph. Record terminal voltage against current for a real battery and the data lands on a straight line running DOWNHILL: terminal voltage equals epsilon minus I times r. Where the line meets the voltage axis — zero current — it reads the emf. The slope of the line is negative r. One straight line surrenders both of the battery's constants, which is exactly why this experiment is a standard practical investigation: plot, extend to the intercept, take the gradient, done.

Second, loading. Add lamps in PARALLEL and external resistance falls; total current climbs; the lost volts I times r climb with it; and the terminal voltage SAGS — so every lamp already connected dims a little. Keep that four-link chain in strict order — resistance down, current up, lost volts up, terminal voltage down — because explanation questions award their marks link by link. It is also the anatomy of a car starting at night: the starter motor is a ravenous low-resistance parallel branch, the current leaps on the turn of the key, the internal toll leaps too, and the headlights droop until the engine fires.

Third, power — the rate of energy transfer. The parent formula is P equals V times I, and Ohm's law spins off two variants: I squared R, and V squared over R. In our 18 volt circuit the 2 ohm resistor dissipates I squared R — 4 times 2 — 8 watts, while the battery itself wastes 4 times 1 — 4 watts as internal heat. Totals confirm it: the chemistry supplies emf times current, 36 watts; the parallel pair takes V squared over R in each branch, 14,4 plus 9,6 — 24 watts; and 8 plus 24 plus 4 rebuilds the 36. Efficiency questions live in that split — useful output against total generated — and the internal resistance always skims its share.

The final expert questions are with you now — intercept for the emf, gradient for r, and every added branch is a tax on the terminal voltage.

# Part 2 — Simplifier

Now the whole topic in everyday clothes: a battery that charges a fee on the way out, a river deciding how to flow, and the night-time car park mystery every driver has seen.

## Subtopic: The Battery Charges a Toll

Picture the battery as a depot with one exit gate, and at the gate stands a toll collector who never sleeps. The depot promises a certain push to every parcel of charge it sends out — that promise is the emf, the full strength of the chemistry. But no parcel leaves without passing the gate, and the collector takes a cut of the push as it goes by. What actually arrives on the road outside — at the terminals — is the promise minus the cut. The cut is the lost volts, and its price list is simple: current times internal resistance.

The toll has one merciful rule: no traffic, no charge. A battery delivering zero current pays nothing, which is why an idle battery shows its full promised voltage on a meter. The instant current flows, the collector starts charging — and the busier the gate, the steeper the total fee. Double the current and the toll doubles with it. Trickle-feed a wall clock and the fee is negligible; slam a heavy load across the terminals and the fee eats a visible slice of the promise.

You have met this collector personally. That old torch cell reading full voltage on a multimeter but producing only an amber glow? Its chemistry has aged, its internal resistance has swollen, and its toll gate now confiscates most of the push the moment real current tries to leave. The promise on the meter never changed; the fee structure did. Keep the three words straight and this whole subtopic is yours: emf is the promise, terminal voltage is the delivery, and the toll — current times internal resistance — is the difference between them.

Your first questions are with you now — promise, toll, delivery, and the toll only exists while current is moving.

## Subtopic: One River, Many Channels

Let current be a river. SERIES resistors are obstacles strung along one river — a weir, then rapids, then a narrow gorge, one after the other. Every drop of water must negotiate all of them in turn, so the difficulties simply add. String on another obstacle and the river as a whole flows less freely: series resistance can only grow.

PARALLEL resistors are the river dividing around islands into side-by-side channels. Each drop chooses exactly one channel — no drop runs two. And here sits the result that ambushes almost everyone at first: cutting ANOTHER channel makes the total flow EASIER, even if the new channel is a mere trickle-stream. Reason it through: the new channel carries water that yesterday had to squeeze through the old ones, so every existing channel breathes easier. More ways through, less overall resistance — without exception. That is precisely why the wiring in your home puts every appliance on its own parallel branch: each new appliance opens its own channel, draws its own current, and leaves the others undisturbed.

The two layouts also divide the spoils differently, and knowing WHICH quantity is shared is half of every circuit mark. Series obstacles share the PUSH: the total voltage is split along the line, and the biggest resistor commandeers the biggest share. Parallel channels share the FLOW: every channel spans the same two banks, so every channel feels the same voltage — the narrow one simply passes less current. Say it as a chant: in series the current is common; in parallel the voltage is common. Decide which chant applies before touching the calculator, every time.

Questions on this section are coming to you now — obstacles in a line add up, extra channels ease the flow, and always name the shared quantity first.

## Subtopic: The Night the Headlights Dimmed

Now assemble the toll and the channels into one story every taxi rank knows. A car idles in the dark, headlights bright and steady: modest current, tiny toll at the battery's gate, nearly the whole promise reaching the lamps. The driver turns the key. Somewhere under the bonnet, the starter motor — a huge, greedy, low-resistance load — joins the circuit as a new parallel channel, and for a second or two the headlights visibly droop. Then the engine catches, the starter drops out, and the lights recover.

Explain it as four links, in strict sequence. Link one: a new parallel branch opens, so the external resistance falls. Link two: lower resistance, so the total current from the battery surges. Link three: more current, so the internal toll — current times internal resistance — surges too. Link four: a bigger toll leaves less at the terminals, and the headlights, wired across those very terminals, dim with the sag. Deliver the links in that order whenever a question adds a branch and asks about a meter reading; each link is where a mark lives.

The same four links run through the kitchen. Overload one multiplug and the toaster slows while the heater roars; the lights on that circuit dip as the compressor of the fridge kicks in. Every added device is a new channel, every channel lifts the total current, and every extra ampere pays toll across tired wires and the source's own innards.

Finish with the mechanic's trick, because it turns the physics into a diagnosis. A battery that shows a confident reading at rest but collapses the instant it must crank has developed a swollen internal resistance — the idle meter tested only the promise, while cranking tested the delivery. No charger cures aged chemistry; the toll gate has simply become extortionate. The last questions of the lesson are yours now — new branches raise the current, every ampere pays the toll, and the terminal voltage tells you the truth under load.
