# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from flask import (
    Blueprint,
    views,
    render_template,
    request
)
from .models import Images
from utils import field
from utils.utils import *
from werkzeug.utils import secure_filename
front_bp = Blueprint('front', __name__, url_prefix='/')


class IndexView(views.MethodView):
    '''
    首页视图
    '''
    def get(self):
        images = Images.query.all()
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
        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS=config.ALLOWED_PIC_EXTENSIONS):
            filename = secure_filename(file.filename)
            new_name = rename(filename)

class AboutView(views.MethodView):

    '''
    关于视图
    '''
    def get(self):
        pass

    def post(self):
        pass

front_bp.add_url_rule('', view_func=IndexView.as_view('index'))
front_bp.add_url_rule('about/', view_func=AboutView.as_view('about'))
front_bp.add_url_rule('image/', view_func=ImageView.as_view('image'))