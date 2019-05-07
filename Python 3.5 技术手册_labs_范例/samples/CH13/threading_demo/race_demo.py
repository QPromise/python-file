import threading

def setTo1(data):
    while True:
        data['Justin'] = 1
        if data['Justin'] != 1:
            raise ValueError('setTo1 資料不一致：{}'.format(str(data)))

def setTo2(data):
    while True:
        data['Justin'] = 2
        if data['Justin'] != 2:
            raise ValueError('setTo2 資料不一致：{}'.format(str(data)))

data = {}

t1 = threading.Thread(target = setTo1, args = (data, ))
t2 = threading.Thread(target = setTo2, args = (data, ))

t1.start()
t2.start()

