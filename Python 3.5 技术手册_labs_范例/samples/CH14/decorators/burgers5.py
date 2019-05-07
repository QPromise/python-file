class sidedish1:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        return self.func() + 30

@sidedish1
def friedchicken():
    return 49.0

print(friedchicken())    #   79.0