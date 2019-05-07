import sys

number = int(sys.argv[1])
if number % 2:
    print('{} 為奇數'.format(number))
else:
    print('{} 為偶數'.format(number))
