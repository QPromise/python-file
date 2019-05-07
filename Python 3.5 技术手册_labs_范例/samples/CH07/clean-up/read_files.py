import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except FileNotFoundError:
        print('找不到檔案', arg)
    else:
        try:
            print(arg, ' 有 ', len(f.readlines()), ' 行 ')
        finally:
            f.close()
