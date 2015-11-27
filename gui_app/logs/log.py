from logging import getLogger
# logger = getLogger(__name__)
logger = getLogger('app')


def info(scid, res, parm, msg):
    if res != None :
        response = str(res.status_code) + ':' + res.reason
        url = ', ' + res.url
        logger.info(response + ', ' + scid + ', ' + msg + url )
    elif parm != None:
        logger.info(scid + ', ' + msg + parm )
    else:
        logger.info(scid + ', ' + msg )

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
            msg = 'msg'

        elif res.status_code == 401:
            msg = 'msg'

        elif res.status_code == 403:
            msg = 'msg'

        elif res.status_code == 404:
            msg = 'msg'

        elif res.status_code == 500:
            msg = 'msg'

        elif res.status_code == 101:
            msg = 'msg'

        elif res.status_code == 102:
            msg = 'msg'

        elif res.status_code == 901:
            msg = 'msg'

        elif res.status_code == 902:
            msg = 'msg'
        else:
            msg = 'msg'

        logger.error(response + ', ' + scid + ', ' + msg + str(ex))
    if res != None and ex == None:
        msg = 'msg'
        response = str(res.status_code) + ':' + res.reason

        logger.error(response + ', ' + scid + ', ' + msg)
    else:
        logger.error(scid + ', ' + str(ex) )
