# import urllib.request as urllib
from http import cookiejar
from urllib import parse, request
import requests

# 请求的头
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
data = {
    'a': r'1'
}
encoding = 'utf-8'
header = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36')

def demo():
    url = 'http://www.baidu.com'
    # 1 直接请求
    response = request.urlopen(url)
    # 2 包装后请求
    data1 = parse.urlencode(data).encode(encoding)
    request2 = request.Request(url, headers=headers, data=data1)

    # 2.1 cookie处理
    cj = cookiejar.CookieJar() # cookie容器
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    request.install_opener(opener)

    response2 = request.urlopen(request2)

    # 获取状态码
    print('response -->', response.getcode())
    print('response2 -->', response2.getcode())
    print('response2 s page -->\n' + response2.read().decode(encoding))
    print('cookiejar -->', cj)

def download_resource():
    url = r'http://inews.gtimg.com/newsapp_match/0/11136291358/0'
    filename = 'haha.jpg'
    # request.urlretrieve(url, 'haha.jpg') # 服务器有反爬虫，需要添加header，但是urllib里没有相关参数
    # 方法一 另外加头（验证失败，报错too many values to unpack）
    # opener = request.build_opener()
    # opener.addheaders = [header]
    # request.install_opener(opener)
    # request.urlretrieve(url, filename)

    # 方法二 使用urlopen下载
    try:
        req = request.Request(url, headers=headers)
        data = request.urlopen(req).read()
        with open(filename, 'wb') as f:
            f.write(data)
    except Exception as e:
        print(str(e))

def frequently_methods():
    '''
    常用函数
    '''
    # * 编码解码
    qs = parse.urlencode({"name":"老王", "age":18})
    print(qs)
    data = parse.parse_qs(qs)
    print(data)

    print("===============================================================")

    # * url解析
    url = 'http://inews.gtimg.com/newsapp_match/0/11136291358/0;aabbcc?wd=meinv#i'
    result = parse.urlparse(url)
    print(result.scheme)
    print(result.netloc)
    print(result.path)
    print(result.params)
    print(result.query)
    print(result.fragment)  # 锚点
    
    # parse.urlsplit(url) # 这个函数和urlparse基本一样，urlparse多了一个params属性（即上面的 aabbcc 参数）

    print("===============================================================")


def get_live2d_model():
    """
        PoiLive2D – 为你的博客添加一个看板娘 WordPress插件
        来源： https://daidr.me/archives/code-176.html
        由于 1.0.6 版的原插件，live2d/model/pio/里没有model.moc文件，手动爬下来放进去才能显示看板娘
    """
    url = 'https://daidr.me/wp-content/plugins/live2d/live2d/model/pio/model.moc'
    res = requests.get(url)
    with open('model.moc', 'wb') as fp:
        fp.write(res.content)
    

if __name__ == "__main__":
    # demo()
    # download_resource()
    # frequently_methods()
    get_live2d_model()
