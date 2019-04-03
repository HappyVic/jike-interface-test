import os
import unittest
from common.Log import MyLog as Log
import readConfig as readConfig
from common import HTMLTestRunner
from common.configEmail import MyEmail

localReadConfig = readConfig.ReadConfig()


class AllTest:
    def __init__(self):
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_file_path()
        on_off = localReadConfig.get_email("on_off")
        self.caseListFile = os.path.join(readConfig.ProDir, "caseList.txt")
        self.caseFile = os.path.join(readConfig.ProDir, "testCase")
        self.caseList = []
        self.email = MyEmail.get_email()

    def set_case_list(self):
        """
        set case list
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name + ".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("================================== 测试开始 ==================================")
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='即刻接口测试报告', description='用例执行情况')
                runner.run(suit)
                fp.close()

            else:
                logger.info("没有需要测试的案例")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            # 通过电子邮件发送测试报告
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                logger.info("不向开发人员发送报告电子邮件")
            else:
                logger.info("未知状态")

            logger.info("================================== 测试结束 ==================================")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
