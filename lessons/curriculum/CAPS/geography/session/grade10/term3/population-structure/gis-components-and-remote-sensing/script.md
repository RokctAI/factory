# Part 1 — Expert

Every population map in this term — density maps, growth maps, migration maps — was almost certainly made with two technologies working together: a Geographical Information System that stores and analyses the data, and remote sensing that collects much of it from above. This session defines a GIS properly, works through its five components and its layer principle, then defines remote sensing, distinguishes satellite images from aerial photographs, and shows how South Africa uses both to count, plan for and serve its people.

## Subtopic: What a GIS Is — Layers of Information

A GEOGRAPHICAL INFORMATION SYSTEM, or GIS, is a computerised system that captures, stores, analyses, manages and displays geographically referenced information — that is, information tied to a specific position on the earth's surface.

The definition has two halves and both earn marks. The first half says a GIS handles DATA: it is a database. The second half says the data is GEOREFERENCED: every entry knows its position, usually through coordinates of latitude and longitude. A spreadsheet of clinic names is just a list; the moment each clinic carries its coordinates, the list becomes geographical information a GIS can map and interrogate.

The organising idea of every GIS is the LAYER. Each theme of information about an area is stored as a separate transparent sheet: one layer holds the rivers, another the roads, another the settlements, another rainfall, another population density. Because every layer is georeferenced to the same coordinate system, the computer can stack any combination of them, perfectly aligned, over the same piece of ground.

That stacking is called OVERLAY ANALYSIS, and it is the power of the whole system. Questions no single map could answer become simple. Where should a new clinic go? Stack the population density layer, the existing clinics layer and the roads layer, and ask the computer for densely populated places more than ten kilometres from any clinic but close to a road. Which schools lie inside a flood zone? Stack schools over the floodplain layer and the answer falls out. The GIS is not just an electronic atlas; it answers WHERE questions by combining evidence.

A GIS stores two kinds of data about everything on those layers. SPATIAL DATA records where a feature is and what shape it has. ATTRIBUTE DATA records what the feature is like — the descriptive facts attached to it. For a school, the spatial data is its position; the attribute data is its name, the number of learners, the language of instruction. Click a feature on a GIS map and the attribute table opens: that link between position and description is the heart of the system.

Take this section's questions now: the definition with both halves, the layer principle and overlay analysis, and spatial against attribute data.

## Subtopic: The Five Components of a GIS

A GIS is more than software on a laptop. The standard answer lists FIVE components, and a component question is one of the most predictable in this topic.

Component one: HARDWARE — the physical equipment. Computers and servers that store and process the data, screens that display it, printers and plotters that output maps, and the field equipment that captures positions, above all GPS receivers, including the one inside every smartphone.

Component two: SOFTWARE — the programs that do the GIS work: capturing, storing, analysing and displaying the layers. Professional packages such as ArcGIS and the free QGIS are the tools planners use; in a looser sense, familiar mapping applications on a phone are GIS software too.

Component three: DATA — and this is the component experts call the most important and the most expensive. Without accurate, up-to-date georeferenced data, the finest hardware and software produce nonsense. Data enters a GIS from surveys, from GPS capture, from digitised paper maps, from census records, and — massively — from remote sensing. South Africa's census, run by Statistics South Africa, is one of the country's great data harvests, and its results flow straight into GIS layers used for planning.

Component four: PEOPLE — the trained operators, analysts and decision-makers who capture the data, run the analysis and interpret the results. A GIS proposes; people decide.

Component five: PROCEDURES, sometimes called methods — the rules and step-by-step ways of working that keep the system reliable: how data is checked, how often layers are updated, how accuracy is verified, who may change what.

Hold the five in a sentence: hardware and software do the work, data feeds them, people drive them, procedures keep them honest. Drop any one and the system fails — outdated data misleads, untrained people misread, missing procedures let errors breed silently.

Pause for this section's questions: the five components named, why data is called the most important, and what each component contributes.

## Subtopic: Remote Sensing — Information Without Contact

REMOTE SENSING is the gathering of information about the earth's surface from a distance, without physical contact — from sensors carried on satellites orbiting the earth or on aircraft flying above it.

The principle is reflection. The sun's energy strikes the earth, and every surface reflects it differently: healthy vegetation, bare soil, water, tar and tin roofs each return their own signature of visible light and invisible wavelengths such as infrared. A SENSOR on the satellite or aircraft measures the reflected energy, and a computer converts those measurements into an image. Because sensors read wavelengths the human eye cannot, remote sensing images can show things no photograph from a window seat could — stressed crops before they wilt visibly, moisture in soil, heat leaking from a city.

Distinguish the two main platforms. SATELLITE IMAGES are captured from space by satellites such as the Landsat series, which has photographed the earth continuously since 1972, and the European Sentinel satellites. A satellite covers enormous areas and, crucially, returns over the same spot again and again on a fixed cycle, so it builds a time series — the same city photographed every few days for decades. AERIAL PHOTOGRAPHS are taken from aircraft flying far lower, so they show much finer detail over much smaller areas. South Africa's mapping agency uses corrected aerial photographs, called orthophotos, as the base for the 1 to 10 000 orthophoto maps used in mapwork.

The strengths of remote sensing follow directly. It covers vast and inaccessible areas — ocean, desert, mountain, conflict zones — that ground surveys cannot reach. It repeats, so it detects CHANGE: compare this year's image with last year's and the difference is deforestation, dam levels, urban growth. It is safe and, per square kilometre, cheap. Its limits matter too: clouds block optical sensors, images need skilled interpretation, and a satellite can see a settlement but cannot knock on a door and ask who lives there — remote sensing counts roofs, not names, so the census on the ground remains irreplaceable. Remote sensing and GIS are partners: the sensor collects, the GIS stores the result as a layer and analyses it against everything else.

Your questions on this section are ready now: the definition, how reflected energy becomes an image, satellite images against aerial photographs, and the strengths and limits.

## Subtopic: Satellites, Aerial Photographs and Population Work

Now put the toolkit to work on this term's subject — population — with South African examples an examiner will recognise.

Tracking informal settlement growth. Cities such as Johannesburg, eThekwini and Cape Town grow fastest at their informal edges, between censuses, where municipal records lag reality. Satellite images taken months apart show new roof clusters appearing; analysts digitise them into a GIS layer of new settlement, overlay water, sanitation and clinic layers, and the map of unserved households draws itself. That is how planners decide where the next standpipes, toilets and clinics go.

Planning and checking the census. Before counting, Statistics South Africa uses aerial photographs and satellite imagery to divide the whole country into small counting areas and to make sure no dwelling — including the newest shack on the newest edge — is missed from an enumerator's map. Afterwards, census totals join GIS layers as the attribute data behind population density maps, and the census's small-area boundaries are themselves a GIS product.

Disasters and disease. When floods struck KwaZulu-Natal in April 2022, before-and-after satellite images identified destroyed neighbourhoods and cut roads while the ground was still impassable, and GIS overlay of damage on population density showed where the most people needed help fastest. The same logic serves health planning: overlay clinic positions on settlement growth and the underserved areas stand out.

Agriculture and food security. Satellite sensors reading infrared can measure how healthily crops are growing across whole provinces, warning of drought and poor harvests months before they reach markets — knowledge that matters directly to a population's food supply.

South Africa's own capacity is worth naming. The South African National Space Agency, SANSA, receives and distributes satellite data from its Hartebeesthoek station, and the country has built and flown its own small earth-observation satellites, including SumbandilaSat. Daily life runs on the same toolkit: navigation applications on a phone combine GPS positioning, remote-sensed imagery and GIS layers every time a route is calculated.

The final questions of this part are with you now: informal settlements, the census, disaster response, and South Africa's own space capacity.

# Part 2 — Simplifier

Now the same machinery through a phone, a lasagne and an eye in the sky.

## Subtopic: The Smartphone Map You Already Use

Open the map application on any smartphone and search for the nearest pizza. A map appears, a blue dot marks your position, red pins mark pizza places, and a route draws itself along the roads. In that ordinary moment, a full Geographical Information System just ran in your pocket.

Match it to the definition. Information tied to positions on the earth: the pizza places all carry coordinates. Stored: in the map company's database. Analysed: the application worked out which pizza place is nearest and which streets connect it to you. Displayed: the map on the screen. Captured, stored, analysed, displayed — georeferenced information. That is a GIS, word for word.

Now find the five components hiding in the moment. Hardware: the phone in your hand, plus the distant computers holding the map. Software: the map application itself. Data: every road, every shop, every opening time — and this is the part that cost the most to build, because someone had to collect and check all of it. People: you, asking the question and choosing the pizza. Procedures: the company's rules for updating roads and fixing errors, which is why a new road appears on the map a few weeks after it opens rather than never.

One more idea and the pocket example is complete. The application knows two different things about that pizza place. WHERE it is — the pin on the map. That is spatial data. And WHAT it is — its name, its menu, its rating. That is attribute data. Tap the pin and the facts open. Position plus description, linked: the whole trick of GIS in one tap.

Quick check — this section's questions are coming to you now: the definition matched to the phone, the five components found in your pocket, and the pin against the facts behind it.

## Subtopic: A Lasagne of Maps

Here is the idea that turns a GIS from an electronic atlas into a thinking tool, and it looks exactly like a lasagne.

Take one piece of South Africa. Draw its rivers on a transparent plastic sheet. On a second sheet, same size, the roads. On a third, the towns and settlements. On a fourth, shade population density. On a fifth, mark every clinic. Five separate sheets, each showing one theme, each drawn to the same scale over the same ground.

Alone, each sheet answers only its own small question. Now stack them, edges lined up, and hold the pile to the light. Suddenly the layers talk to each other. The dense-population shading glows in a spot where the clinic sheet shows nothing — an underserved community, visible in a second. A settlement sits where the river sheet shows a floodplain — a warning, visible in a second. The road sheet shows the one route a water tanker could take to reach it.

That stack of transparencies is precisely what a GIS holds in its memory, with two upgrades. First, the computer can stack any combination instantly — rainfall over settlements, growth over clinics — where paper would drown a planner in sheets. Second, the computer can ANSWER QUESTIONS across the stack: show every school within five kilometres of the river; find dense settlement further than ten kilometres from a clinic. Planners call it overlay analysis. You can call it holding the lasagne to the light.

The catch is the same as any lasagne: it is only as good as its ingredients. If the clinic layer is five years old, the analysis recommends building a clinic where one already stands. That is why the data component costs the most and matters the most, and why the procedures component — the update rules — exists at all. A GIS never makes old data true; it only makes it look convincing.

Questions on the layers are up now: what a layer is, what stacking lets you ask, and why stale data is the danger.

## Subtopic: The Eye in the Sky and the Census

Last piece: where does all that layered data come from? A great deal of it comes from machines that never touch the ground.

Remote sensing means finding out about the earth's surface WITHOUT touching it — sensing from a distance, using cameras and sensors on satellites in orbit and on aircraft. The satellite sees a huge area in one pass and, better still, comes back over the same spot every few days, year after year. Line up its images like frames of a film and the earth starts to move: a dam shrinking through a drought, a coastline changing, a city's edge creeping outward. The aircraft flies much lower, sees a much smaller patch in much finer detail, and provides the photographs behind South Africa's 1 to 10 000 orthophoto maps — the ones where single houses are visible.

And the sensors cheat human eyesight. They read kinds of light our eyes cannot, such as infrared, and healthy plants shout in infrared. That is how a satellite can tell struggling mielies from thriving mielies across the whole Free State, and warn of a poor harvest months before people feel it.

Now connect the eye in the sky to counting people, because this is the exam link. A city's informal edges grow week by week, faster than any office record. Satellite images a few months apart show exactly where new roofs have appeared. Those new roofs become a GIS layer; stack it over the water, toilet and clinic layers, and the map announces where services must go next. Before a census, Statistics South Africa uses aerial and satellite images to make sure every dwelling in the country sits inside somebody's counting area, so no one is invisible to the count. And when the KwaZulu-Natal floods of April 2022 cut roads and flattened neighbourhoods, before-and-after satellite images told rescuers where the damage was worst while the ground was still under water.

But keep the limit in view, because examiners love it: the satellite counts ROOFS, never people. It cannot ask who lives below, how old they are, or what language they speak. For that, a human being with a clipboard still knocks on the door. The eye in the sky and the person at the door need each other — one sees everywhere, the other asks everything.

The final questions of the lesson are with you now — sensing without touching, satellites against aircraft, the roof-counting trick, and the limit only a human can cross.
