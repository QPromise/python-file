class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 實作 __eq__ 與 __hash__ 方法

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(1, 1)
ps = {p1, p2, p3}
print(ps)

p2.x = 1
p2.y = 1
print(ps)

