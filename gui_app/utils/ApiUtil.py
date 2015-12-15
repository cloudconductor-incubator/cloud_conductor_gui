import re
import json
import requests
from ..logs import log
from ..enum.ResponseType import Response
from ..enum.LogType import Message
from ..utils.ErrorUtil import ApiError


class Url():
    url = 'http://127.0.0.1:8000/api/v1/'

    token = url + 'tokens'

    projectList = url + 'projects/'
    projectCreate = url + 'projects/create/'
    projectEdit = lambda id, id2: id2 +  'projects/{0}/update/'.format(id)
    projectDetail = lambda id, id2: id2 +  'projects/{0}/detail/'.format(id)
    projectDelete = lambda id, id2: id2 +  'projects/{0}/delete/'.format(id)
    assignmentList = url + 'assignments/'

    cloudList = url + 'cloud/list/'
    cloudCreate = url + 'cloud/create/'
    cloudEdit = lambda id, id2: id2 +  'cloud/{0}/update/'.format(id)
    cloudDetail = lambda id, id2: id2 +  'cloud/{0}/detail/'.format(id)
    cloudDelete = lambda id, id2: id2 +  'cloud/{0}/delete/'.format(id)

    baseImageList = url + 'base_images/list/'
    baseImageCreate = url + 'base_images/create/'
    baseImageEdit = lambda id, id2: id2 +  'base_images/{0}/update/'.format(id)
    baseImageDetail = lambda id, id2: id2 +  'base_images/{0}/detail/'.format(id)
    baseImageDelete = lambda id, id2: id2 +  'base_images/{0}/delete/'.format(id)

    systemList = url + 'system/list/'
    systemCreate = url + 'system/create/'
    systemEdit = lambda id, id2: id2 +  'system/{0}/update/'.format(id)
    systemDetail = lambda id, id2: id2 +  'system/{0}/detail/'.format(id)
    systemDelete = lambda id, id2: id2 +  'system/{0}/delete/'.format(id)

    applicationList = url + 'application/list/'
    applicationCreate = url + 'application/create/'
    applicationEdit = lambda id, id2: id2 +  'application/{0}/update/'.format(id)
    applicationDetail = lambda id, id2: id2 +  'application/{0}/detail/'.format(id)
    applicationDelete = lambda id, id2: id2 +  'application/{0}/delete/'.format(id)

    environmentList = url + 'environment/list/'
    environmentCreate = url + 'environment/create/'
    environmentEdit = lambda id, id2: id2 +  'environment/{0}/update/'.format(id)
    environmentDetail = lambda id, id2: id2 +  'environment/{0}/detail/'.format(id)
    environmentDelete = lambda id, id2: id2 +  'environment/{0}/delete/'.format(id)

    blueprintList = url + 'blueprint/list/'
    blueprintCreate = url + 'blueprint/create/'
    blueprintEdit = lambda id, id2: id2 +  'blueprint/{0}/update/'.format(id)
    blueprintDetail = lambda id, id2: id2 +  'blueprint/{0}/detail/'.format(id)
    blueprintDelete = lambda id, id2: id2 +  'blueprint/{0}/delete/'.format(id)

    patternList = url + 'pattern/list/'
    patternCreate = url + 'pattern/create/'
    patternEdit = lambda id, id2: id2 +  'pattern/{0}/update/'.format(id)
    patternDetail = lambda id, id2: id2 +  'pattern/{0}/detail/'.format(id)
    patternDelete = lambda id, id2: id2 +  'pattern/{0}/delete/'.format(id)


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
    if payload != None:
        r = requests.get(url, params=payload)
    else:
        r = requests.get(url)
    log.info(scid, r, None, Message.api_url.value)

    if r.status_code == Response.Created.value:
        log.info(scid, None, r.text, Message.api_response.value)
        param =  json.loads(r.text)
        return param
    else:
        raise ApiError(log.errorMessage(r, None))

def requestPut(url, scid, payload): #-- change post
    if payload != None:
        r = requests.get(url, params=payload)
    else:
        r = requests.get(url)
    log.info(scid, r, None, Message.api_url.value)

    if r.status_code == Response.Created.value:
        log.info(scid, None, r.text, Message.api_response.value)
        param =  json.loads(r.text)
        return param
    else:
        raise ApiError(scid, r)

def requestDelete(url, scid, payload): #-- change post
    if payload != None:
        r = requests.get(url, params=payload)
    else:
        r = requests.get(url)
    log.info(scid, r, None, Message.api_url.value)

    if r.status_code == Response.No_Content.value:
        log.info(scid, None, r.text, Message.api_response.value)
        param =  json.loads(r.text)
        return param
    else:
        raise ApiError(scid, r)

def request(req, scid, code):
    if req.status_code == code:
        log.info(scid, None, req.text, Message.api_response.value)
        param =  json.loads(r.text)
        return param
    else:
        log.error(scid, req, None)  #-- nasi
        raise ApiError(scid, r)
