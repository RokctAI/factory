# Part 1 — Expert

The laws of probability are already in your hands; today is about the containers that hold them. Genuine questions never arrive as formulae — they arrive as stories: three cultural activities with overlapping members, two sweets pulled from a packet one after the other, a whole school cross-classified in a grid. Each story shape has a tool built for it, and this session masters all three: the three-event Venn diagram, the tree diagram for events in sequence, and the contingency table — finishing with the skill that actually decides your mark: recognising from the wording alone which tool the story wants.

## Subtopic: Venn Diagrams with Three Events

Three overlapping circles slice the rectangle into eight regions: three single-activity regions, three exactly-two overlaps, one centre shared by all three, and the outside. Eight regions could be chaos; the discipline that tames them is one rule scaled up from two circles: START AT THE CENTRE and build outwards.

Here is the worked survey: 120 learners, three activities — choir, drama, chess. Given: 4 do all three; 12 do choir and drama but not chess; 9 do choir and chess but not drama; 7 do drama and chess but not choir; 25 do choir only; 18 drama only; 20 chess only. The centre takes 4. The three exactly-two regions take 12, 9 and 7 — and watch the wording: these arrived as but-not counts, so they enter directly. If a question instead said 12 do choir AND drama, full stop, that count INCLUDES the centre, because the all-three members certainly do both — the region would then get 12 minus 4, which is 8. That one reading decision — does the number swallow the centre or not — decides most three-circle questions.

The single-activity regions take 25, 18 and 20. Add everything placed: 25 plus 18 plus 20 plus 12 plus 9 plus 7 plus 4 gives 95, so the outside — no activity at all — holds 120 minus 95, which is 25.

With the diagram full, every question is a read-off. Probability a random learner does exactly one activity: 25 plus 18 plus 20 is 63, over 120, which simplifies to 21 over 40. At least two activities: 12 plus 9 plus 7 plus 4 is 32, over 120 — 4 over 15. Choir in total: 25 plus 12 plus 9 plus 4 is 50, over 120 — 5 over 12.

Pause here — the questions for this section are with you now. Centre first, read but-not against bare and-counts with care, and audit all eight regions back to the total.

## Subtopic: Tree Diagrams — Events in Sequence

When events happen one after another, the tree diagram takes over, and it earns its keep most when the events are DEPENDENT — when the first stage rewrites the second stage's odds.

The worked example: a packet holds 4 orange and 2 mint sweets; two are drawn, one after the other, without replacement. Stage one branches: orange with probability 4 over 6, mint with 2 over 6. Stage two is where discipline matters, because the second-stage probabilities are CONDITIONAL on the branch you are standing on. After an orange goes, 5 sweets remain, 3 orange and 2 mint: branches 3 over 5 and 2 over 5. After a mint goes, the remaining 5 hold 4 orange and 1 mint: branches 4 over 5 and 1 over 5. Writing those changed numerators and denominators is the entire meaning of without replacement; copying stage one's probabilities onto stage two is the classic error.

Two working rules run the whole tree. MULTIPLY along a path: orange then orange is 4 over 6 times 3 over 5, which is 12 thirtieths — 2 fifths. ADD between paths that satisfy the same event: one of each flavour happens along two different paths — orange then mint, 4 over 6 times 2 over 5, and mint then orange, 2 over 6 times 4 over 5 — each 8 thirtieths, together 16 thirtieths, which is 8 over 15.

Then the audit: the four path products — 12, 8, 8 and 2 thirtieths — must total exactly 1. Mint then mint is 2 over 6 times 1 over 5, which is 2 thirtieths — 1 over 15. All paths sum to 30 thirtieths. If your paths miss 1, some branch is carrying a wrong probability, and the audit points at it before any marker can.

Stop for this section's questions now — condition every second-stage branch on its history, multiply along, add across, and audit to 1.

## Subtopic: Contingency Tables and Testing Independence

The contingency table is the container for two CHARACTERISTICS recorded across one population — gender and transport, sport and grade. One characteristic runs down the rows, the other across the columns, and the totals live in the margins.

The worked table: 160 learners classified by gender and how they arrive at school. Boys: 24 cycle, 36 walk — 60 boys. Girls: 40 cycle, 60 walk — 100 girls. Column totals: 64 cyclists, 96 walkers; grand total 160. Every cell probability is a direct read: the probability a random learner is a boy who cycles is 24 over 160, which is 0,15. Marginals come from the margins: probability of boy is 60 over 160, which is 0,375; probability of cycling is 64 over 160, which is 0,4.

Now the headline question: is gender independent of transport? Run the product test on a cell. Probability of boy times probability of cycling is 0,375 times 0,4, which is 0,15 — and the actual cell reads exactly 0,15. Equality holds, so boy and cycles are independent events; and in a two-by-two table, one passing cell means every cell passes — the two characteristics are independent. See the same fact inside the rows: 24 of the 60 boys cycle, which is 40 percent, and 40 of the 100 girls cycle — also exactly 40 percent. Independence means the cycling rate does not care which row you sit in.

Tilt the data — say 30 boys cycled and only 34 girls — and the rates tear apart: 50 percent for boys against 34 for girls. The product test now fails, 0,1875 in the cell against the expected 0,15, and transport DEPENDS on gender. Identical table shape, opposite verdict — the verdict lives in the numbers, never in the layout.

The questions on this section are in front of you now — margins first, cells as probabilities, and let the product test deliver the verdict.

## Subtopic: Choosing the Tool and Mixing the Rules

The last skill is diagnosis: read the story, name its shape, reach for the matching container.

Overlap language — or, and, only, neither, at least one — with the whole population counted at ONE moment: Venn diagram, two or three circles as the story demands. Sequence language — first, then, one after another, without replacement: tree diagram, second stage conditioned on the first. Two characteristics tabulated over a population — a grid of counts, or a sentence like classified by gender and transport: contingency table, margins first. And wherever the word independent touches data, one response: run the product test and report the verdict with both numbers in the sentence.

Some questions blend a tool with the rules. A netball team plays a final on Saturday. If it is windy, the probability the team wins is 0,35; if it is calm, 0,7. The forecast gives wind a probability of 0,4. Probability the team wins? This is sequence — weather first, result second — so build the tree: windy-and-win is 0,4 times 0,35, which is 0,14; calm-and-win is 0,6 times 0,7, which is 0,42. Winning lives on both paths: add them, 0,56. Multiply along, add across — the tree could not care less whether its stages are sweets or weather.

One closing habit for all three tools: give answers as probabilities in simplest form, and when a question asks for a conclusion — independent or not, more likely or not — write the sentence with the numbers inside it. The tools organise the arithmetic; the sentence banks the marks.

The final questions of this part are with you now — name the story shape, pick its tool, and finish with the sentence.

# Part 2 — Simplifier

The same three tools again — this time as a house with eight rooms, a packet with a memory, and a register at the school gate.

## Subtopic: Eight Rooms, Filled from the Middle

Picture the activities survey as a house with eight rooms. Three big rooms for the loyal members who do one activity only, three shared rooms where two activities meet, one tiny room dead centre for the do-everything heroes, and a stoep outside for learners who do none.

There is exactly one safe order for filling the house: start in the middle room and spread outwards, because the middle is the only room whose number ever arrives clean. Four do all three — four go in the middle, no interpretation required. Then the shared rooms, then the loyal rooms, and whoever remains stands on the stoep: 120 minus the 95 placed inside leaves 25 outside.

The trap waits at the shared rooms' doors. Twelve do choir and drama but not chess — that is a room count, straight in. But twelve do choir and drama, with no but, counts everyone in BOTH activities — including the four heroes in the middle, who obviously do choir and drama too. Then the shared room receives only twelve minus four, which is eight. One small word — only, or but not — decides whether the middle gets subtracted. Hunt for that word and underline it before you place a single number.

Once every room is full, answering means standing in the passage and pointing. Exactly one activity — point at the three loyal rooms: 63 of 120. At least two — point at the four rooms where activities share walls: 32 of 120. The house does the thinking; you point and add.

Quick check before we carry on — questions on this are with you right now. Middle room first, hunt the word only, and audit the whole house back to 120.

## Subtopic: The Sweet Packet Remembers

A packet of six sweets: four orange, two mint. You take one, eat it, take another. The whole point of the tree diagram is a single strange fact: the packet REMEMBERS. Once an orange is gone, the packet holds three orange and two mint — the second draw walks into a different world than the first did. Once a mint is gone, it holds four orange and one mint — a different world again. Without replacement means every branch of the story carries fresh arithmetic, and the tree is nothing more than the story drawn with its worlds attached.

The two moves on the tree are and and or wearing disguises. Following one path — orange, THEN orange — is an and-story, and and multiplies: four sixths of the time the first is orange, and inside that world, three fifths of second draws are orange too. Four sixths times three fifths is two fifths. Wanting one of each flavour is an or-story — orange-then-mint OR mint-then-orange — and or adds the qualifying paths: eight thirtieths plus eight thirtieths is sixteen thirtieths, which is eight fifteenths.

And every tree hands you a receipt. Its full set of paths is every possible future, so the path products must total exactly 1 — thirty thirtieths in our packet. Add them at the end of every tree question: landing on 1 certifies every branch was built honestly; missing 1 points at the broken branch. It is the fastest self-check in the topic, and hardly anyone bothers. Be the one who does.

Your questions for this part are up now — give every branch its new world, multiply along the path, add the paths that qualify, and collect the receipt.

## Subtopic: The Register at the School Gate

Each morning the gate register at a school of 160 records two facts per learner: boy or girl, cycled or walked. Total it up and you are holding the contingency table — gender down the side, transport across the top, margins keeping score: 60 boys, 100 girls, 64 cyclists, 96 walkers.

Reading it is pointing. Probability a random learner is a boy who cycles: the boy-cycle cell over the grand total — 24 over 160. Probability of cycling at all: the cycle column's margin over the total — 64 over 160.

The real question is whether the two facts are CONNECTED: does knowing the gender shift the cycling odds? Interrogate each row on its own. Among the 60 boys, 24 cycle — 40 percent. Among the 100 girls, 40 cycle — 40 percent again. Identical rates: both rows tell one story, gender carries no information about transport, and the product test agrees formally — 0,375 times 0,4 equals the cell's 0,15 exactly. Independent. Now tilt the register — 30 boys cycling against 34 girls — and the rows argue: 50 percent against 34. Knowing the gender now genuinely moves the odds. Dependent, and the product test fails on cue: 0,1875 in the cell against the expected 0,15.

That is everything independence ever means in a table: do the rows tell the same story or different stories? Row percentages for the intuition, the product test for the proof, and a written sentence carrying both numbers for the marks.

And here come the last questions of the lesson, right now — margins first, point at cells, compare the rows' stories, and prove the verdict with one multiplication.
