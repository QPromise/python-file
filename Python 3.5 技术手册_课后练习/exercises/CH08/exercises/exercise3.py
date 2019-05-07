import sys

def dump(src, dest):
    with src, dest:
        dest.write(src.read())

src_path = sys.argv[1]
encoding = sys.argv[2]
dest_path = sys.argv[3]

dump(
    open(src_path, 'r', encoding=encoding),
    open(dest_path, 'w', encoding='UTF-8')
)