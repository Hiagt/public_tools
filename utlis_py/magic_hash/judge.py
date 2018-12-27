# -*- coding: utf-8 -*-

"""
@Time    : 2018/12/27 19:11
@Author  : Hiagt
@File    : judge.py
@Software: PyCharm

判断是否是某种hash值
"""

__hex__ = "0123456789ABCDEFabcdef"


def is_md5(obj_str):
    """
    :param obj_str:   string
    :return:    是否符合md5规则
    """
    if len(obj_str) == 32 and is_hex(obj_str):
        return True
    return False


def is_sha1(obj_str):
    """
    :param obj_str: string
    :return:  是否符合sha1规则
    """
    if len(obj_str) == 40 and is_hex(obj_str):
        return True
    return False
    pass


def is_hex(obj_str):
    if obj_str is None:
        return False
    for x in obj_str:
        if x not in __hex__:
            return False
    return True


