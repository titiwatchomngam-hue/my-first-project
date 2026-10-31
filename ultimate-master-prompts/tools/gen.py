import json, re, sys
import jp, kr, cn
from phrases import P

def hangul_only(s):
    return re.sub(r'[^가-힣]', '', s)

def build():
    out = []
    for i, p in enumerate(P, 1):
        j = jp.sentence(p['jp'][1])
        k = kr.sentence(p['kr'][1])
        c = cn.sentence(p['cn'][1])
        kr_pron = p['kr'][1] if hangul_only(p['kr'][1]) != hangul_only(p['kr'][0]) else ''
        out.append({
            'n': i, 'cat': p['cat'], 'th': p['th'],
            'en': {'text': p['en'][0], 'read': p['en'][1]},
            'jp': {'text': p['jp'][0], 'roma': j['ro'], 'read': j['th']},
            'kr': {'text': p['kr'][0], 'pron': kr_pron, 'roma': k['rr'], 'read': k['th']},
            'cn': {'text': p['cn'][0], 'roma': c['py'], 'read': c['th'], 'sandhi': c['changes'], 'retro': c['retro'],
                   'tts': p.get('tts_cn', '')},
            'note': p.get('note', ''),
        })
    return out

if __name__ == '__main__':
    data = build()
    json.dump(data, open('phrases.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for d in data:
        print(f"#{d['n']} [{d['cat']}] {d['th']}")
        print(f"  EN {d['en']['text']}  /  {d['en']['read']}")
        print(f"  JP {d['jp']['text']}  /  {d['jp']['roma']}  /  {d['jp']['read']}")
        pr = f"[{d['kr']['pron']}] " if d['kr']['pron'] else ''
        print(f"  KR {d['kr']['text']}  /  {pr}{d['kr']['roma']}  /  {d['kr']['read']}")
        extra = ''
        if d['cn']['sandhi']: extra += '  ↪ เสียงเปลี่ยน: ' + ', '.join(d['cn']['sandhi'])
        if d['cn']['retro']: extra += '  ↪ ม้วนลิ้น: ' + ', '.join(d['cn']['retro'])
        print(f"  CN {d['cn']['text']}  /  {d['cn']['roma']}{extra}  /  {d['cn']['read']}")
        if d['note']: print('  💡', d['note'])
