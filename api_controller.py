from service.stock_info import StockItem
import os
import sys
import json
from os import getpid
from flask import Flask, jsonify, request, make_response, send_from_directory, render_template
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

import model.logger

LOG = model.logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'log/output.log'))

# app.secret_key = os

app = Flask(__name__, template_folder="template", static_folder="template")

view_data = []
cors = CORS(app, resources={
    r"/rows/*": {"origin": "*"},
    r"/api/*": {"origin": "*"},
})

# db = db_manager.create_app(app)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'this is secret'

user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
db_name = os.environ["DB_NAME"]
db_port = os.environ["DB_PORT"]
db_host = os.environ["DB_HOST"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(user, password, db_host, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
# app.config.from_object('config.Config')

@app.route('/rows', methods=['GET'])
def test_data():
    if len(view_data) == 0:
        set_data()
    response = app.response_class(
        response=json.dumps(view_data, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/data', methods=['POST'])
def set_data():
    from model.entity.stock import Stock
    stock_parser = StockItem()
    stock_name_list, stock_list = stock_parser.get_stock_list()

    for index, stock_id in enumerate(stock_list):
        print("progress {0}/{1}".format(index, len(stock_list)))
        stock = str(stock_id).zfill(6)
        print(stock)
        data = stock_parser.make_financial_statements(stock_name=stock_name_list[index], stock_item=stock)

        print(data)
        if data != None:
            view_data.append(data)




@app.route('/save', methods=['POST'])
def save_db():
    from model.entity.stock import Stock
    stock_parser = StockItem()
    stock_name_list, stock_list = stock_parser.get_stock_list()

    for index, stock_id in enumerate(stock_list):
        print("progress {0}/{1}".format(index, len(stock_list)))
        stock = str(stock_id).zfill(6)
        print(stock)
        data = stock_parser.make_financial_statements(stock_name=stock_name_list[index], stock_item=stock)
        db.create_all() # In case user table doesn't exists already. Else remove it.

        print(data)
        if data != None:
            view_data.append(data)
            db.session.add(data)
            db.session.commit() # This is needed to write the changes to database
            Stock.query.all()


@app.route('/', methods=['GET'])
def get_data():
    if len(view_data) == 0:
        set_data()

    return render_template('index.html', view_data=json.dumps(view_data, default=lambda x: x.__dict__))


@app.errorhandler(404)
def not_found(error):
    """ error handler """
    LOG.error(error)
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    fh = open("application.pid", "w")
    fh.write(str(getpid()))
    fh.close()
    app.run(host='0.0.0.0', port=5010)
