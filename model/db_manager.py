import pymysql
from model.private_constants import Constant

class DbManager:

    def get_data(self):
        conn = pymysql.connect(host=Constant.host,
                               user=Constant.user_name,
                               password=Constant.password,
                               db=Constant.db_stock, charset="utf8")
        curs = conn.cursor()

        sql = "select * from stock"
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()
        print(rows)     # 전체 rows

        # Connection 닫기
        conn.close()

    def save_data(self, datas):
        conn = pymysql.connect(host=Constant.host,
                               user=Constant.user_name,
                               password=Constant.password,
                               db=Constant.db_stock, charset="utf8")
        sql = "insert into stock(id,) values (%s, %s, %s)"
        # for data in datas:

