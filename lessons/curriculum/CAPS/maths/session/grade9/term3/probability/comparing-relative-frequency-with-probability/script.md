# Part 1 — Expert

Last lesson calculated probabilities and counted relative frequencies; this lesson puts them in the same table and asks why they disagree. The CAPS instruction is to compare relative frequency with probability and explain possible differences, and the explanation is one of the most useful ideas in all of statistics. A fair coin has a probability of one half for heads, yet 50 tosses gave 27 heads, a relative frequency of 0.54. Is the coin unfair, or is that simply what chance looks like? We set the two side by side for coins, dice and marbles, separate the differences caused by chance variation from those caused by bias in the equipment or the method, watch the relative frequency settle towards the probability as the number of trials grows, and use relative frequency to estimate probabilities that no calculation can give, such as the chance that the morning taxi is late. The error museum at the end collects the beliefs about luck that this lesson is designed to correct.

## Subtopic: Relative Frequency Against Probability

The probability of an outcome is a theoretical value, fixed by the structure of the experiment before any trial is run. The relative frequency is an observed value, produced by a particular set of trials, and a different set of trials produces a different value. Comparing them means writing both in the same form, as decimals or percentages, and looking at the size and direction of the difference.

A fair coin was tossed 50 times and landed heads 27 times. Probability of heads: 0.5. Relative frequency: 27 over 50, which is 0.54. The difference is 0.54 minus 0.5, which is 0.04, or 4 percentage points, in the direction of more heads. In counts, the expected number of heads was 0.5 times 50, which is 25, and the observed number was 27, two more than expected.

The die from last lesson was rolled 60 times with frequencies 8, 11, 9, 12, 10 and 10 for the faces 1 to 6. The probability of each face is 1 over 6, about 0.167, and the expected frequency of each is 10. The relative frequency of a 1 was 8 over 60, about 0.133, below the probability; of a 4, 12 over 60, which is 0.2, above it; of a 5 and a 6, 10 over 60, exactly equal. The differences between observed and expected counts were negative 2, plus 1, negative 1, plus 2, 0 and 0, and they add to zero, because the observed and expected counts both total 60.

The bag of 5 red, 3 blue and 2 yellow marbles was used for 50 draws with replacement and gave 22 red, 18 blue and 10 yellow. Probabilities: 0.5, 0.3 and 0.2. Relative frequencies: 22 over 50, which is 0.44; 18 over 50, which is 0.36; 10 over 50, which is 0.2. Red came up less often than predicted, blue more often, yellow exactly as predicted.

The comparison table has five columns: outcome, probability, expected frequency, observed frequency, relative frequency, and a sixth for the difference if the question asks for it. It makes the pattern visible at a glance: the relative frequencies are close to the probabilities but rarely equal to them, and the differences go in both directions. The next section explains why. The questions for this section are with you now: the coin's 0.54 against 0.5, the die's six comparisons, the marbles, and the differences that add to zero.

## Subtopic: Why Results Differ: Chance Variation and Bias

There are two kinds of reason for a difference between relative frequency and probability, and a good explanation names the right one.

The first is chance variation. Each trial of a random experiment is unpredictable, and the outcomes do not take turns. In 50 tosses of a fair coin, 25 heads is the single most likely result, yet its probability is only about 11 percent; results between 20 and 30 heads are all ordinary. Chance variation is unavoidable, it goes in either direction, it does not mean that anything is wrong, and it is relatively large when the number of trials is small. The coin's 27 heads, the die's 8 ones and 12 fours, and the marbles' 22 reds are all well within the range that chance produces, so the correct explanation for each is chance variation.

The second is bias, a systematic cause that pushes the results in one direction every time. Bias can lie in the equipment: a die with a chipped corner or a weighted face, a bent coin, a spinner whose sectors are not truly equal or whose pointer sticks, a bag in which the marbles differ in size so that the larger ones are grabbed more often. Bias can lie in the method: placing the die rather than throwing it, a spinner flicked so gently that it turns only a little from where it started, not shaking the bag, not replacing the marble, or recording results carelessly, such as a 6 written as a 9. Bias does not shrink as the number of trials grows; it persists.

The way to tell the two apart is to look at the size of the difference against the number of trials, and to repeat the experiment. A die rolled 600 times has an expected frequency of 1 over 6 times 600, which is 100, for each face. Chance variation in 600 rolls usually keeps each face within about 18 of 100. If a 6 came up 160 times, a relative frequency of about 0.267 against a probability of about 0.167, the gap of 60 is far too large for chance, and the honest conclusion is that the die or the throwing method is probably biased towards 6. If a 6 came up 108 times, the gap of 8 is ordinary, and the die gives no reason for suspicion.

So the explanation for a difference is written in three parts: the size of the difference, whether it is large or small for the number of trials, and the cause, chance variation for a small difference and possible bias, named specifically, for a large or persistent one. The fix differs too: more trials reduce the effect of chance, while bias must be found and removed. Your questions on this section are ready: chance variation in 50 tosses, the sources of bias in equipment and method, the die with 160 sixes in 600 rolls, and the three-part explanation.

## Subtopic: More Trials, Closer Relative Frequencies

The most important property of relative frequency is what happens as trials accumulate: for a fair experiment, the relative frequency settles closer and closer to the probability. This is sometimes called the law of large numbers, and it is why relative frequency is a trustworthy estimate when the number of trials is large and a shaky one when it is small.

A class tossed a coin and recorded the running total of heads. After 10 tosses there were 7 heads, a relative frequency of 0.7. After 50 tosses, 27 heads, 0.54. After 100, 46 heads, 0.46. After 500, 258 heads, 0.516. After 1000, 512 heads, 0.512. Plotted on a broken-line graph with the number of tosses on the horizontal axis and the relative frequency on the vertical, the line swings widely at first, then wanders less and less, and hugs the horizontal line at 0.5 more closely the further right it goes.

Look carefully at what settles and what does not. The gap between the relative frequency and the probability shrank: 0.2 after 10 tosses, 0.04 after 50, 0.016 after 500, 0.012 after 1000. But the gap between the number of heads and the expected number did not shrink: it was 2 after 10 tosses, 2 after 50, 4 below after 100, 8 above after 500 and 12 above after 1000. The coin did not correct its early excess of heads by producing extra tails. The count gap can drift and even grow, but it is divided by an ever larger number of trials, so its effect on the relative frequency fades. The relative frequency approaches the probability by dilution, not by compensation.

Pooling results is the practical way to get many trials. Thirty learners each tossing a coin 20 times produce 600 tosses between them; each learner's relative frequency may be anywhere from about 0.3 to 0.7, but the class total, combined in one table, will very likely give a relative frequency between about 0.46 and 0.54. Individual results scatter; combined results settle.

The practical rule follows. When a relative frequency is used to estimate a probability, state the number of trials, because 7 heads in 10 and 512 in 1000 deserve very different levels of trust. And when a relative frequency differs from a probability, ask whether there were enough trials for the difference to mean anything before suspecting bias. The questions for this section are ready: the running table of tosses, the shrinking gap in relative frequency, the count gap that grows, and pooling a class's results.

## Subtopic: Estimating Probability from Data and the Error Museum

Many real probabilities cannot be calculated, because the outcomes are not equally likely and no symmetry argument applies. For these, a relative frequency from a large number of trials or observations is the estimate, and this is how insurers, weather services and sports coaches actually work.

A learner recorded whether the morning taxi arrived late on 40 school days; it was late on 6. The estimated probability of a late taxi is 6 over 40, which is 0.15. Over a school year of 200 days, the prediction is 0.15 times 200, which is about 30 late days, a useful number for a family deciding whether to leave earlier. Rain fell on 9 of the 30 days of April last year, a relative frequency of 0.3, so the estimated probability of rain on an April day is about 0.3. A bottle cap was thrown 300 times and landed top up 105 times, a relative frequency of 0.35; in 1000 throws about 350 top-up landings are expected.

Every such estimate carries its basis and its caution: the number of trials, and the assumption that the conditions stay the same. The taxi estimate assumes the route, the season and the traffic are similar next term; the April estimate assumes this April resembles last April, which one year of data cannot guarantee. More observations strengthen the estimate; changed conditions weaken it.

The error museum, five exhibits. Exhibit one: expecting the relative frequency to equal the probability in a small experiment, and declaring a coin unfair because it gave 27 heads in 50 tosses. Exhibit two: the gambler's fallacy, believing that after several heads a tail is more likely, or that a die is due a 6. Exhibit three: believing that the count of heads must even out exactly, when only the relative frequency settles and the count gap may grow. Exhibit four: estimating a probability from a handful of trials, such as 3 successes in 5 giving 0.6, without saying that 5 trials is far too few. Exhibit five: blaming chance for a large, persistent difference, such as 160 sixes in 600 rolls, or blaming bias for a small one, such as 27 heads in 50.

Layout for marks on a comparison question: write the probability and the relative frequency in the same form, state the difference and its direction, judge whether it is large or small for the number of trials, name the cause, chance variation or a specific bias, and say what further trials would show. The questions for this section are with you now: the taxi, the rain and the bottle cap, the basis and caution of an estimate, and the five exhibits.

# Part 2 — Simplifier

Now the same lesson again through what should happen against what did happen, luck that evens out slowly, and the data as the only judge — plain words, same rules.

## Subtopic: What Should Happen and What Did Happen

Probability is what should happen. Relative frequency is what did happen. Put them next to each other and they are close, but almost never equal.

A fair coin should land heads half the time. Tossed 50 times, it landed heads 27 times. Should: 25. Did: 27. As fractions of the tosses: should 0.5, did 0.54. Close, two more heads than expected.

A die should give each face 10 times in 60 rolls. One class got 8, 11, 9, 12, 10 and 10. Some faces a little over, some a little under, two spot on. The overs and unders cancel out, because both lists add up to 60.

So why the difference? Usually just luck. Each toss is a surprise, and surprises do not line up neatly. In 50 tosses, getting exactly 25 heads only happens about one time in nine; anything from 20 to 30 is ordinary. But sometimes the difference is a sign of a problem. A chipped or weighted die, a bent coin, a spinner that sticks, or a sloppy method, like placing the die instead of throwing it or not shaking the bag, pushes the results the same way every time. That is called bias.

How do you tell luck from bias? Size. A die rolled 600 times should give about 100 sixes, and luck usually keeps it within about 18 of that. 108 sixes: luck. 160 sixes: something is wrong with the die or the throwing. Your questions on this section are ready: should against did, the 27 heads, luck against bias, and the die with 160 sixes.

## Subtopic: Luck Evens Out Slowly

Here is the magic of doing more tries. The more times you toss the coin, the closer the fraction of heads creeps to one half.

A class kept a running count. After 10 tosses, 7 heads: 0.7, way off. After 50, 27: 0.54. After 100, 46: 0.46. After 500, 258: 0.516. After 1000, 512: 0.512. Draw it as a line and it zigzags wildly at the start, then calms down and hugs the one-half line.

But watch the trick. The fraction gets closer to one half, yet the number of extra heads did not shrink at all: 2 extra after 10 tosses, 12 extra after 1000. The coin never paid back its early heads with bonus tails. The extra 12 just became tiny compared with 1000 tosses. Luck evens out by being drowned, not by being cancelled.

That is why a class should pool its results. Thirty learners each tossing 20 times is 600 tosses together. One learner's fraction could be 0.3 or 0.7; the whole class's fraction will very likely land between about 0.46 and 0.54. And it is why you always say how many tries you did: 7 out of 10 and 512 out of 1000 are not equally believable. The questions for this section: the running count, the fraction that settles, the extra heads that do not disappear, and pooling.

## Subtopic: When Only the Data Can Tell

Some chances you can never work out on paper. Is the morning taxi late? There are no six equal faces to count. The only way is to watch and record. A learner noted the taxi for 40 school days and it was late on 6: a chance of about 6 out of 40, which is 0.15. Over 200 school days, expect about 30 late mornings, so it might be worth leaving earlier.

Rain on 9 of last April's 30 days gives about 0.3 for an April day. A bottle cap thrown 300 times landing top up 105 times gives about 0.35, so in 1000 throws expect about 350.

Two cautions go with every estimate like these. Say how many tries it came from, because 6 out of 40 is a start but 60 out of 400 would be stronger. And say what you are assuming stays the same: the same route and traffic for the taxi, a similar April for the rain.

And clear out the myths. A coin is not unfair because it gave 27 heads in 50. After a run of heads, tails is not due. The count of heads does not have to even out; only the fraction settles. Five tries is far too few to judge anything. And a big gap that keeps happening is not just luck. Should against did; luck evens out slowly; when there is no formula, the data is the judge. The final questions of the lesson are with you now: the taxi estimate, the two cautions, and the five myths.
