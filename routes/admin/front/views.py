from flask import Blueprint, request, render_template, jsonify, current_app, make_response, session, g, url_for
from exts import cache, db
import random
import string
from utils import restful


from io import BytesIO
from models.admin import AdminModel
from hashlib import md5
from flask_avatars import Identicon
from utils.captcha import Captcha
import os
from .forms import LoginForm, SetForm, AvatarForm
from api.admin import adminLogin, adminUploadAvatar
from models.admin import AdminModel
from .decorators import login_required

bp = Blueprint("front", __name__, url_prefix="/admin")


@bp.before_request
def front_before_request():
    admin_id = session.get("admin_id")
    if admin_id:
        admin = AdminModel.query.get(admin_id)
        setattr(g, "admin", admin)
    else:
        setattr(g, "admin", None)


@bp.route("/login", methods=['post'])
def login():
    # print('111')
    form = LoginForm(request.form)
    if form.validate():
        login_data = adminLogin(form)
        return login_data
    else:
        message = form.messages[0]
        return restful.params_error(message=message)

    #测试
    # control = true
    # if (control):
    #     resp = restful.ok(message="成功登录")
    # else:
    #     resp = restful.server_error(message="登录失败")
    # return resp


@bp.route("/logout")
@login_required
def logout():
    session.clear()
    return restful.ok(message="成功登出")



@bp.route("/avatar/upload")
@login_required
def upload_avatar():
    form = AvatarForm(request.form)
    if form.validate:
        upload_avatar_data = adminUploadAvatar(form)
        return upload_avatar_data
    else:
        message = form.messages[0]
        return restful.params_error(message=message)



@bp.route("/setting", methods=['POST'])
@login_required
def setting():
    form = SetForm(request.form)



