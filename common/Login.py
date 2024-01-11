# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/5 10:02
@Auth ： zt

"""
from common.sendhttp import send_http
from common.read_config import ReadConfig

conf = ReadConfig("../conf/conf.ini")


def login(username, password):

    url = conf.get_url()
    url_login = url + "/hkm-auth/server/auth/login"
    headers = conf.get_headers()
    payload = {
                "password": password,
                "username": username
              }

    login_request = send_http(url=url_login, method="POST", headers=headers, data=payload)

    return login_request