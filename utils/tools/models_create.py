import os
import sys
import sqlacodegen.main
from dotenv import load_dotenv, find_dotenv

# 生成models文件到models文件夹下
if __name__ == '__main__':
    load_dotenv(find_dotenv('.env'))
    env_dist = os.environ
    username = env_dist.get('MYSQL_USERNAME')
    password = env_dist.get('MYSQL_PASSWORD')
    host = env_dist.get('MYSQL_HOST')
    port = env_dist.get('MYSQL_PORT')
    database = env_dist.get('MYSQL_DATABASE')
    order = 'sqlacodegen --noviews --outfile ../../models/models.py mysql+pymysql://{}:{}@{}:{}/{}' \
        .format(username, password, host, port, database)
    temp = order.split(' ')[1:]
    genarr = []
    for a_temp in temp:
        if not a_temp == '':
            genarr.append(a_temp)
    sys.argv.extend(genarr)
    sqlacodegen.main.main()
