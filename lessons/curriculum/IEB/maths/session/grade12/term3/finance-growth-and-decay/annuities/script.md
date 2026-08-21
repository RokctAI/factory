# Part 1 — Expert

Growth and decay carried single amounts through time. Real financial life runs on STREAMS of equal payments: a monthly savings debit order, a monthly loan instalment, a fund topped up every month against the day a machine gives out. The mathematics of payment streams is the annuity, and it is nothing more than the geometric series of term one, finally earning its keep. Four movements ahead: the future value formula and where it comes from, the present value formula and loan repayments, sinking funds, and the outstanding balance that exposes what a loan truly costs.

## Subtopic: Future Value — Saving a Stream of Payments

An annuity is a sequence of EQUAL payments at EQUAL intervals with compound interest running throughout. The future value question asks: deposit x at the end of every month into an account earning i per month — what is the accumulated pile worth immediately after payment number n?

Derive it; never lean on memory alone. The final payment lands on the target date and earns nothing: worth x. The payment before it earns one month: x times one plus i. The one before that: x times one plus i squared. All the way back to the very first payment, which travelled nearly the whole road: x times one plus i to the power n minus one. Added up, that is a geometric series — first term x, common ratio one plus i, n terms — and the sum formula from term one hands over the result: F equals x times the quantity one plus i to the power n, minus one, all divided by i. That fraction is the future value factor, and being able to rebuild it from the series is a skill worth owning.

Worked case. Save 1 500 rand at the end of every month for 5 years at 9 percent per annum compounded monthly. The monthly rate is 0,0075; n is 60. One comma zero zero seven five to the sixtieth power is 1,56568, so the factor is 0,56568 over 0,0075 — 75,4241. F comes to 113 136,21 rand. Now dissect it: sixty deposits of 1 500 rand supplied 90 000; the remaining 23 136,21 is compound interest earned by the stream itself.

Timing is doctrine. The formula assumes payments at the END of each period, valued at the instant of the final payment. Any other arrangement — a first payment made today, or a valuation taken months after the final deposit — is handled by growing the whole fund, or individual payments, through the missing months. Read the dates in a question like a hawk reads a field.

Pause here — the questions for this section are with you now. Line the payments up, ask each one how many months it earned, and let the geometric sum carry the load.

## Subtopic: Present Value — the Mathematics of Loans

Now reverse the direction of the money. A bank hands you a lump P today; you repay x at the end of every month for n months. Fairness fixes the deal: P must equal the value TODAY of the entire future stream. A payment of x arriving k months from now is worth x divided by one plus i to the power k today — discounting, which is growth run in reverse. Summing the discounted payments gives another geometric series, and it collapses to P equals x times one minus the quantity one plus i to the power minus n, all over i.

The standard loan question inverts the formula: given the loan, find the instalment. Borrow 180 000 rand for a bakkie at 10,5 percent per annum compounded monthly — monthly rate 0,00875 — over 4 years, 48 payments. Rearranged: x equals P times i over one minus one comma zero zero eight seven five to the power minus forty-eight. The power first: 1,00875 to the forty-eighth is 1,5192, its reciprocal is 0,6582, and one minus that gives 0,3418. So x equals 1 575 over 0,3418 — 4 608,61 rand per month.

Now multiply out the truth. Forty-eight payments of 4 608,61 come to about 221 213 rand, against a loan of 180 000. The gap, roughly 41 213 rand, is the price of borrowing — nearly a quarter of the bakkie again. That one calculation, more than any other in this course, is consumer self-defence.

Keep the two formulas separated by the question they answer. Building a future pile from savings: future value. Settling money received today: present value. One verb in the question decides the stream — save, or borrow.

Stop for this section's questions now — discount every payment back to today for a loan, solve for whichever letter is hidden, and always weigh the total of the stream against the amount borrowed.

## Subtopic: Sinking Funds — Saving for the Machine's Funeral

A business often runs both formulas in the same breath. A machine wears out; its replacement will cost more than the original did, courtesy of inflation; the old unit will fetch only a scrap price, courtesy of depreciation. A SINKING FUND is a future value annuity engineered to close exactly that gap.

Full worked case. A machine costs 800 000 rand today. Its replacement is due in 6 years, with equipment prices inflating at 7 percent per annum: the new machine will cost 800 000 times 1,07 to the sixth — 1 200 584,28 rand. The old machine depreciates on the reducing balance at 12 percent per annum: after 6 years it resells for 800 000 times 0,88 to the sixth — 371 523,27 rand. The fund must therefore reach the shortfall: 1 200 584,28 minus 371 523,27, which is 829 061,01 rand.

Monthly payments into the fund earn 9 percent per annum compounded monthly — 0,0075 per month, 72 payments. Set the future value formula equal to the target: x times the quantity 1,0075 to the power seventy-two, minus one, over 0,0075, equals 829 061,01. The factor works out to 95,0070, so x equals 829 061,01 over 95,0070 — 8 726,31 rand per month.

Anatomy of the question: THREE different rates performed three different jobs — inflation priced the future machine, depreciation priced the scrap, and the fund's own interest rate grew the payments. Keeping those three lanes apart is the whole difficulty; inside each lane the calculation is a single familiar formula. Timing traps breed here too: if payments run from one month from now to month seventy-two, the formula applies untouched — but a question that starts payments TODAY, or that parks the purchase three months beyond the final payment, shifts the exponents, and a timeline diagram is the only dependable guard.

The questions on this section are in front of you now — three rates, three lanes, one target: future cost minus scrap equals what the fund must deliver.

## Subtopic: Outstanding Balance and What a Loan Really Costs

Eighteen months into the four-year bakkie loan, how much is still owed? Not five eighths of the debt remaining — far more, and the reason is the engine room of all loan mathematics. The OUTSTANDING BALANCE at any moment equals the present value of the REMAINING payments, discounted at the loan's own rate.

Compute it. After 18 payments, 30 remain. Balance equals 4 608,61 times one minus 1,00875 to the power minus thirty, all over 0,00875. The power: 1,00875 to the thirtieth is 1,2987, reciprocal 0,7700, so the bracket is 0,2300 and the factor is 26,2851. Balance: about 121 138 rand. Sit with the injustice of that arithmetic: over a third of the payments made — roughly 82 955 rand handed over — yet about two thirds of the original 180 000 still standing.

The explanation hides inside every single instalment. Each month, interest is charged on the CURRENT balance; the instalment settles that interest first, and only the leftover attacks the debt. Early on the balance is heavy, so interest swallows the lion's share: month one charges 0,875 percent of 180 000 — 1 575 rand — leaving just 3 033,61 of the 4 608,61 to reduce what is owed. Late in the loan the balance is light, the interest bite is small, and nearly the whole instalment lands as demolition. Amortisation front-loads the interest — which is why settlement quotes startle borrowers, and why paying even slightly above the instalment in the early years shortens a loan out of all proportion.

The final questions of this part are with you now — the balance is the present value of what remains, every payment splits into interest first and debt second, and that split drifts month by month in the borrower's slow favour.

# Part 2 — Simplifier

Now the same annuities told through a kitchen-table savings jar and a furniture-shop credit book — same formulas, same answers, built from things you can picture.

## Subtopic: Sixty Envelopes on the Table

Picture five years of saving: at the end of every month you seal 1 500 rand in an envelope and drop it into an account paying three quarters of a percent a month. Now spread all sixty envelopes across the table and interview each one: how long did YOU earn interest? The last envelope, dropped on the final day: zero months — worth exactly 1 500. Its neighbour: one month — worth 1 500 times 1,0075. The very first envelope: fifty-nine months of quiet growth. Sixty envelopes, each worth the previous one times 1,0075 — a geometric series lying in plain sight on the table.

Term one already taught you to sum exactly such a series, and finance simply names the answer the future value of an annuity: payment times the quantity growth factor to the n, minus one, over the rate. For our sixty envelopes: 113 136,21 rand. You contributed 90 000; compounding quietly stacked 23 136 on top — and the oldest envelopes did most of that earning.

That is the whole formula — envelopes in a row, geometric sum, finished. What deserves permanent suspicion in any question is the CALENDAR: the formula assumes each envelope lands at month-END, and the counting stops at the final drop. First envelope sealed today instead? Every envelope earns one extra month. Value wanted three months after the last drop? The entire pile grows three more months. Sketch the envelopes on a timeline before you trust any formula.

Quick check before we carry on — questions on the envelope row are coming to you right now. Ask every payment how long it earned, and check the calendar twice.

## Subtopic: The Furniture Shop's Fair Price

A furniture shop makes an offer: take the dining suite home today, pay 650 rand a month for two years. What does that suite genuinely cost? Every promised payment is worth LESS than its face value right now — 650 rand arriving next year is only worth whatever you would bank today to have 650 then, which is 650 shrunk backwards through the interest rate. Money loses today-value the further off it stands.

So the honest cash price is all twenty-four payments, each shrunk back to today, then added. That shrunken total is another geometric series, and its closed form is the present value formula: payment times one minus the shrink factor to the power minus n, all over the rate. The shop naturally runs it in reverse: start from the cash price and solve for the monthly payment that repays it — precisely what a bank does with a vehicle loan. A 180 000 rand loan at 0,875 percent a month over forty-eight months costs 4 608,61 monthly; forty-eight of those total about 221 213 rand. The suite-on-credit and the bakkie-on-credit obey one sentence: the lump today equals the stream's shrunken value, and everything above the lump is the fee for impatience.

Future value and present value are twins looking in opposite directions: one gazes forward from a saving stream to a pile, the other gazes backward from a repayment stream to a debt. The question's verb chooses the twin — SAVE means future, OWE means present.

Your questions for this part are up now. Shrink every promised payment back to today, and judge any credit deal by the gap between the stream's total and the lump.

## Subtopic: The Debt That Shrinks From the Wrong End

Here is the part nobody explains to first-time borrowers. Eighteen months into the four-year bakkie loan, having faithfully paid 18 of the 48 instalments — nearly 83 000 rand — you request a settlement figure and the bank replies: 121 138 rand, please. Two thirds of the loan still standing. It feels like a trick; it is arithmetic.

Think of the debt as a water tank with a filler pipe you never asked for. Every month, interest pours IN at 0,875 percent of whatever currently sits in the tank, and your instalment bails OUT a fixed 4 608,61. In month one the tank is brim-full: interest pours in 1 575, so your bucket removes only 3 034 of actual debt. The fuller the tank, the harder interest pushes back, and the less each bucket achieves. Only as the level falls does each instalment begin to land almost whole. Debt drains slowly at first and quickly at the end — from the wrong end, as every borrower feels it.

The settlement figure itself is simple to compute and worth computing: what you owe now is the today-value of the payments you have NOT yet made — thirty future instalments, shrunk back to the present. It is the furniture-shop formula with the remaining months in the exponent.

Two defences fall straight out of the tank picture. Any extra rand paid early strikes the water when the tank is fullest, cancelling the interest that rand would have poured in for years — early overpayments punch far above late ones. And when comparing loan offers, never compare instalments alone: multiply out each full stream, subtract the loan, and compare the leaks.

And here come the last questions of the lesson, right now: the tank fills with interest before your bucket lands, what remains owing is the shrunken value of the remaining payments, and every early extra rand is a blow against the flood at its strongest.
