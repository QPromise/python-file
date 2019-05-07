text = input('輸入一個字串：')
for letter in text:
    if letter.isupper():
        continue
    print(letter, end='')