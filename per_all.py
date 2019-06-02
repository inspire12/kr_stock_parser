import urllib
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager

class GetAllByMarketCapitalization:
    def __init__():
        print("init")
        self.input_dir="./output"

    def get_stock():
        # response=urllib2.urlopen("http://m.stock.naver.com/sise/siseList.nhn?menu=market_sum&sosok=0")
        # soup = BeautifulSoup(response)
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
        print(DRIVER_BIN)
        driver = webdriver.Chrome(executable_path = DRIVER_BIN)
        url = 'http://m.stock.naver.com/sise/siseList.nhn?menu=market_sum&sosok=0'
        driver.get(url)
        driver.implicitly_wait(100)
        elem = driver.find_element_by_tag_name("body")
        start_of_pagedowns = 5
        no_of_pagedowns = 70

        #content > div > div.ct_box.dmst_item > div.dmst_lst_wrp > div.u_pg.count._more_btn_wrapper > a > div > span > span
        more = driver.find_elements_by_xpath('//span[@class="u_pg_txt _more_txt"]')[0]
        elem.send_keys(Keys.PAGE_DOWN)
        while start_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            start_of_pagedowns-=1
            print(start_of_pagedowns)

        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            more.click()
            time.sleep(0.1)
            no_of_pagedowns-=1
            print(no_of_pagedowns)

        post_elems = driver.find_elements_by_class_name("_list_wrap")

        for post in post_elems:
            print ("table tr data : " + post.text)
            tr = post.text

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # print(soup)
        result = "".encode('utf-8')
        # result += "■"+soup.find('tr',onclick="nclk('mim.index', '', '', 'http://m.stock.naver.com/sise/siseIndex.nhn?code=KOSPI');").get_text().replace('<br/>','').replace('\n',' ').strip().encode('utf-8')+'\n'
        # result += "□"+soup.find('tr',onclick="nclk('mim.index', '', '', 'http://m.stock.naver.com/sise/siseIndex.nhn?code=KOSDAQ');").get_text().replace('<br/>','').replace('\n',' ').strip().encode('utf-8')+'\n'

        table = soup.find('tbody').find_all('tr')
        print("table data : " + table)
        cnt = 0
        for stock in table:
            result += "▶"+stock.get_text().replace('<br/>','').replace('\n',' ').strip().encode('utf-8')+'\n'
            cnt += 1
            if cnt>5:
                break
        return result
