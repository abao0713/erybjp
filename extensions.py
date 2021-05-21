# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         extensions.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------


# from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from flask_mail import Mail
# from flask_ckeditor import CKEditor
# from flask_moment import Moment
# from flask_bcrypt import Bcrypt
# from flask_caching import Cache
from flask_cors import CORS
from flask_apscheduler import APScheduler
scheduler = APScheduler()
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# bcrypt = Bcrypt()
# cache = Cache()
cors = CORS()
# debug_toolbar = DebugToolbarExtension()
# serialize = Marshmallow()
# bootstrap = Bootstrap()
# moment = Moment()
# ckeditor = CKEditor()
#mail = Mail()
db = SQLAlchemy()
