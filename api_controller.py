from service.stock_info import StockItem
import os
import sys
import json
from flask import Flask, jsonify, request, make_response, send_from_directory, render_template

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

import model.logger

LOG = model.logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'log/output.log'))


app = Flask(__name__, template_folder="template", static_folder="template")


view_data = []

@app.route('/data', methods=['POST'])
def set_data():
    stock_parser = StockItem()
    stock_name_list, stock_list = stock_parser.get_stock_list()

    for index, stock_id in enumerate(stock_list):
        print("progress {0}/{1}".format(index, len(stock_list)))
        stock = str(stock_id).zfill(6)
        print(stock)
        data = stock_parser.get_financial_statements(stock_name = stock_name_list[index], stock_item=stock)
        print(data)
        if data != None:
            view_data.append(data)

        # if index > 10:
        #     break
        # break # test


@app.route('/', methods=['GET'])
def get_data():
    if len(view_data) == 0:
        # stock_id = 183350
        # stock_parser = StockItem()
        # data = stock_parser.get_financial_statements(stock_name = "피에스케이", stock_item=str(stock_id).zfill(6))
        # if data != None:
        #     view_data.append(data)
        set_data()

    return render_template('index.html', view_data=json.dumps(view_data, default=lambda x: x.__dict__))



@app.errorhandler(404)
def not_found(error):
    """ error handler """
    LOG.error(error)
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0')