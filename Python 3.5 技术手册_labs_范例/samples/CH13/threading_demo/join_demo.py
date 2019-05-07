import threading

def demo():
    print('Thread B 開始...')
    for i in range(5):
        print('Thread B 執行...')
    print('Thread B 將結束...')
 
print('Main thread 開始...')
tb = threading.Thread(target = demo)
tb.start()
tb.join(); # Thread B 加入 Main thread 流程

print('Main thread 將結束...')
