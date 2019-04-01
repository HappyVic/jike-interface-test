# -*- coding:utf-8 -*-
#!/usr/bin/python
import json
import unittest
import time
import paramunittest
from common import commontest
from common import configHttp as ConfigHttp

smscode_xls = commontest.get_xls("userCase.xlsx", "smscode")
configHttp = ConfigHttp.ConfigHttp()


@paramunittest.parametrized(*smscode_xls)
class TestSms(unittest.TestCase):
    def setParameters(self, case_name, method, mobilePhoneNumber, areaCode, action, result, success):

        self.case_name = str(case_name)
        self.method = str(method)
        self.response = None
        self.areaCode = str(areaCode)
        self.result = str(result)
        self.mobilePhoneNumber = str(mobilePhoneNumber)
        self.action = str(action)
        self.success = bool(success)

    def setUp(self):
        """

        :return:
        """
        print("开始测试用例"+self.case_name)
        print(self.success)

    def testSmsCode(self):
        """
        test body
        :return:
        """
        # set url
        print("---------"+self.result)


    def tearDown(self):
        print("测试结束，输出log完结\n\n")






if __name__ == "__main__":
    run = TestSms()