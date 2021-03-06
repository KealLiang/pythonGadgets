from selenium import webdriver
import selenium as se
import threading

import time
'''
    selenium的作用：是个机器人，可以默认人在浏览器的操作
    原意是为了自动化测试，爬虫只是衍生功能
    
    功能分类
    1、基本使用
    2、定位元素
    3、操作表单元素
    4、行为链（类似按键精灵）
    5、操作cookie
    6、页面等待 用于不确定元素是否存在时：隐式等待（等待指定时间才抛异常）、显示等待（出现则停止）
        * driver.implicitly_wait(20)
        * WebDriverWait(driver, 20).until( expected_conditions.presence_of_element_located((By.ID, 'idvalue')) )
    7、切换tab页
    8、执行js代码 例如：driver.execute_script("window.open('https://www.douban.com/')") 实现打开新tab页
    9、设置代理
'''

driver_path = r'E:\Learning\ChromDrivers\chromedriver.exe'
# driver_path = r'E:\Learning\ChromDrivers\chromedriver80.0.3987.16.exe'
# driver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver80.0.3987.16.exe'

url = 'http://www.baidu.com/'
driver = webdriver.Chrome(executable_path=driver_path)

def open_and_close(url):
    driver.get(url)
    time.sleep(5)
    driver.close()  # 关闭tab
    # driver.quit() # 退出浏览器

def open_with_selfheader():
    headers = """
        Host: wenshu.court.gov.cn
        Connection: keep-alive
        Pragma: no-cache
        Cache-Control: no-cache
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Referer: http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=bea2d3fd13be8ac4b7262e8bb6c27af6&s8=02
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8
        Cookie: HM4hUBT0dDOn80S=ZjHASQjD36ML79tkJO4PeMc4uimKVSlKGFU1qDRUyZ0CUmk5XGT8Z2ETArodMsgz; SESSION=56b873f9-8900-4769-8a1a-623235a4467a; wzws_cid=bee5440b6c0326b19a1059815e04a5650f807bd92532c5ac13857839155d31fb73f4e33cbc9c24f8c88ad3e5da18230c52df4877c4e751d7b86ff9a6ae8dc284d1d763f10f1cc1817fcd7046b96998b9; HM4hUBT0dDOn80T=4OKsdEx..m2MdYI6SitCCgvB5vjEBl4kDFhgN_UxnFk6a8fJUoCtssAwqXDl.uBnC9Y3hVd4CKBz0AugsLBmphoWaznPFYZCYVczC72aUeKJLb5AWUXz1hFIrav5n1IimO55cmUWEJWnAar4M6q_mrVG8XEtAO9ZDTyWpM8YKCFjqEuojyJiwhDGDaIINx2JAlqbDv7tbeDor1hJ9L4.ZPUYS0zJi4xPXar6HZuTP3P72_98_wvpQdCBfz6rla0XBC9cnzkjfTMAYWjFPHZrQYx9EGsQGObelDkqijOYUuQ61OuxgE4CYJML84IoIUJvZT9xKTynT6rBaWJ6yvtc2exavUnTnbo.7H5KTF3RUOWqHEq
    """
    gov_url = 'http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=bea2d3fd13be8ac4b7262e8bb6c27af6&s8=02'
    options = webdriver.ChromeOptions()
    options.add_argument(headers)
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    browser.get(gov_url)
    time.sleep(500)
    driver.quit()

def find_elements(url):
    '''
        定位元素的方法都有两个版本，带s的返回多个
    '''
    driver.get(url)
    # inputBox = driver.find_element_by_id('kw')
    inputBox = driver.find_element_by_xpath('//input[@id="kw"]')
    inputBox.send_keys('python')
    time.sleep(5)


def new_tab():
    taburl = 'https://www.digitalgx.com.cn/show-29-215-1.html'
    driver.get(url)
    driver.execute_script("window.open('" + taburl + "')")
    print('driver中当前的页面是：%s' % driver.current_url)
    driver.switch_to.window(driver.window_handles[1]) # 浏览器里看到的虽然是新界面，但必须要做这个动作，driver中的焦点才会放到新页面
    print('driver中当前的页面是：%s' % driver.current_url)
    for i in range(1000):
        driver.execute_script("window.location.reload()")
        time.sleep(0.1)

if __name__ == "__main__":
    # print(se.__version__)
    # open_and_close(url)
    # find_elements(url)
    new_tab()
    # open_with_selfheader()
