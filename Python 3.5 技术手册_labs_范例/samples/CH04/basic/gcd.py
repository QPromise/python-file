print('輸入兩個數字...')

m = int(input('數字 1: '))
n = int(input('數字 2: '))

while n != 0:
   r = m % n
   m = n
   n = r
   if m == 1:
       print('互質')
       break
else:
    print("最大公因數：", m)