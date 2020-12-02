# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    #  捕获全局异常， 统一以自定义异常对象返回
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config['DEBUG']:
            return APIException()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True)
