# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         config.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------


import os
import redis as redis
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # HOST = "http://127.0.0.1:5000/"
    # HOST = "http://139.196.165.161:6851/"
    # HOST = "http://172.16.26.119:6851/"
    SCHEDULER_API_ENABLED = True
    JOBS = [
        {
            'id': 'ybj001',  # 任务唯一ID
            'func': 'uiplatform.services.scheduler:h5check_job',
            # 执行任务的function名称，app.test 就是 app下面的`test_check_web.py` 文件，`shishi` 是方法名称。文件模块和方法之间用冒号":"，而不是用英文的"."
            'args': '',  # 如果function需要参数，就在这里添加
            'trigger': 'interval',
            'seconds': 1800
        }
    ]
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = ''
    # flask_redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_URL = "redis://:305634841@127.0.0.1:6379/0"
    REDIS_DB = 0
    REDIS_PWD = 305634841
    REDIS_EXPIRE = 60
    # flask_session的配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=305634841)
    SESSION_USE_SIGNER = True  # 对cookies的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据有效期秒
    # 日志配置 ###############################################################
    LOG_PATH = os.path.join(basedir, "logs", "catch.log")
    LOG_FORMATTER = (
        "%(asctime)s [%(name)s] [%(thread)d:%(threadName)s] "
        "%(filename)s:%(module)s:%(funcName)s "
        "in %(lineno)d] "
        "[%(levelname)s]: %(message)s"
    )
    LOG_MAX_BYTES = 50 * 1024 * 1024  # 日志文件大小
    LOG_BACKUP_COUNT = 10  # 备份文件数量
    LOG_INTERVAL = 1
    LOG_WHEN = "D"

    # 设置邮件发送相关参数
    EMAIL_HOST = "smtp.163.com"
    EMAIL_USER = "13686821736@163.com"
    EMAIL_PORT = "25"
    # 邮箱授权码
    EMAIL_PASSWORD = "a305634841"
    EMAIL_SENDER = "13686821736@163.com"
    EMAIL_TITLE = "Interface Test Report"
    CREDENTIALS = (EMAIL_SENDER,EMAIL_PASSWORD)
    SUBJECT = '自动化的日志'
    # 收件人
    EMAIL_RECEIVER = "305634841@qq.com,2870550420@qq.com"
    # 缓存设置
    CACHE_TYPE = "redis"
    # 模板自动加载设置
    TEMPLATES_AUTO_RELOAD = True
    FLASK_ENV = "production"



    # 静态回调, 引入APP
    @staticmethod
    def init_app(app):
        #  环境参数 默认为production
        DEBUG = "development"
        PORT = 6851
        return


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_USE_TLS = True
    HOST = "http://127.0.0.1:5000/"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:xsdwadrcsefbjjbshjjd@139.196.165.161/flasken?charset=utf8"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置每次请求结束后会自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
    # 钉钉服务配置
    DINGURL = "https://oapi.dingtalk.com/robot/send?access_token=94365d973019b26147e61de5e1ef23ad86d5ce8a4f36e6c56a03b72c681c8705"
    DINGSIGN = "SEC4cf8edcdeb0cd0066b4f42e005585c833ec119c642b0c5bf2881d39a221d4940"
    # 钉钉服务配置
    DINGURL_CHECK = "https://oapi.dingtalk.com/robot/send?access_token=94365d973019b26147e61de5e1ef23ad86d5ce8a4f36e6c56a03b72c681c8705"
    DINGSIGN_CHECK = "SEC4cf8edcdeb0cd0066b4f42e005585c833ec119c642b0c5bf2881d39a221d4940"
    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')

class TestingConfig(Config):
    TESTING = True
    HOST = "http://139.196.165.161:6851/"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:xsdwadrcsefbjjbshjjd@139.196.165.161/flasken?charset=utf8"

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')

class ProductionConfig(Config):
    HOST = "http://172.16.26.119:6851/"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:xsdwadrcsefbjjbshjjd@139.196.165.161/erybjp?charset=utf8"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    # 设置每次请求结束后会自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 钉钉服务配置
    DINGURL = "https://oapi.dingtalk.com/robot/send?access_token=94365d973019b26147e61de5e1ef23ad86d5ce8a4f36e6c56a03b72c681c8705"
    DINGSIGN = "SEC4cf8edcdeb0cd0066b4f42e005585c833ec119c642b0c5bf2881d39a221d4940"
    # 钉钉服务配置
    DINGURL_CHECK = "https://oapi.dingtalk.com/robot/send?access_token=e8d376fc62d90de95d3905d9e4ad4f28b8c13cffdf0a36b82bcf6376e7a2f59a"
    DINGSIGN_CHECK = "SECe38026d8d3fa1d406842069effbd67d2ef0768409e2d89d2cb69bb48c3d86e59"

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


