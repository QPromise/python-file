def map_lt(mapper, lt):
    result = []
    for ele in lt:
        result.append(mapper(ele))
    return result

lt = ['Justin', 'caterpillar', 'openhome']
print(map_lt(str.upper, lt))
print(map_lt(len, lt))