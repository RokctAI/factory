# Part 1 — Expert

Today we handle two events at the same time. One event was a counting exercise; two events are a matter of territory — regions, overlaps, and the rule that prevents anyone being counted twice. Our tools are the Venn diagram, the addition rule for P of A or B, and the precise vocabulary of mutually exclusive and complementary events. One survey of 50 learners runs through the entire session, and by the end you will build a two-event Venn diagram from nothing, extract any probability from it, and quote the addition rule with its famous subtraction fully explained.

## Subtopic: Two Events in One Picture

The running survey: in a grade group of 50 learners, 24 play netball, 18 play tennis, and 10 play BOTH. Here is the Venn diagram that organises it. A large rectangle stands for the sample space S — all 50 learners; every learner lives somewhere inside that rectangle. Inside it, two overlapping circles: circle A for netball players, circle B for tennis players. The overlap — the lens where the circles cross — holds the learners in BOTH events. Four regions altogether: the overlap, the piece of A outside the overlap, the piece of B outside the overlap, and the area inside the rectangle but outside both circles — the learners who play neither sport.

Now the filling rule, and it is absolute: START WITH THE OVERLAP. Ten learners play both — the 10 goes into the lens first. Why first? Because the 24 netball players INCLUDE those 10: the figure 24 covers the entire circle A, overlap included. So the netball-only region holds 24 minus 10, which is 14. The tennis-only region holds 18 minus 10, which is 8. The neither region collects whatever remains of the 50: the three circle regions hold 14 plus 10 plus 8, which is 32, and 50 minus 32 leaves 18. Write 18 outside the circles, inside the rectangle.

Audit the finished diagram: 14 plus 10 plus 8 plus 18 equals 50. Every learner placed exactly once, no learner placed twice. A Venn diagram whose regions do not total the sample space is broken before a single probability is calculated.

Pause here — questions on this section are coming to you now. Overlap first, subtract outward, total to check: that order IS the method.

## Subtopic: The Addition Rule

This section's question: what is the probability that a randomly chosen learner plays netball OR tennis? Remember that in probability, OR is inclusive — netball, tennis, or both all qualify.

The tempting wrong move adds the two probabilities straight: 24 over 50 plus 18 over 50 gives 42 over 50. The diagram exposes the crime: the 10 learners in the lens were counted twice — once inside the 24, once inside the 18. Adding whole circles double-counts the overlap. The repair is a single subtraction: remove the overlap exactly once.

Stated in general, that repair is the ADDITION RULE — learn it word for word: P of A or B equals P of A, plus P of B, MINUS P of A and B. The subtracted term is the probability of the overlap, taken out once because the addition took it in twice.

Execute it: 24 over 50, plus 18 over 50, minus 10 over 50 — that is 32 over 50, which simplifies to 16 over 25, or 0,64. Confirm from the regions directly: netball-only 14, both 10, tennis-only 8 — 14 plus 10 plus 8 is 32 learners inside at least one circle, giving 32 over 50 again. Rule and regions agree, and that pair of roads is your permanent verification method.

The rule also drives in REVERSE, and reverse questions are everywhere. Given P of A is 0,5, P of B is 0,35, and P of A or B is 0,7 — find P of A and B. Substitute: 0,7 equals 0,5 plus 0,35 minus the unknown. The unknown equals 0,85 minus 0,7, which is 0,15. Any single missing value among the four can be recovered from the other three — the addition rule is a four-variable machine, never a one-direction formula.

Stop for this section's questions now — forwards and backwards, and always name what the subtraction is removing.

## Subtopic: Mutually Exclusive Events

Certain pairs of events CANNOT occur together. Draw one numbered card from a box holding cards 1 to 10: the event "the number is below 3" — outcomes 1 and 2 — and the event "the number is above 8" — outcomes 9 and 10. No single draw can land in both events; the two sets share no outcome at all. Such events are MUTUALLY EXCLUSIVE: if one happens, the other is ruled out.

On the Venn diagram, mutual exclusivity is visible as geography: the circles are drawn apart, not overlapping — the intersection region simply does not exist. No lens, and therefore nothing to double-count.

The algebraic consequence: P of A and B is 0, and the addition rule drops its subtraction. For mutually exclusive events ONLY: P of A or B equals P of A plus P of B. On the card box: P of below 3 is 2 over 10; P of above 8 is 2 over 10; the events are mutually exclusive, so P of one or the other is 4 over 10 — two fifths.

Now the discipline: the short form of the rule is a PRIVILEGE, earned and declared. Before you drop the subtraction, write the justification — "the events are mutually exclusive, so P of A and B equals nought". Using the short rule on events that do overlap inflates the answer, sometimes past 1 — and any probability past 1 is the addition rule shouting that an overlap was ignored. Test the logic in reverse: netball and tennis were NOT mutually exclusive — ten learners prove it — so the full rule with its subtraction was compulsory there.

Pause now for this section's questions — hunt for shared outcomes, or certify that none exist, before you choose which form of the rule to use.

## Subtopic: Complementary Events and Full Machinery Problems

Complementary events are mutual exclusivity pushed to its limit. Events A and not-A are complementary when they are mutually exclusive AND exhaustive — they can never both happen, and together they swallow the whole sample space. Every outcome sits in exactly one of the two, so P of A plus P of not-A equals 1.

Keep the distinction razor-sharp, because it is a favourite theory question. Mutually exclusive claims only one thing: no overlap. Complementary claims two: no overlap AND nothing left over outside. The card events "below 3" and "above 8" are mutually exclusive but NOT complementary — the numbers 3 through 8 belong to neither event, so the pair fails to cover the sample space. Complementary requires a perfect two-piece split; exclusive merely bans sharing.

Now run the full machinery on the survey. The probability that a learner plays NEITHER sport: the neither region holds 18 of the 50, so 18 over 50 — 0,36. Confirm through the complement shortcut: "neither" is the complement of "netball or tennis", so 1 minus 0,64 is 0,36. Two roads, one answer. The probability that a learner plays exactly one of the two sports: netball-only 14 plus tennis-only 8 is 22, so 22 over 50 — 11 over 25. And note the language carefully: "exactly one" excludes the lens, while "at least one" includes it — the wording of the question selects the regions.

One more mutually exclusive calculation, pure algebra this time: P of A is 0,25, P of B is 0,4, with A and B mutually exclusive. Then P of A or B is 0,65, and P of neither is 1 minus 0,65 — which is 0,35.

The compressed method for any two-event problem: draw the rectangle and the circles; fill the overlap first and subtract outward; audit the total; translate the question's language — or, and, exactly one, neither, at least — into regions; quote the addition rule in full unless mutual exclusivity has been declared and justified; and check large answers through the complement. The final questions of this part are with you now — the survey may change, the machinery never does.

# Part 2 — Simplifier

The same machinery once more, built this time from two long ropes laid out on the school hall floor and a stack of name cards. Nothing new is on its way: the answers will land on the same 0,64 and 0,36. What changes is that the diagram becomes a floor you can walk on, and the subtraction becomes something you personally watch happen.

## Subtopic: Two Ropes in the School Hall

March the whole grade into the hall. Tape a huge rectangle on the floor — all 50 learners must stand somewhere inside it. Now lay down two big rope rings that cross each other in the middle: the left ring is netball, the right ring is tennis.

Give the instructions. Play netball? Stand inside the left ring. Play tennis? Stand inside the right ring. Play both? There is exactly one honest spot for you — the lens where the ropes cross: inside both rings at once, a member of each team without being cut in half. Play neither? Stay inside the taped rectangle but outside both ropes — still part of the grade, just outside these two clubs.

Now stage our survey. The ten both-players walk into the lens FIRST — the overlap fills first, always, because those ten are hiding inside both team totals. Netball claims 24 in total, but 10 of them are already standing in the lens, so only 14 stand in the netball-only crescent. Tennis claims 18; 10 are in the lens, so 8 stand tennis-only. Count the placed feet: 14 plus 10 plus 8 is 32. The grade numbers 50, so 18 learners remain on the open floor — the neither group. Head-count audit: 14, 10, 8 and 18 make 50. Every learner has one pair of shoes and one patch of floor.

That is the whole truth about a Venn diagram: it is a map of where people stand when two yes-or-no questions are asked at the same time.

Quick check before we push on — a few questions about the ropes are coming to you right now. For each learner described, decide: which of the four patches of floor?

## Subtopic: Why We Subtract the Overlap

Stay in the hall. The sports organiser needs one number: how many learners play at least one of the two sports? A helper tries the obvious route: read the netball register — 24 names — and the tennis register — 18 names — and add them: 42. But look down at the floor: only 32 learners are standing inside rope. Who are the 10 phantoms?

Walk to the lens and study the ten learners standing there. Every one of them appears on BOTH registers — once as a netball player, once as a tennis player. The addition counted their bodies twice. They are not two people each; they are one person holding two memberships. Adding club registers counts memberships, not human beings.

The repair takes exactly one move: subtract the overlap once. Forty-two minus 10 is 32 — and now the arithmetic agrees with the floor. Say the full logic in a single breath: add the two clubs, then subtract the shared members once, because the addition welcomed them twice. That sentence IS the addition rule: P of A or B equals P of A plus P of B minus P of A and B. Divide all the head-counts by 50 and the identical repair runs in probabilities: 24 fiftieths plus 18 fiftieths minus 10 fiftieths — 32 fiftieths, which is 0,64.

And now the rule's built-in alarm makes sense. If skipping the subtraction ever pushes a probability beyond 1, the rule is screaming that somebody was counted twice. The subtraction is not decoration — it is the machine keeping itself honest.

Your questions for this section are up now. In every one, find the people who were greeted twice, and greet them back out exactly once.

## Subtopic: Never Together, and Covering Everything

Two final patterns, both about how the ropes can lie on the floor.

Pattern one: the rings pulled completely apart — not a centimetre of shared floor. That is MUTUALLY EXCLUSIVE: nobody CAN stand in both, because "both" is not a place that exists. Real cases: one card drawn from the 1-to-10 box, "below 3" and "above 8" — no card is both; one learner being in Grade 10 and in Grade 11 at the same moment — impossible. With no lens there is nothing to double-count, so the rule relaxes: add the two probabilities and stop. But the relaxed rule must be EARNED out loud: the events cannot happen together, so the overlap's probability is nought. On the card box: 2 tenths plus 2 tenths is 4 tenths — two fifths — and no subtraction was ever owed.

Pattern two: the strictest layout possible — two regions that avoid overlapping AND between them cover the entire rectangle, leaving no open floor at all. That is COMPLEMENTARY: every single person stands in exactly one of the two regions. Rain or no rain. On time or late. Even or odd. Two probabilities, everything covered, nothing shared — so they must total exactly 1, which is why "not" costs one subtraction: P of not-A equals 1 minus P of A.

Separate the two patterns with the open-floor test. Rings pulled apart can still leave people standing on open floor — "below 3" and "above 8" leave the 3s through 8s outside both ropes, so those events are exclusive but NOT complementary. Complementary means empty floor: nobody outside, nobody shared, a perfect two-way split of everyone. Exclusive bans sharing; complementary bans sharing AND leftovers.

You now own the entire two-event world: the four patches of floor, overlap-first filling, the subtraction that keeps addition honest, and the two special layouts with their earned shortcuts. The final questions of the lesson are arriving now — place each event inside its rope, watch the lens like a hawk, and let the head-count confirm you. The floor is mapped; walk it with confidence.
