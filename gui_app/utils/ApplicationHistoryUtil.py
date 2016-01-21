import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_history_list(code, token, id):
    if StringUtil.isEmpty(id):
        return None

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {'auth_token': token}

    url = Url.applicationHistoryList(id, Url.url)
    list = ApiUtil.requestGet(url, code, data)
    return list


def get_history_list2(code, token, id):
    if StringUtil.isEmpty(id):
        return None

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    apps = get_history_list(code, token, id)

    if StringUtil.isEmpty(apps):
        return None

    dic = {}
    list = []
    for app in apps:
        dic['id'] = str(app.get('id'))
        dic['version'] = app.get('version')
        dic['revision'] = app.get('revision')
        list.append(dic.copy())

    return list


def get_new_history(code, token, id):
    if StringUtil.isEmpty(id):
        return None

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    apps = get_history_list(code, token, id)

    if StringUtil.isEmpty(apps):
        return None

    dic = {}
    for app in apps:
        if int(dic.get('id', 0)) < app.get('id'):
            dic['id'] = str(app.get('id'))
            dic['version'] = app.get('version')
            dic['revision'] = app.get('revision')
        print(dic)
    return dic


def get_history_detail(code, token, id, his_id):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {
            'auth_token': token,
            }

    url = Url.applicationHistoryDetail(id, his_id,Url.url)
    list = ApiUtil.requestGet(url, code, data)
    return list


def create_history(code, token, id, url, type, protocol, revision,
                   pre_deploy, post_deploy, parameters):

    if StringUtil.isEmpty(id):
        return None

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    # -- URL set
    url = Url.applicationHistoryCreate(id, Url.url)

    # -- Set the value to the form
    data = {
        'auth_token': token,
        'url': url,
        'type': type,
        'protocol': protocol,
        'revision': revision,
        'pre_deploy': pre_deploy,
        'post_deploy': post_deploy,
        'parameters': parameters,
    }
    # -- API call, get a response
    response = ApiUtil.requestPost(url, code, data)

    return response
