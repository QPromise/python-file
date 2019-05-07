from urllib.request import urlopen

def download(url, file):
    with urlopen(url) as url, open(file, 'wb') as f:
        f.write(url.read())

urls = [
    'http://openhome.cc/Gossip/Encoding/',
    'http://openhome.cc/Gossip/Scala/',
    'http://openhome.cc/Gossip/JavaScript/',
    'http://openhome.cc/Gossip/Python/'
]
        
filenames = [
    'Encoding.html',
    'Scala.html',
    'JavaScript.html',
    'Python.html'
]

for url, filename in zip(urls, filenames):
    download(url, filename)
