from flask import logging

from api_controller import db


class Stock(db.Model):
    __table_name__ ='stock'

    id = db.Column(db.String(11), primary_key=True)
    name = db.Column(db.String(11))

    market_capitalization = db.Column(db.String(11))
    per = db.Column(db.Float)

    roe_trend = db.Column(db.Float)
    dividend_rate = db.Column(db.Float)


    def __init__(self, id=id, name=name, market_capitalization=market_capitalization
                 , per=per, roe_trend=roe_trend, dividend_rate=dividend_rate):
        self.id = id
        self.name=name
        self.per= per
        self.roe_trend =roe_trend
        self.market_capitalization= market_capitalization
        self.dividend_rate =dividend_rate

    def __repr__(self):
        return 'id : %s' %(self.id)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

