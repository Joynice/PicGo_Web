# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from flask import (
    Blueprint,
    views,
    render_template,
    request
)
import os
from .models import Images
from utils import field
from utils.utils import *
from utils.GithubApi import GithubTools
from exts import db

front_bp = Blueprint('front', __name__, url_prefix='/')


class IndexView(views.MethodView):
    '''
    首页视图
    '''

    def get(self):
        images = Images.query.order_by(Images.create_time.desc()).all()
        context = {
            'images': images
        }
        return render_template('front/front_index.html', **context)

    def post(self):
        return field.params_error(message='不支持该方法')


class ImageView(views.MethodView):
    '''
    上传图片文件
    '''

    def get(self):
        return field.params_error(message='不支持该发方法')

    def post(self):
        file = request.files['file']
        filename = file.filename
        content = file.read()
        if not file:
            return field.params_error(message='未接收到文件')
        if not allowed_file(file.filename, ALLOWED_EXTENSIONS=config.ALLOWED_PIC_EXTENSIONS):
            return field.params_error(message='图片格式不合法')
        if not file_len(content):
            return field.params_error(message='图片大小超过{}M'.format(int(config.ALLOWED_PIC_LEN / 1024 / 1024)))
        new_name = rename(filename)
        if config.STORE_TYPE == 'github':  # github存储
            git = GithubTools()
            code, link = git.create_file('{}{}'.format(config.PATH, '/' + new_name), content)
            if code:
                image = Images(name=new_name, link=link, type='github')
                db.session.add(image)
                db.session.commit()
                return field.layui_success(message='上传成功,请拷贝链接使用', data={'link': link, 'id': image.id})
            else:
                return field.params_error(message=link)
        elif config.STORE_TYPE == 'server':  # 本地存储
            img = open(os.path.join(config.LOCAL_STORAGE_PATH ,new_name),'wb')
            img.write(content)
            img.close()
            link = request.url_root + 'static/images/' + new_name
            image = Images(name=new_name, link=link, type='server')
            db.session.add(image)
            db.session.commit()
            return field.layui_success(message='上传成功,请拷贝链接使用', data={'link': link, 'id': image.id})
        else:
            return field.params_error('配置文件中STORE_TYPE字段设置不正确')


class AboutView(views.MethodView):
    '''
    关于视图
    '''

    def get(self):
        pass

    def post(self):
        pass


class DeleteImageView(views.MethodView):
    '''
    删除图片
    '''

    def get(self):
        return field.params_error(message='不支持改方法')

    def post(self):
        id = request.form.get('id')
        if not id:
            return field.params_error(message='参数缺失')
        image = Images.query.get(id)
        if not image:
            return field.params_error(message='没有改图片')
        filename = image.name
        if image.type == 'github':
            git = GithubTools()
            code, message = git.delete_file('{}{}'.format(config.PATH, '/' + filename))
            db.session.delete(image)
            db.session.commit()
            return field.success(message=message)
        elif image.type == 'server':
            path = os.path.join(config.LOCAL_STORAGE_PATH ,filename)
            if os.path.exists(path):
                os.remove(path)
                db.session.delete(image)
                db.session.commit()
                return field.success(message='删除成功')
            else:
                return field.params_error(message='没有改图片')
        else:
            return field.params_error('配置文件中STORE_TYPE字段设置不正确')


front_bp.add_url_rule('', view_func=IndexView.as_view('index'))
front_bp.add_url_rule('about/', view_func=AboutView.as_view('about'))
front_bp.add_url_rule('images/', view_func=ImageView.as_view('images'))
front_bp.add_url_rule('delete/', view_func=DeleteImageView.as_view('delete'))
