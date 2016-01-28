from collections import OrderedDict
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url


def get_permission_list(code, token, role_id):
    print("et_permission_list:1")
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(role_id):
        return None
    print("et_permission_list:2")
    url = Url.permissionList(role_id, Url.url)
    data = {'auth_token': token}
    list = ApiUtil.requestGet(url, code, data)

    return list
