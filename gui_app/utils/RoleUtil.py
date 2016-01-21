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


def create_role(code, token, project_id,name, description , params):
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
            if param.split('-')[1] in ['manage','create','update','destroy']:
                url = Url.permissionCreate(role["id"], Url.url)
                data = {
                    'auth_token': token,
                    'action': param.split('-')[1],
                    'model': param.split('-')[0],
                }
                permission = ApiUtil.requestPost(url, code, data)
        #ApiUtil.requestPost(url, code, data)


    return role

def edit_role(code, token, id,name, description , params):
    # -- Create a project, api call
    url = Url.roleEdit(id,Url.url)
    data = {
        'auth_token': token,
        'name': name,
        'description': description
    }

    # -- API call, get a response
    role = ApiUtil.requestPut(url, code, data)


    url = Url.permissionList(id,Url.url)
    permissions = ApiUtil.requestGet(url, code, data)
    old_value = []
    old_id = []
    for permission in permissions:
        old_value.append(permission["model"] + "-"  + permission["action"])
        pass

    i = 0
    for param in params:
        if '-' in param:
            if param.split('-')[1] in ['manage','read','create','update','destroy']:
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

        if permission["model"] + "-"  + permission["action"] in old_value:
            url = Url.permissionDelete(id,permission["id"], Url.url)
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

    url = Url.roleDetail(id,Url.url)
    data = {'auth_token': token}
    role = ApiUtil.requestGet(url, code, data)

    url = Url.permissionList(id,Url.url)
    permissions = ApiUtil.requestGet(url, code, data)

    check_value = []
    for permission in permissions:
        check_value.append(permission["model"] + "-"  + permission["action"])
        pass

    check_items = []
    actions =["manage","read","create","update","destroy"]
    models = []
    models.append({"no":"1", "name":"Project", "item_name":"project"})
    models.append({"no":"2", "name":"Cloud", "item_name":"cloud"})
    models.append({"no":"3", "name":"BaseImage", "item_name":"base_image"})
    models.append({"no":"4", "name":"Blueprint", "item_name":"blueprint"})
    models.append({"no":"5", "name":"System", "item_name":"system"})
    models.append({"no":"6", "name":"Environment", "item_name":"environment"})
    models.append({"no":"7", "name":"Application", "item_name":"application"})
    models.append({"no":"8", "name":"Pattern", "item_name":"pattern"})
    models.append({"no":"9", "name":"Account", "item_name":"account"})
    models.append({"no":"10", "name":"Role", "item_name":"role"})

    for model in models:
        items = []
        for action in actions:
            if model["item_name"] + "-"  + action in check_value:
                items.append({"item_name":model["item_name"] + "-" + action,"checked":"checked"})
            else:
                items.append({ "item_name":model["item_name"] + "-" +action,"checked":""})

        check_items.append({"no":model["no"], "name":model["name"], "items":items})
        pass


    return {'role':role,'check_items':check_items}


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


def add_session_role(session, role, permissions):
    session['role_id'] = role['id']

    for per in permissions:
        if per.get("model") == 'project':
            session['m_project'] = True

            if per.get("action") == 'manage':
                session['project_manage'] = True

            elif per.get("action") == 'read':
                session['project_read'] = True

            elif per.get("action") == 'create':
                session['project_create'] = True

            elif per.get("action") == 'update':
                session['project_update'] = True

            elif per.get("action") == 'destroy':
                session['project_destroy'] = True

        elif per.get("model") == 'account':
            session['m_account'] = True

            if per.get("action") == 'manage':
                session['account_manage'] = True

            elif per.get("action") == 'read':
                session['account_read'] = True

            elif per.get("action") == 'create':
                session['account_create'] = True

            elif per.get("action") == 'update':
                session['account_update'] = True

            elif per.get("action") == 'destroy':
                session['account_destroy'] = True

        elif per.get("model") == 'role':
            session['m_role'] = True

            if per.get("action") == 'manage':
                session['role_manage'] = True

            elif per.get("action") == 'read':
                session['role_read'] = True

            elif per.get("action") == 'create':
                session['role_create'] = True

            elif per.get("action") == 'update':
                session['role_update'] = True

            elif per.get("action") == 'destroy':
                session['role_destroy'] = True

        elif per.get("model") == 'cloud':
            session['m_cloud'] = per.get("model")

            if per.get("action") == 'manage':
                session['cloud_manage'] = True

            elif per.get("action") == 'read':
                session['cloud_read'] = True

            elif per.get("action") == 'create':
                session['cloud_create'] = True

            elif per.get("action") == 'update':
                session['cloud_update'] = True

            elif per.get("action") == 'destroy':
                session['cloud_destroy'] = True

        elif per.get("model") == 'base_image':
            session['m_baseimage'] = per.get("model")

            if per.get("action") == 'manage':
                session['baseimage_manage'] = True

            elif per.get("action") == 'read':
                session['baseimage_read'] = True

            elif per.get("action") == 'create':
                session['baseimage_create'] = True

            elif per.get("action") == 'update':
                session['baseimage_update'] = True

            elif per.get("action") == 'destroy':
                session['baseimage_destroy'] = True

        elif per.get("model") == 'pattern':
            session['m_pattern'] = True

            if per.get("action") == 'manage':
                session['pattern_manage'] = True

            elif per.get("action") == 'read':
                session['pattern_read'] = True

            elif per.get("action") == 'create':
                session['pattern_create'] = True

            elif per.get("action") == 'update':
                session['pattern_update'] = True

            elif per.get("action") == 'destroy':
                session['pattern_destroy'] = True

        elif per.get("model") == 'blueprint':
            session['m_blueprint'] = True

            if per.get("action") == 'manage':
                session['blueprint_manage'] = True

            elif per.get("action") == 'read':
                session['blueprint_read'] = True

            elif per.get("action") == 'create':
                session['blueprint_create'] = True

            elif per.get("action") == 'update':
                session['blueprint_update'] = True

            elif per.get("action") == 'destroy':
                session['blueprint_destroy'] = True

        elif per.get("model") == 'system':
            session['m_system'] = per.get("model")

            if per.get("action") == 'manage':
                session['system_manage'] = True

            elif per.get("action") == 'read':
                session['system_read'] = True

            elif per.get("action") == 'create':
                session['system_create'] = True

            elif per.get("action") == 'update':
                session['system_update'] = True

            elif per.get("action") == 'destroy':
                session['system_destroy'] = True

        elif per.get("model") == 'environment':
            session['m_environment'] = per.get("model")

            if per.get("action") == 'manage':
                session['environment_manage'] = True

            elif per.get("action") == 'read':
                session['environment_read'] = True

            elif per.get("action") == 'create':
                session['environment_create'] = True

            elif per.get("action") == 'update':
                session['environment_update'] = True

            elif per.get("action") == 'destroy':
                session['environment_destroy'] = True

        elif per.get("model") == 'application':
            session['m_application'] = per.get("model")

            if per.get("action") == 'manage':
                session['application_manage'] = True

            elif per.get("action") == 'read':
                session['application_read'] = True

            elif per.get("action") == 'create':
                session['application_create'] = True

            elif per.get("action") == 'update':
                session['application_update'] = True

            elif per.get("action") == 'destroy':
                session['application_destroy'] = True

        elif per.get("model") == 'application_history':
            session['m_application_history'] = per.get("model")

            if per.get("action") == 'manage':
                session['application_history_manage'] = True

            elif per.get("action") == 'read':
                session['application_history_read'] = True

            elif per.get("action") == 'create':
                session['application_history_create'] = True

            elif per.get("action") == 'update':
                session['application_history_update'] = True

            elif per.get("action") == 'destroy':
                session['application_history_destroy'] = True

        elif per.get("model") == 'deployment':
            session['m_deployment'] = per.get("model")

            if per.get("action") == 'manage':
                session['deployment_manage'] = True

            elif per.get("action") == 'read':
                session['deployment_read'] = True

            elif per.get("action") == 'create':
                session['deployment_create'] = True

            elif per.get("action") == 'update':
                session['deployment_update'] = True

            elif per.get("action") == 'destroy':
                session['deployment_destroy'] = True

        # -- wizard
#         if w_cloud_registrarion:
#
#         elif w_make_new_app:
#
#         elif w_app_env:
#
#         elif w_deploying_app:



