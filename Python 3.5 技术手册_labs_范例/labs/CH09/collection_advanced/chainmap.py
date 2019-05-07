class ChainMap:
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


c = ChainMap({'A' : 'Justin'}, {'A' : 'Monica', 'B' : 'Irene'})
print(c.maps)

print(c['A'])

c['A'] = 'caterpillar'
print(c.maps)

del c['A']
print(c.maps)