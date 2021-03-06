from lxml import etree
from bs4 import BeautifulSoup
import re

import json
import csv

'''
解析篇：
1、xpath
2、BeautifulSoup
3、正则

数据结构：
1、json
python中的json与对象转换，使用json模块
json.dump() json -> 对象
json.load() 对象 -> json

2、csv
csv文件类似excel，纯文本，逗号分隔列数据
-- 读
1) csv.reader(fp) 返回一个迭代器，里面是list
2) csv.DictReader(fp) 返回一个迭代器，里面是有序的字典
-- 写
1) csv.writer(fp) 返回一个writer，有操作写行的api
2) csv.DictWriter(fp,header) 同上，注意此方式表头要单独写入writer.writeheader()
'''

def parse_text():
    text = """
    <h3><a name="t4"></a><a name="t4"></a>解决办法：</h3>
    """
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


def parse_baidu_file():
    parser = etree.HTMLParser(encoding='utf-8') # 指定解析器
    htmlElement = etree.parse(r'crawl\baidu.html', parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

def beautiful_soup_demo():
    html = ''
    with open(r'crawl\baidu.html', 'r', encoding='utf-8') as fp:
        html = fp.read()
        # print(html)
    soup = BeautifulSoup(html) # 构建BeautifulSoup对象
    trs = soup.find_all('tr')[1:]  # 过滤掉第一个
    
    # * find和find_all
    for tr in trs:
        # infos1 = list(tr.strings)  # strings获取所有字符，返回的是个生成器
        # print(infos1)
        infos = list(tr.stripped_strings) # stripped_strings获取所有非空白字符
        print(infos)

    # * select选择器（使用css选择器语法）
    a = soup.select('a.toindex')  # 获取所有class为toindex的a标签
    print(a)

def regex_demo():
    text = 'The shirt price is $89.99'
    ret = re.match(r'.*(\$\d+\.?\d*).*', text)
    print(ret.group(1))  # 分组取数，注意group(0)=group() 默认整个字符串外面有个括号
    
    # 使用re.VERBOSE参数，为正则表达式添加注释
    com = re.compile(r"""
        \d+ # 小数点前面的数
        \.? # 小数点本身
        \d* # 小数点后面的数
    """, re.VERBOSE)
    r = re.search(com, text)
    print(r.group())
    


if __name__ == "__main__":
    # parse_baidu_file()
    # beautiful_soup_demo()
    regex_demo()