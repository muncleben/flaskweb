#coding: UTF-8
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config():
    SECRET_KEY = "www.bpshare.com-%s" % os.urandom(24)
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR, 'static/upload')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass
config = {
    "development": DevelopmentConfig,
    # "test": TestConfig,
    # "Production": ProductionConfig,
}