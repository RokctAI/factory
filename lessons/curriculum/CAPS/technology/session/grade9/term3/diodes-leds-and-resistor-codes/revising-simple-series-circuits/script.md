# Part 1 — Expert

This session revises simple series circuits with cells, a switch and lamps. The anchor is a Technology room in Mthatha where each pair of learners has a 4.5 volt battery pack, a push switch, a torch bulb in a holder and crocodile leads, with half the circuits refusing to light on the first try because of a loose lead or a dead cell. The governing idea is that a working circuit is a complete loop from the positive terminal through the switch and the load back to the negative terminal, that faults are found by checking the loop section by section with a known-good lamp or a meter, and that the PAT indicator circuit is this same loop with an LED and series resistor as the load and a sensor as the switch. Drawing, building and fault-finding a simple series circuit and measuring its voltage and current are examinable.

## Subtopic: The Simple Series Circuit: Cell, Switch and Lamp

The simplest useful circuit is a supply, a switch and a load in one loop. The supply is a cell or a battery of cells; the switch opens and closes the loop; the load is the component that does the work, here a lamp. Drawn with symbols: the battery on the left with its positive terminal at the top, a wire from the positive terminal to the switch, the switch to the lamp, the lamp back to the negative terminal. With the switch open there is a gap and the lamp is off; close it and the loop is complete, current flows from positive through the switch and lamp to negative, and the lamp lights.

Each part has a job and a rating. The battery's voltage must suit the lamp: a 4.5 volt battery with a bulb rated 3.5 to 4.5 volts gives full brightness; a 1.5 volt cell with the same bulb gives a dull glow; a 9 volt battery burns it out. The switch must carry the current without heating; a small push switch is fine for a torch bulb. The lamp's rating is printed on its base in volts and sometimes amperes or watts. Matching the supply to the load is the first design decision in any circuit and it returns with the LED next week, where the match is made with a resistor.

Why series here: with one load there is only one loop to make, and a switch must be in series with whatever it controls, because it works by breaking the path. A switch in parallel with the lamp would short the lamp out when closed, sending the current round the switch instead of through the lamp, and would also drain the battery hard. Every control switch in every circuit this term, including the sensors, is in series with the thing it controls.

The questions for this section are with you now: the three-part loop and its symbols, matching supply to load, and why the switch is in series.

## Subtopic: Building, Fault-Finding and Measuring the Circuit

Building the circuit on a board or with crocodile leads is quick; getting it to work the first time is not guaranteed. When the lamp does not light with the switch closed, the fault is found methodically, not by shaking things. First the supply: is the battery pack fresh, are the cells the right way round, is the connector clean? Test by touching the lamp holder's leads directly to the battery terminals; if it lights, the battery and lamp are fine and the fault is in the switch or leads. Second the lamp: is it screwed home, is the filament intact; swap in a known-good lamp. Third the switch: with the circuit live, bridge the switch with a spare lead; if the lamp lights, the switch is faulty or wired to the wrong terminals. Fourth the leads: a crocodile clip gripping insulation instead of metal is the commonest fault of all.

Two meters make this precise. A voltmeter is connected across a component, in parallel with it, and reads the voltage between its two ends: across the battery it should read about 4.5 volts; across a working lamp with the switch closed, nearly the same; across an open switch, the full battery voltage, since the switch is where the whole voltage is dropped when nothing flows; across a closed switch, nearly zero. An ammeter is connected in the loop, in series, so that all the current passes through it; for a torch bulb on 4.5 volts it reads a few tenths of an ampere, perhaps 0.3. A reading of zero with the switch closed means the loop is broken somewhere.

Recording the measurements forms the first row of the Ohm's law table in a later session: 4.5 volts across the lamp, 0.3 amperes through it. Safety with the meters: an ammeter is never connected across the battery, because its very low resistance would let a large current flow and damage the meter or the battery; the voltmeter is safe across anything in these low-voltage circuits.

The questions for this section are with you now: methodical fault-finding, the voltmeter across and the ammeter in the loop, and expected readings.

## Subtopic: From the Series Circuit to the PAT Indicator Circuit

The PAT indicator grows from this loop by substitution. Replace the lamp with an LED and a series resistor: the LED is the load that shows the warning, bright and efficient, and the resistor keeps its current safe, which is next week's work. Replace the push switch with a sensor: a float switch, two probes in the water, a reed switch and magnet, or later a transistor driven by a light-dependent resistor. Keep the battery, three cells in series for 4.5 volts. The circuit is still supply, switch and load in one loop; only the parts have become more suited to the job.

The habits learnt on the simple circuit carry over. Draw first, with symbols, positive at the top. Match the supply to the load. Put every control in series with what it controls. When it fails, test the supply, then the load, then the switch, then the leads, in that order. Measure voltage across and current through. These are the habits that make the PAT model work on the day of the presentation rather than on the bench the week before.

A quick exercise: draw the torch circuit, then redraw it as the PAT indicator with a float switch, an LED, a resistor and a 4.5 volt battery, and list the ratings needed for each part. The error museum, four exhibits. One: a switch in parallel with the lamp, shorting it. Two: a 9 volt battery on a 4.5 volt bulb. Three: an ammeter across the battery. Four: fault-finding by wiggling every lead at once so that the fault is never located.

The questions for this section are with you now: how the simple loop becomes the PAT indicator, the habits that carry over, and the ratings exercise.

# Part 2 — Simplifier

Now the same lesson again with the battery packs, push switches and torch bulbs in Mthatha — plain words, same facts.

## Subtopic: One Loop, Three Parts

Supply, switch, load, one loop. Battery on the left, positive up. Wire to the switch, switch to the lamp, lamp back to negative. Switch open: gap, dark. Switch closed: loop, light.

Match the volts. 4.5 volt battery, 4.5 volt bulb: bright. 1.5 volts: dull. 9 volts: dead bulb. Ratings are printed on the base.

The switch goes in series with what it controls, because it works by breaking the path. In parallel it would short the lamp out and flatten the battery.

Keep one loop, three parts in mind and try the questions for this part: the simple circuit.

## Subtopic: When It Does Not Work

It does not light. Do not shake it. Check the battery: touch the lamp straight to it. Check the lamp: swap in a good one. Check the switch: bridge it with a lead. Check the leads: a clip on the plastic is the usual culprit.

Voltmeter goes across a part: about 4.5 across the battery, almost the same across a working lamp, full volts across an open switch, nearly zero across a closed one. Ammeter goes in the loop: about 0.3 amperes for a torch bulb. Zero means a break.

Never put the ammeter across the battery. Write down your volts and amps; you will use them for Ohm's law.

Hold when it does not work in mind and try this part's questions: faults and meters.

## Subtopic: The Same Loop With Better Parts

Same loop, better parts. Lamp becomes LED plus resistor. Push switch becomes a float switch or probes or a sensor. Battery stays three cells, 4.5 volts.

Habits: draw first, match the volts, controls in series, test supply then load then switch then leads, volts across and amps through.

Exercise: draw the torch, redraw it as the tank indicator, list the ratings.

Pocket summary of the lesson. A simple series circuit is a supply, a switch and a load in one loop, drawn with symbols and working only when the loop is complete. The supply voltage must match the load's rating, and every control switch sits in series with what it controls. Faults are found in order: supply, load, switch, leads. A voltmeter is connected across a component and an ammeter in the loop, never across the battery. The PAT indicator is this same loop with an LED and resistor as the load and a sensor as the switch.

Hold the same loop with better parts, and take the final questions of the lesson: growing the circuit.
