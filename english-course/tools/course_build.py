"""Generate Thai readings for every English line of the course; export JSON + Markdown."""
import json, re, sys
import en_th as E
import course_data as D

E.load('cmu_extract/cmudict/data/cmudict.dict')

# Names and words that need a fixed reading (Thai names keep their Thai spelling)
E.OVERRIDE.update({
    'nok': 'นก', 'somchai': 'สม-ชาย', 'hua': 'หัว', 'hin': 'หิน', 'chiang': 'เชียง', 'mai': 'ใหม่',
    'ms.': 'มิ(ซ)', 'a.m.': 'เอ-**เอ็ม**', 'p.m.': 'พี-**เอ็ม**', 'wi-fi': '**ไว**-ไฟ', 'ok': 'โอ-**เค**', 'tv': 'ที-**วี**',
    'really': '**เรีย**-ลี', 'parents': '**แพ**-เริน(ท)(ส)',
})
for d in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
    for ph in E.CMU[d]:
        if ph[-2:] == ['D', 'EY2']:
            E.PHONES[d] = ' '.join(ph)
            break
E.PHONES['invite'] = 'IH1 N V AY2 T'          # noun: send you an invite
E.PHONES['stomachache'] = 'S T AH1 M AH0 K EY2 K'
E.PHONES['live'] = 'L IH1 V'                  # verb (อาศัยอยู่), not the adjective
E.PHONES['thirteen'] = 'TH ER0 T IY1 N'       # stress on -teen only
E.PHONES['excuse'] = 'IH0 K S K Y UW1 Z'      # verb: Excuse me
E.OVERRIDE['appointment'] = 'อะ-**พอย(น)**-เมิน(ท)'   # t usually silent (as in the reference file)
E.MULTI[('is', 'it')] = 'อิ-ซิท'              # linked, as in the reference file
E.PHONES.update({
    'use': 'Y UW1 Z',                  # verb: use the meter
    'email': 'IY1 M EY2 L',            # US stress on the first syllable
    'perfect': 'P ER1 F IH2 K T',      # adjective
    'every': 'EH1 V R IY0',            # two syllables, like everyone
    'sometimes': 'S AH1 M T AY2 M Z',
    'outside': 'AW2 T S AY1 D',
    'curry': 'K ER1 IY0',              # US
    'mic': 'M AY1 K',                  # microphone, said like Mike
    'wanted': 'W AA1 N T IH0 D',       # same vowel as want
})
E.MULTI[('team', 'up')] = 'ที-มัพ'            # linked, as in the reference file
E.MULTI[('watch', 'your')] = 'วา-เชอ(ร)'      # linked, as in the reference file
E.OVERRIDE['schedule'] = '**สเก**-จู(ล)'
E.OVERRIDE['reschedule'] = 'รี-**สเก**-จู(ล)'

unknown = set()
def R(s):
    return E.sentence(s, unknown)

out = dict(course=D.COURSE, modules=D.MODULES, steps=D.TEACH_STEPS, lesson0=D.LESSON0, sounds=[], lessons=[])
for g in D.SOUNDS:
    out['sounds'].append(dict(t=g['t'], d=g['d'], pairs=[dict(a=a, ar=R(a), am=am, b=b, br=R(b), bm=bm) for a, am, b, bm in g['pairs']]))
for l in D.L:
    o = dict(n=l['n'], mod=l['mod'], th=l['th'], en=l['en'], goal=l['goal'], scene=l['scene'],
             cast={k: dict(name=v[0], g=v[1], role=v[2]) for k, v in l['cast'].items()})
    o['phrases'] = [dict(en=e, r=R(e), th=t, note=nt) for e, t, nt in l['phrases']]
    o['dialogue'] = [dict(who=w, en=e, r=R(e), th=t) for w, e, t in l['dialogue']]
    p = l['pattern']
    o['pattern'] = dict(f=p['f'], ex=p['ex'], examples=[dict(en=e, r=R(e), th=t) for e, t in p['examples']])
    s = l['sound']
    o['sound'] = dict(t=s['t'], d=s['d'], words=[dict(en=w, r=R(w)) for w in s['words']])
    o['trap'] = l['trap']
    o['mission'] = dict(task=l['mission']['task'], model=[dict(en=e, r=R(e)) for e in l['mission']['model']])
    o['teach'] = l['teach']
    out['lessons'].append(o)

if __name__ == '__main__':
    print('UNKNOWN:', sorted(unknown))
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else 'course.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    n = sum(len(l['phrases']) + len(l['dialogue']) + len(l['pattern']['examples']) + len(l['mission']['model']) for l in out['lessons'])
    print('lessons', len(out['lessons']), 'english lines', n)
