# Part 1 — Expert

Until now, statistics has described ONE measurement at a time — marks, masses, waiting times, each with its own mean and spread. Grade twelve moves to pairs: two measurements taken on the same individual, and the question of whether they travel together. Four pieces of equipment by the end: the scatterplot and how to read it, the least squares regression line from the calculator, the correlation coefficient r, and the discipline of prediction — interpolation, extrapolation, and what correlation can never prove.

## Subtopic: Bivariate Data and the Scatterplot

Bivariate data is paired data: two numbers per individual. Six learners record how many practice papers they completed before an assessment and the mark achieved: 2 papers paired with 49 percent, 3 with 52, 4 with 55, 5 with 61, 6 with 63, and 7 papers with 68 percent. The pairing IS the information — shuffle one column and the story is destroyed, even though both columns keep exactly the same numbers.

The scatterplot displays the pairs honestly: the explanatory variable — the one suspected of driving the other — along the horizontal axis, the response variable up the vertical, one dot per individual, and never any joining of dots. Papers completed is explanatory; the mark responds.

Reading a scatterplot is three judgements. Direction: do the dots climb to the right, a positive association, or fall, a negative one? Form: do they run in a straight lane, or bend? Strength: are they packed tightly along the lane, or sprayed loosely? Our six dots climb steadily in a tight, straight lane: strong, positive, linear. Scan also for outliers — a dot far from the lane, say a learner who worked through 7 papers and scored 35, would demand investigation before any line is fitted.

Pause here — the questions for this section are with you now. Pairs on axes, explanatory across, and judge direction, form and strength before touching any formula.

## Subtopic: The Least Squares Regression Line

When the lane is straight, one line summarises it best. Draw any candidate line through the cloud and measure each dot's vertical miss — the residual, actual y minus predicted y. The least squares regression line is the line making the SUM OF THE SQUARES of those misses as small as possible. Squaring stops positive and negative misses cancelling and punishes large misses hardest; least squares means smallest total squared error.

The fitting itself belongs to the calculator. Enter the six pairs in statistics mode, two-variable, and request the coefficients of y hat equals a plus b x. For our data the calculator reports a equal to 40,77 and b equal to 3,83, both correct to two decimals. The equation of the regression line: y hat equals 40,77 plus 3,83 x.

The marks live in the interpretation. The gradient b says: each additional practice paper raises the predicted mark by about 3,83 percentage points. The intercept a says: a learner who completes zero papers is predicted about 41 percent — meaningful here, since zero papers is a real possibility just left of the data. In many data sets the intercept is merely the line's anchor, not a sensible scenario; say so whenever x equals 0 sits far outside the data.

One structural fact worth treasuring: the least squares line always passes through the point x bar with y bar — the mean of x paired with the mean of y. Ours are 4,5 and 58, and indeed 40,77 plus 3,83 times 4,5 lands on 58. That is both a property and a free check of your calculator work.

Stop for this section's questions now — smallest sum of squared vertical misses, calculator for a and b, interpretation in context for the marks.

## Subtopic: The Correlation Coefficient r

The line describes the trend; r describes how faithfully the dots obey it. The correlation coefficient r lives between minus 1 and plus 1. Its sign copies the direction of the line: positive r for an uphill lane, negative for downhill. Its SIZE measures tightness: near 1 or minus 1, the dots hug the line; near zero, the cloud is shapeless and the line summarises almost nothing.

Rough bands for commentary, always reported with direction AND strength: size from about 0,9 upward, very strong; 0,7 to 0,9, strong; 0,5 to 0,7, moderate; 0,3 to 0,5, weak; below 0,3, very weak to none. The calculator delivers r on the same screenful as a and b. For the practice-paper data r is 0,99: a very strong positive linear correlation — papers and marks climb together almost perfectly in a straight lane.

Three cautions guard this number. First, r measures LINEAR association only: dots lying on a perfect curve can return an r near zero, so always look at the scatterplot before quoting r. Second, r carries no units and ignores unit changes — papers to pages leaves r untouched. Third, and heaviest: correlation is not causation. A strong r between two variables does not prove one drives the other. Children's shoe sizes correlate strongly with their reading ability, yet big feet teach nobody to read — age drives both. Comment on association; never claim proof of cause.

Quick pause — the questions on r are with you now. Sign for direction, size for strength, scatterplot first, and no causal claims.

## Subtopic: Prediction, Interpolation and Extrapolation

The payoff of the line is prediction. A learner plans to complete 5,5 papers' worth of practice: y hat equals 40,77 plus 3,83 times 5,5, which is 61,83 — predict about 62 percent. This is interpolation: 5,5 sits comfortably inside the observed range of 2 to 7 papers, where the line has earned its authority.

Now a learner announces 20 practice papers. The arithmetic obliges — 40,77 plus 3,83 times 20 is about 117,34 — and the answer is nonsense: no mark exceeds 100. That is extrapolation, prediction outside the observed range, and it fails because the line's straightness was only ever verified between 2 and 7. Real relationships bend: fatigue, diminishing returns, ceilings. An extrapolated answer must be flagged as unreliable, and an impossible one — above 100 percent — must be rejected outright, and writing that sentence is where the credit sits.

The full working routine, in order: plot or inspect the scatterplot; judge direction, form, strength; if linear, fit y hat equals a plus b x by calculator; quote and interpret b in context; quote r with direction and strength in words; predict only inside the data range; and refuse to convert association into cause. Each step earns its own credit, and the order is the logic.

The final questions of this part are with you now — predict inside the fence, flag anything outside it, and let the scatterplot licence every number you quote.

# Part 2 — Simplifier

Now the same regression and correlation from a tuck shop queue and a pinboard of dots — same rules, same answers.

## Subtopic: Two Numbers Per Person

Measure one thing per person and you get a list: everyone's height, or everyone's mark. Measure TWO things per person, keeping them attached, and you get pairs — and that attachment is bivariate data. Six friends each report practice papers completed and the mark scored: 2 papers with 49, up to 7 papers with 68. The attachment carries the story; tear the columns apart and the story dies, though every number survives.

The scatterplot is the pairs pinned on a board: papers across, marks up, one dot per friend. Across goes the suspected driver — papers completed, the explanatory variable; up goes the outcome — the mark, responding. Dots are never joined: this is not the path of one traveller but a photograph of six separate people.

Reading the photo is three quick judgements, no formulae. Which way does the crowd lean — uphill to the right, or downhill? Does it keep to a straight lane, or curve away? And is it a tight queue or a loose stroll? Our six dots: uphill, straight, tight. One friend far off the lane — 7 papers, 35 percent — would be an outlier with a story of its own, checked before any summarising.

Quick check before we carry on — questions on reading the dots are coming to you right now. Driver across, outcome up, no joining, and lean, lane and tightness before anything else.

## Subtopic: The Line That Owes the Least

Stretch a ruler through the cloud of dots to summarise the trend. Wherever you lay it, every dot sends an invoice: the vertical gap between itself and the ruler — its residual. Some dots bill from above, some from below. The least squares line is the one ruler position with the smallest possible total of SQUARED invoices. Squaring stops the above-bills cancelling the below-bills and makes large invoices punishingly expensive, so the ruler settles where no dot is badly let down.

Finding the ruler's equation is calculator work: statistics mode, enter the six pairs, read off y hat equals a plus b x. Here: y hat equals 40,77 plus 3,83 x. The letters have street meanings. The b, 3,83, is the slope of the ruler: one more practice paper buys about 3,83 more percentage points — b is the price of a paper, paid in marks. The a, 40,77, is where the ruler starts: the predicted mark for zero papers.

And one elegant freebie: the ruler always balances through the average point — mean papers with mean mark, here 4,5 and 58. Like a see-saw pivoting at its centre, the least squares line cannot avoid the heart of the data. Check it: 40,77 plus 3,83 times 4,5 is 58. If your calculator's line misses the balance point, re-enter the data.

Your questions for this part are up now. Squared invoices, smallest total, slope as the price of a paper, and the ruler balancing on the average point.

## Subtopic: How Tight Is the Queue

Two clouds can share the same ruler and tell opposite stories: in one, dots filing neatly along it; in the other, dots milling loosely around it. The correlation coefficient r is the tidiness score. It runs from minus 1 to plus 1. The sign is the lean — plus for uphill, minus for downhill. The size is the discipline of the queue: near 1, dots in single file along the lane; near 0, a crowd with no lane at all.

Our practice-paper data scores r equal to 0,99 — very strong, positive, linear: nearly single file, marching uphill. The words matter as much as the number: always report direction AND strength, in context. And r ships with warning labels. Label one: r only understands straight lanes — a perfect curve can score near zero, so study the photo before trusting the score. Label two: tidiness is not blame. Children's shoe sizes and reading levels queue up beautifully together, but big feet cause no reading — growing older drives both. Strong correlation licenses the sentence, the variables are strongly associated, and never the sentence, one causes the other.

Prediction is the last stop, and it has a fence. Inside the observed range — say 5,5 papers — trust the ruler: about 62 percent. Outside it — 20 papers — the ruler promises 117 percent, and marks stop at 100: the straight lane was only photographed between 2 and 7 papers, and past the photo's edge the road may bend. Predicting inside the fence is interpolation; jumping the fence is extrapolation, and every jump must be flagged as unreliable.

And here come the last questions of the lesson, right now: sign for the lean, size for the queue's discipline, photo before score, and predictions inside the fence only.
