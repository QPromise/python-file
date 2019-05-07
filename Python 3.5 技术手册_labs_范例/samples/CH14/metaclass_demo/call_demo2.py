def metafunc(clzname, parents, attrs):
     print(clzname, parents, attrs)
     return type(clzname, parents, attrs)

class Some(metaclass = metafunc):
     def doSome(self):
         print('XD')

