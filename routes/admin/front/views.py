from flask import Blueprint, request, render_template, jsonify, current_app, make_response, session, g, url_for
from exts import cache, db
from utils import restful
from .forms import LoginForm, SetForm, AvatarForm
from api.admin import adminLogin, setGlobalAdmin, adminUploadAvatar, adminSet, indexInfo, userInfo
from models.admin import AdminModel
from .decorators import login_required

bp = Blueprint("front", __name__, url_prefix="/admin")


@bp.before_request
def front_before_request():
    admin_id = session.get("admin_id")
    print(admin_id)
    setGlobalAdmin(admin_id)


@bp.route("/", methods=['GET'])
def test():
    return "ok"

@bp.route("/login", methods=['post'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        login_data = adminLogin(form)
        return login_data
    else:
        message = form.messages[0]
        return restful.params_error(message=message)


@bp.route("/logout")
@login_required
def logout():
    session.clear()
    return restful.ok(message="成功登出")


@bp.route("/avatar/upload", methods=['post'])
@login_required
def upload_avatar():
    form = AvatarForm(request.files)
    if form.validate:
        upload_avatar_data = adminUploadAvatar(form)
        return upload_avatar_data
    else:
        message = form.messages[0]
        return restful.params_error(message=message)



@bp.route("/setting", methods=['POST'])
# @login_required
def setting():
    form = SetForm(request.form)
    print(form)
    if form.validate():
        set_data = adminSet(form)
        return set_data
    else:
        message = form.messages[0]
        return restful.params_error(message=message)


@bp.route("/index", methods=['GET'])
def index():
    user_num, new_user_num, old_user_num, garbage_num, play_num, top_words_list, top_images_list, top_vocal_list = indexInfo()
    return restful.ok(data={"user_today": user_num, "new_user_today": new_user_num, "old_user_today": old_user_num, "gb_classify_today": garbage_num, "game_play_today": play_num,
                            "top_info_today": {"top_words_list_today": top_words_list,
                            "top_picture_list_today": top_images_list,
                            "top_vocal_list_today": top_vocal_list}},
                      message="成功进入首页")



@bp.route("/users", methods=['GET'])
def users():
    male_number, female_number, male_age_dist, female_age_dist, top_user_dist, user_login_by_week, user_game_by_week = userInfo()
    return restful.ok(data={"population": {
                                "male_number": male_number,
                                "female_number": female_number},
                            "age_dist": {
                                "male_age_dist": male_age_dist,
                                "female_age_dist": female_age_dist},
                            "top_user_dist": top_user_dist,
                            "user_login_by_week": user_login_by_week,
                            "user_game_by_week": user_game_by_week},
                    message="成功进入用户分析页面")
