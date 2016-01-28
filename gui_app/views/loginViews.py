# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response
import json
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, get_object_or_404, redirect
from ..forms import loginForm
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..enum.MessageCode import Error
from django.core.exceptions import ValidationError
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import TokenUtil
from ..utils import AccountUtil
from ..utils import ProjectUtil
from ..utils import RoleUtil
from ..utils import PermissionUtil
from ..utils.ApiUtil import Url
from .import roleViews
from ..logs import log

# Create your views here.


def login(request):
    try:
        if request.method == "GET":
            return render(request, Html.login, {'message': ''})
        else:
            #-- Get a value from a form
            code = FuncCode.login.value
            session = request.session
            msg = ''
            p = request.POST
            #-- Validate check
            form = loginForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.login, {'message': msg})

            #-- TokenAPI call, get a response
            password = p.get('password')
            email = p.get('email')
            tokens = TokenUtil.get_token(code, email, password)

            if tokens:
                token = tokens.get('auth_token')
            else:
                raise(Error.Authentication.value)

            #-- AccountApi call, get a response
            account = AccountUtil.get_account(code, token, email)
            if not account:
                raise(Error.Authentication.value)


            #-- ProjectListAPI call, get a response
            projects = ProjectUtil.get_project_list(code, token)
            project_list = ''
            project_id = ''
            project_name = ''

#             if account.get('admin'):
#                 for pj in projects:
#                     if RoleUtil.get_role_list(code, token, account_id=account.get('id')):


            print(projects)
            if projects:
                print(1)
                project_list = projects

                for project in projects:
                    project_id = project.get('id')
                    project_name = project.get('name')
                    print(2)
                    break

            print(4)

            #-- RoleListAPI call, get a response
            role = RoleUtil.get_account_role(code, token, project_id, account.get('id'))
            print(role)
            if not role:
                raise(Error.Authentication.value)
            #-- PermissionListAPI call, get a response
            print(role.get('id'))
            print(5)
            permissions = PermissionUtil.get_permission_list(code, token, role.get('id'))

            if not permissions:
                raise(Error.Authentication.value)

            #-- Add to session
            addLoginSession(token, account, project_list, project_id, project_name, session, role, permissions)

            return redirect(Path.top)

    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.login, {"message": str(ex)})

def addLoginSession(token, account, project_list, project_id, project_name, session, role, permissions):
        # -- token
        session['auth_token'] = token

        # -- account
        session['account_id'] = account.get('id')
        session['account_name'] = account.get('name')
        session['account_admin'] = account.get('admin')

        # -- projects
        session['project_list'] = project_list
        session['project_id'] = project_id
        session['project_name'] = project_name

        # -- Role and role_id and menu
        RoleUtil.add_session_role(session, role, permissions)


def logout(request):
    # session delete
    request.session.clear()
    return render(request, Html.login, {'message': ''})
