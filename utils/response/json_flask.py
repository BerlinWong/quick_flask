from flask import Flask, jsonify

from utils.response.json_response import JsonResponse
# 规范Flask响应

class JsonFlask(Flask):
    def make_response(self, rv):
        """视图函数可以直接返回: list、dict、None"""
        if rv is None or isinstance(rv, (list, dict, str)):
            rv = JsonResponse.success(rv)

        if isinstance(rv, JsonResponse):
            rv = jsonify(rv.to_dict())

        return super().make_response(rv)
