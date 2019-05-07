def len_greater_than(num):
    def len_greater_than_num(elem):
        return len(elem) > num
    return len_greater_than_num

lt = ['Justin', 'caterpillar', 'openhome']
print(list(filter(len_greater_than(6), lt)))
print(list(map(len, lt)))