# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/9 9:55
@Auth ： zt

"""

import pytest
import configparser
from py.xml import html
from py._xmlgen import html
from common import yaml_util
from common.Login import login

from common.read_config import ReadConfig
conf = ReadConfig("../conf/conf.ini")

# 定义一个全局变量，用于存储内容
global_data = {}


@pytest.fixture(scope="session")
def set_global_data():
    """
    设置全局变量，用于关联参数
    :return:
    """

    def _set_global_data(key, value):
        global_data[key] = value

    return _set_global_data


@pytest.fixture(scope="session")
def get_global_data():
    """
    从全局变量global_data中取值
    :return:
    """

    def _get_global_data(key):
        return global_data.get(key)

    return _get_global_data


# @pytest.fixture(scope="session")
# def pytest_configure():
#     # 读取配置文件
#
#     config_file = "../conf/conf.ini"  # 文件路径
#     config = configparser.ConfigParser(allow_no_value=True)
#     conf = config.read(config_file, encoding="utf-8")
#
#     return conf
#
#
# @pytest.fixture(scope="session")
# def get_db_config(pytest_configure):
#     # 获取数据来配置项
#     db_config = {}
#
#     db_config['host'] = pytest_configure.get('EVN', 'host')
#     db_config['port'] = pytest_configure.getint('EVN', 'port')
#     db_config['username'] = pytest_configure.get('EVN', 'username')
#     db_config['password'] = pytest_configure.get('EVN', 'password')
#     db_config['database'] = pytest_configure.get('EVN', 'database')  # 连接数据库
#
#     return db_config
#
#
# @pytest.fixture(scope="session")
# def get_url_config(pytest_configure):
#     # 获取数据来配置项
#     url_config = {}
#     url_config['headers'] = pytest_configure.get("HEADERS", "headers")
#     url_config['url'] = pytest_configure.get("EVN", "url")
#
#     return url_config


@pytest.fixture(scope="class")
def get_Authorization():
    headers = conf.get_headers()
    userdata = conf.get_user()

    login_request = login(userdata["username"], userdata["password"])
    headers['Authorization'] = login_request['data']['token']

    return headers, userdata['username']


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):  #添加summary内容
    prefix.extend([html.p("所属部门: 科创金融业务线/技术开发部")])
    prefix.extend([html.p("测试人员: 张腾")])


def pytest_html_report_title(report):
    report.title = "安徽农担大数据中心web端测试报告"

