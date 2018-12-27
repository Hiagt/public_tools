# -*- coding: utf-8 -*-

"""
@Time    : 2018/12/27 19:21
@Author  : Hiagt
@File    : io_hash.py
@Software: PyCharm
"""
import hashlib

from . import BLOCK_SIZE


def io_md5(io_obj):
    my_hash = hashlib.md5()
    io_obj.seek(0)
    while True:
        data = io_obj.read(BLOCK_SIZE)
        if not data:
            break
        my_hash.update(data)
    return my_hash.hexdigest()


def io_sha1(io_obj):
    my_hash = hashlib.sha1()
    io_obj.seek(0)
    while True:
        data = io_obj.read(BLOCK_SIZE)
        if not data:
            break
        my_hash.update(data)
    return my_hash.hexdigest()

