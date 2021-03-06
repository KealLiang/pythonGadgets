'''
GIL: global interpreter lock
全局解释器锁，这东西保证了同一时刻只有一个线程在cpu上执行字节码
使得python中的thread无法将任务映射到物理cpu上
这不是python的问题，是CPython解释器的问题，JPython无此问题

解决办法：
1、使用其他非CPython的编译器
2、使用其他语言编写子线程中的代码，没错，python可以直接加载其他语言的程序来执行，例：
from ctypes import *
from threading import Thread
lib = cdll.LoadLibrary("./libdead_loop.so") # 加载当前目录下的libdead_loop.so
t = Thread(target = lib.Deadloop) # Deadloop是lib中写的方法
t.start() # 此时线程将不再受GIL影响
'''
# 示例：注意，以下程序使用ctrl+C命令只能终止主线程，子线程需要手动杀掉
import threading

def run():
    while True:
        pass

# 子线程中跑一个
t = threading.Thread(target=run)
t.start()

# 主线程中跑一个
while True:
    pass