# Part 1 — Expert

This session covers switches in series as AND logic, switches in parallel as OR logic, and the convention that current flows from positive to negative. The anchor is a bakery in Kimberley with a dough mixer whose motor runs only when the lid is closed and the start button is held, and a delivery van whose interior light comes on when the driver's door or the sliding door opens. The governing idea is that the arrangement of switches in a circuit expresses a logical rule, series meaning all conditions must be met and parallel meaning any one is enough, that these rules are recorded in truth tables, and that conventional current is drawn leaving the positive terminal and returning to the negative so that every diagram is read the same way. Drawing and explaining AND and OR switch circuits, completing truth tables and applying the current convention are examinable.

## Subtopic: Switches in Series: AND Logic

Two switches in series with a lamp and a cell form a single loop with two gaps. Current can flow only when both gaps are closed; if either switch is open the loop is broken and the lamp is off. This is AND logic: the lamp is on when switch A is closed and switch B is closed. The truth table lists every combination: A open and B open, off; A open and B closed, off; A closed and B open, off; A closed and B closed, on. Only one of the four rows gives an output.

AND logic is the safety rule of machines. The bakery mixer has a lid switch that closes when the lid is down and a start button that closes when pressed, in series with the motor's control circuit, so the blades turn only when the lid is on and the button is pressed; lift the lid and the motor stops. A microwave oven runs only when the door is shut and the start button is pressed. A car starts only when the key is turned and, in many cars, the clutch or brake is pressed. Two conditions both required is always two switches in series.

In the PAT device, AND logic could make a buzzer sound only when the tank is low and a night-silence switch is in the on position, so the grandmother can disable the sound at bedtime by opening one switch while the LED, on its own branch, keeps working. Writing the rule in words first, buzzer sounds when low and enabled, and then drawing the switches in series, is the design method.

The questions for this section are with you now: the series switch circuit and its truth table, AND logic as the safety rule, and an AND use in the PAT device.

## Subtopic: Switches in Parallel: OR Logic

Two switches in parallel with each other, that pair in series with a lamp and a cell, give two routes through the switch section. If either switch is closed the current has a complete path and the lamp is on; only when both are open is the lamp off. This is OR logic: the lamp is on when switch A is closed or switch B is closed, or both. The truth table: both open, off; A closed only, on; B closed only, on; both closed, on. Three of the four rows give an output.

OR logic is the rule of convenience and of alarms. The van's interior light comes on when the driver's door switch or the sliding door switch closes. A house alarm sounds when any one of several door and window sensors is triggered. A staircase light has a switch at the top and at the bottom that, in simple form, are in parallel so that either turns it on. A burglar alarm with pressure mats under each window is a long parallel chain: any mat closes the circuit.

In the PAT device, OR logic lets the LED be lit by the level sensor or by a test button, so the grandmother can press the button to check that the battery and LED still work even when the tank is full. Sensor in parallel with the test button, that pair in series with the LED and its resistor and the battery. Again the rule is written in words, LED lights when low or testing, and then drawn.

The questions for this section are with you now: the parallel switch circuit and its truth table, OR logic in alarms and lights, and an OR use in the PAT device.

## Subtopic: Conventional Current From Positive to Negative and Reading Logic in Devices

Current direction is a convention. Long before electrons were known, scientists agreed to draw current flowing from the positive terminal of the supply, through the circuit, to the negative terminal. Later it was found that the moving charges in a metal wire are electrons travelling the other way, from negative to positive, but the convention was kept because it changes nothing about how circuits behave and every diagram, textbook and component marking in the world uses it. Conventional current flows from positive to negative; arrows on diagrams show this; and components that care about direction, the diode and the LED met next week, are drawn so that conventional current passes through them from the triangle's base to its point.

Reading logic in real devices is the skill the examination tests. Given a description, a machine that runs only when the guard is closed and the pedal is pressed, draw two switches in series. Given a light that comes on when either door opens, draw two switches in parallel. Given a combination, a buzzer that sounds when the tank is low and the silence switch is on, or when the test button is pressed, draw the level sensor and the silence switch in series, then that pair in parallel with the test button. The words all, both and only when signal AND; the words any, either and or signal OR.

Build the circuits with push switches on a board, complete the truth tables by testing, and check that the measured tables match the predicted ones. The error museum, four exhibits. One: putting switches in parallel for a safety interlock, so that pressing start alone runs the machine with the guard open. Two: drawing current arrows from negative to positive. Three: a truth table with the wrong number of rows; two switches always give four. Four: confusing switches in parallel, which is OR, with lamps in parallel, which is about brightness and independence.

The questions for this section are with you now: the current direction convention and why it is kept, reading AND and OR from descriptions, and testing truth tables.

# Part 2 — Simplifier

Now the same lesson again with the bakery mixer and the delivery van in Kimberley — plain words, same facts.

## Subtopic: Both Must Be On

Two switches in a row with a lamp. Both must be closed or the lamp is off. That is AND. Truth table: off, off, off, on. Only the last row lights.

Safety rule: the mixer runs only when the lid is down and the button is pressed. Microwave: door shut and start pressed. Two musts, two switches in series.

PAT use: buzzer only when the tank is low and the night switch is on. Flip the night switch and the buzzer is silent while the LED keeps working on its own branch.

Keep both must be on in mind and try the questions for this part: AND.

## Subtopic: Either Will Do

Two switches side by side, then the lamp. Either closed and the lamp is on. Only both open is off. That is OR. Truth table: off, on, on, on.

Convenience and alarms: van light on when either door opens, alarm when any sensor trips, stair light from top or bottom.

PAT use: LED lights when the tank is low or the test button is pressed, so she can check the battery any time.

Hold either will do in mind and try this part's questions: OR.

## Subtopic: Which Way the Arrows Point

Current is drawn from positive to negative. Electrons actually go the other way, but the agreed arrows never changed and everything is built on them. Diodes and LEDs are drawn for current going in at the triangle's base, out at the point.

Read the words. All, both, only when: series, AND. Any, either, or: parallel, OR. Mixed: sensor and night switch in series, that pair in parallel with the test button.

Build them, fill the truth tables by testing, compare with your predictions.

Pocket summary of the lesson. Switches in series give AND logic: the output works only when every switch is closed, which is the safety interlock rule. Switches in parallel give OR logic: the output works when any switch is closed, which is the alarm and convenience rule. Each pair of switches has a four-row truth table. Conventional current is drawn from the positive terminal to the negative, and direction-sensitive components are drawn to match.

Hold which way the arrows point, and take the final questions of the lesson: current direction and reading logic.
