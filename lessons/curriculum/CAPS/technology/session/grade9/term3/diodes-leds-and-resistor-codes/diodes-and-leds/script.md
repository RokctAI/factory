# Part 1 — Expert

This session covers diodes, which allow current in one direction only, and LEDs as indicators. The anchor is a cellphone charger plug opened on a bench in Polokwane, its small black diodes turning the mains alternating current into the one-way current a battery needs, next to a bag of coloured LEDs for the PAT indicators, one of them already dead because a learner wired it straight to the battery. The governing idea is that a diode conducts when its anode is more positive than its cathode and blocks when reversed, that an LED is a diode which emits light when conducting and drops a fixed voltage of about 2 volts, and that the remaining supply voltage must be absorbed by a series resistor to hold the current to a safe 10 to 20 milliamperes. Drawing the diode and LED symbols with correct polarity, explaining one-way conduction and justifying the series resistor are examinable.

## Subtopic: The Diode: A One-Way Valve for Current

A diode is a two-terminal component that conducts current in one direction only. Its terminals are the anode and the cathode. When the anode is connected toward the positive side of the supply and the cathode toward the negative, the diode is forward biased and conducts, behaving almost like a closed switch, except that it uses up about 0.7 volts across itself. When connected the other way, cathode toward positive, it is reverse biased and blocks, behaving like an open switch. The symbol is a triangle pointing at a bar: the triangle is the anode side and shows the direction conventional current may flow, the bar is the cathode and is marked on the real component by a band at one end.

Diodes are everywhere that current must be kept one-way. In a charger they rectify, turning alternating current, which reverses direction many times a second, into current flowing one way to charge the battery. In a solar panel system a diode stops the battery draining back through the panel at night. Across a relay coil or a motor a diode absorbs the voltage spike when the current is switched off, protecting the transistor that does the switching. In a circuit where a battery might be connected the wrong way round, a diode in series stops reversed current from damaging the components.

Testing a diode shows the behaviour. In a loop with a battery, a lamp and the diode, connect the diode one way: the lamp lights, slightly dimmer than without the diode because of the 0.7 volts the diode takes. Reverse the diode: the lamp is off, although the loop looks complete. Nothing else in the course so far behaves like this; a lamp or resistor works either way round. The one-way behaviour is the whole point, and it is why the diode's symbol has a direction.

The questions for this section are with you now: anode, cathode and forward and reverse bias, the symbol and the band, and uses of ordinary diodes.

## Subtopic: The LED: A Diode That Lights, and Why It Needs a Resistor

A light-emitting diode is a diode made from materials that give off light when current passes through them in the forward direction. It has the diode's one-way behaviour, lights only when forward biased, and the symbol is the diode symbol with two small arrows pointing away from it to show emitted light. On the component, the longer leg is usually the anode, and the rim of the plastic body has a flat spot on the cathode side. An LED is far more efficient than a filament lamp, converting most of its energy to light rather than heat, lasts tens of thousands of hours, switches on instantly and comes in red, green, yellow, blue and white, as well as high-brightness types visible in daylight.

The LED's weakness is that it has almost no resistance of its own once it conducts. A red LED drops about 2 volts across itself whatever the current, and if it is connected straight across a 4.5 volt battery the battery tries to force the remaining 2.5 volts through a component with nearly zero resistance; the current rises to whatever the battery can give, the LED heats and dies in a fraction of a second. This is the dead LED in the bag. The LED must be fed a controlled current, usually 10 to 20 milliamperes, and the component that does this is a resistor in series.

The resistor works by taking the voltage the LED does not need. With a 4.5 volt battery and an LED dropping 2 volts, the resistor must drop the other 2.5 volts. If the current is to be 10 milliamperes, which is 0.01 amperes, the resistor must have a value of 2.5 divided by 0.01, which is 250 ohms; the nearest common value is 270 ohms, and the 470 ohm resistor used in the PAT circuits gives a safe, slightly dimmer 5 milliamperes. This calculation is Ohm's law, treated fully in a later session; for now the rule is that every LED has a series resistor of a few hundred ohms on a 4.5 to 9 volt supply, and the value is chosen so the current is well under 20 milliamperes.

The questions for this section are with you now: the LED as a light-emitting diode and its symbol and legs, why an LED without a resistor burns out, and how the resistor value is chosen.

## Subtopic: Using LEDs as Indicators in the PAT Device

In the PAT device the LED is the output that tells the grandmother the tank is low. Its circuit is the 4.5 volt battery, the sensor switch, the resistor and the LED in series, with the LED's anode toward the positive side. The choice of LED matters: a standard 5 millimetre red LED is fine indoors but is washed out by daylight; a high-brightness red or white LED, or two LEDs in series with a smaller resistor, is visible from across a room in sunlight. Red is the colour of warning and is seen well by older eyes. A flashing LED, which has a tiny circuit inside that blinks it, draws attention better still and uses less battery because it is off half the time.

Several LEDs can show several states. Green for tank full, red for tank low: two sensors, two LEDs, each with its own resistor, in parallel across the battery so that each gets the full voltage. A row of LEDs at different heights, each with a probe, becomes the LED ladder seen in the shop. Each LED always has its own resistor; sharing one resistor between LEDs in parallel leads to one LED hogging the current and the others dimming.

Handling LEDs: identify the anode by the longer leg and the cathode by the flat spot before soldering; never connect an LED directly across a battery, even to test it, without a resistor; bend legs with pliers, not fingers, near the body; and check polarity in the diagram before the board, because a reversed LED simply does not light and may be mistaken for a dead one. The error museum, four exhibits. One: LED straight across the battery with no resistor. Two: LED reversed, with the long leg toward negative. Three: one resistor shared by several parallel LEDs. Four: drawing the LED symbol without the arrows, so it reads as an ordinary diode.

The questions for this section are with you now: the LED indicator circuit and LED choice for daylight, several LEDs for several states, and handling and polarity.

# Part 2 — Simplifier

Now the same lesson again with the opened charger plug and the bag of LEDs in Polokwane — plain words, same facts.

## Subtopic: Current Goes One Way Only

A diode lets current through one way and blocks it the other. Anode toward positive and it conducts, using about 0.7 volts. Flip it and it blocks. Symbol: a triangle pointing at a bar; the triangle shows the way current may go; the bar matches a band on the real part.

Chargers use diodes to make one-way current for the battery. Solar systems use one to stop the battery leaking back at night. Motors get one to soak up the spike when switched off.

Test it: battery, lamp, diode. One way, lamp lights a bit dimmer. Other way, dark, even though the loop looks complete.

Keep current goes one way only in mind and try the questions for this part: diodes.

## Subtopic: A Light That Must Be Protected

An LED is a diode that glows when current goes the right way. Symbol: diode plus two little arrows flying off. Long leg is the anode, flat spot on the rim is the cathode. Efficient, cool, long life, instant, many colours.

Weakness: once it conducts it has almost no resistance. Straight across 4.5 volts it drops 2, the battery forces the rest through, the current shoots up, and it dies in a flash. That is the dead one in the bag.

Fix: a resistor in series to take the spare volts. 4.5 minus 2 is 2.5 volts; for 10 milliamperes that is 250 ohms, so use 270 or the PAT's 470. Every LED gets a resistor of a few hundred ohms.

Hold a light that must be protected in mind and try this part's questions: LEDs and the resistor.

## Subtopic: Long Leg to Plus, Resistor in Line

PAT indicator: battery, sensor switch, resistor, LED in a loop, long leg toward positive. Pick a high-brightness red LED for daylight, or a flashing one to catch the eye and save battery.

Two states, two LEDs: green full, red low, each with its own resistor, side by side across the battery. Never share one resistor between parallel LEDs.

Handle it: find the long leg and the flat spot, never test without a resistor, bend legs with pliers, check polarity on paper first. A reversed LED just sits dark.

Pocket summary of the lesson. A diode conducts only when its anode is toward positive and blocks when reversed; its symbol is a triangle pointing at a bar and the bar matches the band on the part. An LED is a diode that emits light when conducting, drops about 2 volts and has almost no resistance, so it must have a series resistor of a few hundred ohms to hold its current to a safe 10 to 20 milliamperes. In the PAT, a high-brightness LED with its resistor, correctly polarised, is the indicator, and each LED has its own resistor.

Hold long leg to plus, resistor in line, and take the final questions of the lesson: LEDs in the PAT.
