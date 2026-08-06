# Part 1 — Expert

Today's work puts a number on uncertainty. Probability is the mathematics of "how likely", and this session builds its two engines: theoretical probability, computed by counting what COULD happen, and relative frequency, measured by counting what DID happen. One ordinary die and one bag of coloured counters run through the whole session, and by the close you will define the vocabulary precisely, compute with both engines, and know exactly when each one is the right tool.

## Subtopic: The Language of Probability

Precision first, because every question in this topic is written in this vocabulary.

An EXPERIMENT is any action with an uncertain result: rolling a die, flipping a coin, drawing a counter from a bag. An OUTCOME is one possible result of that experiment — rolling a 4, say. The SAMPLE SPACE, written S, is the set of ALL possible outcomes. For one roll of an ordinary six-sided die: S contains 1, 2, 3, 4, 5 and 6, and we write n of S equals 6 — the number of outcomes in the sample space. An EVENT, usually written E or A, is the collection of outcomes you care about. The event "rolling an even number" contains 2, 4 and 6, so n of E equals 3.

Every probability lives on a fixed scale, from 0 to 1. Probability 0 means impossible: rolling a 7 on this die. Probability 1 means certain: rolling a number less than 7. Everything uncertain sits strictly between, and the halfway mark, 0,5, means as likely as not. Probabilities may be written as fractions, decimals or percentages — a half, 0,5, and 50 percent are the same statement — but a probability of 1,4, or a negative probability, is meaningless, and writing one in an examination signals a broken calculation. Any answer outside the 0-to-1 scale must send you back to find the error.

Pause here — questions on this section are coming to you now. They test the vocabulary: sample space, event, and the scale that contains every probability ever computed.

## Subtopic: Theoretical Probability

The first engine. When every outcome in the sample space is EQUALLY LIKELY — a fair die, an unbiased coin, a well-shaken bag — the probability of an event is a pure counting exercise. The definition: P of E equals n of E over n of S — the number of outcomes in the event, divided by the number of outcomes in the sample space.

Run it on the die. The probability of rolling an even number: the event holds 2, 4 and 6, so n of E is 3; the sample space holds six outcomes. P equals 3 over 6, which simplifies to a half, or 0,5. The probability of rolling a number greater than 4: the event holds 5 and 6, so P equals 2 over 6, which is a third.

Now the bag, which is this topic's favourite prop. A bag holds 5 red counters, 3 blue and 2 green — ten in total, so n of S is 10. One counter is drawn without looking. P of blue equals 3 over 10 — as a decimal, 0,3. P of red equals 5 over 10, a half. P of red or green equals 7 over 10, because 5 reds and 2 greens make 7 favourable counters.

Two disciplines make these marks safe. First, COUNT the sample space honestly — the equally-likely requirement means counting counters, not colours: there are three colours, but ten counters, and the denominator is 10, never 3. Second, always simplify or convert as the question directs, and keep fractions exact — 3 over 10 is exact; 0,33 for a third is already an approximation.

Stop for this section's questions now. Count the event, count the space, divide — and make sure what you count is equally likely.

## Subtopic: Relative Frequency

The second engine, for the real world, where equal likelihood cannot be assumed. A plastic bottle top is flipped: it can land cap-up or cap-down, but nothing says these are equally likely — the top is not symmetrical. Theory is silent here. The only way in is to EXPERIMENT.

Flip the bottle top 200 times. Suppose it lands cap-up 120 times. The RELATIVE FREQUENCY of cap-up is the number of times the event occurred, divided by the number of trials: 120 over 200, which is 0,6. That number is the experimental probability — the data's estimate of the truth.

The crucial behaviour: relative frequency SETTLES as trials increase. After 10 flips, the result might be 0,8 — small samples swing wildly. After 200 flips, 0,6. After 2 000, perhaps 0,58. The estimate steadies as evidence accumulates. That settling is the observed pattern this topic is built on — more trials give a more trustworthy estimate, and the relative frequency of a fair experiment drifts toward its theoretical value in the long run.

This also explains short-run "misbehaviour" of fair objects. A fair coin flipped 50 times that shows 27 heads has a relative frequency of 0,54 — not 0,5. That is not evidence of bias; it is normal small-sample wobble. Conversely, if 2 000 flips showed 0,7 heads, suspicion would be justified — a large sample sitting far from theory is exactly how a loaded coin or an unfair die is caught.

When to use which engine: symmetric objects with equally likely outcomes — dice, coins, cards, counters — use theoretical probability. Irregular objects and real-world processes — bottle tops, drawing pins, weather, taxi arrivals — use relative frequency from data. And when an experiment on a symmetric object is available, the two engines should roughly agree; a large disagreement indicts the object, not the mathematics.

Pause now for this section's questions — occurrences over trials, and judgement about sample size.

## Subtopic: Complementary Events

The finishing tool, and the greatest shortcut in the topic. The COMPLEMENT of an event A, written "not A", is the event that A does NOT happen — it contains every outcome of the sample space outside A. Rolling a die: if A is "rolling a 6", then not-A is "rolling 1, 2, 3, 4 or 5".

Because A and not-A between them cover the whole sample space and share no outcomes, their probabilities must total exactly 1: P of A plus P of not-A equals 1. Rearranged into its working form: P of not-A equals 1 minus P of A.

Compute with it. P of not rolling a 6: 1 minus a sixth, which is five sixths — no counting of five separate outcomes required. The weather service says the probability of rain tomorrow is 0,3: the probability of no rain is 1 minus 0,3, which is 0,7. From the bag: P of not drawing a green counter is 1 minus 2 tenths, which is 8 tenths, or four fifths — confirm it directly: 5 reds plus 3 blues are 8 non-green counters out of 10. Both roads agree, and the shortcut scales to problems where direct counting is painful.

The pair of properties to quote in theory questions: an event and its complement are mutually exclusive — they cannot both happen — and together they are exhaustive — one of them MUST happen. That is precisely why their probabilities sum to 1. This identity is the workhorse behind every "at least one" question waiting in Grade 11 and 12 — learn it as a reflex now: the phrase "not" or "at least" should trigger the subtraction from 1 before any counting begins.

The compressed method for the whole part: name the sample space and count it; equally likely means divide counts; irregular means run trials and divide occurrences; and the word "not" means 1 minus. The final questions of this part are in front of you now — vocabulary, both engines, and the complement shortcut.

# Part 2 — Simplifier

The same ideas again now, built from a washing line, a bag of sweets and a long afternoon of flipping things. Nothing new arrives: the answers will land on the same halves, thirds and 0,6. What changes is that likelihood will become something you can see and place.

## Subtopic: A Scale From Impossible to Certain

Picture a washing line stretched between two poles. The left pole is labelled IMPOSSIBLE — zero. The right pole is labelled CERTAIN — one. Every event in the universe pegs somewhere on this line, and probability is nothing more than the position of the peg.

Peg some events. "The sun sets this evening" — hard against the right pole, at 1. "A die shows 7" — hard against the left pole, at 0: the die has no 7 to offer. "A newborn baby is a girl" — almost exactly the middle of the line, 0,5: as likely as not. "A die shows an even number" — also mid-line, because three of the six faces are even. "Rain in Cape Town in July" — well right of middle; "rain in the Karoo in July" — well left of middle. Every everyday feeling of "no chance", "maybe", "surely" is a rough peg position; probability just replaces the feeling with a number.

Two consequences follow from the line itself. Nothing pegs left of 0 — you cannot be less likely than impossible. Nothing pegs right of 1 — you cannot be more likely than certain. So when a calculation hands you 1,4 or a negative, the answer is not unusual — it is WRONG, and the line just told you so. Keep the line in your head as a permanent error detector.

Quick check before we carry on — a few questions on the washing line are coming to you right now. Place each event by feel first, then by number.

## Subtopic: Counting Your Way to a Probability

Now the fair-object engine, rebuilt from a bag of sweets. Ten sweets in a packet: 5 red, 3 blue, 2 green. Shake well, close your eyes, take one.

Ask the only two questions that matter. Question one: how many sweets COULD you grab? Ten — every sweet is an equal candidate, because your eyes are closed and the bag is shaken. Question two: how many of those would make you happy, if blue is your colour? Three. Happy grabs over possible grabs: 3 out of 10. That fraction IS the probability — 0,3, a peg just left of the middle of the washing line.

Every fair-object question is these two counts and a divide. Chance of an even roll on a die: six faces could land, three are even — 3 over 6, a half, dead centre on the line. Chance of red or green from the bag: ten candidates, and 5 reds plus 2 greens make 7 happy ones — 7 over 10, well right of middle.

The one trap, and it is the topic's favourite: count THINGS, not TYPES. The bag holds three colours, and the lazy answer says "one colour in three, so a third". But the sweets are the equal candidates, not the colours — 5 reds give red five tickets in the draw, green only two. Denominator 10, always. Whenever a question lists group sizes, the equal candidates are the individuals, and the group sizes are just a fast way of counting them.

Your questions for this section are up now. Two counts and a divide — and count sweets, never colours.

## Subtopic: Try It a Hundred Times

Last idea: what to do when nothing about the object is fair or symmetrical — and why more evidence beats less.

A bottle top is nothing like a die. Flip it: cap-up or cap-down, but its shape is lopsided, so no amount of clever counting predicts the split. When theory cannot count, experience must count instead. Flip it, and flip it, and flip it, writing down what happens. After 200 flips: 120 cap-ups. Experience says: cap-up runs at 120 out of 200 — 0,6. That number, occurrences divided by attempts, is the relative frequency — probability measured instead of reasoned.

Feel why the sample size matters with a smaller story. Flip the top just 5 times and get 4 cap-ups: is cap-up really 0,8? You would not bet on it — five flips is gossip, not evidence. Two hundred flips is a report. Two thousand is an audit. The wobble shrinks as the pile of evidence grows, and the settling value is the object's true tendency showing through. That is also why a fair coin showing 27 heads in 50 flips alarms nobody — short runs wobble — while a coin showing 1 400 heads in 2 000 flips would rightly end the game: big samples do not lie that far from a half.

So carry both engines, and choose by the object. Symmetrical and fair — dice, coins, shaken bags: count and divide, no experiment needed. Lopsided or alive — bottle tops, drawing pins, weather, whether the taxi comes on time: gather data and divide occurrences by attempts. And when you CAN do both, the two answers should shake to the same neighbourhood — theory predicting, experience confirming.

You now hold the whole starter kit of probability: the washing line, the two counts, the flip-and-tally, and the "not" shortcut that subtracts from 1. And here come the final questions of the lesson, right now — place the peg, pick the engine, and trust the counting you have practised. This topic rewards exactly the care you have just given it.
