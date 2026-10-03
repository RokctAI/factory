# Part 1 — Expert

Term 4 moves geometry from the flat page into space, and it begins with the five most symmetrical solids that exist. The CAPS instruction is to revise the properties and definitions of the five Platonic solids in terms of their faces, vertices and edges. We start with the vocabulary of any polyhedron, counting faces, edges and vertices on prisms and pyramids, then meet the tetrahedron, cube, octahedron, dodecahedron and icosahedron and record their counts in a table. We check every row with Euler's formula, learn to calculate the edges and vertices of a solid from its faces alone, and finish with the elegant argument, built from interior angles of regular polygons, that explains why there can be exactly five Platonic solids and not one more. The counting habits of this lesson are used again when we draw nets and calculate surface areas later this term.

## Subtopic: Polyhedra: Faces, Edges and Vertices

A polyhedron is a closed three-dimensional solid whose surface is made entirely of flat polygons. Each flat polygon is a face. The straight line segment where two faces meet is an edge. The corner point where three or more edges meet is a vertex, plural vertices. A solid with any curved surface, such as a cylinder, cone or sphere, is not a polyhedron; those solids are the next lesson.

Prisms and pyramids are the familiar polyhedra. A prism has two congruent, parallel end faces joined by rectangular side faces, and it is named after its end face. A pyramid has one base and triangular side faces that meet at a single apex, and it is named after its base.

Count the triangular prism systematically. Faces: 2 triangular ends and 3 rectangles, 5 faces. Vertices: 3 on each triangular end, 6 vertices. Edges: 3 around each end and 3 joining the ends, 9 edges. The square-based pyramid: faces, 1 square base and 4 triangles, 5 faces; vertices, 4 on the base and 1 apex, 5 vertices; edges, 4 around the base and 4 rising to the apex, 8 edges. A pentagonal prism has 7 faces, 10 vertices and 15 edges; a hexagonal pyramid has 7 faces, 7 vertices and 12 edges.

Counting reliably needs a method, because a solid seen in a drawing hides some of its faces, edges and vertices behind it. Count by structure, not by pointing: for a prism, the end faces contribute 2 faces, each end polygon with n sides contributes n vertices and n edges, and the sides contribute n faces and n more edges, so a prism on an n-sided end has n plus 2 faces, 2n vertices and 3n edges. A pyramid on an n-sided base has n plus 1 faces, n plus 1 vertices and 2n edges. Check the triangular prism: n is 3, so 5 faces, 6 vertices, 9 edges.

A polyhedron is convex if it has no dents: a straight line joining any two points of the solid stays inside it. All the prisms and pyramids in this lesson are convex, and so are the Platonic solids. The questions for this section are with you now: the definitions of face, edge and vertex, the counts for the triangular prism and square pyramid, and the general rule for a prism.

## Subtopic: The Five Platonic Solids

A Platonic solid, also called a regular polyhedron, is a convex polyhedron in which every face is the same regular polygon, all sides and angles equal, and the same number of faces meets at every vertex. Both conditions are required. There are exactly five such solids, named by their number of faces, from the Greek words for 4, 6, 8, 12 and 20.

The tetrahedron has 4 faces, each an equilateral triangle, with 3 faces meeting at each vertex. It has 4 vertices and 6 edges. It is the triangular pyramid with every edge equal.

The cube, or regular hexahedron, has 6 square faces, with 3 meeting at each vertex. It has 8 vertices and 12 edges.

The octahedron has 8 equilateral triangle faces, with 4 meeting at each vertex. It has 6 vertices and 12 edges, and it looks like two square-based pyramids joined base to base.

The dodecahedron has 12 faces, each a regular pentagon, with 3 meeting at each vertex. It has 20 vertices and 30 edges.

The icosahedron has 20 equilateral triangle faces, with 5 meeting at each vertex. It has 12 vertices and 30 edges.

Recorded in a table with columns for name, face shape, number of faces, faces at each vertex, vertices and edges, the data shows patterns worth noticing. Three of the five are made of equilateral triangles, and they differ only in how many triangles meet at a corner: 3, 4 or 5. The cube and the octahedron share 12 edges, and the cube's 6 faces and 8 vertices are the octahedron's 8 faces and 6 vertices swapped. The dodecahedron and the icosahedron share 30 edges and swap 12 and 20 the same way. Solids related like this are called duals: placing a dot at the centre of each face of a cube and joining the dots of neighbouring faces produces an octahedron. The tetrahedron, with 4 faces and 4 vertices, is its own dual.

Platonic solids appear in real objects because their symmetry makes them fair. A board-game die must give every face an equal chance, so dice are made as tetrahedra, cubes, octahedra, dodecahedra and icosahedra, the four-, six-, eight-, twelve- and twenty-sided dice. Crystals of table salt grow as cubes, and many viruses have an icosahedral outer shell. Your questions on this section are ready: the definition with its two conditions, the five names with their face shapes and counts, and the dual pairs.

## Subtopic: Euler's Formula and Counting from the Faces

For every convex polyhedron the numbers of vertices, edges and faces are linked by Euler's formula: the number of vertices minus the number of edges plus the number of faces equals 2, written V minus E plus F equals 2. Check it on all five Platonic solids. Tetrahedron: 4 minus 6 plus 4 is 2. Cube: 8 minus 12 plus 6 is 2. Octahedron: 6 minus 12 plus 8 is 2. Dodecahedron: 20 minus 30 plus 12 is 2. Icosahedron: 12 minus 30 plus 20 is 2. It holds for the prisms and pyramids too: the triangular prism gives 6 minus 9 plus 5, which is 2, and the square pyramid 5 minus 8 plus 5, which is 2.

Euler's formula is a checking tool and a solving tool. As a check, a count that does not satisfy it is wrong, so a learner who counts 8 vertices, 12 edges and 7 faces on a cube has miscounted somewhere. As a solver, any two of the three numbers give the third: a polyhedron with 10 vertices and 15 edges has 2 minus 10 plus 15, which is 7, faces, which matches the pentagonal prism.

There is a second way to count edges and vertices that needs only the faces, and it explains the numbers rather than merely checking them. Every edge is shared by exactly 2 faces. So if you count the sides of all the faces, you count every edge twice, and the number of edges is the total number of sides divided by 2. The dodecahedron has 12 pentagons, 12 times 5 is 60 sides, and 60 divided by 2 is 30 edges. The icosahedron has 20 triangles, 20 times 3 is 60 sides, and again 30 edges.

Every vertex is shared by the same number of faces, call it m, so counting the corners of all the faces counts each vertex m times, and the number of vertices is the total number of corners divided by m. The dodecahedron's 60 corners with 3 faces at each vertex give 60 divided by 3, which is 20 vertices. The icosahedron's 60 corners with 5 at each vertex give 60 divided by 5, which is 12 vertices. The octahedron's 8 triangles have 24 corners; with 4 at each vertex that is 6 vertices, and its 24 sides give 12 edges.

So from just two facts, the face shape and the number of faces at each vertex, the whole table can be built, and Euler's formula confirms it. The questions for this section are ready: Euler's formula on each solid, finding a missing count, and edges and vertices from the faces.

## Subtopic: Why Only Five, and the Error Museum

Why are there exactly five Platonic solids? The argument uses only the interior angle of a regular polygon and the fact that at least 3 faces must meet at every vertex of a solid, because 2 faces can only meet along an edge and would close nothing. At a vertex the angles of the faces meeting there must add to less than 360 degrees; if they add to exactly 360 the faces lie flat, and if they add to more they cannot fit around a point at all.

The interior angle of a regular polygon with n sides is n minus 2, times 180, divided by n. Equilateral triangle: 60 degrees. Square: 90 degrees. Regular pentagon: 108 degrees. Regular hexagon: 120 degrees.

Now try every possibility. Triangles: 3 at a vertex make 180 degrees, the tetrahedron; 4 make 240, the octahedron; 5 make 300, the icosahedron; 6 make 360, which is flat, a tiling of the floor, not a solid. Squares: 3 at a vertex make 270, the cube; 4 make 360, flat. Pentagons: 3 make 324, the dodecahedron; 4 make 432, too much. Hexagons: 3 make 360, flat, which is why a honeycomb is a flat tiling. Any polygon with more sides has an interior angle above 120 degrees, so even 3 of them exceed 360. That leaves exactly five combinations, and each one produces exactly one solid. The proof is over two thousand years old and it is complete.

The error museum, five exhibits. Exhibit one: calling any solid made of equal triangles a Platonic solid; two tetrahedra glued face to face give a triangular bipyramid with 6 equilateral faces, but 3 faces meet at some vertices and 4 at others, so it fails the second condition. Exhibit two: counting only the visible faces, edges and vertices in a drawing, such as 3 faces and 7 vertices for a cube. Exhibit three: confusing the counts, such as giving the cube 8 faces and 6 vertices, which are the octahedron's numbers. Exhibit four: forgetting to halve when counting edges from faces, giving the dodecahedron 60 edges. Exhibit five: calling a soccer ball an icosahedron; the traditional ball is made of 12 pentagons and 20 hexagons, two different shapes, so it is not a Platonic solid at all.

Layout for marks: for a definition, state both conditions, congruent regular polygon faces and the same number of faces at each vertex; for counts, show the method, such as faces times sides divided by 2 for edges; and verify with V minus E plus F equals 2. The questions for this section are with you now: the angle sums at a vertex, the flat cases, and the five exhibits.

# Part 2 — Simplifier

Now the same lesson again through flat sides, folds and corners, five perfectly fair dice, and the corner that has to fit — plain words, same rules.

## Subtopic: Flat Sides, Folds and Corners

Pick up a box. The flat sides are faces. The folds where two flat sides meet are edges. The pointy corners are vertices. Any solid made only of flat sides is a polyhedron. Anything with a curved bit, like a tin can or a ball, is not one.

Count a cereal box: 6 faces, 12 edges, 8 corners. Count a triangular chocolate box: 2 triangle ends and 3 rectangles make 5 faces; 3 corners at each end make 6 corners; 3 edges round each end plus 3 running along make 9 edges. Count a square pyramid: a square bottom and 4 triangles, 5 faces; 4 corners at the bottom and 1 on top, 5 corners; 4 edges round the bottom and 4 going up, 8 edges.

The danger is counting only what you can see. A picture of a box shows 3 faces, but there are 6. Count by building it in your head: the ends, then the sides, never by poking at the picture.

There is a magic check that works on every solid like these: corners take away edges add faces always gives 2. The box: 8 take away 12 add 6 is 2. The triangular box: 6 take away 9 add 5 is 2. The pyramid: 5 take away 8 add 5 is 2. If your numbers do not make 2, you have miscounted. Your questions on this section are ready: faces, edges and corners on a box, a triangular box and a pyramid, and the magic 2.

## Subtopic: Five Fair Dice

Some solids are perfectly even: every face is the same regular shape, and every corner looks exactly like every other corner. There are only five of them, the Platonic solids, and you have probably rolled some in board games, because perfectly even solids make perfectly fair dice.

The 4-sided die is the tetrahedron: 4 triangles, 4 corners, 6 edges, 3 triangles at each corner. The 6-sided die is the cube: 6 squares, 8 corners, 12 edges. The 8-sided die is the octahedron: 8 triangles, 6 corners, 12 edges, 4 triangles at each corner, like two pyramids stuck bottom to bottom. The 12-sided die is the dodecahedron: 12 pentagons, 20 corners, 30 edges. The 20-sided die is the icosahedron: 20 triangles, 12 corners, 30 edges, 5 triangles at each corner.

Notice the pairs. The cube has 6 faces and 8 corners; the octahedron has 8 faces and 6 corners; both have 12 edges. The dodecahedron and icosahedron swap 12 and 20 and share 30 edges. And the tetrahedron, with 4 and 4, pairs with itself.

There is a shortcut for edges. Count all the sides of all the faces, then halve, because every edge belongs to two faces. Icosahedron: 20 triangles times 3 sides is 60, halved is 30 edges. Dodecahedron: 12 pentagons times 5 is 60, halved is 30. The magic 2 still works: the icosahedron's 12 take away 30 add 20 is 2. The questions for this section: the five dice and their counts, the swapping pairs, and the halving shortcut for edges.

## Subtopic: Why Only Five Fit

Why only five? Think about one corner. At least three faces must meet there, and their angles must add up to less than a full turn of 360 degrees, otherwise the corner goes flat or will not close.

A triangle's corner is 60 degrees. Three triangles at a corner: 180, fine, the tetrahedron. Four: 240, fine, the octahedron. Five: 300, fine, the icosahedron. Six: 360, flat as a floor tile. So triangles give three solids.

A square's corner is 90. Three squares: 270, fine, the cube. Four: 360, flat. A pentagon's corner is 108. Three: 324, fine, the dodecahedron. Four: 432, too much. A hexagon's corner is 120. Three: 360, flat, like a honeycomb. Anything with more sides is even bigger, so nothing else fits. Five solids, and that is the end of the list for ever.

Watch out for impostors. Two triangle pyramids glued together have 6 equal triangle faces, but some corners have 3 triangles and some have 4, so it is not one of the five. A soccer ball is made of pentagons and hexagons, two different shapes, so it is not one either.

Flat sides, folds and corners with the magic 2; five fair dice with the halving shortcut; corners that must add to less than 360. The final questions of the lesson are with you now: the corner angles, why six triangles go flat, and spotting the impostors.
