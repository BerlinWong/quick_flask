# -*- coding: utf-8 -*-

# 规范Flask响应
class JsonResponse(object):
    """
    统一的json返回格式
    """

    def __init__(self, data, code, msg):
        self.data = data
        self.code = code
        self.msg = msg

    @classmethod
    def success(cls, data=None, code=200, msg='success'):
        return cls(data, code, msg)

    @classmethod
    def error(cls, data=None, code=None, msg='error'):
        return cls(data, code, msg)

    def to_dict(self):
        return {
            "code": self.code,
            "msg": self.msg,
            "data": self.data
        }
