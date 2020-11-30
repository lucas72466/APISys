# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""

from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    msg = 'client type is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0
