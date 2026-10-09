# Part 1 — Expert

This session covers the AND and OR logic gates and where they are used. The anchor is a microwave oven in a Pietermaritzburg kitchen: it heats only when the door is closed AND the start button is pressed, and it stops if the door opens OR the timer ends, which is two gates making a kitchen safe without anyone thinking about them.

## Subtopic: Logic: Inputs, Outputs and the Idea of a Gate

Logic in electronics is the handling of signals that have only two states. A switch is open or closed; a lamp is off or on; a sensor reports no or yes; a wire is at low voltage or high voltage. We call the two states 0 and 1, or low and high, or false and true, or off and on, and all four pairs mean the same thing. A logic gate is a device with one or more inputs and one output, each of which is either 0 or 1, and a rule that fixes the output for every possible combination of inputs. The gate does not think; it simply obeys its rule, instantly and every time, which is exactly what makes it trustworthy enough to run a microwave, a lift, a car or a computer.

In this term, gates are built from switches and a lamp, because a switch is a perfect two-state input and a lamp a perfect two-state output; in real equipment gates are made from transistors on a chip, millions of them, but the rules are identical. A single switch and a lamp is already a kind of gate, the simplest: output equals input. The interesting gates appear when there are two or more inputs and the output depends on how they combine. The two we study are AND and OR, and a third, NOT, which turns a 1 into a 0, waits for Grade 9.

Why does this matter beyond the classroom? Because every control decision is built from these pieces. A safety interlock that requires two conditions before a machine runs is an AND. An alarm that triggers on any of several sensors is an OR. A traffic light's controller, a washing machine's programme, a bank card reader's checks, are stacks of ANDs and ORs. When you can see the gate in a machine, you can design a machine that behaves safely, and that is the design skill the panic button project will test.

The questions for this section are with you now: what two-state signals are, what a logic gate is, and why gates matter for control.

## Subtopic: The AND Gate: Both Switches, One Lamp

The AND gate: its output is 1 only when every input is 1. With two inputs, A and B, the output is on only when A is on and B is on; if either is off, or both, the output is off. Build it with two switches in series with a lamp and a cell: the current can reach the lamp only if the first switch is closed and the second is closed, since they lie on the same single path; open either and the path is broken. Series switches are an AND gate. Test it on the bench: both open, dark; A closed only, dark; B closed only, dark; both closed, light. Four combinations, one lit.

The symbol is a D shape, flat on the input side with two lines entering, rounded on the output side with one line leaving. The rule in words: "The output is on when A AND B are on." The everyday uses are safety interlocks and double conditions. The microwave heats when the door is closed AND start is pressed. A car's engine starts when the key is turned AND, in a manual, the clutch is pressed, or in an automatic the gear lever is in park. A lift moves when the doors are closed AND a floor button has been pressed. A bank ATM pays out when the card is valid AND the PIN is correct. A paper guillotine in a print shop cuts when both hands are on two separate buttons, so that no hand can be under the blade. Industrial presses, lawnmowers that need a lever held and a cord pulled, and two-key missile launches in films are all the same gate.

The design logic is that AND demands more before it acts, which makes it the gate for anything dangerous or costly, because the extra condition is a guard. The weakness is the same thing: if one input fails off, a stuck door switch or a broken sensor, the whole system refuses to work, which is annoying but safe, the failure mode engineers prefer for machines that can hurt.

The questions for this section are with you now: the AND rule, the series-switch circuit and its four test results, the symbol, and where AND is used.

## Subtopic: The OR Gate: Either Switch, One Lamp, and Where Each Is Used

The OR gate: its output is 1 when any input is 1, and 0 only when all inputs are 0. With two inputs, the output is on if A is on, or B is on, or both are on; it is off only when both are off. Build it with two switches in parallel, side by side, feeding a lamp: the current has two possible paths, and if either switch is closed the lamp lights; both must be open to darken it. Parallel switches are an OR gate. Test it: both open, dark; A only, light; B only, light; both, light. Four combinations, three lit.

The symbol is a curved shape, like a shield or an arrowhead, with a concave input side where two lines enter and a pointed output side with one line leaving. The rule in words: "The output is on when A OR B is on." Note that "or" here includes both, which is sometimes called inclusive OR; the everyday sense of "either but not both" is a different gate.

Uses: alarms and multiple triggers. A burglar alarm sounds if the front door opens OR a window opens OR a movement sensor fires. A car's interior light comes on if the driver's door OR a passenger door opens. A fire alarm sounds if any smoke detector in the building triggers. The microwave stops if the door opens OR the timer reaches zero. A hospital nurse is called if any patient on the ward presses a button. And the panic button you will design next week is an OR at heart: the alarm must sound if the button in the bedroom OR the button in the kitchen OR the one by the gate is pressed. The design logic is that OR acts on the first sign of trouble, which makes it the gate for alarms and warnings; its weakness is false alarms, since any one faulty sensor can trigger the whole system.

Side by side: AND is series switches, demands everything, guards actions; OR is parallel switches, accepts anything, raises alarms. Real systems combine them: the microwave runs when door closed AND start pressed, and stops when door open OR timer done. Being able to say which gate a situation needs is the whole skill.

The error museum, four exhibits. One: switches in parallel called an AND gate, or series called OR. Two: OR described as "one or the other but not both". Three: the AND symbol drawn with the flat side at the output. Four: an alarm designed with AND, so that two doors must open before it sounds.

The questions for this section are with you now: the OR rule, the parallel-switch circuit and its test results, the symbol, where OR is used, and how AND and OR compare.

# Part 2 — Simplifier

Now the same lesson again with a microwave that heats only with the door shut and start pressed — plain words, same facts.

## Subtopic: Yes and No

Logic means signals with only two states. A switch is open or closed, a lamp off or on, a sensor no or yes, a wire low or high. Call them 0 and 1, or off and on, or false and true; same thing. A logic gate has inputs and one output, each 0 or 1, and a rule that fixes the output for every mix of inputs. It does not think; it obeys, instantly, every time, which is why you can trust it with a microwave, a lift or a computer.

This term we build gates from switches and a lamp: a switch is a perfect two-state input, a lamp a perfect two-state output. Real gates are transistors on a chip, millions of them, same rules. One switch and a lamp is the simplest gate: output equals input. Things get interesting with two inputs, when the output depends on how they combine. Our two are AND and OR; NOT, which flips 1 to 0, comes next year.

Why care? Every control decision is built from these. A machine that needs two conditions before it runs: AND. An alarm that fires on any of several sensors: OR. Traffic lights, washing machine programmes, bank card checks: stacks of ANDs and ORs. See the gate in a machine and you can design a safe one, which is what the panic button project asks.

Hold the 0 and the 1 in mind and try the questions for this part: yes and no.

## Subtopic: Both, or Nothing

AND: output is 1 only when every input is 1. Two inputs, A and B: on only when A is on and B is on; either off, output off. Build it: two switches in series with a lamp and a cell. Current reaches the lamp only if the first switch is closed and the second is closed, same single path; open either, path broken. Series switches are AND. Test: both open, dark; A only, dark; B only, dark; both, light. Four combinations, one lit.

Symbol: a D, flat on the input side with two lines in, round on the output side with one line out. Words: "on when A AND B are on." Uses: safety and double conditions. Microwave heats when door closed AND start pressed. Car starts when key turned AND clutch pressed, or lever in park. Lift moves when doors closed AND a floor pressed. ATM pays when card valid AND PIN right. Print-shop guillotine cuts when both hands press two separate buttons, so no hand is under the blade. Presses, mowers with a lever and a cord, two-key launches in films: all AND.

AND asks for more before it acts, so it guards anything dangerous or costly. Its weak point is the same: one input stuck off, a broken door switch, and nothing works, annoying but safe, which is the failure engineers want for machines that can hurt.

Hold the two switches in a row in mind and try the questions for this part: both, or nothing.

## Subtopic: Either Will Do

OR: output is 1 when any input is 1, and 0 only when all are 0. Two inputs: on if A, or B, or both; off only when both are off. Build it: two switches in parallel, side by side, feeding a lamp. Two paths; close either and the lamp lights; both must be open to darken it. Parallel switches are OR. Test: both open, dark; A only, light; B only, light; both, light. Four combinations, three lit.

Symbol: a curved shield or arrowhead, hollow input side with two lines in, pointed output with one line out. Words: "on when A OR B is on." This "or" includes both; "one but not both" is a different gate.

Uses: alarms and many triggers. Burglar alarm: front door OR window OR movement sensor. Car interior light: driver's door OR passenger door. Fire alarm: any smoke detector. Microwave stops: door open OR timer done. Nurse call: any patient's button. And your panic button: bedroom button OR kitchen button OR gate button. OR acts on the first sign of trouble, so it is the alarm gate; its weak point is false alarms, since one faulty sensor fires everything.

Side by side: AND is series, wants everything, guards actions. OR is parallel, takes anything, raises alarms. Real machines mix them: microwave runs on door closed AND start, stops on door open OR timer. Knowing which gate a situation needs is the skill.

Pocket summary of the lesson. Two states, 0 and 1. A gate obeys a rule for every input mix. AND: series switches, output only when all inputs on, D symbol, interlocks. OR: parallel switches, output when any input on, shield symbol, alarms. Say which one the job needs.

Hold the two switches side by side in mind, and take the final questions of the lesson: either will do.
