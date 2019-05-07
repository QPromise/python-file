import sys
from contextlib import contextmanager

@contextmanager
def file_reader(filename):
    try:
        f = open(filename, 'r')
        yield f
    finally:
        f.close()

with file_reader(sys.argv[1]) as f:
    for line in f:
        print(line, end='')
