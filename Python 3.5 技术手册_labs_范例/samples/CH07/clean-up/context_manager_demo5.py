import sys
from contextlib import suppress

with suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')
