import cProfile
import sorting
import random

l = list(range(500))
random.shuffle(l)
cProfile.run('sorting.selectionSort(l)')