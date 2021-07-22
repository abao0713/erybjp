# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         BaseLoggers.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/6/8
#----------------------------


import os
from config import basedir
import logging
from datetime import datetime
import threading
import time



class Log(object):
    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''
        global logPath, resultPath, basedir
        resultPath = os.path.join(basedir, "logs")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M")))
        # if not os.path.exists(logPath):
        #     os.mkdir(logPath)

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(os.path.join(resultPath, "output.log"))
        fh.setLevel(logging.INFO)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name+"----msg:"+msg)

    def get_result_path(self):
        """
        get result file path
        :return:
        """
        path = os.path.join(basedir, "my_report")
        result_path = os.path.join(path, "my_report.html")
        return result_path

    def get_report_path(self):
        """
        get test report path
        :return:
        """
        return logPath

    def write_result(self, result):
        """
        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            pass


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log(logger):

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log(logger)
            MyLog.mutex.release()

        return MyLog.log


log = MyLog.get_log("logger")
logger = log.get_logger()


if __name__ == "__main__":
    log = MyLog.get_log("logger")
    Logger = log.get_logger()
    Logger.debug("test debug")
    Logger.info("test info")
    log.get_report_path()