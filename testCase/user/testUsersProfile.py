# -*- coding:utf-8 -*-
#!/usr/bin/python
import time
import unittest
import paramunittest
from common.Log import MyLog
from common import commontest
from common import configHttp as ConfigHttp

smscode_xls = commontest.get_xls_case("userCase.xlsx", "usersProfile")
configHttp = ConfigHttp.ConfigHttp()


@paramunittest.parametrized(*smscode_xls)
class TestUsersProfile(unittest.TestCase):
    def setParameters(self, case_name, method, username, screenName , result):

        self.case_name = str(case_name)
        self.method = str(method)
        self.response = None
        self.username = str(username)
        self.screenName = str(screenName)
        self.result = str(result)


    def setUp(self):
        """

        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def testUsersProfile(self):
        """
        test body
        :return:
        """
        # set url
        self.url = commontest.get_url_from_xml('usersProfile')
        configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers()

        # set params
        params = {"username": self.username}
        configHttp.set_params(params)

        # test interface
        self.response = configHttp.get()

        # check result
        self.checkResult()


    def tearDown(self):
        time.sleep(2)
        self.log.build_case_line(self.case_name, str(self.response))
        print("测试结束，输出log完结\n\n")


    def checkResult(self):
        """
        检查测试结果
        :return:
        """
        self.info = self.response.json()#返回json数据
        commontest.show_return_msg(self.response)#显示返回消息


        if self.result == '1':
            self.assertEqual(self.info['user']['screenName'], self.screenName)
            self.assertEqual(self.response.status_code,200)

        if self.result == '0':
            self.assertIsNotNone(self.info['user']['screenName'])
            self.assertEqual(self.response.status_code, 200)


if __name__ == "__main__":
    run = TestSms()