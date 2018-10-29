#coding=utf8

from flask import Flask
from models import db,migrate
from views import admin

# 初始化app
def creat_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    admin.init_app(app)
    migrate.init_app(app,db)
    return app

# 注册蓝图
def register_blueprint(app):
    from .web import web
    app.register_blueprint(web)
