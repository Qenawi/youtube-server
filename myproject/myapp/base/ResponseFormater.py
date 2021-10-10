#   Qenawi created ResponseFormater.py at 4/29/21, 11:00 PM
#   ResponseFormater.py @Docs
#

import json
from django.http import JsonResponse

failed_code = 300
success_code = 200
un_auth_code = 408
old_version_code = 405


def clean_response(data, msg):
    response_dict = {"code": success_code}
    if msg is not None:
        response_dict['msg'] = msg
    else:
        response_dict['msg'] = "success"
    response_dict['data'] = data
    print(response_dict)
    return JsonResponse(response_dict)


def error_response(exc):
    response_dict = {"code": failed_code, 'msg': exc.__str__()}

    return JsonResponse(response_dict)


def error_response_from_string(msg):
    response_dict = {}
    response_dict["code"] = failed_code
    response_dict['msg'] = str(msg)
    return JsonResponse(response_dict)


def sucess_response_from_string(msg):
    response_dict = {"code": success_code, 'msg': str(msg)}
    return JsonResponse(response_dict)


def error_response_from_string_with_code(msg, code):
    response_dict = {"code": code, 'msg': str(msg)}
    return JsonResponse(response_dict)
