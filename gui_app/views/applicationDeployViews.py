# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
import ast
from collections import OrderedDict
from ..forms import selecttForm
from ..utils import ApplicationUtil
from ..utils import EnvironmentUtil
from ..utils import StringUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..enum.FunctionCode import FuncCode
from ..logs import log


def applicationSelect(request):
    try:
        session = request.session
        code = FuncCode.appDep_application.value
        token = session.get('auth_token')
        project_id = session.get('project_id')
        application = ''
        list = ''

        list = ApplicationUtil.get_application_list2(
            code, token, project_id)
        print(list)

        if request.method == "GET":
            application = request.session.get('w_app_select')

            return render(request, Html.appdeploy_applicationSelect,
                          {'list': list, 'application': application,
                           'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Session add
            application = StringUtil.stringToDict(param.get('id'))
            form = selecttForm(application)
            if not form.is_valid():

                return render(request, Html.appdeploy_applicationSelect,
                              {'list': list, 'application': application,
                               'form': form, 'message': ''})

            request.session['w_app_select'] = application

            return redirect(Path.appdeploy_environmentSelect)
    except Exception as ex:
        log.error(FuncCode.appDep_application.value, None, ex)

        return render(request, Html.appdeploy_applicationSelect,
                      {'list': list, 'application': application,
                       'message': str(ex)})


def environmentSelect(request):
    list = ''
    try:
        code = FuncCode.appDep_environment.value
        session = request.session
        environment = session.get('w_env_select')
        token = session['auth_token']
        project_id = session['project_id']

        list = EnvironmentUtil.get_environment_list2(
            code, token, project_id)

        if request.method == "GET":

            return render(request, Html.appdeploy_environmentSelect,
                          {"list": list, 'environment': environment,
                           'message': ''})
        elif request.method == "POST":
            param = request.POST

            environment = environmentPut(param)

            form = selecttForm(environment)
            if not form.is_valid():
                return render(request, Html.appdeploy_environmentSelect,
                              {"list": list, 'environment': environment,
                               'form': form,
                               'message': ''})

            request.session['w_env_select'] = environment

            return redirect(Path.appdeploy_confirm)
    except Exception as ex:
        log.error(FuncCode.appDep_environment.value, None, ex)

        return render(request, Html.appdeploy_environmentSelect,
                      {"list": '', 'environment': '', 'message': str(ex)})


def confirm(request):
    try:
        code = FuncCode.appDep_confirm.value
        session = request.session
        app_session = session.get('w_app_select')
        env_session = session.get('w_env_select')

        if request.method == "GET":

            return render(request, Html.appdeploy_confirm,
                          {'application': app_session,
                           'environment': env_session, 'message': ''})
        elif request.method == "POST":
            session = request.session
            code = FuncCode.newapp_confirm.value
            token = session.get('auth_token')
            project_id = ''

            env_id = env_session.get('id')
            app_id = app_session.get('id')

            # -- environment create

            # -- application deploy
            ApplicationUtil.deploy_application(code, token, env_id, app_id)

            # -- session delete
            sessionDelete(session)

            return redirect(Path.top)
    except Exception as ex:
        log.error(FuncCode.newapp_confirm.value, None, ex)
        session = request.session

        return render(request, Html.appdeploy_confirm,
                      {"application": session.get('application'),
                       'environment': session.get('environment'),
                       'message': str(ex)})


def environmentPut(req):
    if StringUtil.isEmpty(req):
        return None

    env = req.get('id', None)
    if StringUtil.isNotEmpty(env):
        env = ast.literal_eval(env)

        environment = {
            'id': str(env.get('id')),
            'name': env.get('name'),
        }
        return environment
    else:
        return env


def putBlueprint(param):

    blueprint = param.get('blueprint', None)
#    if blueprint != None and blueprint != '':
#        blueprint = ast.literal_eval(blueprint)
    if not (blueprint is None) and not (blueprint == ''):
        blueprint = ast.literal_eval(blueprint)

        param['blueprint_id'] = blueprint.get('id')
        param['version'] = blueprint.get('version')

    return param


def sessionDelete(session):

    if 'w_env_select' in session:
        del session['w_env_select']

    if 'w_app_select' in session:
        del session['w_app_select']
