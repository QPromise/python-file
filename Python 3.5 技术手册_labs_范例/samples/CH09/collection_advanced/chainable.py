from collections import UserList

class MthChainList(UserList):
    def for_each(self, action):
        for elem in self:
            action(elem)

    def filter(self, predicate):
        return MthChainList(elem for elem in self if predicate(elem))

    def map(self, mapper):
        return MthChainList(mapper(elem) for elem in self)

lt = MthChainList(['a', 'B', 'c', 'd', 'E', 'f', 'G'])
lt.filter(str.islower).map(str.upper).for_each(print)