from flask_cors import CORS

from utils.response.json_flask import JsonFlask
from utils.response.json_response import JsonResponse

# app = Flask(__name__)

app = JsonFlask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 异常处理
@app.errorhandler(Exception)
def error_handler(e):
    """
    全局异常捕获，也相当于一个视图函数
    """
    return JsonResponse.error(msg=str(e), code=e.code)


if __name__ == '__main__':
    app.run()
