# from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
from model.dto.stock import Stock
import logging

class StockItem:
    def __init__(self):
        print("init")

    def get_stock_list(self):
        df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
        return df["회사명"], df["종목코드"]

    def get_financial_statements(self, stock_name, stock_item):
        naver_url = "https://finance.naver.com/item/main.nhn?code=" + stock_item
        raw_stock_html = requests.get(naver_url)
        html = raw_stock_html.text
        soup = BeautifulSoup(html, 'html.parser')
        # finance_html = soup.select('div.section.cop_analysis div.sub_section')
        market_capitalization = self._get_market_capitalization(soup)
        shares_count = self._get_shares_count(soup)
        dividend_rate = self._get_dividend_rate(soup)
        bps, net_income, roi_list = self._extract_finanacial_data(stock_item=stock_item)
        # bps = self._get_sales(soup)
        # net_income = 0
        # roi_list = []
        if self.filter_stock(bps, market_capitalization=market_capitalization, shares_count=shares_count):
            return
        # market_capitalization, net_income, roe_list, dividend_rate):
        return Stock(stock_name=stock_name,
                     stock_id=stock_item,
                     market_capitalization=market_capitalization,
                     net_income=net_income,
                     roe_list=roi_list,
                     dividend_rate=dividend_rate)


    def _extract_finanacial_data(self, stock_item):
        try:
            url = 'http://media.kisline.com/highlight/mainHighlight.nice?nav=1&paper_stock=' + stock_item
            tables = pd.read_html(url)
            df = tables[7]  # 기간 재무재표
            data = self._refine_financial_data(df)
            bps = data[14]
            net_income = data[3]
            roi_list = self._get_roi_list(df)
        except:
            # test
            bps=0
            net_income = 0
            roi_list =[]

        return bps, net_income, roi_list


    # 매출
    def _get_sales(self, soup):
        raw_text = soup.find_all("tbody")[2][1][3][0][0]


        print(raw_text)


    def _get_market_capitalization(self, soup):
        raw_text = soup.find('em', id='_market_sum').text
        text = raw_text.strip().replace(",", "").replace("\n","").replace("\t","")

        if "조" in text:
            targets = text.split("조")
            return int(targets[0]) * 10000 + int(targets[1])

        return int(soup.find('em', id='_market_sum').text.strip().replace(",", ""))

    def _get_shares_count(self, soup):
        raw = soup.find_all("div", {"class": "first"})[0].contents[1]
        try:
            shares_count = raw.contents[7].contents[3].find("em").text.replace(",", "")
        except:
            shares_count = 0

        return shares_count

    def _get_dividend_rate(self, soup):
        try:
            dividend_rate = soup.find("em", {"id": "_dvr"}).contents[0]
        except:
            dividend_rate = 0

        return dividend_rate

    def _get_roi_list(self, df):
        data = df.to_dict()
        keys = list(data.keys())
        dict = {}

        for key in keys:
            # print(key[1])
            roe = data[key][9]  # ROE
            dict[key[1]] = roe
        return dict


    # * 주당 순 자산 500억이상 bps
    # * 시가총액 1000억 이상
    # * 상장 주식수 1000만개 이상
    def filter_stock(self, bps, market_capitalization, shares_count):
        if int(bps) < 500:
            print(bps)
            return True
        if int(market_capitalization) < 1000:
            print(market_capitalization)
            return True
        if int(shares_count) < 1000000:
            print(shares_count)
            return True
        return False

    # {0: '매출액(억원)', 1: '영업이익(억원)', 2: '영업이익율(%)', 3: '당기순이익(억원)',
    # 4: '순이익율(%)', 5: '자산총계(억원)', 6: '부채총계(억원)', 7: '자본총계(억원)', 8: '유보율(%)',
    # 9: 'ROE', 10: 'PER', 11: 'PBR', 12: 'PSR', 13: 'EPS(원)', 14: 'BPS(원)',
    # 15: 'SPS(원)', 16: 'EBITDA(억원)', 17: 'EV/EBITDA'}
    def _refine_financial_data(self, df):
        data = df.to_dict()
        keys = list(data.keys())
        # print(data[keys[0]])
        # print(keys[-1])  # 최신
        return data[keys[-1]]
