# coding=utf-8
from models import db, Articles
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

class admin_view(ModelView):
    column_labels = dict(
        url = u'网址',
	title = u'标题',
	author = u'来源',
	article = u'正文',
	time = u'时间'	
    )


admin = Admin(name='后台管理')

admin.add_view(admin_view(Articles,db.session,name='文章'))
