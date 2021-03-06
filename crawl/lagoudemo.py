import urllib.request as urllib
from http import cookiejar
from urllib import parse, request

import time
import requests

# 这段爬拉勾的示例是失败的，拉勾有反爬要用下面有预请求的方法
def demo():
    # * 实际的请求地址
    url = r'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'

    # * 拉勾需要先请求这个地址拿到cookie，在放入上面的地址才能获取上面接口中的数据
    url1 = r'https://www.lagou.com/jobs/list_Java/p-city_213?&cl=false&fromSearch=true&labelWords=&suginput='
    
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Java'
    }
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Accept': r'application/json, text/javascript, */*; q=0.01',
        'Referer': r'https://www.lagou.com/jobs/list_Java/p-city_213?px=default',
        'Host': r'www.lagou.com'
    }
    
    req = request.Request(url1, headers=headers, method='POST', data=parse.urlencode(data).encode('utf-8'))
    resp = request.urlopen(req)
    print(resp.read().decode('utf-8'))


def lagou():
    size = 2
    # 预请求（为了拿cookie）
    url1 = r'https://www.lagou.com/jobs/list_Java'
    # ajax请求（实际的请求）
    url = r'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'needAddtionalResult': 'false',
        'px': 'default',
        'city': '佛山'
    }
    url = url + '?' + parse.urlencode(params) # 参数还是放在实际请求上

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': url1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Host': 'www.lagou.com'
    }
    # 通过data来控制翻页
    for page in range(1, size):
        data = {
            'first': 'false',
            'pn': page,
            'kd': 'java'
        }
        s = requests.Session() # 建立session，为了在多次请求中共享cookie
        s.get(url=url1, headers=headers, timeout=3)
        cookie = s.cookies  # 获取cookie
        print(cookie)
        respon = s.post(url=url, headers=headers, data=data, cookies=cookie, timeout=3)
        time.sleep(7)
        # print(respon.text)

        with open('lagoudata.txt', 'w', encoding='utf-8') as f:
            f.write(respon.text)


def proxy_methods():
    # python 使用代理爬数据
    # 代理推荐：西刺免费代理、快代理、代理云
    url = 'http://httpbin.org/ip'

    # * 不使用代理时
    # res = request.urlopen(url)
    # print(res.read())

    # * 使用代理时
    # handler = request.ProxyHandler({'http': '117.88.176.23:3000'})
    # opener = request.build_opener(handler)
    # res = opener.open(url)
    # print(res.read())

    # * requests使用代理
    proxy = {
        'http': '222.95.144.125:3000'
    }
    res = requests.get(url, proxies=proxy)
    print(res.json())


if __name__ == "__main__":
    # demo()
    # lagou()
    proxy_methods()