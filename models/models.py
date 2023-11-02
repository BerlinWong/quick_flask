# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, Integer, String, text
from sqlalchemy.dialects.mysql import ENUM, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AllSzShStock(Base):
    __tablename__ = 'all_sz_sh_stock'

    id = Column(Integer, primary_key=True)
    code = Column(String(255), comment='代码')
    stock_name = Column(String(255), comment='股票名称')
    industry = Column(String(255), comment='行业')
    flag = Column(String(255), comment='深圳/上海')
    add_date = Column(DateTime, comment='添加日期')
    suggestion = Column(Integer, comment='是否推荐')


class ChineseCalendar(Base):
    __tablename__ = 'chinese_calendar'
    __table_args__ = {'comment': '中国节假日和双休日数据表以及工作日数据表'}

    day_is = Column(Date, primary_key=True, comment='日期')
    day_name = Column(VARCHAR(100), comment='日名称')
    day_type = Column(ENUM('Holiday', 'Weekend', 'Workday'), server_default=text("'Holiday'"), comment='日期类型：节假日或双休日和工作日')


class IndexList(Base):
    __tablename__ = 'index_list'
    __table_args__ = {'comment': '指数列表\\r\\n'}

    index_code = Column(VARCHAR(255), primary_key=True, comment='指数代码')
    index_only_code = Column(VARCHAR(255), comment='纯代码，不含sh/sz')
    index_name = Column(VARCHAR(255), comment='指数名称')
    index_name_eng = Column(VARCHAR(255), comment='指数英文名称')
    exchange = Column(VARCHAR(255), comment='交易所')
    is_listening = Column(Integer, comment='0-监听;1-不监听')


class IndexWeight(Base):
    __tablename__ = 'index_weight'

    id = Column(Integer, primary_key=True)
    index_code = Column(VARCHAR(16), nullable=False)
    stock_code = Column(VARCHAR(16), nullable=False)
    weight = Column(Float(8))
    day_date = Column(Date, nullable=False)
