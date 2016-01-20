# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
from collections import OrderedDict
from ..forms import roleForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..enum.MessageCode import Error
from ..utils import ApiUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..enum.FunctionCode import FuncCode
from ..logs import log


def roleList(request):
    try:
        roles = None
        # -- Get a project list, API call
        code = FuncCode.roleList.value
        token = request.session['auth_token']
        roles = RoleUtil.get_role_list(code, token)

        return render(request, Html.roleList, {'role': roles, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.roleList.value, None, ex)

        return render(request, Html.roleList, {"role": '', 'message': str(ex)})


def roleDetail(request, id):
    try:

        return render(request, Html.roleDetail, {'role': '', 'message': ''})
    except Exception as ex:
        log.error(FuncCode.roleDetail.value, None, ex)

        return render(request, Html.roleDetail, {'role': '', 'message': str(ex)})


def roleCreate(request):

    check_items = []
    check_items.append({"no":"1", "name":"Project", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"project"})
    check_items.append({"no":"2", "name":"Cloud", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"cloud"})
    check_items.append({"no":"3", "name":"BaseImage", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"base_image"})
    check_items.append({"no":"4", "name":"Blueprint", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"blueprint"})
    check_items.append({"no":"5", "name":"System", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"system"})
    check_items.append({"no":"6", "name":"Environment", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"environment"})
    check_items.append({"no":"7", "name":"Application", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"application"})
    check_items.append({"no":"8", "name":"Pattern", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"pattern"})
    check_items.append({"no":"9", "name":"Account", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"account"})
    check_items.append({"no":"10", "name":"Role", "m":"manage", "r":"read", "c":"create", "u":"update", "d":"destroy", "item_name":"role"})

    try:
        code = FuncCode.roleCreate.value
        token = request.session['auth_token']
        project_id= request.session['project_id']


        if request.method == "GET":

            return render(request, Html.roleCreate, {'message': '',
                                                     'role':{"token":token,'project':project_id},
                                                     'items':check_items,'save': True})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST

            form = roleForm(request.POST)
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.roleCreate, {'role': p, 'message': msg, 'items':check_items,'save': True})

            checkbox = False
            for param in request.POST:
                if '-' in param:
                    if param.split('-')[1] in ['manage','create','update','destroy']:
                        checkbox = True
                        break

            if checkbox == False:
                return render(request, Html.roleCreate, {'role': p, 'message': Error.CheckboxNotSelected.value, 'items':check_items,'save': True})

            # -- API call, get a response
            RoleUtil.create_role(code, token,project_id, p.get('name'), p.get('description'),p)

            # -- Validate check

            return redirect(Path.roleList)
    except Exception as ex:
        log.error(FuncCode.roleCreate.value, None, ex)
        return render(request, Html.roleCreate, { 'message': str(ex),'role': request.POST,
                                                 'items':check_items,'save': True},)


def roleEdit(request, id):
    try:
        code = FuncCode.roleEdit.value
        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }

        if request.method == "GET":

            return render(request, Html.roleEdit, {'message': str(ex)})
        else:
            # -- Get a value from a form


            return redirect(Path.roleList)
    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.roleEdit, {'message': str(ex)})

def roleDelete(request, id):
    try:
        # -- URL and data set
        url = Url.roleDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.roleDelete.value, data)

        return redirect(Path.roleList)
    except Exception as ex:
        log.error(FuncCode.roleDelete.value, None, ex)

        return render(request, Html.roleDetail, {'role': '', 'message': ex})
