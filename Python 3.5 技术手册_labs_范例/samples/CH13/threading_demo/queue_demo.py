import threading, queue

def producer(clerk):
    for product in range(10):
        clerk.put(product)
        print('店員進貨 ({})'.format(product))

def consumer(clerk):
    for product in range(10):
        print('店員賣出 ({})'.format(clerk.get()))

clerk = queue.Queue(1);
threading.Thread(target = producer, args = (clerk, )).start()
threading.Thread(target = consumer, args = (clerk, )).start()
