# coding=utf8
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True,)
    url = db.Column(db.String(200))
    title = db.Column(db.String(100),unique=False)
    author = db.Column(db.String(30),unique=False)
    article = db.Column(db.TEXT,unique=False)
    time = db.Column(db.DateTime)
# 转json
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


