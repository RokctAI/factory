# Part 1 — Expert

Two classes can share the same average and be nothing alike: one steady, one wild. Measures of centre cannot see that difference — measures of SPREAD exist for it. This session revises the five number summary and box-and-whisker diagram, builds grade eleven's new precision instruments — variance and standard deviation — then uses centre and spread together to diagnose the shape of data and to catch outliers with an exact rule instead of a feeling.

## Subtopic: The Five Number Summary and the Box-and-Whisker

The running dataset: ten learners' test marks, already sorted — 44, 48, 50, 52, 53, 55, 56, 58, 60, 84.

The five number summary is minimum, lower quartile, median, upper quartile, maximum. Minimum 44, maximum 84. The median of ten values sits between the fifth and sixth: 53 and 55 average to 54. The lower quartile is the median of the bottom five values — 44, 48, 50, 52, 53 — which is the third one, 50. The upper quartile is the median of the top five — 55, 56, 58, 60, 84 — which is 58. So the summary reads: 44, 50, 54, 58, 84.

The box-and-whisker diagram draws those five numbers on a scaled line: a box from 50 to 58 with a bar at the median 54, a short whisker reaching left to 44, and a long whisker stretching right to 84. Two spread measures fall straight out. The range, maximum minus minimum, is 40 — but it depends entirely on the two most extreme values, so one strange mark controls it completely. The interquartile range, upper quartile minus lower, is 58 minus 50, which is 8: the span of the middle half of the class, immune to whatever happens at the ends. Already the picture is talking: the middle half of this class is packed into eight marks, while one whisker reaches out twenty-six marks to the right. Hold that thought for the last subtopic.

Pause here — the questions for this section are with you now. They build a five number summary and read a box plot: sort first, quartiles are medians of halves, and say what the long whisker suggests.

## Subtopic: Variance and Standard Deviation

The interquartile range ignores the extremes by design — but sometimes you want a spread measure that listens to EVERY value. That is the standard deviation: roughly, the average distance of the data from its mean.

The recipe, on a small clean dataset: 4, 6, 7, 9 and 14 — say, goals scored in five netball matches. Step one, the mean: the sum is 40, divided by 5 gives 8. Step two, deviations from the mean: minus 4, minus 2, minus 1, 1 and 6. Note that these deviations always sum to zero — the data below the mean exactly balances the data above — which is precisely why we cannot just average them. Step three, square each deviation to kill the signs: 16, 4, 1, 1 and 36. Step four, average the squares: the sum is 58, divided by 5 gives 11,6. That number is the VARIANCE. Step five, undo the squaring: the square root of 11,6 is 3,41. That is the standard deviation — on average, a match sits about three and a half goals away from the mean of 8.

Why both names? Variance is the natural stopping point of the algebra, but its units are squared — goals squared means nothing to a coach. Square rooting returns to the units of the data, which is why the standard deviation is the reported measure. In the exam, show the table: values, deviations, squared deviations, then the two-line finish. And know your calculator's statistics mode well enough to CHECK the table — the calculator confirms, the table earns the marks.

Stop for this section's questions now — mean, deviations, squares, average, root: five steps in a fixed order.

## Subtopic: Symmetric and Skewed Data

Centre and spread combine into a diagnosis of SHAPE. Data is symmetric when it spreads evenly about its centre; skewed when one tail stretches further than the other. The naming convention follows the TAIL, not the hump: a long right tail is positively skewed, or skewed to the right; a long left tail is negatively skewed.

Two instruments detect skewness. First, compare mean and median. The median only counts heads — it does not care how far the extreme values sit. The mean shares out the total, so a long tail drags it in the tail's direction. Our test marks: the mean is 560 divided by 10, which is 56, while the median is 54. Mean above median — dragged right — signals positive skew, and the culprit is visible: the 84. For symmetric data the two sit essentially together; mean below median signals negative skew. The chant: the mean chases the tail.

Second, read the box plot. In a symmetric dataset the median bar cuts the box near its middle and the whiskers stretch about equally. In our plot, the right whisker is nearly five times the left — the picture shouts what the numbers whispered.

One caution for interpretation questions: skewness is about the SHAPE of the distribution, not about quality. A positively skewed mark distribution means most learners scored modestly while a few scored very high — it is a description, not a verdict. In the exam, justify any skewness claim with evidence: quote mean against median, or describe the box plot, in one written sentence.

The questions on this section are in front of you now — name the tail, compare mean with median, and quote your evidence.

## Subtopic: Identifying Outliers

An outlier is a value implausibly far from the rest of the data. The eye suspects the 84; grade eleven replaces suspicion with a rule. The fences: a value is an outlier if it lies below the lower quartile minus 1,5 times the interquartile range, or above the upper quartile plus 1,5 times the interquartile range.

Apply it. The quartiles were 50 and 58, so the interquartile range is 8, and 1,5 times that is 12. Lower fence: 50 minus 12 is 38 — no mark falls below 38. Upper fence: 58 plus 12 is 70 — and 84 stands far beyond it. So 84 is an outlier by rule, and the sentence to write is exactly that: 84 is greater than 70, the upper fence, therefore 84 is an outlier.

Why fences built from quartiles? Because quartiles are robust — the middle of the data cannot be moved by the very extremes we are testing. Contrast the outlier's effect on our other measures. With the 84, the mean is 56 and the standard deviation works out to about 10,4. Remove it, and the mean of the remaining nine drops to about 52,9 while the standard deviation collapses to about 4,7 — less than half. One value doubled the apparent spread and lifted the centre by three marks. The median, meanwhile, barely moves, and the interquartile range not at all. That is the closing principle of the topic: mean and standard deviation are precise but fragile; median and interquartile range are blunt but robust. When outliers are present, report the robust pair, and say why.

The final questions of this part are with you now — compute the fences, compare each suspect against them, and write the conclusion as an inequality.

# Part 2 — Simplifier

Now the same measures from a taxi rank and a tuck-shop queue — same numbers, same rules, with a picture behind each one.

## Subtopic: Five Landmarks on One Road

Think of the ten test marks as ten houses along one straight road, sorted from the first house at number 44 to the last at number 84. The five number summary is just five landmarks on that road: where the road starts, the quarter mark, the halfway mark, the three-quarter mark, and where it ends.

The box-and-whisker is a map of those landmarks. The box is the stretch between the quarter and three-quarter marks — the middle half of all the houses, the ordinary neighbourhood. The bar inside is the halfway landmark. The whiskers are the roads out to the first and last house. On our map, the neighbourhood is compact — from 50 to 58, eight marks wide — but the road out to the last house runs a long, lonely twenty-six marks. A map like that tells you immediately: almost everyone lives close together, and somebody built a mansion far out of town.

Two ways to measure the road. End to end — the range, 40 — but that measurement is hostage to the mansion; move one extreme house and the whole answer changes. Or measure just the neighbourhood — the interquartile range, 8 — which stays put no matter what gets built at the edges. That is why the box plot pairs so naturally with medians and quartiles: every part of the picture is stable.

Quick check before we carry on — questions on this are with you right now. Read each box plot like a map: where is the neighbourhood, how long are the roads out, and which side stretches?

## Subtopic: The Average Distance from Home

A netball coach wants one number for how CONSISTENT her shooter is. The shooter's five matches: 4, 6, 7, 9, 14 goals, averaging 8. Consistency is about distance from that average — how far each match strayed from home base.

The straight distances are 4 below, 2 below, 1 below, 1 above, 6 above. Try to average them with their signs and you get zero — the belows perfectly cancel the aboves, every single time, for any dataset. The mean is the balance point, so this always happens, and the zero says nothing about consistency.

The fix is to square each distance first. Squaring does two jobs: it makes everything positive so nothing cancels, and it punishes big strays more than small ones — a distance of 6 becomes 36, while three small distances of 1, 1 and 2 together only make 6. Average the squared distances: 58 over 5 is 11,6 — the variance. But 11,6 is in goals SQUARED, a unit no scoreboard shows, so take the square root to come back to real goals: 3,41. That is the standard deviation — the shooter's typical distance from home. A rival shooter averaging 8 with a standard deviation of 1,2 is the safer pick for a final: same class of player, far shorter wanderings.

Your questions for this part are up now — distances from home, squared so they cannot cancel, averaged, then rooted back to real units.

## Subtopic: The Mansion and the Fences

Back on the road of houses, that mansion at 84 needs formal treatment, because eyeballing is not evidence. The rule builds two fences past the neighbourhood, at one and a half neighbourhoods' width beyond each end of the box. Neighbourhood width 8, so one and a half widths is 12: the lower fence stands at 50 minus 12, which is 38, and the upper fence at 58 plus 12, which is 70. Any house past a fence is officially an outlier. The mansion at 84 is well past 70 — verdict delivered, in writing: 84 is beyond the upper fence of 70, so 84 is an outlier.

Why does one mansion matter so much? Watch what it does to each measuring tool. The mean invites every house to share the road's total equally, so the mansion drags the mean from about 53 up to 56 — the average now describes a road most residents do not live on. The standard deviation is even more impressionable, because squaring makes distant houses shout: the mansion alone hoists it from about 4,7 to about 10,4, more than doubling the apparent spread. But the median only counts heads down the line — it barely feels the mansion — and the neighbourhood width does not move at all.

So the topic's closing wisdom: when the data holds an outlier, describe the road with the head-counting tools — median and interquartile range — and say in one sentence why the mean and standard deviation would mislead. Naming the fragile tool and the reason is exactly what interpretation questions pay for.

And here come the last questions of the lesson, right now — build the fences, judge every suspect against them, and choose robust tools when a mansion is on the road.
