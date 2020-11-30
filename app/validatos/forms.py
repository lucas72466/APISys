# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validatos.base import BaseForm


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(message='can not be empty'), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(
        validators=[
            Email(message='invalidate email')
        ])

    secret = StringField(
        validators=[
            DataRequired(),
            # 密码仅能包含字母数字和"_"
            Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
        ])

    nickname = StringField(
        validators=[
            DataRequired(),
            length(min=2, max=22)
        ])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()






