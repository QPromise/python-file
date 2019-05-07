import random, threading, time

def tortoise(total_step):
    step = 0
    while step < total_step:
        step += 1
        print('烏龜跑了 {} 步...'.format(step))

def hare(total_step):
    step = 0
    flags = [True, False]
    while step < total_step:
        sleeping = flags[int(random.random() * 10) % 2]
        if sleeping:
            print('兔子睡著了zzzz')
        else:
            step += 2
            print('兔子跑了 {}  步...'.format(step))

t = threading.Thread(target = tortoise, args = (10,))
h = threading.Thread(target = hare, args = (10,))

t.start()
h.start()
