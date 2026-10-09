### subtopic_1 — What a Resistor Does and How Its Value Is Marked
**Assistant:** Why do the bands use a number of zeros instead of just three digits?

**Tutor:** Because three digits can only reach 999, and resistors run from under one ohm to over ten million, which is eight orders of magnitude. A multiplier band covers that whole range with the same ten colours: two digits give the shape of the number and the third band slides it up or down by powers of ten, so brown black black is 10, brown black red is 1000 and brown black green is a million, all with the same first two bands. It also matches how the standard values are arranged, since 47, 470, 4700 and 47 000 are all in the series and all read yellow violet with a different third band. Reading two digits and a count of zeros feels odd for a few minutes and then becomes faster than reading three digits would be, because you only ever learn one set of ten colours.

***

### subtopic_2 — Reading the Three Value Bands
**Assistant:** How can I tell which end to start from if the bands are evenly spaced?

**Tutor:** Use three clues in turn. First, the tolerance band is usually a colour that never appears as a first digit: gold or silver, and no resistor begins with gold, so if one end is gold or silver, start from the other end. Second, the tolerance band is normally spaced a little further from its neighbour than the value bands are from each other, even when it looks even at first glance; a close look under good light usually shows the gap. Third, if both clues fail, read it both ways and ask which answer is a standard value: red violet yellow is 270 000, a standard value, while yellow violet red is 4700, also standard, so that one is genuinely ambiguous and you reach for the meter. In practice the gold band settles nearly every case in a school kit, and the multimeter settles the rest in two seconds.

***

### subtopic_3 — The Tolerance Band, Checking With a Meter and Choosing Values
**Assistant:** Does a 5 percent tolerance matter for the LED resistor?

**Tutor:** No, and it is worth seeing why with numbers. A 470 ohm resistor at 5 percent could be as low as 447 ohms or as high as 494. With a 4.5 volt battery and a 2 volt LED, the resistor drops 2.5 volts, so the current is 2.5 over 447, about 5.6 milliamperes, or 2.5 over 494, about 5.1 milliamperes. The LED cannot tell the difference, the eye cannot tell the difference, and both are far below the 20 milliampere limit. Tolerance matters when a resistor sets a time, a frequency or a measured voltage, where a 5 percent error becomes a 5 percent error in the result and a designer might pay for 1 percent parts. For an indicator LED, the cheapest 5 or even 10 percent resistor is the right choice, and spending more is wasted money in a budget that is already tight.
