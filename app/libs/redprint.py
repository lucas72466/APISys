# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
@created_time : 28/11/2020 23:16
"""


class RedPrint:
    """
    用于蓝图与视图函数之间的注册媒介， 方便分离视图函数
    """
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))  # 先暂存到列表中， 当能够接触到blueprint时一起注册
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = f'/{self.name}'
        for f, rule, options in self.mound:
            endpoint = options.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
