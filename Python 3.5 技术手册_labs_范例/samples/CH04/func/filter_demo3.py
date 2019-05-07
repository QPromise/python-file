def filter_lt(predicate, lt):
    result = []
    for elem in lt:
        if predicate(elem):
            result.append(elem)
    return result

lt = ['Justin', 'caterpillar', 'openhome']
print('大於 6：', filter_lt(lambda elem: len(elem) > 6, lt))
print('小於 5：', filter_lt(lambda elem: len(elem) < 5, lt))
print('有個 i：', filter_lt(lambda elem: 'i' in elem, lt))