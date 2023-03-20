# ###################################################################
# 段怡冰

import time
from utils.data_process import Class_To_Data
from utils import restful

from operation.users import UserOperation
from operation.error import ErrorInfoOperation
from operation.garbageSearch import GarbageSearchOperation


def userInfo(data):
    user_opt = UserOperation()
    user_info = user_opt._userInfo(data["user_id"])
    if user_info:
        user_info_json = Class_To_Data(user_info, user_opt.__fields__, 1)
        return restful.ok(message="信息获取成功", data=user_info_json)
    else:
        return restful.params_error(message="信息获取失败")


def userModify(data):
    user_opt = UserOperation()
    user_info = user_opt._modify(open_id=data["user_id"], user_name=data['user_name'],
                             email=data['email'], avatar=data['avatar'], sex=data['sex'],
                             age=data['age'], school=data['school'], location=data['location'])
    if user_info:
        user_info_json = Class_To_Data(user_info, user_opt.__fields__, 1)
        return restful.ok(message="信息修改成功", data=user_info_json)
    else:
        return restful.params_error(message="信息修改失败")


def errorInfoUpload(data):
    error_opt = ErrorInfoOperation()
    error_num = error_opt._errorNum()
    error_num = str(int(error_num) + 1)
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    feedback = error_opt._errorAdd(error_num, data['user_id'], data["garbage_id"], data["error_content"], current_time)
    if feedback == "ok":
        return restful.ok(message="上传成功")
    else:
        return restful.params_error(message="上传失败")


def searchInfo(data):
    garbage_search_opt = GarbageSearchOperation()
    # garbage_opt = GarbageOperation()
    # 精确查询垃圾分类
    search_class = garbage_search_opt._searchExact(data["content"])
    if search_class:
        # 写入search表中查询信息
        search_num = garbage_search_opt._searchNum()
        search_num = str(int(search_num) + 1)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        search_result = garbage_search_opt._searchAdd(search_num, data['user_id'], search_class.garbage_id, search_class.garbage_class, current_time)

        search_class = Class_To_Data(search_class, garbage_search_opt.__fields__, 1)
        if search_result == "ok":
            return restful.ok(message="查询成功", data=search_class)
        else:
            return restful.params_error(message="查询失败")
    return restful.params_error(message="查询失败")

