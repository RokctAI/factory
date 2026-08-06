# Part 1 — Expert

Growth and decay moved single amounts through time. Real financial life moves STREAMS of equal payments: monthly savings, monthly loan instalments, a fund fed every month against the day a machine dies. The mathematics of payment streams is the annuity, and it is geometric series from term one, cashing its cheque. Four movements: the future value formula and its derivation, the present value formula and loan repayments, sinking funds, and the outstanding balance that reveals what a loan really costs.

## Subtopic: Future Value — Saving a Stream of Payments

An annuity is a sequence of EQUAL payments at EQUAL intervals with compound interest throughout. The future value question: deposit x at the end of every month into an account earning i per month — what is the pile worth just after payment number n?

Derive, never memorise blindly. The final payment arrives at the target date and earns nothing: worth x. The one before earns one month: x times one plus i. The one before that: x times one plus i squared. Back to the first payment, which rode almost the whole journey: x times one plus i to the power n minus one. The total is a geometric series with first term x, ratio one plus i, n terms. The sum formula from term one delivers: F equals x times the quantity one plus i to the power n, minus one, all over i. That fraction is the future value factor, and the derivation is examinable in exactly this form.

Worked case. Save 1 000 rand at the end of every month for 5 years at 6 percent per annum compounded monthly. The monthly rate is 0,005; n is 60. One comma zero zero five to the sixtieth is 1,34885, so the factor is 0,34885 over 0,005 — 69,77. F is 69 770,03 rand. Now read the anatomy: sixty deposits of 1 000 rand put in 60 000; the extra 9 770,03 is compound interest earned by the stream.

Timing is doctrine. This formula assumes payments at the END of each period, with the value taken at the moment of the last payment. Any other arrangement — first payment today, valuation months after the last payment — adjusts by growing the whole fund or individual payments by the missing months. Read the dates like a hawk.

Pause here — the questions for this section are with you now. Line the payments up, count each one's earning months, and let the geometric sum do the heavy lifting.

## Subtopic: Present Value — the Mathematics of Loans

Flip the question. A bank gives you a lump P today; you repay x at the end of every month for n months. Fairness demands: P must equal the value TODAY of all future payments. A payment of x arriving in k months is worth x divided by one plus i to the k today — discounting, growth run backwards. Sum the discounted payments: a geometric series again, and it collapses to P equals x times one minus the quantity one plus i to the power minus n, all over i.

The loan question inverts it: given the loan, find the instalment. Borrow 250 000 rand for a car at 12 percent per annum compounded monthly — monthly rate 0,01 — over 5 years, 60 payments. Rearrange: x equals P i over one minus one comma zero one to the power minus sixty. Compute the power: 1,01 to the sixtieth is 1,8167, so its reciprocal is 0,5504, and one minus that is 0,4496. Then x is 2 500 over 0,4496 — 5 561,11 rand per month.

Multiply out the truth: sixty payments of 5 561,11 total about 333 667 rand, on a loan of 250 000. The difference, roughly 83 667 rand, is the price of borrowing — a third again of the car. This single calculation, more than any other in the syllabus, is consumer self-defence.

Keep the two formulas apart by their questions. Saving toward a future pile: future value. Paying off money received today: present value. The exam decides which stream you are in by one word — save, or borrow.

Stop for this section's questions now — discount every payment to today for a loan, solve for whichever letter is missing, and always compare total payments against the amount borrowed.

## Subtopic: Sinking Funds — Saving for the Machine's Funeral

Businesses run both formulas at once. A machine wears out; its replacement will cost more than it did, thanks to inflation; the old one will fetch only scrap value, thanks to depreciation. A SINKING FUND is a future value annuity built to cover the gap.

Full worked case. A machine costs 500 000 rand today. Its replacement is needed in 5 years, with equipment prices inflating at 6 percent per annum: the new machine will cost 500 000 times 1,06 to the fifth — 669 112,79 rand. The old machine depreciates on reducing balance at 15 percent: in 5 years it resells for 500 000 times 0,85 to the fifth — 221 852,66 rand. The fund must therefore accumulate the shortfall: 669 112,79 minus 221 852,66, which is 447 260,13 rand.

Monthly payments into the fund earn 8 percent per annum compounded monthly — rate 0,08 over 12 per month, 60 payments. Set the future value formula equal to the target: x times the quantity one plus 0,08 over 12, to the power sixty, minus one, over 0,08 over 12, equals 447 260,13. The factor computes to 73,4769, so x is 447 260,13 over 73,4769 — 6 087,09 rand per month.

Anatomy of the question: THREE different rates did three different jobs — inflation priced the future machine, depreciation priced the scrap, and the fund's own interest rate grew the payments. Keeping the three lanes separate is the entire difficulty; the calculation inside each lane is one formula. Timing traps live here too: if the fund starts one month from now and the machine is replaced at month sixty, payments run one to sixty exactly as the formula assumes — but a question that starts payments TODAY, or delays the purchase three months past the last payment, shifts the exponents, and the timeline diagram is the only reliable guard.

The questions on this section are in front of you now — three rates, three lanes, one target: future cost minus scrap equals what the fund must reach.

## Subtopic: Outstanding Balance and What a Loan Really Costs

Two years into the five-year car loan, how much is still owed? Not three fifths of the debt — far more, and the reason is the engine of all loan mathematics. The OUTSTANDING BALANCE at any moment equals the present value of the REMAINING payments, discounted at the loan rate.

Compute it. After 24 payments, 36 remain. Balance equals 5 561,11 times one minus 1,01 to the power minus thirty-six, over 0,01. The power: 1,01 to the thirty-sixth is 1,4308, reciprocal 0,6989, so the bracket is 0,3011 and the factor is 30,1075. Balance: about 167 431 rand. Pause on the injustice of the arithmetic: two fifths of the payments made — roughly 133 467 rand paid — yet exactly two thirds of the original 250 000 still owing.

The explanation lives inside every instalment. Each month, interest is charged on the CURRENT balance; the instalment first covers that interest, and only the remainder chips the debt. Early in the loan the balance is fat, so interest devours most of the payment: month one charges one percent of 250 000 — 2 500 rand — leaving only 3 061,11 of the 5 561,11 to reduce debt. Late in the loan the balance is thin, interest is small, and almost the whole instalment is demolition. Amortisation front-loads the interest, which is why early settlement quotes surprise borrowers, and why paying even slightly more than the instalment in the early years shortens a loan dramatically.

The final questions of this part are with you now — balance is the present value of what remains, each payment splits into interest first and debt second, and the split shifts month by month in the borrower's slow favour.

# Part 2 — Simplifier

Now the same annuities from a stokvel bench and a furniture-shop credit book — same formulas, same answers, built from things you can picture.

## Subtopic: Sixty Envelopes on the Table

Picture saving for five years: at the end of every month you put 1 000 rand into an envelope and drop it into an account paying half a percent a month. Now lay all sixty envelopes on the table and ask each one: how long did YOU earn interest? The last envelope, dropped on the final day: zero months — worth exactly 1 000. The one before: one month — worth 1 000 times 1,005. The first envelope: fifty-nine months of growth. Sixty envelopes, each worth the previous times 1,005 — a geometric series, sitting right there on the table.

Term one taught the sum of exactly such a series, and the finance world names the result the future value of an annuity: payment times the quantity growth factor to the n, minus one, over the rate. For our sixty envelopes: 69 770,03 rand. You supplied 60 000; compounding quietly added 9 770 on top, and the earliest envelopes did most of that earning.

That is the entire formula — envelopes in a row, geometric sum, done. What deserves your suspicion in any question is the CALENDAR: the formula assumes each envelope is dropped at month-END, and the counting stops at the final drop. First envelope today instead? Every envelope earns one extra month. Value needed three months after the last drop? The whole pile grows three more months. Draw the envelopes on a line before trusting any formula.

Quick check before we carry on — questions on the envelope row are coming to you right now. Ask every payment how long it earned, and check the calendar twice.

## Subtopic: The Furniture Shop's Fair Price

A furniture shop offers: take the lounge suite today, pay 500 rand a month for two years. What is that suite really costing? Every future payment is worth LESS than its face value today — 500 rand arriving next year is worth what you would bank today to have 500 then, which is 500 shrunk backwards by the interest rate. Money loses today-value the further away it stands.

So the fair cash price is all twenty-four payments, each shrunk back to today, added up. That shrunken sum is another geometric series, and its closed form is the present value formula: payment times one minus the shrink factor to the power minus n, all over the rate. The shop, of course, runs it the other way: start from the cash price, solve for the monthly payment that repays it — which is exactly what a bank does with a car loan. A 250 000 rand loan at one percent a month over sixty months costs 5 561,11 monthly; sixty of those total about 333 667 rand. The suite-on-credit and the car-on-credit both obey the same sentence: the lump today equals the stream's shrunken value, and everything above the lump is the fee for impatience.

Future value and present value are twins with opposite gazes: one looks forward from a saving stream to a pile, the other looks backward from a paying stream to a debt. The question's verb picks the twin — SAVE means future, OWE means present.

Your questions for this part are up now. Shrink every promised payment back to today, and judge every credit deal by the gap between the stream's total and the lump.

## Subtopic: The Debt That Shrinks From the Wrong End

Here is the part nobody tells first-time borrowers. Two years into the five-year car loan, having faithfully paid 24 of the 60 instalments — some 133 000 rand — you ask for a settlement figure and the bank says: 167 431 rand, please. Two thirds of the loan still standing. It feels like a scam; it is arithmetic.

Think of the debt as a water tank with a leak-filling pipe. Every month, interest pours IN at one percent of whatever is currently in the tank, and your instalment bails OUT a fixed 5 561,11. In month one the tank is full: interest pours in 2 500, so your bucket removes only 3 061 of actual debt. The fuller the tank, the harder interest fights back, and the less your bucket achieves. Only as the level drops does each instalment start landing almost whole. Debt shrinks slowly at first, fast at the end — from the wrong end, as borrowers experience it.

The settlement figure itself is easy to compute and worth computing: what is owed now is the today-value of the payments you have NOT yet made — thirty-six future instalments, shrunk back to the present. The formula is the furniture-shop one with the remaining months in the exponent.

Two defences follow from the tank picture. Any extra rand paid early strikes water when the tank is fullest, cancelling the interest that rand would have generated for years — early overpayments are worth far more than late ones. And when comparing loan offers, never compare instalments alone: multiply out the full stream, subtract the loan, and compare the leaks.

And here come the last questions of the lesson, right now: the tank fills with interest before your bucket lands, what remains owing is the shrunken value of the remaining payments, and every early extra rand is a strike against the flood at its strongest.
