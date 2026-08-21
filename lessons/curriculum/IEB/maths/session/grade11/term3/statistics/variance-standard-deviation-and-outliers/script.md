# Part 1 — Expert

Two classes can post identical averages and still be opposites: one tightly bunched, one scattered to the winds. Measures of centre are blind to that difference — measures of SPREAD were invented for it. This session revises the five number summary and the box-and-whisker diagram, constructs grade eleven's new precision instruments — variance and standard deviation — and then combines centre and spread to diagnose the shape of a dataset and to convict outliers with an exact rule instead of a suspicion.

## Subtopic: The Five Number Summary and the Box-and-Whisker

The running dataset: ten learners' test marks, already sorted — 38, 42, 45, 47, 49, 51, 52, 54, 56, 86.

The five number summary is minimum, lower quartile, median, upper quartile, maximum. Minimum 38, maximum 86. The median of ten values falls between the fifth and sixth: 49 and 51 average to 50. The lower quartile is the median of the bottom five values — 38, 42, 45, 47, 49 — which is the third one, 45. The upper quartile is the median of the top five — 51, 52, 54, 56, 86 — which is 54. The summary reads: 38, 45, 50, 54, 86.

The box-and-whisker diagram lays those five numbers on a scaled line: a box from 45 to 54 with a bar at the median 50, a short whisker reaching left to 38, and a long whisker stretching right all the way to 86. Two spread measures drop straight out. The range, maximum minus minimum, is 48 — but it is governed entirely by the two most extreme values, so one strange mark owns it outright. The interquartile range, upper quartile minus lower, is 54 minus 45, which is 9: the width of the middle half of the class, untouched by whatever happens at the ends. The picture is already talking: the middle half of this class fits inside nine marks, while one whisker runs thirty-two marks to the right. Keep that thought for the final subtopic.

Pause here — the questions for this section are with you now. They build a five number summary and read a box plot: sort first, quartiles are medians of halves, and say what the long whisker suggests.

## Subtopic: Variance and Standard Deviation

The interquartile range ignores the extremes on purpose — but sometimes a spread measure must listen to EVERY value. Enter the standard deviation: loosely, the typical distance of the data from its mean.

The recipe, on a small clean dataset: 3, 5, 8, 10 and 14 — goals scored in five hockey matches. Step one, the mean: the sum is 40, divided by 5 gives 8. Step two, deviations from the mean: minus 5, minus 3, 0, 2 and 6. Notice the deviations sum to zero — data below the mean exactly balances data above — which is precisely why averaging them raw tells you nothing. Step three, square each deviation to destroy the signs: 25, 9, 0, 4 and 36. Step four, average the squares: the sum is 74, divided by 5 gives 14,8. That number is the VARIANCE. Step five, undo the squaring: the square root of 14,8 is about 3,85. That is the standard deviation — a typical match sits nearly four goals from the mean of 8.

Why keep both names? Variance is where the algebra naturally rests, but its units are squared — goals squared appears on no scoreboard. The square root returns to the data's own units, which is why standard deviation is the measure you report. In assessments, show the table: values, deviations, squared deviations, then the two-line finish. Learn your calculator's statistics mode well enough to CHECK the table — the calculator confirms, the table earns the marks.

Stop for this section's questions now — mean, deviations, squares, average, root: five steps in a fixed order.

## Subtopic: Symmetric and Skewed Data

Centre and spread together diagnose SHAPE. Data is symmetric when it spreads evenly around its centre; skewed when one tail reaches further than the other. The naming follows the TAIL, never the hump: a long right tail is positively skewed, or skewed to the right; a long left tail is negatively skewed.

Two instruments detect skew. First, set the mean against the median. The median merely counts heads — it does not care how far away the extremes sit. The mean shares out the total, so a long tail hauls it in the tail's direction. Our test marks: the mean is 520 divided by 10, which is 52, while the median is 50. Mean above median — hauled right — announces positive skew, and the culprit is in plain sight: the 86. Symmetric data parks the two together; mean below median announces negative skew. The chant to remember: the mean chases the tail.

Second, read the box plot. Symmetric data puts the median bar near the middle of its box with whiskers of similar length. Our plot has a right whisker of thirty-two marks against a left whisker of seven — the picture shouts what the numbers whispered.

One caution for interpretation questions: skewness describes SHAPE, not quality. A positively skewed mark distribution says most learners scored modestly while a few scored very high — a description, not a judgement. Whenever you claim skewness, attach evidence in a written sentence: quote mean against median, or describe the whiskers.

The questions on this section are in front of you now — name the tail, compare mean with median, and quote your evidence.

## Subtopic: Identifying Outliers

An outlier is a value implausibly distant from the rest. The eye accuses the 86; grade eleven demands a trial. The fences: a value is an outlier if it lies below the lower quartile minus 1,5 times the interquartile range, or above the upper quartile plus 1,5 times the interquartile range.

Run the trial. The quartiles were 45 and 54, so the interquartile range is 9, and 1,5 times that is 13,5. Lower fence: 45 minus 13,5 is 31,5 — no mark falls below it. Upper fence: 54 plus 13,5 is 67,5 — and 86 stands far outside. So 86 is an outlier by rule, and the sentence to write is precisely that: 86 is greater than 67,5, the upper fence, therefore 86 is an outlier.

Why build fences from quartiles? Because quartiles are robust — the middle of the data cannot be dragged around by the very extremes under investigation. Now watch the outlier's effect on the fragile tools. With the 86 included, the mean is 52 and the standard deviation computes to about 12,5. Remove it, and the mean of the remaining nine drops to about 48,2 while the standard deviation collapses to about 5,5 — less than half. One value more than doubled the apparent spread and lifted the centre by almost four marks. The median, meanwhile, shifts barely at all, and the interquartile range not one bit. That is the topic's closing principle: mean and standard deviation are precise but fragile; median and interquartile range are blunt but robust. When outliers are present, report the robust pair, and say why.

The final questions of this part are with you now — compute the fences, test each suspect against them, and write the verdict as an inequality.

# Part 2 — Simplifier

The same measures again — as landmarks on a road, distances from home, and a mansion that gets put on trial.

## Subtopic: Five Landmarks on One Road

Picture the ten test marks as ten houses along one straight road, sorted from the first house at number 38 to the last at number 86. The five number summary is nothing more than five landmarks on that road: where it begins, the quarter mark, the halfway mark, the three-quarter mark, and where it ends.

The box-and-whisker is the map of those landmarks. The box spans the quarter mark to the three-quarter mark — the middle half of all the houses, the ordinary neighbourhood. The bar inside is the halfway landmark. The whiskers are the roads out to the first and last houses. On our map the neighbourhood is tight — from 45 to 54, nine marks wide — but the road out to the final house runs a long, lonely thirty-two marks. Such a map speaks instantly: nearly everyone lives close together, and somebody has built a mansion far out of town.

Two ways to measure the road. End to end — the range, 48 — but that measurement is hostage to the mansion: relocate one extreme house and the whole answer changes. Or measure only the neighbourhood — the interquartile range, 9 — which stands firm no matter what appears at the edges. That stability is why the box plot keeps company with medians and quartiles: every piece of the picture is steady.

Quick check before we carry on — questions on this are with you right now. Read every box plot like a map: where is the neighbourhood, how long are the roads out, and which side stretches?

## Subtopic: The Average Distance from Home

A hockey coach wants one number for how CONSISTENT her striker is. The striker's five matches: 3, 5, 8, 10, 14 goals, averaging 8. Consistency is a question of distance from that average — how far each match wandered from home base.

The raw distances are 5 below, 3 below, exactly home, 2 above, 6 above. Average them with their signs and the answer is zero — the belows cancel the aboves perfectly, every time, for any dataset, because the mean is the balance point. That zero says nothing about consistency.

The repair is to square each distance first. Squaring does two jobs at once: it makes every term positive so nothing can cancel, and it punishes long wanderings more than short ones — a distance of 6 becomes 36, while distances of 2 and 3 together contribute only 13. Average the squared distances: 74 over 5 is 14,8 — the variance. But 14,8 lives in goals SQUARED, a unit no scoreboard has ever displayed, so take the square root to return to real goals: about 3,85. That is the standard deviation — the striker's typical distance from home. A rival striker also averaging 8 but with a standard deviation of 1,5 is the safer selection for a final: same output, far shorter wanderings.

Your questions for this part are up now — distances from home, squared so they cannot cancel, averaged, then rooted back to real units.

## Subtopic: The Mansion and the Fences

Back on the road of houses, the mansion at 86 must stand trial, because eyeballing is not evidence. The rule erects two fences beyond the neighbourhood, each at one and a half neighbourhood-widths past its end of the box. Neighbourhood width 9, so one and a half widths is 13,5: the lower fence stands at 45 minus 13,5, which is 31,5, and the upper fence at 54 plus 13,5, which is 67,5. Any house beyond a fence is officially an outlier. The mansion at 86 towers past 67,5 — verdict delivered, in writing: 86 is beyond the upper fence of 67,5, so 86 is an outlier.

Why does one mansion matter so much? Watch each measuring tool react. The mean makes every house share the road's total equally, so the mansion hauls the mean from about 48 up to 52 — an average describing a road most residents do not live on. The standard deviation is even more suggestible, because squaring makes distant houses roar: the mansion single-handedly hoists it from about 5,5 to about 12,5, more than doubling the apparent spread. The median, though, just counts heads down the line — it scarcely notices the mansion — and the neighbourhood width does not move at all.

Hence the topic's parting wisdom: when data holds an outlier, describe the road with the head-counting tools — median and interquartile range — and explain in one sentence why the mean and standard deviation would mislead. Naming the fragile tool and the reason is exactly what interpretation questions pay for.

And here come the last questions of the lesson, right now — build the fences, judge every suspect against them, and choose robust tools when a mansion is on the road.
