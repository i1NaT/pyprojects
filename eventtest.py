import threading
import time

event = threading.Event()


def cal(name):
    print('%s 启动' % threading.currentThread().getName())
    print('%s 准备开始计算状态' % name)
    event.wait()
    print('%s 收到通知了。' % threading.currentThread().getName())
    print('%s 正式开始计算！' % name)


threading.Thread(target=cal, args=('甲',)).start()
threading.Thread(target=cal, args=('乙',)).start()
time.sleep(2)
print('------------------')
print('主线程发出事件')
event.set()
