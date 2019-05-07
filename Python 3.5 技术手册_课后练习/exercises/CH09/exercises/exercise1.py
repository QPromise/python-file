from collections import defaultdict
from collections.abc import MutableMapping

class MultiMap(MutableMapping):
    def __init__(self, *maps):
        self.map = defaultdict(set)
        for m in maps:
            for k in m:
                self.map[k].add(m[k])

    def __getitem__(self, key):
        if key in self.map:
            return self.map[key]
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.map[key].add(value)

    def __delitem__(self, key):
        del self.map[key]

    def __iter__(self):
        return iter(self.map)

    def __len__(self):
        return len(self.map)

    def __str__(self):
        return str(self.map)[len("defaultdict(<class 'set'>, ") :  -1]

mmap = MultiMap({'A' : 'Justin'}, {'A' : 'Monica', 'B' : 'Irene'})
print(mmap) # 顯示 {'B': {'Irene'}, 'A': {'Justin', 'Monica'}}

mmap['B'] = 'Pika'
print(mmap) # 顯示 {'B': {'Irene', 'Pika'}, 'A': {'Justin', 'Monica'}}

