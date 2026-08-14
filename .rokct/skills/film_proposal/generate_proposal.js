#!/usr/bin/env node
/**
 * ROKCT STUDIOS — Film Proposal Generator
 *
 * Reads the production bible from film/{project}/ and writes
 * a broadcast-ready eTV submission .docx
 *
 * Usage (from repo root):
 *   node .rokct/skills/film_proposal/generate_proposal.js [project] [out.docx]
 *
 * Defaults:
 *   project  → venda_nga_december
 *   out.docx → film/{project}/proposal.docx
 *
 * What it reads:
 *   film/{project}/00_index.md
 *   film/{project}/metarules/world_rules.md
 *   film/{project}/characters/*.md
 *   film/{project}/scenes/all_scenes.md
 *   film/{project}/themes/all_themes.md
 *   film/{project}/bubbles/*.md
 *
 * Update any bible file → rerun → fresh proposal.
 */

'use strict';
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageBreak, VerticalAlign
} = require('docx');
const fs   = require('fs');
const path = require('path');

// ─── PATHS ───────────────────────────────────────────────────────────────────
const project    = process.argv[2] || 'venda_nga_december';
const outputArg  = process.argv[3] || null;
const SCRIPT_DIR = path.dirname(path.resolve(__filename));
// Script lives at .rokct/skills/film_proposal/ → repo root is 3 levels up
const REPO_ROOT  = path.resolve(SCRIPT_DIR, '../../..');
const BIBLE      = path.join(REPO_ROOT, 'film', project);
const OUT        = outputArg ? path.resolve(outputArg) : path.join(BIBLE, 'proposal.docx');

if (!fs.existsSync(BIBLE)) {
  console.error(`\nERROR: Cannot find bible folder:\n  ${BIBLE}\n`);
  process.exit(1);
}
console.log(`\nReading bible: ${BIBLE}`);

// ─── READ ────────────────────────────────────────────────────────────────────
function read(rel) {
  const f = path.join(BIBLE, rel);
  return fs.existsSync(f) ? fs.readFileSync(f, 'utf8') : '';
}
function readChars() {
  const dir = path.join(BIBLE, 'characters');
  if (!fs.existsSync(dir)) return {};
  return Object.fromEntries(
    fs.readdirSync(dir).filter(f => f.endsWith('.md'))
      .map(f => [f.replace('.md',''), fs.readFileSync(path.join(dir,f),'utf8')])
  );
}

const IDX    = read('00_index.md');
const WORLD  = read('metarules/world_rules.md');
const SCENES = read('scenes/all_scenes.md');
const CHARS  = readChars();

// ─── PARSE ───────────────────────────────────────────────────────────────────
function section(text, heading) {
  const re = new RegExp(`##+ ${heading}[\\s\\S]*?(?=\\n##+ |$)`, 'i');
  const m  = text.match(re);
  return m ? m[0].replace(/^##+ [^\n]+\n/, '').trim() : '';
}
function strip(t) {
  return t.replace(/\*\*(.+?)\*\*/g,'$1').replace(/\*(.+?)\*/g,'$1')
          .replace(/^#+\s+/gm,'').replace(/^[-*]\s+/gm,'')
          .replace(/`([^`]+)`/g,'$1').replace(/\[([^\]]+)\]\([^)]+\)/g,'$1').trim();
}
function paras(t) {
  return strip(t).split(/\n\n+/).map(p=>p.replace(/\n/g,' ').trim()).filter(Boolean);
}

function getLogline() {
  const s = section(IDX,'The Logline');
  return paras(s)[0] || 'A man from Thohoyandou tattooed his dream on his chest before the world knew his name. This documentary is as permanent as that tattoo.';
}
function getCompany() {
  const m = IDX.match(/ROKCT INTELLIGENCE[^\n]*/i);
  return m ? m[0].trim() : 'ROKCT INTELLIGENCE (PTY) LTD t/a ROKCT STUDIOS';
}
function getCQ() {
  return paras(section(WORLD,'The Central Question'))[0] || 'What does a man from Thohoyandou have to carry, sacrifice, and survive to make the world hear him — and what does he hold onto when everything else is negotiable?';
}

function charData(slug) {
  const t = CHARS[slug]; if (!t) return null;
  const name  = (t.match(/^# (.+)$/m)||['','Unknown'])[1].trim();
  const role  = paras(section(t,'Role')).slice(0,2).join(' ');
  const fee   = (t.match(/\*\*Fee:\*\*\s*(R[\d,]+)/i)||['','—'])[1];
  const id    = (t.match(/\*\*Identity:\*\*\s*([^\n]+)/i)||['','Negotiated'])[1].trim();
  const arch  = section(t,'Archive Bubbles — Verified Facts')
                  .split('\n').filter(l=>/^[-*]/.test(l.trim()))
                  .map(l=>strip(l).replace(/^[-*]\s*/,'')).slice(0,4);
  return { name, role, fee, id, arch };
}

function sceneBlock(n) {
  const re  = new RegExp(`# Scene ${n}[^\n]*\n([\\s\\S]*?)(?=\n# Scene |$)`);
  const m   = SCENES.match(re); if (!m) return null;
  const blk = m[0];
  const title   = (blk.match(/^# Scene \d+ — (.+)$/m)||['',''])[1].trim();
  const runtime = (blk.match(/## Runtime\n([^\n]+)/)||['',''])[1].trim();
  const desc    = paras(section(blk,'What Happens')).slice(0,2).join(' ');
  return { title, runtime, desc };
}

// ─── DESIGN ──────────────────────────────────────────────────────────────────
const DARK   = '1A1A1A', WHITE  = 'FFFFFF', ACCENT = 'C0392B',
      MID    = '555555', LIGHT  = 'F5F5F5', RULEC  = 'CCCCCC';

const B  = s => ({ style: BorderStyle.SINGLE, size: s||1, color: RULEC });
const NB = () => ({ style: BorderStyle.NONE,  size: 0,    color: WHITE });
const brds  = { top:B(), bottom:B(), left:B(), right:B() };
const noBrds= { top:NB(),bottom:NB(),left:NB(),right:NB() };

const sp = (pt=120) => new Paragraph({ spacing:{ before:0, after:pt } });
const hr = (color=RULEC, sz=4) => new Paragraph({
  spacing:{ before:0, after:160 },
  border:{ bottom:{ style:BorderStyle.SINGLE, size:sz, color } }
});

const h1 = t => new Paragraph({ heading:HeadingLevel.HEADING_1, children:[new TextRun({ text:t, bold:true, size:28, font:'Arial', color:DARK })] });
const h2 = t => new Paragraph({ heading:HeadingLevel.HEADING_2, children:[new TextRun({ text:t, bold:true, size:22, font:'Arial', color:ACCENT })] });
const h3 = t => new Paragraph({ spacing:{before:200,after:80}, children:[new TextRun({ text:t, bold:true, size:20, font:'Arial', color:DARK })] });

const body = (t, o={}) => new Paragraph({
  spacing:{before:0,after:120},
  children:[new TextRun({ text:t, size:20, font:'Arial', color:o.color||DARK, bold:!!o.bold, italics:!!o.italic })]
});
const bul = t => new Paragraph({
  numbering:{reference:'bullets',level:0}, spacing:{before:0,after:80},
  children:[new TextRun({ text:t, size:20, font:'Arial', color:DARK })]
});
const centred = (t, sz=20, opts={}) => new Paragraph({
  alignment:AlignmentType.CENTER, spacing:{ before:opts.before||0, after:opts.after||80 },
  children:[new TextRun({ text:t, size:sz, font:'Arial', color:opts.color||DARK, bold:!!opts.bold, italics:!!opts.italic })]
});

function cl(text, width, o={}) {
  return new TableCell({
    width:{ size:width, type:WidthType.DXA },
    borders: o.noBorder ? noBrds : brds,
    shading:{ fill:o.fill||WHITE, type:ShadingType.CLEAR },
    margins:{ top:60, bottom:60, left:o.pad||120, right:o.pad||120 },
    verticalAlign:VerticalAlign.CENTER,
    children:[new Paragraph({
      alignment:o.align||AlignmentType.LEFT,
      children:[new TextRun({ text, size:o.size||18, font:'Arial', color:o.color||DARK, bold:!!o.bold, italics:!!o.italic })]
    })]
  });
}
const hRow = (...cols) => new TableRow({ children: cols.map(([t,w]) => cl(t,w,{fill:DARK,color:WHITE,bold:true})) });
const dRow = (cols, shade) => new TableRow({ children: cols.map(([t,w,o={}]) => cl(t,w,{fill:shade?LIGHT:WHITE,...o})) });

// ─── BUDGET DATA ─────────────────────────────────────────────────────────────
const BUDGET = [
  ['Producer / Director fee',         'Principal creative and production leadership',                   'R45,000'],
  ['Camera equipment rental',         'Multi-camera locked setup, lenses, supports — 6 days',          'R35,000'],
  ['Sound recordist + equipment',     '6 shoot days',                                                   'R18,000'],
  ['Lighting equipment rental',       'Production studio lighting setup',                               'R12,000'],
  ['Editor fee',                      'Assembly through picture lock incl. bubble layer composition',   'R32,000'],
  ['Colour grade',                    '3-grade system — studio, b-roll, reconstruction',               'R12,000'],
  ['Sound mix',                       'Final broadcast mix',                                            'R10,000'],
  ['Music licensing / composer',      'VenRap track clearances or original score',                     'R14,000'],
  ['Production studio rental + dress','Thohoyandou studio hire and preparation',                        'R8,000' ],
  ['Transport + fuel',                'Local Thohoyandou transport, 6 shoot days',                      'R6,000' ],
  ['Subtitling',                      'English subtitles — professional service',                       'R8,000' ],
  ['Participant fees',                '6 principal contributors',                                        'R32,000'],
  ['Dramatic reconstruction',         'Local performers, 1 shoot day',                                  'R8,000' ],
  ['Archive / social media research', 'Ricky Rick archive, community bubble collection',                'R5,000' ],
  ['Contingency',                     '5%',                                                             'R13,120'],
];

const PARTICIPANTS = [
  ['mizo_phyll','2 dedicated shoot sessions, full identity on camera, closing performance, music licensing'],
  ['the_wife',  'Most intimate testimony, full identity, sensitive subject matter'],
  ['tman_gavin','Supporting witness, negotiated identity'],
  ['nicodemic', 'Supporting witness, negotiated identity'],
  ['the_producer','Supporting witness, full identity, origin story'],
  ['the_faith_witness','Single session, supporting role'],
];

const SCHEDULE = [
  ['Day 1','Mizo Phyll — primary interview (60–90 min recorded)','Production studio, Thohoyandou'],
  ['Day 2','Wife, Tman Gavin, Nicodemic — individual interviews, isolated from each other','Production studio, Thohoyandou'],
  ['Day 3','DJ Davic + Faith witness — interviews','Production studio, Thohoyandou'],
  ['Day 3','Mizo Phyll — return interview (situational questions) + closing performance','Production studio, Thohoyandou'],
  ['Day 4','B-roll — Thohoyandou streets, Maniini Block J, VenRap environment','Thohoyandou locations'],
  ['Day 5','Dramatic reconstruction — early career scenes','Thohoyandou locations'],
  ['Day 6','Contingency / pickup shots','TBC'],
];

const SUBJECTS = [
  ['Mizo Phyll (Livhuwani Aubrey Ratshiungo)','Principal subject — the spine','Thohoyandou','Full face'],
  ['Wife of Mizo Phyll','Most intimate voice','Thohoyandou','Full face'],
  ['Tman Gavin','Supporting witness','Thohoyandou','Negotiated'],
  ['Nicodemic','Supporting witness','Thohoyandou','Negotiated'],
  ['DJ Davic','Producer — origin story','Thohoyandou','Full face'],
  ['Faith community witness','Spiritual reckoning','Thohoyandou','Negotiated'],
];

const CHECKLIST = [
  ['✓','Detailed treatment of proposed documentary (this document)'],
  ['✓','Description of locations and names of individuals to be interviewed (Sections 10 and 11)'],
  ['☐','Location release form — production studio, Thohoyandou'],
  ['☐','Location release forms — Thohoyandou b-roll locations'],
  ['☐','Subject release forms — all six principal contributors'],
  ['☐','Signed e.tv disclaimer form'],
  ['✓','Production budget with detailed personnel and resource breakdown (Section 9)'],
  ['✓','Confirmation of key personnel based in Limpopo province'],
  ['☐','Production company registration details'],
  ['☐','Names, race and gender of shareholders'],
  ['☐','Names, race and gender of directors'],
  ['☐','Names, race and gender of senior personnel and positions'],
  ['☐','Details of training initiatives in past 12 months'],
];

// ─── BUILD ───────────────────────────────────────────────────────────────────
function build() {
  const company = getCompany();
  const logline = getLogline();
  const cq      = getCQ();

  // Character section rows
  const charSlugs = [
    ['mizo_phyll',       'The Spine'],
    ['the_wife',         'The Most Intimate Voice'],
    ['tman_gavin',       'The Witness — Same Streets, Different Outcome'],
    ['nicodemic',        'The Witness — Same Streets, Different Outcome'],
    ['the_producer',     'The Producer Who Believed First'],
    ['the_faith_witness','The Spiritual Reckoning'],
    ['ricky_rick',       'The Absent Presence'],
  ];

  const charItems = [];
  charSlugs.forEach(([slug, label]) => {
    const c = charData(slug); if (!c) return;
    charItems.push(h2(`${c.name} — ${label}`));
    c.role.split(/\n+/).map(p=>p.trim()).filter(Boolean).slice(0,3).forEach(p => charItems.push(body(p)));
    if (c.arch.length) {
      charItems.push(body('Verified facts for this character:', {bold:true}));
      c.arch.forEach(a => charItems.push(bul(a)));
    }
    charItems.push(sp(120));
  });

  // Scene arc rows
  const arcItems = [];
  for (let i=1; i<=7; i++) {
    const s = sceneBlock(i); if (!s) continue;
    arcItems.push(h3(`${s.title}${s.runtime ? '  —  ' + s.runtime : ''}`));
    if (s.desc) arcItems.push(body(s.desc));
    arcItems.push(sp(100));
  }

  // Participant fee table rows
  const partRows = PARTICIPANTS.map(([slug, just], i) => {
    const c = charData(slug);
    const name = c ? c.name : slug;
    const fee  = c ? c.fee  : '—';
    return dRow([[name,3200,{bold:true}],[just,4360,{italic:true,color:MID}],[fee,1800,{align:AlignmentType.RIGHT}]], i%2!==0);
  });

  const children = [
    // ── COVER ──
    sp(2400),
    centred('DOCUMENTARY PROPOSAL',20,{color:MID,bold:true}),
    centred('e.tv — Hidden Gems of Mzansi: Regional Documentaries',20,{color:MID,after:80}),
    sp(400), hr(ACCENT,8), sp(200),
    centred('AGAINST ALL ODDS',22,{color:MID,bold:true}),
    centred('VENDA NGA DECEMBER',52,{color:DARK,bold:true,before:120,after:120}),
    centred('The King of VenRap',22,{color:MID,bold:true}),
    sp(200), hr(ACCENT,8), sp(400),
    centred('A Documentary Film',20,{color:MID}),
    centred('Thohoyandou, Vhembe District, Limpopo',20,{color:MID,bold:true,before:60,after:60}),
    sp(600),
    centred(company,20,{bold:true}),
    centred('Limpopo, South Africa',18,{color:MID,before:80,after:80}),
    sp(300),
    centred('Running time: 23 minutes  |  Language: Tshivenda / English — with English subtitles',18,{color:MID}),
    centred('Proposed budget: R265,120.00',18,{color:MID,before:60,after:60}),
    centred('Submission: documentaries@etv.co.za',18,{color:MID}),
    new Paragraph({ children:[new PageBreak()] }),

    // ── 1 LOGLINE ──
    h1('1. LOGLINE'), hr(), sp(80),
    new Paragraph({ spacing:{before:0,after:200}, children:[new TextRun({ text:logline, size:24, font:'Arial', color:DARK, italics:true, bold:true })] }),
    sp(200),

    // ── 2 HIDDEN GEM ──
    h1('2. THE HIDDEN GEM — THOHOYANDOU AND VENRAP'), hr(), sp(80),
    body('South Africa knows Limpopo for the Kruger National Park, the baobab trees, and the Beit Bridge border. What it does not know — what it has never been shown — is that deep in the Vhembe District, in the streets and yards of Thohoyandou, a music culture grew without asking anyone\'s permission.'),
    body('VenRap. Venda hip-hop. A sound that carries the Tshivenda language, the Limpopo landscape, the spiritual depth of a people, and the hunger of young men who grew up in the northernmost corner of the country and decided the world needed to hear them.'),
    body('Most South Africans have never heard of VenRap. Most South Africans could not find Thohoyandou on a map. One man changed that. He carried Thohoyandou on his chest — literally — and took it to stages, studios, and collaborations that the north had never seen before.'),
    body('This documentary is the story of that man, that place, and that journey. It is made by someone who was there at the beginning — who designed the first album cover, who watched from Musina before anyone believed. This access cannot be bought. No outsider can make this film.'),
    sp(200),

    // ── 3 STORY ──
    h1('3. THE STORY'), hr(), sp(80),
    body('There is a tattoo on his chest. Three words: VENDA NGA DECEMBER.'),
    body('He got it before the record deal. Before the national stages. Before the collaborations with artists the whole country knew. He got it when he was a young man from Thohoyandou with dreads, a deep faith, and a sound nobody had a name for yet. The tattoo was a declaration — a vow, a flag planted in his own skin before the world decided whether he was worth anything.'),
    body('This documentary never leaves that tattoo. Every conversation, every testimony, every moment of the film radiates outward from those three words and returns to them. This is not a career documentary. It does not follow a timeline or trace a discography. It asks one question:',{bold:false}),
    sp(80),
    new Paragraph({ indent:{left:720}, spacing:{before:80,after:80}, children:[new TextRun({ text:cq, size:22, font:'Arial', color:DARK, italics:true })] }),
    sp(120),
    body('The answer lives in his chest.'),
    sp(200),

    // ── 4 SUBJECT ──
    h1('4. THE SUBJECT — MIZO PHYLL'), hr(), sp(80),
    body('Mizo Phyll — Livhuwani Aubrey Ratshiungo — is the King of VenRap. He says so himself when he introduces himself: Ndi dzi king. And he is not wrong.'),
    body('He came from Maniini Block J, Thohoyandou, when VenRap was not yet a genre anyone recognised. He carried the Rastafari faith — the dreads, the doctrine, the vows. He made hip-hop that sounded like nowhere else in South Africa because it came from nowhere else.'),
    body('Then the music industry found him. The industry had conditions. The dreads came off. What that meant — to him, to his faith community, to his wife, to the men who grew up alongside him in the same yards — is the emotional heart of this documentary.'),
    body('He worked with the late Ricky Rick. He brought Venda to national stages. He created the Venda Nga December platform for Venda artists. He won the first-ever Best Tshivenda Hip-Hop category at the Tshivenda Music Awards in 2012. He has agreed in principle to participate — full face, full name, the tattoo on camera.'),
    sp(200),

    // ── 5 CHARACTERS ──
    h1('5. CHARACTERS'), hr(), sp(80),
    ...charItems, sp(200),

    // ── 6 ARC ──
    h1('6. NARRATIVE ARC — 23 MINUTES'), hr(), sp(80),
    ...arcItems, sp(200),

    // ── 7 VISUAL ──
    h1('7. VISUAL AND PRODUCTION APPROACH'), hr(), sp(80),
    h2('The Production Studio'),
    body('All principal interviews are conducted in a single controlled studio environment in Thohoyandou — dressed and lit specifically for this documentary. No natural light. Complete control of the image. The studio creates visual unity across all characters, evokes the sacred consultation space of indigenous tradition, and eliminates location noise and continuity problems. This is a deliberate aesthetic decision, not a budget limitation.'),
    h2('The Bubble Information Layer'),
    body('This documentary introduces a second simultaneous information track — a bubble layer that surfaces verified facts, archived quotes, and community testimony throughout the film, without ever interrupting the speaker or cutting away from their face. Three types operate across the film:'),
    bul('Archive Bubbles — verified historical facts appearing as clean text during informational moments. Example: "My African Dream — first artist to win Best Tshivenda Hip-Hop, Tshivenda Music Awards (2012)"'),
    bul('Cut Floor Bubbles — extraordinary material from interviews that the 23-minute structure cannot hold, including the late Ricky Rick\'s own archived public words about Mizo Phyll. His own words, from the record. Not paraphrased. Not narrated.'),
    bul('Community Bubbles — public social media testimony collected during pre-production. Facebook does not forget. These fill the dark spaces during the closing performance.'),
    h2('Multi-Camera Setup'),
    body('The studio operates on a multi-camera locked-off system. Multiple cameras are positioned and secured before each interview. The director functions as interviewer — fully present in the conversation, not managing equipment. Minimal crew of two in the room.'),
    h2('The Chest — The Film\'s Recurring Image'),
    body('The tattoo on his chest is the film\'s visual heartbeat. It is the opening image. It is the ad break transition device at every break. It is a detail shot during interview. It is the film\'s last image before black. VENDA NGA DECEMBER is the most repeated image in this documentary.'),
    h2('The Closing Performance and Credits'),
    body('The film ends with a live performance in the studio — alone, no audience, no stage, no direction. As he raps, community testimony fills the dark spaces around him. Then the messages transform — same visual format — into credits. The names of the people who made this film arrive in the same format as the facts that carried the whole film. The credits are the film\'s final argument: these names were also permanent.'),
    h2('Dramatic Reconstruction'),
    body('Brief reconstructions are used for moments that cannot be filmed — early career dismissal, the first performance nobody attended. Shot in a warmer, overexposed colour treatment. Silent, narrated. Local performers. One shoot day.'),
    sp(200),

    // ── 8 PLAN ──
    h1('8. PRODUCTION PLAN'), hr(), sp(80),
    new Table({
      width:{ size:9360, type:WidthType.DXA },
      columnWidths:[1200,5760,2400],
      rows:[
        hRow(['Day',1200],['Activity',5760],['Location',2400]),
        ...SCHEDULE.map(([d,a,l],i) => dRow([[d,1200,{bold:true}],[a,5760],[l,2400,{italic:true,color:MID}]],i%2!==0))
      ]
    }),
    sp(200),

    // ── 9 BUDGET ──
    h1('9. PRODUCTION BUDGET'), hr(), sp(80),
    new Table({
      width:{ size:9360, type:WidthType.DXA },
      columnWidths:[3200,4160,2000],
      rows:[
        hRow(['Line Item',3200],['Detail',4160],['Amount',2000]),
        ...BUDGET.map(([item,detail,amount],i) => dRow(
          [[item,3200],[detail,4160,{italic:true,color:MID}],[amount,2000,{align:AlignmentType.RIGHT}]],
          i%2!==0
        )),
        new TableRow({ children:[
          cl('TOTAL',3200,{fill:DARK,color:WHITE,bold:true,size:20}),
          cl('',4160,{fill:DARK}),
          cl('R265,120',2000,{fill:DARK,color:WHITE,bold:true,size:20,align:AlignmentType.RIGHT})
        ]})
      ]
    }),
    sp(160),
    h2('Participant Fee Breakdown'),
    new Table({
      width:{ size:9360, type:WidthType.DXA },
      columnWidths:[3200,4360,1800],
      rows:[
        hRow(['Participant',3200],['Justification',4360],['Fee',1800]),
        ...partRows
      ]
    }),
    sp(80),
    body('All participant fees: 50% on signed release form, 50% on completion of filming days. All payments via EFT with signed receipts.',{italic:true,color:MID}),
    sp(200),

    // ── 10 LOCATIONS ──
    h1('10. LOCATIONS'), hr(), sp(80),
    h2('Primary — Production Studio, Thohoyandou'),
    body('Controlled studio environment — rented room in Thohoyandou, dressed and lit as a professional production studio. Used across Days 1, 2 and 3. Address confirmed on production company registration.'),
    h2('Secondary — Thohoyandou Town and Surrounds'),
    body('Maniini Block J and surrounding streets, Thohoyandou town centre, Vhembe District locations associated with the VenRap scene. All filming in public spaces or with confirmed location permission. Used for b-roll and dramatic reconstruction, Days 4 and 5.'),
    sp(200),

    // ── 11 SUBJECTS ──
    h1('11. SUBJECTS TO BE INTERVIEWED'), hr(), sp(80),
    new Table({
      width:{ size:9360, type:WidthType.DXA },
      columnWidths:[2800,3160,1800,1600],
      rows:[
        hRow(['Subject',2800],['Role',3160],['Location',1800],['Identity',1600]),
        ...SUBJECTS.map((r,i) => dRow(r.map((t,j)=>[t,[2800,3160,1800,1600][j]]),i%2!==0))
      ]
    }),
    sp(80),
    body('Formal signed release forms to be submitted with the final proposal package. Mizo Phyll and DJ Davic have agreed in principle to participate. All other subjects have been approached.',{italic:true,color:MID}),
    sp(200),

    // ── 12 NO PRESENTER ──
    h1('12. PRESENTER / COMMENTATOR'), hr(), sp(80),
    body('This documentary does not use a presenter or narrator. The film is entirely built from the voices of its principal subjects and the bubble information layer. A presenter\'s voice would impose a singular interpretation on a story whose power comes from allowing multiple truths to coexist. The production studio is the presenter. The tattoo is the narrator. The audience is the judge.'),
    sp(200),

    // ── 13 WHY ──
    h1('13. WHY THIS STORY. WHY THOHOYANDOU. WHY NOW.'), hr(), sp(80),
    body('South Africa has never seen a documentary about VenRap. It has never been shown Thohoyandou as a music capital. It does not know that a man from the streets of Vhembe carried his hometown tattooed on his chest all the way to national stages and never took it off.'),
    body('This is the hidden gem. Not just the artist — the entire culture he came from and represents. A music tradition that grew without permission, without industry support, without anyone in Johannesburg paying attention — and produced a King.'),
    body('Every South African who has ever come from somewhere the country overlooked will recognise this film. Every person who has ever had to negotiate between where they came from and where they are going will understand this film.'),
    new Paragraph({ spacing:{before:160,after:200}, children:[new TextRun({ text:'That is a national audience. And this is their hidden gem.', bold:true, size:22, font:'Arial', color:DARK, italics:true })] }),
    sp(200),

    // ── 14 COMPANY ──
    h1('14. PRODUCTION COMPANY INFORMATION'), hr(), sp(80),
    new Table({
      width:{ size:9360, type:WidthType.DXA },
      columnWidths:[3600,5760],
      rows:[
        ['Company name', company],
        ['Province of operation','Limpopo'],
        ['Production base','Limpopo, South Africa'],
        ['Key personnel location','All key personnel are based in Limpopo province'],
        ['Registration number','[To be completed]'],
        ['Director details','[To be completed]'],
        ['Shareholder details','[To be completed]'],
        ['BEE details','[To be completed]'],
        ['Training initiatives (12 months)','[To be completed]'],
      ].map(([k,v],i) => dRow([[k,3600,{bold:true}],[v,5760]],i%2!==0))
    }),
    sp(200),

    // ── 15 CHECKLIST ──
    h1('15. SUBMISSION DOCUMENTS CHECKLIST'), hr(), sp(80),
    new Table({
      width:{ size:9360, type:WidthType.DXA },
      columnWidths:[720,8640],
      rows: CHECKLIST.map(([check,text],i) => new TableRow({ children:[
        new TableCell({ width:{size:720,type:WidthType.DXA}, borders:noBrds, margins:{top:60,bottom:60,left:0,right:120}, children:[new Paragraph({ alignment:AlignmentType.CENTER, children:[new TextRun({ text:check, size:18, font:'Arial', color:check==='✓'?ACCENT:DARK, bold:true })] })] }),
        new TableCell({ width:{size:8640,type:WidthType.DXA}, borders:noBrds, shading:{fill:i%2===0?WHITE:LIGHT,type:ShadingType.CLEAR}, margins:{top:60,bottom:60,left:120,right:120}, children:[new Paragraph({ children:[new TextRun({ text, size:18, font:'Arial', color:DARK })] })] })
      ]}))
    }),
    sp(200),

    // ── CLOSE ──
    hr(ACCENT,6), sp(120),
    centred('AGAINST ALL ODDS  /  VENDA NGA DECEMBER  /  The King of VenRap',20,{bold:true}),
    centred('A documentary film. Thohoyandou, Limpopo. 2026.',18,{color:MID,italic:true,before:80,after:80}),
    centred(company,18,{bold:true}),
    centred('documentaries@etv.co.za',18,{color:MID,before:60,after:60}),
  ];

  return new Document({
    numbering:{ config:[{ reference:'bullets', levels:[{ level:0, format:LevelFormat.BULLET, text:'–', alignment:AlignmentType.LEFT, style:{ paragraph:{ indent:{ left:720, hanging:360 } } } }] }] },
    styles:{
      default:{ document:{ run:{ font:'Arial', size:20 } } },
      paragraphStyles:[
        { id:'Heading1', name:'Heading 1', basedOn:'Normal', next:'Normal', quickFormat:true, run:{ size:28, bold:true, font:'Arial', color:DARK }, paragraph:{ spacing:{ before:360, after:120 }, outlineLevel:0 } },
        { id:'Heading2', name:'Heading 2', basedOn:'Normal', next:'Normal', quickFormat:true, run:{ size:22, bold:true, font:'Arial', color:ACCENT }, paragraph:{ spacing:{ before:240, after:80 }, outlineLevel:1 } }
      ]
    },
    sections:[{
      properties:{ page:{ size:{ width:11906, height:16838 }, margin:{ top:1440, right:1260, bottom:1440, left:1260 } } },
      children
    }]
  });
}

// ─── WRITE ───────────────────────────────────────────────────────────────────
const doc = build();
Packer.toBuffer(doc).then(buf => {
  fs.mkdirSync(path.dirname(OUT), { recursive:true });
  fs.writeFileSync(OUT, buf);
  console.log(`✅  Proposal written → ${OUT}`);
  console.log(`    ${(buf.length/1024).toFixed(1)} KB   |   Edit any file in film/${project}/ and rerun.\n`);
}).catch(err => {
  console.error('Build error:', err.message);
  process.exit(1);
});
