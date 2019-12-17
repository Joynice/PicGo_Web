# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

import os

class config:
    DEBUG = True
    SECRET_KEY = 'HELLO WORLD'

    #github 配置
    GITHUB_USERNAME = 'Joynice'
    GITHUB_PASSWORD = 'liran123/'
    REPOSITORIES = 'image'  #仓库名
    BRANCH = 'master' #分支
    PATH = 'img' # 存储路径

    #sqlite配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///images.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #图片配置
    ALLOWED_PIC_EXTENSIONS = ('png', 'jpg', 'gif', 'jpeg', 'JPG', 'PNG', 'GIF', 'JPEG')
    ALLOWED_PIC_LEN = 10*1024