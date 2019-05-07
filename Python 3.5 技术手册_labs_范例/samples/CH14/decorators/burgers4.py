def sidedish1(clz):
    class SideDishOne:
        def __init__(self):
            self.meal = clz()

        def getContent(self):
            return self.meal.getContent() + " | 可樂 | 薯條"

        def price(self):
            return self.meal.price() + 30.0

    return SideDishOne

@sidedish1
class FriedChicken:
    def getContent(self):
        return "不黑心炸雞"
    def price(self):
        return 49.0

friedchicken = FriedChicken()
print(friedchicken.getContent())   # 不黑心炸雞 | 可樂 | 薯條
print(friedchicken.price())        # 79.0