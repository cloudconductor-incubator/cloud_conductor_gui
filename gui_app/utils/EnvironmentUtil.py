import re
import ast
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..enum.StatusCode import Environment
from ..logs import log
PATRITION = '/'


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


def create_environment(code, form, session):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(form):
        return None

    if StringUtil.isEmpty(session.get('auth_token')):
        return None

    param = putBlueprint(form)
    inputs = createJson(param)
    env = addEnvironmentParam(form, inputs, session)
    # -- Create a environment, api call
    url = Url.environmentCreate
    # -- API call, get a response
    environment = ApiUtil.requestPost(url, code,
                                      StringUtil.deleteNullDict(env))

    return environment


def delete_system(code, token, id):

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(id):
        return None

    url = Url.environmentDelete(id, Url.url)
    data = {'auth_token': token}
    ApiUtil.requestDelete(url, code, data)


def putBlueprint(param):

    blueprint = param.get('blueprint', None)
    if blueprint is not None and blueprint != '':
        blueprint = ast.literal_eval(blueprint)

        param['blueprint_id'] = blueprint.get('id')
        param['version'] = blueprint.get('version')

    return param


def putMap(jmap, key, val):
    ''' KEY VALUE parameter to DICT '''
    if key.find(PATRITION) != -1:
        kf = key.find(PATRITION)
        k1 = key[0:kf]
        k2 = key[kf + 1:]
        if k1 not in jmap:
            jmap[k1] = {}
        putMap(jmap[k1], k2, val)
    else:
        jmap[key] = val


def createJson(prm):
    ''' HTTP parameter to DICT  '''
    pmap = {}
    for k in prm.keys():
        if k.find('json/') == 0:
            kp = k[5:]
            putMap(pmap, kp, prm[k])

    return pmap


def addEnvironmentParam(param, temp_param, session):
    # candidates_attributes
    print(param)
    candidates_attributes = []
    dic = {
        "cloud_id": param.get("candidates_attributes_1"), "priority": "1"}
    candidates_attributes.append(dic)

    if param.get("candidates_attributes_2"):
        dic = {
            "cloud_id": param.get("candidates_attributes_2"), "priority": "2"}
        candidates_attributes.append(dic)

    if param.get("candidates_attributes_3"):
        dic = {
            "cloud_id": param.get("candidates_attributes_3"), "priority": "3"}
        candidates_attributes.append(dic)

    print(candidates_attributes)
    data = {
        "auth_token": session.get("auth_token"),
        "project_id": session.get("project_id"),
        "system_id": param.get("system_id"),
        "blueprint_id": str(param.get("blueprint_id")),
        "version": str(param.get("version")),
        "name": param.get("name"),
        "description": param.get("description", ""),
        "candidates_attributes": candidates_attributes
    }

    if param.get("user_attributes"):
        data["user_attributes"] = param.get("user_attributes")

    print(str(temp_param).replace('\'', '\"'))
    if temp_param:
        tp = str(temp_param).replace('\'', '\"')
        data["template_parameters"] = tp.replace(' ', '')

    return data
