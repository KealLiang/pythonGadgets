import math

def main():
    '''
    打包命令： pyinstaller -F -i 图标.ico io_.py
    '''
    upper = None
    try:
        upper = int(input("请输入需要生成几以内的质数："))
    except Exception:
        input("对不起，请输入数字！")
    writePrime(upper)
    input("生成完成，请查看 存储质数.txt")

def writePrime(upper):
    filename = '存储质数.txt'
    content = []
    for i in range(1, upper + 1):
        if isPrime(i):
            content.append(i)
    # 打开并写入
    # with as打开不用手动关
    with open(filename, 'w', encoding='utf-8') as f:
        print_2_file(f, upper, content)

def isPrime(i):
    for j in range(2, math.floor(i / 2) + 1):
        if i % j == 0:
            return False
    return True

def print_2_file(f, upper, content):
    f.write('%s里总共有%s个质数\n' % (str(upper), str(len(content))))
    for i in range(len(content)):
        if i % 20 == 0:
            f.write('\r\n')
        f.write('\t' + str(content.pop(0)))

def open_and_print(filename):
    '''
    打开传入的文件并处理异常
    '''
    content = None # 因为下面要用if判断，所以必须在开头就定义，否则文件打开失败时会异常（因为打开失败时content未定义）
    try:
        f = open(filename, 'rb')
        content = f.read()
        f.close()
    except Exception as e:
        e.with_traceback()
        print('文件%s打开失败' % filename)
    # 打印文件内容
    if content:
        print(content.decode())


if __name__ == "__main__":
    main()