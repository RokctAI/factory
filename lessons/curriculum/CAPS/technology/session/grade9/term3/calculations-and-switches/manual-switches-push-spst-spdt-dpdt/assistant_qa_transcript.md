### subtopic_1 — What a Switch Is: Poles, Throws and Contacts
**Assistant:** Why does reversing a motor need a DPDT and not just an SPDT?

**Tutor:** Because reversing means swapping both of the motor's connections at once, and an SPDT can only re-route one wire. A motor turns one way when its terminal A is positive and B is negative, and the other way when A is negative and B is positive. To change from one to the other you must move terminal A from positive to negative and, at the same moment, terminal B from negative to positive; that is two wires, each going to one of two places, which is two poles and two throws. The DPDT does it with one lever: each pole is a motor terminal, each pair of throws is a positive and a negative, and the trick is wiring the supply to the two sets of throws crossed over, so that flipping the switch swaps which supply rail each terminal sees. With an SPDT you could switch terminal A between positive and negative, but terminal B would stay where it was, and in one position the motor would see positive on both terminals and simply stop.

***

### subtopic_2 — Push Switches and the SPST Toggle
**Assistant:** The test button and the reed switch are both just switches. Why does one have to be a push switch?

**Tutor:** Because of what each one is for and who closes it. The reed switch is closed by the magnet on the float when the water drops, and it must stay closed as long as the tank is low, without anyone holding it; it is the sensor, and it latches by the position of the float, not by a mechanism. The test button is for a person to check that the battery and LED work, and it must not stay on after the check, because a test button left on would light the LED permanently and the grandmother would think the tank was always low. A momentary push-to-make does exactly this: contact while pressed, open when released, so the LED lights for the second of the test and then goes back to telling the truth about the tank. A latching SPST as a test switch would be a design fault that the comparison table should catch under the specification that the warning must mean the tank is low.

***

### subtopic_3 — SPDT and DPDT Switches: Changeover and Reversing
**Assistant:** How can I tell which type a switch is just by looking at it?

**Tutor:** Count the terminals and try the action. Two terminals means one pole and one throw: SPST if it stays, push-to-make or push-to-break if it springs back; a push-to-break is rarer and usually marked. Three terminals in a row means SPDT: the middle one is nearly always the common and the outer two are the throws, and a multimeter on the continuity setting confirms which pair is joined in each position. Six terminals in two rows of three means DPDT: each row is one SPDT with its common in the middle, and the dotted line in the symbol is the mechanical link between them. Four terminals in two rows of two is a DPST, two on-off switches on one lever, used where both wires of a supply must be broken for safety. Reading the switch like this before wiring it saves the usual twenty minutes of wondering why the motor only stops and never reverses.
