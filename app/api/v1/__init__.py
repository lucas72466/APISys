# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
@created_time : 28/11/2020 23:05
"""
from flask import Blueprint
from app.api.v1 import user, book


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)  # v1模块的蓝图， 注册各个子红图后注册到app

    user.api.register(bp_v1)
    book.api.register(bp_v1)

    return bp_v1