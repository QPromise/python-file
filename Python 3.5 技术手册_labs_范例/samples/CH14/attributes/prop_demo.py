def prop(getter, setter, deleter):
    class PropDesc:
        def __get__(self, instance, owner):
            return getter(instance)
        def __set__(self, instance, value):
            setter(instance, value)
        def __delete__(self, instance):
            deleter(instance)

    return PropDesc()

class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def del_radius(self):
        del self.__radius

    radius = prop(get_radius, set_radius, del_radius)

ball = Ball(10)
print(ball.radius)
ball.radius = 5
print(ball.radius)
