# Part 1 — Expert

This session answers the question no average can answer: how SPREAD OUT is the data? The tools are the measures of dispersion — range, quartiles, the interquartile range, percentiles — and the five-number summary they assemble into, drawn as the box-and-whisker diagram. One dataset of eleven juice-kiosk sales figures travels through the whole session, and by the end you will compute every measure, construct the diagram from its summary, and read anyone else's diagram like a report.

## Subtopic: Range and Why Spread Matters

Two small datasets, both test scores out of 100, both with a mean of exactly 60. Dataset A: 56, 58, 60, 62, 64. Dataset B: 30, 45, 60, 75, 90. Identical means — utterly different stories. Dataset A is a steady performer: every mark presses close to 60. Dataset B lurches from failing to outstanding. Any summary reporting only the centre treats these two as twins, which is why every serious data report carries TWO kinds of number: a centre, and a spread.

The simplest spread measure is the RANGE: maximum minus minimum. Dataset A: 64 minus 56 is 8. Dataset B: 90 minus 30 is 60. One subtraction each, and the difference between the datasets becomes a visible number.

But the range carries a weakness you must be able to name: it consults ONLY the two most extreme values, so a single outlier owns it outright. Let one learner scoring 95 join dataset A and its range explodes from 8 to 39, even though the original five marks still huddle around 60. The range is quick, fragile, and easily distorted — which is precisely why the quartile tools of the next section were invented.

Pause here — questions on this section are coming to you now. They test the calculation and, more importantly, the weakness: know exactly what the range cannot see.

## Subtopic: Quartiles and the Interquartile Range

The running dataset arrives: a juice kiosk recorded how many cups it sold on eleven school days. Ordered: 3, 5, 8, 10, 12, 13, 18, 21, 24, 26, 33.

Quartiles slice the ordered data into four equal-sized groups using three cut points. The middle cut is the median, also called the second quartile. Eleven values: the median is the sixth, with five below and five above — count in: 3, 5, 8, 10, 12, then 13. The median is 13.

The LOWER quartile, Q1, is the median of the lower half — the five values beneath the median: 3, 5, 8, 10, 12. Their middle is the third: 8. So Q1 is 8. The UPPER quartile, Q3, is the median of the upper half: 18, 21, 24, 26, 33. Middle value: 24. So Q3 is 24. With an odd number of values, the median itself joins neither half — it is the fence between the halves, never a resident of either.

Now the star measure: the INTERQUARTILE RANGE, IQR, is Q3 minus Q1 — 24 minus 8, which is 16. Read its meaning precisely: the middle 50 percent of all the days sold between 8 and 24 cups, and that middle half spans just 16 units. Because the IQR is measured between the quartiles, extreme days cannot touch it: the dead day of 3 and the heat-wave day of 33 sit entirely outside the fences. The IQR is the outlier-resistant range. The semi-interquartile range is simply half of it — 16 over 2 is 8 — occasionally requested by name, never harder than one halving.

Full range for contrast: 33 minus 3 is 30. Range 30, IQR 16: the extremes stretch nearly twice as wide as the middle half — and stating that comparison is already analysis.

Stop for this section's questions now. Order, cut, and remember: lower half's middle, upper half's middle, subtract.

## Subtopic: The Five-Number Summary and the Box-and-Whisker Diagram

Line up the five numbers you now own, smallest to largest: the minimum 3, then Q1 at 8, the median 13, Q3 at 24, and the maximum 33. That ordered list is the FIVE-NUMBER SUMMARY — the complete skeleton of the dataset, centre and spread in five values.

The box-and-whisker diagram is that summary made visual, and you must be able to build it from words alone. Start with a horizontal number line covering the data — 0 to about 35 here. Above it, draw a rectangular box beginning at Q1, which is 8, and ending at Q3, which is 24: the box IS the middle half of the data, and its length IS the IQR. Inside the box, draw a vertical line at the median, 13. Then the whiskers: one horizontal line from the box's left wall out to the minimum at 3, another from the right wall out to the maximum at 33. Five landmarks, one box, two whiskers — done.

Now the reading rule that unlocks every interpretation question: each of the four sections — left whisker, left half of the box, right half of the box, right whisker — holds ONE QUARTER of the data. Roughly 25 percent of the days live in each section, always, regardless of how long or short a section looks. A LONG section does not contain more days; it contains the same quarter of days stretched over a wider band of values. Long section, spread-out quarter; short section, tightly bunched quarter. That single sentence is the entire craft of reading these diagrams.

Check ours: the left whisker runs 3 to 8 — five units for a quarter of the days, tightly packed quiet days. The right whisker runs 24 to 33 — nine units for the same quarter: the busy days are far more spread out.

Pause now for this section's questions — assemble the diagram in your head from the five numbers, and read every section as a quarter.

## Subtopic: Percentiles, Skew and Comparing Two Box Plots

Three finishing tools convert computation into commentary.

First, percentiles — the fine-grained cousins of quartiles. The p-th percentile is the value below which p percent of the data lies. Three of them you already know under other names: Q1 is the 25th percentile, the median is the 50th, Q3 is the 75th. So "the 75th percentile of sales was 24" and "Q3 was 24" are one and the same sentence. If a selection squad takes only learners at the 90th percentile in a trial test, it demands a mark that only 10 percent of candidates beat — percentiles rank you against the group, never against the paper.

Second, skew. A perfectly symmetrical dataset places its median in the middle of the box with matching whiskers. When the right side stretches longer — median closer to Q1, long right whisker, exactly like our juice data with its median 5 units from Q1 but 11 from Q3 — the data is skewed to the right, also called positively skewed: most values bunch low, with a tail of large values. A stretched left side means skewed to the left, negatively skewed. State it with the evidence attached: "the median lies nearer the lower quartile and the upper whisker is longer, so the distribution is skewed to the right."

Third, comparison — the favourite question format: two box plots sharing one number line. Compare them in two sentences, one idea each. Sentence one, centres: whichever median is higher, that group typically scored more. Sentence two, spreads: whichever box is longer, that group's middle half varied more — less consistent. Class A with median 62 and IQR 10 against class B with median 58 and IQR 26: A typically scored higher AND was more consistent. Never compare centres alone; the spread sentence carries marks of its own.

The compressed method: order the data; median, then quartiles from the halves; five-number summary; box on the quartiles, whiskers to the extremes; read each section as a quarter; comment on centre, spread and skew. The final questions of this part are with you now — a different diagram, the identical six moves.

# Part 2 — Simplifier

The same tools once more, rebuilt with your own hands — comparing two pizza deliveries, folding a strip of paper, stretching a box until it confesses. Nothing new is coming: the five numbers will land exactly where they landed. What changes is that spread will stop being a formula and become something you can feel.

## Subtopic: Same Average, Different Story

Two pizza places both print the same promise on the flyer: average delivery, 40 minutes. Place one runs a tight kitchen: deliveries take 38, 39, 40, 41 or 42 minutes. Place two sends one scooter across the whole suburb: deliveries take 25, 30, 40, 50 or 55 minutes. Both average exactly 40 — yet nobody would call them the same service. From place one you can promise hungry friends a time. From place two the pizza might beat you home, or arrive cold an hour after kickoff — and the flyer's "average" hides all of that.

The lesson inside the story: an average reports the CENTRE of the data; it says nothing about how far the data WANDERS from that centre. Spread is the wandering. Two datasets can share a centre and differ wildly in spread — and the spread is usually the fact you actually care about: reliability, consistency, risk.

The quickest wandering-meter is the range: slowest delivery minus fastest. Place one: 42 minus 38, a range of 4 minutes. Place two: 55 minus 25, a range of 30. One number each, and the flyer's trick is exposed. But mark the range's blind spot: a single freak delivery — a flat tyre, a wrong address — and the range balloons, even if every other pizza arrived on the dot. It measures only the two most extreme stories, never the everyday ones. Hold onto that weakness; the next section builds the repair.

Quick check before we carry on — a few questions on centre versus spread are coming to you right now. Ask of each scenario: is this about where the middle sits, or about how far things wander?

## Subtopic: Folding the Line in Half, Then in Half Again

The juice kiosk again: eleven days of cup sales — 3, 5, 8, 10, 12, 13, 18, 21, 24, 26, 33. Write the eleven numbers, in order, along a strip of paper.

Fold one: fold the strip at its middle. Eleven numbers — the sixth is dead centre, five on either side. The sixth reads 13. That is the median, the 50-50 cut: half the days sold fewer cups, half sold more.

Fold two: take the piece LEFT of the fold — five numbers — and fold it at ITS middle: the third number, 8. Fold three: the piece RIGHT of the first fold — five numbers — folds at 24. Three folds, three creases: 8, 13, 24. The quartiles are nothing more than the middle of the strip, then the middles of each half. And the number ON the first crease, 13, sits on the fold itself — with eleven values, the middle one belongs to neither half.

Now read what the creases did: they cut eleven days into four little groups of roughly equal size. The middle two groups together — the days between 8 and 24 — are the middle half of all days: the ordinary days, free of dead-quiet mornings and heat-wave stampedes. How wide is ordinary? From 8 to 24: sixteen cups wide. That width is the interquartile range — and because it is measured crease to crease, the wild days at 3 and 33 cannot stretch it. The IQR is the range that ignores drama. Half of it, 8, is the semi-interquartile range — the same fact, halved.

Your questions for this section are up now. Fold, fold, fold: middle of the strip, middle of each half, and read the width between the creases.

## Subtopic: Drawing the Box in Words

The five numbers of the juice kiosk, in order: 3, 8, 13, 24, 33 — minimum, first crease, middle, second crease, maximum. The box-and-whisker diagram is these five landmarks laid on a number line, and you can narrate it with your eyes shut.

Put the number line down. At 8 and 24, raise two walls and join them into a box — the box is home to the middle half of the days, the ordinary days. Draw the median line inside at 13. From each wall, stretch a whisker: left to the minimum at 3, right out to the maximum at 33. The picture announces: ordinary days live in the box; the whiskers reach out to the quietest and busiest days on record.

The one rule that makes you dangerous at reading these: every section holds a QUARTER of the days. The stubby left whisker, 3 to 8: a quarter of the days, squeezed tight — the quiet days are all alike. The long right whisker, 24 to 33: the SAME quarter-sized crowd, stretched wide — busy days come in many sizes. Long never means many; long means spread. Repeat it before every reading question.

And when two boxes share one number line — two classes, two delivery services, two months of sales — your comparison always has two sentences. Where do the median lines sit? Higher median, typically bigger values. How long are the boxes? Longer box, more wandering in the middle half — less consistency. And if the shape is lopsided, add the bonus phrase: a long right side means skewed to the right, a tail of big values.

You now own the complete toolkit: range with its named weakness, the three folds, the five landmarks, the box you can draw from words alone, and the quarter-per-section rule that reads any box back into facts. The final questions of the lesson are arriving right now — five numbers, four quarters, two sentences of comparison. Finish strong.
