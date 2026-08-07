# Part 1 — Expert

Every mapwork paper closes with a block of Geographical Information Systems questions, and every year those marks are surrendered by candidates who treat GIS as a mystery instead of a vocabulary. This session builds the whole toolkit in order: what a GIS is and the two kinds of data it stores, how information stacks into layers, what buffering and querying actually do, and how resolution and data manipulation questions are phrased in the examination. The running example throughout is a town planner deciding where new houses may be built on the edge of a growing town — the exact scenario the examiners love, because it forces every GIS tool to earn its keep.

## Subtopic: What a GIS Is and the Two Kinds of Data

A Geographical Information System is a computerised system that captures, stores, manipulates, analyses and displays spatially referenced information — information tied to a position on the Earth's surface. Five verbs, and the memorandum pays for them: capture, store, manipulate, analyse, display. A filing cabinet stores; only a GIS does all five.

Everything inside the system is one of two kinds of data, and telling them apart is the single most common GIS question. Spatial data is the position and shape of a feature — where the school sits, the path a river follows, the outline a dam makes. Attribute data is the information attached to that feature — the name of the school, the number printed on a road, the depth of the dam. Here is the exam's favourite trap: a road drawn on the map is spatial data, but the route number written on that road is attribute data. The number three hundred and ten on a national road describes the road; it does not position it. Say it as a rule: the drawing is spatial, the label is attribute.

Spatial features themselves come in three shapes. A point feature has position but no length — a trig beacon, a windmill, a spot height. A line feature has length but no real width at map scale — a river, a road, a railway, a power line. An area feature encloses space — a dam, a cultivated field, an urban block. Examiners ask for these with qualifiers: a natural line feature is a river; a constructed line feature is a road. One adjective, one noun, both marks.

Underneath everything sit the two ways a computer can hold a map. Vector data builds features from points, lines and polygons — crisp shapes, perfect for property boundaries and road networks. Raster data builds the scene from a grid of equal cells, the way a photograph is built from pixels — the natural form of satellite images and orthophotos. Vector draws the farm fence as a line; raster paints the farm as a patch of cells.

The questions on this section are with you now: the five verbs of the definition, spatial against attribute, the three feature shapes with their qualifiers, and vector against raster.

## Subtopic: Data Layering — The Transparency Stack

Now the idea the whole system stands on. Data layering is the storing of different kinds of information in separate layers that can be placed on top of one another and viewed in any combination. Picture the layers as clear plastic sheets over the same base: one sheet carries only the drainage — every river, dam and pan; one carries the transport network; one the contours; one the vegetation; one the cadastral layer, which is the property boundaries; one the buildings and land use. Because every sheet is georeferenced to the same coordinates, they align perfectly when stacked.

Why separate the information at all? Because separation is what makes analysis possible. The town planner working on our housing question does not want the whole cluttered map at once. The planner pulls three sheets only: drainage, to see the streams and the flood-prone ground; contours, to see the steep slopes; existing buildings, to see what is already taken. Everything irrelevant stays out of sight. When the mapwork paper asks you to name the data layer shown, answer with the theme, not the object: a sheet full of rivers and dams is the drainage layer; a sheet of roads and railways is the transport layer.

The examination has a practical version of this question, and it is free marks for anyone who has thought about it once. You are shown two or three small sketches — say a woodland patch, a stream, and an empty frame — and asked to combine the layers into the empty frame. The skill is purely careful copying: every feature keeps its own position, because all the layers share the same coordinates. Redraw each feature where it stands, overlapping where the originals overlap, and the marks are yours — one mark per layer placed correctly.

Take this section's questions now: the definition of data layering, the standard layer names, why layers are kept separate, and the rule that makes combining sketches safe.

## Subtopic: Buffering, Querying and Data Integration

Three tools turn the stacked layers into decisions, and between them they carry most of the GIS marks in recent papers.

Buffering draws a zone of chosen width around a feature, so that whatever falls inside the zone is treated differently from whatever falls outside. Around a point the buffer is a circle; around a line, a corridor; around an area, a widened band. The planner in our running example buffers a stream at one hundred metres: no houses inside the strip, because the river floods. Around ground that has sunk into hollows — dolomite country with sinkholes and subsiding ground — the buffer becomes a no-build zone that keeps foundations off dangerous rock. Around a conservation woodland it holds development at a respectful distance. When a mapwork question shows open land kept empty between a town and a hazard and asks why, the word the memorandum wants is buffering, and the evidence it wants named is the hazard itself: the sinkholes, the wetland, the floodplain, the protected trees.

Querying is asking the database a question and letting it fetch every feature that satisfies the condition. Show all erven larger than five hundred square metres. Show every clinic within ten kilometres of the taxi rank. The query searches attribute and spatial data together — that is why both kinds exist. Data integration is the step before any of this can work: bringing data from different sources into one system so the layers can talk to each other — the municipal property register, the satellite image, the census figures, all georeferenced to the same grid. And once integrated, statistical analysis lets the planner count, average and compare: how many households sit inside the flood buffer; what percentage of the town lies on steep ground.

Pause for this section's questions: what buffering is and the shapes it makes, two exam situations that call for it, what a query does, and why integration must happen first.

## Subtopic: Resolution, Data Manipulation and the Way GIS Is Examined

Resolution is the clarity of an image — formally, the amount of detail a raster image holds, set by the size of its cells. Small cells, many pixels, high resolution, sharp detail. Large cells, few pixels, low resolution, a blocky blur. When the paper prints two photographs and asks which has fewer pixels, look for the blurrier one: fewer pixels means each pixel is larger, so edges smear and small features vanish. The reason line writes itself: the image is less clear because the resolution is low and the pixels are large.

Data manipulation is changing how stored data is presented so it serves the task better — and the examiners test it with one specific move: an unclear area on the orthophoto, and the instruction to manipulate the scale to make the image clearer. The answer is to enlarge the scale — zoom in — so the same ground occupies more image and the detail opens up. Manipulation also covers converting between formats and reprojecting data, but the enlarge-the-scale answer is the one the memorandum prints.

Now the shape of the examination itself. The GIS block sits at the end of the mapwork question and runs to roughly seven marks, mixing three question types. Type one: multiple-choice vocabulary — attribute data, resolution, buffering — where a memorised definition scores instantly. Type two: application to the mapped area — name a natural line feature in a stated block, name the layer a sketch shows, give evidence supporting a buffer. Type three: the practical redraw, combining given layers into one frame. Every one of these rewards the same preparation: know the definitions cold, then practise pointing each tool at a real map. Where does the planner end our story? The layers are stacked, the buffers are drawn, the query returns the safe, flat, dry, unclaimed land — and the houses are placed by evidence rather than by guesswork. That is the whole discipline in one sentence: GIS turns a map into an argument.

This part's closing questions are ready for you now: resolution and pixels, the scale manipulation the memo expects, the three question types, and the planner's final decision.

# Part 2 — Simplifier

Now the same toolkit again, rebuilt from things you already own: a burger, a stack of tracing paper, a schoolyard rule and a phone camera.

## Subtopic: The Burger That Explains the Whole System

Start with supper. A burger arrives as separate layers — bun, patty, lettuce, cheese — and the whole point of a burger is that the layers are made separately but eaten together. Nobody cooks the lettuce into the patty. That is a Geographical Information System: the rivers on one layer, the roads on another, the property lines on a third, all stacked over the same spot of Earth so they line up perfectly when you look down through them.

And what is actually written on each layer? Two kinds of things, and you can hear the difference in an ordinary sentence about a person. Where your friend is standing — that is spatial. Their name, their age, their phone number — those are attributes, facts pinned to the person. On the map it is identical: the drawn line of the road is spatial; the little number sitting on the road naming which road it is — that is attribute data. The drawing is the where; the label is the what.

One more pair, and then the burger is fully built. A computer can remember a map two ways. Vector is remembering the outlines — dot, line, shape — like a neat pen drawing of the farm fences. Raster is remembering a photo — millions of tiny squares of colour, like the pictures on your phone. Zoom deep into any photo and it crumbles into blocks: those blocks are the raster cells. Drawings stay sharp when you zoom; photos eventually turn to blocks. Keep that one sentence and the vector-raster question is banked.

The questions for this section are up now: the burger layers, where against what, and the pen drawing against the phone photo. Answer them slowly; every one is hiding in something you have seen today.

## Subtopic: The Chalk Circle Around the Beehive

Here is buffering, straight from the schoolyard. There is a beehive in the corner tree, so the teacher draws a chalk circle ten steps wide around it and announces one rule: nobody plays inside the circle. Nothing about the tree changed. What changed is that the space around a danger now has an edge, and the edge makes the rule enforceable. That chalk circle is a buffer: a zone of chosen width drawn around a feature so the inside can be treated differently from the outside.

Towns draw chalk circles for grown-up reasons. A strip along a river where no one may build, because rivers flood. A ring around ground that has caved into sinkholes, because foundations and holes do not mix. A band around a woodland the town wants kept wild. When your exam map shows a suspicious empty gap between houses and trouble, the empty gap is the answer: development stopped there because a buffer holds it back, and your evidence is whatever the trouble is — the sinkholes, the wet ground, the protected trees.

Querying is even more familiar, because you run queries all day. When you type a song's name into a music app, you are asking a giant database to fetch every track matching your words — you do not scroll through every song ever recorded. A planner does the same with land: show every open plot bigger than five hundred square metres, further than one hundred metres from the stream. The computer fetches; the planner chooses. And the quiet step that makes it all possible is integration — getting the town's property lists, photos and measurements into one system first, the way all your music has to be in the app before searching can find anything.

Your questions for this section are ready: the chalk circle, the exam's empty gap, the music-app search, and the step that must happen before searching works.

## Subtopic: Pixels, Zooming In and Free Marks

Last tool, and it lives in your pocket. Take a photo of the scoreboard from across the field and zoom in later: the numbers turn into fuzzy blocks. The picture does not hold enough pixels for that much zoom — each pixel is big, edges smear, detail drowns. That fuzziness has a name: low resolution. Resolution is simply how much detail an image holds, and pixels are the grains it is built from. Fine grains, sharp image. Fat grains, porridge.

So when the paper shows two photographs and asks which has fewer pixels, pick the blurry one, and give the reason like a professional: it is less clear because its pixels are larger and its resolution lower. And when the paper says an area on the orthophoto is hard to read and asks how manipulating the scale would help — the answer is the move your thumbs already know: make the scale larger. Zoom in. More image for the same ground, and the detail opens up.

Now collect the whole lesson in one pass, because together these ideas are the easiest marks on the entire paper. The map is a burger of layers. Each layer holds where things are, plus labelled facts about them. Drawings are vector; photos are raster, built from pixels, and their sharpness is resolution. Chalk circles called buffers keep trouble at a distance, searches called queries fetch what you ask for, and none of it works until the data is integrated into one system. Six definitions, one running picture, roughly seven marks — waiting at the end of the mapwork paper for whoever arrives calm.

The final questions of the lesson are with you now: the fuzzy scoreboard, the zoom answer the memo wants, and the six ideas told as one story. Take them one at a time and let the pictures do the remembering.
