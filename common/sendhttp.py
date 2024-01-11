# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/5 9:59
@Auth ： zt

"""
import requests
import json
import traceback
from common import Log

log = Log.TestLog(logger='send_http').get_log()


def send_http(url, method, headers, data):
    if method == 'POST':
        response = requests.request(url=url, method="POST", headers=headers, data=json.dumps(data))

    elif method == "GET":
        response = requests.request(url=url, method="GET", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        try:
            response_json = json.loads(response.text)
            return response_json
        except Exception as error:
            print(error)
            log.error(traceback.format_exc())
    else:
        log.error("【FAIL】HTTP请求失败|%s" % str(response))
