# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from collections import OrderedDict
from ..forms import projectForm
from ..forms import cloudForm
from ..forms import baseImageForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import ProjectUtil
from ..utils import CloudUtil
from ..utils import SystemUtil
from ..utils import EnvironmentUtil
from ..utils import BaseimageUtil
from ..utils import StringUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.CloudType import CloudType
from ..enum.OSVersion import OSVersion
from ..enum.FunctionCode import FuncCode
from ..logs import log


def systemSelect(request):
    try:
        session = request.session

        id = session.get('project_id')
        token = session.get('auth_token')
        code = FuncCode.cloudReg_project.value

        if request.method == "GET":
            list = SystemUtil.get_system_list2(code, token, id)
            print(list)

            return render(request, Html.newapp_systemSelect, {"system": list, 'message': ''})
        elif request.method == "POST":

            p = Path.newapp_applicationCreate
            print(Path.newapp_applicationCreate)

            return redirect('mkappApplicationCreate')

    except Exception as ex:
        log.error(FuncCode.newapp_system.value, None, ex)

        return render(request, Html.newapp_systemSelect, {"system": '', 'message': str(ex)})


# def systemCreate(request):
#     try:
#         if request.method == "GET":
#
#             project = request.session.get('project')
#             p = {'auth_token': request.session['auth_token']}
#             if project:
#                 p.update(project)
#
#             return render(request, Html.newapp_applicationCreate, {"project": p, 'message': ''})
#         elif request.method == "POST":
#             param = request.POST
#             # -- Validate check
#             form = projectForm(param)
#             if not form.is_valid():
#                 project = param.copy()
#                 return render(request, Html.newapp_applicationCreate, {"project": project, 'message': form.errors})
#
#             # -- Session add
#             project = projectPut(param)
#             request.session['project'] = project
#
#             return redirect(Path.newapp_environmntSelect)
#     except Exception as ex:
#         log.error(FuncCode.newapp_applicationCreate.value, None, ex)
#
#         return render(request, Html.newapp_applicationCreate, {"project": request.POST, 'message': str(ex)})


def applicationCreate(request):
    try:
        if request.method == "GET":
            param = {
                     'auth_token': request.session['auth_token'],
                     'project_id': request.session['project_id'],
                     }

            cloud = request.session.get('cloud')
            if StringUtil.isNotEmpty(cloud):
                param.update(cloud)

            return render(request, Html.newapp_applicationCreate, {"cloud": param, 'cloudType': list(CloudType),'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Validate check
            form = cloudForm(param)
            if not form.is_valid():
                cloud = param.copy()

                return render(request, Html.newapp_applicationCreate, {"cloud": cloud, 'cloudType': list(CloudType), 'message': form.errors})

            # -- Session add
            cloud = cloudPut(param)
            request.session['cloud'] = cloud

            return redirect(Path.newapp_environmntSelect)
    except Exception as ex:
        log.error(FuncCode.newapp_applicationCreate.value, None, ex)

        return render(request, Html.newapp_applicationCreate, {"cloud": request.POST, 'cloudType': list(CloudType), 'message': str(ex)})


def environmentSelect(request):
    try:
        if request.method == "GET":
            list = SystemUtil.get_system_list2(code, token, id)
            print(list)

            return render(request, Html.newapp_environmntSelect, {"baseImage": param, 'osversion': list(OSVersion), 'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Validate check
            form = baseImageForm(param)
            if not form.is_valid():
                baseimage = param.copy()

                return render(request, Html.newapp_environmntSelect, {"baseImage": baseimage, 'osversion': list(OSVersion), 'message': form.errors})

            baseimage = baseimagePut(request.POST)
            request.session['baseimage'] = baseimage

            return redirect(Path.newapp_confirm)
    except Exception as ex:
        log.error(FuncCode.newapp_environmntSelect.value, None, ex)

        return render(request, Html.newapp_environmntSelect, {
                                                                  "baseimage": request.POST, 'message': str(ex),
                                                                  'wizard': True})


def confirm(request):
    try:
        session = request.session
        pj_session = session.get('project')
        cl_session = session.get('cloud')
        bi_session = session.get('baseimage')

        if request.method == "GET":

            return render(request, Html.newapp_confirm, {"project": pj_session, 'cloud': cl_session, 'baseImage': bi_session, 'message': ''})
        elif request.method == "POST":
            session = request.session
            code = FuncCode.cloudReg_confirm.value
            token = session.get('auth_token')
            project_id = ''

            print(pj_session)

            # -- project Create
            if pj_session:
                project = ProjectUtil.create_project(code, token, pj_session.get('name'),
                                                     pj_session.get('description'))
                project_id = project.get('id')
            else:
                project_id = session.get('project_id')

            print(project_id)
            # -- cloud Create
            cloud = CloudUtil.create_cloud(code, token, project_id,
                                           cl_session.get('name'), cl_session.get('type'), cl_session.get('key'),
                                           cl_session.get('secret'), cl_session.get('entry_point'),
                                           cl_session.get('tenant_name'), cl_session.get('description'))

            # -- baseimage Create
            print(cloud)
            print(cloud.get('id'))
            baseimage = BaseimageUtil.create_baseimage(code, token, cloud.get('id'), bi_session.get('ssh_username'),
                                                       bi_session.get('source_image'), bi_session.get('os_version'))

            # -- session delete
            sessionDelete(session)

            return redirect(Path.top)
    except Exception as ex:
        log.error(FuncCode.newapp_confirm.value, None, ex)
        session = request.session

        return render(request, Html.newapp_confirm, {"project": session.get('project'),'cloud': session.get('cloud'),
                                                          'baseImage': session.get('baseimage'), 'message': str(ex)})


def projectPut(req):
    if StringUtil.isEmpty(req):
        return None

    project = {
        'name': req.get('name'),
        'description': req.get('description'),
    }
    return project


def cloudPut(req):
    if StringUtil.isEmpty(req):
        return None

    cloud = {
        'name': req.get('name'),
        'type': req.get('type'),
        'key': req.get('key'),
        'secret': req.get('secret'),
        'entry_point': req.get('entry_point'),
        'description': req.get('description'),
        'tenant_name': req.get('tenant_name'),
    }
    return cloud


def baseimagePut(req):
    if StringUtil.isEmpty(req):
        return None

    baseimage = {
        'os_version': req.get('os_version'),
        'source_image': req.get('source_image'),
        'ssh_username': req.get('ssh_username'),
    }
    return baseimage



def sessionDelete(session):

    if 'project' in session:
        del session['project']

    if 'cloud' in session:
        del session['cloud']

    if 'baseimage' in session:
        del session['baseimage']