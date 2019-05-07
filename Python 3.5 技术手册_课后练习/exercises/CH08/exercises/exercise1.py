import urllib.request

def dump(src, dest):
    with src, dest:
        dest.write(src.read())

dump(
    urllib.request.urlopen('http://openhome.cc'),
    open('index.html', 'wb')
)