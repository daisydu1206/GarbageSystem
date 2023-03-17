from flask_wtf import Form
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import Email, Length, EqualTo
from flask_wtf.file import FileAllowed, FileSize
from wtforms import ValidationError
from exts import cache
from flask import request
from models.admin import AdminModel
class BaseForm(Form):
    @property
    def messages(self):
        message_list = []
        if self.errors:
            for errors in self.errors.values():
                message_list.extend(errors)
        return message_list

class LoginForm(BaseForm):
    admin_name = StringField(validators=[Length(3, 20, message="用户名格式不符合要求")])
    password = StringField(validators=[Length(6, 20, message="密码错误")])


class SetForm(BaseForm):
    admin_name = StringField(validators=[Length(3, 20, message="用户名格式不符合要求")])
    password = StringField(validators=[Length(6, 20, message="密码长度不符合要求")])
    repeat_password = StringField(validators=[EqualTo("password", message="两次密码不一致")])
    email = StringField(validators=[Email(message="邮箱格式错误")])



class AvatarForm(BaseForm):
    image = FileField(validators=[FileAllowed(['jpg', 'jpeg', 'png'], message="图片格式错误"),
                                  FileSize(max_size=1024*1024*5, message="图片最大不能超过五兆")])

