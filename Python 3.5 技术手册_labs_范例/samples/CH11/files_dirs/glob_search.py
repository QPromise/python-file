import sys, os, glob

try:
    path = sys.argv[1]
    pattern = sys.argv[2]
except IndexError:
    print('請指定搜尋路徑與 glob 模式')
    print('例如：python glob_search.py c:\workspace **/*.py')
else:
    os.chdir(path)
    for p in glob.iglob(pattern, recursive = True):
        print(p)
