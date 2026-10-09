### subtopic_1 — The npn Transistor: Three Legs and a Tiny Current That Controls a Large One
**Assistant:** Why do we need the transistor at all if the reed switch could light the LED directly in the final PAT design?

**Tutor:** The reed switch could, because it is a real metal contact that can carry the LED's few milliamperes with nothing lost. Most sensors are not like that. A light-dependent resistor does not switch; its resistance slides from a few hundred ohms in sunlight to a megohm in darkness, and the current it lets through at any point is far too small and too gradual to light an LED on its own. A pair of moisture probes passes a few microamperes through damp soil, a thermistor changes its resistance gently with temperature, a touch plate conducts a trickle through skin. None of these can do work; all of them can supply the base of a transistor with the fraction of a milliampere it needs. So the transistor is the bridge between a sensor that can only signal and a load that needs current. The Rustenburg team avoided it because their sensor happened to be a switch; the teams with night lights and moisture alarms cannot.

***

### subtopic_2 — The Transistor as a Switch Driven by a Sensor
**Assistant:** What does the base resistor actually do, and why does the value not seem to matter much?

**Tutor:** It limits the base current to a safe and sufficient amount, and the reason the value is forgiving is that the transistor only needs a little and tolerates a fair range. The base-emitter junction behaves like a diode: once it reaches about 0.6 volts it conducts, and without a resistor it would take as much current as the supply could push and burn out, exactly like an LED without its resistor. With a 4.5 volt supply and 0.6 volts across the junction, the resistor has about 3.9 volts across it; 10 kilohms gives 0.39 milliamperes, 100 kilohms gives 0.039. With a gain of 100, those allow collector currents up to 39 or 3.9 milliamperes before the transistor saturates, and since the LED only wants about 5 milliamperes, either works, with the smaller resistor giving a harder, more certain switch-on. The value matters when the load is bigger or the sensor is weaker, and the method is always Ohm's law: supply minus 0.6, over the base current you need.

***

### subtopic_3 — The Transistor as an Amplifier and Practical Precautions
**Assistant:** Is the transistor really amplifying energy? Where does the extra come from?

**Tutor:** No, and this is a point worth being clear on for the examination. The transistor does not create energy; it controls energy that the battery supplies. The small base current is the control, like the hand on a tap; the large collector current is water from the mains, not from the hand. In the switch circuit the battery pushes the LED current through the collector and emitter, and the transistor merely allows or forbids it. In the amplifier, the battery supplies all the power that drives the loudspeaker, and the transistor shapes that power into a copy of the microphone's tiny signal, enlarged. A transistor with no supply amplifies nothing, which is why every radio needs a battery however weak the station. The word amplifier describes what happens to the signal's size and shape, not a free gift of energy, and the law that work in equals work out, met in the mechanical terms, is not broken.
