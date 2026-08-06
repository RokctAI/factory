# Part 1 — Expert

Grade 10 introduced emf, potential difference and current as separate ideas. Grade 11 connects them with the single most used equation in electricity, then makes you solve entire networks with it — up to four resistors, series and parallel mixed — and finishes by pricing the electricity on a municipal bill. This session builds each layer in order: Ohm's law and its limits, the two combination rules, the full method for a mixed network, and the power and energy formulas that turn circuits into rands and cents.

## Subtopic: Ohm's Law and the Conductors That Break It

The statement, examinable: the current through a conductor is directly proportional to the potential difference across it, provided the temperature remains constant. In symbols, R equals V over I — the resistance is the potential difference across the conductor divided by the current through it. One ohm is one volt per ampere.

Rearranged three ways, the same law answers three question types: V equals I R for the voltage across a known resistor carrying a known current; I equals V over R for the current a voltage pushes through a resistance; and R equals V over I to measure a resistance. If 12 volts across a resistor drives 3 amperes through it, the resistance is 12 divided by 3, which is 4 ohms.

A conductor that obeys the law is called OHMIC: plot current against potential difference for a resistor at constant temperature and the graph is a straight line through the origin — double the voltage, double the current, constant ratio. A conductor whose graph bends is NON-OHMIC, and the standard example is a light bulb filament. As the filament carries more current it heats toward 2 500 degrees Celsius, its resistance climbs with the temperature, and each extra volt buys less extra current than the one before — the graph of current against voltage flattens. The condition hiding inside Ohm's law, at constant temperature, is exactly the condition the filament violates.

For the exam, know both graphs: ohmic, a straight line through the origin, gradient constant; non-ohmic filament, a curve that flattens as voltage grows, because the resistance rises with temperature.

Attempt this section's questions now — quote the law with its temperature condition every time it is asked.

## Subtopic: Resistors in Series and in Parallel

Two rules combine any set of resistors into one equivalent resistance, and everything else in the topic stands on them.

IN SERIES, resistors form a single path, one after another. The same current threads through all of them; the potential differences add. The equivalent resistance is the plain sum: R total equals R one plus R two plus R three. Series resistors always INCREASE the total resistance — each added resistor is another obstacle in the only road. A 4 ohm and a 12 ohm resistor in series make 16 ohms.

IN PARALLEL, resistors sit side by side between the same two points. Each carries its own current; the potential difference across every branch is IDENTICAL, because both ends of every branch touch the same two nodes. The currents add. The rule: one over R total equals one over R one plus one over R two plus one over R three. For exactly two resistors, a shortcut: product over sum. The same 4 ohm and 12 ohm in parallel give 4 times 12 over 4 plus 12, which is 48 over 16, which is 3 ohms.

Look hard at that answer: 3 ohms is SMALLER than either 4 or 12. Parallel resistors always decrease the total resistance below the smallest branch, because every new branch is another open road for current — more roads, more total traffic, less overall opposition. Three resistors of 6, 3 and 2 ohms in parallel: one over R equals one sixth plus one third plus one half, which is one sixth plus two sixths plus three sixths, exactly one — so R total is 1 ohm, smaller than all three.

Two habit checks before moving on. After any parallel calculation, confirm the answer is below the smallest branch; if not, you probably forgot to flip the fraction at the end — one over R is what the sum gives, and the reciprocal must be taken. And remember what each configuration shares: series shares the CURRENT, parallel shares the VOLTAGE.

This section's questions are with you now — sum for series, reciprocal sum for parallel, then flip.

## Subtopic: Solving a Mixed Network Step by Step

The examination circuit mixes both rules: typically one resistor in series with a parallel pair, all across a battery. The method never changes, and it earns marks at every line.

The circuit: a 12 volt battery with negligible internal resistance drives a 2 ohm resistor, which then feeds a parallel combination of a 6 ohm and a 3 ohm resistor, and the current returns to the battery.

Step one: collapse the network to one resistance. The parallel pair first: 6 times 3 over 6 plus 3, which is 18 over 9, giving 2 ohms. The circuit is now a 2 ohm and a 2 ohm in series: total 4 ohms.

Step two: total current from the battery. I equals V over R total: 12 divided by 4, which is 3 amperes. This current flows through the battery and through the series 2 ohm resistor.

Step three: walk the voltages. Across the series resistor: V equals I R, 3 multiplied by 2, which is 6 volts. The battery supplies 12, so the parallel pair receives 12 minus 6, which is 6 volts — and that same 6 volts sits across BOTH branches, because parallel branches share voltage.

Step four: split the current. Through the 6 ohm branch: 6 volts divided by 6 ohms, which is 1 ampere. Through the 3 ohm branch: 6 divided by 3, which is 2 amperes. Check: 1 plus 2 equals 3 amperes, exactly the total that arrived — current is conserved at every junction. Notice the pattern worth remembering: the SMALLER resistance carries the LARGER share of the current.

The checks are not decoration; they are how you catch your own slips under exam pressure. Voltages around the loop must add to the battery voltage: 6 plus 6 is 12. Branch currents must add to the arriving current: 1 plus 2 is 3. Run both checks every time and wrong answers cannot survive to the end of the page.

Work through this section's questions now, collapsing first, then walking voltages, then splitting currents.

## Subtopic: Power, Energy and the Price of Electricity

Power is the rate at which electrical energy is converted, measured in watts, one watt being one joule per second. Three interchangeable formulas: P equals V I, power equals voltage times current; P equals I squared R, current squared times resistance; and P equals V squared over R, voltage squared over resistance. Pick whichever pair of quantities the question has already given you.

In the network above: total power from the battery is V times I, 12 multiplied by 3, which is 36 watts. The series resistor converts I squared R, 3 squared times 2, which is 18 watts. The 6 ohm branch: V squared over R, 6 squared over 6, which is 6 watts. The 3 ohm branch: 6 squared over 3, which is 12 watts. Add the three: 18 plus 6 plus 12 equals 36 — every watt the battery supplies is accounted for.

Energy is power multiplied by time: W equals P delta t, in joules when power is in watts and time in seconds. A 100 watt lamp burning for one minute converts 6 000 joules.

But joules are too small for a household bill, so municipalities sell the KILOWATT-HOUR: the energy converted by one kilowatt running for one hour, which is 1 000 watts times 3 600 seconds, or 3,6 million joules. The billing recipe: kilowatt-hours equal power in KILOWATTS multiplied by time in HOURS. A 2 kilowatt kettle running for half an hour uses 2 times 0,5, which is 1 kilowatt-hour. At a tariff of 2 rand 50 per kilowatt-hour, that boiling session costs 2 rand 50. A 3 kilowatt geyser heating for 4 hours a day uses 12 kilowatt-hours daily — 30 rand a day, around 900 rand a month, which is why the geyser dominates every household bill.

The traps: watts must become kilowatts before billing arithmetic, minutes must become hours, and the kilowatt-hour is a unit of ENERGY, not power — calling it power costs the definition mark.

The final questions of this part are in front of you now — three power formulas, one energy formula, and the geyser paying for the revision.

# Part 2 — Simplifier

Now the same circuit ideas as water, traffic and a municipal bill you can actually read.

## Subtopic: One Road or Many Roads

Resistors combine in exactly two ways, and you already understand both from traffic.

SERIES is one road through several roadblocks. Every car must pass roadblock one, then roadblock two, then three. Add a roadblock and the whole road slows — total resistance grows with every resistor you add in series. And since there is only the one road, every car passes every roadblock: series resistors all carry the SAME current.

PARALLEL is opening side roads. Between the same two taxi ranks, one road or three roads? With three, the traffic splits itself among them and the total flow between the ranks INCREASES — which means the overall opposition dropped. That is the rule learners find unbelievable until they see the traffic: adding a resistor in PARALLEL always lowers the total resistance, below even the smallest branch, because every branch is one more open road. The 4 ohm with a 12 ohm beside it: 3 ohms total. Less than 4. More roads, easier travel.

The maths follows the picture. Series: just add — 4 plus 12 is 16. Parallel: add the EASE of each road rather than its difficulty — that is why the fractions flip — and for two resistors the shortcut is product over sum: 48 over 16, which is 3.

Your home is wired in parallel, and now you can see why. Every appliance gets the full 230 volts, each switches on and off without cutting the others, and the more you switch on, the more total current flows into the house.

Your questions on this section are with you now — one road adds roadblocks, side roads open traffic.

## Subtopic: Walking Through the Circuit Like a Marker

The mixed circuit — one resistor, then a parallel pair — frightens learners into freezing. Markers solve it with a calm four-move walk, and the walk never changes.

Move one: SHRINK. Fold the parallel pair into one number first — product over sum — then add the series resistor. The whole circuit becomes a single resistance, and the battery sees just one customer. Our example: the 6 and 3 fold into 2; add the series 2; the battery sees 4 ohms.

Move two: TOTAL CURRENT. Battery voltage divided by that single resistance: 12 over 4 is 3 amperes. That is the current leaving the battery, and it must pass through anything wired in series on the way.

Move three: SPEND THE VOLTS. The battery's 12 volts get spent along the loop. The series resistor takes volts equal to current times its resistance: 3 times 2, so 6 volts. Whatever remains — 12 minus 6, so 6 volts — lands across the parallel pair, and BOTH branches feel that same 6 volts. Parallel means same voltage; that is the sharing rule.

Move four: SPLIT THE AMPS. Each branch draws its own current from its shared voltage: 6 volts over 6 ohms gives 1 ampere; 6 volts over 3 ohms gives 2 amperes. The easier road carries more traffic — always check that the smaller resistor got the bigger current. Then the final audit: 1 plus 2 returns the 3 amperes you started with. The books balance.

Shrink, total, spend, split. Written as four labelled steps, this walk collects method marks even when one number slips — and the balance checks at the end catch the slip anyway.

The questions for this section are coming to you now — do the four moves in order, every time.

## Subtopic: Reading the Bill Like a Physicist

Electricity feels expensive and mysterious until you know the one unit the bill is written in. Municipalities do not sell volts or amps. They sell KILOWATT-HOURS, and a kilowatt-hour is beautifully concrete: run something rated one kilowatt for one hour, and you have used exactly one kilowatt-hour.

So every appliance in your house is a spender with a rate. The kettle: 2 kilowatts — but it only runs minutes at a time. Boil it for half an hour of total use and that is 1 kilowatt-hour: about 2 rand 50 at a typical tariff. The real thief is the geyser: 3 kilowatts, heating water roughly 4 hours across each day. That is 12 kilowatt-hours daily, around 30 rand a day, 900 rand a month — usually more than everything else combined. A phone charger, by contrast, sips a few thousandths of a kilowatt; charge it nightly for a month and you spend less than a single kettle boil.

Two numbers decide every line of the bill: the appliance's POWER — how fast it spends — and the TIME it runs. Multiply kilowatts by hours, then by the tariff. That is the whole secret, and it is also the saving strategy: you cut the bill by attacking big powers and long times. Shorter geyser hours, a geyser blanket, filling the kettle only as much as you need — these beat unplugging chargers a thousand times over.

One last translation. Watts measure how FAST energy is used — the speed of spending. Kilowatt-hours measure HOW MUCH was used — the total spent. A powerful appliance used briefly can cost less than a weak one running all day; the marathon beats the sprint on the bill.

The last questions of the lesson are yours now — kilowatts times hours times tariff, and check the geyser first.
