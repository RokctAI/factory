# Part 1 — Expert

An arithmetic sequence grows by addition. Its twin grows by multiplication, and swapping the operation changes everything: this is the mathematics behind compound interest, price inflation, breeding populations and decaying isotopes. This session assembles the geometric sequence piece by piece: the ratio test that certifies membership, the general term with its exponent, the algebra of geometric means and hidden variables, and the modelling questions where the world multiplies.

## Subtopic: The Constant Ratio Test

A geometric sequence is a list in which every term equals the previous term times one fixed number. That fixed number is the common ratio, written r, and division exposes it: any term divided by its predecessor. Take 3; 12; 48; 192. Twelve over three is 4. Forty-eight over twelve is 4. One hundred and ninety-two over forty-eight is 4. Constant quotient, so the sequence is geometric with r equal to 4.

The same two disciplines as the arithmetic world apply, translated from subtraction into division. Direction: r is the later term over the earlier one, never the reverse. Persistence: a single matching quotient proves nothing. The list 2; 6; 18; 36 opens geometric — 6 over 2 is 3 and 18 over 6 is 3 — then collapses, because 36 over 18 is 2. Check the quotient along the whole list.

The ratio owes you no favours. It may be a fraction: 162; 54; 18; 6 has r equal to one third, and the sequence decays instead of growing. It may be negative: 5; minus 10; 20; minus 40 has r equal to minus 2, and the signs alternate forever. What r may never be is zero, and no term of a geometric sequence may be zero — one zero would poison every division after it and destroy the test itself.

Pause here — the questions for this section are with you now. Divide neighbour by neighbour, check the quotient more than once, and treat fractions, negatives and decay as full citizens.

## Subtopic: The General Term T n Equals a r to the Power n Minus One

Watch the terms assemble. T1 is a. T2 is a times r. T3 is a times r squared. T4 is a times r cubed. The exponent on r trails the position by one — same logic as the arithmetic case, because the first term is a starting point, not a multiplication. So T n equals a times r to the power n minus one.

Forwards first. For 3; 12; 48; 192, T n equals 3 times 4 to the power n minus one. Certify it on a visible term: T4 should be 192, and 3 times 4 cubed is 3 times 64, which is 192. Now term eight: 3 times 4 to the seventh. Four to the seventh is 16 384, so T8 is 49 152. Feel the scale — multiplication leaves addition far behind almost immediately, and that runaway character defines this whole topic.

Backwards next. Which term of the sequence equals 3072? Set 3 times 4 to the power n minus one equal to 3072, so 4 to the power n minus one equals 1024. Recognise 1024 as 4 to the fifth — drive both sides to the same base, the exponential-equation skill from earlier grades. Then n minus one is 5 and n is 6: the number 3072 is the sixth term.

Finally, recovering a and r from two given terms. Suppose T2 is 10 and T5 is 80. Then a r equals 10, and a r to the fourth equals 80. DIVIDE the equations — division does for geometric sequences what subtraction does for arithmetic ones — and a vanishes: r cubed equals 8, so r is 2 and a is 5. Read the picture: from position two to position five is three multiplications, and the value grew eightfold — two, cubed. The general term is T n equals 5 times 2 to the power n minus one, and the check on the other fact gives T5 equal to 5 times 16, which is 80. Confirmed.

Stop for this section's questions now — build the general term, prove it on a term you can see, and when two terms are given, divide them and read off a power of r.

## Subtopic: Geometric Means and Unknowns in the Terms

Three consecutive terms of a geometric sequence obey one law: the ratio across the first pair equals the ratio across the second. Cross-multiply and it becomes the workhorse — the middle term squared equals the product of its two neighbours. That is the geometric counterpart of equal gaps.

Worked case. The terms x; x plus 4; x plus 6 are consecutive terms of a geometric sequence — find x. Middle squared equals neighbour product: the quantity x plus 4, squared, equals x times the quantity x plus 6. Expand: x squared plus 8 x plus 16 equals x squared plus 6 x. The squares cancel, leaving 2 x equal to minus 16, so x is minus 8. Substitute back — always — and the terms are minus 8; minus 4; minus 2. Divide both ways: minus 4 over minus 8 is a half, and minus 2 over minus 4 is a half. A legitimate geometric sequence with r equal to one half, living entirely below zero, which the definition happily allows.

Geometric means are the inserted numbers that make a list multiply evenly. Insert two geometric means between 5 and 320. Two insertions make 5 the first term and 320 the fourth, so 320 equals 5 times r cubed, giving r cubed equal to 64 and r equal to 4. The sequence is 5; 20; 80; 320, and the means are 20 and 80. Count multiplications as means plus one — two means, three jumps.

One caution the marker rewards: when r emerges from an even root, two signs survive. If r squared equals 16, then r is 4 or minus 4, and each sign builds its own honest sequence. Present both unless the question closes the door — for instance by declaring every term positive.

The questions on this section are in front of you now — middle squared equals neighbour product, substitute back to inspect the real terms, and honour both signs when an even root delivers the ratio.

## Subtopic: Multiplication Models the World

Geometric sequences surface wherever change is proportional to current size: money earning interest, prices inflating, bacteria dividing, medication concentrations fading, a dropped ball losing a fixed fraction of its height. Translation asks the familiar three questions. Starting value: a. Multiplier per step: r. And is the target a term's value or a position?

Worked case. A ball is dropped from 10 metres, and every bounce reaches four fifths of the height before it. The heights run 10; 8; 6,4; and so on — a geometric sequence with a equal to 10 and r equal to 0,8. The height after the third bounce is T4 in sequence language, because the drop height occupies position one. T4 equals 10 times 0,8 cubed. Now 0,8 cubed is 0,512, so T4 is 5,12 metres. The off-by-one danger here bites hard: decide in writing whether the starting value is term one, and the exponent will behave.

Second case, growth. A culture of 400 bacteria doubles every hour, so after n hours the count is 400 times 2 to the power n — with this story the natural index starts at zero hours, and the exponent simply counts doublings. After eight hours: 400 times 256, which is 102 400. The meta-lesson: pick the indexing that fits the story, declare it, and never switch midstream.

Percentages become ratios in a single move: growth of 5 percent each year means r equal to 1,05; decay of 12 percent means r equal to 0,88. The ratio is one plus or one minus the rate — the very object the finance chapters will call one plus i later in the year.

The final questions of this part are with you now — name the multiplier, commit the indexing to paper, and convert every percentage to its ratio before the formula sees it.

# Part 2 — Simplifier

Now the same geometric sequences through a photocopier and a message that keeps getting forwarded — identical rules, identical answers, built from things you can picture.

## Subtopic: The Photocopier Set to Seventy-Five Percent

Place a poster on a photocopier set to reduce, copy it, then copy the copy, then copy that. Every page comes out a fixed fraction of the one before. That is a geometric sequence: not equal steps, but equal SHRINKS — or equal stretches when the machine enlarges. The dial on the machine is the common ratio r.

Testing a sequence is comparing each copy against its original: divide every term by the one before it. Constant quotient means one machine made the whole pile. In 3; 12; 48; 192, each division answers 4 — a machine set to quadruple. In 2; 6; 18; 36, the first divisions answer 3 but the final one answers 2 — someone touched the dial mid-run, so the pile is not geometric.

The dial can shrink: 162; 54; 18; 6 divides to one third every time, a pile of ever-smaller pages. The dial can even flip the sheet: 5; minus 10; 20; minus 40 multiplies by minus 2, alternating face-up, face-down, face-up. The only forbidden setting is zero — one blank page and every copy afterwards is blank, and division cannot even ask its question any more.

Quick check before we carry on — questions on spotting the ratio are coming to you right now. Divide neighbour by neighbour, and welcome fractions, negatives and shrinking as ordinary settings.

## Subtopic: One Message, a Chain of Forwards

A message reaches 3 people. Each of them forwards it to 4 more. Round one: 3 readers. Round two: 12. Round three: 48. To know the readership in round eight you do not trudge through the rounds — you take the start, 3, and apply the multiplier 4 seven times. That is the general term: T n equals a times r to the power n minus one. Seven, not eight, because round one is the launch, and forwarding only begins after it.

The exponent is the dividing line between the two sequence families. Adding 4 seven times contributes 28 more readers. MULTIPLYING by 4 seven times contributes a factor of 16 384 — round eight reaches 49 152 readers from a start of three. Multiplication does not climb; it detonates. The same detonation is why money under compound interest is this topic wearing a suit.

The formula reverses cleanly. Which round reaches exactly 3072 readers? Set 3 times 4 to the power n minus one equal to 3072. Divide by 3: 4 to the power n minus one equals 1024. Count your fours: 1024 is 4 to the fifth. So n minus one is 5, and n is 6 — round six. Same-base reasoning, straight from the exponents toolbox.

And when two rounds are known but the start is not — round two reached 10 and round five reached 80 — divide the larger fact by the smaller. The start cancels, leaving r cubed equal to 8: three forwards multiplied the audience by eight, so each forward doubles it, and the launch must have been 5 readers.

Your questions for this part are up now. Start times multiplier to the power jumps, and when two terms are known, divide and let the start erase itself.

## Subtopic: The Fair Middle, Multiplied

The arithmetic world's fair middle sat halfway between two numbers. The geometric world has its own fairness: equal MULTIPLICATION at every step. Between 5 and 320, which inserted numbers make the list multiply evenly? Two insertions create three jumps, so the dial setting obeys r cubed equals 64 — r is 4, and the list runs 5; 20; 80; 320. The inserted 20 and 80 are geometric means.

For any three terms in a row, keep the shortcut close: the middle term squared equals the product of its neighbours. Verify on 5; 20; 80 — twenty squared is 400, and 5 times 80 is 400. That identity powers every hidden-variable question. Given x; x plus 4; x plus 6 geometric, write the quantity x plus 4, squared, equals x times the quantity x plus 6. The x squared on each side cancels and x is minus 8, so the true terms are minus 8; minus 4; minus 2 — each term half its predecessor. Negative terms, ratio one half, entirely healthy. The mark-saving habit is substituting back and dividing to SEE the constant ratio with your own eyes.

One final care. If the algebra reports r squared equals 16, the dial could read 4 or minus 4, and each produces a genuine sequence — one steady, one alternating in sign. Offer both until the question itself chooses.

And here come the last questions of the lesson, right now: middle squared equals neighbours multiplied, jumps count as means plus one, and an even root on r leaves two possible machines until the question picks one.
