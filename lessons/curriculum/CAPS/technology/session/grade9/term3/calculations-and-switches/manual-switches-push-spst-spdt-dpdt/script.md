# Part 1 — Expert

This session covers manual switches: push, single-pole single-throw, single-pole double-throw and double-pole double-throw. The anchor is the switch drawer in a Technology room in East London, with doorbell push buttons, light-switch toggles, a three-way changeover from a bedside lamp and a chunky slide switch from a toy car that reverses its motor, each one opened to show the contacts moving. The governing idea is that a switch is described by its poles, the number of separate circuits it controls, and its throws, the number of positions each pole can connect to, so that SPST breaks one path, SPDT routes one path to either of two, and DPDT does so for two paths and can reverse a motor's polarity. Identifying switch types by symbol and function, choosing the correct switch for a purpose and drawing them in circuits are examinable.

## Subtopic: What a Switch Is: Poles, Throws and Contacts

A switch is a mechanical device that joins or separates metal contacts to complete or break a circuit. It carries no logic of its own; it is the designer's arrangement of switches that gives AND and OR. Every switch is described by two numbers. Poles are the number of separate circuits the switch controls at once: a single-pole switch has one moving contact, a double-pole switch has two that move together. Throws are the number of positions each pole can be connected to: a single-throw switch connects or disconnects one path, a double-throw switch connects its pole to either of two paths.

Switches are also described by their action. A toggle or slide switch stays where it is put, called latching. A push switch returns when released, called momentary, and comes in two kinds: push-to-make, which closes the circuit while pressed, used for doorbells and test buttons; and push-to-break, which opens the circuit while pressed, used for the fridge light that goes off when the door closes on the button. Rotary switches turn to several positions; key switches need a key; microswitches are tiny snap-action switches worked by a lever, found inside appliances to detect a lid or a door.

Switch ratings matter even in low-voltage circuits. A switch is rated for a maximum current and voltage; a small slide switch from the kit handles perhaps half an ampere at 12 volts, ample for an LED and a buzzer, but a motor drawing 2 amperes needs a larger switch or its contacts will heat and burn. The symbol for a switch is a gap in the line with a hinged bar, drawn in the open position, with the poles and throws shown by extra contacts and a dotted line linking poles that move together.

The questions for this section are with you now: poles and throws, latching and momentary actions, and ratings and the symbol.

## Subtopic: Push Switches and the SPST Toggle

The push-to-make switch is the simplest: two contacts and a spring, closed only while the button is held. Its symbol is a gap with a bar above it pushed down by an arrow or a short stem. It is used wherever a brief action is wanted: a doorbell, a keyboard key, a calculator button, the test button on the PAT indicator, the horn of a car. In the PAT it sits in parallel with the sensor so that pressing it lights the LED regardless of the tank, proving the battery and LED are alive, and releases to let the sensor take over.

The single-pole single-throw toggle, SPST, is the ordinary on-off switch: one pole, one throw, two terminals, latching. Its symbol is the plain gap and bar. The light switch on a wall, the power switch on a radio, the slide switch on a torch, and the silence switch on the PAT buzzer branch are all SPST. In the PAT it sits in series with the buzzer so that opening it silences the buzzer while the LED, on its own parallel branch, carries on. SPST is the switch for a plain on-off job and should be chosen whenever nothing more is needed, because it is the cheapest and simplest.

Drawing the PAT control section: battery positive to a junction; one path through the reed switch, another through the push-to-make test button, rejoining at a second junction; from there one branch through the resistor and LED to negative, and a second branch through the SPST silence switch and the buzzer to negative. Four switches of two types in one small circuit, each with a stated purpose, is the kind of design an examiner likes to see explained.

The questions for this section are with you now: the push-to-make switch and its uses, the SPST toggle and the silence switch, and drawing the PAT control section.

## Subtopic: SPDT and DPDT Switches: Changeover and Reversing

The single-pole double-throw switch, SPDT, has one pole and two throws: three terminals, a common and two others, and the common is connected to one or the other depending on the position. It is a changeover switch. Its symbol is a bar hinged at the common that can rest on either of two contacts. Uses: selecting between two lamps from one supply, a bedside switch that chooses the main lamp or the night light, a two-speed fan motor choosing between two windings, and in the PAT a possible choice between a steady LED and a flashing LED. Some SPDT switches have a centre-off position, which gives on-off-on in one switch.

The double-pole double-throw switch, DPDT, is two SPDT switches moved by one lever, with six terminals and a dotted line in the symbol joining the two bars. Each pole changes over independently of the other electrically but together mechanically. The famous use is reversing a motor: wire the two poles so that in one position the motor's terminals see positive and negative one way round, and in the other position the other way round, with the supply wires crossed between the two sets of contacts. Flick the switch and the motor reverses, which is how a toy car goes backwards and how a window winder or a small gate motor changes direction.

Choosing a switch for a purpose is a design question with a clear method: how many circuits must be controlled at once, that is the poles; how many positions must each be routed to, that is the throws; should it stay or return, latching or momentary; and what current must it carry. A doorbell is one circuit, one position, momentary: push-to-make. A buzzer silence is one circuit, on or off, latching: SPST. A choice of two indicators is one circuit, two positions, latching: SPDT. A motor reverse is two circuits, two positions, latching: DPDT. The error museum, four exhibits. One: using an SPDT where an SPST would do, adding cost and a dangling terminal. Two: trying to reverse a motor with an SPST. Three: drawing the switch closed on the diagram. Four: using a tiny slide switch for a motor current it cannot carry.

The questions for this section are with you now: the SPDT changeover and its uses, the DPDT and motor reversal, and choosing a switch by poles, throws, action and rating.

# Part 2 — Simplifier

Now the same lesson again with the switch drawer in East London, each switch opened to show its contacts — plain words, same facts.

## Subtopic: Metal That Touches or Does Not

A switch is metal contacts that touch or do not. Poles: how many circuits it controls at once. Throws: how many positions each pole can connect to.

Latching stays where you put it. Momentary springs back. Push-to-make closes while pressed; push-to-break opens while pressed, like the fridge light button.

Switches have ratings. A little slide switch is fine for LEDs and buzzers, not for a 2 amp motor. Symbol: a gap and a bar, drawn open.

Keep metal that touches or does not in mind and try the questions for this part: poles, throws and actions.

## Subtopic: One Way to Break a Loop

Push-to-make: two contacts and a spring. Doorbell, keyboard key, horn. In the PAT, the test button in parallel with the sensor: press it, the LED lights, let go, the sensor is back in charge.

SPST: one pole, one throw, plain on-off, two terminals. Wall light switch, torch slide. In the PAT, the silence switch in series with the buzzer. Use SPST whenever on-off is all you need.

Draw the PAT: plus to a junction, reed switch and test button side by side, join up, then two branches: resistor and LED; silence switch and buzzer. Back to minus.

Hold one way to break a loop in mind and try this part's questions: push and SPST.

## Subtopic: Choose Between Two, or Flip Everything

SPDT: one pole, two throws, three terminals. The common goes to one or the other. Changeover: main lamp or night light, two fan speeds, steady LED or flashing LED. Some have a centre-off.

DPDT: two SPDTs on one lever, six terminals, dotted line in the symbol. Cross the wires between the two sides and it reverses a motor. Toy car, window winder, gate motor.

Choose: how many circuits, how many positions, stay or spring back, how much current. Doorbell: push-to-make. Silence: SPST. Two indicators: SPDT. Reverse a motor: DPDT.

Pocket summary of the lesson. A switch is described by poles, the circuits it controls, and throws, the positions each pole can take, and by whether it latches or springs back. Push-to-make switches give a momentary contact for test buttons and doorbells; SPST gives plain on-off for silence switches and lights; SPDT changes one circuit over between two paths; DPDT does so for two circuits and reverses a motor when wired with crossed connections. Choose by poles, throws, action and current rating, and draw every switch open.

Hold choose between two, or flip everything, and take the final questions of the lesson: SPDT, DPDT and choosing.
