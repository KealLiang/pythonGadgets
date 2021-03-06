import requests
from lxml import etree
from urllib import request
from urllib import error
import re
import os

import time
import queue
import threading

'''
    *** 注意，由于CPython解释器存在GIL锁，所以是伪的多线程
    python中
        多线程：适合IO密集型任务（存疑，因为切换线程也有开销）
        多进程：适合cpu密集型任务
'''


# 多线程的方式 begin
class Producer(threading.Thread):
    headers = {
        'Referer': 'https://pos.baidu.com/wh/o.htm?ltr=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }

    # *args 所有的无名称参数
    # *kwargs 所有的有名称参数keyword的缩写
    # 下面的写法就能接收任意的参数
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)  # 传参给父类固定写法
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            res = requests.get(url, headers=self.headers)
            html = etree.HTML(res.text)
            imgs = html.xpath(
                "//div[@class='page-content text-center']//img[@referrerpolicy='no-referrer']")  # 报错invalid predicate表示xpath写错了
            for img in imgs:
                # print(etree.tostring(img))
                img_url = img.get('data-original')
                img_name = img.get('alt')
                suffix = os.path.splitext(img_url)[1]  # 拆出后缀
                name = re.sub(r'[/\?,\.!？，。！]', '', img_name)  # 替换掉特殊字符
                filename = name + suffix
                self.img_queue.put((img_url, filename))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, path, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)  # 传参给父类固定写法
        self.page_queue = page_queue
        self.img_queue = img_queue
        self.path = path

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, filename = self.img_queue.get()
            try:
                request.urlretrieve(img_url, filename=self.path + filename)
                print('%s    下载完成~' % filename)
            except error.HTTPError as e:
                print('URL[ %s ]请求异常： %s' % (img_url, e.msg))
                continue


# 多线程的方式 end


# 单线程的方式 begin
headers = {
    'Referer': 'https://pos.baidu.com/wh/o.htm?ltr=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}


def doutu_pull():
    url = 'http://www.doutula.com/photo/list/?page=1'
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    imgs = html.xpath(
        "//div[@class='page-content text-center']//img[@referrerpolicy='no-referrer']")  # 报错invalid predicate表示xpath写错了
    img_urls = {}
    for img in imgs:
        # print(etree.tostring(img))
        img_url = img.get('data-original')
        img_name = img.get('alt')
        img_urls[img_name] = img_url
    return img_urls


def doutu_save(urls):
    if urls == None:
        return
    for (k, v) in urls.items():
        suffix = os.path.splitext(v)[1]  # 拆出后缀
        name = re.sub(r'[/\?,\.!？，。！]', '', k)  # 替换掉特殊字符
        filename = name + suffix
        try:
            request.urlretrieve(v, filename='crawl/doutu/' + filename)  # 可以直接保存文件的方法
        except error.HTTPError as e:
            print('URL[ %s ]请求异常： %s' % (v, e.msg))
            continue


# 单线程的方式 end

def make_dirs(path):
    if(not os.path.exists(path)):
        os.makedirs(path)

def get_limit():
    while True:
        try:
            limit = int(input("请输入需要下载的表情页数，最大10页："))
            if(limit > 10 or limit < 0):
                print("页数不合法！请重新输入")
            else:
                return limit
        except ValueError:
            print("请输入数字！")

def multi_threads_download(limit):
    path = r'crawl/doutu/'
    make_dirs(path)
    page_queue = queue.Queue(100)
    img_queue = queue.Queue(1000)
    for i in range(limit):
        url = 'http://www.doutula.com/photo/list/?page=' + str(i + 1)
        page_queue.put(url)

    for x in range(max(3, limit)):
        p = Producer(page_queue, img_queue)
        p.start()
    time.sleep(max(3, limit))  # 不在这里睡一下的话，Consumer 里的page_queue和img_queue都是空的直接break了，怀疑是python的 GIL全局解释器锁 造成的（除非page_queue内容够多才能越过）
    for x in range(2):
        c = Consumer(page_queue, img_queue, path)
        c.start()

if __name__ == "__main__":
    print("===== 准备开始下载，耐心等等哦~ =====")
    # 单线程
    # doutu_save(doutu_pull())

    # 多线程
    limit = get_limit()
    multi_threads_download(limit)

