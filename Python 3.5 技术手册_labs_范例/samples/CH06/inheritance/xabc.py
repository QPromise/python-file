from abc import ABCMeta, abstractmethod

class Ordering(metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not (self > other and self == other)

    def __le__(self, other):
        return (not self >= other) or self == other

    def __ne__(self, other):
        return not self == other

