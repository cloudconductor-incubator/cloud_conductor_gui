# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from django.shortcuts import redirect
from ..forms import accountForm
from ..utils import AccountUtil
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
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
        # -- account DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.accountDetail(id, Url.url)
        print(url)
        data = {
                'auth_token': token
                }
        p = ApiUtil.requestGet(url, FuncCode.accountDetail.value,data)

        return render(request, Html.accountDetail, {'account': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.accountDetail.value, None, ex)

        return render(request, Html.accountDetail, {'account': '', 'message': str(ex)})

def accountCreate(request):

    try:
        token = request.session['auth_token']
        code = FuncCode.accountCreate.value
        list = RoleUtil.get_role_list(code, token, project_id=request.session['project_id'])

        if request.method == "GET":
            data = {
                    'auth_token': token
                    }

            return render(request, Html.accountCreate, {'account': data, 'roleList': list,'message': ''})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = accountForm(request.POST)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.accountCreate, {'account': p, 'message': form.errors})
            # -- AccountCreateAPI call, get a response
            response = AccountUtil.get_account_create(code, token, p['name'], p['email'], p['password'], p['repassword'], p['admin'])

            return redirect(Path.accountList)
    except Exception as ex:
        log.error(FuncCode.accountCreate.value, None, ex)

        return render(request, Html.accountCreate, {'account': request.POST, 'message': ex})


def accountEdit(request, id):
    try:
        if request.method == "GET":
            token = request.session['auth_token']
            url = Url.accountDetail(id, Url.url)
            data = {
                    'auth_token': token
                    }
            p = ApiUtil.requestGet(url, FuncCode.accountEdit.value, data)
            p.update(data)

            return render(request, Html.accountEdit, {'account': p, 'message': ''})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = accountForm(request.POST)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.accountEdit, {'account': p, 'message': msg})

            # -- URL set
            url = Url.accountEdit(id, Url.url)
            # -- Set the value to the form
            data = {
                    'auth_token': request.session['auth_token'],
                    'email': p['email'],
                    'password': p['password'],
                    'repassword': p['repassword'],
                    'admin': p['admin'],
                    'role': p['role'],
                    }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.accountEdit.value, data)

            return redirect(Path.accountList)
    except Exception as ex:
        log.error(FuncCode.accountEdit.value, None, ex)

        return render(request, Html.accountEdit, {'account': request.POST, 'message': ex})


def accountDelete(request, id):
    try:
        url = Url.accountDetail(id, Url.url)
        r = requests.get(url)
        p = json.loads(r.text)

        return redirect(Path.accouuntList)
    except Exception as ex:
        log.error(FuncCode.accountDetail.value, None, ex)

        return render(request, Html.accountDelete, {'account': '', 'message': str(ex)})
