# Past-Paper Worked Example — Q11.3.2

**Source:** Department of Basic Education — Grade 12 Maths P1, November 2025, question Q11.3.2.

**© Department of Basic Education, 2025. Reproduced for educational use with attribution.**

## Question (4 marks)

Eight runners compete in a race where there are no tied finishes. Bongi and Andrew are two of the competitors. Calculate the probability that TWO OR MORE runners finish the race after Andrew and before Bongi.

## Method

count gap arrangements probability

## Memo working

Count the favourable finishes where Andrew and Bongi are separated by 2, 3, 4, 5 or 6 of the other runners, with Andrew ahead. If exactly k runners separate them, the pair occupies positions i and i + k + 1, which can be placed in 7 - k ways, and the other 6 runners fill the remaining positions in 6! ways. Summing for k = 2 to 6: 5×6! + 4×6! + 3×6! + 2×6! + 1×6! = 6!(15) favourable outcomes. The total number of finishes is 8!, so P = 6!(15)/8! = 15/56 = 0,27. (Alternative memo method uses the complement: [8! - (7!·2 + 2·6·6!)]/(8!·2) = 21 600/80 640 = 15/56.)

## Answer (per marking guidelines)

15/56 = 0,27
