# ##########################################
# 段怡冰
import json
import requests
from flask import Blueprint, request

from api.user import*
from utils import restful

user = Blueprint('user', __name__, url_prefix="/user")

# 获取用户id
# {"user_id":"123"}
@user.route('/getInfo',methods=['POST'])
def getInfo():
    data = request.data
    if data:
        data = json.loads(data)
        user_info_result = userInfo(data)
        return user_info_result
    else:
        return restful.params_error(message="参数错误")


@user.route('/modify',methods=['POST'])
def modify():
    data = request.data
    if data:
        data = json.loads(data)
        user_info_result = userModify(data)
        return user_info_result
    else:
        return restful.params_error(message="参数错误")


@user.route("/errorInfo",methods=['POST'])
def errorInfo():
    data = request.data
    if data:
        data = json.loads(data)
        error_info_result = errorInfoUpload(data)
        return error_info_result
    else:
        return restful.params_error(message="参数错误")



@user.route("/search/text",methods=['POST'])
def searchtext():
    data = request.data
    if data:
        data = json.loads(data)
        search_result = searchInfo(data)
        return search_result
    else:
        return restful.params_error(message="参数错误")

@user.route("/search/voice",methods=['POST'])
def searchvoice():
    data = request.data
    if data:
        data = json.loads(data)
        search_result = searchInfo(data)
        return search_result
    else:
        return restful.params_error(message="参数错误")
