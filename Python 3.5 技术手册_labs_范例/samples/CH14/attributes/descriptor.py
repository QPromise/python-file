class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, end = '\n\n')

    def __set__(self, instance, value):
        print(self, instance, value, end = '\n\n')

    def __delete__(self, instance):
        print(self, instance, end = '\n\n')

class Some:
    x = Descriptor()

s = Some()
s.x
s.x = 10
del s.x

Some.x
