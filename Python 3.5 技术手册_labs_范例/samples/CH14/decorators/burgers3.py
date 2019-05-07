def sidedish(number):
    return {
        1 : lambda meal: (lambda: meal() + 30),
        2 : lambda meal: (lambda: meal() + 40),
        3 : lambda meal: (lambda: meal() + 50),
        4 : lambda meal: (lambda: meal() + 60)
    }.get(number, lambda meal: (lambda: meal()))

@sidedish(2)
@sidedish(3)
def friedchicken():
    return 49.0

print(friedchicken()) #  顯示139.0