import sys

words = set(sys.argv[1:])
print('有 {} 個不重複字串：{}'.format(len(words), words))