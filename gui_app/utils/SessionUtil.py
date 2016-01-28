import re
from django.shortcuts import redirect
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils import ProjectUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def edit_project_session(code, token, session, id=None, name=None):

    project_list = ProjectUtil.get_project_list3(code, token)

    session['project_list'] = project_list

    if session.get('project_id') == id:

        if not name:
            session['project_id'] = ''
            session['project_name'] = ''
        else:
            session['project_id'] = id
            session['project_name'] = name
#         if id in project_list:
#             for project in project_list:
#                 project_id = project.get('id')
#                 project_name = project.get('name')
#                 break


def check_login(request):
    if request.session.get('auth_token') is (u"" or None):
        return False
    else:
        return True


def check_permission(request, model, action, account_id=None):

    permission = False
    model_action = request.session.get(model)
    if action == 'list' or action == 'read':
        if model_action.get('manage') == True or model_action.get('read') == True or model_action.get('create') == True or request.session.get('update') == True or model_action.get('destroy') == True:
            permission = True

    elif action == 'create':
        if model_action.get('manage') == True or model_action.get('create') == True:
            permission = True

    elif action == 'update':
        if model_action.get('manage') == True or model_action.get('update') == True:
            if StringUtil.isEmpty(account_id):
                permission = True
            elif request.session.get('account_admin') or request.session.get('account_id') == int(account_id):
                permission = True

    elif action == 'destroy':
        if model_action.get('manage') == True or model_action.get('destroy') == True:
            permission = True

    return permission
