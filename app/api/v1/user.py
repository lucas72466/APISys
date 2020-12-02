# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.user import User

api = RedPrint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)

