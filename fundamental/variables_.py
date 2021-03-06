# 1、全局变量与局部变量
num = 10
# 全局变量的命名规范
gl_pi = 3.14

def demo1():
    # python不允许函数中直接修改全局变量，除非使用global修饰
    # global num
    num = 999
    print("demo1 ==>", num)

def demo2():
    print("demo2 ==>", num)
    print("theme ==>", theme)
    # print("name ==>", name)

theme = "实验室"

demo1()
demo2()
# 使用在函数调用的下方定已的变量，会报错
name = "小米"

# 2、交换两个变量的值
a = 6
b = 1000
b, a = (a, b) # python中独有的交换两个变量的方法
print("a=%d, b=%d" % (a, b))


# 3、多值函数与拆包
def demo3(*m_tuple, **m_dict):
    print(m_tuple)
    print(m_dict)

v_tuple = (1, 2, 3, 4, 5)
v_dict = {"name": "熊明", "age": 18}

demo3(v_tuple, v_dict)
demo3(*v_tuple, **v_dict)  # 拆包


# python内置变量
print("__name__ ==>", __name__)
