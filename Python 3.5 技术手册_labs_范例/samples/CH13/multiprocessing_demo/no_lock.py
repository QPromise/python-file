from multiprocessing import Process, Lock

def f(i):
    print('hello world', i)
    print('hello world', i + 1)

if __name__ == '__main__':
    for num in range(100):
        Process(target=f, args=(num, )).start()