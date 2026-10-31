# NativeSense English Starter

A 24-lesson English speaking course for Thai beginners who want to communicate, not just pass a test. Every English line has a Thai-script reading (US English), a Thai meaning, and a play button that uses the device's own voices.

**Open the app: https://claude.ai/artifact/Gkmb7QDFRbWsMWdAyBkXA6**

| File | What it is |
|---|---|
| [`COURSE.md`](COURSE.md) | The whole course as a readable book: every phrase, dialogue, pattern, tip, mission, and teaching plan |
| [`course-app.html`](course-app.html) | A copy of the published app page |
| [`tools/`](tools/) | The scripts that generate the readings, the app, and the book |

## What's in it

- **Start here:** how to read the Thai readings, and 7 sound contrasts Thai speakers often miss (final sounds, th, v/w, r/l, s/z, short/long vowels, word stress), with an ear-training game.
- **6 modules × 4 lessons:** first words · everyday survival · work and school (including a visa-day lesson) · small talk and friends · stories and opinions · when things go wrong.
- **Each lesson:** a can-do goal, 8 key phrases, a 6–7 line dialogue (play it all, or hide speaker B and practise their lines), a sentence pattern with three swaps, a pronunciation focus, one common Thai-speaker mistake, a 10-question mixed quiz, and a speaking mission.
- **For teachers:** every lesson has a 45-minute plan (warm-up question, listen and repeat, pattern drill, A/B role-play cards, wrap-up).
- **Review:** flashcards from the lessons you've finished; the ones you don't know yet come back first.

## Using the app

- It works on a phone. Tap the speaker button to hear a line, the second button to hear it slowly.
- Progress is saved to your claude.ai account (so it follows you between devices) when the page can reach it, and always in the browser as a backup. People you share the link with as Viewers keep their progress in their own browser only.
- The link is private to you. To use it with colleagues or students, open the page and use **Share**.
- If a play button is silent, the device has no English voice: add one in the device's text-to-speech settings, or open the page in Chrome or Safari.

## How the readings are made

The Thai readings follow the same rules as the NativeSense Polyglot reference file (`../ultimate-master-prompts/NativeSense-Polyglot-Reference.txt`, sections 1–2). `tools/en_th.py` converts US pronunciations from the CMU Pronouncing Dictionary into Thai script: brackets for final sounds Thai would drop, bold for stress, US flap t, and linking for *Could you* (คุ-จู) and similar. All 500 English lines were generated this way and then checked by hand, with a small list of overrides for names, linked phrases, and words whose dictionary entry didn't fit the context (for example *excuse* as a verb, *live* as อาศัยอยู่, *perfect* stressed on the first syllable).

To rebuild after editing `tools/course_data.py` (needs Python 3 and the CMU dictionary file at `tools/cmu_extract/cmudict/data/cmudict.dict`, from the `cmudict` package on PyPI):

```bash
cd tools
```

```bash
python3 course_build.py course.json
```

```bash
python3 course_app_build.py ../course-app.html
```

```bash
python3 course_book.py ../COURSE.md
```
