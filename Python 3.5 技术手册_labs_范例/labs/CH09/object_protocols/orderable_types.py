class Customer:
    def __init__(self, name, symbol, age):
        self.name = name
        self.symbol = symbol
        self.age = age

    # 實作 __lt__ 方法

    def __str__(self):
        return "Customer('{name}', '{symbol}', {age})".format(**vars(self))

    def __repr__(self):
        return self.__str__()

customers = [
    Customer('Justin', 'A', 40),
    Customer('Irene', 'C', 8),
    Customer('Monica', 'B', 37)
]

print(sorted(customers))