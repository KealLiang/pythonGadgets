'''
任务：创建一个自己的可迭代对象
'''
import time
from collections.abc import Iterable
from collections.abc import Iterator

'''
不用继承Iterable的方式实现
知识点：
    1、创建对象，self使用，内置方法
    2、isinstance判断是否有某种能力
    3、raise一个异常来停止迭代：StopIteration
'''
class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_pos = 0

    def add(self, name):
        self.names.append(name)

    # python中认为某个类只要有特定内置方法的实现，就表示这类属于某个特定类
    def __iter__(self):
        return self  # 返回一个迭代器，本例中Classmate自己就是

    def __next__(self):
        time.sleep(0.5)
        if self.current_pos < len(self.names):
            ret = self.names[self.current_pos]
            self.current_pos += 1
            return ret
        else:
            raise StopIteration
        
c = Classmate()
c.add("张三")
c.add("李斯")
c.add("王五")

print("Classmate是否是Iterable：", isinstance(c, Iterable)) # 因为有__iter__(self)
print("Classmate是否是Iterator：", isinstance(c, Iterator)) # 因为有__next__(self)

for name in c:
    print(name)