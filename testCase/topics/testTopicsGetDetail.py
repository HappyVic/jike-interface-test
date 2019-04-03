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
from common import getHeaders

login_xls = commontest.get_xls_case("detailCase.xlsx", "getDetail")
configHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(*login_xls)
class TopicsGetDetail(unittest.TestCase):
    def setParameters(self, case_name, method, topics_id, ref, result, topics_roles_dict):

        self.case_name = str(case_name)
        self.method = str(method)
        self.topics_id = topics_id
        self.ref = ref
        self.result = str(result)
        self.topics_roles_dict = eval(topics_roles_dict)
        self.response = None

    def setUp(self):
        """

        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def testTopicsGetDetail(self):
        """
        test body
        :return:
        """
        # set url
        self.url = url.topics_getDetail
        configHttp.set_url(self.url)

        # set headers
        getHeaders.login_refresh_token()
        configHttp.set_headers()

        # set params
        params = {"id": self.topics_id, "ref": self.ref}
        configHttp.set_params(params)

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

            self.assertDictEqual (self.info['data']['involvedUsers']['bulletin'], self.topics_roles_dict)
            self.assertEqual(self.response.status_code, 200)
            self.assertEqual(self.info['success'], True)

        # if self.result == '0':
        #     self.assertIsNotNone(self.info['user']['screenName'])
        #     self.assertEqual(self.response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
