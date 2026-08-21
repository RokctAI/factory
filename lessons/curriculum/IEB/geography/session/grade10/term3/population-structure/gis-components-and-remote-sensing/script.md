# Part 1 — Expert

Behind every population map you have met this term — density shading, growth curves mapped onto provinces, migration arrows — stand two technologies working as a team: a Geographical Information System, which stores and interrogates the data, and remote sensing, which gathers a huge share of that data from above the earth. This session builds the proper definition of a GIS, walks through its five components and the layer principle that gives it power, then defines remote sensing, separates satellite images from aerial photographs, and ends with the ways South Africa points both tools at its own population.

## Subtopic: What a GIS Is — Layers of Information

A GEOGRAPHICAL INFORMATION SYSTEM, or GIS, is a computerised system that captures, stores, analyses, manages and displays geographically referenced information — information anchored to a definite position on the earth's surface.

Read that definition as two halves, because each half carries marks. Half one: a GIS is a DATABASE — it holds and processes data. Half two: the data is GEOREFERENCED — every record knows its location, normally through latitude and longitude coordinates. A list of hospital names in a document is only a list; attach coordinates to each hospital and it becomes geographical information that a GIS can plot, query and compare.

The idea that organises everything inside a GIS is the LAYER. Each theme of information about an area lives on its own transparent sheet: rivers on one layer, the road network on another, homesteads and towns on a third, rainfall on a fourth, population density on a fifth. Because all the layers share one coordinate system, the computer can lay any selection of them over the same ground in perfect registration.

Combining layers is called OVERLAY ANALYSIS, and it is what turns a GIS from a map cabinet into an analytical machine. Where should a district build its next high school? Stack the layer of school-age population, the layer of existing schools and the road layer, then ask for areas thick with learners but further than a set distance from any school and reachable by road. Which farmhouses stand inside the hundred-year floodline? Lay the buildings layer over the floodplain layer and read off the intersection. The GIS answers WHERE questions by weighing several maps at once — something no single paper map can do.

Every feature on those layers carries two kinds of data. SPATIAL DATA describes where the feature sits and what geometry it has — a point, a line, an area. ATTRIBUTE DATA describes the feature itself — its measurable and nameable characteristics. For a hospital, the spatial data is its coordinates; the attribute data is its name, its number of beds, whether it has a trauma unit. Select a feature on screen and its attribute table opens — that welded link between position and description is the essence of GIS.

Take this section's questions now: the definition with both halves, the layer principle and overlay analysis, and spatial against attribute data.

## Subtopic: The Five Components of a GIS

A GIS is not merely a program installed on a computer. The complete system has FIVE components, and listing them with a phrase of explanation each is one of the most dependable questions in this topic.

One: HARDWARE — the physical machinery. The computers and servers that hold and crunch the data, the screens that display maps, printers and plotters that produce them on paper, and the capture devices in the field — above all GPS receivers, one of which lives inside every smartphone sold today.

Two: SOFTWARE — the programs that perform the GIS operations of capture, storage, analysis and display. Professionals work in packages such as QGIS, which is free, and ArcGIS; in the broad sense, the mapping application on a phone is GIS software as well.

Three: DATA — the component specialists rank as the most valuable and the most costly to build. The finest computer running the finest program produces rubbish if the layers it chews on are wrong or stale. Data reaches a GIS from field surveys, GPS capture, digitised maps, administrative records and, on an enormous scale, from remote sensing. In South Africa the national census run by Statistics South Africa is a landmark data harvest, and its counts flow directly into the GIS layers on which schools, clinics and pipelines are planned.

Four: PEOPLE — trained operators to capture and clean the data, analysts to run and interpret the overlays, and decision-makers to act on the results. The system computes; humans conclude.

Five: PROCEDURES, also called methods — the working rules that keep the whole operation trustworthy: schedules for updating layers, standards for checking accuracy, records of who changed what and when.

A one-line summary holds them together: hardware and software are the engine, data is the fuel, people steer, procedures are the service manual. Remove any component and the system degrades — stale fuel misleads, unskilled steering crashes, and without the manual, errors accumulate unseen.

Pause for this section's questions: the five components named, why data is ranked first, and what each contributes.

## Subtopic: Remote Sensing — Information Without Contact

REMOTE SENSING means collecting information about the earth's surface from a distance, with no physical contact — using sensors mounted on satellites in orbit or on aircraft.

The physics is reflection. Solar energy pours onto the earth, and every kind of surface bounces it back differently: green leaves, dry grass, open water, tar, corrugated iron — each returns its own mixture of visible light and invisible wavelengths such as infrared. The SENSOR aboard the platform measures the returning energy, and software assembles the measurements into an image. Because sensors register wavelengths beyond human vision, their images reveal what no ordinary photograph can: crops under drought stress before any wilting shows, dampness held in soil, the heat signature of a burning veld fire through its own smoke.

Now separate the two platforms, because questions do. SATELLITE IMAGES come from orbit — from workhorses like the Landsat series, imaging the earth continuously since 1972, and the European Sentinel fleet. A satellite sweeps enormous areas and, decisively, revisits the same ground on a fixed schedule, building a time series: the same dam, the same city edge, photographed every few days for years. AERIAL PHOTOGRAPHS are taken from aircraft at far lower altitude, trading coverage for detail: small areas, fine resolution. Geometrically corrected aerial photographs — orthophotos — are the foundation of South Africa's 1 to 10 000 orthophoto map series, the large-scale sheets on which individual buildings can be seen.

The strengths of remote sensing follow from the setup. Reach: it observes places no field team can easily go — open ocean, desert, high mountains, disaster zones. Repetition: because the satellite returns, it detects CHANGE — set two images side by side and deforestation, shrinking dams and spreading suburbs declare themselves. Economy and safety: per square kilometre it is cheap, and nobody's boots touch dangerous ground. The limits deserve equal weight: cloud blinds optical sensors; images mean nothing without trained interpretation; and a sensor registers structures, not circumstances — it can count the roofs of a settlement but cannot learn a single resident's age, language or employment. The ground census stays irreplaceable. GIS and remote sensing therefore work as partners: the sensor harvests, the GIS files the harvest as a layer and analyses it against all the others.

Your questions on this section are ready now: the definition, how reflected energy becomes an image, satellite images against aerial photographs, and the strengths and limits.

## Subtopic: Satellites, Aerial Photographs and Population Work

Now aim the toolkit at this term's subject — people — through South African applications worth quoting in any answer.

Watching the informal edge grow. Metros such as Ekurhuleni and Buffalo City expand fastest along their informal fringes, in the years between censuses, while official records fall behind. Satellite images captured a few months apart reveal each new cluster of roofs; analysts trace them into a GIS layer of recent settlement and overlay water, sanitation and clinic layers — and the map of households living beyond the reach of services assembles itself. That map decides where the next standpipes and mobile clinics are sent.

Preparing and checking the census. Before a single household is visited, Statistics South Africa uses aerial photography and satellite imagery to carve the entire country into small enumeration areas and to verify that every dwelling — down to the newest shack on the newest fringe — appears on some enumerator's map. Afterwards the counts become attribute data behind density and service-planning layers, and the enumeration boundaries themselves live on as GIS products.

Disasters. When fires swept through Knysna and along the Garden Route in June 2017, satellite sensors mapped the burn scars and before-and-after images showed which neighbourhoods had been destroyed while roads were still closed; overlaying damage on population layers directed relief to where the most people had lost the most. During the Western Cape drought that threatened Cape Town with Day Zero, satellite time series of Theewaterskloof Dam showed the water surface contracting month by month — hard evidence for rationing decisions affecting millions.

Food security. Infrared-reading sensors measure crop vigour across entire provinces, flagging failing maize and sunflower harvests in the North West or Free State months before shortfalls reach markets — early warning that matters directly to feeding a population.

Name the national capacity too. The South African National Space Agency, SANSA, receives and distributes satellite data at its Hartebeesthoek ground station, and South African engineers have built and flown small earth-observation satellites, among them the nanosatellite ZACube-2, which monitors veld fires and ship traffic along our coast. And every phone-guided journey — GPS position, remote-sensed imagery, GIS road layers — runs the same three technologies you have just learned, in miniature.

The final questions of this part are with you now: informal settlements, the census, disaster response, and South Africa's own space capacity.

# Part 2 — Simplifier

Now the same machinery through a phone, a pile of tracing paper and an eye in the sky.

## Subtopic: The Smartphone Map You Already Use

Late on a Sunday, someone in your house needs medicine, and you grab a phone and search for a pharmacy that is open. A map slides up: a blue dot for you, pins for the pharmacies, one marked open until ten, and a route threading through the streets toward it. In those five seconds, a complete Geographical Information System ran in your hand.

Check it against the definition, phrase by phrase. Geographically referenced information: every pharmacy on that map carries coordinates. Stored: on the map provider's servers. Analysed: the app filtered for open now, ranked by distance, and computed the quickest route. Displayed: the map glowing on the screen. Captured, stored, analysed, displayed — georeferenced throughout. That is the definition of a GIS, ticked off item by item.

Now find the five components inside the moment. Hardware: the phone, its GPS chip, and the server farms far away. Software: the mapping app. Data: every street, every shop, every opening time — the piece that cost years and fortunes to gather, which is why data is called the most valuable component. People: you, framing the question and choosing the pharmacy. Procedures: the provider's update rules — the reason the new roundabout appears on the map within weeks, and the reason a pharmacy that closed down eventually loses its pin.

One last pair of terms and the pocket example is complete. The app knows two sorts of things about that pharmacy. WHERE it stands — the pin. That is spatial data. WHAT it is — its name, its hours, its phone number. That is attribute data. Tap the pin, and the attributes unfold. Location stitched to description: the entire trick of GIS, demonstrated in one tap.

Quick check — this section's questions are coming to you now: the definition matched to the phone, the five components found in your pocket, and the pin against the facts behind it.

## Subtopic: A Stack of Tracing Paper

Here is the idea that upgrades a GIS from an electronic map book into a thinking machine — and you can build it yourself with tracing paper.

Choose one rural district. On the first sheet of tracing paper, trace its rivers. On a second sheet, exactly the same size, the gravel roads. On a third, every homestead. On a fourth, shade where the people are thickest. On a fifth, mark the schools. Five sheets, one theme each, all drawn to one scale over one piece of ground.

Each sheet alone answers only its own narrow question. But square up the corners, press the pile flat against a window, and let the light come through — suddenly the sheets argue with each other. Here the homestead sheet is crowded but the school sheet is blank: children walking hours to class, exposed in a glance. There a line of homesteads sits inside the river sheet's floodplain: a warning nobody had noticed. And the road sheet shows which single road a bus or a water tanker could use to reach them.

That pile against the window is exactly what a GIS keeps in memory — with two superpowers added. Speed: the computer stacks any combination in an instant — rainfall over grazing, new settlement over clinics — where paper would bury you. And questioning: the computer can interrogate the whole pile at once — list every homestead more than five kilometres from a school; find the crossings where road meets river. The professionals call it overlay analysis. You can call it pressing the pile to the window.

But the window trick has the same weakness as any recipe: bad ingredients, bad result. If the school sheet is six years old, the analysis will demand a school where one already stands. That is why data is the expensive component, and why procedures — the update rules — exist. A GIS cannot make stale data true; it can only make it look authoritative.

Questions on the layers are up now: what a layer is, what stacking lets you ask, and why stale data is the danger.

## Subtopic: The Eye in the Sky and the Census

Final piece: where do all those layers come from? A remarkable share comes from machines that never touch the ground.

Remote sensing is learning about the earth's surface WITHOUT touching it — sensing from a distance with instruments on satellites and aircraft. The satellite's gifts are size and rhythm: it sees a vast area in one pass and returns over the same spot every few days, indefinitely. Play its images in order like film frames and the landscape starts moving — the water line of Theewaterskloof Dam creeping backwards through the Cape drought, suburbs pushing outward year by year, a coastline redrawing itself. The aircraft flies low and slow by comparison, photographing small patches in beautiful detail — and corrected aerial photographs, orthophotos, underlie South Africa's 1 to 10 000 maps, where you can pick out single rooftops.

The sensors also out-see us. They read light our eyes cannot, infrared above all — and thriving plants blaze in infrared while struggling plants dim. That is how a satellite tells healthy maize from failing maize across an entire province, and how a harvest warning can sound months before the silos confirm it.

Now weld the eye in the sky to the counting of people, because that is the connection this topic examines. A metro's informal fringe grows week by week, far ahead of any office file. Two satellite images a few months apart show precisely where new roofs have sprouted; those roofs become a GIS layer; stack it over the water, toilet and clinic layers and the map points to where services must go next. Before each census, Statistics South Africa uses aerial and satellite images to slice the country into enumeration areas so that every dwelling falls inside somebody's route — nobody invisible to the count. And when fire tore through Knysna in June 2017, before-and-after satellite images showed rescuers and planners which streets had burned while the smoke still blocked the roads.

Hold on to the limit, though, because the best answers always state it: the satellite counts ROOFS, never people. It cannot ask who sleeps under the roof, their ages, their language, whether they found work. For those answers a human being still walks up the path and knocks. The eye in the sky and the person at the door are partners — one sees everywhere, the other asks everything.

The final questions of the lesson are with you now — sensing without touching, satellites against aircraft, the roof-counting trick, and the limit only a human can cross.
