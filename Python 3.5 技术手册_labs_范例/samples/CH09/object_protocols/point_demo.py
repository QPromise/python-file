class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, that):
        if hasattr(that, 'x') and hasattr(that, 'y'):
            return self.x == that.x and self.y == that.y
        return False

    def __hash__(self):
        return 41 * (41 + self.x) + self.y

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

