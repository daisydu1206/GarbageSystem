from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_caching import Cache
from flask_wtf import CSRFProtect
from flask_avatars import Avatars
from flask_apscheduler import APScheduler

db = SQLAlchemy()
mail = Mail()
cache = Cache()
avatars = Avatars()
scheduler = APScheduler()