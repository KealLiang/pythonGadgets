import requests
import re
import json
import time
import chardet

host = r'https://m.aniu.com.cn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045109 Mobile Safari/537.36 MMWEBID/2948 MicroMessenger/7.0.10.1580(0x27000A5E) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
    'Referer': 'https://m.aniu.com.cn/superfund/check_account/',
    'Cookie': 'csrftoken=R8f7fEW87ui1PUD6svzuXalpfstLxEih; sessionid=0dpoojlq37f3xwu7l9tmr8taugtfbwl6'
}



def query_fund_info():
    url = r'/superfund/fundassetsdetail/86602/'
    s = requests.Session()
    res = s.get(host + url, headers=headers, timeout=10, verify=False)
    return res.text

def map_fund_result(html):
    # html = '''<p class="info-title">aabbcc</p>
    # <p class="info-title">def</p>
    # '''
    regex = r'<p class="info-title">(.*)</p>'
    ret = re.findall(regex, html)

    # 转换
    fundDict = {}
    if ret != None:
        for s in ret:
            part = s.split(' ')
            fundDict[part[1]] = part[0]
    print(fundDict)

    with open('crawl/aniuchoose.txt', 'w', encoding='utf-8') as fp:
        json.dump(fundDict, fp, ensure_ascii=False)
        # for (k, v) in fundDict.items():
        #     fp.write("%s %s\n" % (k, v))

def get_funds_from_eastmoney():
    """
        从天天基金查基金信息
    """
    fundDict = {}
    with open('crawl/aniuchoose.txt', 'r', encoding='utf-8') as fp:
        fundDict = json.load(fp)
    # 从天天基金拿数据
    host = 'http://fund.eastmoney.com/'
    s = requests.Session()
    for (k, v) in fundDict.items():
        url = host + k + '.html'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'Referer': url
        }
        res = s.get(url, headers=head, timeout=5)
        # print(chardet.detect(res.content)) # 检查网页原本的编码
        time.sleep(1)
        fileName = 'crawl/gentou/funds'+v+'.html'
        with open(fileName, 'w', encoding='utf-8') as fp:
            fp.write(res.content.decode('utf-8'))

def getTimestamp():
    return int(round(time.time() * 1000))

# 阿牛跟投BOSS
def gentou():
    url = host + '/superfund/fundinvest/179792/gentou_invest/'
    tail = '?_=' + str(getTimestamp())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045109 Mobile Safari/537.36 MMWEBID/2948 MicroMessenger/7.0.10.1580(0x27000A5E) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
        'Referer': url,
        'Cookie': 'csrftoken=v5yoaHLGBH3MVLfWnSV7Qp8HwfBRuXOv; sessionid=fzcdwwwdvyhrrkw200g4phm09566zfxq',
        'X-Requested-With': 'XMLHttpRequest' # 重要，加上这行表示异步ajax请求的头后才能返回跟投的数据
    }
    print(url)
    print(url+tail)
    s = requests.session()
    res = s.get(url + tail, headers=headers, timeout=5)
    # 返回的json中 key=lingtou_myfunds 里的就是BOSS投的
    write2File('crawl/gentou.txt', res)

# 跟投招财虎的星光
def gentou2():
    url = host + '/superfund/fundinvest/179809/gentou_invest/1314672/'
    tail = '?_=' + str(getTimestamp())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045109 Mobile Safari/537.36 MMWEBID/2948 MicroMessenger/7.0.10.1580(0x27000A5E) Process/tools NetType/WIFI Language/zh_CN ABI/arm64',
        'Referer': url,
        'Cookie': 'csrftoken=v5yoaHLGBH3MVLfWnSV7Qp8HwfBRuXOv; sessionid=fzcdwwwdvyhrrkw200g4phm09566zfxq',
        'X-Requested-With': 'XMLHttpRequest' # 重要，加上这行表示异步ajax请求的头后才能返回跟投的数据
    }
    print(url)
    print(url+tail)
    s = requests.session()
    res = s.get(url + tail, headers=headers, timeout=5)
    # 返回的json中 key=lingtou_myfunds 里的就是BOSS投的
    write2File('crawl/gentou2.txt', res)
    
def write2File(filename, res):
    time.sleep(1)
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(res.content.decode('utf-8'))

# 把爬下来的原始文件拆为可读的
def readForHumen(filename, tofile, lingtouKey, lingtouFundsFile):
    ret = {}
    lingtou = {}
    with open(filename, 'r') as fp:
        s = json.load(fp)
        lingtou = s[lingtouKey]
        ret = s
        # ret = s.encode('utf-8').decode('unicode_escape') # Unicode转为中文
    with open(tofile, 'w', encoding='utf-8') as fp:
        json.dump(ret, fp, sort_keys=True, indent=2, ensure_ascii=False)
    # 把领头的所选基金挑出来
    lingtoufile = lingtouFundsFile+str(getTimestamp())+'.txt'
    with open(lingtoufile, 'x', encoding='utf-8') as fp:
        json.dump(lingtou, fp, sort_keys=True, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    # html = query_fund_info()
    # map_fund_result(html)
    # get_funds_from_eastmoney()
    # gentou()
    # readForHumen('crawl/gentou.txt', 'crawl/gentou/gentou.cn.txt', 'lingtou_myfunds', 'crawl/gentou/lingtou')
    gentou2()
    readForHumen('crawl/gentou2.txt', 'crawl/gentou/gentou2.cn.txt', 'trade_lingtou_myfunds', 'crawl/gentou/lingtou2.')