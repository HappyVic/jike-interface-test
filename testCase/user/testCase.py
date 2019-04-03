# -*- coding:utf-8 -*-
# !/usr/bin/python
import json
import unittest
import time
import paramunittest
from common.Log import MyLog
from common import commontest
from common import url
from common import configHttp
from common import jikeToken

login_xls = commontest.get_xls_case("userCase.xlsx", "login")
configHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(*login_xls)
class TestCase(unittest.TestCase):
    def setParameters(self, case_name, method, mobilePhoneNumber, areaCode, action, result, success):

        self.case_name = str(case_name)
        self.method = str(method)
        self.mobilePhoneNumber = str(mobilePhoneNumber)
        self.areaCode = str(areaCode)
        self.action = str(action)
        self.result = str(result)
        self.success = bool(success)
        self.response = None

    def setUp(self):
        """

        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def testCase(self):
        """
        test body
        :return:
        """
        # set url
        self.url = url.users_profile
        configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers()

        # set params
        params = {"username": self.username}
        configHttp.set_params(params)

        # set date
        data = json.dumps(
            {"mobilePhoneNumber": self.mobilePhoneNumber, "password": self.password, "reaCode": self.areaCode})
        configHttp.set_data(data)

        # test interface
        self.response = configHttp.get()

        # check result
        self.checkResult()

    def tearDown(self):
        time.sleep(1)
        self.log.build_case_line(self.case_name, str(self.response))
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        """
        检查测试结果
        :return:
        """
        self.info = self.response.json()  # 返回json数据
        commontest.show_return_msg(self.response)  # 显示返回消息

        if self.result == '1':
            self.assertEqual(self.info['user']['screenName'], self.screenName)
            self.assertEqual(self.response.status_code, 200)

        if self.result == '0':
            self.assertIsNotNone(self.info['user']['screenName'])
            self.assertEqual(self.response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
