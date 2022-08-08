import os
import time
import threading
from django.shortcuts import get_object_or_404
from ninja import Router
from seldom.utils import file
from app_project.models import Project
from app_case.models import TestCase, CaseResult
from app_utils.response import response, Error
from app_case.api_schma import RunCaseIn
from app_case.api_utils import thread_run_case

router = Router(tags=["case"])


@router.post('/{case_id}/running')
def running_case(request, case_id: int, run_case: RunCaseIn):
    """
    运行测试用例
    """
    # 运行环境
    env = run_case.env

    case = get_object_or_404(TestCase, pk=case_id)
    case.status = 1
    case.save()

    case_info = [{
        "file": case.file_name,
        "class": {
            "name": case.class_name,
            "doc": case.class_doc
        },
        "method": {
            "name": case.case_name,
            "doc": case.case_doc
        }
    }]

    # 项目目录添加环境变量
    project = Project.objects.get(id=case.project_id)
    file.add_to_path(project.address)
    test_dir = os.path.join(project.address, "TestCase")

    # 定义报告
    report_name = f'{str(time.time()).split(".")[0]}.xml'
    # 丢给线程执行用例
    threads = []
    t = threading.Thread(target=thread_run_case, args=(test_dir, case_info, report_name, case.id, env))
    threads.append(t)
    for t in threads:
        t.start()

    return response()


@router.post('/{case_id}/result')
def get_case_result(request, case_id: int):
    """
    获得测试用例
    """
    results = CaseResult.objects.filter(case_id=case_id).order_by("-create_time")
    if len(results) == 0:
        result = []
    else:
        result = results[0]
    return response(result=result)
