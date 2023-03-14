from exts import db
from datetime import datetime

class GameInfoModel(db.Model):
    __tablename__ = "game_info"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_content = db.Column(db.String(255))
    game_answer = db.Column(db.Integer)


class PlayModel(db.Model):
    __tablename__ = "play"
    play_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.String(100), db.ForeignKey("user.open_id"))
    game_id = db.Column(db.Integer, db.ForeignKey("game_info.game_id"))
    user_answer = db.Column(db.Integer)

    game_info = db.relationship("GameInfoModel", backref=db.backref("plays"))



class PlayGameModel(db.Model):
    __tablename__ = "play_game"
    play_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.String(100), db.ForeignKey("user.open_id"))
    user_score = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now)
    give_answer = db.Column(db.Integer, db.ForeignKey("play.play_id"))

    play_records = db.relationship("PlayModel", backref=db.backref("plays"))
    user = db.relationship("UserModel", backref=db.backref("plays"))




# Run git config --global user.email "you@example.com" git config --global user.name "Your Name"










