x = 10

def outer():
    y = 20

    def inner():
        z = 30
        print('inner locals:', locals())

    inner()
    print('outer locals:', locals())

outer()
