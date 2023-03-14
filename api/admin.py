from operation.admin import AdminOperation
from utils import restful
from flask import session, current_app, g
from utils.data_process import Class_To_Data
import os
from hashlib import md5
import time

def adminLogin(form):
    admin_name = form.admin_name.data
    password = form.password.data
    admin_opt = AdminOperation()
    admin = admin_opt._findAdmin(admin_name)
    if not admin:
        return restful.params_error(message="用户名或密码错误")
    admin = Class_To_Data(admin, admin_opt.__fields__, 1)
    if admin['password'] != password:
        return restful.params_error(message="用户名或密码错误")
    session['admin_id'] = admin['admin_id']
    return restful.ok(message="成功登录")


def adminUploadAvatar(form):
    image = form.image.data
    filename = image.filename
    _, ext = os.path.splitext(filename)
    filename = md5((g.admin.admin_id + str(time.time())).encode("utf-8")).hexdigest() + ext
    image_path = os.path.join(current_app.config['AVATARS_SAVE_PATH'], filename)
    image.save(image_path)
    admin_opt = AdminOperation()
    admin_opt._uploadAvatar(filename)
    return restful.ok(data={"avatar": filename}, message="头像上传成功")

