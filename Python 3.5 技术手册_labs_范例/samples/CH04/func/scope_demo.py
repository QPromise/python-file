x = 10       # 全域

def outer():
    y = 20        # 在 outer() 函式範圍

    def inner():
        z = 30
        print('x = ', x)  # 全域的 x
        print('y = ', y)  # outer() 函式的 y
        print('z = ', z)  # inner() 函式的z

    inner()

    print('x = ', x)      # 全域的 x
    print('y = ', y)      # 全域的 y

outer()
print('x = ', x)          # 全域的 x