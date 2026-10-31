"""Build the practice app page: app_template.html + the checked phrase data."""
import json, sys
from app_data import build_data

out = sys.argv[1] if len(sys.argv) > 1 else 'practice-app.html'
html = open('app_template.html', encoding='utf-8').read()
data = json.dumps(build_data(), ensure_ascii=False, separators=(',', ':'))
open(out, 'w', encoding='utf-8').write(html.replace('__DATA__', data))
print('wrote', out)
