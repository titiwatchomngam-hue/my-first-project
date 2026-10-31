# What changed: from the PDF (Version 1) to NativeSense Polyglot (Complete Edition)

Version 1 is the PDF *คัมภีร์พรอมต์แปลภาษาและโค้ชสอนภาษาฉบับสมบูรณ์*: a universal prompt (§0), four language prompts (§1 EN, §2 JP, §3 KR, §4 CN), and three add-on modes (§5). The Complete Edition is [`master-prompt.md`](master-prompt.md): one complete prompt, ready for a Gemini Gem (or a Claude Project). It was built in five rounds, listed newest first.

## Round 5: Complete Edition, rev. 2 (final consistency pass)

- **Which language Thai input goes to (§4.2):** the order is now explicit. A language named in the message comes first, then replying to a foreign message, then the last language you named or the focus language, then the default. Before, typing JP once could clash with replying to a Korean message.
- **Japanese さん (§10.2):** decided by who's listening in each sentence, and the main translation and 💡 must agree. Round 4 said "the same choice in every level", which was wrong, because level 3 is for friends, where さん is fine.
- **Japanese g (§10.2):** the example りんご now reads ริง-โกะ, matching the "g = ก" rule.
- **→ meaning example (§12):** the example itself added ส่วน; it now follows its own rule.
- US spelling throughout (rumors, traveling).

## Round 4: Complete Edition, after the JP, KR, and CN tests

Every fix is built into its own section.
- **Name:** the Gem is now **NativeSense Polyglot** (your original brand), with an English description in the README.
- **Japanese:** Hepburn keeps ii and ei as written (kuwashii and kiite, not kuwashī and kīte). Romaji must match the kana syllable for syllable; one test reply wrote *wakarain da* for わからないんだ. The g sound is always ก (が = กะ), since one reply wrote งะ and โกะ in the same answer. When talking to outsiders, colleagues get no さん, and that choice must stay the same across every level and note; the test used さん in the main sentence while its own 💡 said to drop it.
- **Korean:** Hangul pronunciation brackets appear only when the sound changes, and they must match the romanization and Thai. The test showed [보조 직원] next to ji-gwon instead of [보조 지권]. Tense consonants close the syllable before them (씨께 ซีก-เก).
- **Chinese:** zh and ch touch behind the gum ridge, while sh and r don't (the test's tip said none of them touch). 我 is always หว่อ; the test wrote it two ways.
- **Thai readings:** ไ ใ เ-า ำ can't take a final consonant, so the extra sound goes in brackets (ไน(น), ไอ(ม)). A final ร is read as น, like ล. Apologize is อะ-พา-ละ-ไจ(ซ). Finals Thai already reads correctly aren't bracketed (ทีม, not ที(ม)).
- **Kanji and hanzi:** memory hooks are labeled วิธีจำ and never presented as a character's real origin. Simplified characters are explained with simplified components (详 = 讠 + 羊).
- **English:** Thai names go by first name or nickname (Khun Ing-Ing); Ms. goes with a surname, not a nickname.
- **→ meanings:** two test replies added มาช่วย where the sentence only said *here to look after*. The rule now carries that example.
- The final check (§15) covers all of the above.

## Round 3: after your first Gemini test

All fixes are built into their own sections; there's nothing to append.
- The Gem wrote แพส-พอร์(ท). §9 now bans ร์ by name, with passport → แพส-พอ(ร)(ท) as the example.
- No stress marks showed up in the reply you pasted. §9 now says exactly what to bold: the stressed syllable of every English word with two or more syllables (**เอ**-นี-แว(ร), อัน-**ทิ(ล)**).
- It wrote *Could everyone please return to your seats*. §10.1 now has a pronoun-agreement rule (everyone → their).
- Its tip for the *th* in *the* described air only. §10.1 now separates voiced *th* (the, this, there) from voiceless (think, thank).
- It labeled sentence blocks "กริยาที่ 1/2", which reads like กริยาช่อง 1/2, and it called the present tense after *until* "always" (เสมอ). §12 now names blocks by their job and requires grammar rules to state their real scope.
- The final check (§15) now covers examples as well as the main translation.
- New test #20 in the README uses your test sentence.

## Round 2: second review and Gemini Gem edition

**Errors found in a second review and corrected**
- 辛苦了 was glossed "ขอบคุณที่เหนื่อย", which isn't natural Thai. Now: "เหนื่อยหน่อยนะ / ขอบคุณที่ทุ่มเท".
- For an unknown speaker, round 1 said to write ครับ/ค่ะ everywhere, which is misspelled in questions. Now: ครับ/ค่ะ in statements, ครับ/คะ in questions.
- The repeat mark was written without spaces (เบาๆ, จริงๆ). It now follows the Royal Society spacing (เบา ๆ, จริง ๆ), matching the prompt's own spelling rule.
- The Japanese old-man speech style ("ข้า…นะ เจ้าหนุ่ม style") was unclear. Now: ข้า/เจ้า in an elder's voice (…หรอก, เจ้าหนุ่ม).
- The Japanese k/t/p rule now covers ち too: ช at the start of a word, จ inside one (こんにちは คน-นิ-จิ-วะ).
- エモい, ガチ, and ぴえん had no Thai gloss. Added.

**Carried over from your แปลชัวร์ Gem, which was tested in Gemini**
- Brackets: the letters outside the brackets must read correctly on their own: feel → ฟี(ล) (ฟีล would be read ฟีน), like → ไล(ค).
- Bold stress on every English reading line, in every format.
- No ์ anywhere in a reading (round 1 banned it only on sounds that must be heard).
- No ครับ/ค่ะ in the Gem's own explanations. If you want them back, see the README.
- No phone numbers, websites, prices, or agency policies unless they were verified in that chat. Scam warnings explain only from the signs in the text and never offer reply options.
- Every → meaning line must match its sentence exactly: nothing added, nothing dropped.
- Thai traps: ไม่ต้อง means "no need to", not "must not" (that's ห้าม); น่าจะ about the past is "should have" or "probably has"; ไม่น่าจะ = probably not; หมื่นห้า = 15,000, แสนสอง = 120,000; 24.00 น. = midnight.
- `แปลด่วน` keeps any ⚠️ line.

**Gem packaging**
- The Gem name is in the first line and in §1 (renamed NativeSense Polyglot in round 4). The name, the Description, the setup steps, and a fallback for Gemini's instruction box (moving §10 into a Knowledge file) are in the README.
- The wording works on both platforms: "Knowledge or project files", "if you can search the web".
- Two new tests: the English bracket and bold rules, and ไม่ต้อง.

## Round 1: rebuild from the PDF

### What was kept

- Your role paragraph is §1, almost word for word.
- Your 4-part answer and its Thai headings are Format A in §12: คำแปล (with the detected context) → ระดับภาษา → ห้องเรียนภาษา (สูตรต่อเลโก้, คำศัพท์และสำนวน, เรดาร์วัฒนธรรม) → ตอบกลับพร้อมใช้.
- The 3 politeness levels, now mapped onto each language's own system (§8): 敬語 / です・ます / タメ口, 하십시오체 / 해요체 / 반말, and so on.
- Everything from the four language prompts (keigo, omitted subjects, furigana, batchim linking, K-slang, tone sandhi, wuxia terms, chengyu) is in the matching language pack (§10).
- The three add-ons are now built-in commands: `โหมดเกม`, `โหมดข่าว`, and `สร้างคอร์ส` (§13). You no longer need to paste them.

### Structural change: 5 prompts became 1

The four language prompts each repeated the core rules, and each had different gaps: only §1 had "Zero Hallucination", only §0 had "Ambiguity Handling", and only §2 handled omitted subjects. Version 2 has one shared core (§1–§9, §11–§15) plus five language packs (§10.1 EN, §10.2 JP, §10.3 KR, §10.4 CN, §10.5 TH), so every language gets every safeguard. The `ตั้งค่า: โฟกัส JP` setting replaces switching between prompts. If you want a lighter single-language version, delete the packs you don't need (see the README).

### Errors fixed

| # | Where | In the PDF | Problem → fix |
|---|---|---|---|
| 1 | §0 | Covers "Thai <-> English, Japanese, Korean, and Chinese" | Nothing says which language a **Thai** message should go into. → §4.2 decides in this order: a target named in the message, the focus language, the language of the message you're replying to, then English with a one-line offer of the others. You can also type `EN` / `JP` / `KR` / `CN`. |
| 2 | End of §0–§4 | "Please acknowledge in Thai that you are ready…" and "พร้อมแปล… ส่งข้อความมาได้เลย!" | In Project instructions there's no separate setup message, so the model can answer your first real text with "พร้อมแล้วครับ" instead of translating it. → A greeting gets a short welcome; text gets translated right away (§4.6). |
| 3 | Highlights #1, §0, §1 | "100% accurate", "Zero Hallucination", "Verify all … before translating" | No model can guarantee this, and the prompt gives it no way to verify, which pushes it to *sound* certain rather than *be* accurate. → §5: mark the exact item you're unsure of, check outside facts with web search when available, cite only pages actually opened, never invent official names, plus a list of what is usually uncertain (Japanese name readings, characters with several readings, new slang, official game terms). |
| 4 | §0 vs §1 | §0 brackets the stressed syllable ("วงเล็บพยางค์ที่ต้องเน้นเสียงหนัก"); §1 bolds it; both ask for stress marks in every language | Two conflicting systems, and stress doesn't fit Japanese (pitch accent), Korean (no word stress), or Chinese (tones). → One legend for all languages (§9): **bold** = English stress only; brackets = a final sound to pronounce (as in แปลเนียน v2); Thai tone marks for Chinese; vowel length and っ for Japanese; the Hangul pronunciation [발음] for Korean. |
| 5 | §1 | "check it out → เช็ค-กิท-เอาท์" | Breaks §1's own connected-speech rule (the words aren't linked), and ์ tells Thai readers *not* to say the t. → เช็ก-กิ-**ดาว(ท)** (US flap t, final t in brackets). |
| 6 | §2 | "Kanji with Furigana (in brackets if helpful)", inside the sentence | Sentences you're meant to copy and send (translations, smart replies) end up with reading brackets inside them. → Readings always go on their own line under the sentence (§9). |
| 7 | §0 | All 4 sections are mandatory for every input | A one-word lookup gets 3 levels and 3 replies; a news article gets readings × levels for every sentence. → §12 picks a format by input (A short text, B long text, C word, D check, E question, F lyrics, G strong language), sizes replies automatically, and adds `แปลด่วน`. |
| 8 | §0, part 4 | Every chat, email, or question gets "ตกลง / ถามต่อ / ปฏิเสธ" | Doesn't fit congratulations, condolences, announcements, or a message *you* are sending. → Replies appear only for messages you received; requests and invitations get that trio, anything else gets three reactions that fit. |
| 9 | Mode 1 | "Master Lore & Glossary Table at the end of every response" + "Top 10" | The table repeats and grows with every reply, and a short scene has to be padded to reach 10. → The table shows only new or changed terms (full table: `อภิธานศัพท์`); the vocabulary list is "up to 10". |
| 10 | Mode 3 | 50 fully detailed items in one reply | Thai and CJK text use a lot of output, so a reply that long tends to get cut off or thin out toward the end. → One group of 10 per reply, then `ต่อ`; a quiz and a combined document are offered at the end. |
| 11 | §4 | "牛逼" listed as slang to decode, with no warning | It's vulgar, and a learner could use it with the wrong people. → Flagged as crude, with 牛 / 厉害 as clean options; Korean 존- / 개- and Chinese 白嫖 flagged too. |
| 12 | §4 | "你好 -> ní hǎo" | Unclear whether the changed tone goes into the pinyin; dictionaries and apps list 你 as nǐ, so searching for ní fails. → Pinyin keeps dictionary tones (except 一/不, as textbooks write them), the spoken change is shown as `↪ เสียงเปลี่ยน: nǐ → ní`, and the Thai reading follows real speech. |
| 13 | Throughout | ครับ hard-coded; nothing on the speaker's gender | Wrong Thai particles and pronouns, and the wrong 僕 / 私 / あたし in Japanese. → A gender setting with neutral forms by default; fiction follows the character. |
| 14 | Small | "ห้ามแปลตรงตัวแบบที่อาจเด็ดขาด" (garbled), "and促音" (missing space), "พรอมต์รวมมิตร **4** ภาษา" (it covers 5), romanization systems not named, "โต-เคียว" | → Wording fixed. Systems named: Hepburn with macrons, Revised Romanization of the pronounced form, Hanyu Pinyin. Japanese k/t/p follow the Thai transcription habit: ค/ท/พ at the start of a word, ก/ต/ป inside one (โต-เกียว). |

### Gaps closed

**From your new brief**
- Any pair among the five languages, not just X⇄Thai (JP→EN, KR⇄CN…), with a one-line Thai meaning.
- New content types (§11): official and government correspondence, news on politics and disasters, tech and game updates and new features, entertainment, and song lyrics.
- `💡 ข้อสังเกต`: a place for assumptions, uncertainties, and things you may have overlooked (who the reader is, time zones, the honorific the recipient expects, Taiwan vs Mainland wording). It shows up only when there's something real to say (§12).
- Accuracy comes first in the priorities (§1, §3). Each language has named reference standards: ราชบัณฑิตยสถาน, 국립국어원, 大辞林/大辞泉 and the NHK accent dictionary, 现代汉语词典 and the Taiwan Ministry of Education dictionary, and Merriam-Webster/Cambridge/Oxford. Your own glossaries override its term choices.

**Pronunciation that Thai readers can actually use**
- **Japanese:** vowel length (おばさん vs おばあさん, ビル vs ビール), っ, whispered vowels (です → เดส), ん before m/k/t, ค/ท/พ vs ก/ต/ป, well-known pitch pairs (雨/飴), and sung readings in lyrics (宇宙 → そら).
- **Korean:** the Hangul pronunciation for every sound change (liaison, nasalization, ㄴ+ㄹ, tensing, aspiration, silent ㅎ, palatalization, final sounds) and one Thai-letter scheme for plain/aspirated/tense consonants. Final ㄹ is written (ล), because a Thai final ล is read as น. Also the ㅢ rules.
- **Chinese:** Thai tone marks for Mandarin tones (1 สามัญ, 2 จัตวา, 3 เอก, 4 โท), 一/不 and 3rd-tone changes, the neutral tone (东西 dōngxi vs dōngxī), a retroflex note (是 vs 四 look the same in Thai letters), erhua, Taiwan readings, and Cantonese with Jyutping.
- **English:** US/UK in the four places they really differ, linking, weak forms, and the flap t.
- `อ่านยังไง`: a drill command with mouth and tongue tips and minimal pairs.

**Traps a translator has to catch**
- Text written only in kanji/hanzi that could be Japanese or Chinese, with false friends (大丈夫, 手紙, 勉強). Also written Cantonese, and Thai typed on the English keyboard layout (`l;ylfu` = สวัสดี).
- Number units: 万 / 만 = หมื่น, 億 / 억 = ร้อยล้าน, 兆 / 조 = ล้านล้าน (and in Mainland technical units, 兆 = mega).
- Era years (令和, 平成, 民國) and BE, date order, Japanese 25時, time zones shown in Thai time, no silent currency conversion, and Korean age (international age by law since 28 June 2023).
- Laughter: 555 ↔ ㅋㅋㅋ ↔ 草/www ↔ 哈哈哈. In Chinese, 555 means *crying*.
- News: hedges stay hedges (とみられる, -것으로 알려졌다, 据报道), and disputed names (竹島/독도, 日本海/동해, 台湾地区) get the source's term plus a neutral note. Disaster scales: 震度 ≠ magnitude, 警報 vs 注意報, evacuation levels, numbered typhoons.
- Names and honorifics: name order as Thai media use it; さん/様/先輩; 씨/님/오빠/형/언니/누나 and why 당신 isn't a polite "you"; 您/贵司/此致敬礼; titles kept in brackets; and the established Thai names for classic wuxia (郭靖 = ก๊วยเจ๋ง, not a fresh Mandarin transcription).
- Game localization: placeholders and tags (`{player}`, `%s`, `<color>`) stay untouched, official terms are used only if verified, each character keeps one voice, and each language's gamer slang is mapped to Thai gamer words (ตู้, การันตี, ดวงเกลือ, สายฟรี).

**Safety (carried over from แปลเนียน v2)**
- Text to translate is treated as data, so an email saying "ignore your instructions" gets translated, not obeyed.
- Scam flag, intensity scale for swearing with softer and polite versions, labels for threats and slurs, honest handling of links, images, and video, and no lyrics written from memory.

**Learning tools and settings**
- `ตรวจ` works for all five languages, including politeness errors (반말 to a boss). New: `ทบทวน` (quiz), `อธิบาย`, and `ตอบกลับ`.
- Settings for focus language, Chinese region (Mainland / Taiwan / Hong Kong), speaker gender, learner level, and reply size. Plus `เมนู` and `รีเซ็ต`.
