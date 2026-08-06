# Part 1 — Expert

Almost every joule of electrical energy in South Africa's grid began as motion — a turbine spinning a coil in a magnetic field. And almost every machine that moves on electricity runs the same trick in reverse. Generators and motors are one piece of physics read in two directions, and this session masters both: electromagnetic induction and the generator, the motor effect and the motor, why the grid chose alternating current, and the rms values that let us do honest power calculations with a current that never stops changing.

## Subtopic: Generators and Electromagnetic Induction

A generator converts mechanical energy to electrical energy, and the principle behind it is electromagnetic induction: when a conductor moves through a magnetic field, or the magnetic flux through a coil changes, an emf is induced across it. Spin a coil between the poles of a magnet and the flux through the coil rises and falls with every rotation, so an emf drives current around the circuit for as long as something keeps the coil turning. Nothing is created from nothing — the turning force does work against magnetic forces, and that work becomes electrical energy.

Build the AC generator part by part, since labelling is a standing exam question. A rectangular coil, often called the armature, rotates in the field between two curved magnet poles. The ends of the coil connect to two SLIP RINGS — complete rings, one per coil end — which rotate with the coil. Two carbon BRUSHES press against the rings, carrying current to the external circuit while allowing the coil to spin freely. As the coil rotates, each side of the coil travels up through the field for half a turn and down for the other half, so the induced emf reverses direction every half rotation: the output is alternating current, flowing one way, then the other, in a smooth repeating wave.

One change of hardware turns AC into DC. Replace the two slip rings with a single ring split into two halves — the SPLIT-RING COMMUTATOR. Each brush now touches whichever half-ring is on its side at that moment, and the halves swap brushes at exactly the instant the coil's emf reverses. The swap cancels the reversal, so the external current always flows the same way: direct current, though it still pulses from zero to maximum and back. Slip rings give AC; a split-ring commutator gives DC — that single sentence settles a mark nearly every year.

This section's questions are with you now — induction needs changing flux, and the rings decide whether the world outside sees AC or DC.

## Subtopic: Motors and the Motor Effect

Run the story backwards. A motor converts electrical energy to mechanical energy, and its principle is the MOTOR EFFECT: a current-carrying conductor in a magnetic field experiences a force. Push current through a coil sitting in a magnetic field and one side of the coil is forced up while the other side is forced down, because the current flows in opposite directions along the two sides. Two opposite forces on the two sides of a pivoted coil produce a turning effect, and the coil rotates.

But an uncorrected coil would only swing half a turn and stop, with the forces then pulling it backwards. The DC motor borrows the generator's trick: a split-ring commutator reverses the current through the coil every half rotation, at just the moment the coil passes the vertical. Reversed current means reversed forces, so the push keeps acting in the same rotational direction, and the coil spins continuously. The parts list mirrors the generator exactly — coil, magnets, brushes, commutator — and that is no coincidence.

The deep statement, and the syllabus asks it directly: a generator and a motor are the SAME device operating in opposite energy directions. Turn the coil by hand and electrical energy comes out — generator. Feed electrical energy in and rotation comes out — motor. Motors surround you: fans, washing machines, drills, pumps, electric vehicles, the compressor in every fridge. Whenever electricity becomes motion, a coil is being pushed around inside a magnetic field.

Questions on this section reach you now — current in a field feels a force, and the commutator's half-turn flip is what turns a single lurch into continuous spinning.

## Subtopic: Why the Grid Chose Alternating Current

South Africa's mains supply is AC, and the syllabus wants the reason argued, not recited. The decisive advantage of AC is that its voltage is easily changed by TRANSFORMERS — devices that step voltage up or down using induction, and which only work on changing current. That matters because of transmission losses. Power lost as heat in a transmission line is I squared times R: it depends on the SQUARE of the current. Transmit a given amount of power at very high voltage and the same power rides on a small current — and a small current squared is a tiny loss. So the grid steps voltage up to hundreds of thousands of volts for the long journey from the power station, then steps it down in stages to the 220 volts at your wall. With DC, cheap and efficient voltage changing was historically impossible, so AC won the grid.

Now picture the AC signal itself, because the graphs are examinable. Plot voltage against time: a smooth wave rising from zero to a positive maximum, falling through zero to an equal negative maximum, and returning — over and over, fifty complete cycles per second in South Africa. The current graph through a resistor is the same shape, rising and falling in step with the voltage. Positive and negative halves simply mean the current flows first one way around the circuit, then the other. A DC graph, by contrast, is a flat horizontal line: constant voltage, one direction forever.

Sketching tips that earn marks: label the maximum voltage V max on the peaks, mark equal positive and negative peaks, and show at least one full cycle. If asked for the current graph in a purely resistive circuit, draw it peaking at the same instants as the voltage — current and voltage rise and fall together in a resistor.

This section's questions arrive now — transformers plus the I squared R argument explain the grid, and the wave crossing zero is a current changing direction.

## Subtopic: RMS Values and Average Power

A puzzle: if AC voltage swings symmetrically positive and negative, its average is zero — yet a kettle on AC boils water. Clearly the simple average is the wrong tool. Heating does not care about direction; it depends on current SQUARED, which is positive in both halves of the cycle. The honest measure of AC is the ROOT MEAN SQUARE value: the rms voltage or current is the equivalent DC value that would deliver the same energy to a resistor. For the sine waves of the grid, the rms values are the maxima divided by the square root of two: I rms equals I max over root two, and V rms equals V max over root two.

The number on your wall plug — 220 volts — is an rms value. The actual peaks are larger: V max equals 220 times root two, which is 311,13 volts. The mains swings between plus 311 and minus 311 volts, and 220 is the DC-equivalent rating hiding inside that swing. Insulation and components must survive the peak; energy bills are computed from the rms.

Average power in a purely resistive circuit uses rms values exactly as DC would: P average equals I rms times V rms, and the two variants I rms squared times R and V rms squared over R follow from Ohm's law. Worked example: a heater of resistance 44 ohms on the 220 volt mains. I rms equals 220 divided by 44 — 5 amperes. Average power: 220 times 5, which is 1100 watts. The maximum current is 5 times root two — 7,07 amperes — and the instantaneous power at the peak of the cycle is double the average: 2200 watts. That factor of two is worth remembering: average power equals half of I max times V max.

The final expert questions are with you now — rms is the DC-equivalent, divide maxima by root two, and power calculations use rms throughout.

# Part 2 — Simplifier

Now the same machinery from the bicycle shed and the kitchen: a dynamo on a wheel, one machine with two personalities, and what 220 volts honestly means.

## Subtopic: The Dynamo on the Bicycle Wheel

An old bicycle dynamo is a generator you can hold in one hand. Flick its little wheel against the tyre, pedal, and the headlamp glows. Pedal faster, it glows brighter. Stop, and it dies instantly. Inside there is nothing but a magnet, a coil, and your legs — and that is the entire secret of the world's power stations.

The rule the dynamo lives by: move a magnet and a coil relative to each other, and the coil produces a voltage. Not magnets alone — a magnet lying beside a coil forever produces nothing. Not coils alone. CHANGE is what pays: flux through the coil growing and shrinking as the parts spin past each other. Your pedalling supplies the motion, and the glowing lamp is your leg-work converted into electrical energy. Notice you can FEEL the conversion: engage the dynamo and pedalling gets slightly harder. The lamp's light is not free — it is bought from your muscles, which is energy conservation working exactly as promised.

A power station is the same dynamo scaled up absurdly: instead of your legs, steam pressure from burning coal, or falling water, or wind spins a turbine, and the turbine spins a coil the size of a bus inside a magnetic field. Eskom is a bicycle dynamo with a very big rider. And the reason the output naturally comes out alternating: as the coil spins, each side sweeps up through the field, then down, then up again — so the pushed current sloshes back and forth in rhythm with the spin.

Your first questions are with you now — no change, no charge: only moving magnetism makes electricity.

## Subtopic: One Machine, Two Personalities

Here is a party trick that is also deep physics: a generator and a motor are the same machine, used in opposite directions. Spin the shaft, and electricity comes out of the wires — generator. Push electricity into the wires, and the shaft spins — motor. Coil, magnets, brushes: identical parts, opposite personalities, depending only on which side you feed.

Why does feeding in current cause spinning? Because the magnetic field pushes on any wire carrying current through it — that is the motor effect. The two sides of the coil carry current in opposite directions, so one side is shoved up while the other is shoved down, and the coil turns like a revolving door pushed on both wings. There is one engineering wrinkle: after half a turn, those pushes would start undoing the rotation. The fix is a small split ring that swaps the current direction every half turn, precisely on cue, so the shove always favours the same rotation. Swap timed right, spin forever.

Once you see the two personalities, you see them everywhere. The fan on your desk: motor. The dynamo: generator. An electric vehicle does BOTH with one machine — driving, the battery feeds the coil and the wheels turn; braking, the wheels turn the coil and pump energy back into the battery. Same copper, both directions, sometimes in the same minute.

Questions on this section are coming to you now — spin it and it makes current; feed it current and it spins.

## Subtopic: What 220 Volts Actually Means

The socket in your wall says 220 volts, but the voltage there is never simply 220. It is a wave: swinging up to about plus 311 volts, down through zero to minus 311, and back — fifty round trips every second. The current in your kettle sloshes forward and backward fifty times a second too. So what is the 220? It is the honest average — but a clever kind of average.

The naive average fails: the wave spends as much time negative as positive, so its plain average is zero, and zero volts boils no water. But the kettle does not care which way current flows — heat comes from current squared, and a squared number is positive both ways. The sloshing current heats on the forward stroke AND the backward stroke, like sandpaper heating wood on both the push and the pull. Average the HEATING rather than the voltage, and you get the rms value: the steady DC voltage that would cook exactly as fast as the wave does. For the grid's smooth wave, that honest number is the peak divided by the square root of two — 311 divided by 1,414 gives 220.

So a 2200 watt kettle on 220 volts draws 10 amperes — in rms terms, the DC-equivalent books. The real current peaks higher, near 14 amperes, twice every cycle, and the wiring is rated to survive the peaks. But your electricity bill, your appliance labels, and every power calculation in the exam run on the rms numbers, because rms is the value that tells the energy truth. One wave, two descriptions: peak for the engineer choosing insulation, rms for everyone paying for the joules. The last questions of the lesson are yours now — 220 is the wave's DC-equivalent, and the peaks stand root-two taller.
