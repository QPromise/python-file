import sys

keyword = sys.argv[1]
words = sys.argv[2:]

print('{} 出現了 {} 次。'.format(keyword, words.count(keyword)))