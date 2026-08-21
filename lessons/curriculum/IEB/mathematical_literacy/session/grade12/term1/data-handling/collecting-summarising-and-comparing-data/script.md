# Part 1 — Expert

Numbers decide arguments in South Africa long before shouting does: clinic queues, fuel prices, rainfall records, water restrictions. Data handling is the craft of settling those arguments honestly — asking a precise question, gathering data without cheating, summarising it fairly and drawing it so the truth is visible to anyone. This session investigates a question that touches almost every family: how long do patients wait to be seen at a clinic? Two clinics keep the score — Ntabeni Clinic, deep rural in Limpopo, and Umbilo Clinic in central Durban — and their waiting times tell a story about access to health care that a single average would smooth away.

## Subtopic: Asking the Question and Collecting the Data

Every investigation starts with a QUESTION, and the strongest questions attach to real issues: health care access, road safety, water supply, the cost of living. Ours: how many minutes does a patient wait between arriving at the clinic and being seen by a nurse, and does the answer differ between a rural and an urban clinic?

Next, decide WHO the question is about. The POPULATION is every patient who visits each clinic. Measuring all of them is impossible, so a SAMPLE is drawn — and it must be drawn fairly, spread across the whole day. Recording only the patients who arrive before seven in the morning builds in BIAS: the early arrivals are seen first, so their short waits would drag the answer downward and flatter the clinic.

Then choose the COLLECTION INSTRUMENT. A QUESTIONNAIRE puts written questions to many people cheaply, but its wording must be short, unambiguous and unleading. An INTERVIEW asks face to face, allowing follow-up questions, though it is slow and the interviewer may sway the answer. A RECORDING SHEET logs what is observed directly — a clerk noting each arrival time and each consultation time, which suits waiting times perfectly because nobody has to remember or estimate anything.

Finally, classify what the sheet delivers. Waiting minutes are NUMERICAL data — numbers you can add, average and cut into quartiles. The reason for the visit — vaccination, medication collection, wound care — is CATEGORICAL data: labels you can count but never average. That distinction governs everything that follows, because means and quartiles exist only for numerical data. The questions for this section are with you now; name the population, the instrument and the data type before a single stroke is tallied.

## Subtopic: Organising: Tallies, Frequency Tables and Class Intervals

The clerk at Ntabeni logs eleven waiting times in minutes: 20, 30, 30, 45, 50, 60, 70, 85, 90, 100 and 120. Raw data is honest but unreadable at scale, so the next step is organisation.

The first tool is the TALLY: one stroke per patient, bundled in fives, converted into a FREQUENCY TABLE that lists each value beside how often it occurs. The value 30 has frequency 2; every other value stands alone with frequency 1.

When many different values appear, single-value rows waste space, so the data is grouped into CLASS INTERVALS of equal width. Using intervals of twenty-five minutes: 0 up to 24 holds only the 20 — frequency 1. The interval 25 to 49 holds 30, 30 and 45 — frequency 3. The interval 50 to 74 holds 50, 60 and 70 — frequency 3. The interval 75 to 99 holds 85 and 90 — frequency 2 — and 100 to 124 holds 100 and 120 — frequency 2. Check the total: 1 + 3 + 3 + 2 + 2 = 11, exactly the number of patients logged. That check is not optional; if the frequencies do not sum to the number of responses, data has been dropped or counted twice.

Two rules protect class intervals. They may never overlap — one interval ends at 49, the next begins at 50, so no waiting time can fall into two rows. And they should share one width, because unequal widths distort every graph drawn from the table.

Grouping trades detail for clarity: the table no longer remembers whether a patient waited 85 or 90 minutes, only that two patients sat in that band. For large data sets the trade is worth it, and a favourite exam move is a borderline value — decide firmly which interval 49 belongs to before you tally it. The questions for this section are ready; bundle the strokes, check the total, and guard the interval boundaries.

## Subtopic: Summarising: Mean, Median, Quartiles and Percentiles

Summary statistics squeeze a data set into a few honest numbers — but only if the data is ordered first. Ntabeni's times already stand in order: 20, 30, 30, 45, 50, 60, 70, 85, 90, 100, 120.

The MEAN adds and divides: the sum is 700, and 700 ÷ 11 = 63,6 minutes to one decimal place. The MEDIAN is the middle of the ordered list: with 11 values the middle is the sixth, which is 60 minutes — five waits below it, five above. The MODE is the most frequent value: 30 minutes, appearing twice. The RANGE is largest minus smallest: 120 − 20 = 100 minutes.

QUARTILES slice the ordered data into four equal parts. The LOWER QUARTILE Q1 is the median of the bottom half — of 20, 30, 30, 45, 50 the middle is 30. The UPPER QUARTILE Q3 is the median of the top half — of 70, 85, 90, 100, 120 the middle is 90. The INTERQUARTILE RANGE, IQR, is Q3 minus Q1: 90 − 30 = 60 minutes, the width of the middle half of the data. Unlike the range, the IQR ignores the extremes, so one marathon wait cannot inflate it.

PERCENTILES refine the same idea: the 25th percentile is Q1, the 50th is the median, the 75th is Q3. A patient at the 90th percentile waited longer than 90% of patients. Clinics track baby weights on percentile charts; schools report test results the same way.

Notice the gap between mean and median — 63,6 against 60. The single two-hour wait pulls the mean upward while the median holds its ground; the mean chases extremes, the median resists them. The questions for this section follow now; order first, count to the middles, and state every statistic in a sentence with its unit.

## Subtopic: The Box-and-Whisker Plot: Comparing Two Data Sets

The FIVE-NUMBER SUMMARY — minimum, Q1, median, Q3, maximum — draws as a BOX-AND-WHISKER PLOT: a box from Q1 to Q3 with a line at the median, and whiskers stretching out to the minimum and maximum. Ntabeni: 20, 30, 60, 90, 120.

Umbilo's eleven waiting times, already ordered: 15, 15, 20, 25, 30, 35, 40, 40, 45, 50, 55. Median: sixth value, 35 minutes. Q1: median of 15, 15, 20, 25, 30, which is 20. Q3: median of 40, 40, 45, 50, 55, which is 45. Five-number summary: 15, 20, 35, 45, 55. IQR: 45 − 20 = 25 minutes.

Now draw both plots on one shared scale and read them together — comparison is the skill final exams reward most in this topic. The medians: Ntabeni 60, Umbilo 35 — the typical rural patient waits twenty-five minutes longer. The boxes: Ntabeni's IQR of 60 against Umbilo's 25 — rural waits are far more spread out, some patients seen quickly and others losing a morning. The right whiskers: Ntabeni reaches 120 while Umbilo stops at 55 — the longest rural wait is a full two hours, longer than any urban wait recorded.

Interpretation must live in context: rural patients typically wait longer AND less predictably than urban patients, and a quarter of Ntabeni's patients wait 90 minutes or more, because a quarter of the data always lies above Q3. That last move — a quarter lies beyond the quartile — is the most examinable sentence in the topic.

A box plot never shows the mean, the mode or the number of patients; it shows position and spread only. Choosing statistics that resist outliers, comparing like with like on one scale, and writing conclusions in context — that is data handling at matric level. The questions for this section are with you now; five numbers per clinic, one shared scale, and conclusions in full sentences.

# Part 2 — Simplifier

Now the same numbers with patients seated in a waiting-room queue instead of listed on a clipboard.

## Subtopic: Lining Up the Queue

Forget formulas for a moment. Take Ntabeni's eleven patients and seat them along the bench in order of waiting time, shortest wait nearest the door: 20, 30, 30, 45, 50, 60, 70, 85, 90, 100, 120 minutes.

The MEDIAN is simply the patient seated dead centre. Eleven patients means the sixth one — count along the bench — and the sixth waited 60 minutes. Five people waited less, five waited more. He is the typical patient, and no unlucky soul at the far end of the bench can move him, because he is found by counting, not adding.

Quartiles? Cut the bench the same way twice more. Take the five patients on his left and find THEIR middle: the third one, 30 minutes. That is the lower quartile — a quarter of the patients waited 30 minutes or less. Take the five on his right; their middle waited 90. That is the upper quartile — a quarter of the patients waited 90 minutes or more. The gap between those two markers, 90 minus 30, is the interquartile range: 60 minutes. It measures how stretched the MIDDLE HALF of the bench is, ignoring the two-hour patient completely.

And percentiles are just a finer version of the same seating plan: at the 90th percentile you sit further along the bench than 90 out of every 100 patients. Baby clinics use it, schools use it — same queue, more cutting points.

Order first, count to the middles. That is the entire machine. Some questions on this section are with you right now; seat the numbers in a line before you touch them, then count, do not calculate.

## Subtopic: The Box Tells the Story

A box-and-whisker plot is just the ordered bench photographed from above. Five numbers pose for the photo: the shortest wait, the lower quartile, the median, the upper quartile and the longest wait. For Ntabeni: 20, 30, 60, 90, 120.

Read the picture like this. The box, drawn from 30 to 90, is where the middle half of the queue sits — half of all the patients are inside that box. The line inside the box at 60 is the median, the typical patient. The whiskers reaching out to 20 and 120 are the extremes: the patient seen almost at once and the patient who lost two hours.

Now the magic of the picture: place Umbilo's box — 15, 20, 35, 45, 55 — directly underneath on the same scale, and the story leaps out without a single calculation. The Umbilo median line stands at 35, the Ntabeni line at 60: typical urban waits are twenty-five minutes shorter. The Umbilo box is narrow, 20 to 45; the Ntabeni box is wide, 30 to 90: rural waits are all over the place, urban ones are predictable. And the Ntabeni whisker stretches to 120 while Umbilo's stops at 55.

One rule unlocks most exam questions: every section of the plot — each whisker, each half of the box — holds a QUARTER of the data. So a quarter of Ntabeni's patients wait 90 minutes or more; half wait between 30 and 90. The box never tells you how MANY patients there were, or the mean — only where they sit and how spread they are. Questions on this section are coming your way now; find the five numbers, then read quarters off the picture like slices of a loaf.

## Subtopic: Mean or Median: Which One to Trust

The Ntabeni bench offers two honest answers to what is the typical wait. The mean adds all eleven times and divides: 700 over 11 gives 63,6 minutes. The median counts to the middle of the bench: 60 minutes. Which one tells the truth?

Both — but each has a weakness, and exams love asking which. Watch what one extreme value does. The patient who waited 120 minutes is one person, yet she lifts the mean above most of the queue. Replace her 120 with 60 and the mean drops to 640 over 11 — about 58,2 — while the median stays exactly where it was, at 60. One number moved the mean by more than five minutes and could not budge the median at all.

That is the rule of thumb: the mean is democratic with rands and minutes — every value votes with its full size, so one tender-rich businessman walking into a township survey sends the average income soaring. The median only asks who sits in the middle, so extremes shout into the wind. When data carries outliers — salaries, house prices, waiting times with one forgotten patient — the median is the safer typical value, and saying so with the reason is a classic short question.

The same suspicion applies to spread. The range, 120 minus 20, listens only to the two most extreme patients. The interquartile range, 60, listens to the solid middle half. A big range with a modest IQR means outliers at the edges, not chaos in the middle.

So when a councillor or an advert quotes an average, ask the data handler's question: mean or median, and who is hiding in the tail? The final questions of the lesson are with you now; test every claim by asking what one extreme value would do to it.
