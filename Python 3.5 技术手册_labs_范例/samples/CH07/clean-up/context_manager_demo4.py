import sys
from contextlib import contextmanager

@contextmanager
def suppress(ex_type):
    try:
        yield
    except ex_type:
        pass

with suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')
