U = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
     'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
T = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
ORD = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10}


def words_to_int(s):
    ws = s.replace('-', ' ').replace('_', ' ').split()
    if not ws:
        return None
    total, cur = 0, 0
    for w in ws:
        if w == 'and':
            continue
        if w in U:
            cur += U[w]
        elif w in T:
            cur += T[w]
        elif w == 'hundred':
            cur = (cur or 1) * 100
        elif w == 'thousand':
            total += (cur or 1) * 1000; cur = 0
        else:
            return None
    return total + cur


def int_to_words(n):
    if n == 0:
        return 'zero'
    out = []
    if n >= 1000:
        out.append(int_to_words(n // 1000) + ' thousand'); n %= 1000
    if n >= 100:
        out.append([k for k, v in U.items() if v == n // 100][0] + ' hundred'); n %= 100
        if n:
            out.append('and')
    if n >= 20:
        t = [k for k, v in T.items() if v == n // 10 * 10][0]
        out.append(t + (' ' + [k for k, v in U.items() if v == n % 10][0] if n % 10 else ''))
    elif n:
        out.append([k for k, v in U.items() if v == n][0])
    return ' '.join(out)
