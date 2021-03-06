import threading
import time

'''
创建线程的 方法二
通过继承的方式创建线程，实现run方法
'''
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print("现在是%d号，我的名字叫%s" % (i, self.name))


if __name__ == "__main__":
    t = MyThread()
    t2 = MyThread()
    t.start()
    t2.start()