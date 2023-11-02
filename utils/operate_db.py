# 该文件对数据库进行增删改查
import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
load_dotenv(find_dotenv('.env'))
env_dist = os.environ
username = env_dist.get('MYSQL_USERNAME')
password = env_dist.get('MYSQL_PASSWORD')
host = env_dist.get('MYSQL_HOST')
port = env_dist.get('MYSQL_PORT')
database = env_dist.get('MYSQL_DATABASE')
engine = create_engine(
    'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(username, password, host, port, database),
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)


class connect_db(object):
    pass
