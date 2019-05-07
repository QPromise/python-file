import sys

odds = [arg for arg in sys.argv[1:] if int(arg) % 2]
print(odds)