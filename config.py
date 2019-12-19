# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

import os

class config:
    DEBUG = True
    SECRET_KEY = 'HELLO WORLD'

    #存储地点：
    # 1. 当前服务器作作为图床:server,
    # 2. github作为图床:github
    STORE_TYPE = 'github'

    #github 配置
    GITHUB_USERNAME = 'xxx'
    GITHUB_PASSWORD = 'xxx'
    REPOSITORIES = 'xxx'  #需要提前创建，仓库名
    BRANCH = 'master' #分支
    PATH = 'xxx' # 存储路径

    # server 配置
    LOCAL_STORAGE_PATH = os.path.join(os.getcwd(),'static','images') #默认存储到项目static/images文件夹下

    #sqlite配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///images.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #图片配置
    ALLOWED_PIC_EXTENSIONS = ('png', 'jpg', 'gif', 'jpeg', 'JPG', 'PNG', 'GIF', 'JPEG')
    ALLOWED_PIC_LEN = 10*1024*1024