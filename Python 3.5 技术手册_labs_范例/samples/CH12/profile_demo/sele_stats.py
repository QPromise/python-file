import cProfile, pstats, random, sorting

l = list(range(500))
random.shuffle(l)
cProfile.run('sorting.selectionSort(l)', 'select_stats')

p = pstats.Stats('select_stats')
p.strip_dirs().sort_stats('name').print_stats()
p.sort_stats('cumulative').print_stats(10)
p.sort_stats('time').print_stats(10)