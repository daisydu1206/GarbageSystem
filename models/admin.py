from exts import db
import shortuuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class AdminModel(db.Model):
    __tablename__ = "admin"
    admin_id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    admin_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now)



