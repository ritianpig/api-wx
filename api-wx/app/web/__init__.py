from flask import Blueprint

# 初始化蓝图
web = Blueprint('web',__name__)

# 导入蓝图对象
from . import api

