import urllib
import time
import sys
from PyQt4.QtGui import QApplication 
from PyQt4.QtCore import Qurl 
from PyQt4.QtWebKit import QwebPage

# from urllib.request import urlopen
from bs4 import BeautifulSoup

class Client(QwebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QwebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)

    def on_page_load(self):
        self.app.quit()


class StockItem:

    def __init__(self):
        print("init")
        self.input_dir="./output"
#
    def run(self, stockItem):

        url = 'https://m.stock.naver.com/item/main.nhn#/stocks/' + stockItem +'/quarter'
        # html = urlopen(url)
        client_response = Client(url)
        html = client_response.mainFrame().toHtml()
        source = BeautifulSoup(html.read(), "html.parser")
        # 매출액 영업이익 당기순이익 영업이익률 순이익률 ROE 부채비율 당최비율 유보율 EPS BPS 주당배당금 시가배당률 배당성향
        result = source.find_all("div")

        print(result)
