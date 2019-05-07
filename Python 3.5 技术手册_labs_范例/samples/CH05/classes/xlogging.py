class Logger:
    __loggers = {}
    def __new__(clz, name):
        if name not in clz.__loggers:
            logger = object.__new__(clz)
            clz.__loggers[name] = logger
            return logger
        return clz.__loggers[name]

    def __init__(self, name):
        if name not in vars(self):
            self.name = name

    def log(self, message):
        print('{name}: {message}'.format(name = self.name, message = message))

