'''
配置相关文件
'''
import os
from datetime import timedelta

# 数据库连接的配置
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "grabage"
db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = db_url
SQLALCHEMY_TRACK_MODIFICALTIONS = False


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "1400094360@qq.com"
MAIL_PASSWORD = "cfhfcxhbkzcgiage"
MAIL_DEFAULT_SENDER = "1400094360@qq.com"

# broker、 backend
# 接收和发送任务
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
# 存储任务结果
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"

# 缓存
CACHE_TYPE = "RedisCache"
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_HOST = "127.0.0.1"
CACHE_REDIS_PORT = "6379"


SECRET_KEY = "abcdefghijklmn"

BASE_DIR = os.path.dirname(__file__)

PERMANENT_SESSION_LIFETIME = timedelta(days=7)


AVATARS_SAVE_PATH = os.path.join(BASE_DIR, "media", "avatars")
POST_IMAGE_SAVE_PATH = os.path.join(BASE_DIR, "media", "post")

