from exts import db
import shortuuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class AdminModel(db.Model):
    __tablename__ = "admin"
    admin_id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    admin_name = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        if "password" in kwargs:
            self.password = kwargs.get("password")
            kwargs.pop("password")
        super(AdminModel, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, newpwd):
        self._password = generate_password_hash(newpwd)

    def check_password(self, rawpwd):
        return check_password_hash(self.password, rawpwd)


