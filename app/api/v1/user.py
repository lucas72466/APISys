# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
@created_time : 28/11/2020 23:05
"""
from app.libs.redprint import RedPrint

api = RedPrint('user')


@api.route('/get')
def get_user():
    return 'lucas'

@api.route('/create')
def create_user():
    pass
