total = 0
count = 0

while True:
    number_str = ''
    try:
        number_str = input('輸入數字（0 結束）：')
        number = int(number_str)
        if number == 0:
            break
        else:
            total += number
            count += 1
    except ValueError as err:
        print('非整數的輸入', number_str)

print('平均', total / count)
