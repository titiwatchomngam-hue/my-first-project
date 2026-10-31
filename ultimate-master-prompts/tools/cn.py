# Pinyin -> Thai reading engine, following the master prompt §10.4.
# Tones: 1 สามัญ, 2 จัตวา, 3 เอก, 4 โท, 5 neutral (short/light).
MAI_EK, MAI_THO, MAI_CHAT = '่', '้', '๋'

INIT = {  # pinyin initial -> (Thai letter, class, high-class pair)
 'b':('ป','mid',None),'p':('พ','pair','ผ'),'m':('ม','single',None),'f':('ฟ','pair','ฝ'),
 'd':('ต','mid',None),'t':('ท','pair','ถ'),'n':('น','single',None),'l':('ล','single',None),
 'g':('ก','mid',None),'k':('ค','pair','ข'),'h':('ฮ','pair','ห'),
 'j':('จ','mid',None),'q':('ช','pair','ฉ'),'x':('ซ','pair','ส'),
 'zh':('จ','mid',None),'ch':('ช','pair','ฉ'),'sh':('ซ','pair','ส'),'r':('ร','single',None),
 'z':('จ','mid',None),'c':('ช','pair','ฉ'),'s':('ซ','pair','ส'),
 'y':('ย','single',None),'w':('ว','single',None),'':('อ','mid',None),
}
# final -> (leading vowel, add ว to onset, vowel sign after onset, tail)
FIN = {
 'a':('',0,'','า'),'o':('',0,'','อ'),'e':('เ',0,'','อ'),'-i':('',0,'ื','อ'),'er':('เ',0,'','อ(ร)'),
 'ai':('ไ',0,'',''),'ai0':('',0,'','าย'),'ei':('เ',0,'','ย'),'ao':('',0,'','าว'),'ou':('โ',0,'','ว'),
 'an':('',0,'ั','น'),'en':('เ',0,'ิ','น'),'ang':('',0,'ั','ง'),'eng':('เ',0,'ิ','ง'),'ong':('',0,'','ง'),
 'i':('',0,'ี',''),'ia':('เ',0,'ี','ย'),'ie':('เ',0,'ี','ย'),'iao':('เ',0,'ี','ยว'),'iu':('',0,'ิ','ว'),
 'ian':('เ',0,'ี','ยน'),'in':('',0,'ิ','น'),'iang':('เ',0,'ี','ยง'),'ing':('',0,'ิ','ง'),'iong':('',0,'','ง'),
 'u':('',0,'ู',''),'ua':('',1,'','า'),'uo':('',0,'ั','ว'),'uai':('',1,'','าย'),'ui':('',0,'ุ','ย'),
 'uan':('',0,'','วน'),'un':('',0,'ุ','น'),'uang':('',0,'','วง'),
 'v':('',1,'ี',''),'ve':('เ',1,'ี','ย'),'van':('เ',1,'ี','ยน'),'vn':('',1,'ิ','น'),
 'ye0':('เ',0,'',''),'yao0':('เ',0,'','า'),'you0':('โ',0,'','ว'),
}
ZERO = {  # syllables with no consonant initial (incl. y-/w- spellings)
 'a':('','a'),'o':('','o'),'e':('','e'),'ai':('','ai0'),'ei':('','ei'),'ao':('','ao'),'ou':('','ou'),
 'an':('','an'),'en':('','en'),'ang':('','ang'),'eng':('','eng'),'er':('','er'),
 'yi':('','i'),'ya':('y','a'),'ye':('y','ye0'),'yao':('y','yao0'),'you':('y','you0'),'yan':('y','ian'),
 'yin':('','in'),'yang':('y','ang'),'ying':('','ing'),'yong':('y','ong'),
 'yu':('','v'),'yue':('y','ve'),'yuan':('y','van'),'yun':('','vn'),
 'wu':('','u'),'wa':('w','a'),'wo':('w','o'),'wai':('w','ai'),'wei':('w','ei'),'wan':('w','an'),
 'wen':('w','en'),'wang':('w','ang'),'weng':('w','eng'),
}
RETRO = ('zh','ch','sh','r')

def parse(base):
    """base pinyin without tone (ü as v) -> (initial, final key)"""
    if base in ZERO:
        return ZERO[base]
    for ini in ('zh','ch','sh','b','p','m','f','d','t','n','l','g','k','h','j','q','x','r','z','c','s'):
        if base.startswith(ini):
            fin = base[len(ini):]
            break
    else:
        raise ValueError(base)
    if ini in ('j','q','x'):
        fin = {'u':'v','ue':'ve','uan':'van','un':'vn'}.get(fin, fin)
    if ini in ('z','c','s','zh','ch','sh','r') and fin == 'i':
        fin = '-i'
    if fin not in FIN:
        raise ValueError(base)
    return ini, fin

def thai(base, tone):
    ini, fin = parse(base)
    letter, cls, high = INIT[ini]
    lead, cw, sign, tail = FIN[fin]
    t = tone
    if tone == 5:
        if fin == 'a': tail = 'ะ'
        elif fin == 'e': tail = 'อะ'
        t = 1
    mark = ''
    if t == 1:
        c = letter
    elif t == 2:
        c, mark = {'mid':(letter, MAI_CHAT), 'pair':(high, ''), 'single':('ห'+letter, '')}[cls]
    elif t == 3:
        c, mark = {'mid':(letter, MAI_EK), 'pair':(high, MAI_EK), 'single':('ห'+letter, MAI_EK)}[cls]
    elif t == 4:
        c, mark = (letter, MAI_THO) if cls == 'mid' else (letter, MAI_EK)
    if cw:
        c += 'ว'
    return lead + c + sign + mark + tail

MARKS = {'a':'āáǎà','e':'ēéěè','i':'īíǐì','o':'ōóǒò','u':'ūúǔù','ü':'ǖǘǚǜ'}
def pinyin(base, tone):
    s = base.replace('v','ü')
    if tone == 5:
        return s
    if 'a' in s: idx = s.index('a')
    elif 'e' in s: idx = s.index('e')
    elif 'ou' in s: idx = s.index('o')
    else: idx = max(i for i,ch in enumerate(s) if ch in 'iouü')
    return s[:idx] + MARKS[s[idx]][tone-1] + s[idx+1:]

def syl(tok):
    """'ni3' or 'ni3>2' (dictionary tone 3, said as 2) -> dict"""
    said = None
    if '>' in tok:
        tok, said = tok.split('>')
        said = int(said)
    base, tone = tok[:-1], int(tok[-1])
    return {'base':base, 'tone':tone, 'said':said or tone,
            'py':pinyin(base, tone), 'py_said':pinyin(base, said or tone),
            'th':thai(base, said or tone), 'retro':parse(base)[0] in RETRO}

LETTER_TH = {'A':'เอ','B':'บี','C':'ซี','D':'ดี','E':'อี','G':'จี','I':'ไอ','J':'เจ','K':'เค','O':'โอ','P':'พี',
             'Q':'คิว','T':'ที','U':'ยู','V':'วี','Y':'วาย'}
PUNCT = {',':(', ',', '), '.':('. ','. '), '?':('?','?'), '!':('!','!'), '—':(' — ',' — ')}
def sentence(spec):
    """spec: words separated by spaces, syllables by '-', punctuation as own tokens.
    e.g. 'ni3>2 hao3 , hen3 gao1-xing4 ren4-shi5 ni3 .'"""
    py_words, th_words, changes, retro = [], [], [], []
    out_py, out_th = '', ''
    for w in spec.split():
        if w in PUNCT:
            out_py = out_py.rstrip() + PUNCT[w][0]
            out_th = out_th.rstrip() + PUNCT[w][1]
            continue
        if w.isdigit():
            out_py += w + ' '; out_th += w + ' '; continue
        if w.isupper():                       # Latin letters said as letter names: GG → จี-จี
            out_py += w + ' '; out_th += '-'.join(LETTER_TH[ch] for ch in w) + ' '; continue
        ss = [syl(x) for x in w.split('-')]
        p = ''
        for i, s in enumerate(ss):
            piece = s['py']
            if i and piece[0] in 'aeoāáǎàēéěèōóǒò':
                piece = "'" + piece
            p += piece
        out_py += p + ' '
        out_th += '-'.join(s['th'] for s in ss) + ' '
        for s in ss:
            if s['said'] != s['tone']:
                changes.append(f"{s['py']} → {s['py_said']}")
            if s['retro'] and s['py'] not in retro:
                retro.append(s['py'])
    out_py = out_py.strip()
    out_py = out_py[0].upper() + out_py[1:]
    import re
    out_py = re.sub(r'([.!?] )([a-zāáǎàēéěèīíǐìōóǒòūúǔù])', lambda m: m.group(1) + m.group(2).upper(), out_py)
    th = out_th.strip()
    if th.endswith('.'): th = th[:-1]
    out_py = out_py.strip()
    return {'py': out_py, 'th': th, 'changes': changes, 'retro': retro}

if __name__ == '__main__':
    tests = {'ma1':'มา','ma2':'หมา','ma3':'หม่า','ma4':'ม่า','ma5':'มะ','ren2':'เหริน','lai2':'ไหล','wo3':'หว่อ',
             'ni3':'หนี่','ni2':'หนี','hao3':'ห่าว','xie4':'เซี่ย','xie5':'เซีย','zai4':'ไจ้','jian4':'เจี้ยน',
             'zhong1':'จง','guo2':'กั๋ว','lao3':'หล่าว','shi4':'ซื่อ','si4':'ซื่อ','ai4':'อ้าย','xue2':'เสวีย',
             'yu2':'อวี๋','qu4':'ชวี่','nv3':'หนวี่','kuai4':'คว่าย','dui4':'ตุ้ย','liu4':'ลิ่ว','xiang3':'เสี่ยง',
             'qing3':'ฉิ่ง','ming2':'หมิง','de5':'เตอะ','zuo4':'จั้ว','ren4':'เริ่น','you3':'โหย่ว','yao4':'เย่า',
             'ye3':'เหย่','yue4':'เยวี่ย','yuan2':'เหยวียน','yun2':'อวิ๋น','jun1':'จวิน','xun2':'สวิน','wai4':'ไว่',
             'wei4':'เว่ย','wen4':'เวิ่น','wang2':'หวัง','er4':'เอ้อ(ร)','hui2':'หุย','hui4':'ฮุ่ย','cuo4':'ชั่ว',
             'guan1':'กวน','huang2':'หวง','cong2':'ฉง','shei2':'เสย','fan4':'ฟั่น','dian3':'เตี่ยน','cai2':'ไฉ'}
    bad = [(k, thai(k[:-1], int(k[-1])), v) for k, v in tests.items() if thai(k[:-1], int(k[-1])) != v]
    print('engine checks:', len(tests), 'bad:', bad)
