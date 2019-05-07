import threading, time

class WorkerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.is_continue = True
        self.task = None
        self.cond = threading.Condition()

    def idle(self):
        return self.task == None

    def apply(self, task):
        with self.cond:
            if self.idle():
                self.task = task
                self.cond.notify()

    def run(self):
        with self.cond:
            while self.is_continue:
                self.cond.wait()
                self.task()
                self.task = None

    def terminate(self):
        self.is_continue = False
        self.apply(WorkerThread.nope)

    @staticmethod
    def nope():
        pass


class WorkerThreadPool:
    def __init__(self):
        self.workers = []
        self.lock = threading.RLock()

    def apply(self, task):
        with self.lock:
            if self.fail_to_allocate(task):
                worker = self.create_worker()
                worker.apply(task)

    def fail_to_allocate(self, task):
        for worker in self.workers:
            if worker.idle():
                worker.apply(task)
                return False
        return True

    def create_worker(self):
        worker = WorkerThread()
        worker.start()
        self.workers.append(worker)
        time.sleep(1) # 給點時間啟動
        return worker

    def clean_idle(self):
        with self.lock:
            for worker in self.workers:
                if worker.idle():
                    self.workers.remove(worker)
                    worker.terminate()

