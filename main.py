from stock_info import StockItem
print("start")
# print (parser.run("005930"))
# pers = GetAllByMarketCapitalization.get_stock())


def run():
    stock_parser = StockItem()
    stock_list = stock_parser.get_stock_list()

    for stock in stock_list:
        stock = str(stock).zfill(6)
        print(stock)
        stock_parser.save_financial_statements(stock_item=stock)



run()
# from selenium import webdriver
# import time, os
#
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
# print(DRIVER_BIN)
# driver = webdriver.Chrome(executable_path = DRIVER_BIN)
# driver.get('http://codepad.org')
#
# # click radio button
# python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
# python_button.click()
#
# # type text
# text_area = driver.find_element_by_id('textarea')
# text_area.send_keys("print('Hello World')")
#
# # click submit button
# submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
# submit_button.click()
