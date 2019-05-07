import sys

def contextmanager(func):
    def wraps(*args, **kwds):
        g = func(*args, **kwds)

        class ContextDecorator:
            def __enter__(self):
                return next(g)

            def __exit__(self, exc_type, exc_val, exc_tb):
                if exc_type:
                    try:
                        g.throw(exc_type, exc_val, exc_tb)
                    except StopIteration:
                        pass
                    return True
                return False

        return ContextDecorator()

    return wraps

def suppress(ex_type):
    try:
        yield
    except ex_type:
        pass

suppress = contextmanager(suppress)

with suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')

def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

closing = contextmanager(closing)

class Some:
    def __init__(self, name):
        self.name = name

    def close(self):
        print(self.name, 'is closed.')


with closing(Some('Resource')) as res:
    print(res.name)
