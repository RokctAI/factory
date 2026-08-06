# Part 1 — Expert

This session lays the foundation stones of every circuit you will ever analyse: current, potential difference, emf, and resistance — the four quantities, their defining formulas, and the two meters that measure them. The working thread is a simple torch circuit: a 6-volt battery, one bulb, one switch, one loop of wire. By the end we will know how much charge flows through it, how much energy every coulomb carries and where that energy goes, why the battery's sticker voltage and its working voltage differ, and what, physically, is resisting all this — down to the collisions happening inside the metal.

## Subtopic: Current — Counting Charge Past a Point

Electric current is the rate of flow of charge. In symbols: I equals Q over delta t — the current equals the charge passing a point, divided by the time it takes to pass. Charge is measured in coulombs; current in amperes, symbol A; and the definition ties them: one ampere is one coulomb per second passing a point. An ampere is not an amount of charge — it is a RATE, charge per second, the way litres per minute is a rate and not a volume.

The formula runs three ways, and exams use all three. Given charge and time, find current: if 300 coulombs pass through a kettle's element in 40 seconds, I equals 300 over 40, which is 7,5 amperes. Given current and time, find charge: our torch bulb carries 0,5 amperes for 2 minutes — convert first, 2 minutes is 120 seconds — so Q equals I times delta t, which is 0,5 times 120, giving 60 coulombs. Given current and charge, find time: delta t equals Q over I.

Direction next, by convention. The current in a circuit diagram is drawn from the POSITIVE terminal of the battery, through the external circuit, and back to the negative terminal. Historically this was named conventional current, chosen before anyone knew that the moving particles in a metal are electrons drifting the opposite way. The convention stands, every diagram uses it, and stating it is a routine mark.

And one misconception to execute early, because it undermines everything later: a battery is NOT a source of constant current, dispensing the same amperes no matter what. A battery supplies a fixed emf — a fixed number of volts — and the CIRCUIT decides how much current flows. Connect a small resistance and the current is large; connect a large resistance and the current is small. The volts are the battery's promise; the amps are negotiated with whatever you connect.

The questions for this section are with you now: the definition with its formula, the kettle and torch numbers reworked, the direction of conventional current, and the misconception about batteries and constant current rejected with a reason.

## Subtopic: Potential Difference, emf and the Energy Story

Current counts the charge; potential difference prices the energy it carries. The definition: potential difference is the work done per unit charge. In symbols: V equals W over Q — the potential difference between two points equals the energy transferred, divided by the charge that carried it. The unit is the volt: one volt is one joule per coulomb. Say the meaning whenever you see the number: a 6-volt battery gives every coulomb 6 joules of energy; a bulb with 6 volts across it takes 6 joules from every coulomb passing through.

Calculations run both ways. A battery does 24 joules of work driving 4 coulombs through itself: V equals 24 over 4, which is 6 volts. And rearranged: with 12 volts across a heater, 60 coulombs deliver W equals V times Q, which is 12 times 60, giving 720 joules of heat.

Now the distinction CAPS names explicitly. The emf of a battery is the voltage measured across its terminals when NO current flows — the open-circuit reading, with the switch off. The terminal potential difference is the voltage across those same terminals when current IS flowing — the working reading, switch on. Measure both on a real battery and the terminal pd comes out slightly LOWER than the emf, because the battery itself resists the current a little and spends some energy internally; the reason gets its full treatment in Grade 12, but the two definitions and the direction of the difference are Grade 10 marks.

Follow the energy through the whole loop, because this story is asked every year. In the battery, chemical potential energy is converted to electrical energy — each coulomb is loaded with its joules. In the bulb's filament, that electrical energy is converted to heat and light. The charge itself is never consumed: the same coulombs circulate round and round the loop. What runs out is the battery's stock of chemical energy — and that is exactly why a battery goes flat: not empty of charge, empty of chemical energy to load the charge with.

Take this section's questions now: V equals W over Q in both directions, emf and terminal pd defined by their switch positions, which of the two reads higher, and the flat-battery story told in energy conversions.

## Subtopic: Reading the Circuit — Ammeters and Voltmeters

Two instruments, two rules, and marks lost every single year for swapping them.

The ammeter measures current. Current is flow THROUGH a component, so the ammeter must be connected in SERIES — spliced into the loop so that the same charge flowing through the component flows through the meter. Break the wire on either side of the torch bulb, insert the ammeter into the gap, and it counts the coulombs per second passing. For the meter not to disturb what it measures, an ammeter is built with a very LOW resistance — adding it to the loop barely changes the current it is trying to read.

The voltmeter measures potential difference. Potential difference is a comparison BETWEEN two points — the energy difference per coulomb across a component — so the voltmeter connects in PARALLEL, one lead on each side of the component, bridging it without interrupting the loop. To avoid stealing current through itself, a voltmeter is built with a very HIGH resistance — only a trickle diverts through the meter, and the circuit behaves as if it were not there.

Polarity matters for both: the meter's positive terminal must face the positive terminal of the battery — connect it reversed and the needle drives the wrong way. And a practical rule for multi-scale meters: connect to the LARGEST scale first, so an unexpectedly large reading cannot slam the needle past its limit and damage the instrument; step down to finer scales once you know the size.

Draw the fully instrumented torch circuit in your mind, and sketch it after. The loop: battery, switch, bulb, back to the battery. The ammeter sits IN the loop, in line with the bulb. The voltmeter hangs OUTSIDE the loop like a bridge, its two leads touching either side of the bulb. Series in the loop, parallel across the gap — one preposition each: current THROUGH, potential difference ACROSS.

Work this section's questions now: each meter placed correctly with its reason, the resistance each is built with and why, the polarity and largest-scale rules, and the instrumented circuit described end to end.

## Subtopic: Resistance — the Opposition in the Wire

Resistance is the opposition of a conductor to the flow of electric current. Symbol R, unit the ohm, symbol omega — and the unit's definition ties the quantities together: one ohm is one volt per ampere, the resistance that lets exactly one ampere flow when one volt is applied. Our torch bulb, carrying 0,5 amperes with 6 volts across it, has R equals V over I, which is 6 over 0,5, giving 12 ohms.

Now go microscopic, because CAPS asks for the mechanism, not just the number. A metal is a lattice of vibrating positive ions bathed in free electrons. Drive a current and the electrons drift through the lattice — and collide, constantly, with the vibrating ions. Each collision transfers kinetic energy from electron to lattice, and that energy appears as heat. Resistance IS this collision story: the electrical energy the battery gave each coulomb is delivered to the metal, collision by collision. Every resistor is a converter of electrical energy into heat — and sometimes light, when the wire runs hot enough to glow, which is the entire job description of a bulb's filament and a kettle's element.

Four factors set a conductor's resistance, each explained by collisions. LENGTH: a longer wire means more lattice to cross and more collisions — resistance increases with length. THICKNESS: a thicker wire offers more parallel room for the drift, like a wider corridor for the same crowd — resistance decreases as cross-section grows. TEMPERATURE: a hotter metal has ions vibrating more violently, making collisions more frequent — resistance rises with temperature. MATERIAL: some metals simply hold the record for easy passage — copper conducts superbly and wires are made of it; nichrome resists strongly and heating elements are made of it.

Close the loop on the energy story. Battery: chemical to electrical. Wires: near-zero resistance, energy passes almost untouched. Bulb: electrical to heat and light, the collisions cashing out every coulomb's load. The charge circulates unconsumed; the chemical stock drains; the battery dies with its charge intact and its energy spent.

The final questions of this part are with you now: the definition and the ohm, the 12-ohm bulb reproduced, the collision mechanism narrated, and all four factors with their microscopic reasons.

# Part 2 — Simplifier

Now the same four ideas through water — because a circuit is a plumbing loop, and you have been reading plumbing your whole life.

## Subtopic: The Water Loop

Picture a closed loop of pipe, completely full of water, with a pump at the bottom. The pump pushes, and the water circulates round and round — the same water, lap after lap. Nothing is sprayed out, nothing drains away.

That is a circuit. The water is the charge — the coulombs. The pump is the battery. The flowing round is the current. And the first big idea is already visible: the pump does not CREATE water, and a battery does not create charge. The charge was always in the wires, the way the water was always in the pipes. The pump just sets it moving.

How would you measure the flow? Stand at one spot and count litres passing per second. Current is exactly that count, but for charge: coulombs passing a point per second, and one coulomb per second is called one ampere. Notice it is a RATE — amps are not "how much electricity", they are "how fast it is passing you", like litres per minute at a tap.

The counting formula is just the sentence in symbols: current equals charge over time. A bulb carrying half an amp for two minutes — 120 seconds — has passed half of 120, which is 60 coulombs. A kettle passing 300 coulombs in 40 seconds is flowing at 300 over 40 — 7,5 amps. Same recipe both ways.

One habit to install now: current in diagrams is drawn flowing from the battery's positive terminal, round the circuit, into the negative terminal. That is the agreed convention everywhere, so draw it without hesitation.

And the misconception to drown on day one: the pump does not deliver the same flow no matter the plumbing. Narrow, clogged pipes and the flow is a trickle; wide, clear pipes and it gushes. Same pump, different flow — the PIPES decide. Batteries are the same: fixed push, and the circuit decides the amps.

Quick check — the questions on this piece are with you now: what flows, what the amp counts, which way the arrows go, and who really decides the current.

## Subtopic: The Push and the Price

If the water only ever goes in a loop, what is the pump actually giving it? Not water — PUSH. Pressure. Energy to spend on the way round.

That is what volts measure. The battery loads every coulomb with a fixed number of joules to spend per lap: a 6-volt battery loads 6 joules onto every coulomb, because a volt is exactly one joule per coulomb. Potential difference is energy per charge — the price tag on the push. So the formula reads: volts equal work over charge. A battery that spends 24 joules pushing 4 coulombs is a 24-over-4 battery: 6 volts. A 12-volt heater visited by 60 coulombs collects 12 times 60 — 720 joules of heat. Volts times coulombs gives joules, always.

Now the sticker-versus-working detail. Read the battery's voltage with everything switched OFF and you get its full promise — the emf. Switch the circuit ON, current flowing, and the reading across the same two terminals dips slightly — the terminal potential difference. Why the dip? The pump itself is slightly clogged — the battery resists its own current a little and spends some energy inside itself. Sticker value with the switch off, slightly lower working value with the switch on: two names, one battery, and the exam wants both definitions and which one reads higher.

And here is the whole life story of a battery in one paragraph. Inside the battery, stored chemical energy loads each passing coulomb — chemical becomes electrical. Inside the bulb, each coulomb spends its load — electrical becomes heat and light. The coulombs themselves never get used up; they circulate forever, the same water round the same loop. What empties is the battery's chemical store. A flat battery is not out of charge — it is out of MONEY to give the charge. That single sentence answers the why-does-a-battery-go-flat question every time it appears.

Your questions for this section are up now: joules per coulomb as the meaning of the volt, the 6-volt and 720-joule sums, emf against terminal pd, and the flat battery explained without the word "empty".

## Subtopic: Clogs, Meters and the Kettle's Secret

Last piece: what fights the flow, and how we take the measurements.

Resistance is the clog in the pipe — anything that makes the water work to get through. In the wire, the story is physical: the metal is a jungle of vibrating ions, and the drifting electrons smack into them over and over, losing energy at every collision. Those collisions ARE the resistance, and the lost energy leaves as heat. That is the kettle's secret, and the toaster's, and the old glowing bulb's: their working parts are DELIBERATELY resistant wire — nichrome, usually — built so that the collisions dump heat exactly where you want it. Copper wires everywhere else are the opposite bet: so little resistance that the energy arrives at the appliance unspent.

Four things make a clog worse, and each is common sense once you see the collisions. Longer pipe: more jungle to cross, more resistance. Thicker pipe: more room to pass, less resistance. Hotter metal: the jungle shakes harder, collisions multiply, more resistance. And the material itself: copper is a highway, nichrome a thornbush. Ohms measure the clog, and one ohm means one volt of push squeezes through one amp of flow. The torch bulb taking 6 volts to carry half an amp is 6 over 0,5 — a 12-ohm clog.

Measuring is two tools with opposite manners. The flow meter — the AMMETER — must sit IN the pipe: cut the loop, splice it in, and the whole flow passes through its counter. It is built nearly clog-free, very low resistance, so adding it barely changes what it measures. The pressure gauge — the VOLTMETER — never joins the loop: it bridges ACROSS a component, one lead each side, comparing the energy before and after. It is built nearly impassable, very high resistance, so almost nothing detours through it. Series for the ammeter, parallel for the voltmeter; through for current, across for volts. Swapping them is the classic lost mark — and in a real laboratory, an ammeter connected across a battery is a short circuit and a burnt-out meter.

So carry the loop out of this lesson in four lines. Current: coulombs per second past a point, decided by the circuit, drawn positive to negative. Volts: joules per coulomb — the battery's loading price, the appliance's spending price. Resistance: collisions in the jungle — longer and hotter means more, thicker and copper means less. Meters: ammeter in the loop, voltmeter across the gap. Here come the last questions of the lesson: the clog factors, the two meters seated correctly, and the kettle's secret told in collisions.
