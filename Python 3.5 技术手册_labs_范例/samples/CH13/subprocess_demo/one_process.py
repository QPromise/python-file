import sys

def foo(filename):
    with open(filename) as f:
        text = f.read()
		
    ct = 0
    for ch in text:
        n = ord(ch.upper()) + 1
        if n == 67:
            ct += 1
    return ct

count = 0
for filename in sys.argv[1:]:
    count += foo(filename)

print(count)
