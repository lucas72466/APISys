# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
@created_time : 28/11/2020 22:51
"""
from app.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
