from itertools import chain
from django.http import JsonResponse


class Error:
    """
    子定义错误码与错误信息
    """
    USER_OR_PAWD_NULL = {"10010": "用户名密码为空"}
    USER_OR_PAWD_ERROR = {"10011": "用户名密码错误"}
    PAWD_ERROR = {"10012": "两次密码不一致"}

    ParamsTypeError = {"30020": "参数类型错误"}
    JSON_TYPE_ERROR = {"30030": "JSON格式错误"}

    USER_ID_NULL = {"40010": "用户id不存在"}

    PROJECT_ID_NULL = {"10020": "项目id不存在"}
    PROJECT_OBJECT_NULL = {"10021": "通过id查询项目不存在"}
    PROJECT_DELETE_ERROR = {"10023": "项目删除失败"}

    FILE_TYPE_ERROR = {"10031": "文件类型错误"}
    FILE_SIZE_ERROR = {"10032": "超出文件大小"}

    CASE_AUDIT_FAIL = {"20021": "没有权限审核用例"}
    CASE_AUDIT_NULL = {"20022": "没有审核通过的用例"}


def model_to_dict(instance: object) -> dict:
    """
    对象转字典
    """
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        data[f.name] = f.value_from_object(instance)
    return data


def response(success: bool = True, error: dict = None, result=None):
    """
    自定义接口返回格式
    """
    if error is None:
        error_code = ""
        error_msg = ""
    else:
        success = False
        error_code = list(error.keys())[0]
        error_msg = list(error.values())[0]

    resp = {
        "success": success,
        "error": {
            "code": error_code,
            "message": error_msg
        },
    }

    if result is None:
        resp["result"] = {}
    elif isinstance(result, (list, dict)) is False:
        resp["result"] = model_to_dict(result)
    else:
        resp["result"] = result

    return JsonResponse(resp)
