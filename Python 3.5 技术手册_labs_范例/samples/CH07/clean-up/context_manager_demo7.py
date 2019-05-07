from contextlib import closing

class Some:
    def __init__(self, name):
        self.name = name

    def close(self):
        print(self.name, 'is closed.')

with closing(Some('Resource')) as res:
    print(res.name)