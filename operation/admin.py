from models.admin import AdminModel
from exts import db
from flask import g
class AdminOperation():
    def __init__(self):
        self.__fields__ = ['admin_id', 'admin_name', 'password', 'email', 'avatar', 'create_time']

    def _findAdmin(self, admin_name):
        admin = AdminModel.query.filter_by(admin_name=admin_name).first()
        return admin

    def _uploadAvatar(self, filename):
        g.user.avatar = filename
        db.session.commit()
