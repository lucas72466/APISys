# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error import APIException
from datetime import date


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise APIException()


class Flask(_Flask):
    json_encoder = JSONEncoder



