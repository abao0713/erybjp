# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         comsrc.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/20
#----------------------------
from flask import jsonify

from uiplatform.models.elemodel import UielementInfo
from serialization import model_to_dict
from qiniu import Auth,put_file
import os,traceback
from os.path import dirname
from uiplatform.utils.common.BaseLoggers import logger
from config import Config,basedir


png_path = os.path.join(basedir,r"uiplatform\utils","data",'picture')

logger.info(f"最原始的图片路径:{png_path}")
if not os.path.exists(png_path):
    os.makedirs(png_path)

#获取Access Key和Secret Key后，进行初始化对接：
q = Auth(access_key="njsuxJI2hz72OgiynZhb1a6mvxZbhKk26Vq78BDv",
         secret_key="uOLJ0gDJEsSrYXIZiirFqRax74MVKPSuAHfr--XX")

class  UploadPicture:
    '''上传图片到七牛空间'''
    def  __init__(self,bucket_name = Config.QINIU_BACKET_NAME,*,host=Config.QINIU_HOST):
        self.host = host
        self.bucket_name = bucket_name

    def __get_token(self,picname):
        try:
            token = q.upload_token(bucket=self.bucket_name,key=picname)  #bukcet为七牛空间名，key为上传后的文件名
            logger.info(f"获取token为:{token}")
            return token
        except Exception as e:
            logger.critical(f"获取token失败，接口报错\n{traceback.format_exc()}")

    def  __delete_png(self,picname):
        '''上传成功之后，删除本地的图片'''
        png = os.path.join(png_path, picname)
        if os.path.exists(png):
            os.remove(png)
            logger.critical(f'删除图片:{picname}成功')
            return {"message":"图片删除成功"}
        else:
            logger.critical("删除图片失败,图片不存在")

    def upload_one_picture(self,picname):
        '''上传一个图片'''
        try:
            if isinstance(picname,str):
                picname = picname.strip()
                png = os.path.join(png_path,picname)
                logger.info(f"上传文件的路径:{png}")
                if os.path.exists(png):
                    token = self.__get_token(picname)
                    ret,info = put_file(token,picname,png)
                    logger.info("图片的路径"+ret.get("key"))
                    imagine_file = f"http://{self.host}/{ret.get('key')}"
                    logger.info(f'上传成功，图片地址为{imagine_file}')
                    self.__delete_png(picname)
                    return imagine_file
                else:
                     logger.critical('上传的文件不存在')
                     return {"message":"上传的文件不存在,请上传正确的文件"}
            elif isinstance(picname,list):
                logger.critical('上传的图片为列表')
                return {"message": "请上传图片类型为字符串,有且只能上传一个"}
            else:
                logger.critical('上传的图片非列表')
                return {"message": "请上传图片类型为字符串"}
        except Exception as e:
              error = traceback.format_exc()
              logger.critical(f"七彩云上传接口报错:\n{error}")
              return {"message":f"七彩云上传接口报错:\n{error}"}



def get_element_info(parent_id):
    element_db = UielementInfo.query.filter(UielementInfo.parent_id == parent_id, UielementInfo.type == "selenium").order_by(UielementInfo.index).all()
    json_data = model_to_dict(element_db)
    return json_data







