class SomeMeta(type):
    def __call__(clz, *args, **kwargs):
        print('call __new__')
        instance = clz.__new__(clz, *args, **kwargs)
        print('call __init__')
        clz.__init__(instance, *args, **kwargs)
        return instance

class Some(metaclass = SomeMeta):
    def __new__(clz):
        print('Some __new__')
        return object.__new__(clz)

    def __init__(self):
        print('Some __init__')

s = Some()