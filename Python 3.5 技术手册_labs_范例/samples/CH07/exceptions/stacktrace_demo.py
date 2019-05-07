def a():
    text = None
    return text.upper()

def b():
    a()

def c():
    b()

try:
    c()
except:
    import traceback
    traceback.print_last()
