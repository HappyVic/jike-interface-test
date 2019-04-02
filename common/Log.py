import os
import readConfig as readConfig
import logging
from datetime import datetime
import threading

localReadConfig = readConfig.ReadConfig()


class Log:
    logging.basicConfig()
    def __init__(self):
        global logPath, resultPath, path
        path = readConfig.ProDir
        resultPath = os.path.join(path, "result")

        if not os.path.exists(resultPath):#判断该文件是否存在
            os.mkdir(resultPath)#创建目录

        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        self.logger = logging.getLogger()#获得一个logger对象，默认是root
        self.logger.setLevel(logging.INFO)#设定INFO级别，所有等级大于等于INFO的信息都会输出

        # 定义handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))#向文件output.log输出日志信息
        # 定义格式
        formatter = logging.Formatter('%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s')#定义日志输出格式
        handler.setFormatter(formatter)#选择一个格式

        self.logger.addHandler(handler)#增加指定的handler

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):#开始
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):#结束
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code):#用例
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name+" - Code:"+code)

    def get_report_file_path(self):#获取报告路径
        """
        get report file path
        :return:
        """
        report_file_path = os.path.join(logPath, "report.html")#报告路径
        return report_file_path

    def get_result_folder_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        logs_file_path = os.path.join(logPath, "output.log")
        fb = open(logs_file_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()#多线程

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()# 获取互斥锁后，进程只能在释放锁后下个进程才能进来
            MyLog.log = Log()
            MyLog.mutex.release()# 互斥锁必须被释放掉

        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")


