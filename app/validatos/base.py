# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException


class BaseForm(Form):

    def __init__(self):
        data = request.get_json(silent=True)  # 在初始化函数中获取data， 在调用时就无需显示传入; silent保持静默， 不抛异常
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        # 改写validate方法， 手动抛出自定义异常
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self  # 如此可以链式调用， 参考函数式编程
