import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_baseimege_list(code, token):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    url = Url.baseImageList
    data = {'auth_token': token}
    list = ApiUtil.requestGet(url, code, data)

    return list


def create_baseimage(code, token, cloud_id, ssh_username, source_image, os_version):


    # -- Create a project, api call
    url = Url.baseImageCreate
    data = {
        'auth_token': token,
        'cloud_id': cloud_id,
        'ssh_username': ssh_username,
        'source_image': source_image,
        'os_version': os_version,
    }
    # -- API call, get a response
    baseimage = ApiUtil.requestPost(url, code, data)

    return baseimage