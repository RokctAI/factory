# Part 1 — Expert

This session covers resistor values printed on the component or given by colour bands, three value bands and a tolerance band. The anchor is a tray of mixed resistors tipped out on a bench in Welkom, learners sorting them into labelled compartments by reading the bands and then confirming with a multimeter, discovering that the yellow, violet, brown resistor they need for the LED is 470 ohms and that its gold band promises it is within 5 percent of that. The governing idea is that resistance is measured in ohms, that the first two bands give significant digits, the third the number of zeros, and the fourth the tolerance, and that the colour sequence black, brown, red, orange, yellow, green, blue, violet, grey, white stands for 0 to 9. Reading and writing resistor colour codes, stating tolerance and selecting a value are examinable.

## Subtopic: What a Resistor Does and How Its Value Is Marked

A resistor is a component made to have a definite resistance, so that it limits current to a chosen amount or divides a voltage in a chosen ratio. Resistance is measured in ohms; a thousand ohms is a kilohm, written with k, and a million ohms is a megohm, written with M. Everyday resistors look like small cylinders with a wire at each end, in values from a few ohms to several megohms. A low resistance lets much current flow for a given voltage; a high resistance lets little. The 470 ohm resistor in the PAT LED circuit sits in the middle of the range and holds the LED current to a few milliamperes from a 4.5 volt battery.

Large power resistors, which handle a lot of current and get warm, are big enough to have their value printed in figures, such as 10R for 10 ohms or 4k7 for 4700 ohms, where the letter stands in for the decimal point so that it cannot be lost in printing. Small resistors have no room for figures and are marked with coloured bands painted round the body. The bands can be read from any angle while the resistor is on a board, which numbers cannot. Variable resistors, met later, usually have their maximum value printed.

The symbol for a resistor is a plain rectangle in the circuit diagram, with the value written beside it, such as 470 ohms or 4k7. The value, not the colour, goes on the diagram. The error of forgetting to write the value is common and leaves the builder unable to pick the right part, so every resistor on a PAT diagram is labelled with its value.

The questions for this section are with you now: what a resistor does and the ohm, printed values on large resistors, and the symbol with its value.

## Subtopic: Reading the Three Value Bands

Ten colours stand for the digits 0 to 9: black 0, brown 1, red 2, orange 3, yellow 4, green 5, blue 6, violet 7, grey 8, white 9. Learners remember the order with a sentence of their own choosing; any phrase whose words begin with the letters B B R O Y G B V G W will do, and inventing one is better than borrowing one. Hold the resistor with the bands grouped toward the left, the lone band, usually gold or silver, toward the right. Read the first band as the first digit, the second band as the second digit, and the third band as the number of zeros to add.

Yellow, violet, brown: 4, 7, one zero, which is 470 ohms. Red, red, red: 2, 2, two zeros, which is 2200 ohms, written 2k2. Brown, black, orange: 1, 0, three zeros, which is 10 000 ohms, 10k. Orange, orange, black: 3, 3, no zeros, which is 33 ohms. Brown, black, red: 1, 0, two zeros, 1000 ohms, 1k. Green, blue, yellow: 5, 6, four zeros, 560 000 ohms, 560k. Writing the two digits and then the zeros, every time, in that order, makes the reading mechanical.

Going the other way, from value to colours, is the same process reversed. 330 ohms: 3, 3, one zero, so orange, orange, brown. 47k, which is 47 000 ohms: 4, 7, three zeros, so yellow, violet, orange. 1M, a million ohms: 1, 0, five zeros, brown, black, green. Two special cases: a third band of black means no zeros, and a third band of gold means divide by 10, so red, red, gold is 2.2 ohms, which appears in power circuits but not in the PAT.

The questions for this section are with you now: the ten colours and their digits, reading three bands to a value, and writing a value as three bands.

## Subtopic: The Tolerance Band, Checking With a Meter and Choosing Values

The fourth band, set apart from the others, is the tolerance: how far the actual resistance may differ from the marked value. Gold means 5 percent, silver means 10 percent, no fourth band means 20 percent; brown means 1 percent and red 2 percent on precision types. A 470 ohm resistor with a gold band is guaranteed to lie between 446.5 and 493.5 ohms. For an LED resistor this spread does not matter; for a timing circuit or a measurement it might, and the designer then specifies a tighter tolerance and pays more for it.

A multimeter set to ohms checks the reading. Touch the probes to the two leads of the resistor, not held in the fingers because skin conducts, and read the display; a marked 470 ohm resistor might show 468 or 473, within its 5 percent. Measuring a resistor while it is in a circuit gives a wrong answer, because other components form parallel paths, so test it loose. The meter also finds a resistor whose bands have faded or whose colours are hard to tell apart, red from orange being the usual trouble under poor light.

Resistors come in standard values, not every number, and the common series runs 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82 and their multiples of ten. A calculation that gives 250 ohms is met with the nearest standard value, 270, or the next value up if the current must not exceed the calculated amount. Choosing up gives a slightly smaller current and a safer LED, which is why the PAT uses 470 ohms rather than 270. The error museum, four exhibits. One: reading the bands from the wrong end, starting at the gold band. Two: treating the third band as a digit instead of the number of zeros. Three: measuring a resistor while holding both leads with the fingers. Four: writing a colour on the circuit diagram instead of a value.

The questions for this section are with you now: the tolerance band and what it guarantees, checking with a multimeter, and standard values and choosing up.

# Part 2 — Simplifier

Now the same lesson again with the tray of resistors tipped out on the bench in Welkom — plain words, same facts.

## Subtopic: A Component That Slows the Current

A resistor resists current. Its value is in ohms; k for thousands, M for millions. Low ohms, lots of current; high ohms, little. The PAT's 470 ohms keeps the LED to a few milliamperes.

Big resistors have numbers printed: 10R, 4k7. Small ones have coloured bands you can read from any angle.

Symbol: a rectangle, with the value written next to it. Value, not colour, on the diagram.

Keep a component that slows the current in mind and try the questions for this part: what a resistor is.

## Subtopic: Two Digits and a Number of Zeros

Colours for 0 to 9: black, brown, red, orange, yellow, green, blue, violet, grey, white. Make up your own sentence to remember the order. Bands grouped to the left, lone band to the right.

First band, first digit. Second band, second digit. Third band, number of zeros. Yellow violet brown: 4, 7, one zero, 470. Red red red: 2200. Brown black orange: 10 000.

Backwards: 330 is 3, 3, one zero: orange orange brown. 47k is 4, 7, three zeros: yellow violet orange.

Hold two digits and a number of zeros in mind and try this part's questions: reading bands.

## Subtopic: How Close Is Close Enough

Fourth band is tolerance: gold 5 percent, silver 10, none 20. A gold 470 lies between about 447 and 494. Fine for an LED.

Check with a multimeter on ohms, resistor loose, not between your fingers. 468 or 473 for a 470 is normal. Faded bands: measure.

Resistors come in standard values: 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82 and tens of those. Need 250? Take 270, or go up for a safer LED. That is why the PAT uses 470.

Pocket summary of the lesson. A resistor limits current and is valued in ohms. Small resistors carry colour bands: the first two give digits, the third the number of zeros, using black to white for 0 to 9, and the fourth, set apart, gives the tolerance, gold 5 percent and silver 10. Yellow, violet, brown is 470 ohms. Values are checked with a multimeter on a loose resistor, chosen from standard values, and written as numbers on the diagram.

Hold how close is close enough, and take the final questions of the lesson: tolerance and choosing values.
