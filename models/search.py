from exts import db
from datetime import datetime

class SearchModel(db.Model):
    __tablename__ = "search"
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.String(100), db.ForeignKey("user.user_id"))
    garbage_id = db.Column(db.Integer, db.ForeignKey("garbage.garbage_id"))
    search_type = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, default=datetime.now)









