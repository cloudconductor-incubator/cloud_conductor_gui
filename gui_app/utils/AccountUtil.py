import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log

def get_account_list(code, token, project_id=None):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    data = {
            'auth_token': token,
            'project_id': project_id,
            }

    url = Url.accountList
    list = ApiUtil.requestGet(url, code, data)
    return list


def get_account(code, token, email):

    if StringUtil.isEmpty(email):
        return None

    list = get_account_list(code, token)

    dic = {}
    for account in list:
        if account.get('email') == email:
            dic['id'] = account.get('id')
            dic['name'] = account.get('name')
            dic['admin'] = account.get('admin')
            dic['email'] = email

            return dic

    return None


def get_account_detail(code, token, id):
    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(id):
        return None

    data = {
            'auth_token': token,
            }

    url = Url.accountDetail(id, Url.url)
    account = ApiUtil.requestGet(url, code, data)

    return account


def get_account_create(code, token, name, email, password, repassword, admin):
    # -- URL set
    url = Url.accountCreate

    # -- Set the value to the form
    data = {
            'auth_token': token,
            'name': name,
            'email': email,
            'password': password,
            'password_confirmation': repassword,
            'admin': int(admin),
            }
    # -- API call, get a response
    response = ApiUtil.requestPost(url, code, data)

    return response