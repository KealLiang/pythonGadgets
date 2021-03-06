import threading
import time

'''
创建线程的 方法一
'''

def saySomething():
    '''
    如果这个函数结束，则运行此函数的线程就结束了
    '''
    for i in range(5):
        print(i, "亲爱的，我是个线程(ง •_•)ง")
        time.sleep(0.5)

def sayHello():
    for i in range(5):
        print(i, "嗯嗯，我也是d=====(￣▽￣*)b")
        time.sleep(0.5)

def main():
    t1 = threading.Thread(target=saySomething)
    t2 = threading.Thread(target=sayHello)

    # printThreading()
    # time.sleep(1)

    t1.start()
    t2.start()

    printThreading2()
    
def printThreading2():
    while True:
        if len(threading.enumerate()) <= 1:
            break
        print(threading.enumerate())
        time.sleep(0.5)

def printThreading():
    print('程序中线程个数：', len(threading.enumerate()))
    for e in threading.enumerate():
        print(e)


if __name__ == "__main__":
    main()