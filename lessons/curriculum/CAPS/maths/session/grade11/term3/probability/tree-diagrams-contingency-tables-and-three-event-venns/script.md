# Part 1 — Expert

Last lesson built the laws; this one builds the machinery. Real probability questions arrive as stories — three sports codes with overlapping squads, two sweets drawn one after the other, two hundred learners cross-classified in a table — and each story shape has a tool designed for it. This session masters the three tools of grade eleven probability: the three-event Venn diagram, the tree diagram for events in sequence, and the contingency table, ending with the skill the examination really tests — choosing the right tool from the wording alone.

## Subtopic: Venn Diagrams with Three Events

Three overlapping circles cut the rectangle into eight regions: three single-code regions, three exactly-two overlaps, one centre where all three meet, and the outside. Eight regions demand discipline, and the discipline is the same as before, scaled up: START AT THE CENTRE and work outwards.

The worked survey: 150 learners, three sports — soccer, netball, athletics. Given: 5 play all three; 15 play soccer and athletics but not netball; 10 play soccer and netball but not athletics; 8 play netball and athletics but not soccer; 30 play soccer only; 22 netball only; 25 athletics only. The centre takes 5. The three two-code regions take 15, 10 and 8 — and note the wording carefully: these were given as exactly-two counts, so they go straight in. If a question instead says 15 play soccer AND athletics, that count INCLUDES the centre, and the region gets 15 minus 5, which is 10. That single reading decision — does the number include the centre or not — is where three-circle questions are won and lost.

The single-code regions take 30, 22 and 25. Sum everything placed: 30 plus 22 plus 25 plus 10 plus 15 plus 8 plus 5 gives 115, so the outside — no sport — holds 150 minus 115, which is 35.

Now the diagram answers anything. The probability a random learner plays exactly one code: 30 plus 22 plus 25 is 77, over 150. At least two codes: 10 plus 15 plus 8 plus 5 is 38, over 150, which simplifies to 19 over 75. Soccer in total: 30 plus 10 plus 15 plus 5, which is 60, over 150 — two fifths.

Pause here — the questions for this section are with you now. Centre first, read exactly-two against and-counts with care, and audit the eight regions against the total.

## Subtopic: Tree Diagrams — Events in Sequence

When events happen one after another, the tree diagram is the tool, and its power is greatest when the events are DEPENDENT — when the first stage changes the second stage's chances.

The worked example: a packet holds 3 red and 2 blue sweets; two are drawn, one after the other, without replacement. Stage one branches: red with probability 3 over 5, blue with 2 over 5. Now stage two — and here the tree earns its keep, because the second-stage probabilities are CONDITIONAL on the branch you sit on. After a red is taken, 4 sweets remain, 2 red and 2 blue: the branches are 2 over 4 and 2 over 4. After a blue, the remaining 4 hold 3 red and 1 blue: branches 3 over 4 and 1 over 4. Writing the changed denominators is the whole point of without replacement; copying stage one's probabilities onto stage two is the classic error.

The two working rules. MULTIPLY along a path: red then red is 3 over 5 times 2 over 4, which is 6 twentieths — 3 tenths. ADD between paths that satisfy the same event: one of each colour happens along two different paths — red then blue, 3 over 5 times 2 over 4, and blue then red, 2 over 5 times 3 over 4 — each 6 twentieths, together 12 twentieths, which is 3 fifths.

The audit: the four path products — 6, 6, 6 and 2 twentieths — must total exactly 1. Blue then blue is 2 over 5 times 1 over 4, which is 2 twentieths — one tenth. All paths sum to 20 twentieths. If your paths do not total 1, a branch probability is wrong somewhere, and the audit finds it before the marker does.

Stop for this section's questions now — condition every second-stage branch on its history, multiply along, add across, and audit to 1.

## Subtopic: Contingency Tables and Testing Independence

The contingency table is the tool for two CHARACTERISTICS recorded across one population — gender and transport, grade and cellphone ownership. Rows for one characteristic, columns for the other, and totals along the margins.

The worked table: 200 learners classified by gender and how they get to school. Boys: 30 walk, 50 take taxis — 80 boys. Girls: 45 walk, 75 take taxis — 120 girls. Column totals: 75 walkers, 125 taxi riders; grand total 200. Every cell probability is a straight read: the probability a random learner is a boy who walks is 30 over 200, which is 0,15. Marginal probabilities come from the margins: probability of boy is 80 over 200, which is 0,4; probability of walking is 75 over 200, which is 0,375.

Now the marquee question: is gender independent of transport? Apply the product test to a cell. Probability of boy times probability of walking is 0,4 times 0,375, which is 0,15 — and the actual cell gives exactly 0,15. Equality holds, so the events boy and walks are independent; and in a two-by-two table, if one cell passes the test, every cell passes — the two characteristics are independent of each other. Notice the structure inside the numbers: 30 out of 80 boys walk, which is 37,5 percent, and 45 out of 120 girls walk — also exactly 37,5 percent. Independence means the walking rate does not care which row you are in.

Change the data slightly — suppose 40 boys walked and only 35 girls — and the walking rates become 50 percent for boys against about 29 percent for girls: the product test fails, 0,2 against 0,15, and transport now DEPENDS on gender. Same table shape, opposite verdict — the verdict lives in the numbers, never in the layout.

The questions on this section are in front of you now — margins first, cells as probabilities, and let the product test speak.

## Subtopic: Choosing the Tool and Mixing the Rules

The final skill is diagnosis. Read the story, identify its shape, reach for the matching tool.

Overlap language — or, and, only, neither, at least one — with everyone counted at the SAME moment: Venn diagram, two circles or three as the story demands. Sequence language — first, then, drawn without replacement, one after another: tree diagram, with second-stage branches conditioned on the first. Two characteristics tabulated across a population — a grid of counts, or a sentence like classified by gender and transport: contingency table, margins first. And the word independent anywhere near data means one thing: run the product test and report the verdict with both numbers.

Some questions mix tools with rules. A soccer team plays Saturday. If it rains, the probability the team wins is 0,4; if it stays dry, 0,65. The forecast says rain with probability 0,3. Probability the team wins? This is sequence — weather, then result — so tree: rain-and-win is 0,3 times 0,4, which is 0,12; dry-and-win is 0,7 times 0,65, which is 0,455. Win happens along both paths: add, 0,575. Multiply along, add across, exactly as with the sweets — the tree does not care whether the stages are sweets or weather.

One closing habit for every tool: state answers as probabilities in simplest form, and when a question asks for a conclusion — independent or not, more likely or not — write the sentence, with the numbers in it. The tools organise the arithmetic; the sentence collects the marks.

The final questions of this part are with you now — name the story shape, pick its tool, and finish with the sentence.

# Part 2 — Simplifier

Now the same three tools from a kota shop, a school gate and a taxi rank — same numbers, same verdicts, with a picture that chooses the tool for you.

## Subtopic: Eight Rooms, Filled from the Middle

Think of the three-sport survey as a house with eight rooms. Three big rooms for the loyal single-sport players, three shared rooms where two codes meet, one small room in the very middle for the all-three heroes, and a stoep outside for everyone who plays nothing.

Filling the house has one safe order: start in the middle room and work outwards, because the middle is the only room whose number ever arrives clean. Five play all three — five go in the middle, no interpretation needed. Then the shared rooms, then the loyal rooms, and whoever is left stands on the stoep: 150 minus the 115 placed inside leaves 35 outside.

The reading trap lives at the shared rooms' doors. Fifteen play soccer and athletics but not netball — that is a room count, straight in. But fifteen play soccer and athletics, with no but, counts everyone in BOTH codes — including the five heroes in the middle room, who also play soccer and athletics. Then the shared room gets only fifteen minus five. One little word — only, or but not — decides whether you subtract the middle. Read for it every time; underline it on the paper.

Once the rooms are full, every question is a matter of standing in the passage and pointing: exactly one code — point at the three loyal rooms, 77 of 150. At least two — point at the four rooms where codes share walls, 38 of 150. The house does the thinking; you just point at rooms and add.

Quick check before we carry on — questions on this are with you right now. Middle room first, hunt the word only, and audit the whole house back to 150.

## Subtopic: The Sweet Packet Remembers

A packet of five sweets: three red, two blue. You take one, eat it, take another. Here is the thing the tree diagram exists to capture: the packet REMEMBERS. After a red goes, the packet holds two red and two blue — the second draw faces a different world than the first did. After a blue goes, it holds three red and one blue — a different world again. Without replacement means every branch of the story carries its own new arithmetic, and the tree is simply the story drawn with its worlds attached.

The two moves on the tree are and and or in disguise. Following one path — red, THEN red — is an and-story, and and multiplies: three fifths of the time the first is red, and in that world, two quarters of the second draws are red too. Three fifths times two quarters is three tenths. Wanting one of each colour is an or-story — red-then-blue OR blue-then-red — and or adds the separate paths: six twentieths plus six twentieths gives three fifths.

And the tree carries its own receipt. The full set of paths is every possible future, so their probabilities must total exactly 1 — twenty twentieths in our packet. Add your path products at the end of every tree question: hitting 1 proves the branches were built honestly; missing it points straight at the broken branch. It is the quickest self-check in the entire topic, and almost nobody uses it. Be the one who does.

Your questions for this part are up now — give every branch its new world, multiply along the path, add the paths that qualify, and collect the receipt.

## Subtopic: The Register at the School Gate

Every morning the gate register at a school of 200 records two facts per learner: boy or girl, walked or taxi. That register, totalled up, is the contingency table — a grid with gender down the side, transport across the top, and the margins keeping the running totals: 80 boys, 120 girls, 75 walkers, 125 riders.

Reading it is pure pointing. Probability a random learner is a boy who walks: the boy-walk cell over the grand total — 30 over 200. Probability of walking at all: the walk column's margin over the total — 75 over 200.

The interesting question is whether the two facts are CONNECTED: does knowing the gender change the walking chances? Interrogate the rows separately. Among the 80 boys, 30 walk — 37,5 percent. Among the 120 girls, 45 walk — 37,5 percent again. Identical rates: the rows tell one story, gender carries no information about transport, and the product test confirms it formally — 0,4 times 0,375 equals the cell's 0,15 exactly. Independent. But tilt the data — 40 boys walking against 35 girls — and the rows split apart, 50 percent against 29: now the register says knowing the gender genuinely shifts the walking odds. Dependent, and the product test fails on cue, 0,2 against 0,15.

That is all independence ever is in a table: do the rows tell the same story or different stories? Percentages within rows for the intuition, the product test for the proof, and a written sentence with both numbers for the marks.

And here come the last questions of the lesson, right now — margins first, point at cells, compare the rows' stories, and prove the verdict with one multiplication.
