import os

def list_all(dir, action):
    for dirpath, dirnames, filenames in os.walk(dir):
        action(dirpath)
        for filename in filenames:
            action(dirpath + '\\' + filename)

list_all(r"c:\workspace", print)