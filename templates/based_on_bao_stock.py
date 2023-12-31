# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd


class BaoStock:
    def __init__(self, stock=None, start_date=None, end_date=None):
        self.stock = stock
        self.start_date = start_date
        self.end_date = end_date

    def processing(self):
        #### 登陆系统 ####
        lg = bs.login()
        # 显示登陆返回信息
        # print('login respond error_code:' + lg.error_code)
        # print('login respond  error_msg:' + lg.error_msg)

        #### 获取沪深A股历史K线数据 ####
        # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
        # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
        # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
        rs = bs.query_history_k_data_plus('sh.' + self.stock,
                                          "date, code, open, close, low, high, preclose, volume",
                                          start_date=self.start_date, end_date=self.end_date,
                                          frequency="d", adjustflag="3")
        if not rs:
            rs = bs.query_history_k_data_plus('sz.' + self.stock,
                                              "date, code, open, close, low, high, preclose, volume",
                                              start_date=self.start_date, end_date=self.end_date,
                                              frequency="d", adjustflag="3")
        # print('query_history_k_data_plus respond error_code:' + rs.error_code)
        # print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

        #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        #### 登出系统 ####
        bs.logout()
        return result

#
# bbs = BaoStock('600010', '2023-10-11', '2023-10-25')
# print(bbs.processing())
