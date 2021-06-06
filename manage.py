# --------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/06/06 11:26
# @project_name : 
# @author :	yuanbaojun
# ------------

from create_app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from extensions import db
from uiplatform.models.elemodel import UielementInfo,Uicaseinfo,Uiresultinfo
# from interface_platform.routes import app_user

app = create_app("development")
# app.register_blueprint(app_user, url_prefix='/user')
manager = Manager(app)
migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

"""终端运行1、 E:\Auto_test\EasyTestPujen>python3 manage.py db init
命令
2、 E:\Auto_test\EasyTestPujen>python3 manage.py db migrate --message "initial migration"
python3 manage.py db migrate --message "initial migration"
3、 E:\Auto_test\EasyTestPujen>python3 manage.py db upgrade

"""








