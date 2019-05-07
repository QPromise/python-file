import random

number = 0
while number != 5:
    number = random.randint(0, 9)
    print(number)
    if number == 5:
        print('I hit 5....Orz')
