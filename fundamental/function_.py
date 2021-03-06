# say_hello() # NameError: name 'say_hello' is not defined


def say_hello(name):
    '''
    打招呼（注释写在函数中首行，函数上方保留2行空行）
    :param name: 名字
    '''
    print('Hello', name)

say_hello('张三')