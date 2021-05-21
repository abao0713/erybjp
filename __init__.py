# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         __init__.py.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/11
#----------------------------



import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import SMTPHandler
from flask import Flask
from config import config
from extensions import scheduler
# from interface_platform.extensions import bootstrap, db, moment, ckeditor, mail, loginManager
from extensions import cors, db
import os

def create_app(config_name = None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = Flask('erybjp', static_folder="uiplatform/utils/data")
    app.config.from_object(config[config_name])

    register_logging(app)  # 注册日志处理器
    register_extensions(app)  # 注册扩展（扩展初始化）
    register_blueprints(app)  # 注册蓝本
    register_commands(app)  # 注册自定义shell命令
    register_errors(app)  # 注册错误处理函数
    register_shell_context(app)  # 注册错误处理函数
    register_template_context(app)  # 注册模板上下文处理函数
    return app




def register_logging(app):
    app.config.setdefault("LOG_PATH", "application.log")

    log_formatter = "%(asctime)s [%(thread)d:%(threadName)s] %(filename)s:%(module)s:%(funcName)s in %(lineno)d] [%(levelname)s]: %(message)s"
    app.config.setdefault("LOG_FORMATTER", log_formatter)
    app.config.setdefault("LOG_MAX_BYTES", 50 * 1024 * 1024)
    app.config.setdefault("LOG_BACKUP_COUNT", 10)
    app.config.setdefault("LOG_INTERVAL", 1)
    app.config.setdefault("LOG_WHEN", "D")
    app.config.setdefault("LOG_LEVEL", "INFO")

    formatter = logging.Formatter(app.config["LOG_FORMATTER"])
    # 将日志输出到文件
    # 指定间隔时间自动生成文件的处理器
    # 实例化TimedRotatingFileHandler
    # interval是时间间隔，
    # backupCount是备份文件的个数，如果超过这个个数，就会自动删除
    # when是间隔的时间单位，单位有以下几种：
    # S 秒
    # M 分
    # H 小时、
    # D 天、
    # W 每星期（interval==0时代表星期一）
    # midnight 每天凌晨
    timed_rotating_file_handler = TimedRotatingFileHandler(
        filename=app.config["LOG_PATH"],
        interval=app.config["LOG_INTERVAL"],
        when=app.config["LOG_WHEN"],
        backupCount=app.config["LOG_BACKUP_COUNT"],
        encoding="utf-8",
    )

    timed_rotating_file_handler.setFormatter(formatter)  # 设置文件里写入的格式
    timed_rotating_file_handler.setLevel(app.config["LOG_LEVEL"])

    # StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(app.config["LOG_LEVEL"])

    # SMTPHandler
    mail_handler = SMTPHandler(
        mailhost=app.config["EMAIL_HOST"],
        credentials=app.config["CREDENTIALS"],
        fromaddr=app.config["EMAIL_RECEIVER"],
        toaddrs=app.config["EMAIL_RECEIVER"],
        subject=app.config["SUBJECT"],
    )
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(formatter)

    # 删除默认的handler
    # app.logger.removeHandler(default_handler)

    # 设置logger
    for logger in (
            app.logger,
            logging.getLogger("sqlalchemy"),
            logging.getLogger("werkzeug"),
    ):
        logger.addHandler(stream_handler)
        logger.addHandler(timed_rotating_file_handler)
        if os.getenv("FLASK_ENV") == "production":
            logger.addHandler(mail_handler)

    # set logger for elk
    # stash_handler = logstash.LogstashHandler(
    #     app.config.get('ELK_HOST'),
    #     app.config.get('ELK_PORT')
    # )
    # root_logger.addHandler(stashHandler)

def register_extensions(app):
    # bootstrap.init_app(app)
    db.app=app
    db.init_app(app=app)
    cors.init_app(app, resources=r'/*')
    scheduler.init_app(app)
    scheduler.start()
    # ckeditor.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)

def register_blueprints(app):
    from uiplatform.router.run_testcase import user
    app.register_blueprint(user, url_prefix = '/auth')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db = db)

def register_template_context(app):
    pass

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        # return render_template('errors/400.html'), 400
        pass
def register_commands(app):
    pass


