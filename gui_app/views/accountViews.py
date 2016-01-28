# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
import json
import requests
from django.shortcuts import redirect
from ..forms import accountForm
from ..utils import AccountUtil
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import SessionUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log


def accountList(request):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request, 'account', 'list') == False:
            return render_to_response(Html.error_403)

        code = FuncCode.accountList.value
        token = request.session.get('auth_token')
        project_id = request.session.get('project_id')

        # -- Get a  list, API call
        accounts = AccountUtil.get_account_list(code, token, project_id)

        return render(request, Html.accountList, {'accounts': accounts, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.accountList.value, None, ex)

        return render(request, Html.accountList, {"accounts": '', 'message': str(ex)})


def accountDetail(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request, 'account', 'read') == False:
            return render_to_response(Html.error_403)

        # -- account DetailAPI call, get a response
        token = request.session['auth_token']
        project_id = request.session['project_id']
        code = FuncCode.accountDetail.value

        account = AccountUtil.get_account_detail(code, token, id)
        role = RoleUtil.get_account_role(
            code, token, project_id, account.get('id'))
        account.update({'role': role.get('name')})

        return render(request, Html.accountDetail, {'account': account, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.accountDetail.value, None, ex)

        return render(request, Html.accountDetail, {'account': '', 'message': str(ex)})


def accountCreate(request):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request, 'account', 'create') == False:
            return render_to_response(Html.error_403)

        token = request.session['auth_token']
        code = FuncCode.accountCreate.value

        if request.method == "GET":

            return render(request, Html.accountCreate, {'account': '', 'form': '', 'message': ''})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = accountForm(request.POST)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.accountCreate, {'account': p, 'form': form, 'message': ''})
            # -- AccountCreateAPI call, get a response
            response = AccountUtil.get_account_create(
                code, token, p['name'], p['email'], p['password'], p['repassword'], p['admin'])

            return redirect(Path.accountList)
    except Exception as ex:
        log.error(FuncCode.accountCreate.value, None, ex)

        return render(request, Html.accountCreate, {'account': request.POST, 'form': '', 'message': str(ex)})


def accountEdit(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request, 'account', 'update', id) == False:
            return render_to_response(Html.error_403)

        if request.method == "GET":
            token = request.session['auth_token']
            url = Url.accountDetail(id, Url.url)
            data = {
                'auth_token': token
            }
            p = ApiUtil.requestGet(url, FuncCode.accountEdit.value, data)
            p.update(data)

            return render(request, Html.accountEdit, {'account': p, 'message': '', 'edit': True})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = accountForm(request.POST)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.accountEdit, {'account': p, 'form': form, 'message': '', 'edit': True})

            # -- URL set
            url = Url.accountEdit(id, Url.url)
            # -- Set the value to the form
            data = {
                'auth_token': request.session['auth_token'],
                'name': p['name'],
                'email': p['email'],
                'password': p['password'],
                'repassword': p['repassword'],
                'admin': p['admin'],
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.accountEdit.value, data)

            return redirect(Path.accountList)
    except Exception as ex:
        log.error(FuncCode.accountEdit.value, None, ex)

        return render(request, Html.accountEdit, {'account': request.POST, 'form': '', 'message': str(ex), 'edit': True})


def accountDelete(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request, 'account', 'destroy') == False:
            return render_to_response(Html.error_403)

        url = Url.accountDetail(id, Url.url)
        r = requests.get(url)
        p = json.loads(r.text)

        return redirect(Path.accouuntList)
    except Exception as ex:
        log.error(FuncCode.accountDetail.value, None, ex)

        return render(request, Html.accountDelete, {'account': '', 'message': str(ex)})
