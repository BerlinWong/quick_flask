import json

import pandas as pd
from flask import request, jsonify
from flask_cors import CORS

from models.models import AllSzShStock
from templates.based_on_bao_stock import BaoStock
from utils.common_crud import BaseSQL
from utils.response.json_flask import JsonFlask
from utils.response.json_response import JsonResponse

# app = Flask(__name__)

app = JsonFlask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 给前端charts绘制K线返回dict数据
@app.route('/get_k_line_dataset_normal', methods=['POST'])
def get_k_line_dataset_normal():
    data = json.loads(request.get_data())
    stock = data.get('stock')
    start_date = data.get('begin')
    end_date = data.get('end')
    print(stock, start_date, end_date)
    bbs = BaoStock(stock, start_date, end_date)
    res = bbs.processing()
    res["open"] = res["open"].astype(float)
    res["close"] = res["close"].astype(float)
    res["low"] = res["low"].astype(float)
    res["high"] = res["high"].astype(float)
    res["volume"] = res["volume"].astype(float)
    jdata = res.to_json(orient='records', force_ascii=False)
    final_res = json.loads(jdata)
    return final_res


# 原先准备给charts绘制K线返回快捷数据的，后改成了dict形式，此接口作废
@app.route('/get_k_line_dataset_v_c', methods=['POST'])
def get_k_line_dataset_v_c():
    data = json.loads(request.get_data())
    stock = data.get('stock')
    start_date = data.get('begin')
    end_date = data.get('end')
    bbs = BaoStock(stock, start_date, end_date)
    res = bbs.processing()
    res = res.drop(['code', 'preclose'], axis=1)
    # res['date'] = pd.to_datetime(res['date'])
    res["open"] = res["open"].astype(float)
    res["close"] = res["close"].astype(float)
    res["low"] = res["low"].astype(float)
    res["high"] = res["high"].astype(float)
    res["volume"] = res["volume"].astype(float)
    return res.to_numpy().tolist()

# 获取所有股票ID
@app.route('/get_all_stock_by_szorsh', methods=['POST'])
def get_all_stock_by_szorsh():
    data = request.get_json()
    basesql = BaseSQL()
    if data == 'sh':
        query_response = basesql.base_select(AllSzShStock, flag='sh')
    elif data == 'sz':
        query_response = basesql.base_select(AllSzShStock, flag='sz')
    else:
        query_response = basesql.base_select(AllSzShStock)
    response_list = []
    for item in query_response:
        response_list.append({
            'stock': item.code,
            'stock_name': item.stock_name,
            'splicing': item.code + '.'+item.flag + ' ## ' + item.stock_name
        })
    basesql.close_session()
    return response_list


# 获取所有建议的股票ID
@app.route('/get_all_stock_by_szorsh_ws', methods=['POST'])
def get_all_stock_by_szorsh_ws():
    data = request.get_json()
    basesql = BaseSQL()
    if data == 'sh':
        query_response = basesql.base_select(AllSzShStock, flag='sh', suggestion=1)
    elif data == 'sz':
        query_response = basesql.base_select(AllSzShStock, flag='sz', suggestion=1)
    else:
        query_response = basesql.base_select(AllSzShStock, suggestion=1)
    response_list = []
    for item in query_response:
        response_list.append({
            'stock': item.code,
            'stock_name': item.stock_name,
            'splicing': item.code + '.'+item.flag + ' ## ' + item.stock_name
        })
    basesql.close_session()
    return response_list


# 异常处理
@app.errorhandler(Exception)
def error_handler(e):
    """
    全局异常捕获，也相当于一个视图函数
    """
    return JsonResponse.error(msg=str(e), code=e.code)


if __name__ == '__main__':
    app.run()
