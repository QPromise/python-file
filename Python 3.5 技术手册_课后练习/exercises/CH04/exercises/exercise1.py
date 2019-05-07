from functools import reduce

def toDigits(num):
    return [] if num == 0 else ([num % 10] + toDigits(num // 10))

def isNarcissistic(number):
    digits = toDigits(number)
    return reduce(lambda sum, d: sum + d ** len(digits),
               digits, 0) == number

def narcissistic(n):
    return [i for i in range(1, 10 ** (n if n < 40 else 39))
                  if isNarcissistic(i)]

print(narcissistic(3))