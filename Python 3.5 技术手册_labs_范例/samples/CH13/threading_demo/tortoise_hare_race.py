import random

flags = [True, False]
total_step = 10
tortoise_step = 0
hare_step = 0

print('龜兔賽跑開始...')
while tortoise_step < total_step and hare_step < total_step:
    tortoise_step += 1
    print('烏龜跑了 {}  步...'.format(tortoise_step))
    sleeping = flags[int(random.random() * 10) % 2]
    if sleeping:
        print('兔子睡著了zzzz')
    else:
        hare_step += 2
        print('兔子跑了 {}  步...'.format(hare_step))

