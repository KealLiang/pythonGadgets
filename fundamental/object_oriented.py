'''
知识点：
1、python中的封装、继承、多态
2、python中变量的可见性（通过命名区分）
    x : 共有变量
    _x : 防止import导入，私有化的属性或方法，from module import * 禁止导入，类对象和子类可以访问
    __x : 私有变量，避免与子类中的属性命名冲突，无法在外部直接访问（名字重整所以访问不到）
    __x__ : 用户名字空间的魔法对象或者属性（换言之内建变量、初始变量）
    x_ : 用来避免冲突
3、name mangling 名字重整，通过此机制可以访问private
4、import的搜寻顺序
5、运行时重新import模组：from imp import reload 调用reload()方法可重新加载包
6、from my_module import XX 本质是在本模组中定义一个叫XX的变量，对XX重新赋值，其实是改变XX的指向，my_module.XX中的值不会改变！
7、python支持多继承
    Parent.__init__()和super().__init__()不一样，使用super()时会去__mro__中找父亲
    MyClass.__mro__中有个元组，按顺序，当前类的下一个类就是super将要调用的父类
    只有多继承时super()指向才有所不同

8、类对象，实例对象
9、类方法，实例方法，静态方法
10、属性方法（类似 VUE 中的 计算属性(computed)）

11、魔法属性
12、对象切片（__getslice__, __setslice__, __delslice__） 是的，切片可以放在等号左边来赋值
13、with关键字本质是用于管理上下文的（实现了__enter__, __exit__的对象都能用with，多用于管理资源，如io、socket等）
    了解用于方法上的装饰注解： @contextmanager
'''

import sys
from imp import reload

def import_search_order():
    print("sys.path这个列表中的顺序就是import找模组的顺序，包找不到时，直接往里插入路径即可")
    for p in sys.path:
        print(p)


class Foo(object):
    def __init__(self, name):
        self.name = name
    
    def obj_func(self):
        print("实例方法，类对象不能调用，只能实例对象调")

    @classmethod
    def class_func(cls):
        print("类方法，与实例方法的区别主要是传递的形参引用不一样，主要用于修改类属性")

    @staticmethod
    def static_func():
        print("静态方法，不传参数")

    @property
    def prop(self):
        return "属性方法，必须返回一个值，调用时不需要括号"

    # python3中才有这种写法
    @prop.setter
    def setProp(self, value):
        pass

    @prop.deleter
    def deleteProp(self):
        pass

    # python2中为属性添加setter和deleter及描述的方法
    BAR = property(prop, setProp, deleteProp, "description...")


if __name__ == "__main__":
    reload(sys)
    import_search_order()
    pass