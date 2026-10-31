# Static sections of the NativeSense Polyglot reference file.
# Tables marked {{...}} are generated from the reading engines in ref_build.py.

HEADER = """# NativeSense Polyglot: Reference (Knowledge file)

For: NativeSense Polyglot, Complete Edition, rev. 3 (TH · EN · JP · KR · CN)
File version: rev. 3, 31 October 2026

## How to use this file

- This file spells out, in detail, the rules in your instructions for Thai readings (§9–§10), numbers and dates (§7), and common terms. Use it for every reading and every term choice.
- The tables and the 30 checked sentences (section 11) were produced with the same rules and checked by hand. When you write a reading, follow the same patterns letter for letter.
- If this file and your instructions ever disagree, your instructions win. Glossaries and term lists the user adds later (in Knowledge or in the chat) win over both.
- This file is your own house style, not an outside source. Don't mention it unless the user asks, and don't cite it as a source for facts about the world.
- Thai readings are approximations for learners. Give the legend (§9 of your instructions) the first time, as usual.

## Contents

1. Thai reading marks (every language)
2. English
3. Japanese
4. Korean
5. Chinese (Mandarin)
6. Numbers, dates, and times
7. Glossary: address and titles
8. Glossary: school, visa, and office
9. Glossary: games
10. Traps: false friends, calques, and etiquette
11. Checked examples: 30 sentences in 4 languages
12. Known mistakes (wrong → right)
"""

SEC1 = """# 1. Thai reading marks (every language)

## 1.1 Layout

- `-` joins the syllables of one word. A space separates words.
- Sounds that link across words are written together: check it out → เช็ก-กิ-**ดาว(ท)** · Could you → คุ-จู · team up → ที-มัพ.
- **Bold** = the stressed syllable. English only, in every word of two or more syllables. Bold the whole syllable, brackets included: อะ-**บาว(ท)** · อิก-**สกิว(ซ)** · **เอ(ฟ)**-รี-วัน · **แพส**-พอ(ร)(ท).
- Punctuation: copy the punctuation of the romanization line (`,` `?` `!` `—`). Keep a full stop between two sentences and drop the one at the very end: ฮะ-จิ-เมะ-มะ-ชิ-เตะ. โยะ-โระ-ชิ-กุ โอะ-เนะ-ไก ชิ-มัส
- Never use ์ (การันต์) anywhere in a reading, including ร์.

## 1.2 Why brackets exist: how Thai readers say a written final letter

| Written Thai final | Thai readers say | What this means for a foreign final sound |
|---|---|---|
| ก ข ค | -k | k → ก (แบ็ก) |
| ด ต ท ศ ษ ส ซ จ ช | -t | t → ท (เย็ท), Korean ㄷ → ด (인터넫 → อิน-ทอ-เน็ด); s, z, sh, ch, j need brackets |
| บ ป พ ฟ | -p | p → พ (English) or บ (Korean); f and v need brackets |
| ม | -m | m → ม |
| น ญ ณ ร ล ฬ | -n | n → น; l and r need brackets |
| ง | -ng | ng → ง |
| ย / ว | -i / -u glide | ย / ว |

## 1.3 Bracket rules

- A bracket after a syllable holds a final sound to say lightly that the Thai letters alone would drop or change. The letters outside the brackets must read correctly on their own.
- Always bracket these final sounds: l (ล), American r (ร), f and v (ฟ), th (ธ), z (ซ), sh and ch (ช), j/dge (จ).
- Before a bracketed final, use the short Thai vowel form where Thai has one (มั(ช) much · บั(ฟ) buff · อิ(ฟ) if · พุ(ช) push); otherwise the open form (แฮ(ฟ) have · เว(ล) well · คอ(ล) call).
- ไ ใ เ-า ำ can't take a final consonant, so any final after them goes in brackets: ไอ(ม) · ไท(ม) · ไน(ส) · ไร(ท) · ไล(ค) · ไล(น) · Japanese ないんだ ไน(น)-ดะ.
- A second (third…) final sound goes in its own bracket, in order: แธง(ค)(ส) · **แพส**-พอ(ร)(ท) · **ดาก**-ยะ-เมิน(ท)(ส) · ซีท(ส) · เน็ก(ส).
- Inside a bracket: k is (ค), t is (ท), d is (ด), p is (พ): แอส(ค) · ไล(ค) · ลอส(ท) · ไท(พ).
- Never bracket a final that Thai already reads correctly (ม น ง, k as ก, t as ท or ด, p as พ or บ): team → ทีม (not ที(ม)) · yet → เย็ท · done → ดัน.
- House rule for English s: right after the vowel, s may be written ส without brackets, as Thai loanwords do (บัส, แก๊ส): จัส(ท) · แอส(ค) · ลอส(ท) · **แพส**-พอ(ร)(ท) · **เรส**-ทรูม · **เควส**-เชิน. After ไ ใ เ-า ำ or after another final, s goes in brackets: ไน(ส) · ซีท(ส) · เน็ก(ส). English z is always bracketed: อิ(ซ) · พลี(ซ) · เนม(ซ).
- Korean ㄹ at the end of a syllable is always (ล): 서울 ซอ-อุ(ล) · 빨리 ปา(ล)-ลี.
- Chinese er and erhua are (ร): 二 èr เอ้อ(ร) · 一点儿 yìdiǎnr อี้-เตี่ย(ร).
- Why ล and ร never stand as finals: Thai reads them as น, so ฟีล would be read ฟีน. That's also why apologize is อะ-**พา**-ละ-ไจ(ซ), not อะ-พอล-ละ-ไจ(ซ).

## 1.4 Mouth tips for sounds Thai letters can't show (give once per chat, in Thai)

- EN v: ฟันบนแตะริมฝีปากล่างเบา ๆ แล้วออกเสียงให้คอสั่น (ไม่ห่อปากแบบ ว)
- EN th ใน the, this, there: ปลายลิ้นแตะใต้ฟันบนเบา ๆ แล้วออกเสียงให้คอสั่น · th ใน think, thank: ท่าเดียวกันแต่มีแค่ลม คอไม่สั่น
- EN z: เสียง ซ ที่คอสั่น เหมือนเสียงผึ้ง zzz
- EN r: ห่อปากเล็กน้อย ม้วนปลายลิ้นขึ้นโดยไม่แตะเพดาน · l: ปลายลิ้นแตะปุ่มเหงือกหลังฟันบน
- EN final sounds: ออกเสียงท้ายเบา ๆ แต่ต้องมี เพราะเปลี่ยนความหมาย (cat ≠ cats, play ≠ played)
- JP ふ: เป่าลมผ่านริมฝีปากที่เปิดเล็กน้อย ฟันไม่แตะปาก (ไม่ใช่ f แบบอังกฤษ)
- JP つ: ท กับ ซ ติดกันเป็นเสียงเดียว (ts)
- JP ら り る れ ろ: ปลายลิ้นดีดเพดานเบา ๆ ครั้งเดียว อยู่ระหว่าง ร กับ ล
- JP เสียงยาว: ลากเสียงยาวเป็นสองจังหวะ เพราะเปลี่ยนความหมาย (おばさん ป้า ≠ おばあさん ยาย)
- KR ㅓ กับ ㅗ: ㅓ อ้าปาก ไม่ห่อ (ออ แบบปากกว้าง) · ㅗ ห่อปากกลม (โอ)
- KR ㅡ: ฉีกปากเหมือนยิ้ม แล้วออกเสียง อือ
- KR ㄲ ㄸ ㅃ ㅉ ㅆ (เสียงตึง): เกร็งคอ ไม่มีลมออก เสียงแข็งและสั้น
- KR ㅋ ㅌ ㅍ ㅊ (เสียงมีลม): ลมพุ่งออกแรง (ถือกระดาษไว้หน้าปาก กระดาษต้องไหว) · ㄱ ㄷ ㅂ ㅈ ต้นคำ: มีลมเบากว่า
- CN zh, ch: ม้วนปลายลิ้นขึ้นไปแตะหลังปุ่มเหงือกแล้วปล่อย (zh ไม่มีลม · ch มีลม) · sh, r: ม้วนลิ้นแบบเดียวกันแต่ไม่แตะ
- CN ü (เขียน yu, ju, qu, xu, nü, lü): ทำปากจู๋เหมือนจะพูด อู แล้วพูด อี
- CN วรรณยุกต์: 1 สูงและเรียบ (สูงกว่าเสียงสามัญของไทยนิดหน่อย) · 2 ขึ้น · 3 ต่ำ (เมื่ออยู่ท้ายวลีจะลงแล้วขึ้น) · 4 ลงแรงและสั้น · เสียงเบา: สั้นและเบา
"""

SEC2 = """# 2. English

English gets only a Thai reading (no romanization). Default US; show UK only where it really differs (§10.1 of your instructions).

## 2.1 Vowels

| Sound (IPA) | Examples | Thai |
|---|---|---|
| iː | see, team, please | อี: ซี · ทีม · พลี(ซ) |
| ɪ | it, minute, visit | อิ: อิท · **มิ**-นิท · **วิ**-ซิท |
| e | yet, ten, ready | เอ็ / เอ: เย็ท · เท็น · **เร**-ดี |
| æ | back, have, thanks | แอ: แบ็ก · แฮ(ฟ) · แธง(ค)(ส) |
| ʌ | done, come, much | อะ/อั: ดัน · คัม · มั(ช) |
| ɑː (and US "short o") | watch, hot (US), sorry (US) | อา: วา(ช) · ฮาท · **ซา**-รี |
| ɒ (UK "short o") | hot, sorry, doctor | อ็อ: ฮ็อท · **ซ็อ**-รี · **ด็อก**-เทอะ |
| ɔː | all, call, talk | ออ: ออ(ล) · คอ(ล) · ทอก |
| ʊ | good, could, book | อุ: กุด · คุด · บุก |
| uː | you, soon, through | อู: ยู · ซูน · ธรู |
| ɝː (US) / ɜː (UK) | her, work, person | เออ: เฮอ(ร) · เวอ(ร)(ค) · **เพอ(ร)**-เซิน |
| ə | the, about, to | เออะ/อะ: เดอะ · อะ-**บาว(ท)** · ทะ |
| ɚ (US) / ə (UK), unstressed | teacher, over | เออ(ร) / เออะ: **ที**-เชอ(ร) / **ที**-เชอะ · **โอ**-เวอ(ร) |
| ən, əl (unstressed) | eaten, little, level | เอิน, เอิ(ล): **อี**-เทิน · **ลิ**-เดิ(ล) · **เล**-เวิ(ล) |
| eɪ | okay, name, play | เอ: โอ-**เค** · เนม · เพล |
| aɪ | I, time, nice | ไอ: ไอ · ไท(ม) · ไน(ส) |
| ɔɪ | boy, point | ออย: บอย · พอย(น)(ท) |
| aʊ | now, how, about | อาว: นาว · ฮาว · อะ-**บาว(ท)** |
| oʊ (US) / əʊ (UK) | go, no, slowly | โอ: โก · โน · **สโล**-ลี |
| ɪr / ɪə | here, really | เอีย: เฮีย(ร) · **เรีย**-ลี |
| er / eə | there, where | แอ: แด(ร) · แว(ร) |
| ʊr / ʊə | sure, tour | อัว: ชัว(ร) · ทัว(ร) |
| ɑːr | car, start | อา: คา(ร) · สตา(ร)(ท) |
| ɔːr | more, your, for | ออ: มอ(ร) · ยอ(ร) · ฟอ(ร) |

## 2.2 Consonants

- At the start of a syllable: p พ · b บ · t ท · d ด · k ค · g ก · f ฟ · v ว · th (think) ธ · th (the) ด · s ซ · z ซ · sh ช · ch ช · j จ · h ฮ · m ม · n น · l ล · r ร · w ว · y ย.
- s before another consonant is ส: speak สปีก · slowly **สโล**-ลี · excuse อิก-**สกิว(ซ)** · student **สตู**-เดิน(ท).
- Clusters keep both letters: please พลี(ซ) · through ธรู · restroom **เรส**-ทรูม · dropped ดราพ(ท).
- Final sounds:

| Final sound | Thai | Examples |
|---|---|---|
| p | พ (bracketed after ไ etc.) | ดราพ(ท) · ที-มัพ · ไท(พ) |
| b | บ | เว็บ |
| t | ท | เย็ท · เก็ท · ฮาท · ไร(ท) · ลอส(ท) |
| d | ด | เพลด · กุด · นีด |
| k | ก, or (ค) in brackets | แบ็ก · สปีก · ทอก · ไล(ค) · แอส(ค) |
| g | ก | บิก · แล็ก |
| m | ม | ทีม · คัม · ไท(ม) |
| n | น | ดัน · ซูน · ไล(น) |
| ng | ง | **เพล**-อิง · ธิง(ค) |
| l | (ล) | ฟี(ล) · คอ(ล) · วิ(ล) |
| r (US) | (ร) | มอ(ร) · ยอ(ร) · แด(ร) |
| f, v | (ฟ) | อิ(ฟ) · แฮ(ฟ) · ไล(ฟ) |
| th | (ธ) | มัน(ธ) |
| s | ส right after the vowel, otherwise (ส) | จัส(ท) · แอส(ค) · ไน(ส) · ซีท(ส) |
| z | (ซ) | อิ(ซ) · พลี(ซ) · เนม(ซ) |
| sh, ch | (ช) | มั(ช) · พุ(ช) · วา(ช) |
| j, dge | (จ) | เพ(จ) · **แด**-มิ(จ) |

## 2.3 US vs UK: the only reading differences to show

| Where | US | UK |
|---|---|---|
| r after a vowel | teacher **ที**-เชอ(ร) · your ยอ(ร) · more มอ(ร) | **ที**-เชอะ · ยอ · มอ |
| t between vowels | water **วอ**-เดอ(ร) · better **เบ**-เดอ(ร) · little **ลิ**-เดิ(ล) | **วอ**-เทอะ · **เบ**-เทอะ · **ลิ**-เทิ(ล) |
| o in hot, doctor | ฮาท · **ดาก**-เทอ(ร) · sorry **ซา**-รี · copy **คา**-พี | ฮ็อท · **ด็อก**-เทอะ · **ซ็อ**-รี · **ค็อ**-พี |
| a in can't, ask, pass, staff | แคน(ท) · แอส(ค) · **แพส**-พอ(ร)(ท) · สแต(ฟ) | คาน(ท) · อาส(ค) · **พาส**-พอ(ท) · สตา(ฟ) |

Other real US/UK differences (write UK only when the user asked for UK or it matters):
- Words: restroom / toilets · line / queue · fill out / fill in (a form) · vacation / holiday · apartment / flat · cell phone / mobile (phone) · check / bill (restaurant) · schedule / timetable (school, trains) · principal / head teacher · homeroom teacher / form tutor.
- Spelling: color / colour · center / centre · organize / organise · traveling / travelling · license / licence (noun) · program / programme (TV; a computer program is "program" in both).
- Dates: April 3, 2026 (said "April third") / 3 April 2026 ("the third of April").

## 2.4 Natural speed: weak forms and linking

Use weak forms for unstressed little words in natural-speed readings:

| Word | Careful | Natural speed |
|---|---|---|
| the | ดี | เดอะ (ดิ before a vowel sound, optional) |
| a / an | เอ / แอน | อะ / เอิน |
| and | แอน(ด) | เอิน |
| to | ทู | ทะ |
| for | ฟอ(ร) | เฟอ(ร) |
| of | อั(ฟ) | เอิ(ฟ) |
| can | แคน | เคิน |
| at | แอท | เอิท |
| from | ฟรัม | เฟริม |
| them | เด็ม | เดิม |
| you / your | ยู / ยอ(ร) | ยะ / เยอ(ร) (fast casual speech only) |

Linking:
- Consonant + vowel: team up ที-มัพ · pick it up พิ-กิ-**ดัพ** · check it out เช็ก-กิ-**ดาว(ท)** · is it อิ-ซิท · hold on โฮ(ล)-ดาน.
- t/d + you: could you คุ-จู · meet you มี-ชู · did you ดิ-จู · watch your วา-เชอ(ร).
- US flap t (t between vowels → ด): it'll **อิ**-เดิ(ล) · a little อะ **ลิ**-เดิ(ล) · photo **โฟ**-โด.

## 2.5 Words (US first; UK only if different)

| Word | US | UK | Note |
|---|---|---|---|
| passport | **แพส**-พอ(ร)(ท) | **พาส**-พอ(ท) | |
| visa | **วี**-ซะ | | |
| document(s) | **ดาก**-ยะ-เมิน(ท)(ส) | **ด็อก**-ยะ-เมิน(ท)(ส) | |
| application | แอ-พลิ-**เค**-เชิน | | |
| form | ฟอ(ร)(ม) | ฟอม | |
| signature | **ซิก**-นะ-เชอ(ร) | **ซิก**-นะ-เชอะ | |
| appointment | อะ-**พอย(น)**-เมิน(ท) | | the t is usually silent |
| interview | **อิน**-เทอ(ร)-วิว | **อิน**-เทอะ-วิว | |
| schedule | **สเก็**-จู(ล) | **เช็**-จู(ล) | many UK speakers also say สเก็-จู(ล) |
| deadline | **เด็ด**-ไล(น) | | |
| staff | สแต(ฟ) | สตา(ฟ) | |
| student | **สตู**-เดิน(ท) | **สติว**-เดิน(ท) | |
| teacher | **ที**-เชอ(ร) | **ที**-เชอะ | |
| principal | **พริน**-ซะ-เพิ(ล) | | UK schools: head teacher |
| parents | **แพ**-เริน(ท)(ส) | | |
| embassy | **เอ็ม**-บะ-ซี | | |
| immigration | อิ-มะ-**เกร**-เชิน | | |
| extension | อิก-**สเต็น**-เชิน | | |
| certificate | เซอ(ร)-**ทิ**-ฟิ-เคิท | เซอะ-**ทิ**-ฟิ-เคิท | |
| copy | **คา**-พี | **ค็อ**-พี | |
| receipt | ริ-**ซีท** | | the p is silent |
| photo | **โฟ**-โด | **โฟ**-โท | |
| restroom | **เรส**-ทรูม | | UK: toilets **ทอย**-เลิท(ส) |
| question | **เควส**-เชิน | | |
| Wednesday | **เว็น(ซ)**-เด | | the first d is silent |
| carry | **แค**-รี | | |
| support | เซอะ-**พอ(ร)(ท)** | เซอะ-**พอ(ท)** | |
| heal | ฮี(ล) | | |
| tank | แทง(ค) | | |
| damage | **แด**-มิ(จ) | | |
| level | **เล**-เวิ(ล) | | |
| update | noun **อัพ**-เดท · verb อัพ-**เดท** | | stress moves |
| event | อิ-**เว็น(ท)** | | |
| server | **เซอ(ร)**-เวอ(ร) | **เซอ**-เวอะ | |
| ranked | แรง(ค)(ท) | | |
| nerf | เนอ(ร)(ฟ) | เนอ(ฟ) | |
| buff | บั(ฟ) | | |
| patch | แพ(ช) | | |
| lag | แล็ก | | |
| skin | สกิน | | |
| noob | นูบ | | |
| GG | จี-จี | | |
"""

JP_RULES = """## 3.2 Rules in one place (with checked examples)

- k t p ch: ค ท พ ช at the start of a word, ก ต ป จ inside one: たかい ทะ-ไก · ちょっと ช็อต-โตะ · こんにちは คน-นิ-จิ-วะ. Particles count as inside a word: か กะ · と โตะ · から กะ-ระ · けど เกะ-โดะ.
- g is ก everywhere: が กะ · ご โกะ · ぎ กิ.
- r = ร, never ล: ら ระ · りょ เรียว.
- つ = สึ. After an open vowel, also close that syllable with ต: まつり มัต-สึ-ริ · あつい อัต-สึ-อิ · ふつか ฟุต-สึ-กะ · おつかれ อ็อต-สึ-กะ-เระ. The romaji doesn't change (matsuri, atsui).
- す = ซุ (すみません ซุ-มิ-มะ-เซ็ง); ず and づ = ซุ.
- Long vowels become Thai long vowels and short ones stay short: おばさん โอะ-บะ-ซัง vs おばあさん โอะ-บา-ซัง · ビル บิ-รุ vs ビール บี-รุ. えい is a long เ- (せんせい เซ็น-เซ); いい is ี (おいしい โอะ-อิ-ชี).
- Thai can't show length in ゃ ゅ ょ combinations: きょ and きょう are both เคียว. The romaji shows it (kyo / kyō).
- ai becomes ไ-: たかい ทะ-ไก · おてあらい โอะ-เตะ-อะ-ไร. A final after ไ goes in brackets: ないんだ ไน(น)-ดะ.
- っ closes the syllable before it: ก before k/g, ป before p/b/f, ส before s/sh/z/j, ต before t/ch/ts/d: がっこう กัก-โก · いっぷん อิป-ปุง · いっしょ อิส-โชะ · ちょっと ช็อต-โตะ · マッチ มัต-จิ. A closed o is written ็อ: もどって โมะ-ด็อต-เตะ.
- ん: ม before m/b/p (さんぽ ซัม-โปะ · ぜんぶ เซ็ม-บุ); ง before k/g (りんご ริง-โกะ) and at the end of a word (にほん นิ-ฮง · すみません ซุ-มิ-มะ-เซ็ง); น everywhere else (ほんとう ฮน-โต · せんせい เซ็น-เซ · えんりょ เอ็น-เรียว). Hepburn writes n' before a vowel or y inside a word: げんいん gen'in เก็น-อิง.
- Whispered u at the end: です เดส · ます มัส (ですか → เดส กะ · います → อิ-มัส). Other whispered vowels stay written: した ชิ-ตะ · すき ซุ-กิ.
- Particles: は = wa วะ · へ = e เอะ · を = o โอะ (in both romaji and Thai).
- Set spellings: こんにちは konnichiwa คน-นิ-จิ-วะ · こんばんは konbanwa คม-บัง-วะ.
- Write the kana line by words, with particles attached to the word before (せきに もどって ください。), and make the romaji match it syllable for syllable.
"""

KR_HEAD = """# 4. Korean

## 4.1 How a Korean reading is built

- Line: `🔊 [pronounced Hangul] romanization · Thai`. The brackets appear only when the pronunciation differs from the spelling: `🔊 [감사함니다] gam-sa-ham-ni-da · คัม-ซา-ฮัม-นี-ดา`, but `🔊 bi-ja · พี-จา` for 비자.
- Romanization = Revised Romanization of the bracketed sound, with hyphens between syllables. Because it follows the brackets, it shows tensing (학교 [학꾜] hak-kkyo); official RR on signs leaves tensing out (hakgyo). Names, places, and brands keep their official spelling (Seoul, Busan, Hyundai, Samsung).
- A "word" is a written word between spaces, and each word starts fresh, even inside a phrase: 다시 와 주세요 → ทา-ชี วา ชู-เซ-โย · 궁금한 게 → คุง-กึม-ฮัน เค. Sound changes across a space still go in the brackets: 밥 먹었어요 [밤 머거써요] · 부를 거예요 [부를 꺼에요].
- Base the Thai on the brackets only; the brackets use only the 7 final sounds (ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅇ).

## 4.2 Consonants

| Letter | Romanization | Thai at the start of a word | Thai inside a word | As a final sound |
|---|---|---|---|---|
| ㄱ | g (k as a final) | ค | ก | ก |
| ㄲ | kk | ก | ก, and it closes an open syllable before it with ก | ก |
| ㅋ | k | ค | ค | ก |
| ㄷ | d (t as a final) | ท | ด | ด |
| ㄸ | tt | ต | ต, closing an open syllable before it with ต | — |
| ㅌ | t | ท | ท | ด |
| ㅂ | b (p as a final) | พ | บ | บ |
| ㅃ | pp | ป | ป, closing an open syllable before it with ป | — |
| ㅍ | p | พ | พ | บ |
| ㅈ | j | ช | จ | ด |
| ㅉ | jj | จ | จ, closing an open syllable before it with ต | — |
| ㅊ | ch | ช | ช | ด |
| ㅅ | s | ซ; ช before ㅣ, ㅟ and y-vowels | same | ด |
| ㅆ | ss | ซ (sharper; never closes the syllable before it) | ซ | ด |
| ㄴ | n | น | น | น |
| ㅁ | m | ม | ม | ม |
| ㅇ | (silent) / ng | อ | อ | ง |
| ㄹ | r / l | ร | ร; ล right after a ㄹ final | (ล) |
| ㅎ | h | ฮ | ฮ | — |

- Closing examples: 오빠 โอป-ปา · 씨께 ซีก-เก · 여꿔늘 ย็อก-กวอ-นึ(ล) · 저쪼기에요 ช็อต-โจ-กี-เอ-โย. ㅆ doesn't close: 이써요 อี-ซอ-โย.
- After ㅅ ㅆ ㅈ ㅊ ㅉ (Thai ช/จ), a y-vowel loses its ย: 셔 ชอ · 쇼 โช · 져 จอ · 포지션 โพ-จี-ช็อน.
- Consonant + ㅑ ㅕ ㅠ: consonant + ย + vowel (며 มยอ · 명동 มย็อง-ดง · 류 รยู · 뉴비 นยู-บี). Consonant + ㅛ ㅖ ㅒ: the consonant goes before the vowel sign (효 ฮโย · 학꾜 ฮัก-กโย · 계 คเย · 걔 คแย).
- Consonant + w-vowel: 과 ควา · 괜 แควน · 권 คว็อน · 귀 ควี. ㅚ and ㅞ: 외 เว · 최 ชเว · 죄송 ชเว-ซง.
"""

KR_CHOICES = """## 4.5 Pronunciation choices used in this style

- -예요 / -이에요: write the everyday [에요]: 거예요 [거에요] · 몇 시예요 [멷 씨에요]. [예요] is also correct.
- ㅖ after a consonant other than ㄹ may be said [ㅔ]: 시계 [시게] · 지혜 [지헤] (both are standard). 례 and 예 keep [ㅖ].
- 의: อึย at the start of a word (의사 อึย-ซา); [이] after a consonant (희망 [히망]) and allowed in later syllables (회의 [회이]); [에] as the particle "of" (우리의 [우리에]).
- ㅐ and ㅔ sound the same in modern Seoul speech; keep แอ / เอ so the reading matches the spelling. ㅚ, ㅙ, ㅞ also sound almost the same (เว/แว).
- 맛있어요: [마시써요] (also standard: [마디써요]).
"""

CN_HEAD = """# 5. Chinese (Mandarin)

## 5.1 Line format

- `🔊 Pinyin with tone marks · Thai ↪ เสียงเปลี่ยน: … ↪ ม้วนลิ้น: …`
- 一 and 不 are written in the pinyin with the tone actually said (yí ge, bú shì, yìqǐ). A 3rd + 3rd change is NOT written in the pinyin; it goes at the end of the line (↪ เสียงเปลี่ยน: nǐ → ní), and the Thai follows the tone actually said (你好 → หนี ห่าว).
- Every syllable with zh, ch, sh, or r goes in ↪ ม้วนลิ้น, written as in the pinyin.
- Spell each syllable the same way every time it carries the same tone: 我 wǒ หว่อ (said wó before another 3rd tone: หวอ) · 是 shì ซื่อ · 好 hǎo ห่าว.

## 5.2 Tones → Thai tone marks, by the Thai letter's class

| Thai initial letter | 1st (ā) | 2nd (á) | 3rd (ǎ) | 4th (à) | Neutral |
|---|---|---|---|---|---|
| Mid class (ป ต ก จ อ) | no mark: ปา | ๋ : ป๋า | ่ : ป่า | ้ : ป้า | short: ปะ |
| Paired low (พ ฟ ท ค ฮ ช ซ) | low letter, no mark: พา | high partner (ผ ฝ ถ ข ห ฉ ส), no mark: ผา | high partner + ่ : ผ่า | low letter + ่ : พ่า | short: พะ |
| Single low (ม น ล ร ย ว) | no mark: มา | ห + letter: หมา | ห + letter + ่ : หม่า | letter + ่ : ม่า | short: มะ |

- Neutral tone: a final -a is written ะ (吗 ma มะ), a final -e is เ-อะ (的 de เตอะ · 了 le เลอะ · 么 me เมอะ); every other neutral syllable uses its 1st-tone spelling (子 zi จือ · 们 men เมิน · 谢谢 xièxie เซี่ย-เซีย · 东西 dōngxi ตง-ซี). Say it short and light.
- Thai can't tell a neutral tone from a 1st tone in those other syllables (东西 dōngxi "ของ" and dōngxī "ตะวันออก-ตะวันตก" are both ตง-ซี). The pinyin shows the difference; mention it when it matters.
"""

CN_RULES = """## 5.6 Tone changes

- 3rd + 3rd: the first becomes 2nd. Not written in the pinyin; shown at the end of the line, and the Thai follows it: 你好 Nǐ hǎo · หนี ห่าว ↪ เสียงเปลี่ยน: nǐ → ní. In a run of 3rd tones, the change depends on how the words group; in quick speech usually all but the last change (我也很好 wǒ yě hěn hǎo is often said wó yé hén hǎo).
- 一: yí before a 4th tone (一个 yí ge · 一下 yíxià · 一样 yíyàng); yì before 1st, 2nd, 3rd (一起 yìqǐ · 一天 yìtiān · 一点 yìdiǎn); yī when counting, in numbers and dates, and at the end of a word (第一 dì-yī · 十一 shíyī · 统一 tǒngyī). Write the tone actually said.
- 不: bú before a 4th tone (不是 bú shì · 不错 búcuò · 不客气 bú kèqi); bù everywhere else (不好 bù hǎo · 不来 bù lái). Write the tone actually said.
- Neutral-tone syllables have no mark (妈妈 māma · 我们 wǒmen · 东西 dōngxi). See 5.7.

"""

CN_ERHUA = """## 5.8 Erhua (儿化), mostly northern speech

Write the r as (ร). A final -n or -i drops before it: 一点儿 yìdiǎnr อี้-เตี่ย(ร) · 这儿 zhèr เจ้อ(ร) · 那儿 nàr น่า(ร) · 哪儿 nǎr หน่า(ร) · 玩儿 wánr หวา(ร). Taiwan speech rarely uses erhua (Taiwan: 一點 yìdiǎn, 這裡 zhèlǐ).
"""

SEC6 = """# 6. Numbers, dates, and times

## 6.1 Thai clock → 24-hour time (for Thai source text)

| Thai | 24-hour | English |
|---|---|---|
| ตีหนึ่ง · ตีสอง · ตีสาม · ตีสี่ · ตีห้า | 01:00 · 02:00 · 03:00 · 04:00 · 05:00 | 1 a.m. … 5 a.m. |
| หกโมงเช้า (ย่ำรุ่ง) | 06:00 | 6 a.m. |
| เจ็ดโมงเช้า = โมงเช้า | 07:00 | 7 a.m. |
| แปดโมงเช้า = สองโมงเช้า | 08:00 | 8 a.m. |
| เก้าโมงเช้า = สามโมงเช้า | 09:00 | 9 a.m. (not 3 a.m.) |
| สิบโมงเช้า = สี่โมงเช้า | 10:00 | 10 a.m. |
| สิบเอ็ดโมงเช้า = ห้าโมงเช้า | 11:00 | 11 a.m. |
| เที่ยง (เที่ยงวัน) | 12:00 | noon |
| บ่ายโมง | 13:00 | 1 p.m. |
| บ่ายสองโมง | 14:00 | 2 p.m. |
| บ่ายสามโมง | 15:00 | 3 p.m. |
| บ่ายสี่โมง = สี่โมงเย็น | 16:00 | 4 p.m. |
| ห้าโมงเย็น | 17:00 | 5 p.m. |
| หกโมงเย็น (ย่ำค่ำ) | 18:00 | 6 p.m. |
| หนึ่งทุ่ม · สองทุ่ม · สามทุ่ม · สี่ทุ่ม · ห้าทุ่ม | 19:00 · 20:00 · 21:00 · 22:00 · 23:00 | 7 p.m. … 11 p.m. |
| เที่ยงคืน (สองยาม) | 00:00 | midnight |

- ครึ่ง = half past: บ่ายสองโมงครึ่ง = 14:30. Official Thai uses the 24-hour clock with นาฬิกา or น.: 14.30 น. = 14:30 · 24.00 น. = midnight.

## 6.2 Big numbers

| Thai | Number | Japanese | Korean | Chinese | English |
|---|---|---|---|---|---|
| หมื่น | 10,000 | 1万 (いちまん) | 만 (never 일만) | 一万 yíwàn | ten thousand |
| แสน | 100,000 | 10万 (じゅうまん) | 십만 | 十万 shíwàn | a hundred thousand |
| ล้าน | 1,000,000 | 100万 (ひゃくまん) | 백만 | 一百万 yìbǎi wàn | a million |
| สิบล้าน | 10,000,000 | 1000万 (せんまん / いっせんまん) | 천만 | 一千万 yìqiān wàn | ten million |
| ร้อยล้าน | 100,000,000 | 1億 (いちおく) | 1억 (일억) | 一亿 yíyì | a hundred million |
| พันล้าน | 1,000,000,000 | 10億 (じゅうおく) | 10억 (십억) | 十亿 shíyì | a billion |
| ล้านล้าน | 1,000,000,000,000 | 1兆 (いっちょう) | 1조 (일조) | 一万亿 yíwàn yì (Mainland) / 一兆 (Taiwan) | a trillion |

Examples: 1.5 แสนบาท = THB 150,000 = 15万バーツ = 15만 바트 = 15万泰铢. 3億円 = 300 ล้านเยน.

## 6.3 Years

- Thai BE = CE + 543: พ.ศ. 2569 = 2026 · ปี 69 = 2026.
- Japan: 令和N年 = 2018 + N (令和8年 = 2026; 令和 started on 1 May 2019) · 平成N年 = 1988 + N (平成31年 = 2019, January to April).
- Taiwan: 民國N年 = 1911 + N (民國115年 = 2026).
- Keep the original year in brackets in official documents.

## 6.4 Japanese counters with irregular readings

| Counter | Readings |
|---|---|
| 時 (o'clock) | 1 いちじ · 4 よじ (not よんじ) · 7 しちじ · 9 くじ (not きゅうじ) |
| 分 (minutes) | 1 いっぷん · 3 さんぷん · 4 よんぷん · 6 ろっぷん · 8 はっぷん (also はちふん) · 10 じゅっぷん / じっぷん |
| 人 (people) | 1 ひとり · 2 ふたり · 3 さんにん · 4 よにん (not よんにん) |
| 日 (dates) | 1 ついたち · 2 ふつか · 3 みっか · 4 よっか · 5 いつか · 6 むいか · 7 なのか · 8 ようか · 9 ここのか · 10 とおか · 14 じゅうよっか · 20 はつか · 24 にじゅうよっか |
| 月 (months) | 4 しがつ · 7 しちがつ · 9 くがつ |
| 歳 (age) | 20 はたち (also にじゅっさい) |

Readings: いちじ Ichiji อิ-จิ-จิ · よじ Yoji โยะ-จิ · くじ Kuji คุ-จิ · じゅっぷん Juppun จุป-ปุง · ふたり Futari ฟุ-ตะ-ริ · よにん Yonin โยะ-นิง · ついたち Tsuitachi สึ-อิ-ตะ-จิ · ふつか Futsuka ฟุต-สึ-กะ · はつか Hatsuka ฮัต-สึ-กะ · しがつ Shigatsu ชิ-กัต-สึ · はたち Hatachi ฮะ-ตะ-จิ.

## 6.5 Korean: native numbers or Sino-Korean numbers

- Native numbers (하나 둘 셋 넷 … 스물) with 시 (o'clock), 명/사람 (people), 개 (things), 살 (age), 번 (times), 시간 (hours of duration). Before a counter: 하나 → 한, 둘 → 두, 셋 → 세, 넷 → 네, 스물 → 스무: 한 시 (1 o'clock) · 두 명 · 스무 살 (20 years old) · 세 번 (three times).
- Sino-Korean numbers (일 이 삼 사 …) with 분 (minutes), 초, 년, 월, 일, 원 (won), 층 (floor), 번 meaning "number" (3번 = No. 3), and phone numbers: 2시 30분 = 두 시 삼십 분 (= 두 시 반) · 5,000원 = 오천 원.
- Months 6 and 10 are irregular: 6월 = 유월 (not 육월) · 10월 = 시월 (not 십월).

## 6.6 Chinese numbers

- 两 liǎng before measure words and for 2 o'clock: 两个人 · 两天 · 两点 (2 o'clock) · 两千 (2,000). 二 èr when counting, in digits, ordinals, and months: 第二 · 十二 · 二十 · 二月.
- In phone, room, and bus numbers, 1 is often said yāo: 110 = yāo yāo líng.
- Time: 点 diǎn (o'clock) · 分 fēn (minutes) · 半 bàn (half past) · 一刻 yí kè (quarter past) · 三刻 sān kè (quarter to). 上午 a.m. · 下午 p.m. · 晚上 evening.
- Dates: 4月3日 in writing; 4月3号 (hào) in speech.
- Money: 元 yuán (written) = 块 kuài (spoken) · 角 jiǎo = 毛 máo (0.1) · 分 fēn (0.01). In Thai, the currency is หยวน.
"""

SEC7 = """# 7. Glossary: address and titles

| Thai | English | Japanese | Korean | Chinese |
|---|---|---|---|---|
| คุณ + ชื่อ | the first name; "Khun + name" for Thai colleagues (Khun Ing-Ing); Mr./Ms. + surname in formal English | 名前 + さん | 이름 + 씨 (peers and juniors) · 이름 + 님 (customers, formal, online) | 姓 + 先生/女士 (formal: 王先生, 李女士) · 小 + 姓 (younger, casual: 小王) |
| พี่ (at work or school) | the person's name | 名前 + さん · 先輩 (せんぱい, senior at school or work) | 선배(님) · 이름 + 씨/님 | 姓/名 + 哥/姐 (casual) · 前辈 qiánbèi (senior in a field) |
| น้อง (at work or school) | the person's name | 名前 + くん/ちゃん (casual) · さん (neutral) | 이름 + 씨 · 이름 alone (반말) | 小 + 名 |
| ครู / อาจารย์ | Mr./Ms. + surname (school) · Professor + surname (university) | 先生 (せんせい) | 선생님 · 교수님 (university) | 老师 lǎoshī |
| ผอ. (ผู้อำนวยการโรงเรียน) | principal (US) / head teacher (UK) | 校長 (こうちょう) | 교장 선생님 | 校长 xiàozhǎng |
| ลูกค้า | customer, client | お客様 (おきゃくさま) | 고객님 · 손님 | 顾客 gùkè · 客户 kèhù |
| เจ้าหน้าที่ / ผู้รับผิดชอบ | staff member · the person in charge | 係の人 (かかりのひと) · 担当者 (たんとうしゃ) | 직원 · 담당자 | 工作人员 gōngzuò rényuán · 负责人 fùzérén |
| ท่าน (very formal) | sir / ma'am | 様 (さま) · 方 (かた) | 님 · 분 | 您 nín |

- English school culture: students say Mr./Ms. + surname, not "Teacher" (international schools in Thailand may use Ms. + first name; follow the school). Thai workplace English: Khun + first name or nickname, or just the name.
- Japanese: never add さん to your own name. To outsiders, drop さん for your own colleagues (担当の〇〇が…); see §10.2 of your instructions.
- Korean: 씨 is never for seniors; 님 after a title (부장님, 선생님). 오빠/형/언니/누나 depend on both genders and closeness.
- Chinese: 你 vs 您 carries the politeness; 小姐 to call a waitress can sound off in mainland China (use 服务员 or 你好).
"""

SEC8 = """# 8. Glossary: school, visa, and office

| Thai | English | Japanese (reading) | Korean | Chinese (pinyin) |
|---|---|---|---|---|
| พาสปอร์ต, หนังสือเดินทาง | passport | パスポート · 旅券 (りょけん, formal) | 여권 [여꿘] | 护照 hùzhào |
| วีซ่า | visa | ビザ · 査証 (さしょう, formal) | 비자 · 사증 (formal) | 签证 qiānzhèng |
| วีซ่านักเรียน | student visa | 留学ビザ (りゅうがくビザ) | 유학 비자 · 학생 비자 | 留学签证 liúxué qiānzhèng · 学生签证 |
| ต่อวีซ่า | extend a visa | ビザを延長する (えんちょうする) | 비자를 연장하다 | 续签 xùqiān · 签证延期 qiānzhèng yánqī |
| สถานทูต | embassy | 大使館 (たいしかん) | 대사관 | 大使馆 dàshǐguǎn |
| สถานกงสุล | consulate | 領事館 (りょうじかん) | 영사관 | 领事馆 lǐngshìguǎn |
| ตม. (สำนักงานตรวจคนเข้าเมือง) | immigration office | 入国管理局 (にゅうこくかんりきょく) · イミグレ (casual) | 출입국관리사무소 · 이민국 | 移民局 yímínjú |
| ใบคำร้อง, ใบสมัคร | application form | 申請書 (しんせいしょ) | 신청서 | 申请表 shēnqǐngbiǎo |
| กรอก (แบบฟอร์ม) | fill out (US) / fill in (UK) | 記入する (きにゅうする) | 작성하다 | 填写 tiánxiě |
| รูปติดบัตร | ID photo, passport photo | 証明写真 (しょうめいしゃしん) | 증명사진 · 여권 사진 | 证件照 zhèngjiànzhào |
| สำเนา | copy | コピー · 写し (うつし) | 사본 · 복사본 | 复印件 fùyìnjiàn |
| เอกสาร | documents | 書類 (しょるい) | 서류 | 材料 cáiliào (to submit) · 文件 wénjiàn |
| ลายเซ็น · เซ็นชื่อ | signature · sign | 署名 (しょめい) · サイン | 서명 · 사인 | 签名 qiānmíng · 签字 qiānzì |
| นัดหมาย | appointment | 予約 (よやく) · アポ (business) | 예약 | 预约 yùyuē |
| สัมภาษณ์ | interview | 面接 (めんせつ) | 면접 · 인터뷰 | 面试 miànshì · 面签 miànqiān (visa interview) |
| ใบรับรองการเป็นนักเรียน | certificate of enrollment | 在学証明書 (ざいがくしょうめいしょ) | 재학증명서 | 在读证明 zàidú zhèngmíng |
| ทรานสคริปต์ | transcript | 成績証明書 (せいせきしょうめいしょ) | 성적증명서 | 成绩单 chéngjìdān |
| ค่าเทอม | tuition, school fees | 学費 (がくひ) · 授業料 (じゅぎょうりょう) | 학비 · 등록금 | 学费 xuéfèi |
| หอพัก | dorm(itory) | 寮 (りょう) | 기숙사 | 宿舍 sùshè |
| ครูประจำชั้น | homeroom teacher (US) / form tutor (UK) | 担任 (たんにん) | 담임 선생님 | 班主任 bānzhǔrèn |
| ผู้ปกครอง | parents, guardians | 保護者 (ほごしゃ) | 학부모 · 보호자 | 家长 jiāzhǎng · 监护人 jiānhùrén |
| นักเรียนแลกเปลี่ยน | exchange student | 交換留学生 (こうかんりゅうがくせい) | 교환학생 | 交换生 jiāohuànshēng |
| กำหนดส่ง | deadline | 締め切り (しめきり) | 마감 · 마감일 | 截止日期 jiézhǐ rìqī |
| ยื่น, ส่ง (เอกสาร) | submit | 提出する (ていしゅつする) | 제출하다 | 提交 tíjiāo · 递交 dìjiāo |
| บัตรคิว | queue number, ticket | 整理券 (せいりけん) · 番号札 (ばんごうふだ) | 번호표 | 排队号码 páiduì hàomǎ · 取号 qǔhào (take a number) |
| ที่รอ, ห้องรอ | waiting area | 待合室 (まちあいしつ) | 대기실 | 等候区 děnghòuqū |
| ค่าธรรมเนียม | fee | 手数料 (てすうりょう) | 수수료 | 手续费 shǒuxùfèi |
| ใบเสร็จ | receipt | 領収書 (りょうしゅうしょ) · レシート | 영수증 | 收据 shōujù · 发票 fāpiào (official invoice) |
| หลักฐานทางการเงิน | proof of funds | 残高証明書 (ざんだかしょうめいしょ) | 잔고증명서 | 存款证明 cúnkuǎn zhèngmíng |
| ตราประทับเข้าเมือง | entry stamp | 入国スタンプ (にゅうこくスタンプ) | 입국 도장 | 入境章 rùjìngzhāng |
| เจ้าหน้าที่ | staff | スタッフ · 職員 (しょくいん) · 係員 (かかりいん) | 직원 · 스태프 | 工作人员 gōngzuò rényuán |
| ห้องน้ำ | restroom (US) / toilets (UK) | お手洗い (おてあらい, polite) · トイレ | 화장실 | 洗手间 xǐshǒujiān · 卫生间 wèishēngjiān · 厕所 cèsuǒ (plain) |

- Japan's own immigration agency is 出入国在留管理庁 (since 2019). For Thailand's immigration office, Japanese residents usually say イミグレ or 入国管理局.
- 材料 in Chinese visa and school paperwork means "the documents you submit", not "materials".
"""

SEC9 = """# 9. Glossary: games

| Thai gamer word | English | Japanese | Korean | Chinese |
|---|---|---|---|---|
| แบก | carry | キャリー | 캐리 | 带飞 dàifēi (being carried: 躺赢 tǎngyíng) |
| ฮีล · สายฮีล | heal · healer | 回復 (かいふく) · ヒーラー | 힐 · 힐러 | 奶 nǎi · 奶妈 nǎimā (slang) · 治疗 zhìliáo |
| แทงก์ | tank | タンク | 탱커 · 탱 | 坦克 tǎnkè · 坦 tǎn |
| ซัพ, ซัพพอร์ต | support | サポート · サポ | 서포터 · 서폿 | 辅助 fǔzhù |
| ป่า | jungle(r) | ジャングル · ジャングラー | 정글 | 打野 dǎyě |
| สายดาเมจ | DPS, damage dealer | アタッカー · DPS | 딜러 | 输出 shūchū |
| บัฟ · เนิร์ฟ (balance) | buff · nerf | 上方修正 (じょうほうしゅうせい) · 下方修正 (かほうしゅうせい) | 상향 · 하향 | 加强 jiāqiáng · 削弱 xuēruò |
| เมต้า | meta | 環境 (かんきょう) · メタ | 메타 | 版本答案 bǎnběn dá'àn (the meta pick) |
| อัปเดต · แพตช์ | update · patch | アップデート · アプデ · パッチ | 업데이트 · 패치 | 更新 gēngxīn · 版本更新 |
| แลค, แล็ก | lag | ラグ | 렉 | 卡 kǎ · 卡顿 kǎdùn |
| เน็ตหลุด | disconnect (DC) | 回線落ち (かいせんおち) | 튕기다 · 튕김 | 掉线 diàoxiàn |
| AFK | AFK | 放置 (ほうち) · 離席 (りせき) | 잠수 | 挂机 guàjī |
| มือใหม่ | newbie (neutral) · noob (teasing) | 初心者 (しょしんしゃ) | 뉴비 · 초보 | 萌新 méngxīn · 菜鸟 càiniǎo (teasing) |
| เทพ, โปร | pro, cracked | 上手い (うまい) · 神 (かみ) | 고수 | 大佬 dàlǎo · 大神 dàshén |
| ตี้, จัดตี้ | party up, team up | パーティーを組む (くむ) · 一緒にやる | 파티 · 같이 하다 | 组队 zǔduì · 开黑 kāihēi (with friends, voice chat) |
| แรงก์ | ranked | ランクマッチ · ランク | 랭크 · 랭겜 | 排位 páiwèi |
| สกิน | skin | スキン | 스킨 | 皮肤 pífū |
| กาชา, สุ่ม | gacha, pull | ガチャ (を引く, ひく) | 가챠 · 뽑기 | 抽卡 chōukǎ |
| การันตี | pity | 天井 (てんじょう) | 천장 | 保底 bǎodǐ |
| เติมเงิน | spend real money | 課金 (かきん) | 현질 | 氪金 kèjīn |
| อีเวนต์ | event | イベント | 이벤트 | 活动 huódòng |
| ยอมแพ้ (โหวต) | surrender, FF | 降参 (こうさん) · サレンダー | 항복 · 서렌 | 投降 tóuxiáng |
| ไอดีรอง | alt account, smurf | サブ垢 (サブあか) | 부캐 | 小号 xiǎohào |
| ฟาร์ม | farm, grind | 周回 (しゅうかい) · 稼ぐ (かせぐ) | 파밍 · 노가다 | 刷 shuā · 肝 gān |
| เกิดใหม่ | respawn | リスポーン | 리스폰 · 부활 | 复活 fùhuó |
| GG | GG | GG · お疲れ (おつかれ) | 지지 · 수고 | GG |

- Game slang moves fast and varies by game and server. When a term isn't in this table or in the instructions, say how sure you are (§5).
- Official localized names of games, characters, skills, and items: never guess; check or mark them (§5).
"""

SEC10 = """# 10. Traps: false friends, calques, and etiquette

## 10.1 Japanese ↔ Chinese false friends (same characters, different meaning)

| Characters | Japanese | Chinese |
|---|---|---|
| 大丈夫 | だいじょうぶ: ไม่เป็นไร, โอเค | dàzhàngfu: ลูกผู้ชายตัวจริง |
| 先生 | せんせい: ครู, หมอ, อาจารย์ | xiānsheng: คุณ (ผู้ชาย), สามี |
| 勉強 / 勉强 | べんきょう: เรียนหนังสือ | miǎnqiǎng: ฝืนใจ, จำใจ |
| 手紙 / 手纸 | てがみ: จดหมาย | shǒuzhǐ: กระดาษชำระ |
| 汽車 / 汽车 | きしゃ: รถไฟ (หัวรถจักรไอน้ำ) | qìchē: รถยนต์ |
| 新聞 / 新闻 | しんぶん: หนังสือพิมพ์ | xīnwén: ข่าว |
| 走る / 走 | はしる: วิ่ง | zǒu: เดิน, ไป, ออกไป |
| 丈夫 | じょうぶ: แข็งแรง, ทนทาน | zhàngfu: สามี |
| 娘 | むすめ: ลูกสาว | niáng: แม่ (ภาษาพูด/ถิ่น) · 姑娘 gūniang = หญิงสาว |
| 愛人 / 爱人 | あいじん: ชู้ | àiren: คู่สมรส (Mainland) |
| 床 | ゆか: พื้น | chuáng: เตียง |
| 湯 / 汤 | ゆ: น้ำร้อน | tāng: ซุป |
| 高校 | こうこう: ม.ปลาย | gāoxiào: มหาวิทยาลัย, สถาบันอุดมศึกษา |
| 工作 | こうさく: งานประดิษฐ์ · การวางแผนเบื้องหลัง | gōngzuò: งาน, ทำงาน |
| 留守 | るす: ไม่อยู่บ้าน | liúshǒu: อยู่เฝ้า (留守儿童 = เด็กที่พ่อแม่ไปทำงานต่างถิ่น) |
| 心中 | しんじゅう: การฆ่าตัวตายพร้อมกัน | xīnzhōng: ในใจ |
| 十分 | じゅうぶん: เพียงพอ · じゅっぷん: สิบนาที | shífēn: มาก, อย่างยิ่ง · 十分钟 shí fēnzhōng: สิบนาที |

## 10.2 Thai → English calques to avoid

| Thai | Not | Natural English |
|---|---|---|
| เปิด/ปิดไฟ, แอร์, ทีวี | open/close the light | turn on/off the light (the AC, the TV) |
| ถ่ายเอกสาร | take a document | make a copy, photocopy |
| กรอกฟอร์ม | write the form | fill out (US) / fill in (UK) the form |
| ยื่นเอกสาร | give documents | submit the documents |
| ต่อวีซ่า | continue the visa | extend (or renew) the visa |
| เลื่อนนัด | move the appointment | reschedule (the appointment) |
| ลางาน · ลาป่วย | leave work | take a day off · call in sick, take sick leave |
| เล่นเฟซบุ๊ก | play Facebook | be on Facebook, scroll Facebook |
| เหมือนกัน (same same) | same same | the same, similar |
| PIC (ผู้รับผิดชอบ) | PIC | the person in charge, point of contact |
| เรียก "ครู" | Teacher! | Mr./Ms. + surname |
| ไปเที่ยว | go to travel | go on a trip, travel, go out |

Also from your instructions: I am agree → I agree · discuss about → discuss · I'm boring → I'm bored · can able to → can / be able to · very like → really like.

## 10.3 Etiquette traps

- Japanese: ご苦労様 is for people below you; to anyone else use お疲れ様です. 了解です to a boss sounds casual; use 承知しました or かしこまりました. Don't call people あなた; use name + さん.
- Korean: 당신 is not a polite "you" (§10.3 of your instructions). 수고하세요 / 수고하셨습니다 to a superior sounds wrong to some people; 감사합니다 is always safe. 저기요 gets a stranger's attention; 아저씨/아줌마 can sound rude.
- Chinese: 你 vs 您 is the politeness switch. 吃了吗 as a greeting sounds old-fashioned. 555 means crying, not laughing.
- English: "Dear Sir/Madam" only when you don't know the name; otherwise Dear + Mr./Ms. + surname (formal) or Hi + first name (email).
"""

SEC12 = """# 12. Known mistakes (wrong → right)

| Wrong | Right | Rule |
|---|---|---|
| แพส-พอร์ท / แพส-พอร์(ท) | **แพส**-พอ(ร)(ท) | No ์ anywhere; an r before another final goes in brackets |
| อะ-พอล-ละ-ไจ(ซ) (apologize) | อะ-**พา**-ละ-ไจ(ซ) | ล can't be a final (Thai reads it น) |
| ที(ม) (team) | ทีม | Don't bracket a final Thai reads correctly |
| ไนน (わからないんだ) | วะ-กะ-ระ-ไน(น)-ดะ | ไ can't take a final |
| kuwashī · kīte | kuwashii · kiite | ii stays ii in Hepburn |
| wakarain da | wakaranai n da | Romaji matches the kana syllable for syllable |
| が written งะ next to ご written โกะ | が กะ · ご โกะ | Japanese g = ก everywhere |
| [보조 직원] | [보조 지권] bo-jo ji-gwon | Liaison: a final consonant moves to a following ㅇ |
| [열락드릴께요] | [열락뜨릴께요] | Tensing after a ㄱ final (락 + 드 → 락뜨) |
| 我 spelled อั่ว, then หวั๋ว | 我 wǒ หว่อ every time (หวอ only when said wó before a 3rd tone) | One spelling per syllable and tone |
| "zh and ch don't touch" | zh, ch touch; sh, r don't | §10.4 of your instructions |
| A memory hook presented as the real origin of a character | Label it วิธีจำ | §12 of your instructions |
| Could everyone please return to your seats? | …to their seats? / Everyone, please return to your seats. | Pronoun agreement |
| Ms. Ing-Ing | Khun Ing-Ing (or Ing-Ing) | Thai names in English |
| Main translation uses さん for your own colleague to an outsider while 💡 says drop it | Decide per listener; the translation and 💡 must agree | §10.2 of your instructions |
| → meaning adds words (ผมแค่มาช่วยดูแลนักเรียน) | ผมแค่มาดูแลนักเรียน | The → line adds nothing and drops nothing |
| Blocks named "กริยาที่ 1/2" | Name blocks by their job | Thai learners read it as กริยาช่อง 1/2 |
| "until ใช้ present simple เสมอ" | Present simple for the future; past for the past | State a rule's real scope |
| "details ต้องเติม s เสมอ" | the details (plural) · in detail (no s) | No "always" when there are exceptions |
| เบา(ท) for about | อะ-**บาว(ท)** | aʊ is always อาว |
"""
