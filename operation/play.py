from models.game import PlayGameModel
from exts import db
from flask import g
from datetime import datetime, timedelta

class PlayOperation():
    def __init__(self):
        self.__fields__ = ['play_id', 'open_id', 'user_score', 'create_time', 'give_answer']

    def _playNumToday(self, day):
        play_num = PlayGameModel.query.filter(PlayGameModel.create_time >= day).count()
        return play_num
