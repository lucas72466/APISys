# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""


class BaseScope:
    allow_api = set()
    allow_module = set()
    forbidden = set()

    def __add__(self, other):
        self.allow_api |= other.allow_api
        self.allow_module |= other.allow_module
        self.forbidden |= other.forbidden
        return self


class AdminScope(BaseScope):
    allow_api = set()
    allow_module = {'v1.user'}


class UserScope(BaseScope):
    forbidden = {'v1.super_get_user'}

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    module_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    elif module_name in scope.allow_module:
        return True
    else:
        return False
