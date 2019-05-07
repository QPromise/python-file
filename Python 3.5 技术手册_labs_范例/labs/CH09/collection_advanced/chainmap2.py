from collections.abc import MutableMapping

class ChainMap(MutableMapping):
    def __init__(self, *maps):
        self.maps = maps

    def lookup(self, key):
        for m in self.maps:
            if key in m:
                return m
        return None

    # 完成未實作之協定

    def keySet(self):
        keys = set()
        for m in self.maps:
            keys.update(m.keys())
        return keys

    def __iter__(self):
        return iter(self.keySet())

    def __len__(self):
        return len(self.keySet())


c = ChainMap({'A' : 'Justin'}, {'A' : 'Monica', 'B' : 'Irene'})
print(list(c))
print(len(c))
print(c.pop('A'))
print(list(c.keys()))
