import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_blueprint_history_list(code, token, blueprint_id, version):

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
    list = ApiUtil.requestGet(url, code, data)

    return list