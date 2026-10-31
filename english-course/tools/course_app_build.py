"""course_template.html + course.json -> the published page."""
import json, sys
html = open('course_template.html', encoding='utf-8').read()
data = json.load(open('course.json', encoding='utf-8'))
out = html.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
open(sys.argv[1], 'w', encoding='utf-8').write(out)
print('wrote', sys.argv[1], len(out.encode('utf-8')), 'bytes')
