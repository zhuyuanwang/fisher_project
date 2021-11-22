# -*- coding: utf-8 -*-
# @Time : 2021/11/20 15:24
# @Author : CircleOne_
# 应用初始化

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['JSON_AS_ASCII'] = False
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)

