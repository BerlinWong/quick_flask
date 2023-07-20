from pandas.io.json import to_json
from sqlalchemy.orm import sessionmaker

from models.models import User
from utils.operate_db import engine


class BaseSQL():
    def __init__(self):
        Session = sessionmaker(engine)
        self.session = Session()

    def __del__(self):
        print("自动关闭连接")
        self.session.close()

    # 查询返回生成器
    def console_sql(self, tb_class, **kwargs):
        return self.session.query(tb_class).filter_by(**kwargs).yield_per(1)

    # 简单查询
    def select(self):
        return self.session.query(User).all()

    # 基本查询器
    def base_select(self, tb_lass, **kwargs):
        return self.session.query(tb_lass).filter_by(**kwargs).all()

    # 全局session 关闭
    def close_session(self):
        self.session.close()




basesql = BaseSQL()
print(basesql.console_sql(User))
basesql.close_session()
