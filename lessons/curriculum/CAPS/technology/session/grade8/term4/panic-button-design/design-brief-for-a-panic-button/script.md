# Part 1 — Expert

This session covers writing a design brief for a panic button system. The anchor is Gogo Mahlangu, seventy-eight, who lives alone in a two-room house in Mamelodi, whose neighbour is a shout away but whose phone is often flat, and whose granddaughter has asked the Grade 8 class to design something that calls help from the bedroom, the kitchen and the toilet outside.

## Subtopic: The Scenario: Who Needs a Panic Button and Why

Design begins with a need, and the need here is a person who cannot reliably summon help. Investigate the scenario by asking who, where, when and what. Who: Gogo Mahlangu, elderly, living alone, mobile but slow, with arthritis in her hands, who sleeps in one room, cooks in another and uses a toilet in the yard. Where: a small house with a yard, a neighbour across the fence who is home most evenings, a street with some passing people, and no alarm company in the area. When might she need help: a fall at night, a stranger at the door or in the yard, a sudden illness, a fire from the paraffin stove. What help exists: the neighbour, who would come if called; a daughter who lives twenty minutes away and has a phone; passers-by who would notice a loud noise.

The same investigation generalises. Across South Africa panic buttons serve households worried about crime, elderly and disabled people living alone, shop and spaza owners, farm workers in isolated places, learners and teachers in schools, and domestic workers alone in large houses. Commercial systems exist, from a wireless button that signals an armed response company to an app that sends a location to a contact list, and they are worth studying as existing solutions: they show what works, what costs, and who is left out, because a monthly fee of several hundred rand excludes exactly the households most at risk. A school project cannot build an armed response network, but it can build a system that makes a loud, unmistakable local alarm from any of several points in a home, and that is a genuine need met at a price a family can afford.

Investigation also means talking to the user, or imagining doing so honestly. Gogo would say: I cannot reach a high switch; my hands do not press small buttons well; I need it to work in the dark and when the power is off; I need it by the bed, the stove and the toilet; I want to be able to stop it when it is a mistake; and I do not want to pay every month. Each of those is a fact that will become a specification.

The questions for this section are with you now: the who, where, when and what of the scenario, who else needs panic buttons, and what the user herself would ask for.

## Subtopic: Writing the Design Brief: Problem, Users, Purpose

A design brief is a short statement of the problem to be solved, the people it is solved for, and the purpose the solution serves. It is written before any drawing, because a brief fixes what success means, and it is written in a few clear sentences, because a brief that runs to a page has started designing instead of briefing. The three parts are the problem, which states the need without naming a solution; the users, which says who will use it and what they are like; and the purpose, which says what the device must achieve for them.

For the scenario, a good brief reads: "Problem: an elderly woman living alone in Mamelodi has no reliable way to call for help in an emergency from the rooms she uses, especially at night or when her phone is flat. Users: Gogo Mahlangu, who is slow-moving with weak hands and poor night vision, and the neighbour and passers-by who must hear and respond. Purpose: to design and make a battery-powered alarm system with a button at the bed, the stove and the outside toilet, any one of which sets off a loud siren and a bright light that the neighbour can hear and see, and which Gogo can switch off herself."

Notice what the brief does and does not do. It names the need, the user and the goal, and the places the buttons must be, which is a fact of the need. It does not say what kind of switch, what voltage, or how the buttons connect, because those are design decisions still to be made. A common mistake is a brief that reads "design a circuit with three push switches in parallel and a buzzer", which is a solution pretending to be a brief; another is a brief so vague, "design something to help Gogo", that nothing could fail it. The test of a good brief is that two different designers could read it and produce two different designs that both satisfy it.

The questions for this section are with you now: the three parts of a brief, the example brief for Gogo, and what a brief must and must not include.

## Subtopic: Specifications and Constraints: What the Device Must Do and Must Not Be

Specifications are the measurable requirements the finished device must meet; constraints are the limits the design must work within. Both are drawn directly from the investigation and the brief, and each should be testable, so that at the end you can say whether the device meets it.

Specifications for Gogo's system: the alarm must be triggered by any one of three buttons, at the bed, the stove and the toilet, pressed alone; each button must be large enough to press with the flat of a weak hand, not a fingertip, at least thirty millimetres across, and mounted low enough to reach from the floor after a fall; the alarm must sound loudly enough to be heard across the fence, judged by a test at the neighbour's door; the alarm must also light a bright lamp visible from the street, for a neighbour who is hard of hearing and for passers-by at night; the system must run from batteries so that it works during load shedding and when the prepaid is empty; the buttons must glow or be marked so they can be found in the dark; there must be a reset switch in the house that only Gogo uses to silence the alarm; and the system must keep working for at least a year on one set of batteries in standby, which means the alarm draws power only when triggered.

Constraints: the model must be built from the components available in the class kit, cells, switches, a buzzer, LEDs and resistors, wire and board; the whole system must cost under a stated budget, say two hundred rand in real components, so that a family could afford it; the circuit must use only low voltage, never mains; it must be buildable by the class in two sessions; the wiring to the outside toilet must be weatherproof or the toilet button must be wireless, which in the model can be shown by a long lead; and the design must be documented with a circuit diagram and a truth table, which is the next lesson. The truth table is already implied: three inputs, eight rows, output 1 in every row except the first, a three-input OR, but writing that now would be jumping to the solution; the specification says "any one button", and next lesson derives the gate from it.

The error museum, four exhibits. One: a brief that is a solution, "three switches in parallel with a buzzer". Two: specifications that cannot be tested, "it must be easy to use", instead of "pressable with the flat of a hand". Three: forgetting load shedding and specifying a mains-powered alarm. Four: a budget that ignores the family's means and specifies an armed-response subscription.

The questions for this section are with you now: the difference between a specification and a constraint, the specifications for Gogo's system, and the constraints on the design.

# Part 2 — Simplifier

Now the same lesson again with Gogo Mahlangu's two-room house, a flat phone and a neighbour across the fence — plain words, same facts.

## Subtopic: The Need

Design starts with a need, and here the need is a person who cannot be sure of calling help. Ask who, where, when, what. Who: Gogo, seventy-eight, alone, slow, arthritis in her hands, sleeps in one room, cooks in another, toilet in the yard. Where: a small house, a yard, a neighbour across the fence most evenings, a street with people passing, no alarm company. When: a fall at night, a stranger in the yard, sudden illness, a paraffin fire. What help exists: the neighbour who would come if called, a daughter twenty minutes away with a phone, passers-by who would notice a loud noise.

The same questions work everywhere. Panic buttons serve homes worried about crime, elderly and disabled people alone, spaza owners, farm workers far from anyone, schools, domestic workers alone in big houses. Shop systems exist, a wireless button to an armed response firm, an app that sends your location, and they are worth studying: they show what works and what it costs, and a monthly fee of hundreds of rand leaves out the people most at risk. A class cannot build an armed response network; it can build a loud local alarm from several points in a home at a price a family can pay. That is a real need met.

Ask the user, or imagine honestly. Gogo would say: I cannot reach a high switch; small buttons are hard for my hands; it must work in the dark and when the power is off; by the bed, the stove and the toilet; I must be able to stop it if it is a mistake; no monthly fee. Every one of those becomes a specification.

Hold the toilet in the yard in mind and try the questions for this part: the need.

## Subtopic: The Brief in Three Sentences

A design brief says three things: the problem, the users, the purpose. Write it before any drawing, because it fixes what counts as success, and keep it to a few sentences, because a long brief has started designing.

For Gogo: "Problem: an elderly woman living alone in Mamelodi has no reliable way to call for help from the rooms she uses, especially at night or when her phone is flat. Users: Gogo Mahlangu, slow-moving, weak hands, poor night vision, and the neighbour and passers-by who must hear and respond. Purpose: design and make a battery-powered alarm with a button at the bed, the stove and the outside toilet, any one of which sets off a loud siren and a bright light the neighbour can hear and see, and which Gogo can switch off herself."

What it does: names the need, the user, the goal, and where the buttons must be, which is part of the need. What it does not do: say what switch, what voltage, how the buttons join; those are design decisions. Two traps. A brief that reads "three push switches in parallel with a buzzer" is a solution in disguise. A brief that reads "design something to help Gogo" is so vague nothing could fail it. Good test: two designers read it and make two different designs that both pass.

Hold the brief's three labels, problem, users, purpose, in mind and try the questions for this part: the brief in three sentences.

## Subtopic: Musts and Must-Nots

Specifications are what the finished device must do, measurable. Constraints are the limits you must work inside. Both come from the investigation and the brief, and each must be testable, so at the end you can say met or not met.

Specs for Gogo: any one of three buttons, bed, stove, toilet, pressed alone, sets off the alarm; each button big enough for the flat of a weak hand, at least thirty millimetres, mounted low enough to reach from the floor after a fall; loud enough to hear across the fence, tested at the neighbour's door; a bright lamp too, visible from the street, for a deaf neighbour and night passers-by; battery powered, so it works in load shedding and when prepaid is empty; buttons that glow or are marked for the dark; a reset switch indoors that only Gogo uses; a year of standby on one set of batteries, so the alarm draws power only when triggered.

Constraints: built from the class kit, cells, switches, buzzer, LEDs, resistors, wire, board; real cost under a set budget, say two hundred rand, so a family could afford it; low voltage only, never mains; buildable by the class in two sessions; the toilet wiring weatherproof or wireless, shown in the model by a long lead; documented with a circuit diagram and a truth table, next lesson. The table is already hiding in the spec: three inputs, eight rows, 1 everywhere but the first, a three-input OR; but writing it now would be leaping to the answer; the spec says "any one button", and next lesson gets the gate from that.

Pocket summary of the lesson. Investigate who, where, when, what, and ask the user. Brief: problem, users, purpose, a few sentences, no solution, not vague. Specs: testable musts, three buttons, big and low, loud and bright, battery, dark-findable, reset, a year of standby. Constraints: kit, budget, low voltage, two sessions, weatherproof, documented.

Hold the thirty-millimetre button near the floor in mind, and take the final questions of the lesson: musts and must-nots.
