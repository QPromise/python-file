class SomeMeta(type):
    def __new__(metaclz, clzname, parents, attrs):
        clz = super(metaclz, metaclz).__new__(
            metaclz, clzname, parents, attrs)
        print('SomeMeta __new__', metaclz, clzname, parents, attrs)
        return clz

    def __init__(clz, clzname, parents, attrs):
        super(__class__, clz).__init__(clzname, parents, attrs)
        print('SomeMeta __init__', clz, clzname, parents, attrs)

Some = SomeMeta('Some', (object,), {'doSome' : (lambda self, x: print(x))})

s = Some()
s.doSome(10)
