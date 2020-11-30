# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from flask import request

from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validatos.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum

api = RedPrint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {  # 使用字典映射来起到switch的作用， 根据注册类型的不同选择对应的方法
        ClientTypeEnum.USER_EMAIL: __register_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_by_email():
    form = UserEmailForm().validate_for_api()
    if form.validate():
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)
