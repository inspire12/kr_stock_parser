import pymysql
import os

from flask_sqlalchemy import SQLAlchemy

class Db:
    def __init__(self):
        print("Db")

    def create_app(self, app):
        app.config.from_object('config')
        app.config['SECRET_KEY'] = 'this is secret'

        user = os.environ['DB_USER']
        password = os.environ['DB_PASSWORD']
        db_name = os.environ["DB_NAME"]
        db_port = os.environ["DB_PORT"]
        db_host = os.environ["DB_HOST"]
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(user, password, db_host, db_name)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:paige12#@13.58.59.206/stock_parser'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        db.init_app(app)
        # app.config.from_object('config.Config')

        return db

    #     self.conn = pymysql.connect(host=db_host, user=user, password=password, db=db_name, charset='utf8', port=int(db_port))
    #     self.curs = self.conn.cursor()
    #
    #
    #
    # def get(self):
    #     table_name = os.environ['DB_TABLE']
    #     sql = "SELECT * from " + table_name
    #     self.curs.execute(sql)
    #     rows = self.curs.fetchall()
    #     for i in rows:
    #         print(i)
    #     self.conn.close()
    #     return rows

