from operation.admin import AdminOperation
from operation.users import UserOperation
from operation.garbageSearch import GarbageSearchOperation
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
    print(session.get("admin_id"))
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
    print(admin_name, password, email)
    admin_opt = AdminOperation()
    admin_opt._updateAdmin(admin_name, password, email)
    return restful.ok(data={"admin_name": admin_name, "password": password, "email": email}, message="信息修改成功")


def indexInfo():
    user_opt = UserOperation()
    today = datetime.datetime.now()

    user_num_today = user_opt._userNumToday()
    new_user_num_today = user_opt._newUserNumToday(today)
    old_user_num_today = user_num_today - new_user_num_today

    garbage_search_opt = GarbageSearchOperation()
    search_num_today = garbage_search_opt._searchNumToday(today)

    play_opt = PlayOperation()
    play_num_today = play_opt._playNumToday(today)

    top_words_garbages = garbage_search_opt._topWordsToay("文本", today)
    top_words_list = []
    for garbage in top_words_garbages:
        top_words_list.append(garbage[0])

    top_images_garbages = garbage_search_opt._topWordsToay("图片", today)
    top_images_list = []
    for garbage in top_images_garbages:
        top_images_list.append(garbage[0])

    top_vocal_garbages = garbage_search_opt._topWordsToay("语音", today)
    top_vocal_list = []
    for garbage in top_vocal_garbages:
        top_vocal_list.append(garbage[0])

    return user_num_today, new_user_num_today, old_user_num_today, search_num_today, play_num_today, top_words_list, top_images_list, top_vocal_list


def userInfo():
    today = datetime.datetime.now()
    user_opt = UserOperation()
    admin_opt = AdminOperation()
    male_number, female_number = user_opt._userNumByGender()
    male_age_dist, female_age_dist = user_opt._userNumByAge()
    dist = user_opt._topDist()
    top_user_dist = {}
    for item in dist:
        top_user_dist[item[0]] = item[1]

    user_login_week = []
    user_game_week = []
    user_infos = admin_opt._userInfoByWeek(today)
    for user_info in user_infos:
        user_login_week.append(user_info[0])
        user_game_week.append(user_info[1])
    # print(user_login_week, user_game_week)
    return male_number, female_number, male_age_dist, female_age_dist, top_user_dist, user_login_week, user_game_week





