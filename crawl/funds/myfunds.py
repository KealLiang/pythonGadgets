import requests
# noinspection PyUnresolvedReferences
from utils import json_util # 导入自定义模块，一般两种方式：1、同级目录直接import 2、想跨目录使用需要安装，放到python安装目录下../Lib/site-packaages中

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Referer': 'http://fund.eastmoney.com/001069.html?spm=search'
}

funds = {
    '501009': '汇添富中证生物科技主题指数A', # 200
    '000878': '中海医药混合A', # 200
    '005911': '广发双擎升级混合', # 200
    '001069': '华泰柏瑞消费成长灵活配置混合', # 200
    '202015': '南方沪深300ETF联接A', # 300 估值策略
    '006087': '华泰柏瑞中证500ETF联接C', # 200
    '000942': '广发中证全指信息技术ETF联接A', # 300 估值策略
    '006140': '广发集嘉债券A', # 银行卡 10
    '270042': '广发纳斯达克100指数A', # 100
    '002450': '平安睿享文娱灵活配置混合A',  # 200
    '161128': '易标普信息科技人民币',  # 100 纳斯达克100 替换停售的广发纳指
    '161903': '万家行业优选组合(LOF)',  # 200
    '006435': '景顺长城创新成长混合',  # 200
    '001938': '中欧时代先锋股票A',  # 200
    '163411': '兴全精选混合' # 200
}

def get_fund_info():
    # url = 'https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&invt=2&ut=267f9ad526dbe6b0262ab19316f5a25b&fields=f3,f12,f14'
    url = 'https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&invt=2&ut=267f9ad526dbe6b0262ab19316f5a25b&fields=f1,f2,f3,f4,f5,f6,f12,f14&secids=0.300601,1.600519,1.603986,0.000661,1.603501,1.600745,1.601658,1.600036,0.300595,0.000858'
    res = requests.get(url, headers=headers)
    with open('temp.txt', 'w', encoding='utf-8') as fp:
        fp.write(json_util.format_json(res.text))
    # print(json_util.format_json(res.text))

if __name__ == "__main__":
    get_fund_info()