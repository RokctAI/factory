# Keeps every word group (<g class="w">, from font.text/texts) inside the
# shape it sits on: a bubble, box, card, sign or tile, with padding from the
# shape's inner stroke edge, or inside the canvas when it sits on nothing.
#
#   check(svg)  -> list of problems (one per word group that does not fit)
#   fix(svg)    -> svg with each misfit group (or stack of lines) shrunk
#                  about its centre, and moved toward the shape's centre
#                  only as far as needed.
#
# The same rules are in lms/dart/test/r3_picture_test.dart ("words sit
# inside their shape"), so the shipped set is checked in CI too.
import math, re
import xml.etree.ElementTree as ET

PAD = 6.0          # px from the container's inner stroke edge, at scale 1
                   # (a fifth of the shape's inner size when that is less)
CANVAS_PAD = 4.0   # px from the canvas edge for words on no shape
NS = '{http://www.w3.org/2000/svg}'

# ---------------------------------------------------------------- matrices
def mul(a, b):
    return (a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1],
            a[0] * b[2] + a[2] * b[3], a[1] * b[2] + a[3] * b[3],
            a[0] * b[4] + a[2] * b[5] + a[4], a[1] * b[4] + a[3] * b[5] + a[5])

I = (1, 0, 0, 1, 0, 0)

def inv(m):
    a, b, c, d, e, f = m
    det = a * d - b * c
    return (d / det, -b / det, -c / det, a / det, (c * f - d * e) / det, (b * e - a * f) / det)

def ap(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])

def mscale(m):
    return math.sqrt(abs(m[0] * m[3] - m[1] * m[2]))

FN = re.compile(r'(matrix|translate|scale|rotate)\s*\(([^)]*)\)')
NUM = re.compile(r'[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?')

def parse_transform(s):
    m = I
    for fn, args in FN.findall(s or ''):
        v = [float(x) for x in NUM.findall(args)]
        if fn == 'matrix':
            t = tuple(v)
        elif fn == 'translate':
            t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif fn == 'scale':
            t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        else:
            a = math.radians(v[0]); ca, sa = math.cos(a), math.sin(a)
            t = (ca, sa, -sa, ca, 0, 0)
            if len(v) == 3:
                t = mul(mul((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
        m = mul(m, t)
    return m

# ------------------------------------------------------------------- paths
TOK = re.compile(r'([MmLlHhVvQqTtCcSsAaZz])|([-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)')
ARGS = dict(M=2, L=2, H=1, V=1, Q=4, T=2, C=6, S=4, A=7, Z=0)

def _arc(x1, y1, rx, ry, phi, fa, fs, x2, y2, n=12):
    if rx == 0 or ry == 0 or (x1 == x2 and y1 == y2):
        return [(x2, y2)]
    rx, ry = abs(rx), abs(ry)
    p = math.radians(phi); cp, sp = math.cos(p), math.sin(p)
    dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
    x1p, y1p = cp * dx + sp * dy, -sp * dx + cp * dy
    lam = x1p * x1p / (rx * rx) + y1p * y1p / (ry * ry)
    if lam > 1:
        rx *= math.sqrt(lam); ry *= math.sqrt(lam)
    num = rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p
    den = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    co = math.sqrt(max(0, num / den)) if den else 0
    if fa == fs:
        co = -co
    cxp, cyp = co * rx * y1p / ry, -co * ry * x1p / rx
    cx = cp * cxp - sp * cyp + (x1 + x2) / 2
    cy = sp * cxp + cp * cyp + (y1 + y2) / 2
    def ang(ux, uy, vx, vy):
        return math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)
    t1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dt = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not fs and dt > 0:
        dt -= 2 * math.pi
    elif fs and dt < 0:
        dt += 2 * math.pi
    out = []
    for i in range(1, n + 1):
        t = t1 + dt * i / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        out.append((cp * x - sp * y + cx, sp * x + cp * y + cy))
    return out

def subpaths(d):
    """Flatten path data into [(points, closed)]."""
    toks = TOK.findall(d)
    out, cur = [], []
    x = y = sx = sy = 0.0
    lq = lc = None  # last quad / cubic control point
    cmd = None
    i = 0
    vals = []
    def flush(closed):
        nonlocal cur
        if len(cur) > 1:
            out.append((cur, closed))
        cur = []
    seq = []
    for c, n in toks:
        if c:
            seq.append(c)
        else:
            seq.append(float(n))
    i = 0
    while i < len(seq):
        if isinstance(seq[i], str):
            cmd = seq[i]; i += 1
            if cmd in 'Zz':
                if cur:
                    flush(True)
                x, y = sx, sy
                lq = lc = None
                continue
        if cmd is None:
            i += 1; continue
        U = cmd.upper(); rel = cmd != U
        k = ARGS[U]
        a = seq[i:i + k]
        if len(a) < k or any(isinstance(v, str) for v in a):
            i += 1; continue
        i += k
        if U == 'M':
            flush(False)
            x, y = (x + a[0], y + a[1]) if rel else (a[0], a[1])
            sx, sy = x, y
            cur = [(x, y)]
            cmd = 'l' if rel else 'L'
            lq = lc = None
            continue
        if not cur:
            cur = [(x, y)]
        if U == 'L':
            x, y = (x + a[0], y + a[1]) if rel else (a[0], a[1]); cur.append((x, y)); lq = lc = None
        elif U == 'H':
            x = x + a[0] if rel else a[0]; cur.append((x, y)); lq = lc = None
        elif U == 'V':
            y = y + a[0] if rel else a[0]; cur.append((x, y)); lq = lc = None
        elif U in 'QT':
            if U == 'Q':
                qx, qy = (x + a[0], y + a[1]) if rel else (a[0], a[1])
                ex, ey = (x + a[2], y + a[3]) if rel else (a[2], a[3])
            else:
                qx, qy = (2 * x - lq[0], 2 * y - lq[1]) if lq else (x, y)
                ex, ey = (x + a[0], y + a[1]) if rel else (a[0], a[1])
            for j in range(1, 9):
                t = j / 8
                cur.append(((1 - t) ** 2 * x + 2 * (1 - t) * t * qx + t * t * ex,
                            (1 - t) ** 2 * y + 2 * (1 - t) * t * qy + t * t * ey))
            lq = (qx, qy); lc = None
            x, y = ex, ey
        elif U in 'CS':
            if U == 'C':
                c1 = (x + a[0], y + a[1]) if rel else (a[0], a[1])
                c2 = (x + a[2], y + a[3]) if rel else (a[2], a[3])
                e = (x + a[4], y + a[5]) if rel else (a[4], a[5])
            else:
                c1 = (2 * x - lc[0], 2 * y - lc[1]) if lc else (x, y)
                c2 = (x + a[0], y + a[1]) if rel else (a[0], a[1])
                e = (x + a[2], y + a[3]) if rel else (a[2], a[3])
            for j in range(1, 9):
                t = j / 8; u = 1 - t
                cur.append((u ** 3 * x + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t ** 3 * e[0],
                            u ** 3 * y + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t ** 3 * e[1]))
            lc = c2; lq = None
            x, y = e
        elif U == 'A':
            ex, ey = (x + a[5], y + a[6]) if rel else (a[5], a[6])
            cur += _arc(x, y, a[0], a[1], a[2], int(a[3]), int(a[4]), ex, ey)
            x, y = ex, ey; lq = lc = None
    flush(False)
    return out

def rect_pts(x, y, w, h, rx, ry):
    rx = min(rx, w / 2); ry = min(ry, h / 2)
    if rx <= 0 or ry <= 0:
        return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    pts = []
    for cx, cy, a0 in ((x + w - rx, y + ry, -90), (x + w - rx, y + h - ry, 0), (x + rx, y + h - ry, 90), (x + rx, y + ry, 180)):
        for j in range(7):
            a = math.radians(a0 + 15 * j)
            pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    return pts

def ell_pts(cx, cy, rx, ry, n=48):
    return [(cx + rx * math.cos(2 * math.pi * j / n), cy + ry * math.sin(2 * math.pi * j / n)) for j in range(n)]

# --------------------------------------------------------------- polygons
def area(p):
    return abs(sum(p[i][0] * p[i - 1][1] - p[i - 1][0] * p[i][1] for i in range(len(p)))) / 2

def inside(p, x, y):
    c = False
    n = len(p)
    for i in range(n):
        x1, y1 = p[i]; x2, y2 = p[i - 1]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c

def densify(p, step=1.0):
    out = []
    n = len(p)
    for i in range(n):
        x1, y1 = p[i - 1]; x2, y2 = p[i]
        L = math.hypot(x2 - x1, y2 - y1)
        k = max(1, int(L / step))
        for j in range(k):
            out.append((x1 + (x2 - x1) * j / k, y1 + (y2 - y1) * j / k))
    return out

def bbox(pts):
    xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
    return min(xs), min(ys), max(xs), max(ys)

def dist_box(px, py, b):
    dx = max(b[0] - px, 0, px - b[2]); dy = max(b[1] - py, 0, py - b[3])
    return math.hypot(dx, dy)

# ---------------------------------------------------------------- reading
def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0

def read(svg):
    """Shapes (in drawing order) and word groups, all in canvas pixels."""
    root = ET.fromstring(svg)
    shapes, words = [], []
    order = [0]
    def walk(el, m, st, in_word):
        tag = el.tag.replace(NS, '')
        m = mul(m, parse_transform(el.get('transform')))
        st = dict(st)
        for a in ('fill', 'stroke', 'stroke-width', 'opacity', 'fill-opacity'):
            if el.get(a) is not None:
                if a in ('opacity', 'fill-opacity'):
                    st[a] = st.get(a, 1) * _num(el.get(a))
                else:
                    st[a] = el.get(a)
        sc = mscale(m)
        if tag == 'g' and el.get('class') == 'w' and not in_word:
            pts = []
            for ch in el.iter():
                t2 = ch.tag.replace(NS, '')
                lm = parse_transform(ch.get('transform')) if ch is not el else I
                if t2 == 'path':
                    sw = _num(ch.get('stroke-width') or el.get('stroke-width') or st.get('stroke-width') or 0)
                    for sp, _ in subpaths(ch.get('d', '')):
                        for (px, py) in sp:
                            pts += [(px - sw / 2, py - sw / 2), (px + sw / 2, py + sw / 2)]
                elif t2 == 'circle':
                    cx, cy, r = _num(ch.get('cx')), _num(ch.get('cy')), _num(ch.get('r'))
                    pts += [(cx - r, cy - r), (cx + r, cy + r)]
            if pts:
                b = bbox(pts)
                quad = [ap(m, b[0], b[1]), ap(m, b[2], b[1]), ap(m, b[2], b[3]), ap(m, b[0], b[3])]
                words.append(dict(el=el, quad=quad, order=order[0], parent=mul(m, inv(parse_transform(el.get('transform'))))))
            order[0] += 1
            return
        if tag in ('rect', 'circle', 'ellipse', 'path') and not in_word:
            fill = st.get('fill', 'black')
            polys = []
            if tag == 'rect':
                rx = _num(el.get('rx')); ry = _num(el.get('ry')) or rx; rx = rx or ry
                polys = [rect_pts(_num(el.get('x')), _num(el.get('y')), _num(el.get('width')), _num(el.get('height')), rx, ry)]
            elif tag == 'circle':
                r = _num(el.get('r')); polys = [ell_pts(_num(el.get('cx')), _num(el.get('cy')), r, r)]
            elif tag == 'ellipse':
                polys = [ell_pts(_num(el.get('cx')), _num(el.get('cy')), _num(el.get('rx')), _num(el.get('ry')))]
            else:
                polys = [sp for sp, _ in subpaths(el.get('d', ''))]
            stroke = st.get('stroke', 'none')
            sw = 0 if stroke == 'none' else _num(st.get('stroke-width', 1)) * sc
            for p in polys:
                if len(p) < 3:
                    continue
                gp = [ap(m, *q) for q in p]
                shapes.append(dict(poly=gp, sw=sw, scale=sc, order=order[0],
                                   filled=fill != 'none' and st.get('opacity', 1) * st.get('fill-opacity', 1) >= .5,
                                   area=area(gp)))
            order[0] += 1
            return
        for ch in el:
            walk(ch, m, st, in_word)
    walk(root, I, {}, False)
    return shapes, words

def is_background(s):
    b = bbox(s['poly'])
    return b[0] <= 2 and b[1] <= 2 and b[2] >= 198 and b[3] >= 198

CANVAS = dict(poly=[(0, 0), (200, 0), (200, 200), (0, 200)], sw=0, scale=1, area=40000, canvas=True)

def container(shapes, w):
    q = w['quad']
    cx = sum(p[0] for p in q) / 4; cy = sum(p[1] for p in q) / 4
    ta = area(q)
    # the shape the words are seen on: the last one drawn under their
    # centre (a bubble drawn over a head is the bubble)
    best = None
    for s in shapes:
        if s['order'] > w['order'] or not s['filled'] or is_background(s):
            continue
        if s['area'] < ta * .5 or not inside(s['poly'], cx, cy):
            continue
        if best is None or s['order'] >= best['order']:
            best = s
    return best or CANVAS

def margin(c):
    if c.get('canvas'):
        return CANVAS_PAD
    # 6px, less on a small shape (a 24px calendar cell keeps ~4.5px):
    # never more than a fifth of the shape's inner size.
    b = bbox(c['poly'])
    inner = min(b[2] - b[0], b[3] - b[1]) - c['sw']
    return c['sw'] / 2 + min(PAD * min(1.0, c['scale']), max(1.5, inner * .2))

def gap(c, quad):
    """How far quad's nearest point is from c's boundary; negative when a
    corner is outside c."""
    for (x, y) in quad:
        if not inside(c['poly'], x, y):
            return -1.0
    b = bbox(quad)
    if '_dense' not in c:
        c['_dense'] = densify(c['poly'], 1.0)
    return min(dist_box(x, y, b) for (x, y) in c['_dense'])

def check(svg):
    shapes, words = read(svg)
    bad = []
    for w in words:
        c = container(shapes, w)
        g_ = gap(c, w['quad'])
        if g_ < margin(c) - 0.5:
            bad.append(dict(order=w['order'], box=bbox(w['quad']), gap=round(g_, 1), need=round(margin(c), 1),
                            canvas=bool(c.get('canvas'))))
    return bad

# ------------------------------------------------------------------ fixing
def _f(v):
    s = f'{v:.1f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s

def _scale_quad(q, cx, cy, s, dx, dy):
    return [(cx + (x - cx) * s + dx, cy + (y - cy) * s + dy) for x, y in q]

def fix(svg):
    shapes, words = read(svg)
    if not words:
        return svg, 0
    cont = [container(shapes, w) for w in words]
    # Stacked lines on one shape move together; side-by-side labels alone.
    n = len(words)
    par = list(range(n))
    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    for i in range(n):
        for j in range(i + 1, n):
            if cont[i] is not cont[j]:
                continue
            a, b = bbox(words[i]['quad']), bbox(words[j]['quad'])
            ov = min(a[2], b[2]) - max(a[0], b[0])
            if ov >= .5 * min(a[2] - a[0], b[2] - b[0]):
                par[find(i)] = find(j)
    groups = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    changes = {}
    moves = {}
    for members in groups.values():
        c = cont[members[0]]
        m = margin(c)
        if all(gap(c, words[i]['quad']) >= m - 0.5 for i in members):
            continue
        ub = bbox([p for i in members for p in words[i]['quad']])
        cx, cy = (ub[0] + ub[2]) / 2, (ub[1] + ub[3]) / 2
        # the shape's centre: the middle of its widest inner box row
        tx, ty = _inner_centre(c, cx, cy)
        def ok(s, t):
            dx, dy = (tx - cx) * t, (ty - cy) * t
            return all(gap(c, _scale_quad(words[i]['quad'], cx, cy, s, dx, dy)) >= m for i in members)
        res = []
        for t in [k / 10 for k in range(11)]:
            if not ok(0.2, t):
                res.append((0, t)); continue
            lo, hi = 0.2, 1.0
            if ok(1.0, t):
                lo = 1.0
            else:
                for _ in range(14):
                    mid = (lo + hi) / 2
                    if ok(mid, t):
                        lo = mid
                    else:
                        hi = mid
            res.append((lo, t))
        best = max(s for s, t in res)
        if best <= 0:
            continue
        s, t = next((s, t) for s, t in res if s >= best * .97)
        dx, dy = (tx - cx) * t, (ty - cy) * t
        A = mul((1, 0, 0, 1, cx + dx, cy + dy), mul((s, 0, 0, s, 0, 0), (1, 0, 0, 1, -cx, -cy)))
        for i in members:
            moves[i] = A
    if not moves:
        return svg, 0
    # Same-size words on same-size shapes (a row of tiles, coins, calendar
    # days) stay the same size: shrink the rest to the smallest. Shrinking a
    # fitting box about its own centre keeps it inside.
    def key(i):
        return round(mscale(mul(words[i]['parent'], parse_transform(words[i]['el'].get('transform')))), 2)
    for i in range(n):
        for j in range(n):
            if i == j or key(i) != key(j) or cont[i].get('canvas') or cont[j].get('canvas'):
                continue
            ai, aj = cont[i]['area'], cont[j]['area']
            if abs(ai - aj) > .3 * max(ai, aj):
                continue
            si = moves[i][0] if i in moves else 1.0
            sj = moves[j][0] if j in moves else 1.0
            if sj < si - 1e-6:
                A = moves.get(i, I)
                q = [ap(A, *p) for p in words[i]['quad']]
                b = bbox(q); qx, qy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
                e = sj / si
                moves[i] = mul(mul((1, 0, 0, 1, qx, qy), mul((e, 0, 0, e, 0, 0), (1, 0, 0, 1, -qx, -qy))), A)
    for i, A in moves.items():
        w = words[i]
        P_ = w['parent']
        T = parse_transform(w['el'].get('transform'))
        changes[w['order']] = mul(mul(inv(P_), mul(A, P_)), T)
    # rewrite the transforms of the changed word groups, in order
    out, idx, pos = [], 0, 0
    order_of = [w['order'] for w in words]
    for mo in re.finditer(r'<g class="w" transform="([^"]*)"', svg):
        o = order_of[idx]; idx += 1
        if o in changes:
            a, b, c2, d, e, f = changes[o]
            if abs(b) < 1e-9 and abs(c2) < 1e-9 and abs(a - d) < 1e-9:
                tr = f'translate({_f(e)} {_f(f)})' + ('' if abs(a - 1) < 5e-4 else f' scale({a:.3f})')
            else:
                tr = 'matrix(' + ' '.join(f'{v:.4f}'.rstrip('0').rstrip('.') for v in (a, b, c2, d)) + f' {_f(e)} {_f(f)})'
            out.append(svg[pos:mo.start(1)] + tr)
            pos = mo.end(1)
    out.append(svg[pos:])
    return ''.join(out), len(changes)

def _chord(p, v, along_x, at):
    """The interval of the line (y = v when along_x, else x = v) inside p
    that holds `at` (or the widest one)."""
    xs = []
    for i in range(len(p)):
        x1, y1 = p[i]; x2, y2 = p[i - 1]
        if along_x:
            if (y1 > v) != (y2 > v):
                xs.append(x1 + (v - y1) * (x2 - x1) / (y2 - y1))
        else:
            if (x1 > v) != (x2 > v):
                xs.append(y1 + (v - x1) * (y2 - y1) / (x2 - x1))
    xs.sort()
    pairs = [(xs[j], xs[j + 1]) for j in range(0, len(xs) - 1, 2)]
    if not pairs:
        return None
    for a, b in pairs:
        if a <= at <= b:
            return a, b
    return max(pairs, key=lambda q: q[1] - q[0])


def _inner_centre(c, cx, cy):
    """The middle of the shape around the words: across, then down."""
    h = _chord(c['poly'], cy, True, cx)
    mx = (h[0] + h[1]) / 2 if h else cx
    v = _chord(c['poly'], mx, False, cy)
    my = (v[0] + v[1]) / 2 if v else cy
    return mx, my


# ---------------------------------------------------------------- overlaps
def _shrink(b, d):
    return (b[0] + d, b[1] + d, b[2] - d, b[3] - d)

def _poly_hits_box(poly, b):
    """True when the filled polygon covers any part of box b."""
    if b[0] >= b[2] or b[1] >= b[3]:
        return False
    for x, y in densify(poly, 1.0):
        if b[0] < x < b[2] and b[1] < y < b[3]:
            return True
    for x, y in ((b[0], b[1]), (b[2], b[1]), (b[2], b[3]), (b[0], b[3]), ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)):
        if inside(poly, x, y):
            return True
    return False

def overlaps(svg):
    """Word groups covered by a filled shape drawn after them, or touching
    another word group."""
    shapes, words = read(svg)
    bad = []
    boxes = [bbox(w['quad']) for w in words]
    for i, w in enumerate(words):
        b = _shrink(boxes[i], .5)
        c = container(shapes, w)
        c_order = c.get('order', -1)
        for s in shapes:
            if not s['filled'] or is_background(s):
                continue
            if s['order'] > w['order']:
                hit = _poly_hits_box(s['poly'], b)
            elif s['order'] <= c_order:
                continue  # under the words' own shape, hidden by it
            else:
                # a shape under the words: its edge must not cross them
                hit = any(b[0] < x < b[2] and b[1] < y < b[3] for x, y in densify(s['poly'], 1.0))
            if hit:
                bad.append(dict(order=w['order'], box=boxes[i], by='shape' if s['order'] > w['order'] else 'edge', shape=s['order']))
                break
        for j in range(i + 1, len(words)):
            o = boxes[j]
            if b[0] < o[2] - .5 and o[0] + .5 < b[2] and b[1] < o[3] - .5 and o[1] + .5 < b[3]:
                bad.append(dict(order=w['order'], box=boxes[i], by='words', other=words[j]['order']))
    return bad
