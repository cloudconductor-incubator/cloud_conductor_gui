from logging import getLogger
import json
# logger = getLogger(__name__)
logger = getLogger('app')


def info(scid, res, parm, msg):
    if res != None:
        response = str(res.status_code) + ':' + res.reason
        url = ', ' + res.url
        logger.info(response + ', ' + scid + ', ' + msg + url)
    elif parm != None:
        logger.info(scid + ', ' + msg + parm)
    else:
        logger.info(scid + ', ' + msg)


def debug(scid, msg, res, param):
    if param != None:
        logger.debug(scid + ' Message:' + msg + ' Response:' + res, param)
    else:
        logger.error(scid + ' Message:' + msg)


def error(scid, res, ex):
    msg = None

    if res != None and ex != None:
        response = str(res.status_code) + ':' + res.reason

        if res.status_code == 400:
            msg = ''

        elif res.status_code == 401:
            msg = ''

        elif res.status_code == 403:
            msg = ''

        elif res.status_code == 404:
            msg = ''

        elif res.status_code == 500:
            msg = ''

        elif res.status_code == 101:
            msg = ''

        elif res.status_code == 102:
            msg = ''

        elif res.status_code == 901:
            msg = ''

        elif res.status_code == 902:
            msg = ''
        else:
            msg = ''

        logger.error(response + ', ' + scid + ', ' + msg + str(ex))
    if res != None and ex == None:
        msg = ''
        response = str(res.status_code) + ':' + res.reason

        logger.error(response + ', ' + scid + ', ' + msg)
    else:
        logger.error(scid + ', ' + str(ex))


def errorMessage(res, ex):
    msg = ''
    response = ''

    if not res and not ex:

        if res.status_code == 400:
            msg = ''

        elif res.status_code == 401:
            msg = ''

        elif res.status_code == 403:
            msg = ''

        elif res.status_code == 404:
            msg = ''

        elif res.status_code == 500:
            msg = ''

        elif res.status_code == 101:
            msg = ''

        elif res.status_code == 102:
            msg = ''

        elif res.status_code == 901:
            msg = ''

        elif res.status_code == 902:
            msg = ''
        else:
            msg = ''

        errormsg = apiErrorMessage(res)

        return errormsg + ', ' + msg + str(ex)

    elif not res and ex:

        errormsg = apiErrorMessage(res)
        return errormsg + ', ' + msg

    else:
        return str(ex)


def apiErrorMessage(res):
    response =  json.loads(res.text)
    apimsg = response.get('error')
    errormsg = str(res.status_code) + ':' + res.reason + '  '+ apimsg

    return errormsg