class Resource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(self.name, ' __enter__')
        return self

    def __exit__(self, type, value, traceback):
        print(self.name, ' __exit__')
        return False

with Resource('res') as resource:
    print(resource.name)