import multiprocessing
# from multiprocessing import Pool # 只需要Pool时可以这样导入
import time
import os
import random

g_distance = 0 # 错误示例：全局变量不能实现进程间的通信！！！

'''
进程使用的资源比线程多，线程比较轻量
进程是资源分配的单位，线程是操作系统调用的单位

知识点：
1、使用multiprocessing创建【多进程】
2、进程间的通信（其实socket也是实现进程间通信的手段之一）
3、进程池
4、os模组的使用（创建文件夹啥的都可以用）
'''
def horse1(q):
    global g_distance
    di = 0
    while True:
        di += 1
        g_distance += di
        addAndPut(q, di)
        print(di, "马儿 %s 跑起来 ε=ε=ε=(~￣▽￣)~" % os.getpid())
        time.sleep(1)

def horse2(q):
    global g_distance
    di = 0
    while True:
        di += 1
        g_distance += di
        addAndPut(q, di)
        print(di, "马儿 %s 跑起来 ε=ε=ε=(~￣▽￣)~" % os.getpid())
        time.sleep(1)

def addAndPut(q, di):
    distance = q.get()
    distance += di
    q.put(distance)

def showDistance(q):
    distance = q.get()
    print("总共跑了：", distance)
    q.put(distance)


def startProcess():
    # 使用队列实现进程间的通信
    q = multiprocessing.Queue()
    distance = 0
    q.put(distance)

    p1 = multiprocessing.Process(target=horse1, args=(q,))
    p2 = multiprocessing.Process(target=horse2, args=(q,))
    p1.start() # 创建进程（复制一份资源，代码不变因此不用复制） 进程 = 代码 + 资源
    p2.start()

    while True:
        # print("总共跑了：", g_distance)
        showDistance(q)
        time.sleep(1)

def worker(tool, i):
    start = time.time()
    print("工人 %s 开始做 %d 号工作，使用工具 %s" % (os.getpid(), i, tool))
    time.sleep(random.random() * 2)
    stop = time.time()
    print("工人 %s 做 %d 号工作总共用了 %0.2f 时间" % (os.getpid(), i, stop - start))

def startProcessWithPool():
    '''
    使用进程池
    使用进程池时，队列使用Manager里的：multiprocessing.Manager().Queue()
    '''
    po = multiprocessing.Pool(3)
    for i in range(10):
        # 每次循环会用空闲出的子进程去调用目标
        po.apply_async(worker, ("扳手", i))

    print("------------- start -------------")
    po.close() # 进程池关闭后不再接收新的请求
    po.join() # 等待po中所有子进程执行完毕，必须在close之后调用（不然会有新的进来）
    print("------------- stop -------------")

if __name__ == "__main__":
    # startProcess()
    startProcessWithPool()