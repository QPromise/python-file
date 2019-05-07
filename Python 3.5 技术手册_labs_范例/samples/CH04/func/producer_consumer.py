import sys
import random

def producer():
    while True:
        data = random.randint(0, 9)
        print('生產了：', data)
        yield data

def consumer():
    while True:
        data = yield
        print('消費了：', data)

def clerk(jobs, producer, consumer):
    print('執行 {} 次生產與消費'.format(jobs))
    p = producer()
    c = consumer()
    next(c)  # 第一次觸發 consumer 產生器
    for i in range(jobs):
        data = next(p)
        c.send(data)

clerk(int(sys.argv[1]), producer, consumer)
