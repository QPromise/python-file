import sys
from contextlib import contextmanager

class Suppress:
    def __init__(self, ex_type):
        self.ex_type = ex_type

    def __enter__(self):
        return None

    def __exit__(self, ex_type, msg, traceback):
        if ex_type == self.ex_type:
            return True
        return False

with Suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')
