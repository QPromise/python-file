import threading

def producer(clerk):
    for product in range(10):
        clerk.purchase(product)
        print('店員進貨 ({})'.format(product))

def consumer(clerk):
    for product in range(10):
        print('店員賣出 ({})'.format(clerk.sellout()))

class Clerk:
    def __init__(self):
        self.product = -1
        self.cond = threading.Condition()

    def purchase(self, product):
        with self.cond:
            while self.product != -1:
                self.cond.wait()
            self.product = product
            self.cond.notify()

    def sellout(self):
        with self.cond:
            while self.product == -1:
                self.cond.wait()
            p = self.product
            self.product = -1
            self.cond.notify()
            return p

clerk = Clerk();
threading.Thread(target = producer, args = (clerk, )).start()
threading.Thread(target = consumer, args = (clerk, )).start()
