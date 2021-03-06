import time
import threading

g_sum = 0
mutex = threading.Lock() # 拿到一个锁
'''
知识点：
1、获取当前线程对象 threading.current_thread()
2、创建线程对象时传参 threading.Thread(target=add1, args=(1000000,))
3、互斥锁的获取，加锁与释放
'''
def add1(num):
    global g_sum
    for i in range(num):
        mutex.acquire() # 加锁
        g_sum += 1      # 操作临界区
        mutex.release() # 释放锁
    print("线程%s中的总数为：%d" % (threading.current_thread().getName(), g_sum))

def add2(num):
    global g_sum
    for i in range(num):
        mutex.acquire()
        g_sum += 1
        mutex.release()
    print("线程%s中的总数为：%d" % (threading.current_thread().getName(), g_sum))

if __name__ == "__main__":
    t1 = threading.Thread(target=add1, args=(1000000,))
    t2 = threading.Thread(target=add2, args=(1000000,))
    t1.start()
    t2.start()

    time.sleep(2)
    print("总数为：", g_sum)