import urllib
import time
import sys

# from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd

class StockItem:

    def __init__(self):
        print("init")
        self.input_dir="./output"


    def test(self, stock_item):
        url = 'https://m.stock.naver.com/item/main.nhn#/stocks/' + stock_item + '/quarter'
        # html = urlopen(url)


    def get_stock_list(self):
        df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
        return df["종목코드"]


    def save_financial_statements(self, stock_item):
        url = 'http://media.kisline.com/highlight/mainHighlight.nice?nav=1&paper_stock=' + stock_item
        tables = pd.read_html(url)
        df = tables[4]    #개별IFRS 연간 재무제표
        print(df)


        df.to_excel('output.xlsx')