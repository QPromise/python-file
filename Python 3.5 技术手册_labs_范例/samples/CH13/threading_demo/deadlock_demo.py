import threading

class Resource:
    def __init__(self, name, resource):
        self.name = name
        self.resource = resource
        self.lock = threading.Lock()

    def action(self):
        with self.lock:
            self.resource += 1
            return self.resource

    def cooperate(self, other_res):
        with self.lock:
            other_res.action()
            print('{} 整合 {} 的資源'.format(self.name, other_res.name))

def cooperate(a, b):
    for i in range(10):
        a.cooperate(b)

res1 = Resource('resource 1', 10)
res2 = Resource('resource 2', 20)

t1 = threading.Thread(target = cooperate, args = (res1, res2))
t2 = threading.Thread(target = cooperate, args = (res2, res1))

t1.start()
t2.start()


