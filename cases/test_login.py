# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/5 9:51
@Auth ： zt

"""
import pytest
from common import Log
from common import yaml_util
from common.sendhttp import send_http
from common.read_config import ReadConfig

log = Log.TestLog(logger='test_login').get_log()
conf = ReadConfig("../conf/conf.ini")


@pytest.mark.test_login
@pytest.mark.parametrize("args", yaml_util.yamlUtil("../data/login.yaml").read_yaml())


class TestLogin(object):

    def test_login(self, args):
        msg = "开始执行登录第{0}条用例：{1}".format(args["id"], args["interfaceName"])
        log.info(msg)
        url = conf.get_url()
        url_login = url+"/hkm-auth/server/auth/login"
        payload = args['payload']
        headers = conf.get_headers()
        response = send_http(url=url_login, method="POST", headers=headers, data=payload)
        try:
            assert args['exceptedresult'] in str(response)
            msg = "{0}用例执行结果：PASS".format(args["interfaceName"])
            log.info(msg)
        except AssertionError as e:
            msg = "{0}用例执行错误：{1}".format(args["interfaceName"], e)
            log.error(msg)
            raise e


# if __name__ == "__main__":
#     pytest.main(["-ra", '-v', '-x', '-k=test_login', '--html=./report/report.html', '--capture=sys'])