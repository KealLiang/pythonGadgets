'''
知识点：
1、协程 协程(coroutine)的并发实质是利用了程序执行期间的耗时等待时间（例如：io、网络请求等），去做别的事，其实还是单线程任务切换，因此协程开销最小
2、yield的逻辑与应用
3、迭代器、生成器
4、greenlet完成多任务并发（实际是对yield的封装，省略了main的管理）
5、gevent完成多任务并发（实质是对greenlet的封装，特点是遇到延时等待时能立刻切换任务）
6、使用gevent需注意的事项：用time.sleep()等待是无效的，需要使用gevent.sleep()
7、针对第6点，可以通过打补丁的方式避免修改原有代码：monkey.patch_all() # gevent中的monkey
'''
import time


def run1():
    count = 0
    while True:
        time.sleep(0.5)
        print('-----------1-----------', count)
        count += 1
        yield


def run2():
    count = 0
    while True:
        time.sleep(0.5)
        print('-----------2-----------', count)
        count += 1
        yield


if __name__ == "__main__":
    c1 = run1()
    c2 = run2()
    while True:
        next(c1)
        next(c2)
