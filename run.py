# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/8 9:01
@Auth ： zt

"""
import pytest
from datetime import datetime
random_time = datetime.now().strftime('%Y%m%d%H%M%S')


if __name__ == '__main__':

    # pytest.main(["-v"])  # 执行所有case
    # pytest.main(["-q", "-s", "-ra", "main.py"])
    # pytest.main(["-ra", '-v', '-x', '-k=test_begin', '--html=./report/report.html', '--capture=sys'])  # 运行指定标签用例
    # pytest.main(["-ra", '-v', '-x', '--html=./report/report.html', '--capture=sys'])  # 默认格式报告
    # pytest.main(["-ra", '-v', '-x', '--html=./report/report_%s.html' % random_time, '--capture=sys'])  # 带时间格式报告
    # pytest.main(['-v', '-q', '--alluredir', './report1.html'])
    # pytest.main(["-ra", '-v', '-x', '-m=test_send_uncheck_list', '--html=./report/report.html', '--capture=sys'])
    # pytest.main(["-ra", '-v', '-x', '-m test_queryimport', '--html=./report/report.html', '--capture=sys'])
    # pytest.main(["-ra", '-v', '-x', '-m test_send_verified_unpass', '--html=./report/report.html', '--capture=sys'])
    pytest.main(["-ra", '-v', '-x', '-m test_queryimport_verified', "--html=./report/report.html", '--capture=sys'])


# import schedule
# import os
# import time
#
# def start(cmd):
#     os.system(cmd)
#     print('自动化测试用例执行完成：%s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# # 设置每5秒执行一次程序
# # schedule.every(5).seconds.do(start, 'pytest -vs test_queryimport_verified.py')
#
# schedule.every(10).minutes.do(start, "pytest.main(['-ra', '-v', '-x', '-m test_queryimport_verified', '--html=./report/report.html', '--capture=sys'])")
#
#
# # schedule.every(10).minutes.do(执行程序函数名)   # 每10分钟执行一次
# # schedule.every().hour.do(执行程序函数名)   # 每小时执行一次
# # schedule.every().day.at("11:30").do(执行程序函数名) # 每天11点半执行
# # schedule.every().monday.do(执行程序函数名) # 每周一执行
# # schedule.every().wednesday.at("15:15").do(执行程序函数名) # 每周三15点15执
#
#
# while True:
#     schedule.run_pending()  # 运行所有可运行的任务
#     time.sleep(1)