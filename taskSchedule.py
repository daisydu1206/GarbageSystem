from exts import scheduler
from operation.users import UserOperation
from operation.admin import AdminOperation
from operation.play import PlayOperation

@scheduler.task("cron", id="index_job", day="*", hour="20", minute='52', second='0')
def userAnalysisJob():
    print("开始更新今日用户信息")
    with scheduler.app.app_context():
        user_opt = UserOperation()
        admin_opt = AdminOperation()
        play_opt = PlayOperation()
        male_number, female_number = user_opt._userNumByGender()
        male_age_dist, female_age_dist = user_opt._userNumByAge()
        dist = user_opt._topDist()
        top_user_dist = {}
        for item in dist:
            top_user_dist[item[0]] = item[1]
        user_login_today = user_opt._userNumToday()
        user_game_today = play_opt._playNumToday()
        admin_opt._updateUserInfo(male_number, female_number, str(male_age_dist), str(female_age_dist), str(top_user_dist), user_login_today, user_game_today)
        print("更新完毕")


