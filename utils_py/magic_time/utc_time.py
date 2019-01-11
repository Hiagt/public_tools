# -*- coding: utf-8 -*-

"""
@Time    : 2018/12/27 17:03
@Author  : Hiagt
@File    : utc_time.py
@Software: PyCharm
"""

import calendar
from datetime import datetime


def timestamp_to_utc_str_time(timestamp):
    """
        将 13 位整数的毫秒时间戳转化成 utc 时间 (字符串格式，含毫秒)
        :param timestamp: 13 位整数的毫秒时间戳 (1456402864242)
        :return: 返回字符串格式 {str}'2016-02-25 12:21:04.242000'
    """
    utc_str_time = datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    return utc_str_time


def timestamp_to_utc_datetime(timestamp):
    """
        将 13 位整数的毫秒时间戳转化成 utc 时间 (datetime 格式)
        :param timestamp: 13 位整数的时间戳 (1456402864242)
        :return: 返回 datetime 格式 {datetime}2016-02-25 12:21:04.242000
    """
    utc_dt_time = datetime.utcfromtimestamp(timestamp / 1000.0)
    return utc_dt_time


def utc_datetime_to_timestamp(utc_datetime):
    """
        将 utc 时间 (datetime 格式) 转为 utc 时间戳
        :param utc_datetime: {datetime}2016-02-25 20:21:04.242000
        :return: 13位 的毫秒时间戳 1456431664242
    """
    utc_timestamp = int(calendar.timegm(utc_datetime.timetuple()) * 1000.0 + utc_datetime.microsecond / 1000.0)
    return utc_timestamp


def datetime_to_str_time(datetime_obj):
    """
        将 datetime 格式的时间 (含毫秒) 转为字符串格式
        :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
        :return: {str}'2016-02-25 20:21:04.242'
    """
    local_str_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    return local_str_time


def str_time_to_datetime(str_time):
    """
        将字符串格式的时间 (含毫秒) 转为 datetime 格式
        :param str_time: {str}'2016-02-25 20:21:04.242'
        :return: {datetime}2016-02-25 20:21:04.242000
    """
    local_datetime = datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S.%f")
    return local_datetime


def utc_str_time_to_timestamp(utc_time_str):
    """
        将 utc 时间 (字符串格式) 转为 13 位的时间戳
        :param utc_time_str: {str}'2016-02-25 20:21:04.242'
        :return: 1456431664242
    """
    # 先将字符串的格式转为 datetime 格式
    utc_datetime = str_time_to_datetime(utc_time_str)
    # 再将 datetime 格式的时间转为时间戳
    timestamp = utc_datetime_to_timestamp(utc_datetime)
    return timestamp


def utc_current_datetime():
    """
        返回 utc 当前时间, datetime 格式, 字符串格式, 时间戳格式
        :return: (datetime 格式, 字符串格式, 时间戳格式)
    """
    # utc 当前时间: datetime 格式
    utc_datetime_now = datetime.utcnow()

    # utc 当前时间: 字符串格式
    utc_str_time_now = datetime_to_str_time(utc_datetime_now)

    # utc 当前时间: 时间戳格式 13位整数
    utc_timestamp_now = utc_datetime_to_timestamp(utc_datetime_now)

    return utc_datetime_now, utc_str_time_now, utc_timestamp_now


if __name__ == '__main__':
    time_str = '2016-02-25 20:21:04.242'

    timestamp1 = utc_str_time_to_timestamp(time_str)
    datetime1 = str_time_to_datetime(time_str)
    time_str2 = datetime_to_str_time(datetime1)
    timestamp2 = utc_datetime_to_timestamp(datetime1)
    datetime3 = timestamp_to_utc_datetime(timestamp2)
    time_str3 = timestamp_to_utc_str_time(timestamp2)
    utc_current_time = utc_current_datetime()
    print('timestamp1: ', timestamp1)
    print('datetime1: ', datetime1)
    print('time_str2: ', time_str2)
    print('timestamp2: ', timestamp2)
    print('datetime3: ', datetime3)
    print('time_str3: ', time_str3)
    print('utc_current_time: ', utc_current_time)
    pass
