# -*- coding: utf-8 -*-

"""
@Time    : 2018/12/27 19:06
@Author  : Hiagt
@File    : str_hash.py
@Software: PyCharm
"""
import hashlib


def md5_str(obj_str):
    """
    :param obj_str:  string
    :return:  字符串的MD5
    """
    md5_hash = hashlib.md5(obj_str.encode(encoding='utf-8'))
    return md5_hash.hexdigest()


def sha1_str(obj_str):
    """
    :param obj_str:  string
    :return:  字符串的sha1
    """
    sha1_hash = hashlib.sha1(obj_str.encode(encoding='utf-8'))
    return sha1_hash.hexdigest()


def sha256_str(obj_str):
    """
    :param obj_str: string
    :return:    字符串的sha1
    """
    sha256_hash = hashlib.sha256(obj_str.encode(encoding='utf-8'))
    return sha256_hash.hexdigest()
