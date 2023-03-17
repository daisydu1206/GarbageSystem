from models.user import UserModel
from exts import db
from flask import g
from datetime import datetime, timedelta
from sqlalchemy import func
class UserOperation():
    def __init__(self):
        self.__fields__ = ['open_id', 'user_name', 'email', 'avatar', 'sex', 'age', 'school', 'location', 'score', 'create_time']

    def _userNum(self):
        user_num = UserModel.query.count()
        return user_num

    def _newUserNum(self, day):
        new_user_num = UserModel.query.filter(UserModel.create_time >= day).count()
        return new_user_num

    def _userNumByGender(self):
        male_number = UserModel.query.filter(UserModel.sex == "男").count()
        female_number = UserModel.query.filter(UserModel.sex == "女").count()
        return male_number, female_number


    def _userNumByAge(self):
        ages = [0, 20, 30, 40, 60, 200]
        male_age_num = []
        female_age_num = []
        for i in range(len(ages) - 1):
            male_age_num.append(
                UserModel.query.filter(UserModel.age >= ages[i], UserModel.age < ages[i + 1],
                                       UserModel.sex == "男").count()
            )
            female_age_num.append(
                UserModel.query.filter(UserModel.age >= ages[i], UserModel.age < ages[i + 1],
                                       UserModel.sex == "女").count()
            )
        return male_age_num, female_age_num


    def _topDist(self):
        top_user_dist = db.session.query(UserModel.location, func.count("*")).group_by(UserModel.location).order_by(
            func.count("*")).limit(5).all()
        return top_user_dist


