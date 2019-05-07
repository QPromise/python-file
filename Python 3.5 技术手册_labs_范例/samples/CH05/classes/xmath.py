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
        return 'Rational({numer}, {denom})'.format(
            numer = self.numer, denom = self.denom
        )