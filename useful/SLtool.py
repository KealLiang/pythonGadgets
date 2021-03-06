import shutil
from time import localtime
from time import strftime
import os

def copy(source, target):
    if not os.path.exists(source):
        print("源目录不存在！")
        return
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)

def getNow():
    t = strftime('%m%d%H%M%S', localtime())
    return t

def main():
    save = 'C:\\Users\\lsrmo\\AppData\\LocalLow\\Nolla_Games_Noita\\save00'
    back = 'E:\\backup\\game\\noita_backup'
    while True:
        op = input("请输入您的操作（1 save  2 load  3 exit）：")
        if '1' == op:
            copy(save, back)
            print("存档完毕！")
        elif '2' == op:
            copy(back, save)
            print("读档完毕！")
        elif '3' == op:
            print("退出！")
            break
        else:
            print("输入有误！")

if __name__ == "__main__":
    main()