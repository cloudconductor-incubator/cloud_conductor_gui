import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_cloud_list(code, token, project_id=None):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    url = Url.cloudList
    data = {
        'auth_token': token,
        'project_id': project_id
    }
    list = ApiUtil.requestGet(url, code, data)

    return list


def get_cloud_detail(code, token, id):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(id):
        return None

    url = Url.cloudDetail(id, Url.url)
    data = {
        'auth_token': token,
        'id': id,
    }
    project = ApiUtil.requestGet(url, code, data)

    return project


def create_cloud2(code, token, project_id, form):

    # -- Create a cloud, api call
    url = Url.cloudCreate
    data = {
        'auth_token': token,
        'project_id': project_id,
    }
    form.update(data)
    # -- API call, get a response
    cloud = ApiUtil.requestPost(url, code, form)

    return cloud


def create_cloud(code, token, project_id, name, type, key, secret,
                 entry_point, tenant_name, description):

    # -- Create a cloud, api call
    url = Url.cloudCreate
    data = {
        'auth_token': token,
        'project_id': project_id,
        'name': name,
        'type': type,
        'key': key,
        'secret': secret,
        'entry_point': entry_point,
        'tenant_name': tenant_name,
        'description': description
    }
    # -- API call, get a response
    cloud = ApiUtil.requestPost(url, code, data)

    return cloud
