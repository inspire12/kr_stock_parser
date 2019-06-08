from service.stock_info import StockItem
import os
import sys
from flask import Flask, jsonify, request, make_response, send_from_directory

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

import model.logger

LOG = model.logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'output.log'))


app = Flask(__name__)


view_data = []

@app.route('/data', methods=['POST'])
def set_data():
    stock_parser = StockItem()
    stock_list = stock_parser.get_stock_list()

    for stock in stock_list:
        stock = str(stock).zfill(6)
        print(stock)
        data = stock_parser.get_financial_statements(stock_item=stock)
        print(data)
        view_data.append(data)
        break # test


@app.route('/test', methods=['GET'])
def get_data():
    if len(view_data) == 0:
        set_data()

    return "hello "


@app.errorhandler(404)
def not_found(error):
    """ error handler """
    LOG.error(error)
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run()