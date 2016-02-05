from collections import OrderedDict
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils.ApiUtil import Url


def get_role_list(code, token, project_id=None, account_id=None):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    url = Url.roleList
    data = {
        'auth_token': token,
    }
    if StringUtil.isNotEmpty(project_id):
        data['project_id'] = project_id
    elif StringUtil.isNotEmpty(project_id):
        data['account_id'] = account_id
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
            if param.split('-')[1] in \
               ['manage', 'read', 'create', 'update', 'destroy']:
                url = Url.permissionCreate(role["id"], Url.url)
                data = {
                    'auth_token': token,
                    'action': param.split('-')[1],
                    'model': param.split('-')[0],
                }
                permission = ApiUtil.requestPost(url, code, data)
        # ApiUtil.requestPost(url, code, data)

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
            if param.split('-')[1] in \
               ['manage', 'read', 'create', 'update', 'destroy']:
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
    models.append({"no": "2", "name": "Assignment",
                   "item_name": "assignment"})
    models.append({"no": "3", "name": "Cloud", "item_name": "cloud"})
    models.append({"no": "4", "name": "BaseImage",
                   "item_name": "base_image"})
    models.append({"no": "5", "name": "System", "item_name": "system"})
    models.append({"no": "6", "name": "Environment",
                   "item_name": "environment"})
    models.append({"no": "7", "name": "Application",
                   "item_name": "application"})
    models.append({"no": "8", "name": "Application History",
                   "item_name": "application_history"})
    models.append({"no": "9", "name": "Deployment",
                   "item_name": "deployment"})
    models.append({"no": "10", "name": "Blueprint",
                   "item_name": "blueprint"})
    models.append({"no": "11", "name": "Blueprint Pattern",
                   "item_name": "blueprint_pattern"})
    models.append({"no": "12", "name": "Blueprint History",
                   "item_name": "blueprint_history"})
    models.append({"no": "13", "name": "Pattern", "item_name": "pattern"})
    models.append({"no": "14", "name": "Account", "item_name": "account"})
    models.append({"no": "15", "name": "Role", "item_name": "role"})
    models.append(
        {"no": "16", "name": "Permission", "item_name": "permission"})

    for model in models:
        items = []
        for action in actions:
            if model["item_name"] + "-" + action in check_value:
                items.append(
                    {"item_name": model["item_name"] + "-" + action,
                     "checked": "checked"})
            else:
                items.append(
                    {"item_name": model["item_name"] + "-" + action,
                     "checked": ""})

        check_items.append(
            {"no": model["no"], "name": model["name"], "items": items})
        pass

    return {'role': role, 'check_items': check_items}


def get_account_role(code, token, project_id, account_id):

    if StringUtil.isEmpty(token):
        return None

    if StringUtil.isEmpty(project_id):
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

    role = None
    for r in roles:
        role = r
        break

    return role


def delete_role(code, token, id):

    if StringUtil.isEmpty(code):
        return None

    if StringUtil.isEmpty(token):
        return None

    url = Url.roleDelete(id, Url.url)
    data = {'auth_token': token}
    ApiUtil.requestDelete(url, code, data)


# def add_session_role(session, role, permissions):
#
#     list = []
#     dic = {}
#     for per in permissions:
#         dic = {}
#         if per.get('model') in list:
#             index = list.index(per.get('model'))
#             model = list.get(index)
#             value = model.get(per.get('model'))
#             if StringUtil.isEmpty(model):
#                 break
#
# #             value.update({per.get('model'): True})
#             value[per.get('action')]=True
#
#             model = value
#             list[index] = value
# #             list.insert(index, per.get('action'))
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
    dic_project = {}
    dic_account = {}
    dic_assignment = {}
    dic_role = {}
    dic_cloud = {}
    dic_base_image = {}
    dic_pattern = {}
    dic_blueprint = {}
    dic_system = {}
    dic_environment = {}
    dic_application = {}
    dic_application_history = {}
    dic_deployment = {}

    for per in permissions:

        #         dic = {}
        if per.get("model") == 'project':

            dic_project['m_project'] = True

            if per.get("action") == 'manage':
                dic_project['manage'] = True

            elif per.get("action") == 'read':
                dic_project['read'] = True

            elif per.get("action") == 'create':
                dic_project['create'] = True

            elif per.get("action") == 'update':
                dic_project['update'] = True

            elif per.get("action") == 'destroy':
                dic_project['destroy'] = True

            session['project'] = dic_project

        elif per.get("model") == 'account':

            dic_account['m_account'] = True

            if per.get("action") == 'manage':
                dic_account['manage'] = True

            elif per.get("action") == 'read':
                dic_account['read'] = True

            elif per.get("action") == 'create':
                dic_account['create'] = True

            elif per.get("action") == 'update':
                dic_account['update'] = True

            elif per.get("action") == 'destroy':
                dic_account['destroy'] = True

            session['account'] = dic_account

        elif per.get("model") == 'assignment':

            dic_assignment['m_assignment'] = True

            if per.get("action") == 'manage':
                dic_assignment['manage'] = True

            elif per.get("action") == 'read':
                dic_assignment['read'] = True

            elif per.get("action") == 'create':
                dic_assignment['create'] = True

            elif per.get("action") == 'update':
                dic_assignment['update'] = True

            elif per.get("action") == 'destroy':
                dic_assignment['destroy'] = True

            session['assignment'] = dic_assignment

        elif per.get("model") == 'role':

            dic_role['m_role'] = True

            if per.get("action") == 'manage':
                dic_role['manage'] = True

            elif per.get("action") == 'read':
                dic_role['read'] = True

            elif per.get("action") == 'create':
                dic_role['create'] = True

            elif per.get("action") == 'update':
                dic_role['update'] = True

            elif per.get("action") == 'destroy':
                dic_role['destroy'] = True

            session['role'] = dic_role

        elif per.get("model") == 'cloud':

            dic_cloud['m_cloud'] = per.get("model")

            if per.get("action") == 'manage':
                dic_cloud['manage'] = True

            elif per.get("action") == 'read':
                dic_cloud['read'] = True

            elif per.get("action") == 'create':
                dic_cloud['create'] = True

            elif per.get("action") == 'update':
                dic_cloud['update'] = True

            elif per.get("action") == 'destroy':
                dic_cloud['destroy'] = True

            session['cloud'] = dic_cloud

        elif per.get("model") == 'base_image':

            dic_base_image['m_baseimage'] = per.get("model")

            if per.get("action") == 'manage':
                dic_base_image['manage'] = True

            elif per.get("action") == 'read':
                dic_base_image['read'] = True

            elif per.get("action") == 'create':
                dic_base_image['create'] = True

            elif per.get("action") == 'update':
                dic_base_image['update'] = True

            elif per.get("action") == 'destroy':
                dic_base_image['destroy'] = True

            session['baseimage'] = dic_base_image

        elif per.get("model") == 'pattern':

            dic_pattern['m_pattern'] = True

            if per.get("action") == 'manage':
                dic_pattern['manage'] = True

            elif per.get("action") == 'read':
                dic_pattern['read'] = True

            elif per.get("action") == 'create':
                dic_pattern['create'] = True

            elif per.get("action") == 'update':
                dic_pattern['update'] = True

            elif per.get("action") == 'destroy':
                dic_pattern['destroy'] = True

            session['pattern'] = dic_pattern

        elif per.get("model") == 'blueprint':

            dic_blueprint['m_blueprint'] = True

            if per.get("action") == 'manage':
                dic_blueprint['manage'] = True

            elif per.get("action") == 'read':
                dic_blueprint['read'] = True

            elif per.get("action") == 'create':
                dic_blueprint['create'] = True

            elif per.get("action") == 'update':
                dic_blueprint['update'] = True

            elif per.get("action") == 'destroy':
                dic_blueprint['destroy'] = True

            session['blueprint'] = dic_blueprint

        elif per.get("model") == 'blueprint_history':

            dic_blueprint['m_blueprint'] = True

            if per.get("action") == 'manage':
                dic_blueprint['manage'] = True

            elif per.get("action") == 'read':
                dic_blueprint['read'] = True

            elif per.get("action") == 'create':
                dic_blueprint['create'] = True

            elif per.get("action") == 'update':
                dic_blueprint['update'] = True

            elif per.get("action") == 'destroy':
                dic_blueprint['destroy'] = True

            session['blueprint_history'] = dic_blueprint

        elif per.get("model") == 'system':

            dic_system['m_system'] = per.get("model")

            if per.get("action") == 'manage':
                dic_system['manage'] = True

            elif per.get("action") == 'read':
                dic_system['read'] = True

            elif per.get("action") == 'create':
                dic_system['create'] = True

            elif per.get("action") == 'update':
                dic_system['update'] = True

            elif per.get("action") == 'destroy':
                dic_system['destroy'] = True

            session['system'] = dic_system

        elif per.get("model") == 'environment':

            dic_environment['m_environment'] = per.get("model")

            if per.get("action") == 'manage':
                dic_environment['manage'] = True

            elif per.get("action") == 'read':
                dic_environment['read'] = True

            elif per.get("action") == 'create':
                dic_environment['create'] = True

            elif per.get("action") == 'update':
                dic_environment['update'] = True

            elif per.get("action") == 'destroy':
                dic_environment['destroy'] = True

            session['environment'] = dic_environment

        elif per.get("model") == 'application':

            dic_application['m_application'] = per.get("model")

            if per.get("action") == 'manage':
                dic_application['manage'] = True

            elif per.get("action") == 'read':
                dic_application['read'] = True

            elif per.get("action") == 'create':
                dic_application['create'] = True

            elif per.get("action") == 'update':
                dic_application['update'] = True

            elif per.get("action") == 'destroy':
                dic_application['destroy'] = True

            session['application'] = dic_application

        elif per.get("model") == 'application_history':

            dic_application_history['m_application_history'] = per.get("model")

            if per.get("action") == 'manage':
                dic_application_history['manage'] = True

            elif per.get("action") == 'read':
                dic_application_history['read'] = True

            elif per.get("action") == 'create':
                dic_application_history['create'] = True

            elif per.get("action") == 'update':
                dic_application_history['update'] = True

            elif per.get("action") == 'destroy':
                dic_application_history['destroy'] = True

            session['application_history'] = dic_application_history

        elif per.get("model") == 'deployment':

            dic_deployment['m_deployment'] = per.get("model")

            if per.get("action") == 'manage':
                dic_deployment['manage'] = True

            elif per.get("action") == 'read':
                dic_deployment['read'] = True

            elif per.get("action") == 'create':
                dic_deployment['create'] = True

            elif per.get("action") == 'update':
                dic_deployment['update'] = True

            elif per.get("action") == 'destroy':
                dic_deployment['destroy'] = True

            session['deployment'] = dic_deployment

        # -- wizard
#         if w_cloud_registrarion:
#
#         elif w_make_new_app:
#
#         elif w_app_env:
#
#         elif w_deploying_app:


def delete_session_role(session):
    if 'project' in session:
        del session['project']

    if 'account' in session:
        del session['account']

    if 'assignment' in session:
        del session['assignment']

    if 'role' in session:
        del session['role']

    if 'cloud' in session:
        del session['cloud']

    if 'baseimage' in session:
        del session['baseimage']

    if 'pattern' in session:
        del session['pattern']

    if 'blueprint' in session:
        del session['blueprint']

    if 'blueprint_history' in session:
        del session['blueprint_history']

    if 'system' in session:
        del session['system']

    if 'environment' in session:
        del session['environment']

    if 'application' in session:
        del session['application']

    if 'application_history' in session:
        del session['application_history']

    if 'deployment' in session:
        del session['deployment']
