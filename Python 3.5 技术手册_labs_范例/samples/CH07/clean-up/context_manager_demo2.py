import sys

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='UTF-8')
        return self.file

    def __exit__(self, type, msg, traceback):
        self.file.close()
        return False

with FileReader(sys.argv[1]) as file:
    for line in file:
        print(line, end='')
