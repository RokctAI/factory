# Part 1 — Expert

Probability so far has leaned on rules — addition, product, complements, Venn and tree diagrams. Grade twelve adds the engine underneath them all: counting. When outcomes are too many to list, the fundamental counting principle counts them without listing, and probability becomes a ratio of two counts. Four pieces of equipment by the end: the counting principle itself, factorial arrangements with restrictions, codes with and without repetition, and probability computed as favourable count over total count.

## Subtopic: The Fundamental Counting Principle

The principle in one sentence: if one task can be done in m ways, and for EACH of those a second task can be done in n ways, then the two tasks together can be done in m times n ways. Choices multiply — they never add — because every option of the first task opens all the options of the second.

Smallest honest example: 4 shirts and 3 pairs of trousers give 4 times 3, which is 12 outfits — each shirt pairs with each trouser. Add 2 pairs of shoes and multiply again: 24 complete outfits. The principle chains through any number of slots.

The working discipline that carries every question in this topic: draw the slots. One dash per decision, in the order the decisions are made; write above each dash how many options remain when that decision is reached; multiply. A three-course meal with 5 starters, 7 mains and 4 desserts: three slots, 5 times 7 times 4, which is 140 different meals. Nobody lists 140 meals; the slots count them in seconds.

When do numbers ADD instead? Only between scenarios that cannot both happen — mutually exclusive cases, like travelling by taxi OR walking. Multiply along a sequence of decisions; add across alternative worlds. Confusing the two is the topic's foundational error.

Pause here — the questions for this section are with you now. Slots in decision order, options above each, multiply along, add only across exclusive cases.

## Subtopic: Arrangements and the Factorial

Now arrange PEOPLE, where each person used is used up. Six learners line up for a photo: 6 choices for the first position, then 5 remain for the second, 4 for the third, and so on down to 1. The count is 6 times 5 times 4 times 3 times 2 times 1, written 6 factorial with an exclamation mark, which is 720. In general, n distinct objects arrange in n factorial ways. The options shrink by one per slot because arrangement forbids reuse — a person cannot stand in two positions.

Restrictions are handled with one strategy: seat the fussy ones first. If a specific learner must stand at the left end, that slot is forced — 1 way — and the remaining five arrange freely: 5 factorial, 120 line-ups. If two specific learners must stand TOGETHER, glue them into one block: now 5 units arrange in 5 factorial ways, and inside the block the pair swaps in 2 ways, giving 5 factorial times 2, which is 240. If those two must NOT stand together, subtract from the total: 720 minus 240 leaves 480 — counting the complement is often the shortest road.

The slogan version: forced positions first, glue for together, complement for apart. Every arrangement question is one of these three moves, or two of them chained.

Stop for this section's questions now — factorial for free arrangements, and fussy first, glue, or complement when conditions bite.

## Subtopic: Codes, Digits and Repetition

Arrangements use each object once, but codes may reuse symbols, and the FIRST question to ask of any code problem is: is repetition allowed? The slot method handles both answers; only the numbers above the slots change.

A 4-digit PIN from the digits 0 to 9, repetition allowed: four slots, 10 options each, 10 to the power 4, which is 10 000 possible PINs. Repetition forbidden: 10, then 9, then 8, then 7 — the product is 5 040. Same slots, different discipline, nearly half the codes gone.

Restrictions land on specific slots, and restricted slots are filled FIRST. Codes of one letter followed by two different digits, where the letter must be a vowel: 5 choices for the vowel slot, 10 for the first digit, 9 for the second — 5 times 10 times 9, which is 450 codes. A common trap: a number plate or code that may not START with zero — the first slot drops to 9 options while later slots, if repetition is allowed, keep all 10.

Letters of a word arrange like people: the word MATHS has 5 distinct letters, so 5 factorial, which is 120 arrangements. Arrangements beginning with a specific letter force the first slot: 1 way there, 4 factorial for the rest, 24.

Quick pause — the questions on codes are with you now. Ask about repetition first, fill restricted slots first, and let the slot numbers tell the story.

## Subtopic: Probability by Counting

Counting powers probability through one formula: when all outcomes are equally likely, the probability of an event equals the number of favourable outcomes over the total number of outcomes. Both counts come from the machinery just built, and the phrase at random is the licence that all outcomes weigh the same.

Case one. A 4-digit PIN is generated at random, repetition allowed. What is the probability that its digits are all different? Total: 10 000. Favourable: the no-repetition count, 5 040. Probability: 5 040 over 10 000, which is 0,504 — slightly better than half, a result most people find surprisingly high.

Case two. The six learners line up at random. Probability that the two friends stand together? Total: 720. Favourable: the glued count, 240. Probability: 240 over 720, which is one third. And the complement rule rides along free: the probability they are separated is 1 minus one third, two thirds — consistent with the direct count of 480 over 720.

Case three. The letters of MATHS are arranged at random. Probability the arrangement begins with M: forced first slot gives 24 favourable out of 120, which is 0,2 — and the shortcut view agrees: the first letter is one random choice among 5 equally likely letters, so one fifth.

The routine never changes: count the total with slots or factorials, count the favourable with the same tools plus the restriction moves, divide, and simplify. Where a direct count is ugly, count the complement and subtract from 1.

The final questions of this part are with you now — same counting machine, run twice, favourable over total.

# Part 2 — Simplifier

Now the same counting from a school uniform, a class photo and a cellphone PIN — same rules, same answers.

## Subtopic: Outfits From a Small Cupboard

A learner owns 4 shirts and 3 pairs of trousers. How many different outfits? Not 4 plus 3 — every one of the 4 shirts can sit above every one of the 3 trousers, so the answer is 4 times 3, which is 12. Picture the grid: shirts along the top, trousers down the side, one cell per outfit — 12 cells. Add 2 pairs of shoes and every existing outfit doubles: 24. Choices multiply, because each new decision multiplies what already exists.

The all-purpose tool is dashes on paper. One dash per decision, in order; above each dash, the number of options available at that moment; multiply across. Tuck shop lunch: 5 rolls, 7 fillings, 4 drinks — three dashes, 5 times 7 times 4, which is 140 lunches. The dashes do in five seconds what a list would take all afternoon to do.

And the one place plus is correct: separate worlds. If lunch is EITHER a tuck shop combo OR one of 3 home lunchboxes, the worlds cannot mix — 140 plus 3. Multiply along a chain of decisions; add between either-or worlds that never meet.

Quick check before we carry on — questions on multiplying choices are coming to you right now. Dashes in order, options on top, times all the way along.

## Subtopic: The Class Photo and the Glued Friends

Six learners line up for a photo. The photographer fills the line one position at a time: 6 candidates for the first spot, 5 left for the second, then 4, 3, 2, and the last learner walks into the only spot remaining. Six times 5 times 4 times 3 times 2 times 1 — 720 different line-ups, written as 6 factorial. The numbers shrink because people get used up: nobody stands twice.

Now the photographer's headaches, each with a standard cure. Headache one: the head learner must stand at the left end. Cure: place the fussy person first — that spot is settled, 1 way — and the other five fill the rest freely: 120 line-ups. Headache two: two best friends refuse to be separated. Cure: tie them together with invisible string and count them as ONE unit — five units arrange in 5 factorial ways, 120 — then remember the string has two sides: the pair can swap inside the knot, times 2, giving 240. Headache three: those same two must be kept APART. Cure: count the opposite. Total minus together: 720 minus 240 is 480. Counting what you do not want and subtracting is often the cleanest photograph of all.

Your questions for this part are up now. Fussy first, string for together, subtract for apart — and factorial when everyone is free.

## Subtopic: What Are the Chances, Counted

Probability is a fraction of two counts: the outcomes you are hoping for, over all the outcomes possible, when every outcome is equally likely — and at random is the phrase that makes them equally likely. All the machinery of dashes, factorials and glue now runs twice per question: once for the bottom of the fraction, once for the top.

The phone PIN. Four digits, each 0 to 9, chosen at random: dashes give 10 times 10 times 10 times 10 — 10 000 possible PINs. How many have four DIFFERENT digits? Dashes again, options shrinking: 10, 9, 8, 7 — 5 040. So the probability a random PIN has no repeated digit is 5 040 over 10 000: 0,504. Better than a coin flip, which surprises nearly everyone — repeats feel common, but they are the minority.

The photo again. All six line up at random. Chance the two friends land together? Bottom: 720. Top: the glued count, 240. Probability one third. Chance they are separated: the complement, 1 minus a third, two thirds — no new counting needed. And the word MATHS, shuffled at random: 120 arrangements, 24 starting with M, probability 0,2 — which is just the honest observation that the first letter is one fair pick out of five.

The whole topic in one sentence: count the world, count your wish, divide — and when the wish is hard to count, count its opposite and subtract from 1.

And here come the last questions of the lesson, right now: bottom count, top count, one clean fraction.
