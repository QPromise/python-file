def cycle(elems):
    while True:
        for elem in elems:
            yield elem

class Repeat:
    def __init__(self, elem, n):
        self.elem = elem
        self.n = n

    # 實作 __iter__ 方法

for elem in Repeat('A', 5):
    print(elem, end = '')

def repeat(elem, n):
    count = 0
    while count < n:
        count += 1
        yield elem

for elem in repeat('A', 5):
    print(elem, end = '')