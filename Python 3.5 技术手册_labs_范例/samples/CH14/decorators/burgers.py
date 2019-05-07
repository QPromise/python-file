def sidedish1(meal):
    return lambda: meal() + 30

@sidedish1
def friedchicken():
    return 49.0

print(friedchicken())    #  顯示 79.0