import sys

def my_excepthook(type, value, traceback):
    print('例外型態：', type)
    print('例外物件：', value)

    while traceback:
        print('..........')
        code = traceback.tb_frame.f_code
        print('檔案名稱：', code.co_filename)
        print('函式或模組名稱：', code.co_name)

        traceback = traceback.tb_next

sys.excepthook = my_excepthook

def test():
    raise Exception('Shit happens!')

test()