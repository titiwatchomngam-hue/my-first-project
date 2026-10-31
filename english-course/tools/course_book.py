"""course.json -> COURSE.md (a readable, printable course book)."""
import json, sys
d = json.load(open('course.json', encoding='utf-8'))
o = []
w = o.append
w(f"# {d['course']['name']}\n")
w(f"**{d['course']['th_name']}** · 24 บท · 6 หมวด\n")
w(d['course']['intro'] + '\n')
w('แอปเวอร์ชันโต้ตอบได้ (มีเสียงอ่าน แบบฝึก และบันทึกความคืบหน้า): https://claude.ai/artifact/Gkmb7QDFRbWsMWdAyBkXA6\n')
w('## วิธีอ่านคำอ่านไทย\n')
for h in d['lesson0']['how']:
    w(f'- {h}')
w('\n## สารบัญ\n')
w('- [บทเริ่มต้น: 7 เสียงที่คนไทยมักพลาด](#บทเริ่มต้น-7-เสียงที่คนไทยมักพลาด)')
for m, th, en in d['modules']:
    w(f'- หมวด {m}: {th} ({en})')
    for l in d['lessons']:
        if l['mod'] == m:
            w(f"  - บทที่ {l['n']}: {l['th']} ({l['en']})")
w('\n## บทเริ่มต้น: 7 เสียงที่คนไทยมักพลาด\n')
for i, g in enumerate(d['sounds'], 1):
    w(f"### {i}. {g['t']}\n")
    w(g['d'] + '\n')
    w('| คำ | คำอ่าน | ความหมาย | คำ | คำอ่าน | ความหมาย |')
    w('|---|---|---|---|---|---|')
    for p in g['pairs']:
        w(f"| {p['a']} | {p['ar']} | {p['am']} | {p['b']} | {p['br']} | {p['bm']} |")
    w('')
for m, th, en in d['modules']:
    w(f'\n# หมวด {m}: {th} ({en})\n')
    for l in d['lessons']:
        if l['mod'] != m:
            continue
        w(f"## บทที่ {l['n']}: {l['th']} ({l['en']})\n")
        w(f"**หลังจบบทนี้:** {l['goal']}\n")
        w('### ประโยคหลัก\n')
        for p in l['phrases']:
            w(f"- **{p['en']}**  \n  คำอ่าน: {p['r']}  \n  {p['th']}" + (f"  \n  _{p['note']}_" if p['note'] else ''))
        w(f"\n### บทสนทนา: {l['scene']}\n")
        w(' · '.join(f"**{k}** = {c['name']} ({c['role']})" for k, c in l['cast'].items()) + '\n')
        for x in l['dialogue']:
            w(f"- **{x['who']}:** {x['en']}  \n  คำอ่าน: {x['r']}  \n  {x['th']}")
        p = l['pattern']
        w(f"\n### สูตรประโยค\n\n`{p['f']}`\n\n{p['ex']}\n")
        for x in p['examples']:
            w(f"- **{x['en']}** · {x['r']} · {x['th']}")
        s = l['sound']
        w(f"\n### ออกเสียง: {s['t']}\n\n{s['d']}\n")
        w(' · '.join(f"{x['en']} ({x['r']})" for x in s['words']) + '\n')
        t = l['trap']
        w(f"### จุดที่คนไทยมักพลาด\n\n- ✗ ~~{t['wrong']}~~\n- ✓ **{t['right']}**\n- {t['why']}\n")
        w(f"### ภารกิจพูด\n\n{l['mission']['task']}\n\nตัวอย่าง:\n")
        for x in l['mission']['model']:
            w(f"- {x['en']} · {x['r']}")
        tc = l['teach']
        w('\n### สำหรับผู้สอน (45 นาที)\n')
        for step, mins, desc in d['steps']:
            extra = f" คำถาม: {tc['warm']}" if step == 'อุ่นเครื่อง' else ''
            w(f"- **{step}** ({mins} นาที): {desc}{extra}")
        w(f"\n- การ์ด A: {tc['A']}\n- การ์ด B: {tc['B']}\n")
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print('wrote', sys.argv[1], sum(len(x) for x in o), 'chars')
