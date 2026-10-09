# Part 1 — Expert

This session covers capacitors, which store and release electrical energy. The anchor is a bench in East London where a 1000 microfarad capacitor is charged for a few seconds from a 4.5 volt battery, disconnected, and then touched across an LED with its resistor, the LED flaring and fading over a second as the stored charge drains away. The governing idea is that a capacitor is two conductors separated by an insulator which store charge and energy when a voltage is applied, that the amount stored for a given voltage is its capacitance in farads, that charging and discharging through a resistor take a time set by resistance times capacitance, and that electrolytic capacitors are polarised and must be connected the right way round. Describing the capacitor's storage and release, its symbol and units, polarity and a simple timing use are examinable.

## Subtopic: What a Capacitor Is and How It Stores Charge

A capacitor is two metal plates, often long foils rolled into a cylinder, separated by a thin insulating layer called the dielectric. When the plates are connected across a battery, the battery pushes electrons onto one plate and pulls them off the other, so one plate becomes negative and the other positive, with the insulator stopping the charge crossing. Charge builds until the voltage between the plates equals the battery's voltage; then no more current flows. The capacitor is charged and holds energy in the electric field between its plates. Disconnect the battery and the charge stays, for seconds to minutes depending on leakage.

The amount of charge a capacitor stores for each volt across it is its capacitance, measured in farads. A farad is enormous, so practical capacitors are measured in microfarads, millionths of a farad, written with the Greek letter mu or a u, in nanofarads, thousand-millionths, and in picofarads, million-millionths. The kit's electrolytic capacitors run from 1 to 1000 microfarads; its ceramic discs from a few picofarads to a few hundred nanofarads. The symbol is two parallel lines with a gap between them, the leads leaving the outer sides; a polarised capacitor has one line curved or a plus sign beside the positive plate.

A capacitor is not a battery, though it is sometimes compared to one. A battery makes energy chemically and delivers it steadily for hours; a capacitor only holds energy that was put in, delivers it quickly, and holds far less: a 1000 microfarad capacitor at 4.5 volts stores about a hundredth of a joule, enough to flash an LED for a second, while an AA cell holds thousands of joules. The capacitor's strength is speed and repeatability: it can charge and discharge millions of times without wearing out.

The questions for this section are with you now: how a capacitor charges and stores energy, capacitance and its units and symbol, and how a capacitor differs from a battery.

## Subtopic: Charging, Discharging and the Time It Takes

Charging through a resistor takes time, and the time is set by the resistor and the capacitor together. Connect a battery, a resistor and a capacitor in series: at the first instant the capacitor is empty and the full battery voltage is across the resistor, so the current is large; as charge builds on the plates the capacitor's voltage rises, less voltage is left for the resistor and the current falls; the charging slows and slows, approaching the battery voltage without quite reaching it. A useful rule is that the capacitor reaches about two thirds of the battery voltage after a time equal to resistance times capacitance, and is nearly full after about five times that.

Resistance times capacitance, with resistance in ohms and capacitance in farads, gives a time in seconds. A 10 kilohm resistor and a 100 microfarad capacitor give 10 000 times 0.0001, which is 1 second; the capacitor is nearly full in about 5 seconds. A 100 kilohm resistor and a 1000 microfarad capacitor give 100 seconds, nearly full in about eight minutes. Doubling either the resistor or the capacitor doubles the time. This product is the basis of every simple electronic timer, from the delay on a bathroom light to the blink of a flashing LED.

Discharging is the reverse: connect the charged capacitor across a resistor or an LED and the current starts large and falls as the voltage drops, with the same time rule. The LED demonstration shows it: a 1000 microfarad capacitor through 470 ohms has a time of about half a second, so the LED flares and is nearly dark within a couple of seconds, which matches what is seen. In a transistor circuit the slowly rising or falling voltage on a capacitor can be used to turn the transistor on or off after a delay, which is the timing circuit built in a later session.

The questions for this section are with you now: why charging slows as the capacitor fills, the resistance times capacitance time rule with an example, and discharging and the LED demonstration.

## Subtopic: Capacitor Types, Polarity and Uses in Simple Circuits

Two families of capacitor appear in the kit. Ceramic and film capacitors are small discs or blocks, non-polarised, with values from picofarads to a few microfarads, marked with a code such as 104 for 100 000 picofarads, which is 100 nanofarads; they can be connected either way round and are used for smoothing and for small timing. Electrolytic capacitors are the aluminium cans with a stripe down one side; they give large values, 1 to thousands of microfarads, in a small size, but they are polarised: the stripe marks the negative lead, which is also the shorter one, and they must be connected with that lead toward the negative side of the circuit. Reversed or over-voltaged, an electrolytic heats, swells and can burst with a pop and a smell, which is why the rated voltage printed on the can, 16 volts or 25 volts in the kit, must be above the circuit's voltage.

Uses in simple circuits. Smoothing: in a charger, a large capacitor after the diodes fills in the gaps between the rectified pulses so that the output is steady. Timing: a capacitor charging through a resistor delays a transistor switching, giving a light that stays on for a set time after a button is released. Storing a burst of energy: a camera flash charges a capacitor slowly and releases it instantly through the flash tube. Blocking steady voltage while passing changing signals in audio circuits. For the PAT, a capacitor could hold the LED on for a moment after a brief sensor contact, or form part of a flashing circuit.

Handling: check the stripe and the plus marking before inserting, match the rated voltage to the supply with margin, discharge a large capacitor through a resistor before handling it, since a charged 1000 microfarad capacitor gives a sharp spark across a screwdriver, and never connect one straight across a battery with no resistor for long, which pulls a large current at the first instant. The error museum, four exhibits. One: an electrolytic connected backwards. Two: a 16 volt capacitor on a 24 volt supply. Three: expecting a capacitor to run a lamp for minutes like a battery. Four: reading 104 on a ceramic as 104 microfarads instead of 100 nanofarads.

The questions for this section are with you now: ceramic versus electrolytic and the polarity rule, uses in smoothing, timing and energy bursts, and safe handling.

# Part 2 — Simplifier

Now the same lesson again with the big capacitor charged from a battery and flaring an LED in East London — plain words, same facts.

## Subtopic: Two Plates and a Gap

Two metal plates with an insulator between. Connect a battery: one plate goes negative, the other positive, charge builds until the capacitor's volts match the battery's. Disconnect and it holds the charge.

Capacitance is how much charge per volt, in farads. A farad is huge, so we use microfarads, nanofarads, picofarads. Symbol: two parallel lines with a gap; a curve or a plus marks the positive side on big ones.

Not a battery. A battery makes energy for hours; a capacitor holds a little and gives it back fast, millions of times over.

Keep two plates and a gap in mind and try the questions for this part: what a capacitor is.

## Subtopic: Fill It Up, Let It Out

Charge through a resistor and it fills fast at first, then slower as its volts rise and the resistor gets less. Two thirds full after resistance times capacitance; nearly full after five of those.

Ohms times farads is seconds. 10 kilohms and 100 microfarads: 1 second. 100 kilohms and 1000 microfarads: 100 seconds. Double either, double the time. That is a timer.

Discharge is the reverse: fast then slow. 1000 microfarads through 470 ohms: half a second, LED flares and fades. A slowly rising voltage can switch a transistor after a delay.

Hold fill it up, let it out in mind and try this part's questions: charging and timing.

## Subtopic: Big Ones Have a Plus and a Minus

Small ceramic discs: either way round, tiny values, codes like 104 meaning 100 nanofarads. Big electrolytic cans: large values, a stripe on the minus lead, the shorter leg. Wrong way round or too many volts and they swell and pop. Rated volts on the can must beat the supply.

Uses: smoothing after diodes in a charger, timing a transistor, storing a burst for a camera flash. In the PAT, holding the LED on a moment longer or helping it flash.

Handle: check the stripe, check the volts, drain a big one through a resistor before touching, do not hold it straight across a battery.

Pocket summary of the lesson. A capacitor is two plates and an insulator that store charge and energy when a voltage is applied and release it when connected to a load; its capacitance is in farads, used in micro, nano and pico fractions. Charging or discharging through a resistor takes a time set by resistance times capacitance, which makes timers. Ceramic capacitors are small and unpolarised; electrolytics are large and polarised, with a stripe on the negative lead and a voltage rating that must exceed the supply.

Hold big ones have a plus and a minus, and take the final questions of the lesson: types, uses and handling.
