'''
深拷贝与浅拷贝
知识点：
1、copy模组
2、深浅拷贝区别
3、python中的赋值语句就是让变量指向同一个地址
4、元组的深浅拷贝都是复制引用，建议不要死记，用id()看看来验证
'''
import copy

def normal_copy():
    a = [11, 22]
    b = a
    b.append(3) # a、b指向的是同一个对象
    print('a ==>', a)
    print('b ==>', b)

def deep_copy():
    a = [11, 22]
    b = copy.deepcopy(a) # 深拷贝
    b.append(3) # a、b指向的是同一个对象
    print('a ==>', a)
    print('b ==>', b)

def shallow_copy():
    # 浅拷贝
    a = [11, 22]
    b = [33, 44]
    c = [a, b]
    d = copy.copy(c) # 这就是浅拷贝
    print(id(d[0]))
    print(id(c[0]))
    
    a.append('gg')

    print(c)
    print(d)

if __name__ == "__main__":
    print("=============== normal_copy ==============")
    normal_copy()
    print("=============== deep_copy ==============")
    deep_copy()
    print("=============== shallow_copy ==============")
    shallow_copy()
    pass