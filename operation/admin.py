from models.admin import AdminModel
from models.userInfo import UserInfoModel
from exts import db
from flask import g
from datetime import datetime, timedelta
class AdminOperation():
    def __init__(self):
        self.__fields__ = ['admin_id', 'admin_name', 'password', 'email', 'avatar', 'create_time']

    def _findAdminByName(self, admin_name):
        admin = AdminModel.query.filter_by(admin_name=admin_name).first()
        return admin

    def _findAdminById(self, admin_id):
        admin = AdminModel.query.get(admin_id)
        return admin

    def _uploadAdminAvatar(self, filename):
        g.admin.avatar = filename
        db.session.commit()

    def _updateAdmin(self, admin_name, password, email):
        g.admin.admin_name = admin_name
        g.admin.password = password
        g.admin.email = email
        db.session.commit()

    def _updateUserInfo(self, male_number, female_number, male_age_dist, female_age_dist, top_user_dist, user_login_today, user_game_today):
        user_info = UserInfoModel(male_number=male_number, female_number=female_number, male_age_dist=male_age_dist, female_age_dist=female_age_dist, top_user_dist=top_user_dist, user_login=user_login_today, user_game=user_game_today)
        db.session.add(user_info)
        db.session.commit()

    def _userInfoByWeek(self, day):
        user_info = db.session.query(UserInfoModel.user_login, UserInfoModel.user_game).filter(UserInfoModel.create_time >= day - timedelta(days=7)).all()
        print(user_info)
        return user_info

