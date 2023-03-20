from models.user import UserModel, LoginModel
from exts import db
from flask import g
from datetime import datetime, timedelta
from sqlalchemy import func
class UserOperation():
    def __init__(self):
        self.__fields__ = ['open_id', 'user_name', 'email', 'avatar', 'sex', 'age', 'school', 'location', 'score', 'create_time']

    def _userNumToday(self):
        user_num_today = LoginModel.query.count()
        return user_num_today

    def _newUserNumToday(self, day):
        new_user_num_today = db.session.query(UserModel.open_id).outerjoin(LoginModel, LoginModel.open_id == UserModel.open_id).filter(UserModel.create_time >= day).count()
        return new_user_num_today

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


    # #################################################################################################
    # 段怡冰
    def _userInfo(self, open_id):
        userInfo = UserModel.query.filter_by(open_id=open_id).first()
        return userInfo

    def _modify(self, open_id, user_name, email, avatar, sex, age, school, location):
        if user_name:
            UserModel.query.filter_by(open_id=open_id).update({UserModel.user_name: user_name})
        if email:
            UserModel.query.filter_by(open_id=open_id).update({UserModel.email: email})
        if avatar:
            UserModel.query.filter_by(open_id=open_id).update({UserModel.avatar: avatar})
        if sex:
            UserModel.query.filter_by(open_id=open_id).update({UserModel.sex: sex})
        if age:
            UserModel.query.filter_by(open_id=open_id).update({UserModel.age: age})
        if school:
            UserModel.query.filter_by(open_id=open_id).update({UserModel.school: school})
        if location:
            UserModel.query.filter_by(open_id=open_id).update({UserModel.location: location})
        db.session.commit()
        return self._userInfo(open_id)