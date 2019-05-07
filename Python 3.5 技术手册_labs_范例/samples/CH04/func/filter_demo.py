def filter_lt(predicate, lt):
    result = []
    for elem in lt:
        if predicate(elem):
            result.append(elem)
    return result

def len_greater_than_6(elem):
    return len(elem) > 6

def len_less_than_5(elem):
    return len(elem) < 5

def has_i(elem):
    return 'i' in elem

lt = ['Justin', 'caterpillar', 'openhome']
print('大於 6：', filter_lt(len_greater_than_6, lt))
print('小於 5：', filter_lt(len_less_than_5, lt))
print('有個 i：', filter_lt(has_i, lt))