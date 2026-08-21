# Part 1 — Expert

Geographical Information Systems questions surrender their marks to anyone who treats GIS as a vocabulary instead of a mystery — and lose them to everyone else. This session builds the entire toolkit in working order: what a GIS is and the two kinds of data it stores, how information stacks into layers, what buffering and querying actually accomplish, and how resolution and data manipulation questions are answered. One running example carries the whole lesson: a municipal planner choosing where a new clinic may be built in a growing coastal town — a scenario that forces every GIS tool to earn its keep.

## Subtopic: What a GIS Is and the Two Kinds of Data

A Geographical Information System is a computerised system that captures, stores, manipulates, analyses and displays spatially referenced information — information tied to a position on the Earth's surface. Five verbs, each individually creditable: capture, store, manipulate, analyse, display. A filing cabinet merely stores; only a GIS performs all five.

Everything held inside the system is one of two kinds of data, and separating them is the most frequently tested single skill. Spatial data is the position and shape of a feature — where the clinic stands, the course a river runs, the outline a reservoir makes. Attribute data is the information attached to the feature — the clinic's name, the number a road carries, the reservoir's capacity. The favourite trap: a road drawn on a map is spatial data, but the route number printed on it is attribute data — the number describes the road; it does not position it. State it as a rule: the drawing is spatial, the label is attribute.

Spatial features come in three shapes. A point feature has position without length — a trig beacon, a windpump, a borehole. A line feature has length but no meaningful width at map scale — a river, a road, a railway, a power line. An area feature encloses space — a reservoir, an orchard, an urban block. Questions attach qualifiers: a natural line feature is a river; a constructed line feature is a road or railway. One adjective plus one noun, both earning.

Beneath all of it lie the two ways a computer can hold a map. Vector data assembles features from points, lines and polygons — crisp geometry, ideal for property boundaries and road networks. Raster data builds the scene from a grid of equal cells, exactly as a photograph is built from pixels — the native form of satellite images and orthophotos. Vector draws the field's fence as a line; raster paints the field as a patch of coloured cells.

The questions on this section are with you now: the five verbs of the definition, spatial against attribute, the three feature shapes with their qualifiers, and vector against raster.

## Subtopic: Data Layering — The Transparency Stack

Now the idea the entire system stands on. Data layering is the storage of different themes of information in separate layers that can be laid over one another and viewed in any combination. Picture clear plastic sheets over one base map: a sheet carrying only drainage — every river, pan and reservoir; a sheet for the transport network; one for contours; one for vegetation; one for the cadastral layer — the property boundaries; one for buildings and land use. Because every sheet is georeferenced to the same coordinate system, the stack aligns perfectly.

Why keep the themes apart? Because separation is what makes analysis possible. Our planner siting the clinic does not want the entire cluttered map at once. Three sheets come out of the drawer: transport, to find land the ambulances and taxis can reach; contours, to exclude the steep slopes; drainage, to keep the site clear of the wetland and the flood-prone flats. Everything irrelevant stays invisible. When a question asks you to name the data layer shown, answer with the theme rather than the object: a sheet of rivers and reservoirs is the drainage layer; a sheet of roads and railways is the transport layer.

There is also a practical version of this question, and it is a gift to anyone who has thought about it once. You are shown two or three small sketches — a patch of woodland, a stream, an empty frame — and asked to combine the layers in the empty frame. The skill is disciplined copying: every feature keeps its own position, because all layers share one coordinate system. Redraw each feature exactly where it stands, letting features overlap where the originals overlap, and the marks arrive one per correctly placed feature.

Take this section's questions now: the definition of data layering, the standard layer names, why layers are kept separate, and the rule that makes combining sketches safe.

## Subtopic: Buffering, Querying and Data Integration

Three tools convert the stacked layers into decisions, and together they carry most GIS marks.

Buffering draws a zone of chosen width around a feature so that the inside of the zone can be treated differently from the outside. Around a point feature the buffer is a circle; around a line, a corridor; around an area, a widened band. Our planner buffers the stream at one hundred metres: no construction inside the strip, because the stream floods. A corridor buffer along the high-voltage power line keeps buildings out of the servitude. A band around the coastal wetland holds development back from a system that both floods and filters. When a map shows a strip of deliberately empty land between development and trouble and asks why, the required word is buffering, and the required evidence is the trouble itself: the floodplain, the wetland, the power line, the protected dunes.

Querying is asking the database a question and letting it fetch every feature that satisfies the condition. Show every open erf larger than four hundred square metres. Show every taxi rank within two kilometres of the proposed site. A query searches attribute and spatial data together — which is exactly why both kinds exist. Data integration is the step that must happen before any of this works: bringing data from different sources into one system so the layers can talk — the municipal property register, the satellite image, the census tables, all georeferenced to the same grid. And once the data is integrated, statistical analysis lets the planner count, average and compare: how many households live beyond five kilometres from the nearest clinic; what percentage of vacant land lies inside the flood buffer.

Pause for this section's questions: what buffering is and the shapes it makes, two situations that call for it, what a query does, and why integration must come first.

## Subtopic: Resolution, Data Manipulation and Answering GIS Questions

Resolution is the clarity of an image — formally, the amount of detail a raster image holds, which is set by the size of its cells. Small cells, many pixels, high resolution, crisp detail. Large cells, few pixels, low resolution, a blocky blur. Shown two photographs and asked which holds fewer pixels, choose the blurrier one: fewer pixels means each pixel is larger, so edges smear and small features drown. The reason sentence writes itself: the image is less clear because its resolution is low and its pixels are large.

Data manipulation is changing how stored data is presented so it serves the task better. The standard test of it: an unclear area on an orthophoto, and an instruction to manipulate the scale to make the image more readable. The answer is to enlarge the scale — zoom in — so the same ground occupies more image and the detail opens up. Manipulation also includes converting between data formats and reprojecting data onto another coordinate system, but the enlarge-the-scale move is the one to produce first.

Now the craft of answering. GIS questions arrive in three recurring types, whatever their packaging. Type one: straight vocabulary — define attribute data, resolution, buffering — where a memorised definition scores instantly. Type two: application to the mapped area — name a natural line feature in a stated block, name the layer a sketch shows, supply the evidence that justifies a buffer. Type three: the practical redraw — combining given layers into a single frame, one mark per feature placed true. All three types reward identical preparation: definitions known cold, then each tool pointed at a real map until the pointing is automatic. And where does our running example end? The layers are stacked, the buffers exclude the wet and the dangerous ground, the query returns the flat, dry, reachable, unclaimed sites — and the clinic is placed by evidence instead of by argument. That is the whole discipline in a sentence: GIS turns a map into an argument you can defend.

This part's closing questions are ready for you now: resolution and pixels, the scale manipulation answer, the three recurring question types, and the planner's final decision.

# Part 2 — Simplifier

The same toolkit again — rebuilt this time from a burger, a chalk line in a schoolyard, a search bar and the camera in your pocket.

## Subtopic: The Burger That Explains the Whole System

Begin at supper. A burger is built as separate layers — bun, patty, lettuce, cheese — and its whole genius is that the layers are made separately and eaten together. Nobody grates the cheese into the patty. That is a Geographical Information System: rivers on one layer, roads on another, property lines on a third, all stacked above the same piece of Earth so that looking down through them shows one aligned picture.

What is written on each layer? Two kinds of things, and an ordinary sentence about a friend separates them. Where your friend is standing — spatial. Her name, her age, her number — attributes, facts pinned to her. The map works identically: the drawn line of the road is spatial data; the little number that names the road is attribute data. The drawing is the where; the label is the what.

One more pair completes the burger. A computer remembers a map in one of two ways. Vector remembers outlines — dot, line, shape — a clean pen drawing of the farm fences. Raster remembers a photograph — thousands of tiny coloured squares, like every image on your phone. Zoom deep into any photo and it collapses into blocks: those blocks are raster cells. Drawings stay sharp under zoom; photos eventually go blocky. Hold that sentence and the vector–raster question is banked.

The questions for this section are up now: the burger layers, where against what, and the pen drawing against the phone photo. Answer them slowly; each one hides inside something you have handled today.

## Subtopic: The Chalk Circle Around the Beehive

Buffering, straight from the schoolyard. Bees have settled in the corner tree, so a teacher paces out ten steps all around it and drags a chalk line into a circle: nobody crosses the chalk. The tree itself has not changed — what changed is that the danger now has a measured edge, and an edge is what makes a rule enforceable. That chalk circle is a buffer: a zone of chosen width drawn around a feature so the inside is treated differently from the outside.

Municipalities draw chalk circles with survey equipment. A strip along the stream where nothing may be built, because streams flood. A corridor under the high-voltage line kept clear of roofs and washing lines. A band around the coastal wetland, holding the diggers back from the town's natural sponge and filter. So when your map shows a suspicious ribbon of empty land between the houses and some trouble, the emptiness itself is the answer: a buffer is holding development back, and your evidence is the trouble — the floodline, the power line, the wetland, the dunes.

Querying you already do before breakfast. Typing a song title into a music app asks a giant database to fetch every track that matches — you never scroll through all recorded music. A planner does the same with land: fetch every open plot bigger than four hundred square metres, more than one hundred metres from the stream, within two kilometres of a taxi route. The computer fetches; the human chooses. And underneath sits the unglamorous step that makes fetching possible — integration: the property register, the aerial photographs and the census must first be loaded into one system on one grid, just as songs must be in the app before a search can find them.

Your questions for this section are ready: the chalk circle, the tell-tale empty ribbon, the music-app search, and the step that must happen before searching works.

## Subtopic: Pixels, Zooming In and Free Marks

The last tool lives in your pocket. Photograph a bird on a fence across the sports field, then zoom in afterwards: the bird dissolves into fuzzy squares. The photo simply does not hold enough pixels for that much zoom — each pixel is large, edges smear, detail drowns. The fuzziness has a name: low resolution. Resolution is how much detail an image holds; pixels are the grains it is built from. Fine grains, sharp picture. Coarse grains, mush.

So when two photographs appear side by side with the question of which holds fewer pixels, pick the blurrier one and give the reason like a professional: it is less clear because its pixels are larger and its resolution lower. And when an orthophoto area is declared hard to read and you are asked how manipulating the scale would help, give the move your thumbs perform daily: enlarge the scale. Zoom in. The same ground spreads across more image, and the detail opens.

Now sweep the whole lesson into one pass, because these ideas together are among the most reliable marks available. The map is a burger of layers. Each layer records where things are, plus labelled facts about them. Drawings are vector; photos are raster, built of pixels, their sharpness called resolution. Chalk circles called buffers keep trouble at a measured distance; searches called queries fetch exactly what is asked; and none of it functions until the data has been integrated into one system. Six definitions, one running story, and a set of marks that waits for whoever arrives calm.

The final questions of the lesson are with you now: the fuzzy bird on the fence, the zoom-in answer, and the six ideas told as one story. Take them one at a time and let the pictures do the remembering.
