# Part 1 — Expert

This session covers truth tables for the AND and OR gates. The anchor is a Grade 8 pair in Soweto with two switches, a lamp and a sheet ruled into a grid of four rows and three columns, ticking each row as the switches click, until the table on paper and the lamp on the bench agree in every case.

## Subtopic: What a Truth Table Is and How to Set One Up

A truth table is a complete list of what a logic circuit does. Its columns are the inputs, one each, followed by the output; its rows are every possible combination of input values, one combination per row, with the output that combination produces written at the end. For two inputs, A and B, each of which can be 0 or 1, there are four combinations, so the table has four rows: A is 0 and B is 0; A is 0 and B is 1; A is 1 and B is 0; A is 1 and B is 1. For three inputs there are eight rows, for four, sixteen; each extra input doubles the rows, since every existing combination now appears once with the new input at 0 and once at 1.

The order of rows matters for completeness, not for truth, and the convention is to count upwards in binary: 00, 01, 10, 11. Write the right-hand input column alternating 0, 1, 0, 1; write the left-hand column as 0, 0, 1, 1. For three inputs the rightmost column alternates every row, the middle every two rows, the leftmost every four. Set up this way, no combination can be left out and none repeated, and two people filling in tables for the same gate will produce identical sheets that can be compared line by line.

The value of the table is that it says everything and only what matters. A description in words, "the lamp lights when both switches are closed", is clear for AND but becomes slippery for larger circuits; a table has no ambiguity, every case is there, and it can be checked against a real circuit row by row. It is also a design document: a designer writes the table of what a system should do before deciding how to build it, and the builder tests the finished system against the table. In the panic button project, the truth table is the specification that the circuit must satisfy and that the examiner will mark.

The questions for this section are with you now: what the columns and rows of a truth table are, how many rows two and three inputs need, and how the binary ordering ensures completeness.

## Subtopic: The AND Truth Table, Tested on the Bench

Fill in the AND table. The output is 1 only when every input is 1, so go down the rows: A 0, B 0, output 0; A 0, B 1, output 0; A 1, B 0, output 0; A 1, B 1, output 1. A single 1 at the bottom and three 0s above it. The shape is the signature of AND: the output column is 0 everywhere except the row where every input is 1.

Now verify it on the bench, which is the half of the lesson that makes the table real. Build the series-switch circuit: cell, switch A, switch B, lamp, in one loop. Take the table's first row: both switches open, 0 and 0; look at the lamp; dark; the table says 0; tick. Second row: A open, B closed; dark; 0; tick. Third row: A closed, B open; dark; 0; tick. Fourth row: both closed; light; 1; tick. Four rows, four ticks, and the table is verified. If any row disagrees, the circuit is wrong or the table is wrong, and finding which is the whole of debugging. Switch B wired across the lamp instead of in series with it, for instance, gives a lamp that lights with A alone, and the third row fails; the table told you where to look.

Record the test honestly, with a column for "predicted" and a column for "observed", and tick or cross each row. An examiner awards marks for a table that matches the gate, for a circuit that matches the table, and for the testing that connects them; a learner who writes the correct table but never tests it has done half the work, and one who tests and finds a disagreement and fixes it has done the real work.

The questions for this section are with you now: the AND table row by row, its signature shape, and how it is verified against the series circuit.

## Subtopic: The OR Truth Table, Comparing the Two, and Reading a Table Back Into a Circuit

Fill in the OR table. The output is 1 when any input is 1, so: A 0, B 0, output 0; A 0, B 1, output 1; A 1, B 0, output 1; A 1, B 1, output 1. A single 0 at the top and three 1s below it. The signature of OR: the output column is 1 everywhere except the row where every input is 0. Verify it on the parallel-switch circuit the same way, row by row: both open, dark, tick; B only, light, tick; A only, light, tick; both, light, tick.

Put the two tables side by side. The input columns are identical, because the inputs are the same four combinations whatever the gate; only the output column differs. AND and OR agree on two rows, the first, where both inputs are 0 and both outputs are 0, and the last, where both inputs are 1 and both outputs are 1. They disagree on the two middle rows, where exactly one input is 1: AND says 0, OR says 1. That is the entire difference between the gates in two cells of a table, and it is why the mixed-input cases are the ones a tester must try; a tester who only tries both-off and both-on cannot tell AND from OR.

Now the reverse skill. Given a table with a single 1 at the bottom, name the gate: AND, and the circuit: switches in series. Given a table with a single 0 at the top: OR, switches in parallel. Given a description of a machine, write its table and then read off the gate: a car's interior light that comes on if either door opens has a 1 in every row but the first, so OR, so two door switches in parallel with the lamp. A lift that moves only when the doors are closed and a button is pressed has a 1 only in the last row, so AND, so two switches in series with the motor. For three inputs, an eight-row table with a single 1 in the final row is a three-input AND, three switches in series; a single 0 in the first row is a three-input OR, three switches in parallel.

The error museum, four exhibits. One: a table with three rows, a combination missed. Two: rows out of binary order, so that two tables cannot be compared. Three: the AND output column written as 0, 1, 1, 1, the OR pattern. Four: a table filled in correctly but never tested on the bench, so a miswired circuit goes unnoticed.

The questions for this section are with you now: the OR table and its signature, the two rows where AND and OR differ, and reading a table back into a gate and a circuit.

# Part 2 — Simplifier

Now the same lesson again with a sheet ruled into four rows and three columns and a lamp that must agree with every line — plain words, same facts.

## Subtopic: Every Case in a Grid

A truth table is the full list of what a logic circuit does. Columns: one per input, then the output. Rows: every possible mix of inputs, one per row, with the output at the end. Two inputs, A and B, each 0 or 1: four mixes, four rows: 0 0, 0 1, 1 0, 1 1. Three inputs: eight rows. Four: sixteen. Each new input doubles the rows, because every old row now appears once with the new input at 0 and once at 1.

Order the rows by counting in binary: 00, 01, 10, 11. Right column goes 0, 1, 0, 1; left column goes 0, 0, 1, 1. With three inputs the right column flips every row, the middle every two, the left every four. Done this way nothing is missed, nothing repeats, and two people's tables for the same gate match line for line.

Why bother? Words get slippery for bigger circuits; a table has every case and no fuzz, and you can check it against a real circuit row by row. It is also the design document: write the table of what the system must do first, build to it, test against it. For the panic button, the truth table is what your circuit must obey and what the examiner marks.

Hold the four rows 00, 01, 10, 11 in mind and try the questions for this part: every case in a grid.

## Subtopic: Filling In AND

AND table: output 1 only when every input is 1. Rows: 0 0 gives 0; 0 1 gives 0; 1 0 gives 0; 1 1 gives 1. One 1 at the bottom, three 0s above. That shape is AND's signature.

Now test it, which makes the table real. Build the series circuit: cell, switch A, switch B, lamp, one loop. Row one: both open; lamp dark; table says 0; tick. Row two: A open, B closed; dark; 0; tick. Row three: A closed, B open; dark; 0; tick. Row four: both closed; light; 1; tick. Four ticks, verified. A row that disagrees means the circuit or the table is wrong, and finding which is debugging. Wire B across the lamp by mistake and the lamp lights with A alone, so row three fails, and the table has pointed at the fault.

Record it honestly: a column for predicted, a column for observed, tick or cross each row. Marks go to a table that matches the gate, a circuit that matches the table, and the testing that joins them. Right table, no test, is half the work; test, find a mismatch, fix it, is the real work.

Hold the single 1 at the bottom in mind and try the questions for this part: filling in AND.

## Subtopic: Filling In OR, and Reading Backwards

OR table: output 1 when any input is 1. Rows: 0 0 gives 0; 0 1 gives 1; 1 0 gives 1; 1 1 gives 1. One 0 at the top, three 1s below. OR's signature. Test on the parallel circuit: both open, dark, tick; B only, light, tick; A only, light, tick; both, light, tick.

Side by side, the input columns are identical; only the output differs. AND and OR agree on the first row, both 0, and the last row, both 1. They disagree on the middle two, where exactly one input is on: AND says 0, OR says 1. That is the whole difference, two cells, and it is why a tester must try the mixed cases; both-off and both-on alone cannot tell the gates apart.

Reading backwards. One 1 at the bottom: AND, switches in series. One 0 at the top: OR, switches in parallel. A car light that comes on when either door opens: 1 in every row but the first, OR, two door switches in parallel with the lamp. A lift that moves only with doors closed and a button pressed: 1 only in the last row, AND, two switches in series with the motor. Three inputs: eight rows, one 1 at the end is a three-input AND, three switches in series; one 0 at the start is a three-input OR, three in parallel.

Pocket summary of the lesson. Columns for inputs then output, rows for every mix, counted in binary so none is missed. AND: single 1 at the bottom; OR: single 0 at the top; they differ only in the mixed rows. Test every row against the real circuit, predicted against observed. Read a table back to its gate and its switch circuit.

Hold the two middle rows where the gates disagree in mind, and take the final questions of the lesson: filling in OR, and reading backwards.
