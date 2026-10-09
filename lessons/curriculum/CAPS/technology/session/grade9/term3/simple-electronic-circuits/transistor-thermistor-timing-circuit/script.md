# Part 1 — Expert

This session covers a transistor circuit with a thermistor, variable resistor, LED, capacitor and switch. The anchor is a breadboard in Welkom beside a mug of warm water and a damp cloth, the LED coming on a second or two after the thermistor is dipped in the water and going off a second or two after it is wrapped in the cloth, the variable resistor turned until the switch-on happens at the temperature the learner wants. The governing idea is that a divider of thermistor and variable resistor produces a base voltage that crosses the transistor's 0.6 volt threshold at a chosen temperature, that the transistor switches the LED, that a capacitor across the base slows the base voltage's changes to prevent flicker and adds a short delay, and that the same circuit senses light or moisture if the thermistor is replaced. Drawing, explaining, building and adapting this circuit are examinable and represent the full electronic content of the PAT.

## Subtopic: The Circuit: Thermistor, Variable Resistor, Transistor, LED, Capacitor and Switch

The circuit is drawn with the 4.5 volt battery on the left, positive at the top, and an SPST switch in the positive lead so that everything after it is dead when the switch is open. From the switched positive, two paths. The sensing divider: an NTC thermistor, drawn as a resistor with a slash and a minus t, from positive to a junction, and a variable resistor, a rectangle with an arrow, from the junction to negative; the variable resistor is 10 kilohms or 100 kilohms depending on the thermistor's room-temperature value. The load path: a 470 ohm resistor and the LED from positive to the transistor's collector, with the emitter to negative. The junction goes through a 10 kilohm base resistor to the base. A capacitor, 100 microfarads electrolytic, is connected from the base to negative, positive lead to the base.

Six component types, seven parts, every one labelled: 4.5 V, SPST, NTC thermistor with its room value such as 10 k, variable resistor 10 k, 10 k base resistor, 470 ohm LED resistor, red LED, BC547 with C B E marked, 100 microfarad capacitor with its plus. Drawn tidily the diagram reads left to right as sensing, deciding, showing, which is the input, process, output pattern of the whole term.

Each part has one job. The switch gives on and off. The thermistor senses temperature. The variable resistor sets the threshold. The base resistor protects the base. The transistor switches. The LED resistor protects the LED. The LED shows. The capacitor smooths and delays. A learner asked to explain the circuit lists the parts with their jobs before describing the action, because the examiner is checking that every component is understood, not just the overall effect.

The questions for this section are with you now: the layout of the circuit with every value, the seven parts and their labels, and one job per part.

## Subtopic: How It Works: Sensing Temperature and Setting the Threshold

The action follows the divider. The thermistor and the variable resistor share the 4.5 volts in proportion to their resistances, and the junction's voltage is what the base sees. At room temperature the NTC thermistor is about 10 kilohms; if the variable resistor is set to about 2 kilohms, the junction sits at 4.5 times 2 over 12, about 0.75 volts, just above the 0.6 the transistor needs, so the LED is on. Cool the thermistor with a damp cloth and its resistance rises to 20 kilohms; the junction falls to 4.5 times 2 over 22, about 0.4 volts; the transistor turns off; the LED goes out. Warm it in a mug and its resistance falls to 3 kilohms; the junction rises to 1.8 volts; the transistor is hard on. Warm enough, light on.

The variable resistor sets where the crossing happens. Turn it up to 5 kilohms and the junction at room temperature is 1.5 volts, so the LED is on until the thermistor is quite cold; turn it down to 500 ohms and the junction at room temperature is 0.2 volts, so the LED is off until the thermistor is quite warm. The user sets the alarm temperature by turning the knob until the LED just comes on at the temperature wanted, for instance in a bath of water at the temperature a baby's bottle should be. The arithmetic is Ohm's law and the voltage divider, and the examination may ask for the junction voltage at a given pair of resistances.

Swapping the thermistor and the variable resistor inverts the circuit: now the junction rises as the thermistor cools, and the LED comes on when it is cold, a frost warning for a seedling tray or a warning that a geyser has gone off. The same two arrangements, sensor on top for warm-on and sensor below for cold-on, apply to every divider sensor circuit, and knowing which is which is a quick way to read any sensor circuit in the examination.

The questions for this section are with you now: the divider voltage at room, cold and warm, setting the threshold with the variable resistor, and inverting for a cold warning.

## Subtopic: The Capacitor's Role, Building the Circuit and Adapting It

The capacitor from base to negative does two things. First, it smooths. As the thermistor hovers near the threshold temperature, the junction voltage wobbles above and below 0.6 volts and without the capacitor the LED would flicker on and off, which is confusing in an alarm. The capacitor holds the base voltage steady for a moment, charging and discharging through the resistors, so a brief wobble does not reach the base. Second, it delays. When the temperature changes sharply, the junction voltage changes quickly but the base voltage follows slowly, taking about resistance times capacitance to move: with 10 kilohms and 100 microfarads that is about a second, so the LED comes on a second or two after the thermistor warms and goes off a second or two after it cools. A larger capacitor gives a longer pause.

Building follows the breadboard method: rails, then components row by row to the diagram, with special care for the three polarised parts, the LED, the transistor and the electrolytic capacitor, and the check against the diagram before power. Testing: switch on at room temperature and note whether the LED is on; adjust the variable resistor until it is just off; warm the thermistor between fingers and watch the LED come on after a pause; wrap it in the damp cloth and watch it go off after a pause; try a larger capacitor and note the longer pause. Record each test. Fault-finding: no LED at any setting points to the LED or transistor polarity; LED always on points to the divider or a shorted thermistor; no delay points to the capacitor reversed or missing.

Adapting: replace the thermistor with an LDR and the circuit becomes a light alarm, warm-on becoming bright-on; replace it with two probes and it becomes a moisture alarm, on when wet; replace the LED and its resistor with a buzzer and the alarm sounds. The transistor's collector current rating allows a small buzzer or a relay coil, but a motor or a large lamp needs a bigger transistor. This one circuit, with its sensor and output swapped, is the electronics of almost every PAT device in the class. The error museum, four exhibits. One: electrolytic capacitor reversed, giving no delay and a warm capacitor. Two: thermistor and variable resistor swapped by accident, giving a cold alarm when a warm one was wanted. Three: variable resistor turned to zero so the junction is at negative and nothing ever switches. Four: explaining the circuit as a whole without naming each part's job.

The questions for this section are with you now: smoothing and delay from the capacitor, building and testing the circuit, and adapting it with other sensors and outputs.

# Part 2 — Simplifier

Now the same lesson again with the breadboard, the warm mug and the damp cloth in Welkom — plain words, same facts.

## Subtopic: Six Parts, One Job

Battery, 4.5 volts, with a switch in the plus lead. Then two paths. Sensing: thermistor from plus to a junction, variable resistor from the junction to minus. Load: 470 ohms and LED from plus to the collector, emitter to minus. Junction through 10 kilohms to the base. Capacitor, 100 microfarads, from base to minus, plus lead on the base.

Label everything: volts, switch type, thermistor value, variable resistor value, both resistors, LED colour, transistor type with C B E, capacitor with its plus.

One job each: switch on-off, thermistor senses, variable resistor sets, base resistor protects, transistor switches, LED resistor protects, LED shows, capacitor smooths and delays.

Keep six parts, one job in mind and try the questions for this part: the circuit and its parts.

## Subtopic: Warm Enough, Light On

The thermistor and the variable resistor share 4.5 volts. Room temperature, 10 kilohms against 2: junction about 0.75 volts, LED on. Cold cloth, 20 kilohms: junction about 0.4, LED off. Warm mug, 3 kilohms: junction 1.8, LED hard on. Warm enough, light on.

Turn the variable resistor up and the LED stays on until it is colder; turn it down and it stays off until it is warmer. Set the alarm temperature by turning the knob until the LED just comes on where you want.

Swap the thermistor and the variable resistor: LED on when cold. Frost warning. Sensor on top: warm-on. Sensor below: cold-on.

Hold warm enough, light on in mind and try this part's questions: the divider and the threshold.

## Subtopic: A Pause Before It Switches

The capacitor on the base stops flicker when the temperature hovers, and adds a pause: about a second with 10 kilohms and 100 microfarads. Bigger capacitor, longer pause.

Build it: rails, rows, three polarised parts checked, diagram check before power. Test: adjust to just off at room temperature, warm it, pause, on; cool it, pause, off; bigger capacitor, longer pause. No LED ever: LED or transistor backwards. Always on: divider. No pause: capacitor.

Adapt it: LDR instead of thermistor, a light alarm; probes instead, a moisture alarm; buzzer instead of LED, it sounds. This is the electronics of nearly every PAT device.

Pocket summary of the lesson. The circuit is a 4.5 volt battery and switch, a divider of NTC thermistor and variable resistor feeding a transistor base through a resistor, a 470 ohm resistor and LED in the collector circuit, and a 100 microfarad capacitor from base to negative. The divider voltage crosses 0.6 volts at a temperature set by the variable resistor, the transistor switches the LED, and the capacitor smooths flicker and adds a delay of about resistance times capacitance. Swapping the sensor's position inverts the action; swapping the sensor or the output adapts the circuit to light, moisture or sound.

Hold a pause before it switches, and take the final questions of the lesson: the capacitor, building and adapting.
