x = 10
def outer():
    x = 100         # 這是在 outer() 函式範圍的 x
    def inner():
        nonlocal x
        x = 1000    # 改變的是 outer() 函式的 x
    inner()
    print(x)        # 顯示 1000

outer()
print(x)           # 顯示 10