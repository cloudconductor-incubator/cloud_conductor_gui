# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import blueprintForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import PatternUtil
from ..utils import BlueprintUtil
from ..utils import BlueprintPatternUtil
from ..utils import SessionUtil
from ..utils import StringUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..enum.FunctionCode import FuncCode
from ..enum.OSVersion import OSVersion
from ..logs import log
from _ast import List


def blueprintList(request):
    blueprints = None
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','list') == False:
            return render_to_response(Html.error_403)


        # -- Get a blueprint list, API call
        project_id = request.session['project_id']
        token = request.session['auth_token']
        blueprints = BlueprintUtil.get_blueprint_list(FuncCode.blueprintList.value, token, project_id)

        return render(request, Html.blueprintList, {'blueprints': blueprints, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.blueprintList.value, None, ex)

        return render(request, Html.blueprintList, {"blueprints": '', 'message': str(ex)})


def blueprintDetail(request, id):
    code = FuncCode.blueprintDetail.value
    pattern = ''
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','read') == False:
            return render_to_response(Html.error_403)

        token = request.session['auth_token']
        project_id = request.session['project_id']

        # -- blueprint DetailAPI call, get a response
        blueprint = BlueprintUtil.get_bluepritn_detail(code, token, id)
        pattern = BlueprintUtil.get_pattern_list(code, id, token, project_id)

        return render(request, Html.blueprintDetail, {'blueprint': blueprint, 'pattern': pattern, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.blueprintDetail.value, None, ex)

        return render(request, Html.blueprintDetail, {'blueprint': '', 'message': str(ex)})


def blueprintCreate(request):
    code = FuncCode.blueprintCreate.value
    osversion = list(OSVersion)
    patterns = ''
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','create') == False:
            return render_to_response(Html.error_403)

        project_id = request.session['project_id']
        token = request.session['auth_token']
        patterns = PatternUtil.get_pattern_list(code, token, project_id)

        if request.method == "GET":

            return render(request, Html.blueprintCreate, {'blueprint': '', 'patterns': patterns, 'osversion': osversion,
                                                          'form': '', 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST

            # -- Validate check
            form = blueprintForm(p)
            if not form.is_valid():

                return render(request, Html.blueprintCreate, {'blueprint': p, 'patterns': patterns,
                                                              'osversion': osversion, 'form': form, 'message': ''})

            # -- 1.Create a blueprint, api call
            blueprint = BlueprintUtil.create_blueprint(code, token, project_id, form.data)

            # -- 2. Add a Pattern, api call
            BlueprintPatternUtil.add_blueprint_pattern_list(code, token, blueprint.get('id'),
                                                            p.getlist('os_version'), p.getlist('pattern_id'))

#           # -- 3. BlueprintBuild, api call
            BlueprintUtil.create_bluepritn_build(code, token, blueprint.get('id'))

            return redirect(Path.blueprintList)
    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.blueprintCreate, {'blueprint': request.POST, 'patterns': patterns,
                                                      'osversion': osversion, 'form': '', 'message': str(ex)})

def blueprintEdit(request, id):
    code = FuncCode.blueprintEdit.value
    osversion = list(OSVersion)
    blueprint = ''
    patterns = ''
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'blueprint','update') == False:
            return render_to_response(Html.error_403)

        project_id = request.session['project_id']
        token = request.session['auth_token']

        blueprint = BlueprintUtil.get_bluepritn_detail(code, token, id)
        patterns = PatternUtil.get_pattern_list(code, token, project_id)
        pattern_list = BlueprintPatternUtil.get_blueprint_pattern_list2(code, token, id)
        print(pattern_list)

        if request.method == "GET":

            return render(request, Html.blueprintEdit, {'blueprint': blueprint, 'patterns': patterns, 'pattern_list': pattern_list,
                                                        'osversion': osversion, 'form': '', 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = blueprintForm(p)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.blueprintEdit, {'blueprint': p, 'patterns': patterns,
                                                            'osversion': osversion, 'form': form, 'message': ''})

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

        return render(request, Html.blueprintEdit, {'blueprint': request.POST, 'patterns': patterns,
                                                    'osversion': osversion, 'form': '', 'message': str(ex)})


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
