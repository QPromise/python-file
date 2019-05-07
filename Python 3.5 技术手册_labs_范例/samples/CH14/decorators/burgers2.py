def sidedish1(meal):
    return lambda: meal() + 30

def sidedish2(meal):
    return lambda: meal() + 40

@sidedish1
@sidedish2
def friedchicken():
    return 49.0

print(friedchicken())   # 顯示119.0