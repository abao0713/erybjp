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
    # HOST = "http://127.0.0.1:6851/"
    # HOST = "http://139.196.165.161:6851/"
    HOST = "http://172.16.26.119:6851/"
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




    # 静态回调, 引入APP
    @staticmethod
    def init_app(app):
        #  环境参数 默认为production
        ENV = "production"
        DEBUG = "development"
        PORT = 5000
        return


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_USE_TLS = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:xsdwadrcsefbjjbshjjd@139.196.165.161/flasken?charset=utf8"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:305634841@127.0.0.1/flasken?charset=utf8"

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://TestDep:4Ehp1ndpfnlN9D0qvg4SZuig@rm-bp15t47j196je1u0l906.mysql.rds.aliyuncs.com/erybjp?charset=utf8"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    @classmethod
    def init_app(cls, app):
        print('>>>>>Two: This app has update')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


