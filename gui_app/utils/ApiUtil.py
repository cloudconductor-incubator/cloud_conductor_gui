import re
import json
import requests
from ..logs import log
from django.conf import settings
from ..utils import StringUtil
from ..enum.ResponseType import Response
from ..enum.LogType import Message
from ..utils.ErrorUtil import ApiError


class Url():
    url = settings.CLOUDCONDUCTOR_URL

    token = url + 'tokens'

    projectList = url + 'projects'
    projectCreate = url + 'projects'
    projectEdit = lambda id, id2: id2 +  'projects/{0}'.format(id)
    projectDetail = lambda id, id2: id2 +  'projects/{0}'.format(id)
    projectDelete = lambda id, id2: id2 +  'projects/{0}'.format(id)

    cloudList = url + 'clouds'
    cloudCreate = url + 'clouds'
    cloudEdit = lambda id, id2: id2 +  'clouds/{0}'.format(id)
    cloudDetail = lambda id, id2: id2 +  'clouds/{0}'.format(id)
    cloudDelete = lambda id, id2: id2 +  'clouds/{0}'.format(id)

    baseImageList = url + 'base_images'
    baseImageCreate = url + 'base_images'
    baseImageEdit = lambda id, id2: id2 +  'base_images/{0}'.format(id)
    baseImageDetail = lambda id, id2: id2 +  'base_images/{0}'.format(id)
    baseImageDelete = lambda id, id2: id2 +  'base_images/{0}'.format(id)

    systemList = url + 'systems'
    systemCreate = url + 'systems'
    systemEdit = lambda id, id2: id2 +  'systems/{0}'.format(id)
    systemDetail = lambda id, id2: id2 +  'systems/{0}'.format(id)
    systemDelete = lambda id, id2: id2 +  'systems/{0}'.format(id)

    applicationList = url + 'applications'
    applicationCreate = url + 'applications'
    applicationEdit = lambda id, id2: id2 +  'applications/{0}'.format(id)
    applicationDetail = lambda id, id2: id2 +  'applications/{0}'.format(id)
    applicationDelete = lambda id, id2: id2 +  'applications/{0}'.format(id)

    applicationDeploy = lambda id, id2: id2 + 'applications/{0}/deploy'.format(id)
    applicationHistoryList = lambda id, id2: id2 + 'applications/{0}/histories'.format(id)
    applicationHistoryDetail = lambda id, id2, id3: id3 + 'applications/{0}/histories/{1}'.format(id, id2)
    applicationHistoryCreate = lambda id, id2: id2 + 'applications/{0}/histories'.format(id)
    applicationHistoryDetail = lambda id, id2, id3: id3 + 'applications/{0}/histories/{1}'.format(id, id2)
    applicationHistoryDelete = lambda id, id2, id3: id3 + 'applications/{0}/histories/{1}'.format(id, id2)

    environmentList = url + 'environments'
    environmentCreate = url + 'environments'
    environmentEdit = lambda id, id2: id2 +  'environments/{0}'.format(id)
    environmentDetail = lambda id, id2: id2 +  'environments/{0}'.format(id)
    environmentDelete = lambda id, id2: id2 +  'environments/{0}'.format(id)

    blueprintList = url + 'blueprints'
    blueprintCreate = url + 'blueprints'
    blueprintEdit = lambda id, id2: id2 +  'blueprints/{0}'.format(id)
    blueprintDetail = lambda id, id2: id2 +  'blueprints/{0}'.format(id)
    blueprintDelete = lambda id, id2: id2 +  'blueprints/{0}'.format(id)
    blueprintBuild = lambda id, id2: id2 +  'blueprints/{0}'.format(id)

    blueprintPattrnList = lambda id, id2: id2 + 'blueprints/{0}/patterns'.format(id)
    blueprintPattrnDetail = lambda id, id2, id3: id3 + 'blueprints/{0}/patterns/{1}'.format(id, id2)
    blueprintPattrnCreate = lambda id, id2: id2 +  'blueprints/{0}/patterns'.format(id)
    blueprintPattrnEdit = lambda id, id2, id3: id3 +  'blueprints/{0}/patterns/{1}'.format(id, id2)
    blueprintPattrnDelete = lambda id, id2, id3: id3 +  'blueprints/{0}/patterns/{1}'.format(id, id2)

    blueprintHistoriesList = lambda id, id2: id2 + 'blueprints/{0}/histories'.format(id)
    blueprintHistoriesParameters = lambda id, id2, id3: id3 + 'blueprints/{0}/histories/{1}/parameters'.format(id, id2)
    blueprintHistoriesEdit = lambda id, id2, id3: id3 +  'blueprints/{0}/histories/{1}'.format(id, id2)
    blueprintHistoriesDetail = lambda id, id2, id3: id3 +  'blueprints/{0}/histories/{1}'.format(id, id2)

    patternList = url + 'patterns'
    patternCreate = url + 'patterns/'
    patternEdit = lambda id, id2: id2 +  'patterns/{0}'.format(id)
    patternDetail = lambda id, id2: id2 +  'patterns/{0}'.format(id)
    patternDelete = lambda id, id2: id2 +  'patterns/{0}'.format(id)

    accountList = url + 'accounts'
    accountCreate = url + 'accounts'
    accountEdit = lambda id, id2: id2 +  'accounts/{0}'.format(id)
    accountDetail = lambda id, id2: id2 +  'accounts/{0}'.format(id)
    accountDelete = lambda id, id2: id2 +  'accounts/{0}'.format(id)

    roleList = url + 'roles'
    roleCreate = url + 'roles'
    roleEdit = lambda id, id2: id2 +  'roles/{0}'.format(id)
    roleDetail = lambda id, id2: id2 +  'roles/{0}'.format(id)
    roleDelete = lambda id, id2: id2 +  'roles/{0}'.format(id)

    permissionList = lambda id, id2: id2 + 'roles/{0}/permissions'.format(id)
    permissionDetail = lambda id, id2, id3: id3 + 'roles/{0}/permissions/{1}'.format(id, id2)
    permissionCreate = lambda id, id2: id2 +  'roles/{0}/permissions'.format(id)
    permissionDelete = lambda id, id2, id3: id3 +  'roles/{0}/permissions/{1}'.format(id, id2)

    assignmentEdit = url + 'assignments'
    assignmentList = url + 'assignments'
    assignmentAdd = url + 'assignments'
    assignmentDelete = lambda id, id2: id2 + 'assignments/{0}'.format(id)
    assignmentRoleList = lambda id, id2: id2 +  'assignments/{0}/roles'.format(id)
    assignmentRoleAdd = lambda id, id2: id2 +  'assignments/{0}/roles'.format(id)
    assignmentRoleDelete = lambda id, id2, id3: id3 +  'assignments/{0}/roles/{1}'.format(id,id2)

    assignmentRoleList = lambda id, id2: id2 + 'assignments/{0}/roles'.format(id)
    assignmentRoleDetail = lambda id, id2, id3: id3 + 'assignments/{0}/roles/{1}'.format(id, id2)
    assignmentRoleCreate = lambda id, id2: id2 +  'assignments/{0}/roles'.format(id)
    assignmentRoleDetail = lambda id, id2, id3: id3 +  'assignments/{0}/roles/{1}'.format(id, id2)

def requestGet(url, scid, payload):
    log.info(scid, None, None, url)
    if payload != None:
        r = requests.get(url, params=payload)
    else:
        r = requests.get(url)
    log.info(scid, r, None, Message.api_url.value)

    if r.status_code == Response.OK.value:
        log.info(scid, None, r.text, Message.api_response.value)
        param =  json.loads(r.text)
        return param
    else:
        raise ApiError(log.errorMessage(r, None))
#         raise ApiError(scid, r)

def requestPost(url, scid, payload): #-- change post
    print(payload)
    if payload != None:
        data=json.dumps(payload)
        print(data)
        r = requests.post(url, data=json.dumps(payload))
#         r = requests.post(url, data=payload)
    else:
        r = requests.post(url)
    log.info(scid, r, None, Message.api_url.value)

    if r.status_code == Response.Created.value or r.status_code == Response.Accepted.value:
        log.info(scid, None, r.text, Message.api_response.value)
        param =  json.loads(r.text)
        print(param)
        return param
    else:
        raise ApiError(log.errorMessage(r, None))

def requestPut(url, scid, payload): #-- change post
    if payload != None:
        r = requests.put(url, data=json.dumps(payload))
    else:
        r = requests.put(url)
    log.info(scid, r, None, Message.api_url.value)

    if r.status_code == Response.OK.value:
        log.info(scid, None, r.text, Message.api_response.value)
        param =  json.loads(r.text)
        return param
    else:
        raise ApiError(log.errorMessage(r, None))

def requestDelete(url, scid, payload): #-- change post
    if payload != None:
        r = requests.delete(url, data=payload)
    else:
        r = requests.delete(url)
    log.info(scid, r, None, Message.api_url.value)

    if r.status_code == Response.No_Content.value:
        json = r.text
        log.info(scid, None, json, Message.api_response.value)

        param = ''
        if StringUtil.isNotEmpty(json):
            param =  json.loads(r.text)

        return param
    else:
        raise ApiError(log.errorMessage(r, None))

def request(req, scid, code):
    if req.status_code == code:
        log.info(scid, None, req.text, Message.api_response.value)
        param =  json.loads(r.text)
        return param
    else:
        log.error(scid, req, None)  #-- nasi
        raise ApiError(log.errorMessage(r, None))
