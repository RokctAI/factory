# Part 1 — Expert

Switch on a car's headlights and they glow steadily — until the engine cranks, and for a moment they dim. Nothing outside the battery changed; the explanation lives INSIDE it. Every real battery resists its own current, and that internal resistance is the idea that turns Grade 11 circuits into the Grade 12 examination favourite. This session rebuilds series and parallel networks, defines emf and internal resistance properly, works the full circuit problems the paper loves, and finishes with the graphs and power calculations that read a battery like a doctor's chart.

## Subtopic: Series and Parallel Networks

Everything starts with two rules of combination, and the syllabus allows networks of up to four resistors, so both rules must be automatic. In SERIES, resistors sit one after another on a single path: the same current passes through each, the voltages across them add up to the total, and the resistances simply add — total resistance equals R one plus R two plus R three. Adding a resistor in series always INCREASES the total resistance, because the current must fight through more material.

In PARALLEL, resistors sit side by side between the same two points: each one feels the SAME voltage, the currents through the branches add up to the total, and the resistances combine by reciprocals — one over the total equals one over R one plus one over R two. For exactly two resistors there is a faster form: product over sum. Adding a resistor in parallel always DECREASES the total resistance, because a new branch is a new road for current — more roads, easier flow. The combined resistance of a parallel pair is always smaller than the smallest branch, which is a free sanity check on every answer.

Work one combination cold. A 6 ohm and a 3 ohm resistor in parallel: product over sum gives 6 times 3 over 6 plus 3, which is 18 over 9 — 2 ohms. Smaller than 3, as parallel demands. Put that pair in series with a 4 ohm resistor and the network totals 4 plus 2, which is 6 ohms. Collapse networks exactly like that: parallel clusters first, into single equivalent resistors, then add along the series spine.

This section's questions are with you now — series adds, parallel adds the reciprocals, and a parallel answer must undercut its smallest branch.

## Subtopic: EMF and Internal Resistance

Now open the battery itself. The emf, symbol epsilon, is the total energy the battery gives each coulomb of charge — measured in volts, and readable on a voltmeter only when the battery delivers NO current. But the chemicals and connections inside the battery resist current too, and that internal resistance, symbol r, behaves exactly like a small resistor hidden inside the cell, in series with everything else.

The master equation of the whole topic: emf equals I times R external plus I times r. In symbols, epsilon equals I R external plus I r. Read it as an energy budget: every volt the chemistry provides is spent either outside the battery, across the external circuit, or inside it, across the internal resistance. The outside share, I times R external, is the TERMINAL voltage — what a voltmeter across the battery reads while current flows. The inside share, I times r, is often called the lost volts: energy that becomes heat inside the battery and never reaches the circuit.

Numbers make it concrete. A battery of emf 12 volts and internal resistance 0,5 ohms drives a 5,5 ohm external resistor. Total resistance: 5,5 plus 0,5, which is 6 ohms. Current: 12 divided by 6 — 2 amperes. Terminal voltage: 2 times 5,5, which is 11 volts. Lost volts: 2 times 0,5 — 1 volt. Budget check: 11 plus 1 equals 12, the emf, exactly. And notice the logic of the open switch: no current means the lost volts I times r are zero, so the voltmeter across the terminals reads the full emf. Switch open, read the emf; switch closed, read less — the difference IS the lost volts.

Questions on this section reach you now — emf is the whole budget, terminal voltage is what escapes the battery, and the difference heats the cell.

## Subtopic: Full Circuit Problems

The examination staple welds the two ideas together: a battery with internal resistance driving a mixed network. One systematic routine solves them all. Step one: collapse the external network to a single R external. Step two: find the main current from epsilon equals I times R external plus r, all in one bracket. Step three: walk back INTO the network, splitting voltages and currents branch by branch.

Run the routine on the standard setup. A battery of emf 24 volts, internal resistance 1 ohm, connected to a 5 ohm resistor in series with a parallel pair of 6 ohms and 3 ohms. Step one: the parallel pair is product over sum, 18 over 9 — 2 ohms; the external network is 5 plus 2, which is 7 ohms. Step two: total resistance including the inside of the battery is 7 plus 1, which is 8 ohms; current equals 24 divided by 8 — 3 amperes. Step three: terminal voltage is 24 minus 3 times 1, which is 21 volts. The 5 ohm resistor takes 3 times 5 — 15 volts. That leaves 21 minus 15, which is 6 volts across the parallel pair, and parallel branches share voltage equally. Branch currents: 6 divided by 6 gives 1 ampere through the 6 ohm; 6 divided by 3 gives 2 amperes through the 3 ohm. Check: 1 plus 2 equals 3 amperes, the main current, exactly.

That final check is not decoration — it is the habit that catches errors before the marker does. Currents into a junction must add up; voltages around the loop must add up to the emf. If the books do not balance, an earlier line is wrong, and thirty seconds of auditing buys back three marks.

This section's questions arrive now — collapse, solve the loop, then walk back in, and let the junction check audit every answer.

## Subtopic: Graphs, Switches and Power

The syllabus tests internal resistance through behaviour, not just calculation, and three behaviours dominate. First, the graph. Measure terminal voltage against current for a battery and the points fall on a straight line sloping DOWNWARD: terminal voltage equals epsilon minus I times r. The vertical intercept, where current is zero, is the emf; the gradient of the line is negative r. One graph, both battery constants — a favourite practical question, and the exact experiment named in this term's formal practical.

Second, the loading effect. Connect more bulbs in PARALLEL and the external resistance falls, so the total current rises, so the lost volts I times r rise, so the terminal voltage DROPS — every bulb burns slightly dimmer. That is the cranking car: the starter motor is a huge parallel load, the current leaps, the lost volts leap, and the headlights sag until the engine catches. Any question that says "another resistor is added in parallel — explain what happens to the voltmeter reading" wants exactly that four-link chain, in order.

Third, power. Power is the rate of energy transfer: P equals V times I, and with Ohm's law it wears two other faces — I squared times R, and V squared over R. In the 24 volt circuit, the 5 ohm resistor dissipates I squared R, which is 9 times 5 — 45 watts, while the battery wastes 9 times 1, which is 9 watts, as internal heat. Efficiency questions live right there: energy delivered against energy generated, and the internal resistance always takes its cut.

The final expert questions are with you now — intercept reads the emf, slope reads the internal resistance, and every added parallel branch taxes the terminal voltage.

# Part 2 — Simplifier

Now the same circuit ideas from the kitchen and the taxi rank: a tired battery, a river splitting into channels, and the night the headlights dimmed.

## Subtopic: The Battery Charges a Toll

Think of a battery as a water pump promising a certain push — say twelve units of push. That promise is the emf: the full effort the chemistry inside can produce. But here is the small print: the water must first squeeze through the pump's own narrow pipes before it ever reaches your circuit. Squeezing costs some of the push. The push actually delivered at the gate — the terminals — is always a little less than the promise, and the missing part was spent inside the pump itself.

That is internal resistance: the battery charging a toll on its own current. No current, no toll — so a battery doing nothing shows its full promise on a voltmeter, twelve out of twelve. The moment current flows, the toll gate opens: the more current passes, the more push is surrendered inside, and the less arrives outside. A small trickle of current pays a small toll; a huge current pays a huge one.

You have felt this in your hands. A torch battery near the end of its life still reads fine on a voltmeter — full promise, no current — but the torch barely glows, because the ageing chemistry has raised the internal toll so high that hardly any push survives the journey out. The promise never changed; the toll did. Emf is the promise; terminal voltage is what the promise looks like after the toll; and the toll is current times internal resistance, every single time.

Your first questions are with you now — promise minus toll equals delivery, and the toll only exists while current flows.

## Subtopic: One River, Many Channels

Picture current as a river. Resistors in SERIES are rapids one after another on the same river: every drop of water must pass through all of them, so their difficulty simply adds. Three sets of rapids are harder than two — series resistance grows with every addition, and the river slows.

Resistors in PARALLEL are the river splitting into side-by-side channels around an island. No drop passes through more than one channel, and here is the part that surprises people: adding ANOTHER channel makes the total journey EASIER, even if the new channel is narrow. Why? Because any new channel carries some water that previously had to queue elsewhere. More paths, less total resistance — always. That is why the combined resistance of a parallel pair is smaller than either branch alone, and why your house wires every appliance in parallel: each new appliance opens a new channel and draws its own current without blocking the others.

The two arrangements also share differently. Series channels share the PUSH: each set of rapids uses up part of the total voltage, big resistors taking the bigger share. Parallel channels share the FLOW: each branch feels the same push across it, and the narrow branch simply passes less water. Same current in series, same voltage in parallel — tattoo that pair of sentences somewhere permanent, because half the marks in circuit questions are just knowing which quantity is shared.

Questions on this section are coming to you now — rapids add difficulty, extra channels remove it, and know what is shared before you calculate anything.

## Subtopic: The Night the Headlights Dimmed

Now put the toll and the channels together, and explain the car. Headlights on: a modest current flows, the battery pays a small internal toll, and nearly the full promise reaches the lamps. Turn the ignition key: the starter motor joins the circuit as a new parallel channel — and not a polite one. It is a hungry, low-resistance channel, and the moment it opens, the total current surges.

Follow the chain, link by link. New parallel branch — external resistance falls. Resistance falls — total current rises. Current rises — the internal toll, current times internal resistance, rises with it. Toll rises — less push left at the terminals. And the headlights, still faithfully connected across those terminals, feel the sag and dim. Four links, always in that order, and the examiner pays a mark per link.

The same chain explains a household mystery: too many appliances on one multiplug, and things weaken — the kettle takes ages, the lights on that circuit dip when the heater kicks in. Every added device is another parallel channel, every channel raises the total current, and every extra ampere pays toll somewhere along thin wires and tired connections.

And the flip side is the mechanic's diagnostic trick: a battery that reads a healthy twelve volts sitting idle but collapses the moment it must deliver cranking current has a swollen internal toll — high internal resistance — and no amount of charging fixes chemistry that has aged. Idle voltage tests the promise; voltage under load tests the battery. The last questions of the lesson are yours now — every new branch raises the current, every ampere pays the toll, and the terminals tell the story.
