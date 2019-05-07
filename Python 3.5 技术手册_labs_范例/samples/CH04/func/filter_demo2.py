def filter_lt(predicate, lt):
    result = []
    for elem in lt:
        if predicate(elem):
            result.append(elem)
    return result

def len_greater_than(num):
    def len_greater_than_num(elem):
        return len(elem) > num
    return len_greater_than_num

lt = ['Justin', 'caterpillar', 'openhome']
print('大於 5：', filter_lt(len_greater_than(5), lt))
print('大於 7：', filter_lt(len_greater_than(7), lt))