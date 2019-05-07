from collections.abc import MutableMapping

class ChainMap(MutableMapping):
    def __init__(self, *maps):
        self.maps = maps

    def lookup(self, key):
        for m in self.maps:
            if key in m:
                return m
        return None

    def __getitem__(self, key):
        m = self.lookup(key)
        if m:
            return m[key]
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        m = self.lookup(key)
        if m:
             m[key] = value
        else:
            self.maps[key] = value

    def __delitem__(self, key):
        m = self.lookup(key)
        if m:
            del m[key]
        else:
            raise KeyError(key)

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
