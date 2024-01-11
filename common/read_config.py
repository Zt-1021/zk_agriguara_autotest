# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/5 10:22
@Auth ： zt

"""

import os
import codecs
import configparser
from common import Log

# proDir = os.path.split(os.path.realpath(__file__))[0]
# configPath = os.path.join(proDir, "config.ini")
log = Log.TestLog(logger='read_config').get_log()


class ReadConfig:
    def __init__(self, configPath):
        # fd = open(configPath)
        # data = fd.read()

        # #  remove BOM
        # if data[:3] == codecs.BOM_UTF8:
        #     data = data[3:]
        #     file = codecs.open(configPath, "w")
        #     file.write(data)
        #     file.close()
        # fd.close()

        self.cf = configparser.ConfigParser(allow_no_value=True)
        self.cf.read(configPath, encoding="utf-8")
        self.sec = ""

    # 获取所有节点
    def get_sections(self):
        sections = self.cf.sections()
        return sections

    # 获取某节点下所有的选项
    def get_opthions(self, section):
        opthions = self.cf.options(section)
        return opthions

    # 获取某节点下的某个选项
    def get_value(self, section, option):
        value = self.cf.get(section, option)
        return value

    # 获取某个节点下所有的选项及选项值(获取元组列表)
    def get_data(self, section):
        data = self.cf.items(section)
        return data

    # 切换环境
    def get_env_data(self,env):

        if env == "test":
            self.sec = "TEST_EVN"
        elif env == "pre":
            self.sec = "PRE_EVN"
        else:
            log.error("无对应环境配置{0}" .format(self.sec))

        return self.sec

    # 添加并写入某节点下的选项及选项值
    def addwrite_opt(self, section, option, value):
        self.cf.set(section, option, value)
        with open('conf.ini', 'w+') as file:
            self.cf.write(file)

    # # 添加节点(有相同节点时会报错，因此需判断)
    # def add_section(self, section):
    #     if section not in self.cf.sections():
    #         self.cf.add_section(section)
    #
    # # 添加某节点下的选项及选项值
    # add_option = conf.set(section='test', option='name', value='vv')
    # print(conf.items(section='test'))
    # with open('conf.ini', 'w+') as file:
    #     conf.write(file)
    #
    # # 移除节点
    # del_section = 'test'
    # if del_section in sections:
    #     conf.remove_section(section=del_section)
    # with open('conf.ini', 'w+') as file:
    #     conf.write(file)
    #
    # # 移除节点下的选项
    # conf.remove_option(section='test', option='name')
    # with open('conf.ini', 'w+') as file:
    #     conf.write(file)

    def get_url(self):
        url = self.cf.get("EVN","url")
        return url

    def get_headers(self):

        headers_config = {}

        headers_config['Host'] = self.cf.get('HEADERS', 'Host')
        headers_config['Content-Length'] = self.cf.get('HEADERS', 'Content-Length')
        headers_config['Content-Type'] = self.cf.get('HEADERS', 'Content-Type')
        headers_config['Ndversion'] = self.cf.get('HEADERS', 'Ndversion')

        return headers_config

    def get_db(self):

        db_config = {}

        db_config['host'] = self.cf.get('EVN', 'host')
        db_config['port'] = self.cf.getint('EVN', 'port')
        db_config['username'] = self.cf.get('EVN', 'username')
        db_config['password'] = self.cf.get('EVN', 'password')
        db_config['database'] = self.cf.get('EVN', 'database')  # 连接数据库

        return db_config

    def get_user(self):

        user = {}
        user['username'] = self.cf.get('EVN', 'user01_name')
        user['password'] = self.cf.get('EVN', 'user01_password')

        return user



# # 查询类方法
# secs = config.sections()  # 获取所有的节点名称
# print("所有的节点名称:", secs)
# options = config.options('logging')  # 获取指定节点的所有key
# print("指定节点的所有key:", options)
# item_list = config.items('logging')  # 获取指定节点的键值对
# print("指定节点的键值对:", item_list)
# val = config.get('logging', 'path')  # 获取指定节点的指定key的value
# print("指定节点的指定key的value:", val)
# val = config.has_section('mysql66')  # 检查指定节点是否存在，返回True或False
# print("指定节点是否存在:", val)
# val = config.has_option('mysql', 'port')  # 检查指定节点中是否存在某个key，返回True或False
# print("指定节点中是否存在某个key:", val)
#
# # 修改配置类方法:增删改
# config.add_section("user")  # 添加一个节点，节点名为user, 此时添加的节点node尚未写入文件
# config.write(open('./conf/test.conf', "w"))  # 将添加的节点user写入配置文件
# secs = config.sections()  # 获取所有的节点名称
# print("修改配置类-add-所有的节点名称:", secs)
#
# config.remove_section("user")  # 删除一个节点，节点名为user, 删掉了内存中的节点user
# config.write(open("./conf/test.conf", "w"))  # 将删除节点node后的文件内容回写到配置文件
# secs = config.sections()  # 获取所有的节点名称
# print("修改配置类-del-所有的节点名称:", secs)
#
# config.set("logging", "user_name", "xiaoming")  # 在已存在的节点中添加一个键值对k1 = v1 ,如果该节点不存在则报错,如果key已经存在，则修改value
# config.write(open("./conf/test.conf", "w"))
# item_list = config.items('logging')  # 获取指定节点的键值对
# print("修改配置类-add option-指定节点的键值对:", item_list)
#
# config.set("logging", "user_name", "zhangsan")  # 在已存在的节点中添加一个键值对k1 = v1 ,如果该节点不存在则报错,如果key已经存在，则修改value
# config.write(open("./conf/test.conf", "w"))
# item_list = config.items('logging')  # 获取指定节点的键值对
# print("修改配置类-update option-指定节点的键值对:", item_list)