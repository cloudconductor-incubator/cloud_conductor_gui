import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..enum.StatusCode import Environment
from ..logs import log


def get_environment_list(code, token, project_id=None):

    # -- Create a cloud, api call
    url = Url.environmentList
    data = {
        'auth_token': token,
        'project_id': project_id,
    }
    # -- API call, get a response
    list = ApiUtil.requestGet(url, code, data)

    return list


def get_environment_list2(code, token, project_id=None):

    environments = get_environment_list(code, token, project_id)

    dic = {}
    list = []
    for env in environments:
        if env.get('status') == Environment.CREATE_COMPLETE.value:
            dic['id'] = str(env.get('id'))
            dic['name'] = env.get('name')
            list.append(dic.copy())

    return list


def get_environment_detail(code, token, id):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(id):
        return None

    url = Url.environmentDetail(id, Url.url)
    data = {
        'auth_token': token,
        'id': id,
    }
    environment = ApiUtil.requestGet(url, code, data)

    return StringUtil.deleteNullDict(environment)


def edit_environment(code, token, id, form, temp_param):
    # -- Create a project, api call
    url = Url.environmentEdit(id, Url.url)
    data = {
        'auth_token': token,
        'name': form.get('name'),
        'description': form.get('description')
    }

    if form.get("user_attributes"):
        data["user_attributes"] = form.get("user_attributes")

    if temp_param:
        print(str(temp_param).replace('\'', '\"'))
        data["template_parameters"] = str(temp_param).replace('\'', '\"')

    # -- API call, get a response
    project = ApiUtil.requestPut(url, code, StringUtil.deleteNullDict(data))

    return project


def addEnvironmentParam(param):
    # candidates_attributes
    candidates_attributes = []
    dic = {
        'cloud_id': int(param.get('candidates_attributes_1')),
        'priority': 1}
    candidates_attributes.append(dic)

    if param.get('candidates_attributes_2'):
        dic = {
            'cloud_id': int(param.get('candidates_attributes_2')),
            'priority': 2}
        candidates_attributes.append(dic)

    if param.get('candidates_attributes_3'):
        dic = {
            'cloud_id': int(param.get('candidates_attributes_3')),
            'priority': 3}
        candidates_attributes.append(dic)

    data = {
        'auth_token': param.get('auth_token'),
        'project_id': param.get('project_id'),
        'system_id': param.get('system_id'),
        'blueprint_id': param.get('blueprint_id'),
        'version': param.get('version'),
        'name': param.get('name'),
        'description': param.get('description'),
        'template_parameters': param.get('template_parameters'),
        'user_attributes': param.get('user_attributes'),
        'candidates_attributes': candidates_attributes,
    }

    return data
