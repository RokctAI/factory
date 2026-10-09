# Part 1 — Expert

This session covers drawing the circuit diagram and truth table for the panic button system. The anchor is the same Grade 8 pair in Soweto, now with three push switches on long leads, a buzzer, an LED and its resistor, a two-cell battery and a sheet of paper that must carry a diagram another learner could build from and a table every row of which the built circuit must match.

## Subtopic: From Specification to Gate: Why the Panic Button Is an OR

Start from the specification, not from a circuit you already like. The specification says: the alarm must sound when the bed button is pressed, or the stove button, or the toilet button, any one alone, and also when more than one is pressed; it must not sound when no button is pressed. Read that as a logic statement with three inputs, bed B, stove S and toilet T, and one output, alarm A: A is 1 when B is 1 or S is 1 or T is 1; A is 0 only when B, S and T are all 0. That is the definition of a three-input OR gate, and we know from the logic lessons that OR is built from switches in parallel. So the heart of the panic button is three push switches in parallel, feeding the alarm from the battery. The gate was not chosen because it is familiar; it was read off the specification, and in the examination the mark is for showing that reasoning.

Check the alternative to be sure. Three switches in series would be a three-input AND: the alarm would sound only when all three buttons were pressed at once, which a woman alone in a two-room house cannot do, so the alarm would never sound; the design would fail the first specification in every row but the last. Writing this down, briefly, shows that the choice was made and not assumed.

Now the output. The specification asks for a loud alarm and a bright light, so the output is two devices, a buzzer and a lamp, and both must operate when any switch closes. They are placed in parallel with each other across the output, so that each receives the full battery voltage and either would work if the other failed; a buzzer and a lamp in series would share the voltage and the buzzer might not sound. If the lamp is an LED, it needs its series resistor, 330 ohms for a 3 volt supply, and its polarity matters, the long leg to positive. A battery of two or three cells in series provides the voltage; the buzzer and lamp are chosen to match it.

The questions for this section are with you now: how the specification is read as a three-input OR, why series switches would fail, and how the two output devices are connected.

## Subtopic: Drawing the Circuit Diagram With Standard Symbols

Draw the diagram with standard symbols, ruler and pencil. The battery sits on the left as two or three cell symbols in series, long thin line positive, short thick line negative, labelled with its voltage, 3 V. From the positive terminal a line runs up and across the top of the diagram. The three push switches hang from that top line as three parallel branches, each a push-to-make switch symbol, a small open contact with a button above it, labelled B, S and T for bed, stove and toilet; their lower ends rejoin at a line below. A dot marks every junction where a branch meets the top or bottom line, six dots in all for three branches. From the rejoined line the circuit continues to the output: the buzzer symbol, a half-circle with two leads, and the lamp, a circle with a cross for a filament lamp or a triangle-with-bar and arrows for an LED with its rectangle resistor in series, the two output branches in parallel with each other, dots at their junctions, and the line returns to the battery's negative terminal.

Then the refinements the specification demands. A reset switch: in the simplest circuit, releasing the button stops the alarm, which is a problem if Gogo has fallen and cannot keep pressing, so a latching arrangement is wanted; at Grade 8 level this is shown as a toggle switch in parallel with the push switches, which Gogo or the neighbour closes to hold the alarm on and opens to silence it, labelled R for reset and described in a note, since a true self-latching circuit uses a relay that Grade 9 introduces. A standby current of zero: because every switch is open in standby, the circuit draws nothing, which satisfies the year-of-batteries specification, and it is worth saying so on the diagram. Long leads to the toilet: shown as a longer line to switch T, with a note that in the real device this run would be in weatherproof cable or replaced by a wireless button.

Finishing rules: straight lines, right-angle corners, symbols standard size and not touching, labels beside every component, values for the battery and resistor, the title "Panic button alarm circuit" and the designer's name and date beneath. Give the diagram to a partner and ask them to list the components and trace the path from positive to negative through each switch alone; if they can, the diagram is buildable.

The questions for this section are with you now: the symbols and layout of the diagram, the junction dots, and the reset, standby and toilet-lead refinements.

## Subtopic: The Eight-Row Truth Table and Testing the Built Circuit

Now the truth table that the circuit must satisfy. Three inputs, B, S and T, so eight rows, counted in binary from 000 to 111: 000, 001, 010, 011, 100, 101, 110, 111. The output A follows the OR rule: 0 for the first row only, where no button is pressed, and 1 for the other seven. Write the full table with the inputs in the left three columns and A in the fourth, and add a fifth column headed "observed" for the bench test. A note below the table states the rule in words: "The alarm sounds when any one or more of the three buttons is pressed, and is silent only when none is pressed."

Build the circuit from your own diagram, one lead at a time with no button pressed, checking against the drawing before connecting the battery. Then test every row. Row one, nothing pressed: silence and dark, observed 0, matches. Row two, toilet only: buzzer and lamp, 1, matches. Row three, stove only: 1. Row four, stove and toilet: 1. Row five, bed only: 1. Row six, bed and toilet: 1. Row seven, bed and stove: 1. Row eight, all three: 1. Eight rows, eight matches, and the table is verified; write the date of the test and the names of the testers. If a row fails, use it to find the fault: if the toilet button alone does nothing while the others work, the toilet branch is open, a loose lead or a dead switch; if the alarm sounds in row one, a switch is wired closed or two leads are touching.

Then test the specification items that the table does not cover: loudness, with the buzzer heard from across the classroom and the lamp seen from the door; the reset, with the toggle holding the alarm on after a button is released and silencing it when opened; and standby, with an ammeter in the main line reading zero when no button is pressed. Record each as met or not met. This is the evidence the examiner wants: a diagram, a table, and a test record that connects them.

The error museum, four exhibits. One: switches drawn in series, an AND, so the alarm needs all three buttons. Two: buzzer and lamp in series with each other, so they share the voltage and one may fail to work. Three: a four-row truth table for a three-input system. Four: a diagram with no junction dots, so a reader cannot tell branches from crossings.

The questions for this section are with you now: the eight-row table and its rule, the row-by-row bench test and how a failed row locates a fault, and the specification tests beyond the table.

# Part 2 — Simplifier

Now the same lesson again with three push switches on long leads, a buzzer, an LED and a sheet that must carry a diagram and a table — plain words, same facts.

## Subtopic: Which Gate Does the Spec Ask For?

Start from the spec, not from a circuit you like. It says: the alarm sounds when the bed button, or the stove button, or the toilet button is pressed, one alone or more than one; silent when none is pressed. As logic: three inputs, B, S, T; one output, A. A is 1 when B or S or T is 1; A is 0 only when all three are 0. That is a three-input OR, and OR is switches in parallel. So the heart is three push switches in parallel between the battery and the alarm. We did not pick OR because we like it; we read it off the spec, and that reasoning is what earns the mark.

Check the other way. Three switches in series is AND: alarm only when all three are pressed at once, impossible for one woman in two rooms, so it would never sound; fails the first spec in every row but the last. Write that down in a line to show you chose.

Output: the spec wants loud and bright, so a buzzer and a lamp, both working whenever any switch closes. Put them in parallel with each other, so each gets the full battery volts and either works if the other dies; in series they would share the volts and the buzzer might stay quiet. An LED needs its 330 ohm resistor in series and its long leg to plus. Two or three cells in series give the volts; pick buzzer and lamp to match.

Hold the three switches side by side in mind and try the questions for this part: which gate does the spec ask for?

## Subtopic: Drawing It Properly

Draw it with standard symbols, ruler and pencil. Battery on the left: two or three cell symbols in series, long thin line plus, short thick line minus, labelled 3 V. A line from plus up and across the top. Three push switches hang from the top line as three parallel branches, each a push-to-make symbol, open contact with a button over it, labelled B, S, T; their bottoms rejoin on a line below. A dot at every junction, six for three branches. From the rejoined line to the output: buzzer symbol, a half-circle with two leads, and the lamp, a circle with a cross for a bulb or the LED triangle with arrows plus its resistor rectangle in series, these two output branches in parallel with each other, dots at their junctions, and the line back to minus.

Refinements the spec asks for. Reset: in the plain circuit, let go and the alarm stops, bad if Gogo has fallen; so a hold-on arrangement, shown at Grade 8 as a toggle switch in parallel with the push switches, labelled R, closed to hold the alarm on and opened to silence it, with a note that a real self-latching version uses a relay, next year. Standby zero: every switch is open at rest, so nothing is drawn, which meets the year-of-batteries spec; say so on the diagram. Toilet lead: a longer line to T, with a note that the real one is weatherproof cable or a wireless button.

Finish: straight lines, square corners, standard symbols not touching, a label by every part, values for battery and resistor, title "Panic button alarm circuit", your name and date. Hand it to a partner: can they list the parts and trace plus to minus through each switch alone? Then it is buildable.

Hold the six dots in mind and try the questions for this part: drawing it properly.

## Subtopic: Eight Rows and a Bench Test

The truth table the circuit must obey. Three inputs, eight rows, counted in binary: 000, 001, 010, 011, 100, 101, 110, 111. Output A: 0 in the first row only, nothing pressed; 1 in the other seven. Inputs in three left columns, A in the fourth, and a fifth column "observed" for the bench. Under it, the rule in words: "The alarm sounds when any one or more buttons is pressed, and is silent only when none is."

Build from your own diagram, one lead at a time, no button pressed, check against the drawing, then connect the battery. Test every row. Nothing pressed: silent, dark, 0, match. Toilet only: buzz and light, 1. Stove only: 1. Stove and toilet: 1. Bed only: 1. Bed and toilet: 1. Bed and stove: 1. All three: 1. Eight matches, verified; date and names. A failed row finds the fault: toilet alone does nothing but the rest work, the toilet branch is open, loose lead or dead switch; alarm sounds with nothing pressed, a switch is wired closed or two leads touch.

Then the spec items the table does not cover: loudness, buzzer heard across the room, lamp seen from the door; reset, toggle holds the alarm on after release and silences when opened; standby, ammeter in the main line reads zero with nothing pressed. Met or not met, each one. Diagram, table, test record: that is what the examiner wants.

Pocket summary of the lesson. Spec says any one button, so three-input OR, so three push switches in parallel; series would be AND and never sound. Buzzer and lamp in parallel at the output, LED with resistor. Diagram with standard symbols, dots at junctions, reset toggle, zero standby, toilet lead noted. Eight-row table, 0 then seven 1s, tested row by row, then loudness, reset and standby.

Hold the single 0 at the top of eight rows in mind, and take the final questions of the lesson: eight rows and a bench test.
