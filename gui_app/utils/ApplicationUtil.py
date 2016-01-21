import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log

def get_application_list(code, token, project_id=None):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {
            'auth_token': token,
            'project_id': project_id,
            }

    url = Url.applicationList
    list = ApiUtil.requestGet(url, code, data)
    return list


def get_application_list2(code, token, project_id=None):

    apps = get_application_list(code, token, project_id)

    if StringUtil.isEmpty(apps):
        return None

    dic = {}
    list = []
    for app in apps:
        dic['id'] = str(app.get('id'))
        dic['name'] = app.get('name')
        list.append(dic.copy())

    return list


def get_application_detail(code, token, id):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {
            'auth_token': token,
            }

    url = Url.applicationDetail(id, Url.url)
    list = ApiUtil.requestGet(url, code, data)
    return list


def create_application(code, token, system_id, name, description, domain):
    # -- URL set
    url = Url.applicationCreate

    # -- Set the value to the form
    data = {
            'auth_token': token,
            'system_id': system_id,
            'name': name,
            'description': description,
            'domain': domain,
            }
    # -- API call, get a response
    response = ApiUtil.requestPost(url, code, data)

    return response

def deploy_application(code, token, environment_id, application_id, application_history_id=None):
    # -- URL set
    url = Url.applicationDeploy(application_id, Url.url)

    # -- Set the value to the form
    data = {
            'auth_token': token,
            'environment_id': environment_id,
            'application_history_id': application_history_id,
            }
    # -- API call, get a response
    response = ApiUtil.requestPost(url, code, data)

    return response

