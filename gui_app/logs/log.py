from logging import getLogger
# logger = getLogger(__name__)
logger = getLogger('app')


def info(screen, msg, res, param):
    if param != None:

        logger.info(screen + ' Message:' + msg + ' Response:' + res, param)
    else:
        logger.info(screen + ' Message:' + msg)

def debug(screen, msg, res, param):
    if param != None:

        logger.debug(screen + ' Message:' + msg + ' Response:' + res, param)
    else:
        logger.error(screen + ' Message:' + msg)

def error(screen, msg, res, param):
    if param != None:

        logger.error(screen + ' Message:' + msg + ' Response:' + res, param)
    else:
        logger.error(screen + ' Message:' + msg)
