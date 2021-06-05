# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         scheduler.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/21
#----------------------------
import pytest
from extensions import scheduler



def h5check_job():
    pytest.main(["-n 4"])
