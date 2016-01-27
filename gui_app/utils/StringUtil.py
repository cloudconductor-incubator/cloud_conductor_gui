import re
import ast


def isEmpty(value):
    if value:
        return False
    else:
        return True


def isNotEmpty(value):
    if not value:
        return False
    else:
        return True


def stringToDict(param):
    if param != None:
        param = ast.literal_eval(param)

    return param


def stringToDictList(list):
    dic_list = []
    if list != None:
        for r in list:
            dic_list.append(stringToDict(r))

    return dic_list


def putKeyVlue(param):

    param = stringToDict(param)
    if param != None:
        param = ast.literal_eval(param)

        for k, v in param.items():
            print('key:', k)

    return param