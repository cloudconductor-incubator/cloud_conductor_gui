import re
from collections import OrderedDict
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def get_role_list(code, token, project_id=None, account_id=None):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    url = Url.roleList
    data = {
        'auth_token': token,
        'project_id': project_id,
    }
    list = ApiUtil.requestGet(url, code, data)

    return list


def create_role(code, token, project_id, name, description, params):
    # -- Create a project, api call
    url = Url.roleCreate
    data = {
        'auth_token': token,
        'project_id': project_id,
        'name': name,
        'description': description
    }
    # -- API call, get a response
    role = ApiUtil.requestPost(url, code, data)

    for param in params:
        if '-' in param:
            if param.split('-')[1] in ['manage', 'create', 'update', 'destroy']:
                url = Url.permissionCreate(role["id"], Url.url)
                data = {
                    'auth_token': token,
                    'action': param.split('-')[1],
                    'model': param.split('-')[0],
                }
                permission = ApiUtil.requestPost(url, code, data)
        #ApiUtil.requestPost(url, code, data)

    return role


def edit_role(code, token, id, name, description, params):
    # -- Create a project, api call
    url = Url.roleEdit(id, Url.url)
    data = {
        'auth_token': token,
        'name': name,
        'description': description
    }

    # -- API call, get a response
    role = ApiUtil.requestPut(url, code, data)

    url = Url.permissionList(id, Url.url)
    permissions = ApiUtil.requestGet(url, code, data)
    old_value = []
    old_id = []
    for permission in permissions:
        old_value.append(permission["model"] + "-" + permission["action"])
        pass

    i = 0
    for param in params:
        if '-' in param:
            if param.split('-')[1] in ['manage', 'read', 'create', 'update', 'destroy']:
                if param in old_value:
                    old_value.remove(param)
                    pass

                else:
                    url = Url.permissionCreate(role["id"], Url.url)
                    data = {
                        'auth_token': token,
                        'action': param.split('-')[1],
                        'model': param.split('-')[0],
                    }
                    permission = ApiUtil.requestPost(url, code, data)

    for permission in permissions:

        if permission["model"] + "-" + permission["action"] in old_value:
            url = Url.permissionDelete(id, permission["id"], Url.url)
            data = {'auth_token': token}
            ApiUtil.requestDelete(url, code, data)

    return role


def get_role_detail(code, token, id):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(id):
        return None

    url = Url.roleDetail(id, Url.url)
    data = {'auth_token': token}
    role = ApiUtil.requestGet(url, code, data)

    url = Url.permissionList(id, Url.url)
    permissions = ApiUtil.requestGet(url, code, data)

    check_value = []
    for permission in permissions:
        check_value.append(permission["model"] + "-" + permission["action"])
        pass

    check_items = []
    actions = ["manage", "read", "create", "update", "destroy"]
    models = []
    models.append({"no": "1", "name": "Project", "item_name": "project"})
    models.append({"no": "2", "name": "Assignment", "item_name": "assignment"})
    models.append({"no": "3", "name": "Cloud", "item_name": "cloud"})
    models.append({"no": "4", "name": "BaseImage", "item_name": "base_image"})
    models.append({"no": "5", "name": "System", "item_name": "system"})
    models.append({"no": "6", "name": "Environment", "item_name": "environment"})
    models.append({"no": "7", "name": "Application", "item_name": "application"})
    models.append({"no": "8", "name": "Application History", "item_name": "application_history"})
    models.append({"no": "9", "name": "Deployment", "item_name": "deployment"})
    models.append({"no": "10", "name": "Blueprint", "item_name": "blueprint"})
    models.append({"no": "11", "name": "Blueprint Pattern", "item_name": "blueprint_pattern"})
    models.append({"no": "12", "name": "Blueprint History", "item_name": "blueprint_history"})
    models.append({"no": "13", "name": "Pattern", "item_name": "pattern"})
    models.append({"no": "14", "name": "Account", "item_name": "account"})
    models.append({"no": "15", "name": "Role", "item_name": "role"})
    models.append({"no": "16", "name": "Permission", "item_name": "permission"})

    for model in models:
        items = []
        for action in actions:
            if model["item_name"] + "-" + action in check_value:
                items.append(
                    {"item_name": model["item_name"] + "-" + action, "checked": "checked"})
            else:
                items.append(
                    {"item_name": model["item_name"] + "-" + action, "checked": ""})

        check_items.append(
            {"no": model["no"], "name": model["name"], "items": items})
        pass

    return {'role': role, 'check_items': check_items}


def get_account_role(code, token, project_id, account_id):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(account_id):
        return None

    url = Url.roleList
    data = {
        'auth_token': token,
        'account_id': account_id,
        'project_id': project_id
    }
    roles = ApiUtil.requestGet(url, code, data)

    if not roles:
        return None

    role = {}
    for r in roles:
        role['id'] = r.get('id')
        role['name'] = r.get('name')
        role['preset'] = r.get('preset')
        role['project_id'] = r.get('project_id')
        role['description'] = r.get('description')
        role['created_at'] = r.get('created_at')
        role['updated_at'] = r.get('updated_at')

        break

    return role


# def add_session_role(session, role, permissions):
#
#     list = []
#     dic = {}
#     for per in permissions:
#
#         if per.get('model') in list:
#             index = list.index(per.get('model'))
#             list.insert(index, per.get('action'))
#         else:
#             dic[per.get('action')]=True
#             list.append({per.get('model'): dic})
# #             list.append(per.get('model'){ per.get('action'):Ture})
#
#
#     print(list)

def add_session_role(session, role, permissions):
    session['role_id'] = role.get('id')

    model_bk = ''

    for per in permissions:

#         dic = {}
        if per.get("model") == 'project':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_project'] = True

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['project'] = dic

        elif per.get("model") == 'account':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_account'] = True

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['account'] = dic

        elif per.get("model") == 'role':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_role'] = True

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['role'] = dic

        elif per.get("model") == 'cloud':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_cloud'] = per.get("model")

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['cloud'] = dic

        elif per.get("model") == 'base_image':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_baseimage'] = per.get("model")

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['baseimage'] = dic

        elif per.get("model") == 'pattern':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_pattern'] = True

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['pattern'] = dic

        elif per.get("model") == 'blueprint':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_blueprint'] = True

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['blueprint'] = dic

        elif per.get("model") == 'system':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_system'] = per.get("model")

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['system'] = dic

        elif per.get("model") == 'environment':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_environment'] = per.get("model")

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['environment'] = dic

        elif per.get("model") == 'application':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_application'] = per.get("model")

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['application'] = dic

        elif per.get("model") == 'application_history':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_application_history'] = per.get("model")

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['application_history'] = dic

        elif per.get("model") == 'deployment':
            if model_bk != per.get("model"):
                dic = {}

            dic['m_deployment'] = per.get("model")

            if per.get("action") == 'manage':
                dic['manage'] = True

            elif per.get("action") == 'read':
                dic['read'] = True

            elif per.get("action") == 'create':
                dic['create'] = True

            elif per.get("action") == 'update':
                dic['update'] = True

            elif per.get("action") == 'destroy':
                dic['destroy'] = True

            session['deployment'] = dic

        # -- wizard
#         if w_cloud_registrarion:
#
#         elif w_make_new_app:
#
#         elif w_app_env:
#
#         elif w_deploying_app:


def delete_session_role(session):

    session['project'] = ''

    session['account'] = ''

    session['role'] = ''

    session['cloud'] = ''

    session['baseimage'] = ''

    session['pattern'] = ''

    session['blueprint'] = ''

    session['system'] = ''

    session['environment'] = ''

    session['application'] = ''

    session['application_history'] = ''

    session['deployment'] = ''
