# tools: how the readings are generated

These scripts produce every Thai reading, romanization, and pronounced-Hangul line in `../NativeSense-Polyglot-Reference.txt` and `../practice-app.html`, following §9–§10 of `../master-prompt.md`. You don't need them to use the Gem; they're here so later edits stay consistent.

| File | What it does |
|---|---|
| `jp.py` | Kana → Hepburn + Thai reading |
| `kr.py` | Pronounced Hangul → romanization + Thai reading |
| `cn.py` | Pinyin with tone numbers → pinyin with tone marks + Thai reading with tone marks |
| `phrases.py` | The 30 checked sentences (input for the engines) |
| `gen.py` | Prints all 30 sentences with their readings for review |
| `ref_text.py`, `ref_build.py`, `jp_tables.py` | Build the reference file |
| `app_template.html`, `app_data.py`, `build_app.py` | Build the practice app |

Run from this folder with Python 3:

```bash
python3 jp.py
```

```bash
python3 kr.py
```

```bash
python3 cn.py
```

Each engine prints its self-checks first. Then rebuild the outputs:

```bash
python3 ref_build.py ../NativeSense-Polyglot-Reference.txt
```

```bash
python3 build_app.py ../practice-app.html
```
