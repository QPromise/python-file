from functools import total_ordering

@total_ordering
class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __add__(self, that):
        return Rational(
            self.numer * that.denom + that.numer * self.denom,
            self.denom * that.denom
        )

    def __sub__(self, that):
        return Rational(
            self.numer * that.denom - that.numer * self.denom,
            self.denom * that.denom
        )

    def __mul__(self, that):
        return Rational(
            self.numer * that.numer,
            self.denom * that.denom
        )

    def __truediv__(self, that):
        return Rational(
            self.numer * that.denom,
            self.denom * that.denom
        )

    def __str__(self):
        return '{numer}/{denom}'.format(
            numer = self.numer, denom = self.denom
        )

    def __repr__(self):
        return self.__str__()

    def __can_eq__(self, other):
        return hasattr(other, 'numer') and hasattr(other, 'denom')

    def __eq__(self, other):
        return self.__can_eq__(other) and (self.numer * other.denom == self.denom * other.numer)

    def __gt__(self, other):
        return self.__can_eq__(other) and (self.numer / self.denom) > (other.numer / other.denom)

r1 = Rational(1, 2)
r2 = Rational(2, 4)

print(r1 == r2)
print(r1 > r2)
print(r1 <= r2)