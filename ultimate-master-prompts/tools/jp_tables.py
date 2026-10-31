import jp
ROWS = ['あいうえお','かきくけこ','がぎぐげご','さしすせそ','ざじずぜぞ','たちつてと','だぢづでど','なにぬねの','はひふへほ','ばびぶべぼ','ぱぴぷぺぽ','まみむめも','やゆよ','らりるれろ','わを']
YOON = ['きゃ','きゅ','きょ','ぎゃ','ぎゅ','ぎょ','しゃ','しゅ','しょ','じゃ','じゅ','じょ','ちゃ','ちゅ','ちょ','にゃ','にゅ','にょ','ひゃ','ひゅ','ひょ','びゃ','びゅ','びょ','ぴゃ','ぴゅ','ぴょ','みゃ','みゅ','みょ','りゃ','りゅ','りょ']
EXTRA = ['ファ','フィ','フェ','フォ','ティ','ディ','トゥ','ドゥ','ウィ','ウェ','ウォ','ヴァ','ヴィ','ヴ','シェ','ジェ','チェ','ツァ']
def both(k):
    r, s = jp.word_reading(k)
    if k in 'あいうえおをアイウエオヲ':
        return r, s, s
    r2, s2 = jp.word_reading('ほ' + k)
    return r, s, s2.split('-', 1)[1]
def cell(k):
    r, s, ins = both(k)
    return f"{k} {r} {s}" + (f" / {ins}" if ins != s else '')
if __name__ == '__main__':
    for row in ROWS: print(' | '.join(cell(k) for k in row))
    print()
    for i in range(0, len(YOON), 3): print(' | '.join(cell(k) for k in YOON[i:i+3]))
    print()
    print(' | '.join(cell(k) for k in EXTRA))
