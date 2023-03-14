from exts import db
from datetime import datetime

class PlayModel(db.Model):
    __tablename__ = "play"
    play_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.String(100), db.ForeignKey("user.user_id"))
    game_id = db.Column(db.Integer, db.ForeignKey("garbage.garbage_id"))
    admin_id = db.Column(db.String(100), db.ForeignKey("admin.admin_id"))
    error_content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    reply_time = db.Column(db.DateTime)

Run git config --global user.email "you@example.com" git config --global user.name "Your Name"










