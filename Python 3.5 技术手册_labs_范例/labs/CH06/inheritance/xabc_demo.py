class Ball:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return hasattr(other, 'radius') and self.radius == other.radius

    def __gt__(self, other):
        return hasattr(other, 'radius') and self.radius > other.radius

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not (self > other and self == other)

    def __le__(self, other):
        return (not self >= other) or self == other

    def __ne__(self, other):
        return not self == other

b1 = Ball(10)
b2 = Ball(20)
b3 = Ball(10)

print(b1 > b2)
print(b1 <= b2)
print(b1 == b2)

