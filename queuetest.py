import queue
import time
import threading


def product(bq):
    str_tuple = ("Python", "Kotlin", "Swift")
    for i in range(99):
        print(threading.current_thread().name + "生产者准备生产元素！")
        time.sleep(0.2)
        bq.put(str_tuple[i % 3])
        print(threading.current_thread().name \
              + "生产者生产元组元素完成")


def consume(bq):
    while True:
        print(threading.current_thread().name + "消费者准备消费元组元素！")
        time.sleep(0.2)
        t = bq.get()
        print(threading.current_thread().name + "消费者消费[ %s ]元素完成！" % t)


bq = queue.Queue(maxsize=1)

threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
# bq = queue.Queue(2)
# bq.put("python")
# bq.put("Python")
# print("Queue was full.")
# bq.put("Swift")
# print("Add Swift!")
