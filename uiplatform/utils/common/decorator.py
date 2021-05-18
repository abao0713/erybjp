# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         decorator.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/17
#----------------------------


# 实现单例模式的装饰器
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

import hashlib
sha1 = hashlib.sha1()
data = 'hello world'
sha1.update(data.encode('utf-8'))
sha1_data = sha1.hexdigest()
print(len(sha1_data))
print(sha1_data)
