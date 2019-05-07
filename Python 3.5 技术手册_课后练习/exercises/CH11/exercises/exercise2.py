import re

file = input('檔案位置：')
encoding = input('檔案編碼：')

with open(file, encoding=encoding) as f:
    html = ''.join(f.readlines())

with open(file, 'w', encoding=encoding) as f:
    f.write(re.sub(r'<a.+>(<img.+>)</a>', r'\1', html))
