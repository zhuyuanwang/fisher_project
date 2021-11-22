# -*- coding: utf-8 -*-
# @Time : 2021/11/20 15:27
# @Author : CircleOne_
# 蓝图初始化

from flask import Blueprint

web = Blueprint('web', __package__)

from app.web import book