class classmth:
    def __init__(self, mth):
        self.mth = mth

    def __get__(self, instance, owner):
        def wrapper(*arg, **kwargs):
            return self.mth(owner, *arg, **kwargs)
        return wrapper

class Other:
    @classmth   # 相當於 doIt = classmth(doIt)
    def doIt(clz, a, b):
        print(clz, a, b)

Other.doIt(1, 2)  # 相當 Other.__dict__['doIt'].__get__(None, Other)(1, 2)
o = Other()
o.doIt(1, 2)      # 相當 Other.__dict__['doIt'].__get__(o, Other)(1, 2)