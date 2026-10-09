### subtopic_1 — The PAT Scenario: A Need That an Electronic Device Can Meet
**Assistant:** Why does the investigation spend so long on the grandmother when the task is to build a circuit?

**Tutor:** Because the circuit will be judged by whether it helps her, not by whether it works on a bench, and most of the decisions that make it helpful come from her and her setting rather than from electronics. Her eyesight decides that the indicator must be a big bright LED and not a tiny one. Her dislike of noise at night decides that any buzzer needs an off switch. Her kitchen window decides where the output goes and how long the wire must be. The sunlight decides the LED's brightness and colour. The lack of mains decides the battery and therefore how little current the circuit may draw. A team that skips her and builds the circuit from a textbook will produce something technically fine and practically useless, and the PAT marks for investigation are given for exactly this kind of finding out. The electronics are the easy part; knowing what to build is the hard part.

***

### subtopic_2 — Investigating Users, Settings and Existing Devices
**Assistant:** What if the existing products all do the job well? Is there any point designing our own?

**Tutor:** Yes, for two reasons that the investigation should write down. First, the existing products are usually a poor fit for the actual user. The ultrasonic gauge needs mains power and costs more than the tank. The LED ladder is designed to sit on the tank, not in a kitchen window ten metres away. The float switch comes with a short wire and a dim lamp. Each solves the general problem and misses the particular one, and recording exactly how it misses is what tells you what your device must do differently. Second, the purpose of the PAT is to learn to design, and studying good existing products is how designers have always learnt. Borrow the float switch idea, borrow the LED indicator, reject the mains supply, add the long wire and the bright LED, and you have a design that is genuinely yours and genuinely better for this household.

***

### subtopic_3 — From Need to Circuit: What the Electronics Must Do
**Assistant:** How do I turn her answers into things the circuit must do?

**Tutor:** Take each answer and ask what component or value it forces. She wants to see it from the kitchen window: so the output must be an LED, it must be bright enough for daylight, which means a high-brightness LED with the right series resistor, and it must be in the kitchen, which means either a long two-core wire from the tank sensor or the sensor mounted where the pipe enters the house. She does not want a buzzer at night: so if the team adds a buzzer, it needs its own switch, and the LED must work without it. She will not change a battery often: so the circuit must draw almost no current when the tank is full, which pushes you toward a sensor that is an open switch until the level drops, rather than one that runs all the time. Each user sentence becomes an electronic sentence with a component in it. Write them in pairs on the investigation page and the design brief practically writes itself.
