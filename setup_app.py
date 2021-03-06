# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         extensions.py
# Description:
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------


from create_app import create_app
app = create_app()
from extensions import db
from uiplatform.models.elemodel import UielementInfo,Uicaseinfo,Uiresultinfo
db.create_all()
url_map = app.url_map
print(url_map)


if __name__ == '__main__':
    app.run(port=6851)
