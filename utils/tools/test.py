import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))
env_dist = os.environ
print(env_dist.get('MYSQL_USERNAME'))