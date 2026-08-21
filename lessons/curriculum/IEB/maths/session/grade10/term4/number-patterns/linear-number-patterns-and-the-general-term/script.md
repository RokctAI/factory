# Part 1 — Expert

This session assembles the single most reusable tool in the number-patterns topic: the general term of a linear pattern. One anchor sequence runs through the whole hour: four, nine, fourteen, nineteen. From it we will extract the rule, write the formula for term n, race forward to term sixty in one line, work backwards from a value to its position, and finish by proving that a chosen number never appears in the sequence at all. Four skills, one formula — and once the formula is built properly, every one of those skills costs a single line of working.

## Subtopic: Finding the Steady Step

A number pattern is an ordered list governed by a rule, and the linear patterns of this topic are the ones that grow or shrink by the same amount at every step. The diagnosis is pure subtraction: take each term and subtract the one before it. Four, nine, fourteen, nineteen: nine minus four gives five, fourteen minus nine gives five, nineteen minus fourteen gives five. Every gap agrees, so the pattern is linear and its constant difference — the letter d — is five. If any single gap disagrees, the label linear is withdrawn and the formula of this lesson may not be used.

Now the language the questions are written in. Each number in the list is a term. T one names the first term, which is four; T two names the second, nine; and T n names the term standing in position n. That last object, T n, is the general term — a formula that accepts any position and returns the term living there. Positions are counting numbers only: first, second, third. Position four and a half does not exist, and that innocent-looking fact will win us a proof later in the lesson.

Falling patterns obey the same test. Fifty, forty-three, thirty-six: forty-three minus fifty is minus seven, and thirty-six minus forty-three is minus seven again. A negative d is entirely respectable — it announces a pattern descending in equal steps of seven. What matters is the direction of the subtraction: always the later term minus the earlier one. Swap the order and the sign flips, and a wrong sign at this stage poisons every later line.

And test every gap you are shown, not merely the first. The list one, three, nine opens with a gap of two, but the next gap is six. That sequence multiplies by three each time — it is not linear, and no amount of hope makes the formula fit it. Three given terms demand two subtractions; five terms demand four. Only when all of them agree may you write down d and move on.

The questions for this section are with you now — gaps subtracted in the correct order, a falling pattern handled, and the multiplying impostor exposed.

## Subtopic: Constructing the Formula for Term n

Every linear pattern's general term has one shape: T n equals d times n, adjusted by a fixed amount. Watch the shape emerge. The multiples of five — five, ten, fifteen, twenty — are the tidiest possible pattern with d equal to five: their general term is simply five n. Our anchor sequence four, nine, fourteen, nineteen takes identical steps of five, but each term sits exactly one below the matching multiple: four is five minus one, nine is ten minus one, fourteen is fifteen minus one. The whole sequence is the five times table slid down by one. Therefore T n equals five n minus one.

The recipe in full generality: read d off the gaps; write d times n; then compute the adjustment by comparing d times one with the actual first term. In symbols the adjustment is T one minus d. Here that is four minus five, which is minus one — and yes, the adjustment is allowed to be negative. Said as a sentence worth memorising: general term equals difference times position, plus first term minus difference.

Then verify, always, against a term the construction did not use. T three ought to be fourteen: five times three minus one is fourteen. Confirmed. That five-second check is the cheapest insurance in the topic, because the only error this recipe ever suffers is a sign slip in the adjustment, and verification exposes it instantly.

Run the recipe on the descending list fifty, forty-three, thirty-six. The difference d is minus seven. Adjustment: fifty minus minus seven, which is fifty-seven. So T n equals minus seven n plus fifty-seven. Check with T two: minus fourteen plus fifty-seven is forty-three. Correct. A negative difference asks for nothing special — only unhurried sign arithmetic.

Why the name linear? Plot position against term value: n equals one against four, two against nine, three against fourteen. The points fall on a perfect straight line whose gradient is d. A linear pattern and a straight-line graph are one idea in two costumes, and questions frequently ask you to say so.

Take this section's questions now — the recipe executed on a rising and a falling pattern, and every formula verified before it is trusted.

## Subtopic: Term Sixty in One Line, and Solving for the Position

A general term is a machine with two directions. Feed in a position and it hands back the term: that is the forward direction. Hand it a term and demand the position: that is the backward direction, where most of the marks live.

Forward first. The sixtieth term of four, nine, fourteen, nineteen: T sixty equals five times sixty minus one — two hundred and ninety-nine. One substitution, one line. The alternative — adding five fifty-nine times — is a full page of arithmetic carrying fifty-nine separate chances to slip, with no built-in check. The general term exists precisely so that position sixty is no harder than position six.

Backward now: which term of the sequence equals one hundred and twenty-four? Set the machine equal to that value and solve. Five n minus one equals one hundred and twenty-four. Add one to both sides: five n equals one hundred and twenty-five. Divide by five: n equals twenty-five. So one hundred and twenty-four is the twenty-fifth term. Notice the shape of the answer: a backward question returns a position, and a position must be a natural number — which sets up the final move.

Is one hundred and sixty-three a term of this sequence? Suppose it is, and chase its position: five n minus one equals one hundred and sixty-three, so five n equals one hundred and sixty-four, so n equals one hundred and sixty-four fifths — thirty-two comma eight. But positions are whole: the sequence has a thirty-second term and a thirty-third term with nothing in between. So the conclusion, written the way markers expect it: one hundred and sixty-three is not a term of the sequence, because n equals one hundred and sixty-four over five is not a natural number. The broken n is not an error in your algebra — the broken n is the proof itself.

Hold the three moves side by side. Forward is substitution. Backward is a one-step linear equation. Membership is the backward move followed by a verdict on whether n landed whole. All three drive through the same formula, which is why constructing T n correctly is always the opening mark of the question.

This section's questions are ready for you — one substitution, one equation, and one membership verdict stated with its reason.

## Subtopic: Hidden Patterns — Triangles, Tables and Call-Out Fees

Examination questions seldom hand over a bare sequence. They wrap the pattern in a diagram or a story, and the skill is unwrapping it back to a first term and a constant difference.

Matchstick triangles in a row. Figure one is a single triangle: three matches. Figure two attaches a second triangle to the first: because they share a side, the total is five matches, not six. Figure three: seven. The sequence three, five, seven has d equal to two — each new triangle borrows one side and contributes only two fresh matches. Adjustment: three minus two is one, so T n equals two n plus one. Figure thirty therefore needs two times thirty plus one — sixty-one matches. The diagram became a formula, and the formula answered a question nobody wants to draw.

Hexagonal tables at a function. One six-sided table seats six. Push two together and the joined edge swallows a seat on each table, leaving ten. Three tables seat fourteen. Sequence six, ten, fourteen; d is four; adjustment six minus four is two; T n equals four n plus two. Fifty guests to seat: four n plus two equals fifty gives four n equals forty-eight, so n equals twelve tables.

Fees and tariffs. A plumber charges a call-out fee of sixty rand plus forty rand per hour; a courier charges a handling fee plus a rate per kilogram. Every such story is T n equals d n plus adjustment, where d is the per-unit rate and the adjustment is the fixed part. Forty rand per hour with a sixty-rand call-out is forty n plus sixty for n hours, and each sub-question collapses to forward, backward, or membership.

Three classic failures, so you can refuse each one. First: miscounting the diagram — the shared match, the swallowed seats. Count at least three figures slowly before writing the sequence. Second: writing T n as d n plus the first term, forgetting to subtract d. The adjustment is first term minus difference, and substituting n equals one catches the mistake in seconds. Third: reporting a position when the question asked for a term, or a term when it asked for a position. Reread the question's final sentence and answer the thing it names.

The final questions of this part are with you now — diagrams unwrapped, stories translated, and each classic failure refused.

# Part 2 — Simplifier

Same topic again, but this time it lives at the post office counter — because a price list that climbs in equal steps is something you have understood since long before algebra had letters.

## Subtopic: The Parcel Price That Climbs Step by Step

A courier prices parcels by whole kilograms. One kilogram costs fourteen rand. Two kilograms: twenty rand. Three kilograms: twenty-six rand. Line the prices up — fourteen, twenty, twenty-six — and listen to the drumbeat: every extra kilogram adds exactly six rand. That steady six is the constant difference d, the heartbeat of the pattern. A list that climbs in identical steps is a linear pattern, and the size of the step is its signature.

How do you check a heartbeat honestly? Subtract neighbours, later minus earlier. Twenty minus fourteen is six. Twenty-six minus twenty is six. Every gap identical — linear confirmed. If four kilograms cost thirty-five rand, that gap would be nine, the rhythm would break, and today's tools would be the wrong tools. Interrogate every gap before you commit.

Patterns can fall too. Think of your phone battery dropping the same percentage every hour of a long trip, or a printing budget shrinking by the same amount each week. Falling in equal steps is still linear — the difference is simply negative — and the direction rule keeps you safe: always subtract the earlier value from the later one, never the reverse.

Names for the positions before we build anything: the one-kilogram price is the first term, the two-kilogram price the second, and the n-kilogram price is the prize we are after — one formula that answers every parcel question without a price chart taped to the wall.

Your questions for this section are ready — find the heartbeat, test every gap, and keep every subtraction pointing the right way.

## Subtopic: A Times Table with a Top-Up

Here is the move that turns a price list into a formula. The six times table — six, twelve, eighteen — is the purest six-step pattern there is. Our prices fourteen, twenty, twenty-six climb by the same six, but each one sits higher than its matching multiple: fourteen is six plus eight; twenty is twelve plus eight; twenty-six is eighteen plus eight. Every price is a multiple of six wearing a top-up of eight. The formula writes itself: price for n kilograms equals six n plus eight.

That is all any general term is: the d times table plus a fixed top-up. The difference comes from the gaps. The top-up is whatever the first term needs beyond one copy of d: first term minus d, fourteen minus six, eight.

Never trust a fresh formula until it reproduces a price you already know. Three kilograms: six times three plus eight is twenty-six — matches the list, so the machine is honest.

Now use its reach. A twenty-kilogram box: six times twenty plus eight — one hundred and twenty-eight rand. No chart, no repeated adding, no arithmetic slip creeping in at step thirteen. One substitution. That is exactly why questions ask for term fifty or term sixty: they are checking whether you own the machine or are still climbing the stairs one price at a time.

And when the question reverses — a customer paid ninety-two rand, how heavy was the parcel? — point the machine backwards: six n plus eight equals ninety-two, so six n equals eighty-four, so n equals fourteen. Fourteen kilograms. Forward is substitution; backward is a small equation. One machine, two directions.

Here are this section's questions — build the top-up formula, test it against a known price, then run it in both directions.

## Subtopic: Can a Parcel Cost Exactly Seventy-Five Rand?

One question style remains — the one that reads strangely until you see its real content: could some parcel cost exactly seventy-five rand? In the language of patterns: is seventy-five a term of the sequence?

Treat it as a backward question and let the algebra pronounce the verdict. Six n plus eight equals seventy-five. Subtract eight: six n equals sixty-seven. Divide: n equals sixty-seven sixths — eleven comma one seven, roughly. The answer is hiding in those decimals. Parcels are priced in whole kilograms only: there is an eleven-kilogram price and a twelve-kilogram price and nothing in between. No parcel costs exactly seventy-five rand. The untidy n is not a blunder — it is the entire proof, and the expected sentence states it: seventy-five is not a term, because n is not a natural number.

Set that against the ninety-two rand parcel from a minute ago: there n came out exactly fourteen, clean and whole, so ninety-two genuinely sits on the price list as the fourteenth term. Whole n means member; broken n means outsider. That one judgement, stated with its reason, earns marks year after year.

The closing checklist for any pattern question, dressed or undressed. One: extract at least three terms and subtract every gap — equal gaps or no linear tools. Two: build the machine — d times n plus the top-up, first term minus d. Three: test the machine on a term you already know. Four: identify the direction — a term from a position is substitution; a position from a term is an equation; membership is that equation plus the whole-number verdict. Five: answer in the units of the story — rand, matches, tables or kilograms — with the reason attached.

Linear patterns return in Grade eleven wearing a changing difference, and in Grade twelve they mature into arithmetic sequences and series. The machine assembled today is the chassis for all of it.

The final questions of the lesson are with you now — verdicts delivered with reasons, and the checklist driven from start to finish.
