### subtopic_1 — The Simple Series Circuit: Cell, Switch and Lamp
**Assistant:** Why does the voltmeter read the full battery voltage across an open switch when nothing is flowing?

**Tutor:** Because with the switch open, the switch is the only place in the loop where the battery's push is not being used up. Think of the battery as trying to drive current round the loop. With the switch closed, the current flows and almost all the battery's voltage appears across the lamp, where the work is done; the closed switch is just a piece of metal with nearly no voltage across it. Open the switch and no current flows anywhere, so the lamp has no voltage across it at all, and the whole of the battery's voltage sits waiting across the gap in the switch, between the contact connected to the battery's positive side and the contact connected, through the lamp, to the negative side. The voltmeter, which draws almost no current itself, reads that waiting voltage. This is actually a useful fault-finding trick: a voltmeter reading full voltage across a component in a dead circuit tells you that component is the break.

***

### subtopic_2 — Building, Fault-Finding and Measuring the Circuit
**Assistant:** Can I just use a bigger battery to make the lamp brighter?

**Tutor:** A little, but only within the lamp's rating, and beyond it you will burn the lamp out. A lamp's filament is designed to run at a certain temperature at its rated voltage; push more voltage through it and more current flows, the filament gets hotter and brighter, and within a few seconds or minutes it melts. A 4.5 volt bulb on 6 volts is noticeably brighter and lasts hours instead of years; on 9 volts it flashes once and is dead. The right way to get more light is a lamp rated for the voltage you have, or several lamps in parallel each getting the rated voltage. This matters for the PAT: an LED has no safe margin at all, and the only way it survives a 4.5 volt battery is the series resistor next week, which does the matching job that choosing the right bulb does here.

***

### subtopic_3 — From the Series Circuit to the PAT Indicator Circuit
**Assistant:** Why does the fault-finding order go supply, load, switch, leads instead of just checking everything?

**Tutor:** Because the order goes from the most likely and easiest to test to the least likely and fiddliest, and because each test gives you information that narrows the next one. Touching the lamp straight onto the battery terminals tests two parts at once, the supply and the load, in one second with no tools; if it lights, you have eliminated the two components most likely to be dead and you know the fault is in the switch or the leads. Bridging the switch tests it in one move. Only then do you go through the leads one by one, and by then you know which section they are in. Checking everything at once, wiggling three leads while pressing the switch, might make it light briefly but tells you nothing about which part was wrong, so the fault comes straight back. Methodical narrowing is how electricians and technicians work on real faults, and the PAT model will reward it.
