from flask import Flask
from app.config import config


def create_app(config_name):
    """
    通过此函数实现Flask对象的创建，在进行对象创建的同时还需要去考虑其他组件的初始化的处理问题
    本次的初始化操作组件包括：
    1. 一些程序的扩展支持
    2. 蓝图的加载
    3. 错误页面的配置
    4. 拦截器（钩子函数）的配置
    5. 自定义过滤器的使用
    6. CSRF校验保护
    :param config_name: 定义不同的启动模式
    :return: 可以直接使用的Flask对象
    """

    app = Flask(__name__)
    app.config.from_object(config.get(config_name) or "development")
    config.get(config_name).__init__(app)
    return app