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
    if param is not None:
        param = ast.literal_eval(param)

    return param


def stringToDictList(list):
    dic_list = []
    if list is not None:
        for r in list:
            dic_list.append(stringToDict(r))

    return dic_list


def putKeyVlue(param):

    param = stringToDict(param)
    if param is not None:
        param = ast.literal_eval(param)

        for k, v in param.items():
            print('key:', k)

    return param


def list_to_record(list):

    if isEmpty(list):
        return None

    record = None

    for param in list:
        record = param
        break

    return record
