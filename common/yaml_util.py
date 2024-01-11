# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/5 10:23
@Auth ： zt

"""

import yaml


class yamlUtil():
    def __init__(self, yaml_file):

        '''
        通过init把文件传入到这个类
        :param yaml_file:
        '''

        self.yaml_file = yaml_file

    #读取ymal文件
    def read_yaml(self):

        '''
        读取yaml，将yaml反序列化，就是把我们yaml格式转换成dict格式
        :return:
        '''

        with open(self.yaml_file, encoding="utf-8", mode="r") as f:
            # value = yaml.safe_load(f.read()) #文件流，加载方式
            value = yaml.load(f, Loader=yaml.FullLoader)  # 文件流，加载方式
            return value

    # 写入（追加）
    def write_yaml(self, data):
        with open(self.yaml_file, encoding="utf-8", mode="a+") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 清空
    def clear_yaml(self):
        with open(self.yaml_file, encoding="utf-8", mode="W") as f:
            f.truncate()