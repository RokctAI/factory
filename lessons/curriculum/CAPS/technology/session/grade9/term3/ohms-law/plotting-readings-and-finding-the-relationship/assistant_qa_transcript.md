### subtopic_1 — Setting Up the Graph: Axes, Scales and Plotting the Points
**Assistant:** Why do we draw one straight line instead of joining the points, when the points are the actual measurements?

**Tutor:** Because the points are measurements with small errors in them, and the line is the best estimate of the relationship underneath. Each cross is where the meters said the readings were, give or take a last digit, a slightly loose clip and a cell that was a little tired. If you join them dot to dot you draw a zigzag that treats every one of those small errors as a real change in the resistor's behaviour, which is not what happened; the resistor did not change its resistance between two cells and three. A single straight line through the cloud of points averages the errors out and shows the thing you were actually looking for, that voltage over current stayed constant. The scatter of the points around the line is also useful: it shows how good your measurements were. A tight scatter means careful work; a loose one means retakes next time.

***

### subtopic_2 — The Line of Best Fit and What a Straight Line Through the Origin Means
**Assistant:** Our line of best fit does not quite go through the origin. Do we force it?

**Tutor:** Think about what you know first, then decide. You know that with no cells there is no voltage and no current, so the true relationship must pass through the origin; that is a physical fact, not a measurement, and it is the strongest point on the graph. If your three points lie slightly to one side of a line through the origin, the right move is to draw the line through the origin and as close to the points as you can, and then to note in the conclusion that the points sit a little above or below it. If the points lie so far off that a line through the origin clearly misses all of them, do not force it; draw the line that fits the points, note that it misses the origin, and look for the cause: a meter zero error, where the ammeter reads a little current with nothing flowing, is the usual one. The graph should tell the truth about the data, and your conclusion should explain the difference between what you expected and what you drew.

***

### subtopic_3 — Finding Resistance From the Gradient and Writing the Conclusion
**Assistant:** Why does the gradient give resistance and not something else?

**Tutor:** Because of what gradient means and what the axes are. Gradient is the change in the vertical quantity divided by the change in the horizontal quantity. Here the vertical quantity is voltage and the horizontal is current, so the gradient is volts divided by amperes, and Ohm's law says that volts divided by amperes is the resistance. If the axes were swapped, current vertical and voltage horizontal, the gradient would be amperes per volt, which is one over the resistance, and you would have to invert it. That is the practical reason this course puts voltage on the vertical axis: the gradient is then the resistance directly, and a steeper line means a larger resistor. For the 100 ohm resistor the line rises 100 volts for every ampere, which on your paper is 4.4 volts for 0.044 amperes; a 470 ohm resistor would give a much steeper line, 4.4 volts for only 0.0094 amperes.
