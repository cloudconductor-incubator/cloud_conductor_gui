import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_project_list(code, token):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    url = Url.projectList
    data = {'auth_token': token}
    list = ApiUtil.requestGet(url, code, data)

    return list


def get_project_list2(code, token):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    url = Url.projectList
    data = {'auth_token': token}
    projects = ApiUtil.requestGet(url, code, data)

    if StringUtil.isEmpty(projects):
        dic = {}
        list = []
        for project in projects:
            dic['project_id'] = project.get('id')
            dic['project_name'] = project.get('name')
            list.append(dic.copy())

        return list

    else:
        return None


def get_project_detail(code, token, id):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(id):
        return None

    url = Url.projectDetail(id, Url.url)
    data = {
        'auth_token': token,
        'id': id,
    }
    project = ApiUtil.requestGet(url, code, data)

    return project


def create_project(code, token, name, description):
    # -- Create a project, api call
    url = Url.projectCreate
    data = {
        'auth_token': token,
        'name': name,
        'description': description
    }
    # -- API call, get a response
    project = ApiUtil.requestPost(url, code, data)

    return project
