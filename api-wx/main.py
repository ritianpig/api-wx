# coding=utf-8
from flask import Flask
from app import creat_app

app = creat_app()

# 设置secret_key
app.secret_key = '123456'
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run()
