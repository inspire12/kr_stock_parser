class Stock:
    def __init__(self, stock_name, stock_id, market_capitalization, net_income, roe_list, dividend_rate):
        self.stock_name = stock_name
        self.stock_id = stock_id
        self.market_capitalization = market_capitalization
        self.per = self.get_per(market_capitalization, net_income)
        self.roe_list = roe_list # list
        self.dividend_rate =dividend_rate


    def get_per(self, 시가총액, 당기순이익):
        return int(시가총액)/ int(당기순이익)