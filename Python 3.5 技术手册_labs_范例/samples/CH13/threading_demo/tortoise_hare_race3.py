import random, threading, time

class Tortoise(threading.Thread):
    def __init__(self, total_step):
        super().__init__()
        self.total_step = total_step

    def run(self):
        step = 0
        while step < self.total_step:
            step += 1
            print('烏龜跑了 {} 步...'.format(step))

class Hare(threading.Thread):
    def __init__(self, total_step):
        super().__init__()
        self.total_step = total_step

    def run(self):
        step = 0
        flags = [True, False]
        while step < self.total_step:
            sleeping = flags[int(random.random() * 10) % 2]
            if sleeping:
                print('兔子睡著了zzzz')
            else:
                step += 2
                print('兔子跑了 {}  步...'.format(step))

Tortoise(10).start()
Hare(10).start()

