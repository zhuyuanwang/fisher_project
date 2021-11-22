# -*- coding: utf-8 -*-
# @Time : 2021/11/20 15:11
# @Author : CircleOne_
# 启动文件

import json

from app import create_app

app = create_app()

@app.route('/hello/<name>/')
def hello(name):
    result = 'hello {name}'.format(name=name)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)