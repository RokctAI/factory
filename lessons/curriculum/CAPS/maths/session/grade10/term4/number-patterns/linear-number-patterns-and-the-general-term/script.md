# Part 1 — Expert

This session builds the machine behind every number-pattern question in the final paper: the linear pattern and its general term. One exam task carries the whole lesson: given the sequence five, eight, eleven, fourteen — find the general term, use it to compute the fiftieth term, determine which term equals ninety-two, and prove that one hundred never appears in the sequence. Four sub-questions, one formula, and by the end the formula will build itself.

## Subtopic: Spotting the Constant Difference

A number pattern is a list with a rule. The patterns of this topic are the linear ones — the sequences that climb, or fall, in equal steps. The test is mechanical: subtract each term from the one after it. Five, eight, eleven, fourteen: eight minus five is three, eleven minus eight is three, fourteen minus eleven is three. The same answer every time — a constant difference, called d. If even one gap disagrees, the pattern is not linear and this topic's formula does not apply.

The vocabulary that the exam expects. Each entry is a term. Position matters: T one is the first term, five; T two is the second, eight; T n is the term sitting in position n, the general term — the formula that turns any position number into its term. Position n is always a natural number: first, second, third. There is no term two and a half.

Check the difference on falling patterns too. Twenty, seventeen, fourteen: seventeen minus twenty is minus three. A negative d is perfectly legal — it simply means the pattern descends by three each step. The subtraction must always be term after minus term before; reversing the order flips the sign and quietly corrupts everything downstream.

One more discipline: test EVERY gap you are given, not just the first. The sequence two, four, eight looks like it starts with d equals two, but the next gap is four — that pattern multiplies, it does not add, and it belongs to a later grade. Three terms need two subtractions; four terms need three. Only when all the gaps agree do you write d equals three and continue.

This section's questions are with you now — differences computed in the right order, negative steps included, and the non-linear impostor unmasked.

## Subtopic: Building the General Term

The general term of every linear pattern has the same shape: T n equals d times n, plus a correction. Here is where the shape comes from. The multiples of three — three, six, nine, twelve — form the cleanest linear pattern with d equals three: T n equals three n. Our sequence five, eight, eleven, fourteen has exactly the same steps, but every term sits two higher than the matching multiple of three: five is three plus two, eight is six plus two, eleven is nine plus two. The whole sequence is the three times table shifted up by two. So T n equals three n plus two.

The recipe in general: find d from the gaps; write d times n; then compute the correction by asking what must be added to d times one to land on the first term. In symbols, the correction is T one minus d. Here: five minus three is two, so T n equals three n plus two. The full formula worth remembering as a sentence: general term equals difference times position, plus first term minus difference.

Always verify against a term you did not use. T three should be eleven: three times three plus two is eleven. It checks. Verification takes five seconds and catches sign slips, which are the only common failure in this construction.

Run the recipe on the falling pattern twenty, seventeen, fourteen. d is minus three. Correction: twenty minus minus three, which is twenty-three. T n equals minus three n plus twenty-three. Verify with T two: minus six plus twenty-three is seventeen. Correct. Negative differences ride the same recipe with no special treatment — the only demand is careful sign arithmetic.

Why is this called a LINEAR pattern? Because T n equals three n plus two is a straight-line rule: position on one axis, term value on the other, and the points march in a perfect line with gradient d. The pattern topic and the straight-line graph are the same mathematics wearing different clothes — a connection the examiners probe directly.

Take this section's questions now — the recipe run forwards, the verification habit installed, and the falling pattern conquered.

## Subtopic: Forwards to Term Fifty, Backwards to Position n

A general term is a two-way machine. Feed it a position, and it returns the term — that is forwards. Feed it a term, and it reveals the position — that is backwards, and it is where the marks concentrate.

Forwards first. The fiftieth term of five, eight, eleven, fourteen: T fifty equals three times fifty plus two — one hundred and fifty-two. One line. Compare that with the alternative: writing out fifty terms by adding three at a time — a page of arithmetic with fifty chances to slip. The general term exists precisely so that position fifty costs no more effort than position five.

Backwards now: which term of the sequence equals ninety-two? Set the machine equal to ninety-two and solve: three n plus two equals ninety-two. Subtract two: three n equals ninety. Divide: n equals thirty. Ninety-two is the thirtieth term. The answer to a backwards question is a position, so it must come out a natural number — and that requirement powers the final sub-question.

Is one hundred a term of this sequence? Assume it is, and hunt its position: three n plus two equals one hundred, so three n equals ninety-eight, so n equals ninety-eight over three — thirty-two comma six recurring. Positions are whole: there is a thirty-second term and a thirty-third, nothing between. Conclusion, stated in exam language: one hundred is not a term of the sequence, because n equals ninety-eight thirds is not a natural number. The non-whole n is not a failure of your algebra — it IS the proof.

The pattern of the three moves: forwards is substitution; backwards is a linear equation; membership is the backwards move plus a judgement on whether n came out whole. All three run through the same formula, which is why building T n correctly is always the first mark of the question.

This section's questions are ready — one substitution, one equation, and one verdict delivered with its reason.

## Subtopic: Patterns in Disguise — Matchsticks, Tables and Tariffs

The final exam rarely serves a naked sequence. It dresses the pattern in a picture or a story, and the skill is undressing it back to first term and constant difference.

The classic: matchstick figures. Figure one is a single square, four matches. Figure two: two squares side by side — the shared inner stick means seven matches, not eight. Figure three: ten. The sequence four, seven, ten has d equals three, because each new square borrows one wall from its neighbour and brings only three new matches. General term: correction is four minus three, one; T n equals three n plus one. Figure twenty: sixty-one matches. The picture became a formula, and the formula answered a question no one wants to draw.

Tables and chairs: one square table seats four; push two tables together and the joined edge swallows two seats, leaving six; three tables seat eight. Sequence four, six, eight; d is two; correction four minus two is two; T n equals two n plus two. Forty guests: two n plus two equals forty gives n equals nineteen tables.

Tariffs: a taxi charges a flat amount plus a rate per kilometre, a plumber charges a call-out fee plus an hourly rate — every such story is T n equals d n plus correction, where d is the per-unit rate and the correction is the flat part. When a question says a driver charges thirty rand plus twelve rand per kilometre, the pattern for n kilometres is twelve n plus thirty, and every sub-question reduces to forwards, backwards, or membership.

The error museum, three exhibits. Exhibit one: counting the picture wrong — the shared matchstick, the swallowed seats; always count at least three figures carefully before trusting the sequence. Exhibit two: using T n equals d n plus T one, forgetting to subtract d — the correction is first term MINUS difference, and verification exposes the slip instantly. Exhibit three: answering a backwards question with the term instead of the position, or the reverse — read what the question asks for: the value, or the place in the queue.

The final questions of this part are with you now — pictures undressed, stories translated, and every museum exhibit caught before it costs.

# Part 2 — Simplifier

Now the whole topic again, one taxi ride at a time — because you have been computing general terms since the first time you asked what a trip would cost.

## Subtopic: The Taxi Fare That Climbs in Equal Steps

A taxi association prices trips by zone. One zone costs twelve rand. Two zones: nineteen rand. Three zones: twenty-six rand. Write the prices in a row — twelve, nineteen, twenty-six — and feel the rhythm: each extra zone adds exactly seven rand. That steady seven is the constant difference, d. A pattern that climbs in equal steps is a linear pattern, and the step size is its heartbeat.

How would you check the rhythm honestly? Subtract neighbours: nineteen minus twelve, seven. Twenty-six minus nineteen, seven again. Every gap the same — linear confirmed. If a fourth zone cost thirty-five rand, the gap would be nine, the rhythm would be broken, and none of today's tools would apply. Always listen to every gap before naming the beat.

And the direction of subtraction matters like direction on a road: always the later price minus the earlier one. A pattern can also fall in equal steps — airtime draining, a data bundle shrinking by the same amount each day — and then the difference is negative. The tools do not change; only the sign does.

Positions get names: the one-zone price is the first term, the two-zone price the second, and the n-zone price is what we are hunting — a formula that answers any zone question without listing every price on the wall.

Your questions for this section are ready — find the heartbeat, check every gap, and mind the direction of every subtraction.

## Subtopic: The Times Table Wearing a Jacket

Here is the trick that turns the price list into a formula. The seven times table — seven, fourteen, twenty-one — is the purest seven-step pattern in mathematics. Our fares, twelve, nineteen, twenty-six, climb by the same seven but sit somewhere else: twelve is seven plus five; nineteen is fourteen plus five; twenty-six is twenty-one plus five. Every fare is the matching multiple of seven, wearing a jacket of five. The formula writes itself: fare for n zones equals seven n plus five.

That is all a general term ever is: the d times table, shifted by a fixed jacket. Find d from the gaps. The jacket is whatever the first term needs beyond d itself: first term minus d, twelve minus seven, five.

Test the formula the way you would test a stranger's promise: against a price you already know. Three zones: seven times three plus five, twenty-six. It matches the list, so the machine is trustworthy.

Now feel the power. Fifteen zones, right across the city: seven times fifteen plus five — one hundred and ten rand. No listing, no adding seven fifteen times, no error creeping in at step eleven. One substitution. That is why examiners ask for term fifty: they are testing whether you own the machine or are still climbing the staircase one step at a time.

And when the question runs the other way — a passenger paid sixty-one rand, how many zones? — set the formula equal to sixty-one: seven n plus five equals sixty-one, so seven n equals fifty-six, so n equals eight. Eight zones. Forwards is substitution; backwards is a small equation. Same machine, both directions.

Here are this section's questions — build the jacket formula, test it on a known fare, then drive it both ways.

## Subtopic: Is Ninety on the Price List?

One question style remains, and it is the one that looks strangest until you see what it really asks: could a trip cost exactly ninety rand? In pattern language: is ninety a term of the sequence?

Treat it as a backwards question and let the algebra deliver the verdict. Seven n plus five equals ninety. Subtract five: seven n equals eighty-five. Divide: n equals eighty-five over seven — twelve comma one four and change. And there is the answer, sitting in the decimals: zones come in whole numbers only; there is a twelve-zone trip and a thirteen-zone trip and nothing in between. No trip costs exactly ninety rand. The messy n is not a mistake — it is the proof, and the exam wants it stated: ninety is not a term, because n is not a natural number.

Contrast with sixty-one from a moment ago: n came out exactly eight, whole and clean, so sixty-one sits proudly on the price list as the eighth term. Whole n means member; broken n means outsider. That single judgement is worth marks every single year.

The closing checklist for any pattern question, story or sequence. One: extract at least three terms and check every gap — equal gaps or no linear tools. Two: build the machine — d times n plus the jacket, first term minus d. Three: test it on a term you know. Four: read what is wanted — a term from a position is substitution; a position from a term is an equation; membership is an equation plus the whole-number verdict. Five: answer the actual question in its own words — rand, matches, tables or zones, with the reason attached.

Linear patterns return in Grade 11 with a changing difference, and in Grade 12 they power arithmetic sequences and series — the machine you built today is the foundation of all of it.

The final questions of the lesson are with you now — verdicts with reasons, and the checklist running start to finish.
