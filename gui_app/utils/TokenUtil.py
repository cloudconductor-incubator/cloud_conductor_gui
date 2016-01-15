import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log

def get_token(code, email, password):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(password):
        return None

    if StringUtil.isEmpty(email):
        return None

    url = Url.token
    data = {'email': email, 'password': password}
    token = ApiUtil.requestPost(url, code, data)

    return token
