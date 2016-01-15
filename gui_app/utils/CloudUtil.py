import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def create_cloud(code, token, project_id, name, type, key, secret, entry_point, tenant_name, description):

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
