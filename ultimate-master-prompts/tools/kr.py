import re
# Pronounced Hangul -> Revised Romanization + Thai reading, following the master prompt §9 and §10.3.
CHO = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
RR_C = {'ㄱ':'g','ㄲ':'kk','ㄴ':'n','ㄷ':'d','ㄸ':'tt','ㄹ':'r','ㅁ':'m','ㅂ':'b','ㅃ':'pp','ㅅ':'s','ㅆ':'ss','ㅇ':'','ㅈ':'j','ㅉ':'jj','ㅊ':'ch','ㅋ':'k','ㅌ':'t','ㅍ':'p','ㅎ':'h'}
RR_V = {'ㅏ':'a','ㅐ':'ae','ㅑ':'ya','ㅒ':'yae','ㅓ':'eo','ㅔ':'e','ㅕ':'yeo','ㅖ':'ye','ㅗ':'o','ㅘ':'wa','ㅙ':'wae','ㅚ':'oe','ㅛ':'yo','ㅜ':'u','ㅝ':'wo','ㅞ':'we','ㅟ':'wi','ㅠ':'yu','ㅡ':'eu','ㅢ':'ui','ㅣ':'i'}
RR_F = {'':'','ㄱ':'k','ㄴ':'n','ㄷ':'t','ㄹ':'l','ㅁ':'m','ㅂ':'p','ㅇ':'ng'}
TH_F = {'ㄱ':'ก','ㄴ':'น','ㄷ':'ด','ㅁ':'ม','ㅂ':'บ','ㅇ':'ง'}          # ㄹ is written (ล)
TENSE_CLOSE = {'ㄲ':'ก','ㄸ':'ต','ㅃ':'ป','ㅉ':'ต'}
Y_VOWELS = ('ㅑ','ㅒ','ㅕ','ㅖ','ㅛ','ㅠ')

def dec(ch):
    c = ord(ch) - 0xAC00
    return CHO[c // 588], JUNG[(c % 588) // 28], JONG[c % 28]

def onset(c, v, word_initial, prev_final):
    if c in ('ㄱ','ㄷ','ㅂ','ㅈ'):
        return {'ㄱ':'คก','ㄷ':'ทด','ㅂ':'พบ','ㅈ':'ชจ'}[c][0 if word_initial else 1]
    if c == 'ㅅ':
        return 'ช' if (v == 'ㅣ' or v in Y_VOWELS or v == 'ㅟ') else 'ซ'
    if c == 'ㄹ':
        return 'ล' if prev_final == 'ㄹ' else 'ร'
    return {'ㄲ':'ก','ㄸ':'ต','ㅃ':'ป','ㅉ':'จ','ㅆ':'ซ','ㅋ':'ค','ㅌ':'ท','ㅍ':'พ','ㅊ':'ช',
            'ㄴ':'น','ㅁ':'ม','ㅎ':'ฮ','ㅇ':'อ'}[c]

# vowel -> (open form, closed form, form before (ล)); 'C' = onset, 'F' = final letter, y/w glides added below
VF = {
 'ㅏ':('Cา','CัF','Cา'),   'ㅐ':('แC','แCF','แC'),   'ㅓ':('Cอ','C็อF','Cอ'),  'ㅔ':('เC','เC็F','เC'),
 'ㅗ':('โC','CF','โC'),    'ㅜ':('Cู','CุF','Cุ'),    'ㅡ':('Cือ','CึF','Cึ'),  'ㅣ':('Cี','CิF','Cิ'),
 'ㅑ':('Yา','YัF','Yา'),   'ㅒ':('แY','แYF','แY'),   'ㅕ':('Yอ','Y็อF','Yอ'),  'ㅖ':('เY','เY็F','เY'),
 'ㅛ':('โY','YF','โY'),    'ㅠ':('Yู','YุF','Yุ'),
 'ㅘ':('Wา','WัF','Wา'),   'ㅙ':('แW','แWF','แW'),   'ㅝ':('Wอ','W็อF','Wอ'),  'ㅟ':('Wี','WิF','Wิ'),
 'ㅚ':('CเV','CเVF','CเV'),'ㅞ':('CเV','CเVF','CเV'),
}
def th_syl(C, v, f, word_initial):
    o = (C == 'อ')
    if v == 'ㅢ':
        return ('อึย' if o else C + 'ี') + TH_F.get(f, '') + ('(ล)' if f == 'ㄹ' else '')
    open_, closed_, before_l = VF[v]
    if f == 'ㄹ': form = before_l
    elif f: form = closed_
    else: form = open_
    pal = C in ('ช', 'จ') and v in Y_VOWELS   # 셔 쇼 져 쳐 쪄: the y-glide merges into ช/จ → ชอ โช จอ
    if pal or o:
        Y = 'ย' if o else C            # 여 → ยอ, 션 → ช็อน
    elif v in ('ㅛ', 'ㅖ', 'ㅒ'):
        Y = None                       # 효 → ฮโย, 계 → คเย, 걔 → คแย (consonant goes before the vowel sign)
    else:
        Y = C + 'ย'                    # 며 → มยอ, 류 → รยู
    W = 'ว' if o else C + 'ว'          # 와 → วา, 과 → ควา
    if Y is None:
        form = C + form.replace('Y', 'ย')
    else:
        form = form.replace('Y', Y)
    form = form.replace('W', W)
    if v in ('ㅚ', 'ㅞ'):
        form = ('' if o else C) + 'เว' + ('็F' if f and f != 'ㄹ' else '')   # 외 เว, 왼 เว็น (like ㅔ: 엔 เอ็น)
    else:
        form = form.replace('C', C)
    form = form.replace('F', TH_F.get(f, ''))
    return form + ('(ล)' if f == 'ㄹ' else '')

def close_prev(t, letter):
    """turn an open Thai syllable into a closed one ending in letter (before a tense consonant)"""
    if t.endswith('(ล)'): return t
    if t.startswith('โ') or t.startswith('เ') or t.startswith('แ'): return t + letter   # โอ → โอป
    if t.endswith('ือ'): return t[:-2] + 'ึ' + letter
    if t.endswith('อ'): return t[:-1] + '็อ' + letter                                  # ยอ → ย็อก
    if t.endswith('า'): return t[:-1] + 'ั' + letter
    if t.endswith('ู'): return t[:-1] + 'ุ' + letter
    if t.endswith('ี'): return t + letter                                               # ซี → ซีก
    return t + letter

def word(w):
    syls = [dec(ch) for ch in w]
    rr, th = [], []
    prev_f = None
    for i, (c, v, f) in enumerate(syls):
        # RR
        rc = RR_C[c]
        if c == 'ㄹ' and prev_f == 'ㄹ': rc = 'l'
        rr.append(rc + RR_V[v] + RR_F[f])
        # Thai
        C = onset(c, v, i == 0, prev_f)
        if c in TENSE_CLOSE and i > 0 and not prev_f and th:
            th[-1] = close_prev(th[-1], TENSE_CLOSE[c])
        th.append(th_syl(C, v, f, i == 0))
        prev_f = f
    return '-'.join(rr), '-'.join(th)

PUNCT = ',.?!'
def sentence(spec):
    """spec: pronounced Hangul with spaces between words; punctuation attached to words"""
    out_rr, out_th = [], []
    for w in spec.split():
        tail = ''
        while w and w[-1] in PUNCT: tail = w[-1] + tail; w = w[:-1]
        r, t = word(w)
        out_rr.append(r + tail); out_th.append(t + tail)
    s = ' '.join(out_rr)
    s = s[0].upper() + s[1:]
    s = re.sub(r'([.!?] )([a-z])', lambda m: m.group(1) + m.group(2).upper(), s)
    th = ' '.join(out_th)
    if th.endswith('.'): th = th[:-1]
    return {'rr': s, 'th': th}

if __name__ == '__main__':
    tests = {'감사함니다':'คัม-ซา-ฮัม-นี-ดา','한구거':'ฮัน-กู-กอ','가방':'คา-บัง','아버지':'อา-บอ-จี','오빠':'โอป-ปา',
             '시':'ชี','사랑':'ซา-รัง','서울':'ซอ-อุ(ล)','빨리':'ปา(ล)-ลี','씨께':'ซีก-เก','몰라요':'โม(ล)-ลา-โย',
             '괜차나요':'แควน-ชา-นา-โย','정말':'ช็อง-มา(ล)','지권':'ชี-กว็อน','멷씨에요':'มย็อด-ซี-เอ-โย',
             '죄송':'ชเว-ซง','의사':'อึย-ซา','히망':'ฮี-มัง','도라가':'โท-รา-กา','여꿔늘':'ย็อก-กวอ-นึ(ล)',
             '포지션':'โพ-จี-ช็อน','효':'ฮโย','시게':'ชี-เก','계':'คเย','걔':'คแย','교':'คโย','학꾜':'ฮัก-กโย',
             '명동':'มย็อง-ดง','류':'รยู','저':'ชอ','셔츠':'ชอ-ชือ','쇼':'โช','쥬스':'ชู-ซือ','요':'โย',
             '예요':'เย-โย','얘':'แย','외':'เว','웨':'เว','최':'ชเว','쉬':'ชวี','의':'อึย','희':'ฮี'}
    bad = []
    for k, v in tests.items():
        got = word(k)[1]
        if got != v: bad.append((k, got, v))
    print('checks', len(tests), 'bad', bad)
    print(word('감사함니다'), word('여꿔늘'), word('저쪼기에요'))
