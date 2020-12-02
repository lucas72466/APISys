# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from flask import Blueprint
from app.api.v1 import user, book, client, token


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)  # v1模块的蓝图， 注册各个子红图后注册到app

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)

    return bp_v1