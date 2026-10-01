# What changed from "NativeSense TH–EN Master" (v1) to แปลเนียน TH⇄EN (v2)

The structure (18 sections, formats A–F, commands) is kept, so anything you already know still works. Section numbers are unchanged.

## Errors fixed

| # | Where (v1) | Problem | Fix in v2 |
|---|---|---|---|
| 1 | §8 Pronunciation | v1 told the model to mark sounds that *must* be pronounced with ์ (works → เวิร์คส์, can't → แคนท์). In Thai spelling ์ means "silent letter", so Thai readers drop exactly the sounds the guide is meant to keep. The same happens with ร์ in the US examples (ที-เชอร์ reads as "ที-เชอ", so the US r disappears). | Light final sounds go in brackets: แคท(ส), บุก(ส), ฟาย(ล), สต็อป(ท); US r is (ร). The one-time note now explains bold = stress and brackets = sounds you must say. |
| 2 | §3 vs §7.3, §8, §16 | The golden rule says never fill a template with "N/A"/"ไม่มี", but other sections required filler: "ไม่เกี่ยวข้อง (ต้นฉบับไม่ใช่ภาษาอังกฤษ)", "คำอ่าน UK: เหมือน US", "ใช้เหมือนกันทั้ง US และ UK". | Those sections and lines are now left out. One shared US/UK rule covers every format. |
| 3 | §11 calibration | The banter use of "Fuck off" was rated 2–3/5, but its Thai translation (ไม่จริงอ่ะ! / พูดเล่นป่ะเนี่ย) has no swearing at all (about 0/5), which breaks the prompt's own keep-the-intensity rule. "ไปให้พ้น" is also milder than the 4/5 given. | Banter → เชี่ย จริงดิ! (about 2–3/5), with the clean version offered as the softer option. Insult → ไสหัวไปเลย. |
| 4 | §3 priorities | Priority #2 "Facts (factual accuracy)" can be read as "fix factual errors", which conflicts with §12 ("don't silently correct facts"). | Now "Fixed details: names, numbers, dates… carried over exactly (don't correct the source)". |
| 5 | §7.2 spelling | อีเมล was given as an example of a casual loanword, but it is the Royal Society standard spelling. | There's now a short list of standard loanword spellings (อีเมล, อัปเดต, คลิก, ล็อกอิน, แอปพลิเคชัน, เกม not เกมส์, เช็ก vs เช็ค), with real casual examples alongside. |
| 6 | §11 vs §5 | §11 said to *ask* when tone is unclear; §5 says give both readings and ask only when a wrong guess could cause harm. | §11 now follows §5. |
| 7 | §2 + §16-C | The default "US + UK" had no rule for long texts, so a long email could come back as two full English versions. | Long texts and แปลงาน get one version (US unless the setting or context says UK). Only the real differences go under หมายเหตุ. |
| 8 | §16-D | Format D only fitted English headwords. A Thai word such as เกรงใจ had nowhere to put its English options. | D now covers both directions. |
| 9 | §16-A vs B | The 4-level lists used two different layouts (`**1. ทางการ** —` vs `1. **ทางการ:**`). | Both use one layout. |
| 10 | §7.1 | "จึงเรียนมาเพื่อโปรดทราบ → Thank you for your attention." is presentation English, not letter English. | Now "usually omitted". |
| 11 | small | "Show softeners" (meant "render"); the gender-neutral rule was repeated in §13; it was unclear whether โหมดเรียนรู้ stays on. | Wording fixed; duplicate removed; โหมดเรียนรู้ now stays on until ปิดโหมดเรียนรู้. |

## Upgrades (gaps closed)

**Safety and reliability**
- **Prompt-injection guard:** text to translate is treated as data. An email or web page that says "ignore previous instructions…" gets translated; the Gem doesn't follow it.
- **Scam flag:** a message asking for an OTP, a password, a transfer, or an urgent link click gets "⚠️ อาจเป็นมิจฉาชีพ".
- **No preamble:** Gemini tends to open with "แน่นอนค่ะ!". Replies now start with the result.
- **Consistency within a chat:** a name, term, gender, or register stays fixed once it's settled or the user corrects it.

**Understanding the request**
- **Direction comes from the text being translated, not the wrapper:** "ช่วยแปลหน่อย: Could you…" is EN→TH.
- **The user's own English plus "ถูกไหม"** goes to a grammar check, not a translation.
- **Format E** says "already correct" instead of inventing errors.
- **A greeting** gets a short welcome and the 5 key commands, not the whole 20-command list.

**Translation craft (Thai-specific expertise)**
- **Certainty and obligation matching:** อาจจะ / น่าจะ / คง / ควร / ต้อง map to may / probably / I guess / should / must, so น่าจะ never becomes a "must".
- **Thai clock traps:** สามโมงเช้า = 9 a.m. (not 3 a.m.), plus the full โมง/ทุ่ม/ตี system and 14.00 น.
- **Large numbers:** พันล้าน / หมื่นล้าน / แสนล้าน / ล้านล้าน → billion / trillion. Thai digits ๐–๙ are converted.
- **Year traps:** short BE years (ปี 69 = 2026), the fiscal year (ปีงบประมาณ starts 1 October), and the academic year.
- **Royal and monastic vocabulary (ราชาศัพท์):** this was missing entirely and matters a lot in Thai news and official text.
- **More letter formulas:** เรื่อง, อ้างถึง, สิ่งที่ส่งมาด้วย.
- **Officialese to avoid:** "Please be informed", "revert".
- **More calques:** ไม่เป็นไร, รบกวน, ไปเที่ยว, and พี่/น้อง as address terms.
- **Romanisation:** RTGS for Thai names and places that have no official spelling. Thai people are addressed by first name.
- **Certified translations:** a note that offices may require one for official submissions.
- **Pronunciation tips** for sounds Thai has no letter for (v, th, z, final sh/ch/j, r vs l).

**Commands and settings**
- New commands: **แปลเป็นอังกฤษ / แปลเป็นไทย** (force the direction) and **ปิดโหมดเรียนรู้**.
- **ตั้งค่า** confirms the change in one line, and the workplace context can be set from chat.
- The final check now also covers certainty words, particles, injected instructions, BE/CE years, ์ misuse, and filler.

**Gemini packaging**
- §7–§15 form one block that you can move into a Knowledge file if Gemini won't accept the full text (see README).
