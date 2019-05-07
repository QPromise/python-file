score = int(input('輸入分數：'))
if score >= 90:
    print('得 A')
elif 90 > score >= 80:
    print('得 B')
elif 80 > score >= 70:
    print('得 C')
elif 70 > score >= 60:
    print('得 D')
else:
    print('不及格')