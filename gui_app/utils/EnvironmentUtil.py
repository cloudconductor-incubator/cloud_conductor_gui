import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
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

    environments = get_system_list(code, token, project_id=None)

    dic = {}
    list = []
    for env in environments:

        dic['id'] = env.get('id')
        dic['name'] = env.get('name')
        list.append(dic.copy())

    return list
