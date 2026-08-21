# Part 1 — Expert

Every probability tool met so far — addition and product rules, complements, Venn and tree diagrams — sits on top of one quieter skill: counting. The moment outcomes become too numerous to write out, the fundamental counting principle counts them without a list, and a probability collapses into one count divided by another. Four instruments to collect before the end: the counting principle itself, factorial arrangements under restrictions, codes with and without repeated symbols, and probability computed as a favourable count over a total count.

## Subtopic: The Fundamental Counting Principle

Here is the whole principle in a single sentence: if a first task can be completed in m ways, and for EVERY one of those a second task can be completed in n ways, then the pair of tasks together can be completed in m times n ways. Sequential choices multiply — never add — because each way of doing the first task keeps every way of doing the second task alive.

Test it on something small enough to check by hand: 5 shirts and 2 pairs of jeans give 5 times 2, which is 10 outfits, since each shirt sits happily above either pair of jeans. Bring in 3 caps and multiply once more: 30 full outfits. The multiplication chains through as many decisions as the question stacks up.

The working habit that carries this entire topic is the slot diagram. Draw one dash for every decision, in the order the decisions happen; above each dash write how many options survive at that moment; multiply straight across. A canteen meal built from 4 starters, 6 mains and 3 desserts: three slots, 4 times 6 times 3, which is 72 different meals. Nobody writes out 72 meals — the slots deliver the count in seconds.

So when does addition ever appear? Only between scenarios that exclude each other — mutually exclusive routes, like riding the bus OR cycling to school. Multiply along a chain of decisions; add across alternative worlds that can never happen together. Mixing those two operations up is the founding error of the whole topic.

Pause here — the questions for this section are with you now. Slots in decision order, surviving options above each, multiply along the chain, add only across exclusive worlds.

## Subtopic: Arrangements and the Factorial

Next, arranging PEOPLE — and a person, once placed, is used up. Five debaters take their seats in a row: 5 candidates for the first seat, then 4 remain for the second, 3 for the third, 2 for the fourth, and the last debater takes the only seat left. The count is 5 times 4 times 3 times 2 times 1, written 5 factorial with an exclamation mark, which is 120. In general, n distinct objects arrange in n factorial ways. The shrinking numbers are the signature of arrangement: no reuse, because nobody occupies two seats.

Every restriction yields to one master strategy: settle the fussy ones first. If the team captain must sit at the right-hand end, that seat is decided — 1 way — and the remaining four debaters arrange freely in 4 factorial ways, 24 seatings. If two cousins insist on sitting TOGETHER, bind them into a single block: four units now arrange in 4 factorial ways, and inside the block the cousins can swap in 2 ways, so 4 factorial times 2, which is 48. If the cousins must NOT sit together, subtract from the total instead: 120 minus 48 leaves 72 — the complement is frequently the fastest route on the page.

Compressed into a slogan: forced seats first, glue for together, complement for apart. Every arrangement question is one of those three moves, or two of them in sequence.

Stop for this section's questions now — factorial when everyone is free, and fussy first, glue, or complement the moment a condition appears.

## Subtopic: Codes, Digits and Repetition

Arrangements consume each object once, but codes may recycle their symbols — so the FIRST question to interrogate in any code problem is: may symbols repeat? The slot diagram absorbs either answer; only the numbers written above the slots change.

A 5-digit unlock code from the digits 0 to 9, repetition allowed: five slots, 10 options each, 10 to the power 5, which is 100 000 codes. Repetition forbidden: 10, then 9, then 8, then 7, then 6 — a product of 30 240. Identical slots, different discipline, and more than two thirds of the codes vanish.

Restrictions attach to particular slots, and a restricted slot is always filled FIRST. A locker code of one non-zero digit followed by two DIFFERENT letters of the alphabet: 9 choices for the digit slot, then 26 for the first letter and 25 for the second — 9 times 26 times 25, which is 5 850 codes. The classic trap in this family: a code or number plate that may not BEGIN with zero — the opening slot falls to 9 options, while later slots, if repetition is permitted, keep the full 10.

Letters of a word behave exactly like people in a row: the word STAR has 4 distinct letters, so 4 factorial, which is 24 arrangements. Arrangements that must begin with S force the first slot — 1 way — leaving 3 factorial for the rest, 6.

Quick pause — the questions on codes are with you now. Interrogate repetition first, fill restricted slots first, and let the slot numbers narrate the count.

## Subtopic: Probability by Counting

All this counting feeds probability through one formula: when every outcome is equally likely, the probability of an event is the number of favourable outcomes divided by the total number of outcomes. Both numbers come from the machinery just assembled, and the phrase at random is the guarantee that outcomes carry equal weight.

Case one. A 5-digit unlock code is generated at random, repetition allowed. Probability that its digits are all different? Total: 100 000. Favourable: the no-repetition count, 30 240. Probability: 30 240 over 100 000, which is 0,3024 — a little under a third, and smaller than most people expect for only five digits.

Case two. The five debaters seat themselves at random. Probability the two cousins sit together? Total: 120. Favourable: the glued count, 48. Probability: 48 over 120, which is two fifths. The complement comes along free of charge: the probability they are separated is 1 minus two fifths, three fifths — agreeing with the direct count of 72 over 120.

Case three. The letters of STAR are shuffled at random. Probability the arrangement begins with S: the forced first slot gives 6 favourable out of 24, which is 0,25 — and a shortcut confirms it: the opening letter is one fair selection among 4 equally likely letters, so one quarter.

The routine is fixed: count the total with slots or factorials, count the favourable with the same tools plus the restriction moves, divide, simplify. Whenever the direct favourable count turns ugly, count its complement and subtract from 1.

The final questions of this part are with you now — one counting machine, run twice, favourable over total.

# Part 2 — Simplifier

Now the same counting told through a school cupboard, a debate-team photo and a phone unlock code — same rules, same answers.

## Subtopic: Outfits From a Small Cupboard

A learner owns 5 shirts and 2 pairs of jeans. How many different outfits? Not 5 plus 2 — each of the 5 shirts goes with either pair of jeans, so the answer is 5 times 2, which is 10. See it as a grid: shirts across the top, jeans down the side, one cell per outfit — 10 cells. Add 3 caps to the cupboard and every existing outfit triples: 30. Choices multiply, because each fresh decision multiplies everything already built.

The tool for everything is dashes on paper. One dash per decision, in order; above each dash, the number of options alive at that moment; multiply across. Canteen lunch: 4 starters, 6 mains, 3 desserts — three dashes, 4 times 6 times 3, which is 72 lunches. The dashes finish in five seconds what a written list would take the whole break to produce.

And here is the one honest home for plus: separate worlds. If lunch is EITHER one of the 72 canteen combos OR one of 4 lunchboxes brought from home, the two worlds cannot overlap — 72 plus 4, which is 76. Multiply along a chain of decisions; add between either-or worlds that never meet.

Quick check before we push on — questions on multiplying choices are coming to you right now. Dashes in order, options on top, times all the way across.

## Subtopic: The Class Photo and the Glued Friends

Five debaters line up for the team photo. The photographer fills the row one spot at a time: 5 candidates for the first spot, 4 left for the second, then 3, then 2, and the final debater walks into the last gap. Five times 4 times 3 times 2 times 1 — 120 different line-ups, written as 5 factorial. The numbers shrink because people get used up: nobody appears twice in one photograph.

Now the photographer's three headaches, each with its standard cure. Headache one: the captain must stand at the right-hand end. Cure: place the fussy person first — that spot is settled, 1 way — and the remaining four fill the rest freely: 24 line-ups. Headache two: the two cousins refuse to be split up. Cure: tie them together with invisible string and treat them as ONE unit — four units arrange in 4 factorial ways, 24 — then remember the string has an inside: the cousins can swap within the knot, times 2, giving 48. Headache three: the same two must be kept APART. Cure: count the opposite. Total minus together: 120 minus 48 is 72. Counting the photographs you do not want and subtracting often gives the tidiest picture of all.

Your questions for this part are up now. Fussy first, string for together, subtract for apart — and plain factorial when everyone stands free.

## Subtopic: What Are the Chances, Counted

Probability is a fraction built from two counts: the outcomes you are hoping for, over every outcome possible, provided each outcome is equally likely — and at random is the phrase that levels them. All the dashes, factorials and invisible string now run twice per question: once for the bottom of the fraction, once for the top.

The unlock code. Five digits, each 0 to 9, generated at random: dashes give 10 times 10 times 10 times 10 times 10 — 100 000 possible codes. How many use five DIFFERENT digits? Dashes again, shrinking as digits get spent: 10, 9, 8, 7, 6 — 30 240. So the probability a random code repeats no digit is 30 240 over 100 000: 0,3024. Under a third — repeats sneak in more easily than five short digits suggest.

Back to the photo. All five line up at random. Chance the cousins land side by side? Bottom: 120. Top: the glued count, 48. Probability two fifths. Chance they are separated: the complement, 1 minus two fifths, three fifths — no fresh counting needed. And the word STAR, shuffled at random: 24 arrangements, 6 beginning with S, probability 0,25 — which is simply the honest remark that the first letter is one fair pick out of four.

The entire topic in one sentence: count the world, count your wish, divide — and when the wish resists counting, count its opposite and subtract from 1.

And here come the last questions of the lesson, right now: bottom count, top count, one clean fraction.
