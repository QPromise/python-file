from multiprocessing import Process, Lock

def f(lock, i):
    lock.acquire()
    try:
        print('hello world', i)
        print('hello world', i + 1)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()