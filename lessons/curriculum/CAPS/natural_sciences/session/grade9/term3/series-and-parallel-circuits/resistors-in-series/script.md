# Part 1 — Expert

This session sets out the behaviour of resistors and bulbs connected in series: the current is the same at every point, the voltage of the source divides between the resistors, and adding resistors in series increases the total resistance and decreases the current. The anchor examples are two identical bulbs on a 6 volt battery, each with 3 volts across it, a 9 volt battery with 3 volts across one resistor and 6 volts across a larger one, and ammeter readings that are identical at every point and fall as each bulb is added. The governing principle is that in a series circuit there is only one path, so all the charge passes through every component, and the energy each unit of charge receives from the source is shared out among the components.

## Subtopic: Current in a Series Circuit

Components are connected in series when they are joined one after another in a single loop, so that there is only one path for the current. If you trace the circuit with your finger from the positive terminal of the battery, you pass through every component in turn before returning to the negative terminal.

The first rule of series circuits: the current is the same at every point. An ammeter placed between the battery and the first bulb, between the first and second bulbs, or between the last bulb and the battery gives exactly the same reading. This is because charge is not used up or stored in the components; every unit of charge that enters a bulb leaves it, so the rate of flow is the same everywhere around the single loop. For example, if one ammeter reads 0,2 amperes, every ammeter in that series circuit reads 0,2 amperes.

A practical consequence: since there is only one path, a break anywhere stops the current everywhere. If one bulb's filament breaks or is unscrewed, the circuit is open and all the bulbs go out. Old strings of festive lights were wired in series, so a single blown bulb made the whole string go dark, and finding the faulty bulb meant testing each one. A switch placed anywhere in a series circuit controls all the components.

An investigation confirms the rule. Build a circuit with a battery, a switch and three bulbs in series, and connect an ammeter first between the battery and the first bulb, then between the first and second bulbs, then between the second and third, then between the third bulb and the battery, switching off each time the ammeter is moved. Record the readings in a table. Within the small errors of the meter, all four readings are the same. A common mistake when doing this practical is to connect the ammeter across a bulb instead of in the loop; that creates a short circuit around the bulb, because an ammeter has almost no resistance, and the bulb goes out.

Drawing a series circuit correctly matters for marks: the components are drawn one after another on a single rectangular loop, with no junctions or branches, and each meter drawn in its correct position, ammeters in the loop and voltmeters on small loops across components.

The questions for this section are with you now: identifying a series circuit, the same current everywhere and why one break stops everything.

## Subtopic: Voltage Divides in Series

The second rule: the voltage of the source is shared between the components in series. The voltages across the individual components add up to the voltage of the source.

Two identical bulbs connected in series to a 6 volt battery each have 3 volts across them, since 3 + 3 = 6 volts. Three identical bulbs on the same battery each have 2 volts, since 2 + 2 + 2 = 6 volts.

If the resistors are not identical, the larger resistance gets the larger share of the voltage. On a 9 volt battery, a resistor of 10 ohms in series with a resistor of 20 ohms has 3 volts across the smaller resistor and 6 volts across the larger, since 3 + 6 = 9 volts, and the larger resistor has twice the resistance and twice the voltage.

The reason is energy. The voltage of the battery is the energy it gives to each unit of charge. As that charge passes through the components in turn, it gives up part of its energy in each one, and by the time it returns to the battery it has given up all of it. So the energy given up in all the components together equals the energy received from the battery. A component with more resistance takes a bigger share of the energy.

Voltages are measured by connecting a voltmeter across each component in turn, and then across the battery. The voltmeter readings provide a check: they should add up to the battery voltage, apart from small losses in the connecting wires.

This idea, the voltage divider, is used in electronics to provide a smaller voltage from a larger one, and in sensors: a light-dependent resistor in series with a fixed resistor gives a voltage that changes with the light level, which can switch a street light on at dusk.

A results table for the voltage investigation has columns for the voltage across each bulb and the voltage across the battery. For example, with three identical bulbs on a 4,5 volt battery, the readings might be 1,5, 1,5 and 1,5 volts across the bulbs and 4,5 volts across the battery. With small real-world differences between bulbs, they might be 1,4, 1,6 and 1,5 volts, which still add up to 4,5 volts. The conclusion is written as: the sum of the voltages across the components in series equals the voltage across the source.

The questions for this section are ready: sharing the voltage between identical and different resistors, and checking that the voltages add up.

## Subtopic: Adding Resistors in Series

The third rule: adding resistors in series increases the total resistance of the circuit, so the current decreases.

The total resistance of resistors in series is the sum of their resistances. A 10 ohm resistor and a 20 ohm resistor in series have a total resistance of 10 + 20 = 30 ohms. The charge must pass through both, so the opposition adds up, just as a longer wire has more resistance than a shorter one.

With the same battery, a larger total resistance means a smaller current. One bulb on a battery might draw 0,3 amperes; with two identical bulbs in series, the current is roughly halved, to about 0,15 amperes; with three, it is smaller still. Each bulb also has a smaller share of the voltage. As a result, every bulb glows more dimly as more bulbs are added. In practice the current does not halve exactly, because a dimmer filament is cooler and has a lower resistance, but the trend is always the same.

This can be summarised in a table for identical bulbs on the same battery: one bulb, full voltage, largest current, brightest; two bulbs, half the voltage each, smaller current, dimmer; three bulbs, a third of the voltage each, smaller current still, dimmer still.

Series circuits are useful when one switch must control everything, when a fuse must protect a whole circuit, since a fuse is always in series with what it protects, and in voltage dividers. They are unsuitable for house lighting, because every light would be dim and one failure would put out all of them.

Comparing a series circuit with a single bulb shows how energy is shared too. With one bulb, all the energy the battery supplies each second goes into that bulb. With two identical bulbs in series, the current is smaller, so the battery supplies less energy each second, and that smaller amount is split between two bulbs. In the ideal case, with half the voltage and half the current, each bulb receives only about a quarter of the energy per second of the single bulb, which is why the drop in brightness is so noticeable. As a side effect, the battery lasts longer, because less current is drawn from it.

The questions for this section are waiting: total resistance, the effect of adding bulbs on current and brightness, and uses of series circuits.

## Subtopic: Analysing Series Circuits and the Error Museum

A typical examination question gives a circuit diagram: a 12 volt battery, a switch, an ammeter and three resistors in series, with a voltmeter across each resistor. If the ammeter reads 0,5 amperes and the voltmeters across the first two resistors read 3 volts and 4 volts, then the third must read 12 − 3 − 4 = 5 volts, and every point in the circuit carries 0,5 amperes. If a fourth resistor is added, the ammeter reading decreases. If any resistor is removed and the gap left open, the ammeter reads zero.

The error museum for this lesson has five exhibits. One: the current is used up, so it is smaller after each bulb; it is the same everywhere. Two: the first bulb is brightest because it gets the current first; identical bulbs in series are equally bright. Three: each bulb in series gets the full battery voltage; the voltage divides. Four: adding a bulb in series makes the current larger; it makes it smaller. Five: one blown bulb only affects itself; it breaks the only path, so all go out.

Layout for a series answer: state that the current is the same everywhere; show the voltages adding to the battery voltage with working; state how total resistance and current change when a resistor is added or removed; and state the effect on brightness.

Fault-finding uses the same rules. If all the bulbs in a series circuit are out, the fault is a break somewhere in the loop. Connecting a voltmeter across each bulb in turn finds it: across a working bulb in an open circuit the reading is zero, but across the broken bulb the voltmeter reads the full battery voltage, because the meter completes the loop through itself. If one bulb is out but the others glow brightly, that bulb has been short-circuited by a wire or by a fault, so the remaining bulbs share the voltage between fewer of them.

The questions for this section are with you now: missing voltages, predicting changes and the five exhibits.

# Part 2 — Simplifier

Now the same ideas again, through one road only, sharing the push and more bulbs, dimmer bulbs — plain words, same facts.

## Subtopic: One Road Only

In a series circuit, everything is on one single loop, one after the other, like beads on a necklace. There is only one road for the current.

Rule one: the current is the same everywhere. Put an ammeter before the first bulb, between the bulbs or after the last bulb, and you get the same number every time. Nothing gets used up along the way. Every bit of charge that goes into a bulb comes out the other side.

So why do people think the first bulb is brighter? They imagine the current gets used up. It does not. Identical bulbs in series glow equally.

And here is the catch with one road: break it anywhere and everything stops. Unscrew one bulb and all the others go out. Old festive lights were like this. One dead bulb and the whole string went dark, and you had to test every bulb to find the culprit.

Test it in class. Move one ammeter to different places around a series loop, switching off each time. The reading stays the same. Be careful to put the ammeter into the loop, not across a bulb, or the bulb will go out.

Keep the one road in mind and try the questions for this part: the same current everywhere and what happens when one bulb breaks.

## Subtopic: Sharing the Push

Rule two: in series, the battery's push, its voltage, is shared out between the bulbs.

Two identical bulbs on a 6 volt battery: each gets 3 volts. Three identical bulbs: each gets 2 volts. Add the shares up and you always get back to the battery's voltage.

Think of the charge as carrying a bag of energy from the battery. It hands out some at each bulb on the way round, and arrives back at the battery with an empty bag. So the shares must add up to what the battery gave.

If the resistors are different, the bigger one takes the bigger share. On a 9 volt battery, a small resistor might get 3 volts and a resistor twice as big gets 6 volts.

To check, connect a voltmeter across each bulb in turn, then across the battery. The bulb readings add up to the battery reading.

Real bulbs are never perfectly identical, so you might read 1,4, 1,6 and 1,5 volts across three bulbs on a 4,5 volt battery. The shares are slightly uneven, but they still add up to 4,5.

Keep sharing the push in mind and try this part's questions: splitting the voltage and adding it back up.

## Subtopic: More Bulbs, Dimmer Bulbs

Rule three: every bulb you add in series makes the whole road harder to travel. The total resistance goes up, so the current goes down.

Resistances in series simply add. A 10 ohm and a 20 ohm resistor make 30 ohms together.

So with one bulb you get a bright light. Add a second identical bulb: each one gets half the voltage, the current drops to about half, and both glow dimly. Add a third: dimmer still.

That is why houses are never wired in series. Every light would be dim, and one blown bulb would plunge the whole house into darkness.

But series has its uses. One switch can control everything on the loop. And a fuse is always put in series, so that when it melts it cuts off everything it protects.

Pocket summary of the lesson. In series there is one path. The current is the same everywhere. The battery's voltage divides between the components and the shares add up to the total. Resistances add, so more resistors mean less current and dimmer bulbs. One break stops everything. Grade 10 to 12 Physical Sciences calculates these values with Ohm's law.

There is one bonus to dim bulbs in series: less current is drawn, so the battery lasts longer. You get less light, but for more time.

Hold more bulbs, dimmer bulbs in mind and take the final questions of the lesson: adding resistances, falling current and why houses are not wired in series.
