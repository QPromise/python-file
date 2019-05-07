import functools

def ascending(a, b): return a - b
def descending(a, b): return -ascending(a, b)

def __select(xs, compare):
    selected = functools.reduce(
        lambda slt, elem: elem if compare(elem, slt) < 0 else slt, xs)
    remain = [elem for elem in xs if elem != selected]
    return (xs if not remain
               else [elem for elem in xs if elem == selected]
                   + __select(remain, compare))

def sorted(xs, compare = ascending):
    '''
    sorted(xs) -> new sorted list from xs' item in ascending order.
    sorted(xs, func) -> new sorted list. func should return a negative integer,
                        zero, or a positive integer as the first argument is
                        less than, equal to, or greater than the second.

    >>> sorted([2, 1, 3, 6, 5])
    [1, 2, 3, 5, 6]
    >>> sorted([2, 1, 3, 6, 5], ascending)
    [1, 2, 3, 5, 6]
    >>> sorted([2, 1, 3, 6, 5], descending)
    [6, 5, 3, 2, 1]
    >>> sorted([2, 1, 3, 6, 5], lambda a, b: a - b)
    [1, 2, 3, 5, 6]
    >>> sorted([2, 1, 3, 6, 5], lambda a, b: b - a)
    [6, 5, 3, 2, 1]
    '''

    return [] if not xs else __select(xs, compare)

if __name__ == '__main__':
    import doctest
    doctest.testmod()