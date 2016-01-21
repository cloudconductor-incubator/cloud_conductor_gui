import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_blueprint_list(code, token, project_id=None):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(project_id):
        return None

    data = {
            'auth_token': token,
            'project_id': project_id,
            }
    url = Url.blueprintList
    list = ApiUtil.requestGet(url, code, data)

    return list


def get_blueprint_list2(code, token, project_id=None):

    blueprints = get_blueprint_list(code, token, project_id)
    print(blueprints)

    if StringUtil.isEmpty(blueprints):
        return None

    dic = {}
    list = []
    for bp in blueprints:
        dic['id'] = str(bp.get('id'))
        dic['name'] = bp.get('name')
        list.append(dic.copy())

    return list


def create_blueprint(code, token, project_id, name, description):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(project_id):
        return None

    if StringUtil.isEmpty(name):
        return None

    data = {
            'auth_token': token,
            'project_id': project_id,
            'name': name,
            'description': description,
            }
    url = Url.blueprintCreate
    list = ApiUtil.requestPost(url, code, data)

    return list


def edit_blueprint(code, token, id, project_id, name, description):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(project_id):
        return None

    data = {
            'auth_token': token,
            'project_id': project_id,
            'name': name,
            'description': description,
            }

    url = Url.blueprintEdit(id, Url.url)
    list = ApiUtil.requestPost(url, code, data)

    return list


def get_blueprint_version(code, data):

    if code == None or data == None:
        return None

    # Get a Blueprint List
    url = Url.blueprintList
    blueprints = ApiUtil.requestGet(url, code, data)

    if blueprints == None:
        return None

    # Create a custom blueprint list
    dic = {}
    list = []
    for bp in blueprints:
        bpid = bp.get('id')
        # Get a Blueprint History
        url = Url.blueprintHistoriesList(bpid, Url.url)
        histories = ApiUtil.requestGet(url, code, data)

        if histories == None:
            break

        for history in histories:

            dic['id'] = bpid
            dic['name'] = bp.get('name')
            dic['version'] = history.get('version')
            list.append(dic.copy())

    return list


def get_blueprint_pattern_list(code, id, token):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(id):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {
            'auth_token': token,
        }

    url = Url.blueprintPattrnList(id, Url.url)
    list = ApiUtil.requestGet(url, code, data)

    if StringUtil.isEmpty(list):
        return None
    else:
        return list


def get_pattern_list(code, id, token, pjid):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(id):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {
            'auth_token': token,
            'project_id': pjid,
        }

    bpptternList = get_blueprint_pattern_list(code, id, token)
    if StringUtil.isEmpty(bpptternList):
        return None

    url = Url.patternList
    patternList = ApiUtil.requestGet(url, code, data)
    if StringUtil.isEmpty(patternList):
        return None

    dic = {}
    list = []
    for bpt in bpptternList :

        for pt in patternList:

            if pt.get('id') == bpt.get('pattern_id'):

                dic['id'] = pt.get('id')
                dic['name'] =  pt.get('name')
                dic['revision'] = pt.get('revision')
                dic['protocol'] = pt.get('protocol')
                list.append(dic.copy())

    return list