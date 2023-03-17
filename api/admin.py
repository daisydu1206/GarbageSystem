from operation.admin import AdminOperation
from operation.users import UserOperation
from operation.garbage import GarbageOperation
from operation.play import PlayOperation
from utils import restful
from flask import session, current_app, g
from utils.data_process import Class_To_Data
import os
from hashlib import md5
import time
import datetime
import json
def adminLogin(form):
    admin_name = form.admin_name.data
    password = form.password.data
    admin_opt = AdminOperation()
    admin = admin_opt._findAdminByName(admin_name)
    if not admin:
        return restful.params_error(message="用户名或密码错误")
    admin = Class_To_Data(admin, admin_opt.__fields__, 1)
    if admin['password'] != password:
        return restful.params_error(message="用户名或密码错误")
    session['admin_id'] = admin['admin_id']
    return restful.ok(message="成功登录")


def setGlobalAdmin(admin_id):
    if admin_id:
        admin_opt = AdminOperation()
        admin = admin_opt._findAdminById(admin_id)
        setattr(g, "admin", admin)
    else:
        setattr(g, "admin", None)

def adminUploadAvatar(form):
    image = form.image.data
    filename = image.filename
    _, ext = os.path.splitext(filename)
    filename = md5((g.admin.admin_id + str(time.time())).encode("utf-8")).hexdigest() + ext
    image_path = os.path.join(current_app.config['AVATARS_SAVE_PATH'], filename)
    image.save(image_path)
    admin_opt = AdminOperation()
    admin_opt._uploadAdminAvatar(filename)
    return restful.ok(data={"avatar": filename}, message="头像上传成功")


def adminSet(form):
    admin_name = form.admin_name.data
    password = form.password.data
    email = form.email.data
    admin_opt = AdminOperation()
    admin_opt._updateAdmin(admin_name, password, email)
    return restful.ok(data={"admin_name": admin_name, "password": password, "email": email}, message="信息修改成功")


def getTodayInfo():
    user_opt = UserOperation()
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    user_num = user_opt._userNum()
    new_user_num = user_opt._newUserNum(today)
    old_user_num = user_num - new_user_num

    garbage_opt = GarbageOperation()
    garbage_num = garbage_opt._garbageNum()

    play_opt = PlayOperation()
    play_num = play_opt._playNumToday(today)

    top_words_garbages = garbage_opt._topWords("文本", today)
    top_words_list = []
    for garbage in top_words_garbages:
        top_words_list.append(garbage[0])

    top_images_garbages = garbage_opt._topWords("图片", today)
    top_images_list = []
    for garbage in top_images_garbages:
        top_images_list.append(garbage[0])

    top_vocal_garbages = garbage_opt._topWords("语音", today)
    top_vocal_list = []
    for garbage in top_vocal_garbages:
        top_vocal_list.append(garbage[0])

    return user_num, new_user_num, old_user_num, garbage_num, play_num, top_words_list, top_images_list, top_vocal_list


def userAnalsis():
    user_opt = UserOperation()
    male_number, female_number = user_opt._userNumByGender()
    male_age_dist, female_age_dist = user_opt._userNumByAge()
    dist = user_opt._topDist()
    top_user_dist = {}
    for item in dist:
        top_user_dist[item[0]] = item[1]

    return male_number, female_number, male_age_dist, female_age_dist, top_user_dist




