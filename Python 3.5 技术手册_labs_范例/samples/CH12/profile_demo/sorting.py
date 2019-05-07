from functools import reduce

def ascending(a, b): return a - b
def descending(a, b): return -ascending(a, b)

def selectionSort(xs, compare = ascending):
    return [] if not xs else __select(xs, compare)

def __select(xs, compare):
    selected = reduce(
        lambda m, k: m if compare(m, k) < 0 else k, xs)
    remain = [elem for elem in xs if elem != selected]
    return (xs if not remain
               else [elem for elem in xs if elem == selected]
                   + __select(remain, compare))

def insertionSort(xs, compare = ascending):
    return ([] if not xs
               else __insert(xs[0],
                   insertionSort(xs[1:], compare), compare))

def __insert(x, xs, compare):
    return ([x] + xs if not xs or compare(x, xs[0]) <= 0
                     else [xs[0]] + __insert(x, xs[1:], compare))

def bubbleSort(xs, compare = ascending):
    return [] if not xs else __up(xs, compare)

def __up(xs, compare):
    if not xs[1:]:
        return xs
    else:
        s = bubbleSort(xs[1:], compare)
        return ([s[0]] + __up([xs[0]] + s[1:], compare)
                    if compare(xs[0], s[0]) > 0
                    else [xs[0]] + s)
