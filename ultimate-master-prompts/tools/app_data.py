"""Export the checked phrase data for the practice app."""
import json, sys
from gen import build
from phrases import P as RAW

def kana_line(spec):
    s = ''
    for tok in spec.split():
        if tok in ('、', '。', '！', '？'):
            s = s.rstrip() + tok
        elif tok.startswith('~'):
            s = s.rstrip() + tok[1:] + ' '
        else:
            s += tok + ' '
    return s.strip()

NOTE_LANGS = {3: ['kr'], 4: ['kr'], 5: ['cn'], 7: ['jp'], 8: ['jp'], 11: ['kr'], 13: ['jp', 'cn'], 17: ['jp', 'kr', 'cn'],
              21: ['cn'], 23: ['cn'], 24: ['cn'], 25: ['cn'], 27: ['jp'], 28: ['jp', 'kr']}
def build_data():
    out = []
    for d, raw in zip(build(), RAW):
        out.append({
            'n': d['n'], 'cat': d['cat'], 'th': d['th'],
            'en': [d['en']['text'], d['en']['read']],
            'jp': [d['jp']['text'], kana_line(raw['jp'][1]), d['jp']['roma'], d['jp']['read']],
            'kr': [d['kr']['text'], d['kr']['pron'], d['kr']['roma'], d['kr']['read']],
            'cn': [d['cn']['text'], d['cn']['roma'], d['cn']['read'], d['cn']['sandhi'], d['cn']['retro'], d['cn']['tts']],
            'note': d['note'], 'noteLangs': NOTE_LANGS.get(d['n'], []),
        })
    assert all(bool(o['note']) == bool(o['noteLangs']) for o in out), 'note tags out of sync'
    return out

if __name__ == '__main__':
    out = build_data()
    json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(len(out), 'phrases')
