# Part 1 — Expert

Statistics until now has described ONE measurement at a time — marks, heights, waiting times, each with its own mean and spread. Grade twelve turns to pairs: two measurements taken on the same individual, and the question of whether they move together. Four pieces of equipment by the end: the scatterplot and how to read it, the least squares regression line from the calculator, the correlation coefficient r, and the discipline of prediction — interpolation, extrapolation, and what correlation does not prove.

## Subtopic: Bivariate Data and the Scatterplot

Bivariate data is paired data: for each individual, two numbers. Six learners record hours studied for a test and the mark achieved: 1 hour paired with 50 percent, 2 with 56, 3 with 60, 4 with 64, 5 with 68, and 6 hours with 74 percent. The pairing is the point — scrambling one column destroys the information even though both columns keep the same numbers.

The scatterplot displays the pairs honestly: the explanatory variable — the one suspected of driving the other — on the horizontal axis, the response variable on the vertical, one dot per individual, and no joining of dots. Hours studied is explanatory; the mark responds.

Reading a scatterplot is three judgements. Direction: do the dots climb to the right, a positive association, or fall, a negative one? Form: do they follow a straight-line lane, or bend? Strength: are they packed tightly along the lane, or scattered loosely? Our six dots climb steadily in a tight, straight lane: strong, positive, linear. Also scan for outliers — a dot far from the lane, like a learner who studied 6 hours and scored 30, would demand investigation before any line is fitted.

Pause here — the questions for this section are with you now. Pairs on axes, explanatory across, and judge direction, form and strength before touching any formula.

## Subtopic: The Least Squares Regression Line

If the lane is straight, one line summarises it best. Draw any candidate line through the cloud and measure each dot's vertical miss — the residual, actual y minus predicted y. The least squares regression line is the line that makes the SUM OF THE SQUARES of those misses as small as possible. Squaring stops positive and negative misses cancelling and punishes big misses hardest; least squares means smallest total squared error.

CAPS puts the fitting itself in the calculator's hands. Enter the six pairs in statistics mode, two-variable, and request the coefficients of y hat equals a plus b x. For our data the calculator reports a equal to 46 exactly and b equal to 4,57 correct to two decimals. The equation of the regression line: y hat equals 46 plus 4,57 x.

The marks are in the interpretation. The gradient b says: for each additional hour studied, the predicted mark rises by about 4,57 percentage points. The intercept a says: a learner who studies zero hours is predicted 46 percent — meaningful here, since zero hours is a real possibility just left of the data. In many data sets the intercept is only the line's anchor, not a sensible scenario; say so when x equals 0 lies far outside the data.

One structural fact, loved by examiners: the least squares line always passes through the point x bar and y bar — the mean of x with the mean of y. Ours are 3,5 and 62, and indeed 46 plus 4,57 times 3,5 lands on 62. That is both a property and a free check of your calculator work.

Stop for this section's questions now — smallest sum of squared vertical misses, calculator for a and b, interpretation in context for the marks.

## Subtopic: The Correlation Coefficient r

The line describes the trend; r describes how faithfully the dots follow it. The correlation coefficient r lives between minus 1 and plus 1. The sign copies the direction of the line: positive r for an uphill lane, negative for downhill. The SIZE measures tightness: near 1 or minus 1, the dots hug the line; near zero, the cloud is shapeless and the line summarises almost nothing.

Rough bands for commentary, always stated with direction AND strength: size from about 0,9 upward, very strong; 0,7 to 0,9, strong; 0,5 to 0,7, moderate; 0,3 to 0,5, weak; below 0,3, very weak to none. The calculator supplies r in the same screenful as a and b. For the study data r is 0,997: a very strong positive linear correlation — hours and marks climb together almost perfectly in a straight lane.

Three cautions guard this number. First, r measures LINEAR association only: dots on a perfect curve can produce an r near zero, so always look at the scatterplot before quoting r. Second, r has no units and does not change when units change — hours to minutes leaves r untouched. Third, and heaviest: correlation is not causation. A strong r between two variables does not prove one drives the other; ice cream sales and drowning numbers correlate strongly, both driven by summer, and no ice cream ban saves swimmers. Comment on association; never claim proof of cause.

Quick pause — the questions on r are with you now. Sign for direction, size for strength, scatterplot first, and no causal claims.

## Subtopic: Prediction, Interpolation and Extrapolation

The payoff of the line is prediction. A learner plans 4,5 hours of study: y hat equals 46 plus 4,57 times 4,5, which is 66,57 — predict about 67 percent. This is interpolation: 4,5 sits comfortably inside the observed range of 1 to 6 hours, where the line has earned its authority.

Now a learner plans 15 hours. The arithmetic obliges — 46 plus 4,57 times 15 is about 114,55 — and the answer is nonsense: no mark exceeds 100. That is extrapolation, prediction outside the observed range, and it fails because the line's straightness was only ever verified between 1 and 6. Real relationships bend: fatigue, diminishing returns, ceilings. An extrapolated answer must be flagged as unreliable, and an impossible one — beyond 100 percent — must be rejected outright, and writing that sentence is where the mark sits.

The full examination routine, in order: plot or inspect the scatterplot; judge direction, form, strength; if linear, fit y hat equals a plus b x by calculator; quote and interpret b in context; quote r with direction and strength in words; predict only inside the data range; and refuse to convert association into cause. Each step is one or two marks, and the order is the logic.

The final questions of this part are with you now — predict inside the fence, flag anything outside it, and let the scatterplot licence every number you quote.

# Part 2 — Simplifier

Now the same regression and correlation from a taxi queue and a line of washing — same rules, same answers.

## Subtopic: Two Numbers Per Person

Measure one thing per person and you get a list: everyone's height, or everyone's mark. Measure TWO things per person, keeping them attached, and you get pairs — that attachment is bivariate data. Six friends each report hours studied and the mark scored: 1 hour with 50, up to 6 hours with 74. The attachment carries the story; tear the columns apart and the story dies, even though every number survives.

The scatterplot is the pairs pinned on a board: hours across, marks up, one dot per friend. Across goes the suspected driver — hours studied, the explanatory variable; up goes the outcome — the mark, responding. Dots are never joined: this is not a graph of a journey but a photograph of six separate people.

Reading the photo is three quick judgements, no formulae. Which way does the crowd lean — uphill to the right or downhill? Does it follow a straight lane or a curve? And is it a tight queue or a loose scatter? Our six dots: uphill, straight, tight. One friend far off the lane — 6 hours, 30 percent — would be an outlier, a story of its own, checked before any summarising.

Quick check before we carry on — questions on reading the dots are coming to you right now. Driver across, outcome up, no joining, and lean, lane and tightness before anything else.

## Subtopic: The Line That Owes the Least

Lay a broomstick through the cloud of dots to summarise the trend. Any position you choose, each dot files a complaint: the vertical gap between itself and the stick — its residual. Some dots complain upward, some downward. The least squares line is the one broomstick position with the smallest possible total of SQUARED complaints. Squaring stops up-complaints cancelling down-complaints and makes big complaints very expensive, so the stick settles where no dot is badly betrayed.

Finding the stick's equation is calculator work: statistics mode, enter the six pairs, read off y hat equals a plus b x. Here: y hat equals 46 plus 4,57 x. The letters have street meanings. The b, 4,57, is the slope of the stick: one more hour of study buys about 4,57 more percentage points — b is the price of an hour, in marks. The a, 46, is where the stick starts: the predicted mark for zero hours of study.

And one elegant fact for free: the stick always balances through the average point — mean hours with mean mark, here 3,5 and 62. Like a see-saw pivoting at its balance point, the least squares line cannot avoid the centre of the data. Check it: 46 plus 4,57 times 3,5 is 62. If your calculator's line misses the balance point, re-enter the data.

Your questions for this part are up now. Squared complaints, smallest total, slope as the price of an hour, and the stick balancing on the average point.

## Subtopic: How Tight Is the Queue

Two clouds can share the same broomstick and tell different stories: in one, dots hugging the stick; in the other, sprayed loosely around it. The correlation coefficient r is the tightness score. It runs from minus 1 to plus 1. The sign is the lean — plus for uphill, minus for downhill. The size is the hug: near 1, dots in single file along the lane; near 0, a crowd milling with no lane at all.

Our study data scores r equal to 0,997 — very strong, positive, linear: almost single file, uphill. The words matter as much as the number: always report direction AND strength, in context. And r comes with warning labels. Label one: r only understands straight lanes — a perfect curve can score near zero, so look at the photo before quoting the score. Label two: tightness is not blame. Ice cream sales and drownings queue up beautifully together every summer, but neither causes the other — the sun drives both. Strong correlation earns the sentence, the variables are strongly associated, and never the sentence, one causes the other.

Prediction is the last stop, with a fence around it. Inside the observed range — say 4,5 hours — trust the stick: about 67 percent. Outside it — 15 hours — the stick predicts 114 percent, and marks stop at 100: the straight lane was only ever photographed between 1 and 6 hours, and beyond the photo's edge the road may bend. Predicting inside the fence is interpolation; jumping the fence is extrapolation, and every jump must be flagged as unreliable.

And here come the last questions of the lesson, right now: sign for the lean, size for the hug, photo before score, and predictions inside the fence only.
