"""US English → Thai-script reading, following §9 and §10.1 of the NativeSense master prompt
and the reference file (section 1–2). Pronunciations come from the CMU Pronouncing Dictionary
(ARPAbet, US English), passed in as a file path.

Conventions (same as the reference file):
- '-' joins syllables of a word; a space separates words; **bold** = primary stress (2+ syllables).
- (x) = a final sound to say lightly that Thai letters would drop or change.
- Never ์. ไ ใ เ-า ำ and glide forms (-าว -อย -ิว) take no unbracketed final.
- The first final may be unbracketed only if Thai reads it right: ก ด ท บ พ ม น ง, and ส (house rule).
- Short-vowel mark ็ before stop finals: เ-็ (เย็ท, เท็น also before nasals), แ-็ (แบ็ก; not before nasals or ส).
"""
import re

VOWELS = {'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'}
CMU = {}

def load(path):
    with open(path, encoding='latin-1') as f:
        for line in f:
            if not line.strip() or line.startswith(';;;'):
                continue
            parts = line.split('#')[0].split()
            word = re.sub(r'\(\d+\)$', '', parts[0].lower())
            CMU.setdefault(word, []).append(parts[1:])

# ---------------------------------------------------------------- syllables
ON2 = {('P','L'),('P','R'),('B','L'),('B','R'),('T','R'),('D','R'),('K','L'),('K','R'),('G','L'),('G','R'),('F','L'),('F','R'),
       ('TH','R'),('SH','R'),('K','W'),('G','W'),('T','W'),('D','W'),('S','W'),('TH','W'),
       ('S','P'),('S','T'),('S','K'),('S','M'),('S','N'),('S','L'),('S','F')}
ON2Y = {('P','Y'),('B','Y'),('K','Y'),('G','Y'),('F','Y'),('V','Y'),('M','Y'),('N','Y'),('HH','Y')}
ON3 = {('S','P','L'),('S','P','R'),('S','T','R'),('S','K','R'),('S','K','W')}
ON3Y = {('S','K','Y'),('S','P','Y')}
LIQ = {'L', 'R', 'W'}

def legal_onset(cs, vowel):
    cs = tuple(cs)
    if not cs:
        return True
    if len(cs) == 1:
        return cs[0] != 'NG'
    yok = vowel in ('UW', 'UH')
    if len(cs) == 2:
        return cs in ON2 or (yok and cs in ON2Y)
    if len(cs) == 3:
        return cs in ON3 or (yok and cs in ON3Y)
    return False

def parse(phones):
    """['HH','AH0','L','OW1'] -> list of (sym, stress or None)"""
    out = []
    for p in phones:
        m = re.match(r'([A-Z]+)([012]?)$', p)
        sym, st = m.group(1), m.group(2)
        out.append((sym, int(st) if st else None))
    return out

def syllabify(phones):
    ph = parse(phones)
    vidx = [i for i, (s, _) in enumerate(ph) if s in VOWELS]
    if not vidx:
        raise ValueError(f'no vowel in {phones}')
    syls = []
    for n, vi in enumerate(vidx):
        syls.append({'on': [], 'v': ph[vi][0], 'st': ph[vi][1], 'co': []})
    syls[0]['on'] = [s for s, _ in ph[:vidx[0]]]
    syls[-1]['co'] = [s for s, _ in ph[vidx[-1] + 1:]]
    for n in range(len(vidx) - 1):
        cons = [s for s, _ in ph[vidx[n] + 1:vidx[n + 1]]]
        nxt_v = syls[n + 1]['v']
        if not cons:
            if syls[n]['v'] == 'ER':          # worry: W ER1 IY0 → เวอ-รี
                syls[n + 1]['on'] = ['R']
                syls[n]['er_link'] = True
            continue
        if len(cons) == 1:
            if cons[0] == 'NG':
                syls[n]['co'] = cons
            else:
                syls[n + 1]['on'] = cons
            continue
        if legal_onset(cons, nxt_v) and cons[0] != 'S' and cons[-1] in LIQ | {'Y'}:
            syls[n + 1]['on'] = cons          # apply → อะ-ไพล, secret → ซี-เคริท
            continue
        start = 0 if (syls[n + 1]['st'] == 1 and cons[0] == 'S' and legal_onset(cons, nxt_v)) else 1
        for k in range(start, len(cons) + 1):
            if legal_onset(cons[k:], nxt_v):
                syls[n]['co'], syls[n + 1]['on'] = cons[:k], cons[k:]
                break
    return syls

# ---------------------------------------------------------------- Thai letters
ONSET = {'P':'พ','B':'บ','T':'ท','D':'ด','K':'ค','G':'ก','F':'ฟ','V':'ว','TH':'ธ','DH':'ด','S':'ซ','Z':'ซ','SH':'ช','ZH':'ช',
         'CH':'ช','JH':'จ','HH':'ฮ','M':'ม','N':'น','L':'ล','R':'ร','W':'ว','Y':'ย'}
UNBR = {'P':'พ','B':'บ','T':'ท','D':'ด','K':'ก','G':'ก','M':'ม','N':'น','NG':'ง','S':'ส'}
BR = {'P':'พ','B':'บ','T':'ท','D':'ด','K':'ค','G':'ก','M':'ม','N':'น','NG':'ง','L':'ล','R':'ร','F':'ฟ','V':'ฟ','TH':'ธ','DH':'ธ',
      'S':'ส','Z':'ซ','SH':'ช','ZH':'ช','CH':'ช','JH':'จ'}
STOP_LETTERS = set('กดทบพ')

UNASP = {'P': 'ป', 'T': 'ต', 'K': 'ก'}
def onset_str(on, flap=False):
    """-> (prefix, main). A leading vowel (เ แ โ ไ) goes between them: สเต็น, สโล, สไตล."""
    if not on:
        return '', 'อ'
    if on[0] == 'S' and len(on) > 1:          # sp st sk sl sm sn sw → ส + ป ต ก ล ม น ว
        rest = [UNASP.get(on[1], ONSET[on[1]])] + [ONSET[c] for c in on[2:]]
        return 'ส', ''.join(rest)
    if on == ['T'] and flap:
        return '', 'ด'                         # US flap: water → วอ-เดอ(ร)
    return '', ''.join(ONSET[c] for c in on)

def render(s, flap=False):
    """one syllable dict -> Thai string (without bold)"""
    on, v, st, co = list(s['on']), s['v'], s['st'], list(s['co'])
    yglide = len(on) >= 2 and on[-1] == 'Y' and v in ('UW', 'UH')
    if yglide:
        on = on[:-1]
    P, C = onset_str(on, flap)
    cluster = len(on) >= 2
    # R after the vowel: changes some vowels, always bracketed
    r_coda = bool(co) and co[0] == 'R'
    takes_final = v not in ('AY', 'AW', 'OY', 'ER') and not yglide and not r_coda
    fin_letter, rest = '', co
    if co and takes_final and co[0] in UNBR:
        fin_letter, rest = UNBR[co[0]], co[1:]
    brackets = ''.join('(' + BR[c] + ')' for c in rest)
    F = fin_letter
    stop = F in STOP_LETTERS
    if yglide:
        core = C + 'ิว'
    elif v == 'IY':
        core = ('เ' + C + 'ีย') if r_coda else C + 'ี' + F
    elif v == 'IH':
        core = ('เ' + C + 'ีย') if r_coda else C + 'ิ' + F
    elif v == 'EY':
        core = 'เ' + C + F
    elif v == 'EH':
        if r_coda:
            core = 'แ' + C
        elif F and F != 'ส':
            core = 'เ' + C + '็' + F
        else:
            core = 'เ' + C + F
    elif v == 'AE':
        core = 'แ' + C + ('็' if stop else '') + F
    elif v == 'AH' and st in (1, 2):
        if F:
            core = C + 'ั' + F
        elif rest:
            core = C + 'ั'                     # much → มั(ช)
        else:
            core = C + 'ะ'                     # mother → มะ-เดอ(ร)
    elif v == 'AH':                            # schwa
        if not F and rest and co[0] in ('JH', 'CH', 'SH'):
            core = C + 'ิ'                     # damage → แด-มิ(จ), English → อิง-กลิ(ช)
        elif F == 'น':
            core = 'เ' + C + 'ิน'
        elif F:
            core = 'เ' + C + 'ิ' + F
        elif rest:
            core = 'เ' + C + 'ิ'               # little → ลิ-เดิ(ล)
        else:
            core = C + ('ิ' if cluster else 'ะ')   # about → อะ-, application → แอ-พลิ-
    elif v == 'ER':
        core = 'เ' + C + 'อ'
        if not s.get('er_link'):
            brackets = '(ร)' + brackets
    elif v == 'AA':
        core = C + 'า' + F
    elif v == 'AO':
        core = C + 'อ' + F
    elif v == 'UH':
        core = (C + 'ัว') if r_coda else C + 'ุ' + F
    elif v == 'UW':
        core = C + 'ู' + F
    elif v == 'OW':
        core = 'โ' + C + F
    elif v == 'AY':
        core = 'ไ' + C
    elif v == 'AW':
        core = C + 'าว'
    elif v == 'OY':
        core = C + 'อย'
    else:
        raise ValueError(v)
    return P + core + brackets

def word_reading(phones, bold=True):
    syls = syllabify(phones)
    parts = []
    for i, s in enumerate(syls):
        prev = syls[i - 1] if i else None
        flap = (bool(prev) and s['on'] == ['T']
                and (s['st'] == 0 or (s['st'] == 2 and prev['st'] == 1))
                and (not prev['co'] or prev['co'] == ['R'])
                and not (s['v'] == 'AH' and s['st'] == 0 and s['co'][:1] == ['N']))
        t = render(s, flap)
        if bold and len(syls) > 1 and s['st'] == 1:
            t = '**' + t + '**'
        parts.append(t)
    return '-'.join(parts)

# ---------------------------------------------------------------- sentences
WEAK = {'a': 'อะ', 'an': 'เอิน', 'of': 'เอิ(ฟ)', 'for': 'เฟอ(ร)', 'and': 'เอิน', 'at': 'เอิท', 'from': 'เฟริม', 'them': 'เดิม',
        'your': 'ยอ(ร)', 'you': 'ยู'}
OVERRIDE = {}          # word -> Thai reading (wins over everything)
MULTI = {('thank', 'you'): 'แธง-คิว'}     # fixed linked expressions
PHONES = {}            # word -> ARPAbet string (wins over CMU's first entry)
NORMAL = {'mr.': 'mister', 'mrs.': 'missus', 'dr.': 'doctor'}
VOWEL_START = re.compile(r'^[aeiou]', re.I)
ABBR = ('a.m.', 'p.m.', 'mr.', 'ms.', 'mrs.', 'dr.')

def phones_for(w):
    if w in PHONES:
        return PHONES[w].split()
    if w in CMU:
        return CMU[w][0]
    return None

def tokens(text):
    """split into (word, trailing punctuation) pairs; keeps apostrophes inside words"""
    out = []
    for raw in text.split():
        low = raw.lower().lstrip('"“(')
        abbr = next((a for a in ABBR if low.startswith(a)), None)
        if abbr:
            out.append((raw.lstrip('"“(')[:len(abbr)], raw.lstrip('"“(')[len(abbr):]))
            continue
        m = re.match(r"^([\"“(]*)(.*?)([.,!?;:\"”)…]*)$", raw)
        word, tail = m.group(2), m.group(3)
        out.append((word, tail))
    return out

def sentence(text, unknown=None):
    toks = tokens(text)
    words = [w for w, _ in toks]
    out = []
    i = 0
    while i < len(toks):
        w, tail = toks[i]
        lw = w.lower()
        lw = NORMAL.get(lw, lw)
        nxt = words[i + 1].lower() if i + 1 < len(words) else ''
        last_in_clause = (tail != '') or i + 1 == len(toks)
        if (lw, nxt) in MULTI and tail == '':
            out.append([MULTI[(lw, nxt)], toks[i + 1][1], None]); i += 2; continue
        if lw in OVERRIDE:
            r = OVERRIDE[lw]
        elif lw == 'the':
            r = 'ดิ' if nxt and VOWEL_START.match(nxt) and not nxt.startswith(('u', 'eu', 'one', 'once')) else 'เดอะ'
        elif lw == 'to' and not last_in_clause:
            r = 'ทู' if nxt and VOWEL_START.match(nxt) else 'ทะ'
        elif lw == 'can' and not last_in_clause:
            r = 'เคิน'
        elif lw == 'and' and (i == 0 or re.search(r'[.!?]', toks[i - 1][1])):
            r = 'แอน(ด)'                       # stressed at the start: And you?
        elif lw in WEAK and not last_in_clause:
            r = WEAK[lw]
        else:
            ph = phones_for(lw)
            if ph is None and '-' in lw:
                subs = [phones_for(p) for p in lw.split('-')]
                if all(subs):
                    r = '-'.join(word_reading(p) for p in subs)
                    out.append([r, tail, None]); i += 1; continue
            if ph is None:
                if unknown is not None:
                    unknown.add(w)
                r = '⟨' + w + '⟩'
                out.append([r, tail, None]); i += 1; continue
            # linking: T/D + you/your → ชู/จู (Could you → คุ-จู, meet you → มี-ชู)
            if nxt in ('you', 'your', "you're", 'yours') and tail == '' and ph[-1] in ('T', 'D'):
                ph2 = ph[:-1]
                link = 'CH' if ph[-1] == 'T' else 'JH'
                nph = phones_for(nxt)
                nph = [link] + nph[1:]
                a = word_reading(ph2)
                b = word_reading(nph)
                tail2 = toks[i + 1][1]
                out.append([a + '-' + b, tail2, None])
                i += 2
                continue
            r = word_reading(ph)
        out.append([r, tail, None])
        i += 1
    s = ''
    for r, tail, _ in out:
        tail = tail.replace('"', '').replace('“', '').replace('”', '')
        s += r + tail + ' '
    s = s.strip()
    if s.endswith('.'):
        s = s[:-1]
    s = s.replace('…', '')
    return s
