class sidedish1:
    def __init__(self, clz):
        self.clz = clz

    def __call__(self):
        class SideDishOne:
            def __init__(self, meal):
                self.meal = meal
            def getContent(self):
                return self.meal.getContent() + " | 可樂 | 薯條"
            def price(self):
                return self.meal.price() + 30.0

        return SideDishOne(self.clz())

@sidedish1
class FriedChicken:
    def getContent(self):
        return "不黑心炸雞"
    def price(self):
        return 49.0

friedchicken = FriedChicken()
print(friedchicken.getContent())   # 不黑心炸雞 | 可樂 | 薯條
print(friedchicken.price())        # 79.0