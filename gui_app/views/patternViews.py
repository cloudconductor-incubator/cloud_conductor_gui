# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
import json
from collections import OrderedDict
from ..forms import patternForm
from ..utils import ApiUtil
from ..utils import SessionUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..enum.FunctionCode import FuncCode
from ..logs import log


def patternList(request):
    try:
        if not SessionUtil.check_login(request):
            return redirect(Path.logout)
        if not SessionUtil.check_permission(request, 'pattern', 'list'):
            return render_to_response(Html.error_403)

        patterns = None
        # -- Get a pattern list, API call
        url = Url.patternList
        print(url)

        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }
        patterns = ApiUtil.requestGet(url, FuncCode.patternList.value, data)
#         patterns = patterns['lists']

        return render(request, Html.patternList,
                      {'patterns': patterns, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.patternList.value, None, ex)

        return render(request, Html.patternList,
                      {"patterns": '', 'message': str(ex)})


def patternDetail(request, id):
    try:
        if not SessionUtil.check_login(request):
            return redirect(Path.logout)
        if not SessionUtil.check_permission(request, 'pattern', 'read'):
            return render_to_response(Html.error_403)

        # -- pattern DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.patternDetail(id, Url.url)
        data = {
            'auth_token': token
        }
        p = ApiUtil.requestGet(url, FuncCode.patternDetail.value, data)

        return render(request, Html.patternDetail,
                      {'pattern': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.patternDetail.value, None, ex)

        return render(request, Html.patternDetail,
                      {'pattern': '', 'message': str(ex)})


def patternCreate(request):
    try:
        if not SessionUtil.check_login(request):
            return redirect(Path.logout)
        if not SessionUtil.check_permission(request, 'pattern', 'create'):
            return render_to_response(Html.error_403)

        if request.method == "GET":

            url = Url.environmentList
            p = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }

            return render(request, Html.patternCreate,
                          {'pattern': p, 'form': '', 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            print(p)
            # -- Validate check
            form = patternForm(p)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.patternCreate,
                              {'pattern': p, 'form': form, 'message': ''})

            # -- Create a pattern, api call
            url = Url.patternCreate
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id'],
                'url': p.get('url'),
                'revision': p.get('revision'),
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.patternCreate.value, data)

            return redirect(Path.patternList)
    except Exception as ex:
        log.error(FuncCode.patternCreate.value, None, ex)

        return render(request, Html.patternCreate,
                      {'pattern': request.POST, 'form': '',
                       "message": str(ex)})


def patternEdit(request, id):
    try:
        if not SessionUtil.check_login(request):
            return redirect(Path.logout)
        if not SessionUtil.check_permission(request, 'pattern', 'update'):
            return render_to_response(Html.error_403)

        if request.method == "GET":

            url = Url.patternDetail(id, Url.url)

            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            p = ApiUtil.requestGet(url, FuncCode.patternEdit.value, data)
            p.update(data)

            print(p)

            return render(request, Html.patternEdit,
                          {'pattern': p, 'form': '', 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = patternForm(p)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.patternEdit,
                              {'pattern': p, 'form': form, 'message': ''})

            # -- Create a pattern, api call
            url = Url.patternEdit(id, Url.url)
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': p['project_id'],
                'url': p['url'],
                'revision': p['revision'],
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.patternEdit.value, data)

            return redirect(Path.patternList)
    except Exception as ex:
        log.error(FuncCode.patternEdit.value, None, ex)

        return render(request, Html.patternEdit,
                      {'pattern': request.POST, 'form': '',
                       'message': str(ex)})


def patternDelete(request, id):
    try:
        if not SessionUtil.check_login(request):
            return redirect(Path.logout)
        if not SessionUtil.check_permission(request, 'pattern', 'destroy'):
            return render_to_response(Html.error_403)

        # -- URL and data set
        url = Url.patternDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.patternDelete.value, data)

        return redirect(Path.patternList)
    except Exception as ex:
        log.error(FuncCode.patternDelete.value, None, ex)

        return render(request, Html.patternDetail, {'pattern': '',
                                                    'message': ex})
