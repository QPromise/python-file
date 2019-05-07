import sys

name = 'Guest'
if len(sys.argv) > 1:
    name = sys.argv[1]
print('Hello, {}'.format(name))