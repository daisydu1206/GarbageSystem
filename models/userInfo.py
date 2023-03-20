from datetime import datetime
from exts import db
class UserInfoModel(db.Model):
    __tablename__ = "user_info"
    create_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d'), primary_key=True)
    male_number = db.Column(db.Integer)
    female_number = db.Column(db.Integer)
    male_age_dist = db.Column(db.String(100))
    female_age_dist = db.Column(db.String(100))
    top_user_dist = db.Column(db.String(100))
    user_login = db.Column(db.Integer)
    user_game = db.Column(db.Integer)
