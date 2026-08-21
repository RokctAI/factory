# Part 1 — Expert

Grade eleven probability moves past single events and asks how events COMBINE: this or that, this and that, not this, and — the deepest question of all — whether one event shifts the chances of another. This session revises the two probability models, builds the Venn diagram and the addition rule, separates the special vocabulary of mutually exclusive and complementary events, and closes with the definition the whole topic stands on: independence and the product rule.

## Subtopic: Two Models — Relative Frequency and Theoretical Probability

A probability is a number between 0 and 1 attached to an event: 0 for impossible, 1 for certain, everything interesting in between. There are exactly two honest ways to obtain that number.

The theoretical model argues from symmetry. When every outcome of an experiment is equally likely, the probability of an event is the number of outcomes inside the event divided by the total number of outcomes in the sample space. A fair die offers six equally likely faces; the event greater than four holds two of them — five and six — so its probability is two sixths, which is one third. No experiment required — but the model's entry fee is the phrase equally likely, and claiming it for a warped die or for tomorrow's weather is a misuse of the model.

The relative frequency model measures instead of arguing. Repeat the experiment many times and divide the number of occurrences by the number of trials. A courier company logs 250 deliveries and finds 35 arrived late: the relative frequency of lateness is 35 over 250, which is 0,14 — the experimental estimate of the probability. Relative frequency is jumpy over a few trials and steadies as the trials pile up, homing in on the true probability. That steadying is why insurers trust claims records and why a weather service can say 30 percent: both are relative frequencies distilled from enormous data.

The skill under examination is choosing the correct model and saying why: manufactured symmetry — coins, dice, cards, fair spinners — invites theory; messy real-world events demand recorded data.

Pause here — the questions for this section are with you now. They ask which model applies and why: hunt for the words equally likely before you count a single outcome.

## Subtopic: Venn Diagrams and the Addition Rule

Now two events together. In a grade of 150 learners, 75 watch cricket, 60 watch rugby, and 25 watch both. The words or and and are an instruction to draw a Venn diagram: a rectangle for the sample space of 150, two overlapping circles for the events.

The golden rule of filling in: START WITH THE OVERLAP. The intersection — both sports — takes 25. Then subtract outwards: cricket only is 75 minus 25, which is 50; rugby only is 60 minus 25, which is 35. The inner regions hold 50 plus 25 plus 35, which is 110, so the outside — neither sport — is 150 minus 110, which is 40. Every learner now sits in exactly one of four regions, and any question about these events reduces to adding the right regions.

The probability of cricket OR rugby — at least one of the two — is the three inner regions: 110 over 150, which simplifies to 11 over 15. Now watch the naive mistake: adding the circles gives 75 plus 60, which is 135 — too big, because the 25 in the overlap were counted twice, once in each circle. Subtract the double-count exactly once and honesty returns: 75 plus 60 minus 25 is 110.

That correction, translated into probabilities, is the addition rule: the probability of A or B equals the probability of A, plus the probability of B, minus the probability of A and B. It holds for every pair of events without exception. In our numbers: 75 over 150, plus 60 over 150, minus 25 over 150, equals 110 over 150. And the rule is a four-variable machine — hand it any three of its quantities and it solves for the fourth.

Stop for this section's questions now — overlap first, subtract outward, and never count anyone twice.

## Subtopic: Mutually Exclusive and Complementary Events

Two special relationships carry their own names, and questions probe the difference between them relentlessly.

Events are MUTUALLY EXCLUSIVE when they cannot occur together — their circles never touch, and the probability of A and B is zero. For these events the addition rule drops its correction term: the probability of A or B is just the probability of A plus the probability of B. One roll of a die: the events six and less than three share no outcomes, so the probability of one or the other is one sixth plus two sixths, which is three sixths — a half. But this shortened rule is a privilege, not a default: applying it to events that do overlap is precisely the error the full rule exists to block.

Events are COMPLEMENTARY when they are mutually exclusive AND together exhaust the sample space: not-A is everything that A is not. Their probabilities must total 1, so the probability of not-A equals 1 minus the probability of A. The complement is the great labour-saver of probability: the chance of at least one late delivery this week is 1 minus the chance of none at all — one subtraction where a direct attack needs many additions.

Now the distinction. Complementary events are always mutually exclusive, but mutually exclusive events are usually NOT complementary. Six and less than three never happen together — yet the outcomes three, four and five belong to neither event, so the pair leaves part of the sample space uncovered, and their probabilities total a half, not 1. To earn the word complementary, check BOTH conditions: no overlap, and nothing left outside.

The questions on this section are in front of you now — exclusive means no overlap; complementary means no overlap AND nothing left over.

## Subtopic: Independent Events and the Product Rule

The deepest idea of the topic: does one event CHANGE the chances of another? Events A and B are INDEPENDENT when the occurrence of one leaves the other's probability exactly where it was — and the working test is the product rule: A and B are independent precisely when the probability of A and B equals the probability of A times the probability of B.

Some independence is physical. Two coin flips: the coin carries no memory, so heads then heads is a half times a half, which is a quarter. Drawing two cards WITH replacement resets the pack between draws; drawing WITHOUT replacement does not — the first draw rewrites the second's chances, and the events are dependent. That contrast becomes the engine of tree diagrams in the next lesson.

But when events live inside data, independence must be TESTED, never assumed — intuition holds no marks. Back to the grade: is watching cricket independent of watching rugby? The probability of cricket is 75 over 150, which is 0,5; of rugby, 60 over 150, which is 0,4; their product is 0,2. The actual probability of both is 25 over 150, which is about 0,167. The test demands equality, and 0,167 is not 0,2: the events are dependent — the overlap is smaller than independence would predict, so the two audiences lean apart. Write the conclusion with its numbers: since 0,167 differs from 0,2, the events are not independent.

One final guard rail: never confuse independent with mutually exclusive — they sit at opposite poles. Mutually exclusive events destroy each other: if one occurs, the other's probability collapses to zero. So two mutually exclusive events with nonzero probabilities can never be independent. Exclusive is about not overlapping; independent is about not influencing.

The final questions of this part are with you now — multiply the separate probabilities, compare with the true and-probability, and let equality or its failure deliver the verdict.

# Part 2 — Simplifier

The same laws again — now with a drawing pin, two WhatsApp groups, and a coin that refuses to remember anything.

## Subtopic: Guessing from Symmetry or Counting the Tally

Two friends argue about a drawing pin: when it falls, does it land point-up or point-down? One says: two ways to land, so fifty-fifty. The other has spent a week flicking the pin off the desk and keeping score: 200 throws, 122 point-up. Who is doing probability properly?

The first friend is borrowing the theoretical model — and misusing it, because that model has an entry requirement: all outcomes must be EQUALLY LIKELY. A coin earns the assumption through symmetry; a drawing pin, top-heavy with a flat head and a sharp spike, earns nothing. The second friend is using the relative frequency model: run the experiment, count, divide. One hundred and twenty-two over two hundred, 0,61 — no symmetry claimed, only evidence presented.

Both models are legitimate on their own ground. Dice, coins, cards, spinners with equal sectors — symmetric by manufacture — invite theory: favourable outcomes over total outcomes. Late deliveries, rain, match results, pin landings — lopsided and messy — demand a tally. And respect the tally's personality: it is erratic when small and honest when large. Ten throws might say 0,7; a thousand throws settle near the truth. So never trust a tiny tally, and never claim theory without symmetry. One sentence in your answer names the model and the reason: the outcomes are equally likely, so the theoretical model applies — or, the probability is estimated from recorded data by relative frequency.

Quick check before we carry on — questions on this are with you right now. First word of your thinking: symmetric, or tallied?

## Subtopic: Two WhatsApp Groups and the Double-Counted Friends

A learner belongs to two WhatsApp groups: the cricket group with 75 members and the rugby group with 60. How many different people is that? The lazy answer, 135, collapses the moment one person sits in both groups — and 25 do. Those 25 names appear on the cricket list AND on the rugby list, so adding the lists counts each of them twice. The honest headcount: 75 plus 60 minus 25, which is 110 distinct people.

That subtraction IS the addition rule. The probability of belonging to one group or the other equals the probability of the first, plus the probability of the second, minus the probability of both — and the minus has exactly one job: cancelling the double-count in the overlap.

The Venn diagram is simply the two group lists drawn as a picture, and its filling order copies the headcount: start with the people in BOTH groups — the overlap, 25 — then subtract to find cricket-only, 50, and rugby-only, 35, and finally count who is in neither: 150 minus 110 leaves 40 learners outside both circles. Four regions, every person in exactly one, and every question becomes pointing at regions and adding.

When may the minus be skipped? Only when the groups genuinely share nobody — mutually exclusive events, circles that never touch, and-probability zero. And the word complementary demands even more: two groups that share nobody AND between them swallow the entire grade. No overlap plus nothing outside — both checks pass, or the word stays unused.

Your questions for this part are up now — fill the overlap first, and let the minus cancel every double-counted friend.

## Subtopic: The Coin Has No Memory

A coin lands heads four times running. The whole room leans in: tails must be due now. The coin could not care less — it has no memory. The fifth flip is a fresh fifty-fifty, and the itching feeling that a tails is owed has an official name: the gambler's fallacy. Independence is exactly this — one event leaving another's chances untouched. And independent probabilities MULTIPLY: heads then heads is a half of a half, one quarter.

The multiplication has a picture: half of all futures start with heads, and inside THAT half, half continue with heads — a half of a half. Every independent hurdle scales the remaining chance by its own factor.

But most of the world is not a coin. Eat one sweet from a packet without replacing it, and the next draw remembers: the packet has changed. Whether two events influence each other is a question of FACT, and when the events live in data, the product rule is the lie detector. Multiply the two separate probabilities — the rate at which the pair WOULD occur together if the events ignored each other — then compare against how often they actually occur together. Match: independent. Mismatch: dependent. Our grade's data predicted cricket times rugby gives 0,2, but reality delivered 0,167 — a visible gap, and a meaningful one: the two audiences pull away from each other. The test demands equality, not nearness.

Last warning, because questions adore it: mutually exclusive is not independence — it is closer to its opposite. Exclusive events assassinate each other: one happens, and the other is finished. Independence means one happening tells you NOTHING about the other. Exclusive is about overlap; independent is about influence. Keep the two words in separate pockets.

And here come the last questions of the lesson, right now — no memory means multiply, changed circumstances mean dependent, and the product rule settles every argument.
