# Part 1 — Expert

Probability in grade eleven stops being about single events and starts being about how events COMBINE: this or that, this and that, not this, and — most importantly — whether one event changes the chances of another. This session revises the two probability models, masters the Venn diagram and the addition rule, sharpens the special vocabulary of mutually exclusive and complementary events, and finishes with the definition that anchors the whole topic: independence and the product rule.

## Subtopic: Two Models — Relative Frequency and Theoretical Probability

Probability assigns a number between 0 and 1 to an event: 0 for impossible, 1 for certain, and everything meaningful in between. There are two honest ways to get that number.

The theoretical model reasons from symmetry. When all outcomes of an experiment are equally likely, the probability of an event equals the number of outcomes in the event, divided by the total number of outcomes in the sample space. A fair die has six equally likely faces; the event even holds three of them; the probability is three sixths, which is a half. The model's power is that no experiment is needed — but it demands the words equally likely, and claiming it for a loaded die or for whether it rains tomorrow is a misuse.

The relative frequency model measures instead of reasons. Run the experiment many times and divide the number of times the event occurred by the number of trials. A taxi association logs 500 morning trips and finds 60 arrived late: the relative frequency of lateness is 60 over 500, which is 0,12 — the experimental estimate of the probability. Relative frequency wobbles when trials are few and settles as they grow; with enough trials it homes in on the true probability. That settling is why an insurer trusts claim records and why a weather service quotes 30 percent: both are relative frequencies from mountains of data.

The exam skill is choosing the right model and saying so: symmetric objects — coins, dice, cards — invite theory; real-world messy events invite recorded data.

Pause here — the questions for this section are with you now. They ask which model applies and why: look for the words equally likely before you count outcomes.

## Subtopic: Venn Diagrams and the Addition Rule

Now two events at once. In a school of 120 grade elevens, 70 stream music, 50 play online games, and 30 do both. Questions about or and and are begging for a Venn diagram: a rectangle for the sample space of 120, two overlapping circles for the events.

The golden rule of filling in: START WITH THE OVERLAP. The intersection — both — takes 30. Then work outward by subtraction: music only is 70 minus 30, which is 40; gaming only is 50 minus 30, which is 20. The regions so far hold 40 plus 30 plus 20, which is 90, so the outside — neither — is 120 minus 90, which is 30. Every learner now lives in exactly one of four regions, and any question about these events is a matter of adding the right regions.

The probability of music OR gaming — meaning at least one of the two — is the three inner regions: 90 over 120, which is 0,75. But watch what happens if you naively add the circles: 70 plus 50 is 120, which would make or a certainty — wrong, because the 30 in the overlap were counted twice, once inside each circle. Subtract the double-count once and the truth returns: 70 plus 50 minus 30 is 90.

That correction, written in probabilities, is the addition rule: the probability of A or B equals the probability of A, plus the probability of B, minus the probability of A and B. It holds for every pair of events, always. In our numbers: 70 over 120, plus 50 over 120, minus 30 over 120, equals 90 over 120. The rule runs in every direction — given any three of its four quantities, solve for the fourth.

Stop for this section's questions now — overlap first, subtract outward, and never count anyone twice.

## Subtopic: Mutually Exclusive and Complementary Events

Two special relationships earn their own vocabulary, and exams test the difference between them relentlessly.

Events are MUTUALLY EXCLUSIVE when they cannot happen together — their circles do not overlap, and the probability of A and B is zero. For such events the addition rule sheds its correction term: the probability of A or B is simply the probability of A plus the probability of B. One die roll: the events multiple of 4 and odd share no outcomes, so the probability of either is one sixth plus three sixths, which is four sixths, two thirds. This simplification is a privilege, not a default — using the short form for overlapping events is the classic error the full rule exists to prevent.

Events are COMPLEMENTARY when they are mutually exclusive AND exhaust the sample space between them: not-A is everything A is not. The two probabilities must total 1, so the probability of not-A equals 1 minus the probability of A. Complementary events are the great shortcut of probability: the chance that at least one late taxi occurs this week is 1 minus the chance that none does — often one subtraction instead of many additions.

Now the distinction. Complementary events are always mutually exclusive, but mutually exclusive events are usually NOT complementary: multiple of 4 and odd never happen together, yet 2 and 6 belong to neither — the two events do not fill the space, and their probabilities total two thirds, not 1. To claim complementary you must check BOTH conditions: no overlap, and nothing left outside.

The questions on this section are in front of you now — exclusive means no overlap; complementary means no overlap AND nothing left over.

## Subtopic: Independent Events and the Product Rule

The deepest idea in the topic: does one event CHANGE the chances of another? Events A and B are INDEPENDENT when the occurrence of one leaves the probability of the other untouched — and the working test is the product rule: A and B are independent exactly when the probability of A and B equals the probability of A times the probability of B.

Some independence is physical. Two coin flips: the coin has no memory, so the probability of heads then heads is a half times a half, a quarter. Drawing two cards WITH replacement resets the pack; drawing WITHOUT replacement does not — the first draw changes the second's chances, making the events dependent. That contrast returns in force with tree diagrams in the next lesson.

But when events live in data, independence must be TESTED, not assumed — feelings do not count. Return to the school: is streaming music independent of gaming? The probability of music is 70 over 120; of gaming, 50 over 120; their product is 3500 over 14400, which is about 0,243. The actual probability of both is 30 over 120, which is exactly 0,25. Close — but the test demands equality, and 0,243 is not 0,25. The events are dependent: gamers stream slightly more than independence would predict. Write the conclusion with the numbers: since 0,25 differs from 0,243, the events are not independent.

Final guard rail: do not confuse independent with mutually exclusive — they are near opposites. Mutually exclusive events sabotage each other totally: if one happens, the other's probability crashes to zero. So two mutually exclusive events with nonzero probabilities can never be independent. Exclusive is about not overlapping; independent is about not influencing.

The final questions of this part are with you now — multiply the separate probabilities, compare with the actual and-probability, and let the numbers deliver the verdict.

# Part 2 — Simplifier

Now the same rules from a tuck shop and two WhatsApp groups — same numbers, same laws, with a picture that makes each one obvious.

## Subtopic: Guessing from Symmetry or Counting the Tally

Two friends argue about the chance a slice of bread lands butter-side down. One says: two sides, so fifty-fifty. The other has actually dropped bread all month and kept a tally: 100 drops, 63 butter-down. Who is right?

The first friend is using the theoretical model — and misusing it, because that model has an entry requirement: all outcomes must be EQUALLY LIKELY. A coin earns that assumption by symmetry; buttered bread, lopsided and sticky on one face, does not. The second friend is using the relative frequency model: run the experiment, count, divide. Sixty-three over a hundred, 0,63 — no symmetry claimed, just evidence.

Both models are legitimate; each has its home ground. Dice, coins, cards, spinners with equal sectors — symmetric by manufacture — invite theory: count the favourable outcomes over the total. Rain, taxi delays, soccer results, insurance claims — messy and lopsided — demand a tally. And the tally has one behaviour worth respecting: it is jumpy at first and honest in the long run. After 10 drops the tally might say 0,7; after 1000 drops it settles near the truth. So never trust a tiny tally, and never claim theory without symmetry. In the exam, one sentence names your model and your reason: the outcomes are equally likely, so the theoretical model applies — or, the probability is estimated from recorded data by relative frequency.

Quick check before we carry on — questions on this are with you right now. First word of your thinking: symmetric, or tallied?

## Subtopic: Two WhatsApp Groups and the Double-Counted Friends

A learner belongs to two WhatsApp groups: the music group with 70 members and the gaming group with 50. How many different people is that? The lazy answer, 120, is wrong the moment even one person sits in both groups — and 30 do. Those 30 friends appear in the music list AND in the gaming list, so adding the lists counts each of them twice. The honest headcount: 70 plus 50 minus 30, which is 90 distinct people.

That subtraction IS the addition rule. The probability of belonging to one group or the other is the probability of the first, plus the probability of the second, minus the probability of both — the minus exists purely to cancel the double-count in the overlap.

The Venn diagram is just the group lists drawn as a picture, and its filling-in rule mirrors the headcount: start with the people in BOTH groups — the overlap, 30 — then subtract to find music-only, 40, and gaming-only, 20, and finally see who is in neither: 120 minus 90 leaves 30 loners outside both circles. Four regions, every person in exactly one, and any question becomes adding regions.

When do you get to skip the minus? Only when the groups genuinely share nobody — mutually exclusive events, non-overlapping circles, and-probability zero. And the word complementary is stronger still: two groups that share nobody AND between them swallow the whole school. No overlap plus nothing outside — both checks, every time, before the word is used.

Your questions for this part are up now — fill the overlap first, and let the minus cancel every double-counted friend.

## Subtopic: The Coin Has No Memory

A coin comes up heads five times in a row. The crowd leans in: surely tails is now due. The coin disagrees — it has no memory. The sixth flip is a fresh half-half, and the feeling that a tails is owed has a name, the gambler's fallacy. Independence is exactly this: one event leaving another's chances untouched. And for independent events, probabilities MULTIPLY: heads then heads is a half of a half, one quarter.

The multiplication makes sense as a shrinking picture: half the futures have heads first, and of THOSE futures, half have heads again — a half of a half. Each independent hurdle scales the chance down by its own factor.

But most of life is not a coin. Take two sweets from a packet without putting the first back, and the second draw remembers: the packet has changed. Whether events influence each other is a question of FACT, and when the events live in data, the product rule is the lie detector. Multiply the two separate probabilities — the chance the pair would show together IF the events ignored each other — then compare with how often they actually show together. Match: independent. Mismatch: dependent. Our school data said music times gaming predicts 0,243, but reality delivers 0,25 — a small gap, and a real one: the events lean on each other slightly. The test demands equality, not nearness.

Last warning, because exams adore it: mutually exclusive is not independence — it is the opposite of it. Exclusive events assassinate each other: one happens, the other is dead. Independence means one happening tells you NOTHING. Exclusive is about overlap; independent is about influence. Keep those two words in separate pockets.

And here come the last questions of the lesson, right now — no memory means multiply, changed circumstances mean dependent, and the product rule settles every argument.
