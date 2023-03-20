from exts import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "user"
    open_id = db.Column(db.String(100), primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    sex = db.Column(db.String(16))
    age = db.Column(db.Integer)
    school = db.Column(db.String(50))
    location = db.Column(db.String(50))
    score = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.now)


class LoginModel(db.Model):
    __tablename__ = "login"
    open_id = db.Column(db.String(100), primary_key=True)




