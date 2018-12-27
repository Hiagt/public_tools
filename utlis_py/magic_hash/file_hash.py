# -*- coding: utf-8 -*-

"""
@Time    : 2018/12/27 19:15
@Author  : Hiagt
@File    : file_hash.py
@Software: PyCharm

文件hash
"""
import hashlib

from . import BLOCK_SIZE


def file_md5(file_dir):
    """
    :param file_dir: 接受文件地址
    :return: 文件MD5
    """
    my_hash = hashlib.md5()
    f_dir = file_dir.decode('utf-8')
    # 以二进制打开文件
    with open(f_dir, 'rb') as openfile:
        while True:
            data = openfile.read(BLOCK_SIZE)
            if not data:
                break
            my_hash.update(data)
    return my_hash.hexdigest()


def file_sha1(file_dir):
    """
    :param file_dir: 接受文件地址
    :return: 文件sha1
    """
    my_hash = hashlib.sha1()
    with open(file_dir, 'rb') as openfile:
        while True:
            data = openfile.read(BLOCK_SIZE)
            if not data:
                break
            my_hash.update(data)
    return my_hash.hexdigest()
