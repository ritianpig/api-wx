from flask import request, jsonify
from sqlalchemy import and_
from models import db,Articles
from . import web

@web.route('/getcontent',methods=["POST","GET"])
def get_wx():
    if request.method == "GET":
        page = request.args.get("page", type=int, default=1)
        if page:
            '''取出数据库最后一条信息'''
            last_ob = db.session.query(Articles).order_by(Articles.id.desc()).first()
            last_id = last_ob.id
            '''定义返回的参数列表'''
            contexts = []
            '''page 代表页码数'''
            results = db.session.query(Articles).order_by(Articles.id.desc()).filter(and_(
                 Articles.id >last_id-5*page,
                 Articles.id <=last_id-5*page+5)).all()
            for result in results:
                contexts.append(result.to_json())
            return jsonify(contexts)
    elif request.method =="POST":
        page = request.args.get("page", type=int, default=1)
        if page:
            '''取出数据库最后一条信息'''
            last_ob = db.session.query(Articles).order_by(Articles.id.desc()).first()
            last_id = last_ob.id
            '''定义返回的参数列表'''
            contexts = []
            '''page 代表页码数'''
            results = db.session.query(Articles).order_by(Articles.id.desc()).filter(and_(
                Articles.id > last_id - 5 * page,
                Articles.id <= last_id - 5 * page + 5)).all()
            for result in results:
                contexts.append(result.to_json())
            return jsonify(contexts)







