# Part 1 — Expert

A single coin or a single die is a simple event, and Grade 8 settled how to find its probability: favourable outcomes over equally likely total outcomes. Grade 9 moves to compound events, two coins, a coin and a die, two dice, two spins of a spinner, two draws from a bag, where the outcomes of two experiments combine. The difficulty is counting: the outcomes multiply, and a careless list misses some or double-counts others. Today we learn two tools that make the counting mechanical and visible, the two-way table for two experiments with few outcomes each, and the tree diagram for experiments in sequence, including the case where the first draw changes the second. By the end you will find probabilities such as the chance of a sum of 7 on two dice and the chance of two reds from a bag without replacement, and justify each with a table or a tree. Grade 10 extends this to Venn diagrams and the addition rule; today we build the foundation.

## Subtopic: Listing Outcomes of Compound Events

Two coins tossed together. Each coin shows heads or tails, so the outcomes of the pair are head-head, head-tail, tail-head and tail-tail: four outcomes, and all four are equally likely, because each coin is fair and the coins do not influence each other. Head-tail and tail-head are different outcomes, the first coin heads and the second tails against the reverse, and treating them as one is the first error of the topic. The probability of two heads is 1 over 4; the probability of exactly one head is 2 over 4, which is a half; the probability of at least one head is 3 over 4.

A coin and a die. The coin has 2 outcomes and the die has 6, so the pair has 2 times 6, which is 12, equally likely outcomes: heads with each of 1 to 6, tails with each of 1 to 6. The probability of heads and a 6 is 1 over 12. The probability of heads and an even number is 3 over 12, which is a quarter. The probability of tails or a 6, meaning either or both, counts the six tails outcomes plus heads-6, which is 7 over 12.

The counting rule behind both: if the first experiment has m equally likely outcomes and the second has n, the compound experiment has m times n equally likely outcomes. Two coins, 2 times 2 is 4; coin and die, 2 times 6 is 12; two dice, 6 times 6 is 36; three coins, 2 times 2 times 2 is 8. The rule is exact only when every outcome of each experiment is equally likely and the experiments do not affect each other.

The sample space is the list of all outcomes, and probability is found by counting favourable outcomes in it over the total. Writing the list in a fixed order, first experiment's outcomes in sequence, second experiment's outcomes under each, prevents omissions. For two coins the list is HH, HT, TH, TT; for the coin and die it is H1 to H6 then T1 to T6. The questions for this section are with you now: the four coin outcomes and why HT differs from TH, the twelve coin-and-die outcomes, the m times n rule, and the three coin-pair probabilities.

## Subtopic: Two-Way Tables for Two Dice

Two dice have 36 outcomes, too many to list comfortably and easy to miscount, so we lay them out in a two-way table: the first die's score 1 to 6 down the side, the second die's score 1 to 6 across the top, and each cell one outcome. The table has 6 rows, 6 columns and 36 cells, all equally likely, each with probability 1 over 36.

Fill each cell with the sum of the two scores. The top left is 2, the bottom right is 12, and the sums run along diagonals: the cells with sum 7 are the six cells from 1 and 6 down to 6 and 1. Count them: the probability of a sum of 7 is 6 over 36, which is 1 over 6. A sum of 2 appears in one cell only, 1 over 36. A sum of 12 likewise, 1 over 36. The sums are not equally likely, which is why a list of eleven possible sums with probability 1 over 11 each is wrong; the table shows that 7 is six times as likely as 2.

Other events are read from the same table. A double, both dice the same, is the main diagonal of six cells, 6 over 36, which is 1 over 6. A sum of at least 10 is the three cells with 10, two with 11 and one with 12, six cells, 1 over 6. A sum of 7 or 11, the winning first roll in some dice games, is 6 plus 2, which is 8 over 36, which is 2 over 9. A sum that is a multiple of 4, meaning 4, 8 or 12, is 3 plus 5 plus 1, which is 9 over 36, which is a quarter.

The table works for any two experiments with few outcomes each: a coin and a die as a 2 by 6 table, two spinners each with four sectors as a 4 by 4 table of 16 cells. It also records real data, as the two-way table of gender and transport did in data handling. From that table of 60 learners, the probability that a learner chosen at random is a girl who uses a taxi is 12 over 60, which is 1 over 5, and the probability that a learner walks is 33 over 60, which is 11 over 20. Your questions on this section are ready: the 36 cells, the six cells of sum 7, why the eleven sums are not equally likely, doubles and sums of at least 10, and the learner table.

## Subtopic: Tree Diagrams and Multiplying Along Branches

When experiments happen in sequence, a tree diagram shows them as branches. From a starting point, one branch for each outcome of the first experiment, labelled with its probability; from the end of each, one branch for each outcome of the second, labelled likewise. Each complete path from the start to a tip is one compound outcome, and its probability is the product of the probabilities along it. The probabilities on the branches leaving any point add to 1, and the probabilities at all the tips add to 1, which is the check.

A spinner is one third red and two thirds blue, and it is spun twice. First spin: red with probability 1 over 3, blue with 2 over 3. From each, the second spin has the same two branches. The four paths are red-red, 1 over 3 times 1 over 3, which is 1 over 9; red-blue, 1 over 3 times 2 over 3, which is 2 over 9; blue-red, 2 over 9; blue-blue, 2 over 3 times 2 over 3, which is 4 over 9. Check: 1 plus 2 plus 2 plus 4 is 9, over 9, which is 1. The probability of one of each colour is red-blue or blue-red, 2 over 9 plus 2 over 9, which is 4 over 9: multiply along a path, add across the paths that make up the event.

A bag holds 3 red and 2 green marbles, and two are drawn without replacement. First draw: red 3 over 5, green 2 over 5. If the first was red, the bag has 2 red and 2 green, so the second is red with 2 over 4 and green with 2 over 4. If the first was green, the bag has 3 red and 1 green, so the second is red with 3 over 4 and green with 1 over 4. The second-draw probabilities depend on the first draw, and the tree records that dependence on its branches. Red-red: 3 over 5 times 2 over 4, which is 6 over 20, which is 3 over 10. Green-green: 2 over 5 times 1 over 4, which is 2 over 20, which is 1 over 10. Different colours: 1 minus 3 over 10 minus 1 over 10, which is 6 over 10, which is 3 over 5; or directly, red-green 6 over 20 plus green-red 6 over 20.

With replacement, the first marble goes back, the bag is unchanged, and the second draw has the same probabilities as the first: red-red is 3 over 5 times 3 over 5, which is 9 over 25, larger than 3 over 10 because the red just drawn is available again. Whether the question says with or without replacement decides the second set of branches, and reading that word is half the question. The questions for this section are ready: the spinner tree with its four tips adding to 1, one of each colour as 4 over 9, the bag without replacement and its changing branches, and 9 over 25 against 3 over 10.

## Subtopic: Choosing the Tool and the Error Museum

The two-way table suits two experiments with few outcomes each, especially when the event depends on combining the two results, such as a sum or a difference on two dice; every cell is visible and the counting is a matter of pointing. The tree diagram suits experiments in sequence, especially when the second depends on the first, as in drawing without replacement, or when there are more than two stages; it carries unequal probabilities on its branches, where the table assumes equally likely cells. A spinner with unequal sectors spun twice needs a tree; two fair dice need a table; a coin and a die work either way. A question that says without replacement is a tree question.

Both tools answer the same kind of question in the same way: identify the outcomes that make up the event, find each one's probability, and add. In a table each outcome is one cell with probability 1 over the number of cells; in a tree each outcome is one path with probability the product along it.

The error museum, five exhibits. Exhibit one: HT and TH counted as a single outcome, giving three equally likely outcomes for two coins and a probability of 1 over 3 for two heads. Exhibit two: the eleven sums of two dice treated as equally likely, 1 over 11 each. Exhibit three: adding along a tree path instead of multiplying, giving 1 over 3 plus 1 over 3 for red-red. Exhibit four: drawing without replacement but leaving the second-draw probabilities unchanged, giving 9 over 25 where 3 over 10 is right. Exhibit five: branch probabilities that do not add to 1 at a point, or tip probabilities that do not add to 1, left unchecked.

Layout for marks: state the sample space size with the m times n rule or draw the table or tree with every branch labelled; identify the favourable cells or paths by circling or listing; write the probability as a fraction, simplified, with the working shown as a product along a path or a count of cells; for an event made of several outcomes, show the addition; and check that the tips add to 1. Probabilities may be left as fractions, or converted to decimals or percentages if asked. The questions for this section are with you now: table against tree, the common method, and the five exhibits.

# Part 2 — Simplifier

Now the same lesson again through writing every way it could happen, a grid for two dice, and branches you multiply along and add across — plain words, same rules.

## Subtopic: Write Every Way It Could Happen

Toss two coins and ask for the chance of two heads. The trick is to write down every way the toss could land before you count anything. Coin one heads and coin two heads. Coin one heads and coin two tails. Coin one tails and coin two heads. Both tails. Four ways, all equally likely, and two heads is one of them: 1 out of 4.

Heads-then-tails and tails-then-heads look alike but are different ways, the way left shoe then right shoe is different from right then left. Squash them into one and you get three ways and a wrong answer of 1 in 3. Exactly one head is two of the four ways, so a half. At least one head is three of the four, so 3 over 4.

A coin and a die together: the coin has 2 ways and the die has 6, so the pair has 2 times 6, which is 12 ways. Heads with a 6 is one of them, 1 over 12. Heads with an even number is heads-2, heads-4, heads-6, three of twelve, a quarter. Tails or a 6 is all six tails ways plus heads-6, seven of twelve.

The shortcut for counting: ways for the first thing times ways for the second thing. Two coins, 2 times 2 is 4. Coin and die, 2 times 6 is 12. Two dice, 6 times 6 is 36. Three coins, 2 times 2 times 2 is 8. It only works when every way of each thing is equally likely and the two things do not interfere with each other. Write the list in a fixed order, first thing's ways in sequence and the second thing's ways under each, so nothing is missed. Your questions on this section are ready: the four ways for two coins, HT against TH, the twelve ways for coin and die, and ways times ways.

## Subtopic: The Dice Grid

Two dice have 36 ways to land, far too many to list without losing one, so draw a grid. First die 1 to 6 down the side, second die 1 to 6 across the top, and every square is one way, each worth 1 over 36.

Write the total of the two dice in each square. The corner squares are 2 and 12. The 7s run on a diagonal from the top right to the bottom left: 1 and 6, 2 and 5, 3 and 4, 4 and 3, 5 and 2, 6 and 1. Six squares, so the chance of a 7 is 6 over 36, which is 1 over 6. A total of 2 is one square, 1 over 36. So the totals are not equally likely, and anyone who says there are eleven totals so each is 1 in 11 has not drawn the grid; 7 is six times as likely as 2.

Read other events straight off the squares. Doubles, both dice the same, are the six squares on the other diagonal: 1 over 6. A total of 10 or more is three squares of 10, two of 11 and one of 12, six squares, 1 over 6. A 7 or an 11 is 6 plus 2, eight squares, 8 over 36, which is 2 over 9. A total that is a multiple of 4 is the 4s, 8s and 12: 3 plus 5 plus 1, nine squares, a quarter.

The grid works for any two things with a handful of ways each: coin and die as 2 by 6, two four-colour spinners as 4 by 4. And it works for real counts too: in the 60-learner table from data handling, a learner picked at random is a girl who takes a taxi with chance 12 over 60, which is 1 over 5, and walks with chance 33 over 60, which is 11 over 20. The questions for this section: 36 squares, the six 7s, eleven totals that are not equal, doubles and 10-or-more, and the learner table.

## Subtopic: Branches: Multiply Along, Add Across

When things happen one after another, draw branches. Start at a dot. One branch for each way the first thing can go, with its chance written on it. From the end of each, one branch for each way the second thing can go. Every path from the start to a tip is one way the whole thing can happen, and its chance is the chances along it multiplied. The branches leaving any dot add to 1, and all the tips together add to 1: that is your check.

A spinner is one third red, two thirds blue, spun twice. First spin: red 1 over 3, blue 2 over 3. Second spin from each: the same. Red-red: 1 over 3 times 1 over 3 is 1 over 9. Red-blue: 2 over 9. Blue-red: 2 over 9. Blue-blue: 4 over 9. Check: 1 plus 2 plus 2 plus 4 is 9 ninths. One of each colour is red-blue or blue-red, so add across those two paths: 4 over 9. Multiply along, add across.

A bag with 3 red and 2 green, two marbles taken out without putting the first back. First: red 3 over 5, green 2 over 5. Now the bag has changed. If red came out, 2 red and 2 green are left, so the second is red 2 over 4 or green 2 over 4. If green came out, 3 red and 1 green are left, so red 3 over 4 or green 1 over 4. Red-red: 3 over 5 times 2 over 4 is 6 over 20, which is 3 over 10. Green-green: 2 over 5 times 1 over 4 is 2 over 20, which is 1 over 10. Different colours: the rest, 1 minus 3 over 10 minus 1 over 10, which is 3 over 5.

Put the first marble back and the bag is as it was, so the second branches match the first: red-red is 3 over 5 times 3 over 5, 9 over 25. The words with replacement or without replacement tell you whether the second set of branches changes, and spotting those words is half the mark. Write every way; grid for two dice; branches for one after another, multiply along, add across, check the tips make 1. The final questions of the lesson are with you now: the spinner tree, 4 over 9 for one of each, the changing bag, and 3 over 10 against 9 over 25.
