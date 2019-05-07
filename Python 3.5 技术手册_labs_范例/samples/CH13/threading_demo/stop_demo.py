import threading, time

class Some:
    def __init__(self):
        self.is_continue = True

    def terminate(self):
        self.is_continue = False

    def run(self):
        while self.is_continue:
            print('running...running')
        print('bye...bye...')

s = Some()
t = threading.Thread(target = s.run)
t.start()
time.sleep(2)
s.terminate()