# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

from config import config
import datetime, time
from shortuuid import uuid

# 判断文件后缀是否在列表中
def allowed_file(filename, ALLOWED_EXTENSIONS=config.ALLOWED_PIC_EXTENSIONS):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def now_time(type='file'):
    '''
    获取现在的时间：时间格式为了让文件夹好命名使用（2019-10-10-10-10-10）的形式
    :type: file -->（2019-10-10-10-10-10）
    :type: str -->（1575878232）
    :return:
    '''
    if type == 'file':
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-')
        return nowtime
    if type == 'str':
        nowtime = str(int(time.time()))
        return nowtime

def rename(name):
    '''
    重构名字的格式
    保存的文件的命名为：时间（2019-10-20-10-10-45）+名字
    :param name:
    :return:
    '''
    name1 = name.split('.')[-1]
    new_name = uuid() +  '.' +name1

    return new_name

def file_len(filename_context):
    '''
    判断文件大小是否满足配置
    :param filename:文件内容
    :return: bool
    '''
    size = len(filename_context)
    if size > config.ALLOWED_PIC_LEN:
        return False
    else:
        return True