import re
# Kana -> Hepburn + Thai reading engine, following the master prompt §9 and §10.2.
BASE = {
 'あ':('','a'),'い':('','i'),'う':('','u'),'え':('','e'),'お':('','o'),
 'か':('k','a'),'き':('k','i'),'く':('k','u'),'け':('k','e'),'こ':('k','o'),
 'が':('g','a'),'ぎ':('g','i'),'ぐ':('g','u'),'げ':('g','e'),'ご':('g','o'),
 'さ':('s','a'),'し':('sh','i'),'す':('s','u'),'せ':('s','e'),'そ':('s','o'),
 'ざ':('z','a'),'じ':('j','i'),'ず':('z','u'),'ぜ':('z','e'),'ぞ':('z','o'),
 'た':('t','a'),'ち':('ch','i'),'つ':('ts','u'),'て':('t','e'),'と':('t','o'),
 'だ':('d','a'),'ぢ':('j','i'),'づ':('z','u'),'で':('d','e'),'ど':('d','o'),
 'な':('n','a'),'に':('n','i'),'ぬ':('n','u'),'ね':('n','e'),'の':('n','o'),
 'は':('h','a'),'ひ':('h','i'),'ふ':('f','u'),'へ':('h','e'),'ほ':('h','o'),
 'ば':('b','a'),'び':('b','i'),'ぶ':('b','u'),'べ':('b','e'),'ぼ':('b','o'),
 'ぱ':('p','a'),'ぴ':('p','i'),'ぷ':('p','u'),'ぺ':('p','e'),'ぽ':('p','o'),
 'ま':('m','a'),'み':('m','i'),'む':('m','u'),'め':('m','e'),'も':('m','o'),
 'や':('y','a'),'ゆ':('y','u'),'よ':('y','o'),
 'ら':('r','a'),'り':('r','i'),'る':('r','u'),'れ':('r','e'),'ろ':('r','o'),
 'わ':('w','a'),'を':('','o'),'ゔ':('v','u'),
}
YOON = {'k':'ky','g':'gy','n':'ny','h':'hy','m':'my','r':'ry','b':'by','p':'py','sh':'sh','ch':'ch','j':'j'}
SMALL_Y = {'ゃ':'a','ゅ':'u','ょ':'o'}
SMALL_V = {'ぁ':'a','ぃ':'i','ぅ':'u','ぇ':'e','ぉ':'o'}
# Thai onset letters: (start of word, inside word)
TH = {'':('อ','อ'),'k':('ค','ก'),'g':('ก','ก'),'s':('ซ','ซ'),'sh':('ช','ช'),'z':('ซ','ซ'),'j':('จ','จ'),
      't':('ท','ต'),'ch':('ช','จ'),'ts':('ส','ส'),'d':('ด','ด'),'n':('น','น'),'h':('ฮ','ฮ'),'f':('ฟ','ฟ'),
      'b':('บ','บ'),'p':('พ','ป'),'m':('ม','ม'),'y':('ย','ย'),'r':('ร','ร'),'w':('ว','ว'),'v':('ว','ว'),
      'ky':('ค','ก'),'gy':('ก','ก'),'ny':('น','น'),'hy':('ฮ','ฮ'),'my':('ม','ม'),'ry':('ร','ร'),'by':('บ','บ'),'py':('พ','ป')}
# ん before ...: letter
def n_final(next_cons):
    if next_cons is None: return 'ง'                 # end of word
    if next_cons in ('m','b','p','my','by','py'): return 'ม'
    if next_cons in ('k','g','ky','gy'): return 'ง'
    return 'น'                                        # t d n r s z ch j ts sh, vowels, y, w, h, f
def q_final(next_cons):                               # っ before ...: letter
    if next_cons in ('k','g','ky','gy'): return 'ก'
    if next_cons in ('p','b','py','by','f'): return 'ป'
    if next_cons in ('s','sh','z','j'): return 'ส'
    return 'ต'                                        # t ch ts d

def to_hira(s):
    return ''.join(chr(ord(c)-0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)

def morae(word):
    """kana word -> list of mora dicts"""
    h = to_hira(word)
    out, i = [], 0
    while i < len(h):
        c = h[i]
        nxt = h[i+1] if i+1 < len(h) else ''
        if c == 'ん': out.append({'t':'N'}); i += 1; continue
        if c == 'っ': out.append({'t':'Q'}); i += 1; continue
        if c == 'ー': out.append({'t':'L'}); i += 1; continue
        if c not in BASE: raise ValueError(f'unknown kana {c!r} in {word}')
        cons, v = BASE[c]
        if nxt in SMALL_Y and cons in YOON and v == 'i':
            out.append({'t':'M','c':YOON[cons],'v':SMALL_Y[nxt]}); i += 2; continue
        if nxt in SMALL_V:
            cc = {'':'w'}.get(cons, cons) if c in 'うゔ' else cons
            if c == 'う': cc = 'w'
            out.append({'t':'M','c':cc,'v':SMALL_V[nxt]}); i += 2; continue
        out.append({'t':'M','c':cons,'v':v}); i += 1
    return out

LONG_PAIRS = {('a','a'),('u','u'),('o','u'),('o','o'),('e','e'),('i','i'),('e','i')}
MACRON = {'a':'ā','u':'ū','o':'ō','e':'ē','i':'ī'}

SPECIAL = {'こんにちは':('konnichiwa','คน-นิ-จิ-วะ'), 'こんばんは':('konbanwa','คม-บัง-วะ')}
def word_reading(word, particle=False):
    if word in SPECIAL: return SPECIAL[word]
    ms = morae(word)
    # --- build syllables
    syls = []
    for k, m in enumerate(ms):
        nxt = next((x for x in ms[k+1:] if x['t'] == 'M'), None)
        nxt_c = nxt['c'] if nxt and ms[k+1]['t'] == 'M' else (None if k+1 >= len(ms) else (nxt['c'] if nxt else None))
        if m['t'] == 'M':
            prev = syls[-1] if syls else None
            if prev and m['c'] == '' and not prev.get('fin') and (prev['v'], m['v']) in LONG_PAIRS and not prev.get('long') and not prev.get('diph'):
                prev['long'] = True; prev['long_kind'] = prev['v'] + m['v']; continue
            if prev and m['c'] == '' and m['v'] == 'i' and prev['v'] == 'a' and not prev.get('fin') and not prev.get('long') and not prev.get('diph'):
                prev['diph'] = True; continue
            # です / ます: whispered final u
            if m['c'] == 's' and m['v'] == 'u' and k == len(ms)-1 and prev and not prev.get('fin') \
               and ((prev['c'], prev['v']) in (('d','e'), ('m','a'))):
                prev['fin'] = 'ส'; prev['fin_kind'] = 'dev'; prev['dev'] = True; continue
            if m['c'] == 'ts' and prev and not prev.get('fin') and not prev.get('long') and not prev.get('diph'):
                prev['fin'] = 'ต'; prev['fin_kind'] = 'q'; prev['tsu_close'] = True
            syls.append({'c':m['c'], 'v':m['v']})
        elif m['t'] == 'N':
            following = ms[k+1] if k+1 < len(ms) else None
            fc = following['c'] if following and following['t'] == 'M' else None
            if following is None: fc = None
            syls[-1]['fin'] = n_final(fc if following else None) if following is None or following['t'] == 'M' else 'ง'
            syls[-1]['fin_kind'] = 'n'
            syls[-1]['n_before_vowel'] = bool(following and following['t'] == 'M' and following['c'] in ('', 'y'))
        elif m['t'] == 'Q':
            following = ms[k+1]
            syls[-1]['fin'] = q_final(following['c']); syls[-1]['fin_kind'] = 'q'
            syls[-1]['q_next'] = following['c']
        elif m['t'] == 'L':
            syls[-1]['long'] = True; syls[-1]['long_kind'] = 'bar'
    # --- Thai
    th = []
    for idx, s in enumerate(syls):
        initial = (idx == 0 and not particle)
        C = TH[s['c']][0 if initial else 1]
        v, fin, long_ = s['v'], s.get('fin'), s.get('long')
        yk = s['c'] in ('ky','gy','ny','hy','my','ry','by','py')
        if s.get('diph'):
            t = 'ไ' + C + (('(' + fin + ')') if fin else '')
        elif s['c'] == 'ts' and v == 'u':
            t = 'สึ' + (fin or '')
        elif yk:
            t = {'a': ('เ'+C+'ีย' if long_ else 'เ'+C+'ียะ') if not fin else 'เ'+C+'ีย'+fin,
                 'u': C+'ิว' + (fin or ''),
                 'o': 'เ'+C+'ียว' + (fin or '')}[v]
        elif v == 'a':
            t = C+'ั'+fin if fin else (C+'า' if long_ else C+'ะ')
        elif v == 'i':
            t = C+'ิ'+fin if fin else (C+'ี' if long_ else C+'ิ')
        elif v == 'u':
            t = C+'ุ'+fin if fin else (C+'ู' if long_ else C+'ุ')
        elif v == 'e':
            if fin and s.get('fin_kind') == 'dev': t = 'เ'+C+fin           # です → เดส
            elif fin: t = 'เ'+C+'็'+fin
            else: t = 'เ'+C if long_ else 'เ'+C+'ะ'
        elif v == 'o':
            if fin and s.get('fin_kind') == 'q': t = C+'็อ'+fin
            elif fin: t = C+fin
            else: t = 'โ'+C if long_ else 'โ'+C+'ะ'
        th.append(t)
    # --- Hepburn
    ro = ''
    for k, s in enumerate(syls):
        piece = s['c'] + s['v']
        if s.get('long'):
            lk = s.get('long_kind')
            if lk == 'ii': piece = s['c'] + 'ii'
            elif lk == 'ei': piece = s['c'] + 'ei'
            else: piece = s['c'] + MACRON[s['v']]
        if s.get('diph'): piece += 'i'
        if s.get('dev'): piece += 'su'
        if s.get('fin_kind') == 'n':
            piece += "n'" if s.get('n_before_vowel') else 'n'
        if s.get('fin_kind') == 'q' and not s.get('tsu_close'):
            nc = s['q_next']
            piece += 't' if nc == 'ch' else nc[0]
        ro += piece
    if particle:
        ro = {'ha':'wa','he':'e','o':'o'}.get(ro, ro)
        if word in ('は',): th = ['วะ']
        if word in ('へ',): th = ['เอะ']
    return ro, '-'.join(th)

PUNCT = {'、':(', ',', '),'。':('. ','. '),'！':('! ','! '),'？':('? ','? '),'…':('… ','… ')}
def sentence(spec):
    """spec: kana words separated by spaces; particles prefixed with ~; punctuation as tokens."""
    ro, th = '', ''
    for w in spec.split():
        if w in PUNCT:
            ro = ro.rstrip() + PUNCT[w][0]; th = th.rstrip() + PUNCT[w][1]; continue
        part = w.startswith('~')
        r, t = word_reading(w.lstrip('~'), particle=part)
        ro += r + ' '; th += t + ' '
    ro = ro.strip(); th = th.strip()
    if th.endswith('.'): th = th[:-1]
    ro = ro[0].upper() + ro[1:]
    ro = re.sub(r'([.!?] )([a-zāīūēō])', lambda m: m.group(1) + m.group(2).upper(), ro)
    return {'ro': ro, 'th': th}

if __name__ == '__main__':
    tests = {'きょう':('kyō','เคียว'),'ひま':('hima','ฮิ-มะ'),'おばさん':('obasan','โอะ-บะ-ซัง'),
             'おばあさん':('obāsan','โอะ-บา-ซัง'),'ビル':('biru','บิ-รุ'),'ビール':('bīru','บี-รุ'),
             'きって':('kitte','คิต-เตะ'),'ちょっと':('chotto','ช็อต-โตะ'),'がっこう':('gakkō','กัก-โก'),
             'です':('desu','เดส'),'ます':('masu','มัส'),'さんぽ':('sanpo','ซัม-โปะ'),'りんご':('ringo','ริง-โกะ'),
             'ほんとう':('hontō','ฮน-โต'),'にほん':('nihon','นิ-ฮง'),'たかい':('takai','ทะ-ไก'),
             'こんにちは':('konnichiwa','คน-นิ-จิ-วะ'),'せんせい':('sensei','เซ็น-เซ'),
             'おいしい':('oishii','โอะ-อิ-ชี'),'きいて':('kiite','คี-เตะ'),'わからないんだ':('wakaranainda','วะ-กะ-ระ-ไน(น)-ดะ'),'まつり':('matsuri','มัต-สึ-ริ'),'あつい':('atsui','อัต-สึ-อิ'),'ずつ':('zutsu','ซุต-สึ'),'ついて':('tsuite','สึ-อิ-เตะ'),
             'チーム':('chīmu','ชี-มุ'),'サポート':('sapōto','ซะ-โป-โตะ'),'おねえさん':('onēsan','โอะ-เน-ซัง')}
    for k, (r, t) in tests.items():
        rr, tt = word_reading(k)
        flag = '' if (rr, tt) == (r, t) else '   <-- expected %s / %s' % (r, t)
        print(f'{k:10} {rr:14} {tt}{flag}')
