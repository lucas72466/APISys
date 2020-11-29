# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
@created_time : 28/11/2020 23:05
"""
from app.libs.redprint import RedPrint

api = RedPrint('book')


@api.route('', methods=['GET'])
def get_book():
    return 'book'
