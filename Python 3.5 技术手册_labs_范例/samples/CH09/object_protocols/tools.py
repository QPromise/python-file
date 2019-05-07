def cycle(elems):
    while True:
        for elem in elems:
            yield elem

class Repeat:
    def __init__(self, elem, n):
        self.elem = elem
        self.n = n

    def __iter__(self):
        elem = self.elem
        n = self.n

        class _Iter:
            def __init__(self):
                self.count = 0

            def __next__(self):
                if self.count < n:
                    self.count += 1
                    return elem
                else:
                    raise StopIteration
					
            def __iter__(self):
                return self

        return _Iter()

for elem in Repeat('A', 5):
    print(elem, end = '')

def repeat(elem, n):
    count = 0
    while count < n:
        count += 1
        yield elem

for elem in repeat('A', 5):
    print(elem, end = '')