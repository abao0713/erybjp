# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         extensions.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------


from uiplatform import create_app
app = create_app(config_name='development')
from uiplatform.extensions import db
db.create_all()
url_map = app.url_map
print(url_map)

