from models.admin import AdminModel
from exts import db
from flask import g
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
