def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

print('輸入兩個數字...')

m = int(input('數字 1: '))
n = int(input('數字 2: '))

r = gcd(m, n)
if r == 1:
    print('互質')
else:
    print("最大公因數：", r)