import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_blueprint_history_list(code, token, id):

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(id):
        return None

    data = {
        'auth_token': token,
    }
    url = Url.blueprintHistoriesList(id, Url.url)
    list = ApiUtil.requestGet(url, code, data)

    return list


def get_blueprint_parameters(code, token, blueprint_id, version):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(blueprint_id):
        return None

    data = {
        'auth_token': token,
    }
    url = Url.blueprintHistoriesParameters(blueprint_id, version, Url.url)
    param = ApiUtil.requestGet(url, code, data)

    return param


def get_blueprint_history_parameters(code, token, blueprint_id, history_id):
    # -- Later modifications
    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(blueprint_id):
        return None

    if StringUtil.isEmpty(history_id):
        return None

    list = get_blueprint_history_list(code, token, blueprint_id)

    history = None
    for his in list:
        if his.get('id') == history_id:
            history = his
            break

    data = {
        'auth_token': token,
    }
    url = Url.blueprintHistoriesParameters(history.get('blueprint_id'),
                                           history.get('version'), Url.url)
    param = ApiUtil.requestGet(url, code, data)

    return param


def get_blueprint_history_detail(code, token, id, version):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {
        'auth_token': token,
    }

    url = Url.blueprintHistoriesDetail(id, his_id, Url.url)
    history = ApiUtil.requestGet(url, code, data)

    return history
