# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

from config import config
import datetime, time

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
    name = name.replace('/', '-').replace(':', '-')
    new_name = now_time() + name
    return new_name