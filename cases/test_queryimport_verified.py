# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/5 11:02
@Auth ： zt

"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(curPath)

import pytest
import pandas
import numpy
import wget
import requests
import urllib.parse
from common import Log
from common import yaml_util
from common import sendhttp
from common.read_config import ReadConfig
from common import Login
from urllib import parse

from urllib.request import urlopen
import io
from openpyxl import load_workbook

log = Log.TestLog(logger='test_queryimport_verified').get_log()
conf = ReadConfig("../conf/conf.ini")

# import importlib, sys
# importlib.reload(sys)
# # print(sys.path)


@pytest.mark.test_queryimport
@pytest.mark.parametrize("args", yaml_util.yamlUtil("../data/queryimport_verified.yaml").read_yaml())
class TestQueryImport(object):

    def test_passorderlist(self, args, get_Authorization):
        """
        检查列表数据列表查询与导出数据的一致性
        :return:
        """
        url = conf.get_url()
        url_list = url+args['url_list']
        url_export = url+args['url_export']

        headers = get_Authorization[0]

        args['payload']['registerName'] = get_Authorization[1]
        payload = args['payload']

        response01 = sendhttp.send_http(url=url_list, method="POST", headers=headers, data=payload)
        response02 = sendhttp.send_http(url=url_export, method="POST", headers=headers, data=payload)

        if response01['status'] == "success":  # 接口请求成功
            # set_global_data("passorderlist", response01)

            if args['amountbloor'] == "1":
                total_amount = response01["data"][args['amount_data']]
            total_sum = response01["data"]["total"]

            msg = "【检查点1】"+args['interfaceName']+"获取接口调用成功"
            log.info(msg)
            assert response01['code'] == 1, msg

            if response02['status'] == "success":  # 接口请求成功
                msg = ("【检查点2】"+args['interfaceName']+"导出接口调用成功,文件链接为%s" %response02['data'])
                log.info(msg)
                assert response02['data'] != "", msg
            else:
                log.error("【FAIL】"+args['interfaceName']+"导出接口调用失败|%s" % str(response01))
                assert 0

            data_excel = pandas.read_excel(response02['data'])

            data_excel_num = data_excel.shape[0]

            if args['amountbloor'] == "1":
                data_excel_amount = 0
                if args['amount_type'] == "申请1":
                    for data in data_excel['申请金额（万元）']:
                        data_excel_amount += data
                elif args['amount_type'] == "申请2":
                    for data in data_excel['申请金额(万元)']:
                        data_excel_amount += data
                elif args['amount_type'] == "担保":
                    for data in data_excel['担保金额(万元)']:
                        data_excel_amount += data
                elif args['amount_type'] == "贷款":
                    for data in data_excel['贷款金额（元）']:
                        data_excel_amount += data
                elif args['amount_type'] == "代偿":
                    data_dai = data_excel[data_excel['申请状态'] == "审批通过"]
                    for data in data_dai['实付应代偿总额（元）']:
                        if data > 0:
                            data_excel_amount += data / 10000
                elif args['amount_type'] == "保费":
                    for data in data_excel['实收保费（元）']:
                        data_int = float(data)
                        data_excel_amount += data_int / 10000

            if total_sum == data_excel_num:
                if args['amountbloor'] == "1":
                    if numpy.allclose(total_amount, float(data_excel_amount)):
                        msg = ("【检查点3】列表与导出数据一致，共%s条，总金额%s万元" %(total_sum,total_amount))
                        log.info(msg)
                        assert 1 == 1 # assert 1 == 1
                    else:
                        log.error("【FAIL】总金额：列表与导出数据不一致，列表共%s条，总金额%s万元；表格共%s条，总金额%s万元" % (total_sum,total_amount,data_excel_num,data_excel_amount))
                        assert 0  # assert 0
                else:
                    log.info("【检查点3】总金额：列表与导出数据总数一致，共%s条；" % (total_sum))
                    assert 1 == 1
            else:
                log.error("【FAIL】总数：列表与导出数据不一致，列表共%s条，总金额%s万元；表格共%s条，总金额%s万元" % (total_sum, total_amount, data_excel_num, data_excel_amount))
                assert 0

        else:
            log.error("【FAIL】"+args['interfaceName']+"获取接口调用失败|%s" % str(response01))
            assert 0
            #
            # # 原始链接及其参数
            # params = dict(parse.parse_qsl(parse.urlsplit(response02['data']).query))
            #
            # # 重新定义参数顺序
            # new_order = ["productCode", "uid", "timestamp", "authKey", "attName"]
            # reordered_params = {key: params[key] for key in new_order}
            #
            # # 构建新的链接,unquote--转码
            # new_link = urllib.parse.unquote(response02['data'][:-len(parse.urlsplit(response02['data']).query)]  + parse.urlencode(reordered_params))
            # print("新的链接为：", new_link)
            # #
            # # # 调用网页上的excel文件，需要采用post请求
            # # ret = requests.post(response02['data'])
            #
            # index_of_questionmark = response02['data'].find("?")
            # if index_of_questionmark != -1:
            #     # 如果存在"?",则截取其前面的部分
            #     result = response02['data'][:index_of_questionmark]
            #     print(result)
            # else:
            #     # 否则返回原始URL
            #     result = response02['data']

if __name__ == '__main__':

    pytest.main(["-ra", '-v', '-x', '-m test_queryimport_verified', "--html=./report/report.html", '--capture=sys'])