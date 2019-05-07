def abstract(func):
    func.__isabstract__ = True
    return func

class Abstract(type):

    def __new__(metaclz, clzname, parents, attrs):
        clz = super(metaclz, metaclz).__new__(metaclz, clzname, parents, attrs)

        # 類別上定義的抽象方法
        abstracts = {name for name, value in attrs.items()
                       if getattr(value, "__isabstract__", False)}

        # 從父類別中繼承下來的抽象方法
        for parent in parents:
            for name in getattr(parent, "__abstractmethods__", set()):
                value = getattr(clz, name, None)
                if getattr(value, "__isabstract__", False):
                    abstracts.add(name)

        # 指定給 __abstractmethods__
        clz.__abstractmethods__ = frozenset(abstracts)

        return clz

class AbstractX(metaclass=Abstract):
    @abstract
    def doSome(self):
        pass

# TypeError: Can't instantiate abstract class AbstractX with abstract methods doSome
x = AbstractX()