# Part 1 — Expert

This session covers npn transistors as switches and amplifiers. The anchor is a bench in Mahikeng with a BC547 transistor in a breadboard, a 4.5 volt battery, an LED with its 470 ohm resistor from collector to positive, and a learner touching a 100 kilohm resistor from positive to the base and watching the LED light from a current far too small to light it directly. The governing idea is that an npn transistor passes a collector-to-emitter current only when a small current flows into its base, that the collector current can be a hundred times the base current, so the transistor acts as an electrically operated switch for sensors and as an amplifier for weak signals, and that the base must always have a resistor to limit its current. Drawing the npn symbol with its legs, explaining its switching action in a sensor circuit and describing it as an amplifier are examinable.

## Subtopic: The npn Transistor: Three Legs and a Tiny Current That Controls a Large One

The npn transistor is a small three-legged component, in the kit a black plastic body with a flat face, type BC547 or similar. Its legs are the emitter, the base and the collector; on the BC547 with the flat face toward you and the legs down, they run collector, base, emitter from left to right, but the data sheet or the kit card is always checked because other types differ. The symbol is a vertical bar for the base with two angled lines leaving it: the collector line plain, the emitter line with an arrow pointing outward, which is the npn marking, and a circle around it in older drawings.

The transistor's action is this: with no current flowing into the base, no current flows from collector to emitter and the transistor is off, like an open switch between those two legs. When a small current flows into the base and out of the emitter, a much larger current is allowed to flow from collector to emitter; the ratio is the current gain, typically 100 or more for a small transistor. One milliampere into the base can let 100 milliamperes through the collector, limited by whatever is in the collector circuit. The base current turns the transistor on; the collector circuit does the work.

The transistor is an npn type because of the layers of treated silicon inside it, n-type, p-type, n-type; the names matter only to remember that for an npn transistor, the base must be made more positive than the emitter, by about 0.6 volts, for it to turn on, and the collector is connected toward the positive supply through the load. The emitter goes to the negative supply. Current flows into the collector and the base, and out of the emitter, which the emitter arrow shows.

The questions for this section are with you now: the three legs and the symbol, the base current controlling the collector current, and the npn polarity.

## Subtopic: The Transistor as a Switch Driven by a Sensor

The transistor switch circuit is built like this. Battery positive to the load, an LED and its 470 ohm resistor, then to the collector. Emitter to battery negative. Base to a resistor, typically 10 to 100 kilohms, and the other end of that resistor to whatever will supply the small turn-on current. Touch the base resistor to positive and the LED lights; let go and it goes out. The base resistor is essential: the base is like an LED's junction and will be destroyed by too much current, and the resistor holds the base current to a fraction of a milliampere while the transistor passes several milliamperes through the LED.

Replace the touch with a sensor. A light-dependent resistor from positive to the base, with a resistor from base to negative, gives a base current that depends on light: in daylight the LDR's resistance is low, base current flows, the transistor is on; in darkness the LDR's resistance is high, base current stops, the transistor is off. Swap the LDR and the resistor and the behaviour inverts, giving a light that comes on in the dark, the night light of the PAT scenarios. Two moisture probes in soil, a thermistor, a touch plate across two contacts, each too weak to work an LED directly, all work the base the same way.

The transistor as a switch has two states and spends its time in one or the other: off, with no collector current, and fully on, called saturated, with the collector current limited only by the load. In between, when the base current is just enough to partly turn it on, the transistor is neither off nor on and gets warm, which is wasteful in a switch and is the region the amplifier uses. For the PAT, a sensor whose change is large, light to dark, wet to dry, takes the transistor cleanly from off to on, which is what a good switch should do.

The questions for this section are with you now: the transistor switch circuit with its base resistor, driving the base from a sensor and inverting the action, and off and saturated states.

## Subtopic: The Transistor as an Amplifier and Practical Precautions

As an amplifier the transistor works in the in-between region on purpose. A small, varying current into the base, from a microphone for example, produces a collector current that varies in the same pattern but a hundred times larger. The pattern is preserved and the size is increased, which is amplification. A radio's weak aerial signal, a microphone's whisper, a guitar pickup's tiny output, all pass through transistor amplifiers before they can drive a loudspeaker. The PAT does not need an amplifier, but the examination asks for the idea: a transistor amplifier makes a small signal larger without changing its shape.

The two uses are the same property seen two ways. As a switch, the base current is either nothing or plenty, and the collector current is either nothing or the maximum the load allows. As an amplifier, the base current is varied gently and the collector current follows it, enlarged. One component, two jobs, depending on how the base is driven.

Precautions keep the transistor alive. Identify the legs from the kit card before inserting; a reversed transistor does nothing or dies. Always use a base resistor. Keep the collector current within the transistor's rating, about 100 milliamperes for a BC547, so a motor or a large lamp needs a bigger transistor. Do not solder with the iron on the leg for more than a few seconds, since heat travels to the junction. Handle on a dry day with a touch to something earthed first, because static can damage small transistors. The error museum, four exhibits. One: no base resistor, so the base burns out. Two: legs in the wrong holes. Three: LED connected without its resistor, now in the collector circuit. Four: expecting a BC547 to drive a motor drawing an ampere.

The questions for this section are with you now: the transistor as an amplifier, the switch and amplifier as one property, and the precautions.

# Part 2 — Simplifier

Now the same lesson again with the BC547 in the breadboard and the LED that lights from a touch in Mahikeng — plain words, same facts.

## Subtopic: A Switch With No Moving Parts

Three legs: collector, base, emitter. Check the kit card for which is which. Symbol: a bar for the base, two slanted legs, the emitter with an arrow pointing out.

No base current: off, like an open switch between collector and emitter. A little base current: on, and a hundred times more current can flow collector to emitter. The trickle opens the tap.

npn: base about 0.6 volts above the emitter to turn on. Collector toward positive through the load. Emitter to negative.

Keep a switch with no moving parts in mind and try the questions for this part: what the transistor is.

## Subtopic: A Trickle Opens the Tap

Switch circuit: positive, LED and 470 ohms, collector. Emitter to negative. Base through 10 to 100 kilohms to whatever turns it on. Touch that resistor to positive, the LED lights. Never leave out the base resistor.

Sensor on the base: LDR from positive to base, resistor base to negative. Light: on. Dark: off. Swap them: dark: on. That is a night light. Probes, a thermistor, a touch plate all do the same.

Two states: off, and fully on. In between it gets warm. A sensor with a big change gives a clean switch.

Hold a trickle opens the tap in mind and try this part's questions: the switch.

## Subtopic: Small In, Big Out, Mind the Legs

Amplifier: a small wobbling base current makes a big wobbling collector current with the same shape. Radio, microphone, guitar. The PAT does not need one, but know the idea: bigger, same shape.

Same property, two uses. Switch: base nothing or plenty. Amplifier: base varied gently, collector follows, enlarged.

Keep it alive: check the legs, always a base resistor, under 100 milliamps collector current for a BC547, quick soldering, touch something earthed first.

Pocket summary of the lesson. An npn transistor has a collector, base and emitter; a small base current lets a much larger current flow from collector to emitter, so it is a switch with no moving parts. With the load in the collector circuit, the emitter to negative and a resistor in the base, a sensor such as an LDR, thermistor or probe pair turns it on and off, and swapping sensor and resistor inverts the action. The same property, small current controlling large, makes it an amplifier. Always use a base resistor and stay within its current rating.

Hold small in, big out, mind the legs, and take the final questions of the lesson: amplifier and precautions.
