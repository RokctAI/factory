# Part 1 — Expert

Today's work handles two events at once. One event was counting; two events are geography — regions, overlaps, and the rule that stops you counting anybody twice. The tools are the Venn diagram, the addition rule for P of A or B, and the special vocabulary of mutually exclusive and complementary events. One survey of 40 learners runs through the whole session, and by the close you will fill a two-event Venn diagram from scratch, compute any probability from it, and quote the addition rule with its famous subtraction explained.

## Subtopic: Two Events in One Picture

The running survey: in a class of 40 learners, 22 play soccer, 15 play chess, and 9 play BOTH. Describe the Venn diagram that organises this. A large rectangle represents the sample space S — all 40 learners; every learner lives somewhere inside it. Inside the rectangle, two overlapping circles: circle A for soccer players, circle B for chess players. The overlap region — the lens shape where the circles intersect — holds the learners in BOTH events. Four regions in total: the overlap, the part of A outside the overlap, the part of B outside the overlap, and the space inside the rectangle but outside both circles — the learners who play neither.

Now the filling rule, and it is non-negotiable: START WITH THE OVERLAP. Nine learners play both — write 9 in the lens first. Why first? Because the 22 soccer players INCLUDE the 9: the count 22 covers the whole circle A, overlap and all. So the soccer-only region holds 22 minus 9, which is 13. The chess-only region holds 15 minus 9, which is 6. And the neither region takes whatever is left of the 40: add the three circle regions — 13 plus 9 plus 6 is 28 — and subtract from 40: twelve learners play neither. Write 12 outside the circles, inside the rectangle.

Check the completed diagram: 13 plus 9 plus 6 plus 12 equals 40. Every learner placed once, nobody placed twice. A Venn diagram that does not total the sample space is wrong before any probability is computed.

Pause here — questions on this section are coming to you now. Overlap first, subtract outward, total to check: the order IS the method.

## Subtopic: The Addition Rule

The question this section answers: what is the probability that a randomly chosen learner plays soccer OR chess? In probability, OR is inclusive — soccer, chess, or both all count.

The tempting wrong answer adds the two probabilities directly: 22 over 40 plus 15 over 40 gives 37 over 40. Look at the diagram to see the crime: the 9 learners in the overlap were counted twice — once inside the 22, once inside the 15. Adding whole circles double-counts the lens. The repair is one subtraction: count the overlap back OUT once.

That repair, stated generally, is the ADDITION RULE — learn it word-perfect: P of A or B equals P of A, plus P of B, MINUS P of A and B. The subtracted term is the overlap's probability, removed once because addition included it twice.

Run it: 22 over 40, plus 15 over 40, minus 9 over 40 — that is 28 over 40, which simplifies to 7 over 10, or 0,7. Verify from the regions directly: soccer-only 13, both 9, chess-only 6 — 13 plus 9 plus 6 is 28 learners in at least one circle, 28 over 40 again. Rule and regions agree, and that double road is your permanent checking method.

The rule also runs BACKWARDS, and examiners love the reverse gear. Given P of A is 0,45, P of B is 0,3, and P of A or B is 0,6 — find P of A and B. Substitute into the rule: 0,6 equals 0,45 plus 0,3 minus the unknown. So the unknown equals 0,75 minus 0,6, which is 0,15. Any one missing piece of the four can be recovered from the other three; the addition rule is a four-variable machine, not a one-way formula.

Stop for this section's questions now — forwards and backwards, and always name what the subtraction removes.

## Subtopic: Mutually Exclusive Events

Some pairs of events CANNOT happen together. Rolling one die: the event "the number is less than 3" — outcomes 1 and 2 — and the event "the number is at least 5" — outcomes 5 and 6. No single roll lands in both events; the two sets share no outcome. Such events are MUTUALLY EXCLUSIVE: the occurrence of one excludes the other.

On the Venn diagram, mutual exclusivity is visible geography: the two circles do not overlap — they are drawn separated, and the intersection region simply does not exist. No lens, nothing to double-count.

Consequence for the algebra: P of A and B is 0, and the addition rule sheds its subtraction. For mutually exclusive events ONLY: P of A or B equals P of A plus P of B. Run the die example: P of less than 3 is 2 over 6; P of at least 5 is 2 over 6; the events are mutually exclusive, so P of one or the other is 4 over 6, which is 2 thirds.

The discipline: the short form of the rule is a PRIVILEGE that must be earned and declared. Before dropping the subtraction, state the justification — "the events are mutually exclusive, so P of A and B equals nought". Using the short rule on overlapping events inflates the answer, sometimes beyond 1 — and an answer beyond 1 is the addition rule telling you an overlap was ignored. Test yourself the other way: soccer and chess were NOT mutually exclusive — nine learners prove it — so the full rule with its subtraction was compulsory there.

Pause now for this section's questions — spot the shared outcomes, or certify there are none, before choosing the form of the rule.

## Subtopic: Complementary Events and Full Machinery Problems

Complementary events are mutual exclusivity taken to its extreme. Events A and not-A are complementary when they are mutually exclusive AND exhaustive — they cannot both happen, and between them they cover the entire sample space. Every outcome belongs to exactly one of them, so P of A plus P of not-A equals 1.

Hold the distinction sharply, because it is a favourite theory question. Mutually exclusive says only: no overlap. Complementary says: no overlap AND nothing left outside. The die events "less than 3" and "at least 5" are mutually exclusive but NOT complementary — the outcomes 3 and 4 belong to neither, so the two events fail to cover the sample space. Complementary demands a perfect two-piece partition; exclusive merely forbids sharing.

Now assemble the full machinery on the survey. The probability that a learner plays NEITHER sport: the neither region holds 12 of the 40, so 12 over 40 — 3 tenths. Confirm with the complement shortcut: "neither" is the complement of "soccer or chess", so 1 minus 7 tenths is 3 tenths. Two roads, same answer. The probability a learner plays exactly one of the two: soccer-only 13 plus chess-only 6 is 19, so 19 over 40 — and note that "exactly one" excludes the overlap, while "at least one" includes it: language chooses regions.

One more mutually exclusive computation, pure algebra: P of A is 0,4, P of B is 0,35, A and B mutually exclusive. Then P of A or B is 0,75, and P of neither is 1 minus 0,75 — 0,25.

The compressed method for any two-event problem: draw the rectangle and circles; fill the overlap first and subtract outward; check the total; then read the question's language — or, and, exactly one, neither, at least — into regions; quote the addition rule in full unless mutual exclusivity is declared and justified; and verify big answers through the complement. The final questions of this part are in front of you now — the survey changes, the machinery never does.

# Part 2 — Simplifier

The same machinery again now, built on a playground with two hoops and a pile of name cards. Nothing new arrives: the answers will land on the same 7 tenths and 3 tenths. What changes is that the diagram will become a place you can stand in, and the subtraction will become something you watched happen.

## Subtopic: Two Hoops on the Playground

Take the class outside. Chalk a big rectangle on the ground — every one of the 40 learners must stand somewhere inside it. Lay down two giant hoops, overlapping in the middle: the left hoop is soccer, the right hoop is chess.

Call the instructions. Play soccer? Stand in the left hoop. Play chess? Stand in the right hoop. Play both? There is exactly one honest place to stand — the overlap, the lens where the hoops share ground: inside both hoops at once, counted in each team without splitting yourself in two. Play neither? Stay inside the rectangle, outside both hoops — still part of the class, just not in these clubs.

Now place our survey. The nine both-players walk to the lens FIRST — the overlap is filled first, always, because those nine are hiding inside both team counts. Soccer claims 22 in total, but 9 of them already stand in the lens, so only 13 stand in the soccer-only crescent. Chess claims 15; 9 are in the lens, so 6 stand chess-only. Count everyone placed so far: 13 plus 9 plus 6 is 28. The class is 40, so 12 learners remain on the outside grass — the neither group. Head-count check: 13, 9, 6 and 12 make 40. Every learner has exactly one pair of feet and exactly one region.

That is all a Venn diagram is: a map of where people stand when two yes-no questions are asked at once.

Quick check before we carry on — a few questions on the hoops are coming to you right now. For each learner described, decide: which of the four patches of ground?

## Subtopic: Why We Subtract the Overlap

Stay on the playground. The principal wants a number: how many learners play at least one of the two games? A helper tries the obvious: read the soccer clipboard — 22 names — and the chess clipboard — 15 names — and add: 37. But look at the ground: only 28 learners are standing inside hoops. Where did the phantom 9 come from?

Walk to the lens and look at the nine learners standing there. Each of them is written on BOTH clipboards — once as a soccer player, once as a chess player. The addition counted their bodies twice. They are not two people each; they are one person with two memberships. Adding club registers counts memberships, not people.

The repair is exactly one move: subtract the overlap once. Thirty-seven minus 9 is 28 — now the arithmetic matches the ground truth. Say the whole logic in one breath: add the two clubs, then subtract the shared members once, because the addition greeted them twice. That sentence IS the addition rule: P of A or B equals P of A plus P of B minus P of A and B. Divide the head-counts by 40 and the same repair happens in probabilities: 22 fortieths plus 15 fortieths minus 9 fortieths — 28 fortieths, 7 tenths.

And now you can read the rule's warning system. If ignoring the subtraction ever pushes a probability past 1, the rule is shouting that an overlap was double-counted. The subtraction is not a decoration — it is the machine's honesty.

Your questions for this section are up now. In each one, find the people greeted twice, and greet them back out once.

## Subtopic: Never Together, and Covering Everything

Two last patterns, both about how the hoops can lie on the ground.

Pattern one: the hoops pulled completely apart — no shared ground at all. That is MUTUALLY EXCLUSIVE: nobody CAN stand in both, because both is not a place that exists. Real examples: on one die roll, "less than 3" and "at least 5" — no number is both; a card drawn is a heart and also a spade — impossible. With no lens, there is nothing to double-count, so the rule relaxes: add the two probabilities, done. But you must EARN the relaxed rule by saying why: the events cannot happen together, so the overlap's probability is nought. On the die: 2 sixths plus 2 sixths is 4 sixths — two thirds — and no subtraction was owed.

Pattern two: the strictest layout of all — two regions that not only avoid overlapping but also swallow the WHOLE rectangle between them, leaving no outside grass. That is COMPLEMENTARY: every single person stands in exactly one of the two regions. Rain or no rain. Pass or fail. Six or not-six. Two probabilities, everything covered, nothing shared — they must add to exactly 1, which is why "not" costs one subtraction: P of not-A is 1 minus P of A.

Keep the two patterns apart with the outside-grass test. Separated hoops can still leave people on the grass — "less than 3" and "at least 5" leave the 3s and 4s standing outside, so those events are exclusive but NOT complementary. Complementary means empty grass: nobody outside, no overlap, a perfect two-way split. Exclusive forbids sharing; complementary forbids sharing AND leftovers.

You now own the whole two-event world: the four patches of ground, overlap-first filling, the subtraction that keeps addition honest, and the two special layouts with their earned shortcuts. And here come the final questions of the lesson, right now — put each event in its hoop, watch the lens, and let the head-count confirm you. Walk in knowing the ground is mapped.
