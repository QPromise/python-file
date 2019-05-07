import os, os.path

def list_all(dir, action):
    action(dir)
    for entry in os.scandir(dir):
        fullpath = os.path.join(dir, entry.name)
        if entry.is_dir():
            list_all(fullpath, action)
        elif entry.is_file():
            print(fullpath)

list_all(r"c:\workspace", print)