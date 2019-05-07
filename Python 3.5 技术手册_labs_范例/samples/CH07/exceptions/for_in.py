def for_in(iterable, do_it):
    iterator = iter(iterable)
    try:
        while True:
            do_it(next(iterator))
    except StopIteration:
        pass

for_in([10, 20, 30], print)

