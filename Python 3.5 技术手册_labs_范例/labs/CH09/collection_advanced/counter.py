from collections import defaultdict
from operator import itemgetter

def count(text):
    counter = defaultdict(int)
    for c in text:
        counter[c] += 1
    return counter.items()

text = 'Your right brain has nothing left.'
for c, n in sorted(count(text), key = itemgetter(0)):
    print(c, ':', n)