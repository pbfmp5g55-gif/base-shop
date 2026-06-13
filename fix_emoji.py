# -*- coding: utf-8 -*-
# index.html から BASE非対応の絵文字を除去し、漢字アイコン等に置換する
import io

path = 'index.html'
with io.open(path, encoding='utf-8', newline='') as f:
    s = f.read()

repl = [
    # アイコン絵文字 -> 漢字1字
    ('<span class="lp-badge-icon">❄</span>', '<span class="lp-badge-icon">冷</span>'),  # ❄ 冷
    ('<span class="lp-badge-icon">\U0001F3ED</span>', '<span class="lp-badge-icon">工</span>'),  # 🏭 工
    ('<div class="lp-howto-icon">✋</div>', '<div class="lp-howto-icon">切</div>'),  # ✋ 切
    ('<div class="lp-howto-icon">\U0001F957</div>', '<div class="lp-howto-icon">菜</div>'),  # 🥗 菜
    ('<div class="lp-howto-icon">\U0001F37A</div>', '<div class="lp-howto-icon">酒</div>'),  # 🍺 酒
    ('<div class="lp-howto-icon">\U0001F96A</div>', '<div class="lp-howto-icon">挟</div>'),  # 🥪 挟
    ('<span class="lp-info-icon">❄</span>', '<span class="lp-info-icon">冷</span>'),  # ❄ 冷
    ('<span class="lp-info-icon">\U0001F4C5</span>', '<span class="lp-info-icon">期</span>'),  # 📅 期
    ('<span class="lp-info-icon">\U0001F9CA</span>', '<span class="lp-info-icon">庫</span>'),  # 🧊 庫
    ('<span class="lp-info-icon">\U0001F3ED</span>', '<span class="lp-info-icon">工</span>'),  # 🏭 工
    ('<span class="lp-info-icon">⚠</span>', '<span class="lp-info-icon">注</span>'),  # ⚠ 注
    # カートアイコン(CSS) -> 削除
    ('content:"\U0001F6D2 "', 'content:""'),  # 🛒
]
for a, b in repl:
    assert a in s, 'NOT FOUND: ' + repr(a)
    s = s.replace(a, b)

# グローバル置換
s = s.replace('\U0001F69A ', '')   # 🚚 + 空白 を削除
s = s.replace('▶', '＞')  # ▶ -> ＞(全角)
s = s.replace('→', '＞')  # → -> ＞(全角)
s = s.replace('℃', '度')  # ℃ -> 度
s = s.replace('—', '-')        # — -> -

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print('done')
