import sys

def test():
    raise Exception('Shit happens!')

try:
    test()
except:
    type, value, traceback = sys.exc_info()
    print('例外型態：', type)
    print('例外物件：', value)

    while traceback:
        print('..........')
        code = traceback.tb_frame.f_code
        print('檔案名稱：', code.co_filename)
        print('函式或模組名稱：', code.co_name)

        traceback = traceback.tb_next