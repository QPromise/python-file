import pool, threading

class Service: # 模擬服務端
    def __init__(self):
        self.pool =  pool.WorkerThreadPool()

    def accept(self, task):
        self.pool.apply(task)

class Client: # 模擬客戶端
    def __init__(self, service):
        self.service = service

    def run(self):
        while True:
            self.service.accept(lambda: print('執行客戶請求...XD'))

service = Service()
for i in range(5):
    client = Client(service)
    threading.Thread(target = client.run).start()
