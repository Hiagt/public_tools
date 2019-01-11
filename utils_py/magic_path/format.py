# -*- coding: utf-8 -*-

"""
@Time    : 2018/12/27 19:38
@Author  : Hiagt
@File    : format.py
@Software: PyCharm
"""

import os.path as op


def normpath(path):
    """格式化路径，消除斜杠等."""
    if isinstance(path, bytes):
        sep = b'\\'
        altsep = b'/'
        curdir = b'.'
        pardir = b'..'
        special_prefixes = (b'\\\\.\\', b'\\\\?\\')
    else:
        sep = '\\'
        altsep = '/'
        curdir = '.'
        pardir = '..'
        special_prefixes = ('\\\\.\\', '\\\\?\\')
    if path.startswith(special_prefixes):
        # in the case of paths with these prefixes:
        # \\.\ -> device names
        # \\?\ -> literal paths
        # do not do any normalization, but return the path unchanged
        return path
    path = path.replace(altsep, sep)
    prefix, path = op.splitdrive(path)

    # collapse initial backslashes
    if path.startswith(sep):
        prefix += sep
        path = path.lstrip(sep)

    comps = path.split(sep)
    i = 0
    while i < len(comps):
        if not comps[i] or comps[i] == curdir:
            del comps[i]
        elif comps[i] == pardir:
            if i > 0 and comps[i - 1] != pardir:
                del comps[i - 1:i + 1]
                i -= 1
            elif i == 0 and prefix.endswith(sep):
                del comps[i]
            else:
                i += 1
        else:
            i += 1
    # If the path is now empty, substitute '.'
    if not prefix and not comps:
        comps.append(curdir)
    return (prefix + sep.join(comps)).replace("\\", "/")
