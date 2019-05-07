import threading

def setTo1(data, lock):
    while True:
        lock.acquire()
        try:
            data['Justin'] = 1
            if data['Justin'] != 1:
                raise ValueError('setTo1 資料不一致：{}'.format(str(data)))
        finally:
            lock.release()

def setTo2(data, lock):
    while True:
        lock.acquire()
        try:
            data['Justin'] = 2
            if data['Justin'] != 2:
                raise ValueError('setTo2 資料不一致：{}'.format(str(data)))
        finally:
            lock.release()

lock = threading.Lock()
data = {}

t1 = threading.Thread(target = setTo1, args = (data, lock))
t2 = threading.Thread(target = setTo2, args = (data, lock))

t1.start()
t2.start()

