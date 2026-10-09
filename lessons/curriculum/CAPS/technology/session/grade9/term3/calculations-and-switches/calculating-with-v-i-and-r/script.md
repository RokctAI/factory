# Part 1 — Expert

This session covers calculating values using resistance in ohms, voltage in volts and current in amperes. The anchor is the Rustenburg team's final circuit on the desk, a 4.5 volt battery, a reed switch, a 470 ohm resistor and a flashing LED, with a buzzer on a second branch, and the question of whether the battery will last the six months promised in the brief, answered with a few lines of arithmetic. The governing idea is that V equals I times R, applied to one component at a time with consistent units, together with the rules that series resistances add and carry a common current and that parallel branches share the supply voltage and their currents add, is enough to find every voltage, current and resistance in the simple circuits of the course. Setting out and solving Ohm's law problems, including series and parallel resistors and LED resistor selection, is examinable.

## Subtopic: Setting Out an Ohm's Law Calculation

A calculation is set out in five lines, and the setting out is marked. Line one: write what is known and what is wanted, with symbols and units, such as V equals 4.5 volts, R equals 470 ohms, I equals question mark. Line two: write the formula in the form needed, I equals V over R. Line three: substitute the numbers with their units, I equals 4.5 volts over 470 ohms. Line four: calculate, I equals 0.0096 amperes. Line five: state the answer in sensible units and check it, 9.6 milliamperes, which is a reasonable current for a small resistor on a battery.

Units are converted before substitution. Milliamperes to amperes, divide by 1000; kilohms to ohms, multiply by 1000; millivolts rarely appear. The answer is converted back if a smaller unit reads better: 0.0096 amperes is 9.6 milliamperes. A quick sense check at the end catches most slips: currents in battery circuits are milliamperes, not amperes or kiloamperes; voltages across components are less than the battery voltage; resistances in the kit run from tens of ohms to hundreds of kilohms.

Practice problems in the three forms. A buzzer rated 30 milliamperes at 4.5 volts has an effective resistance of 4.5 over 0.03, which is 150 ohms. A 2.2 kilohm resistor on 9 volts passes 9 over 2200, which is 0.0041 amperes, 4.1 milliamperes. A current of 20 milliamperes through 220 ohms gives a voltage of 0.02 times 220, which is 4.4 volts. In each, the five lines are written out, and the unit conversion is shown as its own step.

The questions for this section are with you now: the five-line layout, unit conversion before substituting, and practice in all three forms.

## Subtopic: Resistors in Series and the Shared Current

Resistors in series are joined end to end so that the same current flows through each. Their resistances add: 470 ohms in series with 330 ohms behaves as 800 ohms. The supply voltage is shared between them in proportion to their resistances, because each has the same current and V equals I times R for each: on 4.5 volts, the current is 4.5 over 800, which is 0.0056 amperes; the 470 ohm resistor has 0.0056 times 470, about 2.6 volts across it, and the 330 ohm resistor about 1.9 volts, which add back to 4.5. The larger resistor takes the larger share of the voltage.

This is how the LED resistor problem is understood in general. The LED is in series with the resistor and carries the same current; the LED takes its fixed 2 volts; the resistor takes the rest. For a 4.5 volt supply the resistor has 2.5 volts; for 6 volts, 4 volts; for 9 volts, 7 volts. At 10 milliamperes the resistor values are 250, 400 and 700 ohms, so the standard choices are 270, 390 and 680 ohms, or the next size up for a safer current. The same LED needs a different resistor for every supply voltage, and the method gives it in three lines.

A variable resistor in series with a fixed one gives a current that can be adjusted without ever falling to zero: 470 ohms fixed plus 0 to 10 kilohms variable on 4.5 volts gives a current from 4.5 over 470, about 9.6 milliamperes, down to 4.5 over 10 470, about 0.43 milliamperes. The fixed resistor protects the LED when the variable one is turned to zero, which is a design point that comes back in the transistor circuits later in the term.

The questions for this section are with you now: series resistances adding and sharing voltage, the LED resistor for 4.5, 6 and 9 volts, and a fixed resistor protecting against a variable one.

## Subtopic: Resistors in Parallel and Calculations for the PAT Circuit

Resistors in parallel are connected across the same two points, so each has the full voltage across it and each carries its own current given by Ohm's law; the currents add to give the total drawn from the supply. Two 470 ohm resistors in parallel on 4.5 volts each pass 9.6 milliamperes, total 19.2 milliamperes, and the pair behaves like a single resistor of 4.5 over 0.0192, which is about 235 ohms, half of 470. Two equal resistors in parallel halve the resistance; in general the combined resistance of parallel resistors is always less than the smallest of them, because adding a branch adds another path for current.

The PAT circuit uses parallel branches for its two outputs. The LED branch, 470 ohms and a 2 volt LED on 4.5 volts, draws about 5.3 milliamperes. The buzzer branch, a small electronic buzzer drawing 15 milliamperes at 4.5 volts, has its own silence switch. With both on, the battery supplies 5.3 plus 15, about 20 milliamperes; with the buzzer silenced, 5.3. Each branch is calculated on its own with the full 4.5 volts, which is the great convenience of parallel connection for a designer.

Battery life is the current drawn divided into the battery's capacity. Three AA cells hold about 2000 milliampere-hours. While the tank is full the reed switch is open and the circuit draws no current, so the standby life is years. When the tank is low and the LED is on, 5.3 milliamperes gives 2000 over 5.3, about 380 hours, over two weeks of continuous warning, which is far longer than it takes to refill the tank. With the buzzer sounding too, 20 milliamperes gives 100 hours, still four days. The brief's six months is met because the device draws nothing in standby. The error museum, four exhibits. One: adding parallel resistances as if they were in series. Two: giving an LED the same resistor on 9 volts as on 4.5. Three: forgetting to convert milliamperes before dividing. Four: calculating battery life from the warning current when the device spends almost all its time in standby.

The questions for this section are with you now: parallel resistors sharing voltage and adding currents, the PAT's two branches, and battery life.

# Part 2 — Simplifier

Now the same lesson again with the team's final circuit on the desk in Rustenburg — plain words, same facts.

## Subtopic: Formula, Numbers, Unit

Five lines. Known and wanted, with units. Formula. Numbers in with units. Calculate. Answer in a sensible unit, then a sense check.

Convert first: milliamps to amps divide by 1000, kilohms to ohms multiply by 1000. Battery circuits give milliamps, not amps. Nothing has more volts across it than the battery.

Buzzer at 30 milliamps on 4.5 volts: 150 ohms. 2.2 kilohms on 9 volts: 4.1 milliamps. 20 milliamps through 220 ohms: 4.4 volts.

Keep formula, numbers, unit in mind and try the questions for this part: setting out.

## Subtopic: In a Line, They Add Up

Series: same current through each, resistances add. 470 plus 330 is 800. On 4.5 volts, 5.6 milliamps; 2.6 volts across the 470, 1.9 across the 330, back to 4.5. Bigger resistor, bigger share of the volts.

LED and resistor in series: LED takes 2 volts, resistor takes the rest. 4.5 volts leaves 2.5; 6 leaves 4; 9 leaves 7. At 10 milliamps: 250, 400, 700 ohms, so 270, 390, 680. New supply, new resistor.

Fixed resistor plus a variable one: the current can be turned down but never up past the fixed limit. That protects the LED.

Hold in a line, they add up in mind and try this part's questions: series.

## Subtopic: Side by Side, Less Than the Smallest

Parallel: each branch gets the full volts, work each out alone, add the currents. Two 470s on 4.5 volts: 9.6 each, 19.2 total, acting like 235 ohms. Parallel is always less than the smallest.

PAT: LED branch 5.3 milliamps, buzzer branch 15. Both on, 20. Buzzer silenced, 5.3.

Battery: 2000 milliamp-hours. Standby, reed switch open, zero current, years. Warning with LED, 380 hours, two weeks. With buzzer, 100 hours. Six months is easy because standby is zero.

Pocket summary of the lesson. Ohm's law calculations are set out in five lines with units converted first and a sense check at the end. Series resistors add and share the supply voltage in proportion while carrying the same current, which gives the LED resistor for any supply: battery volts minus 2, divided by the current. Parallel branches each take the full voltage, their currents add and the combined resistance is below the smallest. Battery life is capacity divided by current drawn, and a device that draws nothing in standby lasts for months.

Hold side by side, less than the smallest, and take the final questions of the lesson: parallel and battery life.
