# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import blueprintForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..utils import BlueprintUtil
from ..utils import StringUtil
from ..utils import SessionUtil
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..enum.OSVersion import OSVersion
from ..logs import log



def blueprintList(request):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','list') == False:
            return render_to_response(Html.error_403)

        blueprints = None
        # -- Get a blueprint list, API call
        url = Url.blueprintList

        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }
        blueprints = ApiUtil.requestGet(url, FuncCode.blueprintList.value, data)

        return render(request, Html.blueprintList, {'blueprints': blueprints, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.blueprintList.value, None, ex)

        return render(request, Html.blueprintList, {"blueprints": '', 'message': str(ex)})


def blueprintDetail(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','read') == False:
            return render_to_response(Html.error_403)

        # -- blueprint DetailAPI call, get a response
        code = FuncCode.blueprintDetail.value

        token = request.session['auth_token']
        pjid = request.session['project_id']
        url = Url.blueprintDetail(id, Url.url)

        data = {
            'auth_token': token
        }
        p = ApiUtil.requestGet(url, code, data)

        pattern = BlueprintUtil.get_pattern_list(code, id, token, pjid)

        return render(request, Html.blueprintDetail, {'blueprint': p, 'pattern': list(pattern), 'message': ''})
    except Exception as ex:
        log.error(FuncCode.blueprintDetail.value, None, ex)

        return render(request, Html.blueprintDetail, {'blueprint': '', 'message': str(ex)})


def blueprintCreate(request):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','create') == False:
            return render_to_response(Html.error_403)

        data = {
            'project_id': request.session['project_id']
        }
        url = Url.patternList
        patterns = ApiUtil.requestGet(
            url, FuncCode.blueprintCreate.value, data)
#         patterns = patterns['lists']
        patternSelect = {
            'patterns': patterns,
            'OSVersion': list(OSVersion),
        }

        if request.method == "GET":

            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            url = Url.patternList

            data.update({
                'OSVersion': list(OSVersion),
            })

            return render(request, Html.blueprintCreate, {'blueprint': data, 'patternSelect': patternSelect,
                                                          'form': '', 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST

            # -- Validate check
            form = blueprintForm(p)
            if not form.is_valid():
                cpPost = p.copy()

                return render(request, Html.blueprintCreate, {'blueprint': cpPost, 'patternSelect': patternSelect,
                                                              'form': form, 'message': ''})


            # -- 1.Create a blueprint, api call
            url = Url.blueprintCreate
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'description': p['description'],
            }

            blueprint = ApiUtil.requestPost(
                url, FuncCode.blueprintCreate.value, data)

            # -- 2. Add a Pattern, api call
            url2 = Url.blueprintPattrnCreate(blueprint.get('id'), Url.url)
            data = {
                'auth_token': p['auth_token'],
                'pattern_id': p['project_id'],
                'revison': p.get('revison'),
                'os_version': p.get('os_version'),
            }

#             ApiUtil.requestPost(url2, FuncCode.blueprintCreate.value, data)
#
#             # -- 3. BlueprintHistory, api call
#             url3 = Url.blueprintHistoriesParameters(blueprint['id'], Url.url)
#             data = {
#                 'auth_token': p['auth_token'],
#             }
#
#             ApiUtil.requestPost(url3, FuncCode.blueprintCreate.value, data)

            return redirect(Path.blueprintList)
    except Exception as ex:
        log.error(FuncCode.blueprintCreate.value, None, ex)

        return render(request, Html.blueprintCreate, {'blueprint': request.POST, 'form': '', 'message': str(ex)})


def blueprintEdit(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','update') == False:
            return render_to_response(Html.error_403)

        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }
        url = Url.patternList
        patterns = ApiUtil.requestGet(
            url, FuncCode.blueprintCreate.value, data)
#         patterns = patterns['lists']
        patternSelect = {
            'patterns': patterns,
            'OSVersion': list(OSVersion),
        }

        print(patternSelect)

        if request.method == "GET":

            url = Url.blueprintDetail(id, Url.url)

            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            p = ApiUtil.requestGet(url, FuncCode.blueprintEdit.value, data)
            p.update(data)

            url = Url.patternList
            patterns = ApiUtil.requestGet(
                url, FuncCode.blueprintCreate.value, data)


            return render(request, Html.blueprintEdit, {'blueprint': p, 'patternSelect': patternSelect,
                                                        'form': '', 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = blueprintForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.blueprintEdit, {'blueprint': p, 'patternSelect': patternSelect,
                                                            'form': form, 'message': msg})

            # -- Create a blueprint, api call
            url = Url.blueprintEdit(id, Url.url)
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'description': p['description'],
#                 'patterns_attributes': p['patterns_attributes'],
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.blueprintEdit.value, data)

            return redirect(Path.blueprintList)
    except Exception as ex:
        log.error(FuncCode.blueprintEdit.value, None, ex)

        return render(request, Html.blueprintEdit, {'blueprint': request.POST, 'patternSelect': '',
                                                    'form': '', 'message': str(ex)})


def blueprintDelete(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','destroy') == False:
            return render_to_response(Html.error_403)

        # -- URL and data set
        url = Url.blueprintDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.blueprintDelete.value, data)

        return redirect(Path.blueprintList)
    except Exception as ex:
        log.error(FuncCode.blueprintDelete.value, None, ex)

        return render(request, Html.blueprintDetail, {'blueprint': '', 'message': ex})
