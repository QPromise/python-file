import traceback

def dump(src_path, dest_path):
    try:
        with open(src_path, 'rb') as src, open(dest_path, 'wb') as dest:
            dest.write(src.read())
    except:
        with open('exception.log', 'a', encoding='UTF-8') as f:
            traceback.print_exc(file = f)

dump('src.jpg', 'dest.jpg')