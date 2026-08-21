# Part 1 — Expert

In grade 10 you met emf, potential difference and current as three separate characters. Grade 11 ties them together with the one equation the whole of electricity leans on, then demands that you untangle complete networks with it — series and parallel resistors mixed in a single circuit — and closes by converting circuit theory into the rand amounts on a household electricity statement. The plan for this session: the law and the conductors that refuse to obey it, the two rules for combining resistors, a complete method for a mixed network, and the power and energy formulas that put a price on every appliance you own.

## Subtopic: Ohm's Law and the Conductors That Break It

The law itself, word for word: the current through a conductor is directly proportional to the potential difference across it, provided the temperature remains constant. As an equation, R equals V over I — resistance is the potential difference across a conductor divided by the current through it, and one ohm is one volt per ampere.

The same equation rearranges to answer three different requests. V equals I R gives the voltage across a resistor when you know its current. I equals V over R gives the current a supply pushes through a known resistance. R equals V over I measures a resistance from readings. Try one immediately: a resistor carries 2 amperes when 18 volts is placed across it. The resistance is 18 divided by 2, which is 9 ohms.

A conductor that keeps this proportion is called OHMIC. Plot its current against the applied potential difference at constant temperature and you get a straight line passing through the origin — twice the volts, twice the amps, the ratio never wavering. A NON-OHMIC conductor produces a graph that bends, and the classic culprit is the filament of an incandescent bulb. A working filament glows at over two thousand degrees Celsius; as the current grows, the filament gets hotter, its resistance rises with the temperature, and every additional volt delivers a smaller gain in current than the volt before it. The current-against-voltage graph curls over and flattens. Read the fine print of the law again — provided the temperature remains constant — and you can see the filament fails the condition rather than the law.

Both pictures must be at your fingertips: the ohmic straight line through the origin with its constant gradient, and the filament's flattening curve, explained by resistance climbing with temperature.

Try this section's questions now — and every time the law is asked for, state the constant-temperature condition with it.

## Subtopic: Resistors in Series and in Parallel

The entire topic rests on two combination rules, one for each way of wiring.

IN SERIES the resistors stand in a single file along one conducting path. One current threads through every one of them, and their potential differences add up. The equivalent resistance is a straight sum: R total equals R one plus R two plus R three. Every resistor added in series RAISES the total, because it is one more obstacle planted in the only available path. A 6 ohm resistor in series with a 12 ohm resistor makes 18 ohms.

IN PARALLEL the resistors bridge the same two junctions side by side. Each branch draws its own current, but the potential difference across every branch is THE SAME, since each branch touches the identical pair of points. The branch currents add. The rule: one over R total equals one over R one plus one over R two plus one over R three. For exactly two resistors there is a shortcut — product over sum. Take the same 6 ohm and 12 ohm in parallel: 6 times 12 over 6 plus 12 is 72 over 18, which is 4 ohms.

Stare at that result. Four ohms is LESS than either 6 or 12. A parallel combination always lands below its smallest branch, because every extra branch opens another route for charge — more routes, more total current, less overall opposition. One more, with three branches: 12 ohms, 6 ohms and 4 ohms in parallel. One over R total is one twelfth plus one sixth plus one quarter, which is one twelfth plus two twelfths plus three twelfths, six twelfths in all — one half. Flip it: R total is 2 ohms, comfortably below the smallest branch of 4.

Two protective habits. After any parallel calculation, check that the answer sits below the smallest branch — if it does not, you almost certainly stopped at one over R and forgot the final flip. And keep the sharing rules straight: series components share one CURRENT, parallel branches share one VOLTAGE.

This section's questions are with you now — plain sum for series, reciprocal sum and a flip for parallel.

## Subtopic: Solving a Mixed Network Step by Step

The circuit that tests real understanding mixes both wirings: a resistor in series with a parallel pair, the whole arrangement across a battery. One method solves every version of it, and each line of the method carries credit.

Here is the circuit for this session: a 24 volt battery with negligible internal resistance feeds a 4 ohm resistor, the current then reaches a junction and splits between a 6 ohm and a 12 ohm resistor in parallel, and the branches rejoin to return to the battery.

Step one: reduce everything to a single resistance. The parallel pair goes first: 6 times 12 over 6 plus 12, which is 72 over 18, giving 4 ohms. The circuit is now a 4 ohm and another 4 ohm in series — 8 ohms in total.

Step two: the current the battery delivers. I equals V over R total: 24 divided by 8, which is 3 amperes. That 3 amperes passes through the battery and through the series 4 ohm resistor, because there is only one path until the junction.

Step three: distribute the voltage. Across the series resistor, V equals I R: 3 times 4, which is 12 volts. The battery provides 24, so the parallel pair receives 24 minus 12, which is 12 volts — and that identical 12 volts appears across BOTH branches, since parallel branches share voltage.

Step four: split the current. The 6 ohm branch takes 12 divided by 6, which is 2 amperes. The 12 ohm branch takes 12 divided by 12, which is 1 ampere. Add them: 2 plus 1 is 3 amperes, precisely the current that arrived at the junction — charge is conserved wherever paths meet. And notice which branch took more: the SMALLER resistance carried the LARGER current. It always does.

The checks are the safety net, not an optional extra. The potential differences around the loop must total the battery voltage — 12 plus 12 is 24. The branch currents must total the current entering the junction — 2 plus 1 is 3. Do both checks on every network and an arithmetic slip cannot hide until the end of the question.

Work through this section's questions now — reduce first, then walk the volts, then split the amps.

## Subtopic: Power, Energy and the Price of Electricity

Power is the rate at which electrical energy is converted into other forms, measured in watts — one watt is one joule each second. Three equivalent formulas cover every situation: P equals V I, P equals I squared R, and P equals V squared over R. Choose the one whose quantities the question has already handed you.

Apply them to our network. The battery delivers V times I: 24 times 3, which is 72 watts. The series 4 ohm resistor converts I squared R: 3 squared times 4, which is 36 watts. The 6 ohm branch converts V squared over R: 12 squared over 6, which is 24 watts. The 12 ohm branch: 12 squared over 12, which is 12 watts. Total the three resistors: 36 plus 24 plus 12 equals 72 watts — every watt leaving the battery is accounted for in the resistors.

Energy is power multiplied by time: W equals P delta t, giving joules when power is in watts and time in seconds. A 150 watt lamp left on for two minutes converts 150 times 120, which is 18 000 joules.

Joules are far too small a coin for a monthly account, so electricity is sold by the KILOWATT-HOUR: the energy converted when one kilowatt runs for one hour — 1 000 watts times 3 600 seconds, which is 3,6 million joules. The billing arithmetic is simply power in KILOWATTS multiplied by time in HOURS. A 2 kilowatt kettle boiling for a total of fifteen minutes uses 2 times 0,25, which is 0,5 kilowatt-hours; at a tariff of 3 rand per kilowatt-hour that costs 1 rand 50. The heavyweight is the geyser: 3 kilowatts heating for about five hours across a day is 15 kilowatt-hours daily — 45 rand a day, in the region of 1 350 rand a month, which is why the geyser towers over every other line of the account.

Watch the traps: convert watts to kilowatts and minutes to hours BEFORE multiplying, and remember that the kilowatt-hour measures ENERGY, not power — muddling the two forfeits the definition mark.

The final questions of this part are ready for you — three power formulas, one energy formula, and a geyser to price.

# Part 2 — Simplifier

The same circuits again, but now as roads, traffic and a household account you can finally decode.

## Subtopic: One Road or Many Roads

There are only two ways to combine resistors, and the town you live in already taught you both.

SERIES is a single road with several stop-and-search checkpoints. Every vehicle must clear checkpoint one, then two, then three. Plant another checkpoint on that road and the entire journey slows further — series resistance grows with every resistor you add. And because there is just the one road, every vehicle passes every checkpoint: series resistors all carry the SAME current.

PARALLEL is opening extra streets between the same two intersections. Would traffic move better with one street or with three? With three, vehicles spread themselves across the options and the total flow between the intersections goes UP — meaning the overall opposition went DOWN. This is the result that feels wrong until the traffic shows you: wiring a resistor in PARALLEL always drops the total resistance below the smallest branch, because each branch is another street open to traffic. The 6 ohm with a 12 ohm alongside it: 4 ohms overall. Less than 6. More streets, freer movement.

The arithmetic mirrors the picture. Series: simply add, 6 plus 12 is 18. Parallel: you are adding the EASE of each street rather than its difficulty, which is why the fractions turn upside down — and for two resistors the shortcut is product over sum, 72 over 18, which is 4.

Now look at the wiring of your own home: it is parallel throughout, and the traffic picture says why. Every appliance receives the full 230 volts, any one can be switched off without stopping the rest, and each extra appliance you switch on adds another street — more total current drawn from the supply.

Your questions on this section are with you now — checkpoints slow one road, side streets free the traffic.

## Subtopic: Walking Through the Circuit Like a Marker

A mixed circuit — one resistor feeding a parallel pair — makes many learners freeze on sight. The people who mark your work solve it with a calm, fixed, four-move routine, and the routine never varies.

Move one: SHRINK. Fold the parallel pair down to a single number using product over sum, then add whatever sits in series with it. The battery now faces one resistance only. In our circuit the 6 and the 12 fold into 4; add the series 4; the battery sees 8 ohms.

Move two: TOTAL CURRENT. Battery voltage over that single resistance: 24 over 8 is 3 amperes. That is what leaves the battery, and it must pass through everything wired in series before any junction.

Move three: SPEND THE VOLTS. The battery's 24 volts is a budget spent around the loop. The series resistor charges current times resistance: 3 times 4, so 12 volts. The remainder — 24 minus 12, so 12 volts — lands across the parallel pair, and BOTH branches feel that same 12 volts. Parallel means shared voltage. That is the rule.

Move four: SPLIT THE AMPS. Each branch draws its shared voltage divided by its own resistance: 12 over 6 gives 2 amperes, 12 over 12 gives 1 ampere. The easier street carries the heavier traffic — confirm the smaller resistor took the bigger current. Then close the books: 2 plus 1 returns the 3 amperes that arrived. Balanced.

Shrink, total, spend, split. Write the four moves as four labelled steps and the method earns credit even on the day a number slips — and the closing balance checks usually expose the slip before anyone else does.

The questions for this section are coming to you now — four moves, in order, every time.

## Subtopic: Reading the Bill Like a Physicist

An electricity account looks mysterious until you learn the single unit it is written in. Nobody sells you volts or amperes. You are sold KILOWATT-HOURS, and the unit is refreshingly concrete: run a one kilowatt appliance for one hour and you have bought exactly one kilowatt-hour.

Every appliance is therefore a spender with its own spending rate. The kettle spends fast — 2 kilowatts — but only for minutes at a stretch; fifteen minutes of boiling in a day is half a kilowatt-hour, around 1 rand 50 at a typical tariff. The real money leaves through the geyser: 3 kilowatts, running perhaps five hours in total every day to keep the water hot. That is 15 kilowatt-hours a day, about 45 rand daily, roughly 1 350 rand a month — commonly more than everything else in the house combined. At the other extreme, a phone charger sips a few thousandths of a kilowatt; a whole month of nightly charging costs less than one boil of the kettle.

Two numbers set every line of the account: how FAST the appliance spends — its power in kilowatts — and how LONG it runs — its time in hours. Multiply them, then multiply by the tariff. That is the entire secret, and it doubles as the savings plan: attack the big powers and the long hours. Fewer geyser hours, a geyser blanket, boiling only the water you need — these save more in a day than unplugging chargers saves in a year.

One final translation between physics and money. Watts measure how QUICKLY energy is being used — the speed of spending. Kilowatt-hours measure HOW MUCH energy was used — the amount spent. A powerful appliance used briefly can cost less than a feeble one left running all day. On the account, the marathon beats the sprint.

The last questions of the lesson are yours now — kilowatts times hours times tariff, and interrogate the geyser first.
