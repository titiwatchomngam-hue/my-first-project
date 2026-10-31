"""Assemble NativeSense-Polyglot-Reference.txt from the static text and the reading engines."""
import json, re, sys
import jp, kr, cn
import ref_text as T
from jp_tables import both as jp_both
from gen import build as build_phrases

out = []
def w(s=''):
    out.append(s)

# ---------------------------------------------------------------- header, 1, 2
w(T.HEADER); w(T.SEC1); w(T.SEC2)

# ---------------------------------------------------------------- 3 Japanese
w('# 3. Japanese\n')
w('## 3.1 Line format and kana table\n')
ex = jp.sentence('きょう ~は ひま ？')
w(f"- Line: `🔊 kana · Hepburn · Thai`, e.g. `🔊 きょうは ひま？ · {ex['ro']} · {ex['th']}`.")
w('- Hepburn: macrons for long a, u, o, and ee (Tōkyō, kūkō, onēsan) and for every katakana ー (chīmu, sapōto); ii and ei stay as written (oishii, kiite, sensei, yotei).')
w('- Each cell: kana · Hepburn · Thai. Where two Thai forms are given, the first is for the start of a word and the second for inside a word.\n')
ROWS = [('','あいうえお'),('k','かきくけこ'),('g','がぎぐげご'),('s','さしすせそ'),('z','ざじずぜぞ'),('t','たちつてと'),('d','だぢづでど'),
        ('n','なにぬねの'),('h','はひふへほ'),('b','ばびぶべぼ'),('p','ぱぴぷぺぽ'),('m','まみむめも'),('y','や-ゆ-よ'),('r','らりるれろ'),('w','わ---を')]
def jcell(k):
    if k == '-': return ''
    r, s, ins = jp_both(k)
    return f"{k} {r} {s}" + (f" / {ins}" if ins != s else '')
w('| | -a | -i | -u | -e | -o |')
w('|---|---|---|---|---|---|')
for lab, row in ROWS:
    w(f"| {lab or '(vowel)'} | " + ' | '.join(jcell(k) for k in row) + ' |')
w('\nん: see 3.2 (ม / ง / น). を is the particle o: โอะ.\n')
w('### Combined kana (ゃ ゅ ょ)\n')
w('| | -ya | -yu | -yo |'); w('|---|---|---|---|')
for row in [('ky','きゃきゅきょ'),('gy','ぎゃぎゅぎょ'),('sh','しゃしゅしょ'),('j','じゃじゅじょ'),('ch','ちゃちゅちょ'),('ny','にゃにゅにょ'),
            ('hy','ひゃひゅひょ'),('by','びゃびゅびょ'),('py','ぴゃぴゅぴょ'),('my','みゃみゅみょ'),('ry','りゃりゅりょ')]:
    ks = [row[1][i:i+2] for i in (0, 2, 4)]
    w(f"| {row[0]} | " + ' | '.join(jcell(k) for k in ks) + ' |')
w('\n### Katakana for foreign sounds\n')
w(' · '.join(jcell(k) for k in ['ファ','フィ','フェ','フォ','ティ','ディ','トゥ','ドゥ','ウィ','ウェ','ウォ','ヴァ','ヴィ','シェ','ジェ','チェ','ツァ']))
w('')
w(T.JP_RULES)

def jp_row(word, kana, meaning):
    r, s = jp.word_reading(kana)
    return f"| {word} | {kana} | {r} | {s} | {meaning} |"
def jp_srow(text, spec, meaning):
    x = jp.sentence(spec)
    kana = kana_line(spec)
    return f"| {text} | {kana} | {x['ro']} | {x['th']} | {meaning} |"
def kana_line(spec):
    s = ''
    for tok in spec.split():
        if tok in ('、','。','！','？'):
            s = s.rstrip() + tok
        elif tok.startswith('~'):
            s = s.rstrip() + tok[1:] + ' '
        else:
            s += tok + ' '
    return s.strip()

w('## 3.3 Words (checked)\n')
w('| Word | Kana | Hepburn | Thai | Meaning |'); w('|---|---|---|---|---|')
JP_WORDS = [('学校','がっこう','โรงเรียน'),('学生','がくせい','นักเรียน, นักศึกษา'),('留学生','りゅうがくせい','นักเรียนต่างชาติ'),('先生','せんせい','ครู, อาจารย์, หมอ'),
 ('校長','こうちょう','ผู้อำนวยการโรงเรียน'),('担任','たんにん','ครูประจำชั้น'),('保護者','ほごしゃ','ผู้ปกครอง'),('パスポート','パスポート','พาสปอร์ต'),('ビザ','ビザ','วีซ่า'),
 ('書類','しょるい','เอกสาร'),('申請書','しんせいしょ','ใบคำร้อง'),('証明写真','しょうめいしゃしん','รูปติดบัตร'),('コピー','コピー','สำเนา'),('署名','しょめい','ลายเซ็น'),
 ('予約','よやく','การจอง, นัดหมาย'),('面接','めんせつ','สัมภาษณ์'),('大使館','たいしかん','สถานทูต'),('締め切り','しめきり','กำหนดส่ง'),('提出','ていしゅつ','การยื่น, ส่ง'),
 ('手数料','てすうりょう','ค่าธรรมเนียม'),('領収書','りょうしゅうしょ','ใบเสร็จ'),('お手洗い','おてあらい','ห้องน้ำ (สุภาพ)'),('待合室','まちあいしつ','ห้องรอ'),
 ('ガチャ','ガチャ','กาชา'),('課金','かきん','เติมเงิน'),('天井','てんじょう','การันตี (แปลตรงตัว: เพดาน)'),('回復','かいふく','ฮีล, ฟื้นฟู'),('キャリー','キャリー','แบก'),
 ('ドンマイ','ドンマイ','ไม่เป็นไรนะ (จาก don\'t mind)'),('ランクマッチ','ランクマッチ','แรงก์'),('イベント','イベント','อีเวนต์'),('アップデート','アップデート','อัปเดต')]
for a in JP_WORDS: w(jp_row(*a))
w('| 回線落ち | かいせん おち | ' + jp.sentence('かいせん おち')['ro'].lower() + ' | ' + jp.sentence('かいせん おち')['th'] + ' | เน็ตหลุด |')
w('\n### Set phrases\n')
w('| Phrase | Kana | Hepburn | Thai | Use |'); w('|---|---|---|---|---|')
for a in [('お疲れ様です。','おつかれさま です 。','ทักเพื่อนร่วมงาน (เหนื่อยหน่อยนะ)'),('失礼します。','しつれい します 。','ขออนุญาต (เข้า-ออกห้อง, วางสาย)'),
          ('少々お待ちください。','しょうしょう おまち ください 。','กรุณารอสักครู่ (สุภาพ)'),('こちらへどうぞ。','こちら ~へ どうぞ 。','เชิญทางนี้'),
          ('お世話になっております。','おせわ ~に なって おります 。','ประโยคเปิดอีเมลธุรกิจ'),('よろしくお願いいたします。','よろしく おねがい いたします 。','ฝากด้วยนะครับ/คะ (สุภาพมาก)'),
          ('かしこまりました。','かしこまりました 。','รับทราบ (กับลูกค้า)'),('承知しました。','しょうち しました 。','รับทราบ (กับหัวหน้า)')]:
    w(jp_srow(*a))
w('\n## 3.4 Established Thai names vs readings\n')
w('In Thai text, use the established Thai spelling; the 🔊 line still follows the rules above.\n')
w('| Name | Thai text | 🔊 reading |'); w('|---|---|---|')
for name, kana, thai in [('東京','とうきょう','โตเกียว'),('大阪','おおさか','โอซากะ'),('京都','きょうと','เกียวโต'),('北海道','ほっかいどう','ฮอกไกโด'),('沖縄','おきなわ','โอกินาวะ')]:
    r, s = jp.word_reading(kana)
    w(f"| {name} | {thai} | {kana} · {r[0].upper() + r[1:]} · {s} |")
w('')

# ---------------------------------------------------------------- 4 Korean
w(T.KR_HEAD)
w('## 4.3 Vowels: open syllable · closed syllable (with ㄴ) · before a final ㄹ\n')
def syl(c, v, f=''):
    return chr(0xAC00 + kr.CHO.index(c)*588 + kr.JUNG.index(v)*28 + kr.JONG.index(f))
w('| Vowel | Romanization | Alone | Closed | Before (ล) | With ㄱ at the start of a word | With ㅎ |')
w('|---|---|---|---|---|---|---|')
for v in ['ㅏ','ㅓ','ㅗ','ㅜ','ㅡ','ㅣ','ㅐ','ㅔ','ㅑ','ㅕ','ㅛ','ㅠ','ㅒ','ㅖ','ㅘ','ㅙ','ㅚ','ㅝ','ㅞ','ㅟ','ㅢ']:
    a, b, c, g, h = syl('ㅇ', v), syl('ㅇ', v, 'ㄴ'), syl('ㅇ', v, 'ㄹ'), syl('ㄱ', v), syl('ㅎ', v)
    if v == 'ㅢ':
        w(f"| ㅢ | ui | 의 อึย | — | — | 긔 คี (said [기]) | 희 ฮี (said [히]) |")
        continue
    w(f"| {v} | {kr.RR_V[v]} | {a} {kr.word(a)[1]} | {b} {kr.word(b)[1]} | {c} {kr.word(c)[1]} | {g} {kr.word(g)[1]} | {h} {kr.word(h)[1]} |")
w('\n- Closed ㅓ, ㅔ, ㅕ, ㅝ, ㅖ, ㅚ, ㅞ take ็ (อ็อน · เอ็น · ย็อน · ว็อน); closed ㅗ is written without a vowel sign (온 อน · 송 ซง).')
w('- Before (ล), ㅜ ㅠ ㅡ ㅣ ㅟ are written short (울 อุ(ล) · 율 ยุ(ล) · 을 อึ(ล) · 일 อิ(ล) · 윌 วิ(ล)); the others keep the open form (알 อา(ล) · 얼 ออ(ล) · 올 โอ(ล)).\n')

def kr_line(written, pron):
    r = kr.sentence(pron)
    show = re.sub(r'[^가-힣]', '', pron) != re.sub(r'[^가-힣]', '', written)
    rr = r['rr']
    if not re.search(r'[.!?]$', written): rr = rr[0].lower() + rr[1:]
    return (f"[{pron}]" if show else '—'), rr, r['th']

w('## 4.4 Sound changes (checked examples)\n')
w('| Change | Written | Said | Romanization | Thai |'); w('|---|---|---|---|---|')
CH = [('연음 liaison','한국어','한구거'),('연음 liaison','음악','으막'),('연음 liaison','있어요','이써요'),('연음 liaison','읽어요','일거요'),('연음 liaison','앉으세요','안즈세요'),('연음 liaison','맛있어요','마시써요'),
 ('비음화 nasalization','감사합니다','감사함니다'),('비음화 nasalization','국물','궁물'),('비음화 nasalization','작년','장년'),('비음화 nasalization','한국말','한궁말'),('비음화 nasalization','있는','인는'),('비음화 nasalization','먹는','멍는'),('비음화 nasalization','정류장','정뉴장'),('비음화 nasalization','독립','동닙'),
 ('유음화 ㄴ+ㄹ → ㄹㄹ','연락','열락'),('유음화 ㄴ+ㄹ → ㄹㄹ','신라','실라'),('유음화 ㄴ+ㄹ → ㄹㄹ','설날','설랄'),('유음화 ㄴ+ㄹ → ㄹㄹ','한류','할류'),
 ('경음화 tensing','학교','학꾜'),('경음화 tensing','식당','식땅'),('경음화 tensing','학생','학쌩'),('경음화 tensing','잡지','잡찌'),('경음화 tensing','할게요','할께요'),('경음화 tensing','여권','여꿘'),('경음화 tensing','문법','문뻡'),('경음화 tensing','갈 거예요','갈 꺼에요'),
 ('격음화 aspiration','축하해요','추카해요'),('격음화 aspiration','좋다','조타'),('격음화 aspiration','입학','이팍'),('격음화 aspiration','못해요','모태요'),('격음화 aspiration','많다','만타'),
 ('ㅎ 탈락 silent ㅎ','좋아요','조아요'),('ㅎ 탈락 silent ㅎ','괜찮아요','괜차나요'),('ㅎ 탈락 silent ㅎ','많이','마니'),('ㅎ 탈락 silent ㅎ','싫어요','시러요'),
 ('구개음화 palatalization','같이','가치'),('구개음화 palatalization','굳이','구지'),
 ('7 final sounds','꽃','꼳'),('7 final sounds','앞','압'),('7 final sounds','부엌','부억'),('7 final sounds','옷','옫'),('7 final sounds','있다','읻따'),
 ('겹받침 double finals','앉다','안따'),('겹받침 double finals','닭','닥'),('겹받침 double finals','읽다','익따'),('겹받침 double finals','읽고','일꼬'),('겹받침 double finals','삶','삼'),('겹받침 double finals','여덟','여덜'),('겹받침 double finals','밟다','밥따'),('겹받침 double finals','없다','업따'),('겹받침 double finals','값','갑'),('겹받침 double finals','싫다','실타'),
 ('ㄴ 첨가 n insertion','할 일','할릴'),('ㄴ 첨가 n insertion','무슨 일','무슨닐'),('ㄴ 첨가 n insertion','꽃잎','꼰닙'),('ㄴ 첨가 n insertion','색연필','생년필')]
for cat, wr, pr in CH:
    br, rr, th = kr_line(wr, pr)
    w(f"| {cat} | {wr} | {br} | {rr} | {th} |")
w('\n- Double finals: ㄳ→ㄱ, ㄵ→ㄴ, ㄶ→ㄴ, ㄺ→ㄱ (but ㄹ before ㄱ: 읽고 [일꼬]), ㄻ→ㅁ, ㄼ→ㄹ (but 밟다 [밥따]), ㄽ ㄾ ㅀ→ㄹ, ㄿ→ㅂ, ㅄ→ㅂ. When a vowel follows, the second letter moves over (앉으세요 [안즈세요], 읽어요 [일거요]).\n')
w(T.KR_CHOICES)
w('## 4.6 Words and set phrases (checked)\n')
w('| Word | Said | Romanization | Thai | Meaning |'); w('|---|---|---|---|---|')
KR_WORDS = [('학교','학꾜','โรงเรียน'),('학생','학쌩','นักเรียน'),('유학생','유학쌩','นักเรียนต่างชาติ'),('선생님','선생님','ครู'),('교장 선생님','교장 선생님','ผู้อำนวยการโรงเรียน'),('담임 선생님','다밈 선생님','ครูประจำชั้น'),('학부모','학뿌모','ผู้ปกครอง'),
 ('여권','여꿘','พาสปอร์ต'),('비자','비자','วีซ่า'),('서류','서류','เอกสาร'),('신청서','신청서','ใบคำร้อง'),('증명사진','증명사진','รูปติดบัตร'),('사본','사본','สำเนา'),('서명','서명','ลายเซ็น'),('예약','예약','การจอง, นัดหมาย'),('면접','면접','สัมภาษณ์'),('대사관','대사관','สถานทูต'),('마감','마감','กำหนดส่ง'),('제출','제출','การยื่น, ส่ง'),('수수료','수수료','ค่าธรรมเนียม'),('영수증','영수증','ใบเสร็จ'),('화장실','화장실','ห้องน้ำ'),('대기실','대기실','ห้องรอ'),
 ('캐리','캐리','แบก'),('힐','힐','ฮีล'),('탱커','탱커','แทงก์'),('서포터','서포터','ซัพพอร์ต'),('정글','정글','ป่า (เกม MOBA)'),('원딜','원딜','สายยิง (ADC)'),('렉','렉','แลค'),('뉴비','뉴비','มือใหม่'),('현질','현질','เติมเงิน'),('천장','천장','การันตี (แปลตรงตัว: เพดาน)'),('상향','상향','บัฟ'),('하향','하향','เนิร์ฟ'),
 ('수고하셨습니다.','수고하셛씀니다.','เหนื่อยหน่อยนะครับ/คะ (หลังงานเสร็จ)'),('잠시만 기다려 주세요.','잠시만 기다려 주세요.','กรุณารอสักครู่'),('이쪽으로 오세요.','이쪼그로 오세요.','เชิญทางนี้'),('알겠습니다.','알겓씀니다.','รับทราบครับ/ค่ะ'),('실례합니다.','실례함니다.','ขออนุญาต, ขอโทษนะครับ/คะ'),('죄송합니다.','죄송함니다.','ขอโทษครับ/ค่ะ (สุภาพ)'),('잘 부탁드립니다.','잘 부탁뜨림니다.','ฝากเนื้อฝากตัวด้วยครับ/ค่ะ')]
for wr, pr, m in KR_WORDS:
    br, rr, th = kr_line(wr, pr)
    w(f"| {wr} | {br} | {rr} | {th} | {m} |")
w('\n## 4.7 Established Thai names vs readings\n')
w('In Thai text, use the established Thai spelling; the 🔊 line still follows the rules (official romanization for the name itself).\n')
w('| Name | Official romanization | Thai text | 🔊 Thai reading |'); w('|---|---|---|---|')
for name, rom, thai in [('서울','Seoul','โซล'),('부산','Busan','ปูซาน'),('인천','Incheon','อินช็อน'),('제주','Jeju','เชจู'),('대구','Daegu','แทกู')]:
    w(f"| {name} | {rom} | {thai} | {kr.word(name)[1]} |")
w('')

# ---------------------------------------------------------------- 5 Chinese
w(T.CN_HEAD)
w('## 5.3 Initials\n')
w('| Pinyin | Thai letter | Class | 1st · 2nd · 3rd · 4th · neutral |'); w('|---|---|---|---|')
for ini, s in [('b','ba'),('p','pa'),('m','ma'),('f','fa'),('d','da'),('t','ta'),('n','na'),('l','la'),('g','ge'),('k','ke'),('h','he'),
               ('j','ji'),('q','qi'),('x','xi'),('zh','zhi'),('ch','chi'),('sh','shi'),('r','ri'),('z','zi'),('c','ci'),('s','si'),('y','ya'),('w','wa'),('','a')]:
    letter, cls, high = cn.INIT[ini]
    cname = {'mid': 'mid', 'pair': f'paired low (high partner {high})', 'single': 'single low'}[cls]
    tones = ' · '.join(f"{cn.pinyin(s, t)} {cn.thai(s, t)}" for t in (1, 2, 3, 4, 5))
    w(f"| {ini or '(none)'} | {letter} | {cname} | {tones} |")
w('\nThai can\'t separate z/zh, c/ch, s/sh (จ ช ซ for both); the pinyin does, and ↪ ม้วนลิ้น marks zh/ch/sh/r. j/q/x are always followed by i or ü.\n')
w('## 5.4 Finals (house spellings: always use these)\n')
w('| Final | Example | Pinyin | Thai |'); w('|---|---|---|---|')
FIN_EX = [('a','他','ta1'),('o','波','bo1'),('e','喝','he1'),('-i after z c s','四','si4'),('-i after zh ch sh r','日','ri4'),('er','二','er4'),
      ('ai','来','lai2'),('ei','北','bei3'),('ao','好','hao3'),('ou','都','dou1'),('an','看','kan4'),('en','很','hen3'),
      ('ang','忙','mang2'),('eng','冷','leng3'),('ong','中','zhong1'),('i','你','ni3'),('ia','家','jia1'),('ie','谢','xie4'),('iao','小','xiao3'),
      ('iu (iou)','六','liu4'),('ian','天','tian1'),('in','心','xin1'),('iang','想','xiang3'),('ing','请','qing3'),('iong','熊','xiong2'),
      ('u','不','bu4'),('ua','话','hua4'),('uo','国','guo2'),('uai','快','kuai4'),('ui (uei)','对','dui4'),('uan','关','guan1'),('un (uen)','准','zhun3'),
      ('uang','光','guang1'),('ü','女','nv3'),('u after j q x (= ü)','去','qu4'),('üe (ue after j q x)','学','xue2'),('üan (uan after j q x)','选','xuan3'),('ün (un after j q x)','军','jun1')]
for fin, ch, tok in FIN_EX:
    s = cn.syl(tok)
    w(f"| {fin} | {ch} | {s['py']} | {s['th']} |")
w('\n- iong is simplified to -ง (熊 xióng สง); say a light y before the vowel.')
w('- ai after a consonant is ไ- (来 ไหล); with no initial it is อ้าย (爱 ài).\n')
w('## 5.5 Syllables written with y- and w- (no initial consonant)\n')
w('| Spelling | Example | Pinyin | Thai |'); w('|---|---|---|---|')
for fin, ch, tok in [('yi','一','yi1'),('ya','呀','ya1'),('ye','也','ye3'),('yao','要','yao4'),('you','有','you3'),('yan','眼','yan3'),('yin','音','yin1'),
      ('yang','羊','yang2'),('ying','英','ying1'),('yong','用','yong4'),('yu','鱼','yu2'),('yue','月','yue4'),('yuan','元','yuan2'),('yun','云','yun2'),
      ('wu','五','wu3'),('wa','哇','wa1'),('wo','我','wo3'),('wai','外','wai4'),('wei','为','wei4'),('wan','晚','wan3'),('wen','问','wen4'),
      ('wang','王','wang2'),('weng','翁','weng1'),('a, ai, an… (no initial)','爱','ai4')]:
    s = cn.syl(tok)
    w(f"| {fin} | {ch} | {s['py']} | {s['th']} |")
w('\n- 元 as the currency is หยวน in Thai text; the 🔊 reading of yuán is เหยวียน.\n')
w(T.CN_RULES)

def cn_row(word, spec, meaning):
    r = cn.sentence(spec)
    extra = ''
    if r['changes']: extra += ' ↪ เสียงเปลี่ยน: ' + ', '.join(r['changes'])
    if r['retro']: extra += ' ↪ ม้วนลิ้น: ' + ', '.join(r['retro'])
    py = r['py']
    if not re.search(r'[.!?]$', word.replace('。', '.')): py = py[0].lower() + py[1:]
    return f"| {word} | {py} | {r['th']}{extra} | {meaning} |"

w('## 5.7 Neutral-tone words (no mark on the second syllable)\n')
w('| Word | Pinyin | Thai | Meaning |'); w('|---|---|---|---|')
for a in [('谢谢','xie4-xie5','ขอบคุณ'),('东西','dong1-xi5','ของ'),('朋友','peng2-you5','เพื่อน'),('先生','xian1-sheng5','คุณ (ผู้ชาย), สามี'),('知道','zhi1-dao5','รู้'),
          ('喜欢','xi3-huan5','ชอบ'),('麻烦','ma2-fan5','ยุ่งยาก, รบกวน'),('客气','ke4-qi5','เกรงใจ'),('名字','ming2-zi5','ชื่อ'),('我们','wo3-men5','พวกเรา'),
          ('什么','shen2-me5','อะไร'),('怎么','zen3-me5','อย่างไร'),('认识','ren4-shi5','รู้จัก'),('意思','yi4-si5','ความหมาย'),('关系','guan1-xi5','ความสัมพันธ์'),
          ('时候','shi2-hou5','ตอน, เวลา'),('漂亮','piao4-liang5','สวย'),('衣服','yi1-fu5','เสื้อผ้า'),('告诉','gao4-su5','บอก'),('休息','xiu1-xi5','พักผ่อน'),('学生','xue2-sheng5','นักเรียน')]:
    w(cn_row(*a))
w('')
w(T.CN_ERHUA)
w('## 5.9 Words and set phrases (checked)\n')
w('| Word | Pinyin | Thai | Meaning |'); w('|---|---|---|---|')
for a in [('学校','xue2-xiao4','โรงเรียน'),('老师','lao3-shi1','ครู'),('校长','xiao4-zhang3','ผู้อำนวยการโรงเรียน'),('班主任','ban1-zhu3-ren4','ครูประจำชั้น'),('家长','jia1-zhang3','ผู้ปกครอง'),
          ('护照','hu4-zhao4','พาสปอร์ต'),('签证','qian1-zheng4','วีซ่า'),('材料','cai2-liao4','เอกสาร (ที่ต้องยื่น)'),('申请表','shen1-qing3>2-biao3','ใบคำร้อง'),('证件照','zheng4-jian4-zhao4','รูปติดบัตร'),
          ('复印件','fu4-yin4-jian4','สำเนา'),('签名','qian1-ming2','ลายเซ็น'),('预约','yu4-yue1','นัดหมาย'),('面试','mian4-shi4','สัมภาษณ์'),('大使馆','da4-shi3>2-guan3','สถานทูต'),
          ('截止日期','jie2-zhi3 ri4-qi1','กำหนดส่ง'),('提交','ti2-jiao1','ยื่น, ส่ง'),('手续费','shou3-xu4-fei4','ค่าธรรมเนียม'),('收据','shou1-ju4','ใบเสร็จ'),('洗手间','xi3>2-shou3-jian1','ห้องน้ำ'),('等候区','deng3-hou4-qu1','ที่รอ'),
          ('带飞','dai4-fei1','แบก'),('奶妈','nai3-ma1','สายฮีล (สแลง)'),('坦克','tan3-ke4','แทงก์'),('辅助','fu3-zhu4','ซัพพอร์ต'),('打野','da3>2-ye3','ป่า (เกม MOBA)'),('射手','she4-shou3','สายยิง'),
          ('掉线','diao4-xian4','เน็ตหลุด'),('挂机','gua4-ji1','AFK'),('开黑','kai1-hei1','จัดตี้เล่นกับเพื่อน'),('排位','pai2-wei4','แรงก์'),('皮肤','pi2-fu1','สกิน'),('抽卡','chou1-ka3','สุ่มกาชา'),
          ('保底','bao3>2-di3','การันตี'),('氪金','ke4-jin1','เติมเงิน'),('萌新','meng2-xin1','มือใหม่'),('大佬','da4-lao3','โปร, เทพ'),('小号','xiao3-hao4','ไอดีรอง'),
          ('辛苦了。','xin1-ku3 le5 .','เหนื่อยหน่อยนะ / ขอบคุณที่ทุ่มเท'),('请稍等。','qing3 shao1 deng3 .','กรุณารอสักครู่'),('这边请。','zhe4-bian1 qing3 .','เชิญทางนี้'),
          ('麻烦您了。','ma2-fan5 nin2 le5 .','รบกวนด้วยนะครับ/คะ'),('好的。','hao3 de5 .','ได้ครับ/ค่ะ'),('收到。','shou1-dao4 .','รับทราบ (ในแชต)'),('不好意思。','bu4 hao3-yi4-si5 .','ขอโทษนะ, ขอรบกวน')]:
    w(cn_row(*a))
w('')
w('## 5.10 Established Thai names vs readings\n')
w('In Thai text, use the established Thai spelling; the 🔊 line still follows the rules.\n')
w('| Name | Thai text | 🔊 reading |'); w('|---|---|---|')
for name, spec, thai in [('北京','bei3-jing1','ปักกิ่ง'),('上海','shang4-hai3','เซี่ยงไฮ้'),('广州','guang3-zhou1','กวางโจว'),('香港','xiang1-gang3','ฮ่องกง'),('台湾','tai2-wan1','ไต้หวัน'),
                         ('泰国','tai4-guo2','ประเทศไทย'),('曼谷','man4-gu3','กรุงเทพฯ'),('清迈','qing1-mai4','เชียงใหม่'),('普吉','pu3-ji2','ภูเก็ต'),('芭提雅','ba1-ti2-ya3','พัทยา')]:
    r = cn.sentence(spec)
    extra = (' ↪ เสียงเปลี่ยน: ' + ', '.join(r['changes']) if r['changes'] else '') + (' ↪ ม้วนลิ้น: ' + ', '.join(r['retro']) if r['retro'] else '')
    w(f"| {name} | {thai} | {r['py']} · {r['th']}{extra} |")
w('')

# ---------------------------------------------------------------- 6–10
w(T.SEC6); w(T.SEC7); w(T.SEC8); w(T.SEC9); w(T.SEC10)

# ---------------------------------------------------------------- 11 gold examples
w('# 11. Checked examples: 30 sentences in 4 languages\n')
w('Context: the speaker is a Thai school staff member looking after students at a visa appointment (sentences 1–10), everyday polite speech (11–20), and casual online gaming with friends (21–30). Each line is in the one-line 🔊 format.\n')
CAT = {'work': 'งานดูแลนักเรียนและวีซ่า', 'daily': 'ชีวิตประจำวัน', 'game': 'เล่นเกมกับเพื่อน'}
P = build_phrases()
from phrases import P as RAW
for d, raw in zip(P, RAW):
    w(f"## 11.{d['n']} {d['th']} ({CAT[d['cat']]})\n")
    w(f"- EN: {d['en']['text']}")
    w(f"  คำอ่าน: {d['en']['read']}")
    w(f"- JP: {d['jp']['text']}")
    w(f"  🔊 {kana_line(raw['jp'][1])} · {d['jp']['roma']} · {d['jp']['read']}")
    w(f"- KR: {d['kr']['text']}")
    br = f"[{d['kr']['pron']}] " if d['kr']['pron'] else ''
    w(f"  🔊 {br}{d['kr']['roma']} · {d['kr']['read']}")
    w(f"- CN: {d['cn']['text']}")
    extra = ''
    if d['cn']['sandhi']: extra += ' ↪ เสียงเปลี่ยน: ' + ', '.join(d['cn']['sandhi'])
    if d['cn']['retro']: extra += ' ↪ ม้วนลิ้น: ' + ', '.join(d['cn']['retro'])
    w(f"  🔊 {d['cn']['roma']} · {d['cn']['read']}{extra}")
    if d['note']: w(f"- 💡 {d['note']}")
    w('')

# ---------------------------------------------------------------- 12
w(T.SEC12)
w('— End of reference —')

text = '\n'.join(out)
text = re.sub(r'\n{3,}', '\n\n', text)
open(sys.argv[1] if len(sys.argv) > 1 else 'NativeSense-Polyglot-Reference.txt', 'w', encoding='utf-8').write(text)
print(len(text), 'chars,', text.count('\n'), 'lines')
