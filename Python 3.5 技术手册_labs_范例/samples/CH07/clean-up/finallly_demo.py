def test(flag):
    try:
        if flag:
            return 1
    finally:
        print('finally')
    return 0

print(test(True))