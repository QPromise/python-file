import sys

for arg in sys.argv[1:]:
    try:
        with open(arg, 'r') as f:
            print(arg, ' 有 ', len(f.readlines()), ' 行 ')
    except FileNotFoundError:
        print('找不到檔案', arg)

