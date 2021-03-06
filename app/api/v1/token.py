# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validatos.forms import ClientForm

api = RedPrint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {  # 区分不同的用户类型
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # Token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(
        identity['uid'],
        form.type.data,
        identity['scope'],
        expiration
    )
    t = {'token': token.decode('ascii')}
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
